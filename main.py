import datetime

class welcome:
    @staticmethod
    def greet():
        print("******WELCOME TO YOUR TO DO LIST******")

        name = input('Enter your name here:- ')
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print(f'Good Morning {name}')
        elif hour>=12 and hour<17:
            print(f'Good Afternoon {name}')
        else:
            print(f'Good Evening {name}')
    

class To_do_list:

    @staticmethod
    def Add_task():
        user_entry1 = input('Enter the task to do here:- ')

        with open("all_task.txt", "a") as f:
            f.write('\n'+user_entry1)
            
    def show_all_task():

        with open('all_task.txt') as f:
            if f=='':
                print('There are no tasks yet')
            else:
                for line in f:
                    print(f' task - {line}')
    
    def remove_a_task():
        entry = input('Enter the task you want to delete:- ')
        fn = 'all_task.txt'
        f = open(fn)
        output = []
        task_deleted = entry
        for line in f:
            if not line.startswith(task_deleted):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
    

    def add_task_to_comlete():

        user_input = input('Enter the task which you have completed:- ')
        fn = 'all_task.txt'
        f = open(fn)
        output = []
        task_deleted = user_input
        for line in f:
            if not line.startswith(task_deleted):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()

        with open('completed_task.txt', 'w') as e:
            e.write(user_input)
    
    def show_completed_task():

        with open('completed_task.txt') as a:
            value = a.read()
            print(f'Completed task - {value}')



try:
    if __name__ == "__main__":
        while True:
            welcome.greet()
            print('You have the following tasks to complete')
            To_do_list.show_all_task()

            lists = print('''All options
            1.Add Task
            2.remove task
            3.Add task to completed list
            4.Show completed tasks
            5.exit''')
            user_entry = int(input('Enter your Choise here:- '))

            if user_entry==1:
                To_do_list.Add_task()

            elif user_entry==2:
                To_do_list.remove_a_task()
            
            elif user_entry==3:
                To_do_list.add_task_to_comlete()

            elif user_entry==4:
                To_do_list.show_completed_task()
            
            elif user_entry==5:
                print('Thanks For Using This To Do List!!')
                exit()


except Exception as e:
    print('......')