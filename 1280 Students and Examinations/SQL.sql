select st.student_id, st.student_name, sub.subject_name, isnull(e.attended_exams, 0) as 'attended_exams'
from 
	students st
		cross join
	subjects sub
		left join
	(select student_id, subject_name, count(subject_name) as 'attended_exams'
	from examinations
	group by student_id, subject_name) e
		on st.student_id = e.student_id and e.subject_name = sub.subject_name
order by st.student_id, sub.subject_name