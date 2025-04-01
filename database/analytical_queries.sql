-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT reg_ans, 
    SUM(COALESCE(vl_saldo_final, 0) - COALESCE(vl_saldo_inicial, 0)) AS total_despesas
FROM health_expenses
WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
AND data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;


-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT reg_ans, 
       SUM(COALESCE(vl_saldo_final, 0) - COALESCE(vl_saldo_inicial, 0)) AS total_despesas
FROM health_expenses
WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
  AND EXTRACT(YEAR FROM data) = 2024  -- Ano de 2024
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;