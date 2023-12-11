SELECT patient.name, patient.fname, doctor.name, doctor.fname, SUM(bill.amount)
FROM patient
INNER JOIN doctor
ON patient.dr_code = doctor.dr_code
INNER JOIN bill
ON patient.pat_id = bill.pat_id
WHERE bill.amount > 100
GROUP BY patient.pat_id;
