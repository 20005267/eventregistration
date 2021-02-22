# WebApplication for Event Registration

## AIM:
To create a UX design and develop a web application for event registration.
## DESIGN STEPS:

### Step 1: 
Requirement collection.
### Step 2:
Choosing the suitable color scheme
### Step 3:
Creating artboards for individual pages
### Step 4:
Designing layout for individual pages
### Step 5:
Creating links and linking it with artboards
### Step 6:
Preview the prototype.

## DESIGN SCREENS:

![output](./static/img/output1.jpg)

![output](./static/img/output2.jpg)

![output](./static/img/output3.jpg)

![output](./static/img/output4.jpg)

![output](./static/img/output5.jpg)


## WIREFRAME:

![output](./static/img/output6.jpg)

## PROTOTYPE:

![output](./static/img/output7.jpg)

## PROGRAM:

## HOME.HTML:
```
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Home!</title>
  </head>
  <body>
    <div class="jumbotron" style="background-color: pink;">
        <div style="background-color: purple;">
        <div class="container text-center">
  <h1 class="display-4">INTERNATIONAL ART CONTEST</h1>
  <hr class="my-4">
  <p class="lead">You are the artist</p>
</div>
</div>
<div class="container">
    <div class="row">
        <div class="col-12">
        <h4>OIL PAINTING</h4>
        <h4>ABSTRACT ART</h4>
        <h4>DESIGN ART</h4>
        <h4>MODERN ART</h4> 
        </div>
    </div>

</div>
<br>
<div class="row text-center">
    <div class="col-12">
        <h4>DATE: 05.03.2021</h4>
        <h4>TIME: 8.00AM - 5.00PM</h4>
        <h4>PLACE: Italy</h4>
        <h4>REGISTRATION FEES: 1000</h4>
    </div>
</div>
<div class="row text-center">
    <div class="col-12">
        <h4>CONTACT US</h4>
        <h4>E-Mail: workart023@gmail.com</h4>
        <h4>PH.NO: 044-562789267</h4>
    </div>
</div>
<div class="row">
    <div class="col-12 text-center"></div>
    <a href="/register/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Register</a>
</div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

## REGISTER.HTML
```
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Register Now!</title>
  </head>
  <body>
    <div class="jumbotron" style="background-color: pink;">
        <div style="background-color: purple;">
        <div class="container text-center">
  <h1 class="display-4">INTERNATIONAL ART CONTEST</h1>
  <hr class="my-4">
  <p class="lead">You are the artist</p>
</div>
</div>
<div class="container">
    <div class="row">
        <div class="col-12">
            <form action="/register/" method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="exampleFormControlInput1">Name</label>
                    <input type="name" class="form-control" id="name" name="name" placeholder="Ente your Name">
                </div>
                <div class="form-group">
                    <label for="exampleFormControlInput1">Email address</label>
                    <input type="email" class="form-control" id="emil" name="email" placeholder="Enter your E-mail">
                </div>
                <div class="form-group">
                    <label for="exampleFormControlInput1">Phone Number</label>
                    <input type="phonenumber" class="form-control" id="phonenumber" name="phonenumber" placeholder="Enter your Phonenumber">
                </div>
                <div class="form-group">
                    <label for="exampleFormControlInput1">Place</label>
                    <input type="place" class="form-control" id="place" name="place" placeholder="Enter your Place">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>      
</div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

## SUCCESS.HTML:
```

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Registration Successful!</title>
  </head>
  <body>
    <div class="jumbotron" style="background-color: pink;">
        <div style="background-color: purple;">
        <div class="container text-center">
            <h1 class="display-4">INTERNATIONAL ART CONTEST</h1>
            <hr class="my-4">
            <p class="lead">You are the artist</p>
        </div>
    </div>
    <div class="row">
        <div class="col-12 text-center text-success py-10">
            Your Registration has been successfully completed !
        </div>
    </div>
    <div class="row py-5">
            <div class="col-12 text-center">
                <a href="/home/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Home</a>
            </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

## FAILED.HTML:
```
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Registration Failed!</title>
  </head>
  <body>
      <div class="jumbotron">
        <div class="container text-center">
            <h1 class="display-4">INTERNATIONAL ART CONTEST</h1>
            <hr class="my-4">
            <p class="lead">You are the artist</p>
        </div>
    </div>
    <div class="row">
        <div class="col-12 text-center text-success py-10">
            Your Registration has been Failed !
        </div>
    </div>
    <div class="row py-5">
            <div class="col-12 text-center">
                <a href="/home/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Home</a>
            </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>
