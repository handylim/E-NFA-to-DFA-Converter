<!DOCTYPE html>
<html lang="en">
	<head>
		<title>E-NFA to DFA</title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/css/materialize.min.css">
		<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/js/materialize.min.js"></script>
	</head>
	<body>
		<?php $json = json_decode(file_get_contents("result.json")) ?>
		<div class="container">
			<h3 class="center-align">Determinant Finate Automata</h3>
			<div class="divider"></div>
			<div class="card horizontal">
				<table class="striped responsive-table">
					<thead>
						<tr>
							<th></th>
							<th>States</th>
							<?php foreach ($json->alphabet as $alphabet): ?>
								<th><?php echo $alphabet ?></th>
							<?php endforeach ?>
						</tr>
					</thead>
					<tbody>
						<?php foreach ($json->result as $state): ?>
							<tr>
								<td class="right-align" style="width: 1%; white-space: nowrap;">
									<?php
										if ($json->start_state === $state->from)
											echo '-> ';
										foreach ($json->final_state as $f_state)
											if ($f_state === $state->from)
												echo '* '
									?>
								</td>
								<td><?php echo $state->from ?></td>
								<?php foreach ($state->to as $to_state): ?>
									<td><?php echo $to_state ?></td>
								<?php endforeach ?>
							</tr>
						<?php endforeach ?>
					</tbody>
				</table>
			</div>
		</div>
	</body>
</html>
