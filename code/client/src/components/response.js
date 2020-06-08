import React from 'react'

const Response = ({ data }) => {
    return (
        <div>
            {data.map((element) => (
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">ID: {element.Id}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Message: {element.Message}</h6>
                    </div>
                </div>
            ))}
        </div>
    )
};

export default Response