-- Write your query below
select employee_id, 
case 
when (employee_id % 2 != 0) And name not like 'M%'
then salary else 0
End as bonus
from employees
order by employee_id; 