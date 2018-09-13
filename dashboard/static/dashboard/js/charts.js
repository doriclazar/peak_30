function generate_default_data()
{
  var default_chart_data = {
    type: '',
    data: {
      labels: [],
      datasets: [
      ]
    },
    options: {
      responsive: false,
      cutoutPercentage:75 
    }
  }
  return default_chart_data;
}
function generate_chart(raw_data, DOM_id)
{
	var new_data = generate_default_data();
  	new_data['type'] = raw_data[0];
	new_data['data']['labels'] = raw_data[1];

	for (var dataset_count = 0; dataset_count<raw_data[2].length; dataset_count++)
	{
		new_data['data']['datasets'][dataset_count] = [];
		this_dataset = new_data['data']['datasets'][dataset_count]
		this_dataset['data'] = raw_data[2][dataset_count][0];
		this_dataset['backgroundColor'] = raw_data[2][dataset_count][1];
		this_dataset['hoverBackgroundColor'] = raw_data[2][dataset_count][2];
		this_dataset['borderColor'] = raw_data[2][dataset_count][3];
		this_dataset['label'] = raw_data[2][dataset_count][4];
	}
  	var new_DOM = document.getElementById(DOM_id).getContext('2d');
  	var new_chart = new Chart(new_DOM, new_data);
	return new_chart;
}

window.onload = function () 
{
  var task_completion_data = generate_chart(task_completion_raw, "task_completion");
  var time_consumption_chart = generate_chart(time_consumption_raw, "time_consumption");
  var bot_effectiveness_chart = generate_chart(bot_effectiveness_raw, "bot_effectiveness");
}
