"use client";

import { AlarmActivationToggleEvent, api } from "@/lib/api";
import { Box, Table, Title } from "@mantine/core";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";

export default function Events() {
  const { alarmId } = useParams();
  const [alarmEvents, setAlarmEvents] = useState<AlarmActivationToggleEvent[]>(
    []
  );

  useEffect(() => {
    if (alarmId.length) {
      api
        .getEventsByAlarmId(alarmId.toString())
        .then((events) => setAlarmEvents(events));
    }
  }, [alarmId]);

  const rows = alarmEvents.map((event) => (
    <Table.Tr key={event.id}>
      <Table.Td>{new Date(event.timestamp).toLocaleString()}</Table.Td>
      <Table.Td>{event.toggled_to ? "Armed" : "Disarmed"}</Table.Td>
    </Table.Tr>
  ));

  return (
    <Box>
      <Link href="/">Back to alarms</Link>
      <Title order={2}>Events</Title>

      <Table>
        <Table.Thead>
          <Table.Tr>
            <Table.Th>Timestamp</Table.Th>
            <Table.Th>Toggled To</Table.Th>
          </Table.Tr>
        </Table.Thead>
        <Table.Tbody>{rows}</Table.Tbody>
      </Table>
    </Box>
  );
}
