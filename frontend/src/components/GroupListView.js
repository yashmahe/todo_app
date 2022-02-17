import GroupItem from './Group'

export default function GroupView(props) {
    return (
        <div>
            <ul>
                
                {props.groupList.map(group => <GroupItem group={group} />)}
                
            </ul>
        </div>
    )
}