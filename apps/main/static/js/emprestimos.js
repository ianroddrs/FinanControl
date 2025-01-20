new ClipboardJS('#copy-code');
var copyCodeElement = document.getElementById('copy-code');
copyCodeElement.addEventListener('click', function () {
    copyCodeElement.innerHTML = 'Copiado';
    setTimeout(function () {
        copyCodeElement.innerHTML = 'Copiar código do QR Code';
    }, 1000);
});

var options = {
    series: [{
    name: 'Saldo Devedor',
    type: 'column',
    data: [700, 643, 500, 300, 250, 200, 180, 80, 45, 22, 10]
  }, {
    name: 'Juros',
    type: 'line',
    data: [300, 280, 220, 176, 110, 82, 64, 52, 20, 9, 1]
  }],
    chart: {
    height: 350,
    type: 'line',
    stacked: false,
  },
  colors: ['#FF1654', '#247BA0'],
  stroke: {
    width: [0, 2, 5],
    curve: 'smooth'
  },
  plotOptions: {
    bar: {
      columnWidth: '50%'
    }
  },
  
  fill: {
    opacity: [0.85, 0.25, 1],
    gradient: {
      inverseColors: false,
      shade: 'light',
      type: "vertical",
      opacityFrom: 0.85,
      opacityTo: 0.55,
      stops: [0, 100, 100, 100]
    }
  },
  labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003',
    '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'
  ],
  markers: {
    size: 0
  },
  xaxis: {
    type: 'datetime'
  },
  yaxis: {
    title: {
      text: 'Points',
    }
  },
  tooltip: {
    shared: true,
    intersect: false,
    y: {
      formatter: function (y) {
        if (typeof y !== "undefined") {
          return y.toFixed(0) + " points";
        }
        return y;
  
      }
    }
  }
  };

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

        
  var options2 = {
    series: [8250.00, 3564.00, 5421.36, 735.36],
    chart: {
    width: 500,
    type: 'pie',
  },
  colors: ['#FF1654', '#247BA0', '#70C1B3', '#B2DBBF'],
  labels: ['Valor Emprestado', 'Total Pago', 'Saldo Atual', 'Juros'],
  responsive: [{
    breakpoint: 480,
    options: {
      chart: {
        width: 200
      },
      legend: {
        position: 'bottom'
      }
    }
  }]
  };

  var chart2 = new ApexCharts(document.querySelector("#chart2"), options2);
  chart2.render();
