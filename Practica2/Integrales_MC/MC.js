
function Integral_1(x) {
    return Math.sqrt((Math.pow(1-(Math.pow(x,2)),(3))),2)
}

function Integral_2(x) {
    return (Math.E)**(x+(x**2))
}

function Integral_3(x) {
    return (1 + x**2) ** 2
}

function Integral_4(x) {
    return 1/(Math.cos(x) + 2)
}

function Integral_5(x) {
    return Math.log(x)
}

function Aproximacion_Integral(numeros_aleatorios, rango, opc) {
    let sum = 0
    let ui = 0
    let a = parseInt(rango.a.value)
    let b = parseInt(rango.b.value)

    for(let i=0; i<numeros_aleatorios; i++) {
       
        switch(opc) {
            
            case 'F1':  
                        for(let i=0; i<numeros_aleatorios; i++){
                            ui = Math.random()
                            sum += Integral_1(ui*(b-a)+a)
                        }
                        break;
            
            case 'F2':  
                        for(let i=0; i<numeros_aleatorios; i++){
                            ui = Math.random()
                            sum += Integral_2(ui*(b-a)+a)
                        }
                        break;
        
            case 'F3':  
                        for(let i=0; i<numeros_aleatorios; i++){
                            ui = Math.random()
                            sum += Integral_3(ui*(b-a)+a)
                        }
                        break;

            case 'F4':
                        for(let i=0; i<numeros_aleatorios; i++){
                            ui = Math.random()
                            sum += Integral_4(ui*(b-a)+a)
                        }
                        break;
            
            case 'F5':
                        for(let i=0; i<numeros_aleatorios; i++)
                            ui = Math.random()
                            sum += Integral_5(ui*(b-a)+a)
                        break;              
        }
    }   

    return ((b-a)/(numeros_aleatorios))*sum 
}



var simulacion = document.getElementById('simulacion').addEventListener('click', () => {
    
    var integral_opc = document.getElementById('Integrales')

    var rango = {
        a: document.getElementById('a'),
        b: document.getElementById('b') 
    } 

    var numeros_aleatorios = document.getElementById('numeros_aleatorios')

    var ctx = document.getElementById('myChart').getContext('2d')
    var arreglo_x = []
    var arreglo_y = []


    document.getElementById('Resultado').innerHTML = Aproximacion_Integral(numeros_aleatorios.value, rango, integral_opc.value)



    switch(integral_opc.value) {
        
        case 'F1':  

                    for(let i=0; i<1; i+=0.01)
                        arreglo_x.push(i)
                
                    for(let i=0; i<1; i+=0.01)
                        arreglo_y.push(Integral_1(i))
                    break;
        
        case 'F2':
                    for(let i=-2.6; i<1.7; i+=0.01)
                        arreglo_x.push(i)
                    
                    for(let i=-2.6; i<1.7; i+=0.01)
                        arreglo_y.push(Integral_2(i))
                    break;
        
        case 'F3':
                    for(let i=-3; i<3; i+=0.01)
                    arreglo_x.push(i)
                
                    for(let i=-3; i<3; i+=0.01)
                        arreglo_y.push(Integral_3(i))
                    break;  
        
        case 'F4':
                    for(let i=-23; i<23; i+=0.01)
                    arreglo_x.push(i)
                
                    for(let i=-23; i<23; i+=0.01)
                        arreglo_y.push(Integral_4(i))
                    break;

        case 'F5':

                    for(let i=0.1; i<23; i+=0.01)
                    arreglo_x.push(i)
                
                    for(let i=0.1; i<23; i+=0.01)
                        arreglo_y.push(Integral_5(i))
                    break;        

    }

    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: arreglo_x,
            datasets: [{
                label: 'Aproximación de la Integral',
                data: arreglo_y
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })    

})
