import React from 'react'
import clsx from 'clsx'
import { makeStyles } from '@material-ui/core/styles'
import Container from '@material-ui/core/Container'
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Admin from './Admin'

const useStyles = makeStyles((theme) => ({
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 240,
  },
}))

const ThemeOverview = () => {
  const classes = useStyles()
  const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight)

  return (
    <Container maxWidth="lg" className={classes.container}>
      <Grid container spacing={3}>

        <Grid item xs={12} md={8} lg={9}>
          <Paper className={fixedHeightPaper}>
            Theme Overview
          </Paper>
        </Grid>

        <Grid item xs={12} md={4} lg={3}>
          <Paper className={fixedHeightPaper}>
            Theme Overview
          </Paper>
        </Grid>

        <Grid item xs={12}>
          <Paper className={classes.paper}>
            Theme Overview
          </Paper>
        </Grid>

      </Grid>
    </Container>
  )
}

export default () => {
  return (
    <Admin component={ThemeOverview} />
  )
}
