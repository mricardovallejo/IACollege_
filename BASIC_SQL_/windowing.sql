-- WINDOWING ---
--https://e-mc2.net/es/funciones-ventana-window-functions

SELECT 
  empid,
  departamento,
  salario,
  edad 
FROM empleado;


SELECT
  empid,
  departamento,
  salario,
  edad,
  avg(salario) OVER (PARTITION BY departamento) AS salario_medio 
FROM empleado ;

SELECT
  empid,
  departamento,
  salario,
  edad,
  avg(salario) OVER ventana_departamento AS salario_medio 
FROM empleado 
WINDOW 
  ventana_departamento AS (PARTITION BY departamento);
  
SELECT 
  empid,
  departamento,
  salario,
  edad,
  round(avg(salario) OVER ventana_departamento) AS sal_medio, 
  round(avg(edad) OVER ventana_departamento) AS ed_media 
FROM empleado 
WINDOW 
  ventana_departamento AS (PARTITION BY departamento);
  
  
SELECT 
  empid,
  departamento,
  salario,
  edad,
  salario - round(avg(salario) OVER ventana_departamento) AS sal_diff, 
  edad - round(avg(edad) OVER ventana_departamento) AS ed_diff 
FROM empleado 
WINDOW 
  ventana_departamento AS (PARTITION BY departamento);
  
  
--Ahora vamos a hallar el salario medio y la edad media de toda la empresa, sin hacer distinción entre departamentos.
--Para ello definimos la cláusula WINDOW vacia. De esta manera la ventana definida es todo el resultado:

SELECT 
  empid,
  departamento,
  salario,
  edad,
  round(avg(salario) OVER ventana_empresa) AS sal_medio, 
  round(avg(edad) OVER ventana_empresa) AS ed_media 
FROM empleado 
WINDOW 

--Ahora vamos a poner un ejemplo con dos ventanas. Una la vamos a utilizar para hallar en que posición (ranking) se encuentra
--cada empleado por departamentos, en relación al salario que cobra, y la otra para hallar en que posición (ranking) se encuentra 
--cada empleado por departamentos, en relación a la edad que tiene. Utilizaremos la función dense_rank().

SELECT 
  empid,
  departamento,
  salario,
  edad,
  dense_rank() OVER ventana_departamento_salario AS sal_pos,
  dense_rank() OVER ventana_departamento_edad AS ed_pos
FROM empleado 
WINDOW
  ventana_departamento_salario AS 
  (PARTITION BY departamento ORDER BY salario DESC),
  ventana_departamento_edad AS 
  (PARTITION BY departamento ORDER BY edad DESC);
  ventana_empresa AS ();
  
--Y si solamente queremos, por ejemplo, los datos del departamento de producción?. 
--Podemos utilizar una cláusula WHERE para acotar el resultado.

SELECT 
  empid,
  departamento,
  salario,
  edad,
  dense_rank() OVER ventana_departamento_salario AS sal_pos,
  dense_rank() OVER ventana_departamento_edad AS ed_pos
FROM empleado
WHERE 
  departamento = 'produccion'
WINDOW
  ventana_departamento_salario AS 
  (PARTITION BY departamento ORDER BY salario DESC),
  ventana_departamento_edad AS 
  (PARTITION BY departamento ORDER BY edad DESC);
  
--La consulta equivalente para toda la empresa seria:

SELECT 
  empid,
  departamento,
  salario,
  edad,
  dense_rank() OVER ventana_empresa_salario AS sal_pos,
  dense_rank() OVER ventana_empresa_edad AS ed_pos
FROM empleado 
WINDOW
  ventana_empresa_salario AS (ORDER BY salario DESC),
  ventana_empresa_edad AS (ORDER BY edad  DESC);