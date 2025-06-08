# SNMP MIB module (FORTIMAIL-TRAP-MIB-220) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fortinet_12356/FORTIMAIL-TRAP-MIB-220.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:36:31 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(fmlSysSerial,
 fmlTraps) = mibBuilder.importSymbols(
    "FORTIMAIL-MIB-220",
    "fmlSysSerial",
    "fmlTraps")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

fmlTrapCpuHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 101)
)
fmlTrapCpuHighThreshold.setObjects(
    ("FORTIMAIL-MIB-220", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapCpuHighThreshold.setStatus(
        "current"
    )

fmlTrapMemLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 102)
)
fmlTrapMemLowThreshold.setObjects(
    ("FORTIMAIL-MIB-220", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapMemLowThreshold.setStatus(
        "current"
    )

fmlTrapLogDiskHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 103)
)
fmlTrapLogDiskHighThreshold.setObjects(
    ("FORTIMAIL-MIB-220", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapLogDiskHighThreshold.setStatus(
        "current"
    )

fmlTrapMailDiskHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 104)
)
fmlTrapMailDiskHighThreshold.setObjects(
    ("FORTIMAIL-MIB-220", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapMailDiskHighThreshold.setStatus(
        "current"
    )

fmlTrapMailDeferredQueueHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 105)
)
fmlTrapMailDeferredQueueHighThreshold.setObjects(
    ("FORTIMAIL-MIB-220", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapMailDeferredQueueHighThreshold.setStatus(
        "current"
    )

fmlTrapAvThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 106)
)
fmlTrapAvThresholdEvent.setObjects(
    ("FORTIMAIL-MIB-220", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapAvThresholdEvent.setStatus(
        "current"
    )

fmlTrapSpamThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 107)
)
fmlTrapSpamThresholdEvent.setObjects(
    ("FORTIMAIL-MIB-220", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapSpamThresholdEvent.setStatus(
        "current"
    )

fmlTrapSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 201)
)
fmlTrapSystemEvent.setObjects(
      *(("FORTIMAIL-MIB-220", "fmlSysSerial"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlSysEventCode"))
)
if mibBuilder.loadTexts:
    fmlTrapSystemEvent.setStatus(
        "current"
    )

fmlTrapRAIDEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 202)
)
fmlTrapRAIDEvent.setObjects(
      *(("FORTIMAIL-MIB-220", "fmlSysSerial"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlRAIDCode"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlRAIDDevName"))
)
if mibBuilder.loadTexts:
    fmlTrapRAIDEvent.setStatus(
        "current"
    )

fmlTrapHAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 203)
)
fmlTrapHAEvent.setObjects(
      *(("FORTIMAIL-MIB-220", "fmlSysSerial"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlHAEventId"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlHAUnitIp"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlHAEventReason"))
)
if mibBuilder.loadTexts:
    fmlTrapHAEvent.setStatus(
        "current"
    )

fmlTrapArchiveEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 204)
)
fmlTrapArchiveEvent.setObjects(
      *(("FORTIMAIL-MIB-220", "fmlSysSerial"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlArchiveServerIp"),
        ("FORTIMAIL-TRAP-MIB-220", "fmlArchiveFilename"))
)
if mibBuilder.loadTexts:
    fmlTrapArchiveEvent.setStatus(
        "current"
    )

fmlTrapIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0, 301)
)
fmlTrapIpChange.setObjects(
      *(("FORTIMAIL-MIB-220", "fmlSysSerial"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    fmlTrapIpChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTIMAIL-TRAP-MIB-220",
    **{"fmlTrapCpuHighThreshold": fmlTrapCpuHighThreshold,
       "fmlTrapMemLowThreshold": fmlTrapMemLowThreshold,
       "fmlTrapLogDiskHighThreshold": fmlTrapLogDiskHighThreshold,
       "fmlTrapMailDiskHighThreshold": fmlTrapMailDiskHighThreshold,
       "fmlTrapMailDeferredQueueHighThreshold": fmlTrapMailDeferredQueueHighThreshold,
       "fmlTrapAvThresholdEvent": fmlTrapAvThresholdEvent,
       "fmlTrapSpamThresholdEvent": fmlTrapSpamThresholdEvent,
       "fmlTrapSystemEvent": fmlTrapSystemEvent,
       "fmlTrapRAIDEvent": fmlTrapRAIDEvent,
       "fmlTrapHAEvent": fmlTrapHAEvent,
       "fmlTrapArchiveEvent": fmlTrapArchiveEvent,
       "fmlTrapIpChange": fmlTrapIpChange}
)
