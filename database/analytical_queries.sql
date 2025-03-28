-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT reg_ans, 
       SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesas
FROM health_expenses
WHERE descricao = "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR"
  AND data BETWEEN '2024-07-01' AND '2024-09-30'  -- 3º trimestre de 2024
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;


-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT reg_ans, 
       SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesas
FROM health_expenses
WHERE descricao = "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR"
  AND YEAR(data) = 2024  -- ano de 2024
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;