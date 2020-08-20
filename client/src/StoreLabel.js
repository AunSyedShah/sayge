import React from 'react'
import { makeStyles } from '@material-ui/core/styles'

const useStyles = makeStyles({
  label: {
    background: '#5955ff 0% 0% no-repeat padding-box',
    borderRadius: '6px',
    font: '13px/18px',
    color: '#FFFFFF',
    padding: '2px 10px',
  },
})

export default ({ label }) => {
  const classes = useStyles()

  return <span className={classes.label}>{label}</span>
}
