
var logic = function( currentDateTime ){
    
    if( currentDateTime.getDay()==6 ){
      this.setOptions({
        minTime:'08:00',
        maxTime:'13:00'
      });
    }else
      this.setOptions({
        minTime:'08:00',
        maxTime:'20:00'
      });
  };
  $('#datetimepicker').datetimepicker({
    minDate: '0',
    onChangeDateTime:logic,
    onShow:logic,
    disabledWeekDays:[0],
    step:30,
  });

