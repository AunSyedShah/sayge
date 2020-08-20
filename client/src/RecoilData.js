import React from 'react'
import { useRecoilValue } from 'recoil'
import { makeStyles } from '@material-ui/core/styles'
import Paper from '@material-ui/core/Paper'
import Table from '@material-ui/core/Table'
import TableBody from '@material-ui/core/TableBody'
import TableCell from '@material-ui/core/TableCell'
import TableContainer from '@material-ui/core/TableContainer'
import TableHead from '@material-ui/core/TableHead'
import TablePagination from '@material-ui/core/TablePagination'
import TableRow from '@material-ui/core/TableRow'
import { activeDate, theme } from './atoms'


const columns = [
  { id: 'atom', label: 'Recoil Atom' },
  { id: 'atomValue', label: 'Value' },
  { id: 'atomType', label: 'Type' },
]

const useStyles = makeStyles({
  root: {
    margin: '1rem',
    border: '3px solid red',
  },
  container: {
    maxHeight: 300,
  },
  store: {
    background: '#5955FF 0% 0% no-repeat padding-box',
    borderRadius: '6px',
  },
})

export default () => {
  const activeDateValue = useRecoilValue(activeDate)
  const activeTheme = useRecoilValue(theme)
  const data = [
    { atom: 'activeDate', atomValue: activeDateValue, atomType: typeof(activeDateValue) },
    { atom: 'activeTheme', atomValue: activeTheme, atomType: typeof(activeTheme) },
  ]
  const classes = useStyles()
  const [page, setPage] = React.useState(0)
  const [rowsPerPage, setRowsPerPage] = React.useState(10)

  const handleChangePage = (event, newPage) => {
    setPage(newPage)
  }

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value)
    setPage(0)
  }

  return (
    <Paper className={classes.root}>
      <TableContainer className={classes.container}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {data.map((row) => {
              return (
                <TableRow hover role="checkbox" tabIndex={-1} key={row.atom}>
                  {columns.map((column) => {
                    const value = row[column.id]
                    return (
                      <TableCell key={column.id} align={column.align}>
                        {column.format ? column.format(value) : value}
                      </TableCell>
                    )
                  })}
                </TableRow>
              )
            })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={data.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onChangePage={handleChangePage}
        onChangeRowsPerPage={handleChangeRowsPerPage}
      />
    </Paper>
  )
}
