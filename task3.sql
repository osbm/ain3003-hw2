SELECT doctor.name, doctor.fname, patient.name, patient.fname
FROM doctor
INNER JOIN patient
ON doctor.dr_code = patient.dr_code;
