    // Crear fecha mínima y máxima
    var minDate, maxDate;

    // Función de filtrado personalizada que buscará datos en la columna cuatro entre dos valores
    DataTable.ext.search.push(function (settings, data, dataIndex) {
        var min = minDate.val();
        var max = maxDate.val();
        var date= moment(data[5], 'D [de] MMMM [de] YYYY');

        if (
            (min === null && max === null) ||
            (min === null && date <= max) ||
            (min <= date && max === null) ||
            (min <= date && date <= max)
        ) {
            return true;
        }
        return false;
    });

    // Crear entradas de fecha
    minDate = new DateTime('#min', {
        format: 'D [de] MMMM [de] YYYY' // 'LL' indica el formato "1 de abril de 1995"
    });
    maxDate = new DateTime('#max', {
        format: 'D [de] MMMM [de] YYYY' // 'LL' indica el formato "1 de abril de 1995"
    });



    var table = $('#tabla-usuarios').DataTable({
        "responsive": true,
        "language": {
            "decimal": "",
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
            "infoFiltered": "(Filtrado de _MAX_ total entradas)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ Entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        },
        "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
    });
      
   
    // Refilter the table
$('#min, #max').on('change', function () {
    table.draw();
});