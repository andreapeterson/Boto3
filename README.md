# Boto3
Using Boto3 and Python to do tasks on AWS. Today, I finally dug into Boto3. I have used it slightly before running Lambda but this was my first time I began to really deep dive and understand it. I have buuilt my Pythin and AWS skills simultaneously but separetly these path few months, so today was really special to put both skills together with BOTO3 and automate tasks.

On ec2.py - I used EC2 as a client and launched an instance and printed its ID, waited 45 seconds for it to get into a running state, then stopped it and waited 30 seconds then restarted it. Finally, I terminated the instance and printed the IDs of all instances thata re terminated currently in your account. There are print statements throughout updating you of the progress in the terminal.

on EBS.py - I used the resource method for EC2 and filtered instances by tag and created a snapshot for instances who had that tag. Then, I set up a for loop to delete snapshots that were older than 14 days old. 

on ami.py - I mixed the client and resource methods as I realized they both have their strengths. I again filtered instances by their tag but this time took an ami for each. Then, this part is cool- I used the get_waiter() method. On my EC2.py, it was my first file so I had no idea this was a method but I basically just timed how long on average each step took then added a bit of extra time witht he time.sleep() method, you can see how unefficient this is. But, with the waiter method Python will wait until the resource is in the state you specify- so I coded to wait until the image was available, then my code would proceed and transfer the ami to another region. Awesome!
