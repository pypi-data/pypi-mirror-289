from sql_blocks.sql_blocks import *


Select.join_type = JoinType.LEFT
OrderBy.sort = SortType.DESC

def best_movies() -> SelectIN:
    return SelectIN(
        'Review r',  movie=[GroupBy, Distinct], rate=Having.avg(Where.gt(4.5))
    )

def detached_objects() -> tuple:
    def select_actor() -> Select:
        return Select('Actor a', cast=ForeignKey('Cast'),
            name=NamedField('actors_name'), age=Between(45, 69)
        )
    def select_cast() -> Select:
        return Select(
            Cast=Table('role'), id=PrimaryKey, movie=ForeignKey('Movie'),
        )
    def select_movie() -> Select:
        return Select('Movie m', title=Field,
            release_date=[OrderBy, Field], id=PrimaryKey,
            OR=Options(
                genre=Where.eq('Sci-Fi'), awards=Where.like('Oscar')
            ), director=[Where.like('Coppola'), Field, OrderBy]
        )
    return select_actor(), select_cast(), select_movie()

def query_reference() -> Select:
    return Select('Actor a', age=Between(45, 69),
        cast=Select(
            Cast=Table('role'), id=PrimaryKey,
            movie=Select(
                'Movie m', title=Field,
                release_date=[OrderBy, Field],
                id=[
                    SelectIN(
                        'Review r', movie=[GroupBy, Distinct],
                        rate=Having.avg(Where.gt(4.5))
                    ),
                    PrimaryKey
                ], OR=Options(
                    genre=Where.eq('Sci-Fi'), awards=Where.like('Oscar')
                )
            ) # --- Movie
        ), # ------- Cast
        name=NamedField('actors_name'),
    ) # ----------- Actor

SINGLE_CONDITION_GENRE = "( m.genre = 'Sci-Fi' OR m.awards LIKE '%Oscar%' )"
SUB_QUERIES_CONDITIONS = """
    m.genre NOT in (SELECT g.id from Genres g where g.name in ('sci-fi', 'horror', 'distopia'))
    AND (m.hashtag = '#cult' OR m.awards LIKE '%Oscar%')
    AND m.id IN (select DISTINCT r.movie FROM Review r GROUP BY r.movie HAVING Avg(r.rate) > 4.5)
"""

def single_text_to_objects(conditions: str=SINGLE_CONDITION_GENRE):
    return Select.parse(f'''
        SELECT
                cas.role,
                m.title,
                m.release_date,
                a.name as actors_name
        FROM
                Actor a
                LEFT JOIN Cast cas ON (a.cast = cas.id)
                LEFT JOIN Movie m ON (cas.movie = m.id)
        WHERE
                {conditions}
                AND a.age <= 69 AND a.age >= 45
        ORDER BY
                m.release_date DESC
    ''')

def many_texts_to_objects():
    ForeignKey.references = {
        ('Actor', 'Cast'): ('cast', 'id'),
        ('Cast', 'Movie'): ('movie', 'id'),
    }
    actor = Select.parse('''
        SELECT name as actors_name FROM Actor a
        WHERE a.age >= 45 AND a.age <= 69
    ''')[0]
    cast = Select.parse('SELECT role FROM Cast')[0]
    movie = Select.parse("""
        SELECT title, release_date FROM Movie m ORDER BY release_date DESC
        WHERE ( m.genre = 'Sci-Fi' OR m.awards LIKE '%Oscar%' ) GROUP BY director
    """)[0]
    return actor, cast, movie

def two_queries_same_table() -> Select:
    txt1 = """SELECT p.name, p.category
    ,p.price,p.promotional FROM product p
        where p.category in (6,14,29,35,78)
    AND p.Status = p.last_st ORDER BY p.EAN"""
    txt2 = """select stock_amount, EAN,Name       ,expiration_date
    from PRODUCT where price < 357.46 and status = Last_ST order by ean"""
    return Select.parse(txt1)[0] + Select.parse(txt2)[0]

def select_product() -> Select:
    return Select(
        Product=Table('name,promotional,stock_amount,expiration_date'),
        category=[Where.list([6,14,29,35,78]),Field], EAN=[Field, OrderBy],
        price=[Where.lt(357.46),Field], status=Where('= Last_st')
    )

def extract_subqueries() -> dict:
    query_list = single_text_to_objects(SUB_QUERIES_CONDITIONS)
    return {query.table_name: query for query in query_list}