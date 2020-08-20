import React from 'react'
import { Alert, AlertTitle } from '@material-ui/lab'
import { makeStyles } from '@material-ui/core/styles'
import Paper from '@material-ui/core/Paper'
import TextField from '@material-ui/core/TextField'
import { useRecoilState } from 'recoil'
import { activeDate } from './atoms'

const useStyles = makeStyles((theme) => ({
  paper: {
    margin: '2rem',
    width: '100%',
  },
  input: {
    margin: '1rem',
    padding: '1rem',
  }
}))


export default () => {
  const classes = useStyles()
  const [date, setDate] = useRecoilState(activeDate)

  return (
    <Paper className={classes.paper}>
      <Alert severity="warning">
        <AlertTitle>Temporary Date Picker</AlertTitle>
        This date picker uses native browser input which doesn't work in some browsers but it's here to enable date selection. <strong>It will be replaced soon.</strong>
      </Alert>

      <TextField
        id="date"
        className={classes.input}
        label="Date picker"
        type="date"
        defaultValue={date}
        InputLabelProps={{
          shrink: true,
        }}
        onChange={(event) => setDate(event.target.value) }
      />
    </Paper>
  )
}
