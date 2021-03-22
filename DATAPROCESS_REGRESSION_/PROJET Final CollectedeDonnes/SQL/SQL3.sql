---3. SQL


----3.1. Charger le jeu de données « data_person_profiles.txt ».---

CREATE TABLE public.data_person_profiles
(
age integer,
work_class         varchar(50),
salary             integer,
education          varchar(50),
education_num      integer,
marital_status     varchar(50),
occupation         varchar(50),
relationship       varchar(50),
race               varchar(50),
gender             varchar(50),
capital_gain       integer,
capital_loss       integer,
hours_per_week     integer,
country            varchar(50),
target             varchar(50)

    
)

TABLESPACE pg_default;

ALTER TABLE public.data_person_profiles
    OWNER to postgres;



---3.2. Comparer le salaire d'un employé avec le salaire moyen des autres employés---

SELECT SALARY,
	(SELECT AVG(SALARY) FROM DATA_PERSON_PROFILES) AVG_SALARY 
FROM DATA_PERSON_PROFILES;


---3.3. Déterminer les rangs des employées par gros salaire ----   
SELECT *,
	--age, capital_gain, gender,salary, 
	RANK () OVER (ORDER BY salary desc) emp_rank 
FROM
	data_person_profiles;


---3.4. Détermine les 10 premiers rangs des employées par âge, capital-gain et sexe ---
--by age
SELECT 
	age, capital_gain, gender,salary,	RANK () OVER ( 
		ORDER BY age
	) emp_age
FROM
	data_person_profiles limit 10;
--	data_person_profiles order by salary limit 10;
	
--by capital_gain
SELECT 
	age, capital_gain, gender,salary,	RANK () OVER ( 
		ORDER BY capital_gain 
	) emp_capgain
FROM
	data_person_profiles limit 10;

--by gender
SELECT 
	age, capital_gain, gender, salary,	RANK () OVER ( 
		ORDER BY  gender 
	) emp_gender
FROM
	data_person_profiles limit 10;
	
	
	
---3.5. Déterminer la somme de la de perte en capitale (capital loss) par sexe, âge et éducation----
	
--first variant (partition by)
    select distinct  gender , sum(capital_loss)  over (partition by gender) capital_loss from data_person_profiles ;
    select distinct  age , sum(capital_loss)  over (partition by age) capital_loss from data_person_profiles ;
    select distinct  education , sum(capital_loss)  over (partition by education) capital_loss from data_person_profiles  ;

--second variant (group by)
	select  gender , sum(capital_loss) capital_loss from data_person_profiles group by gender order by capital_loss desc;;
    select  age , sum(capital_loss) capital_loss from data_person_profiles group by age order by capital_loss desc;;
	select  education , sum(capital_loss) capital_loss from data_person_profiles group by education order by capital_loss desc;

	