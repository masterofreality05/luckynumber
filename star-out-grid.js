function starOutGrid(grid) {
    let rowAndColumn = 0

    for (let row of grid){
        //iterates through each row. 

        if(row.includes('*')){
            //if the row has a star we want to turn that row into [*  *  * ]
            //then when we find the index of star in each row also to star
            

            indexOfStar = row.indexOf('*')
            //the row which the star is present will be starred out
            grid[indexOfStar] = ['*','*','*']

            //now we have the index lets iterate through the grid again and change the indexed star of each row to star
            for (row of grid){
                row[indexOfStar] = '*'
            }
        }
 }

return grid
}
