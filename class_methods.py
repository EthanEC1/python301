class Tiger:
    property = {
        'color': 'orange'
    }
    similar_animal_list = ['Lion', 'Cat', 'Leopard']

    def remove_name(self, name):
        self.similar_animal_list.remove(name)
        return self.similar_animal_list

the_animal = Tiger()
the_animal.remove_name('Leopard')
print(the_animal.similar_animal_list)