```
## PARTICIPANTS.HTML:
```

<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Contest Participants list</title>
</head>

<body>
    <div class="jumbotron" style="background-color: pink;">
        <div style="background-color: purple;">
        <div class="container text-center">
            <h1 class="display-4">INTERNATIONAL ART CONTEST</h1>
            <hr class="my-4">
            <p>You are the artist</p>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>PARTICIPANTS LIST</h1>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col">NAME</th>
                            <th scope="col">EMAIL</th>
                            <th scope="col">PHONE</th>
                            <th scope="col">PLACE</th>
                        </tr>
                    </thead>
                    <tbody>
                        
                        <tr>                          
                            <td>Abi</td>
                            <td>abi@gmail.com</td>
                            <td>2342424678</td>
                            <td>Chennai</td>
                        </tr>
                        
                        <tr>                          
                            <td>Aishu</td>
                            <td>aishu@gmail.com</td>
                            <td>2379045321</td>
                            <td>Delhi</td>
                        </tr>
                        
                        <tr>                          
                            <td>Lathika</td>
                            <td>sweety@gmail.com</td>
                            <td>9738612304</td>
                            <td>Mumbai</td>
                        </tr>
                        
                        <tr>                          
                            <td>Hari</td>
                            <td>hari@gmail.com</td>
                            <td>985357123</td>
                            <td>USA</td>
                        </tr>
                        
                        <tr>                          
                            <td>Amirtha</td>
                            <td>amir@gmail.com</td>
                            <td>2340926572</td>
                            <td>Paris</td>
                        </tr>
                        
                        <tr>                          
                            <td>vaishu</td>
                            <td>vaishu@gmail.c0m</td>
                            <td>26547893233</td>
                            <td>Europe</td>
                        </tr>
                        
                        <tr>                          
                            <td>Buffkey</td>
                            <td>buffkey@gmail.com</td>
                            <td>3498674091</td>
                            <td>Hyderabad</td>
                        </tr>
                        
                        <tr>                          
                            <td>Amrin</td>
                            <td>amrin@gmail.com</td>
                            <td>3561890847</td>
                            <td>Banglore</td>
                        </tr>
                        
                        <tr>                          
                            <td>Afro</td>
                            <td>afro@gmail.com</td>
                            <td>8930478299</td>
                            <td>London</td>
                        </tr>
                        
                        <tr>                          
                            <td>Keerthu</td>
                            <td>keerthu@gmail.com</td>
                            <td>378496271</td>
                            <td>Singapore</td>
                        </tr>
                        
                        <tr>                          
                            <td>Santho</td>
                            <td>santho@gmail.com</td>
                            <td>2456754323</td>
                            <td>Iran</td>
                        </tr>
                        
                        <tr>                          
                            <td>Sanju</td>
                            <td>sanju@gmail.com</td>
                            <td>9408309221</td>
                            <td>US</td>
                        </tr>
                        
                        <tr>                          
                            <td>Dolly</td>
                            <td>dolly@gmail.com</td>
                            <td>3629180291</td>
                            <td>France</td>
                        </tr>
                        
                        <tr>                          
                            <td>Carolin</td>
                            <td>carolin@gmail.com</td>
                            <td>9775789870</td>
                            <td>China</td>
                        </tr>
                                                
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col-12 text-center">
                <a href="/home/" class="btn btn-primary btn-lg" role="button" >Home</a>
            </div>
        </div>         
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
```

## OUTPUT:
![output](./static/img/output8.jpg)

![output](./static/img/output9.jpg)

![output](./static/img/output10.jpg)
)
![output](./static/img/output11.jpg)


## RESULT:
```
Thus a UX design is created and web application is developed for event registration and is hosted in the
 URL http://kayalvizhi.student.saveetha.in:8000/home.