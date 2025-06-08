# SNMP MIB module (WAN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/WAN-TRAP-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:41:50 2025
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

(extremeAgent,
 extremenetworks) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent",
    "extremenetworks")

(dsx1IfIndex,
 dsx1LineIndex,
 dsx1LineStatus) = mibBuilder.importSymbols(
    "RFC1406-MIB",
    "dsx1IfIndex",
    "dsx1LineIndex",
    "dsx1LineStatus")

(dsx3IfIndex,
 dsx3LineIndex,
 dsx3LineStatus) = mibBuilder.importSymbols(
    "RFC1407-MIB",
    "dsx3IfIndex",
    "dsx3LineIndex",
    "dsx3LineStatus")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
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

wanDsx1LineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 100)
)
wanDsx1LineStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("RFC1406-MIB", "dsx1LineIndex"),
        ("RFC1406-MIB", "dsx1IfIndex"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    wanDsx1LineStatusChange.setStatus(
        ""
    )

wanDsx1LossOfMasterClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 101)
)
wanDsx1LossOfMasterClock.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("RFC1406-MIB", "dsx1LineIndex"),
        ("RFC1406-MIB", "dsx1IfIndex"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    wanDsx1LossOfMasterClock.setStatus(
        ""
    )

wanDsx1NoLossOfMasterClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 102)
)
wanDsx1NoLossOfMasterClock.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("RFC1406-MIB", "dsx1LineIndex"),
        ("RFC1406-MIB", "dsx1IfIndex"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    wanDsx1NoLossOfMasterClock.setStatus(
        ""
    )

wanDsx3LineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 103)
)
wanDsx3LineStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("RFC1407-MIB", "dsx3LineIndex"),
        ("RFC1407-MIB", "dsx3IfIndex"),
        ("RFC1407-MIB", "dsx3LineStatus"))
)
if mibBuilder.loadTexts:
    wanDsx3LineStatusChange.setStatus(
        ""
    )

wanDsx3LossOfMasterClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 104)
)
wanDsx3LossOfMasterClock.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("RFC1407-MIB", "dsx3LineIndex"),
        ("RFC1407-MIB", "dsx3IfIndex"),
        ("RFC1407-MIB", "dsx3LineStatus"))
)
if mibBuilder.loadTexts:
    wanDsx3LossOfMasterClock.setStatus(
        ""
    )

wanDsx3NoLossOfMasterClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 105)
)
wanDsx3NoLossOfMasterClock.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("RFC1407-MIB", "dsx3LineIndex"),
        ("RFC1407-MIB", "dsx3IfIndex"),
        ("RFC1407-MIB", "dsx3LineStatus"))
)
if mibBuilder.loadTexts:
    wanDsx3NoLossOfMasterClock.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAN-TRAP-MIB",
    **{"wanDsx1LineStatusChange": wanDsx1LineStatusChange,
       "wanDsx1LossOfMasterClock": wanDsx1LossOfMasterClock,
       "wanDsx1NoLossOfMasterClock": wanDsx1NoLossOfMasterClock,
       "wanDsx3LineStatusChange": wanDsx3LineStatusChange,
       "wanDsx3LossOfMasterClock": wanDsx3LossOfMasterClock,
       "wanDsx3NoLossOfMasterClock": wanDsx3NoLossOfMasterClock}
)
