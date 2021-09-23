var logic = function( currentDateTime ){
    // 'this' is jquery object datetimepicker
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


// $('#datetimepicker').datetimepicker({
//     minDate: '0',        
//     disabledWeekDays:[0],
//     onChangeDateTime: datePickerTime
// });




// $(document).ready(function(){
//     var schedule_week = ['08:00','08:30','09:00','09:30',
//                      '10:00','10:30','11:00','11:30',
//                      '12:00','12:30','13:00','13:30',
//                      '14:00','14:30','15:00','15:30',
//                      '16:00','16:30','17:00','17:30',
//                      '18:00','18:30','19:00','19:30',
//                      '20:00'];

//     var schedule_saturday = ['08:00','08:30','09:00','09:30',
//                             '10:00','10:30','11:00','11:30',
//                             '12:00','12:30','13:00'];

//     var prev_dayNum;
//     var schedule_used = schedule_week;
//     function initTime(){
//         $('#datetimepicker').datetimepicker(
//             {
//                 disabledWeekDays:[0],
//                 step:30,
//                 allowTimes: schedule_used,
//             }
//         );
//     }
//     initTime();
// });


//  // Use the week schedule by default.

// // Function to initialise the time picker input.

// // On load time initialisation.


// // Initialise the date input.
// $('#date').datetimepicker({
//   timepicker:false,
//   format:'d/m/Y',

//   // On change callback
//   onChangeDateTime:function(dp,$input){

//     var dateVal = $input.val();
//     var timeVal = $('#time').val();
//     //console.log(dateVal +" - "+ (timeVal||"No Time"));

//     // Because of the d/m/Y format, have to process the date a bit to get the day number.
//     val = dateVal.split("/");
//     var dayNum = new Date(val[2]+"/"+val[1]+"/"+val[0]).getDay();
//     //console.log("dayNum: "+dayNum);

//     // if dayNum is zero (sunday), use sunday schedule... Else use the week schedule.
//     schedule_used = (dayNum == 0) ? schedule_sunday : schedule_week;

//     // If the dayNum changed.
//     if( prev_dayNum != dayNum  ){
//       console.log("Changed day!");
//       // Re-initialise datetimepicker
//       $('#time').datetimepicker("destroy");
//       initTime();

//       // If the actual time value is not in schedule.
//       if($.inArray(timeVal,schedule_used) == -1){
//         console.log("Wrong time!");
//         // Clear the time value.
//         $('#time').val("");
//         // Focus the time input so it's obvious the user has to re-select a time.
//         $('#time').focus();
//       }
//     }
//     // Keep this dayNum in memory for the next time.
//     prev_dayNum = dayNum;
//   }
// });