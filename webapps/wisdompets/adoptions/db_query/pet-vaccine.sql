select adoptions_pet.name, species, vaccine_id, adoptions_vaccine.name from adoptions_pet
inner join adoptions_pet_vaccination on adoptions_pet.id = adoptions_pet_vaccination.pet_id
inner join adoptions_vaccine on adoptions_pet_vaccination.vaccine_id = adoptions_vaccine.id
where adoptions_pet.name = 'Nadalee'