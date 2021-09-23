

$(document).ready(function(){
    var schedule_week = ['18:00','18:15','18:30','18:45',
                     '19:00','19:15','19:30','19:45',
                     '20:00','20:15','20:30','20:45',
                     '21:00','21:15','21:30','21:45',
                     '22:00','22:15','22:30'];

    var schedule_sunday = ['12:30','12:45',
                       '13:00','13:15','13:30','13:45',
                       '14:00','14:15','14:30','14:45',
                       '15:00','15:15','15:30','15:45',
                       '16:00','16:15','16:30','16:45',
                       '17:00','17:15','17:30','17:45', 
                       '18:00','18:15','18:30','18:45',
                       '19:00','19:15','19:30','19:45',
                       '20:00','20:15','20:30'
                      ];
    var prev_dayNum;
    var schedule_used = schedule_week;
    function initTime(){
        $('#datetimepicker').datetimepicker(
            {
                disabledWeekDays:[0],
                step:15,
                allowTimes: schedule_used,
            }
        );
    }
    initTime();
});


 // Use the week schedule by default.

// Function to initialise the time picker input.

// On load time initialisation.


// Initialise the date input.
$('#date').datetimepicker({
  timepicker:false,
  format:'d/m/Y',

  // On change callback
  onChangeDateTime:function(dp,$input){

    var dateVal = $input.val();
    var timeVal = $('#time').val();
    //console.log(dateVal +" - "+ (timeVal||"No Time"));

    // Because of the d/m/Y format, have to process the date a bit to get the day number.
    val = dateVal.split("/");
    var dayNum = new Date(val[2]+"/"+val[1]+"/"+val[0]).getDay();
    //console.log("dayNum: "+dayNum);

    // if dayNum is zero (sunday), use sunday schedule... Else use the week schedule.
    schedule_used = (dayNum == 0) ? schedule_sunday : schedule_week;

    // If the dayNum changed.
    if( prev_dayNum != dayNum  ){
      console.log("Changed day!");
      // Re-initialise datetimepicker
      $('#time').datetimepicker("destroy");
      initTime();

      // If the actual time value is not in schedule.
      if($.inArray(timeVal,schedule_used) == -1){
        console.log("Wrong time!");
        // Clear the time value.
        $('#time').val("");
        // Focus the time input so it's obvious the user has to re-select a time.
        $('#time').focus();
      }
    }
    // Keep this dayNum in memory for the next time.
    prev_dayNum = dayNum;
  }
});