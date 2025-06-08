# SNMP MIB module (CISCO-LWAPP-U3INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-U3INTERFACE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:06 2025
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

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappU3InterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 852)
)
if mibBuilder.loadTexts:
    ciscoLwappU3InterfaceMIB.setRevisions(
        ("2017-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappU3InterfaceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappU3InterfaceMIBNotifs = _CiscoLwappU3InterfaceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 0)
)
_CiscoLwappU3InterfaceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappU3InterfaceMIBObjects = _CiscoLwappU3InterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1)
)
_CiscoLwappU3InterfaceMIBTableObjects_ObjectIdentity = ObjectIdentity
ciscoLwappU3InterfaceMIBTableObjects = _CiscoLwappU3InterfaceMIBTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1)
)
_CLU3InterfaceWlanTable_Object = MibTable
cLU3InterfaceWlanTable = _CLU3InterfaceWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLU3InterfaceWlanTable.setStatus("current")
_CLU3InterfaceWlanEntry_Object = MibTableRow
cLU3InterfaceWlanEntry = _CLU3InterfaceWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 1, 1)
)
cLU3InterfaceWlanEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLU3InterfaceWlanEntry.setStatus("current")


class _CLU3InterfaceWlanStatus_Type(TruthValue):
    """Custom type cLU3InterfaceWlanStatus based on TruthValue"""
    defaultValue = 2


_CLU3InterfaceWlanStatus_Type.__name__ = "TruthValue"
_CLU3InterfaceWlanStatus_Object = MibTableColumn
cLU3InterfaceWlanStatus = _CLU3InterfaceWlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 1, 1, 1),
    _CLU3InterfaceWlanStatus_Type()
)
cLU3InterfaceWlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLU3InterfaceWlanStatus.setStatus("current")


class _CLU3InterfaceReportingInterval_Type(Unsigned32):
    """Custom type cLU3InterfaceReportingInterval based on Unsigned32"""
    defaultValue = 30


_CLU3InterfaceReportingInterval_Type.__name__ = "Unsigned32"
_CLU3InterfaceReportingInterval_Object = MibTableColumn
cLU3InterfaceReportingInterval = _CLU3InterfaceReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 1, 1, 2),
    _CLU3InterfaceReportingInterval_Type()
)
cLU3InterfaceReportingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLU3InterfaceReportingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLU3InterfaceReportingInterval.setUnits("seconds")
_CLU3InterfaceClientTable_Object = MibTable
cLU3InterfaceClientTable = _CLU3InterfaceClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLU3InterfaceClientTable.setStatus("current")
_CLU3InterfaceClientEntry_Object = MibTableRow
cLU3InterfaceClientEntry = _CLU3InterfaceClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1)
)
cLU3InterfaceClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLU3InterfaceClientEntry.setStatus("current")


class _CLU3InterfaceClientSkipCount_Type(Unsigned32):
    """Custom type cLU3InterfaceClientSkipCount based on Unsigned32"""
    defaultValue = 0


_CLU3InterfaceClientSkipCount_Type.__name__ = "Unsigned32"
_CLU3InterfaceClientSkipCount_Object = MibTableColumn
cLU3InterfaceClientSkipCount = _CLU3InterfaceClientSkipCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1, 1),
    _CLU3InterfaceClientSkipCount_Type()
)
cLU3InterfaceClientSkipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLU3InterfaceClientSkipCount.setStatus("current")


class _CLU3InterfaceClientKeepAliveCount_Type(Unsigned32):
    """Custom type cLU3InterfaceClientKeepAliveCount based on Unsigned32"""
    defaultValue = 0


_CLU3InterfaceClientKeepAliveCount_Type.__name__ = "Unsigned32"
_CLU3InterfaceClientKeepAliveCount_Object = MibTableColumn
cLU3InterfaceClientKeepAliveCount = _CLU3InterfaceClientKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1, 2),
    _CLU3InterfaceClientKeepAliveCount_Type()
)
cLU3InterfaceClientKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLU3InterfaceClientKeepAliveCount.setStatus("current")


class _CLU3InterfaceClientEstimatePeriod_Type(Unsigned32):
    """Custom type cLU3InterfaceClientEstimatePeriod based on Unsigned32"""
    defaultValue = 0


_CLU3InterfaceClientEstimatePeriod_Type.__name__ = "Unsigned32"
_CLU3InterfaceClientEstimatePeriod_Object = MibTableColumn
cLU3InterfaceClientEstimatePeriod = _CLU3InterfaceClientEstimatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1, 3),
    _CLU3InterfaceClientEstimatePeriod_Type()
)
cLU3InterfaceClientEstimatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLU3InterfaceClientEstimatePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cLU3InterfaceClientEstimatePeriod.setUnits("seconds")


class _CLU3InterfaceClientBackoffTimer_Type(Unsigned32):
    """Custom type cLU3InterfaceClientBackoffTimer based on Unsigned32"""
    defaultValue = 0


_CLU3InterfaceClientBackoffTimer_Type.__name__ = "Unsigned32"
_CLU3InterfaceClientBackoffTimer_Object = MibTableColumn
cLU3InterfaceClientBackoffTimer = _CLU3InterfaceClientBackoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1, 4),
    _CLU3InterfaceClientBackoffTimer_Type()
)
cLU3InterfaceClientBackoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLU3InterfaceClientBackoffTimer.setStatus("current")
if mibBuilder.loadTexts:
    cLU3InterfaceClientBackoffTimer.setUnits("seconds")


class _CLU3InterfaceClientThroughput_Type(Unsigned32):
    """Custom type cLU3InterfaceClientThroughput based on Unsigned32"""
    defaultValue = 0


_CLU3InterfaceClientThroughput_Type.__name__ = "Unsigned32"
_CLU3InterfaceClientThroughput_Object = MibTableColumn
cLU3InterfaceClientThroughput = _CLU3InterfaceClientThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1, 5),
    _CLU3InterfaceClientThroughput_Type()
)
cLU3InterfaceClientThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLU3InterfaceClientThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cLU3InterfaceClientThroughput.setUnits("kbps")


class _CLU3InterfaceClientThreshold_Type(Unsigned32):
    """Custom type cLU3InterfaceClientThreshold based on Unsigned32"""
    defaultValue = 0


_CLU3InterfaceClientThreshold_Type.__name__ = "Unsigned32"
_CLU3InterfaceClientThreshold_Object = MibTableColumn
cLU3InterfaceClientThreshold = _CLU3InterfaceClientThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1, 6),
    _CLU3InterfaceClientThreshold_Type()
)
cLU3InterfaceClientThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLU3InterfaceClientThreshold.setStatus("current")


class _CLU3InterfaceClientEarlyLift_Type(Unsigned32):
    """Custom type cLU3InterfaceClientEarlyLift based on Unsigned32"""
    defaultValue = 0


_CLU3InterfaceClientEarlyLift_Type.__name__ = "Unsigned32"
_CLU3InterfaceClientEarlyLift_Object = MibTableColumn
cLU3InterfaceClientEarlyLift = _CLU3InterfaceClientEarlyLift_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 1, 1, 2, 1, 7),
    _CLU3InterfaceClientEarlyLift_Type()
)
cLU3InterfaceClientEarlyLift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLU3InterfaceClientEarlyLift.setStatus("current")
_CiscoLwappU3InterfaceMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappU3InterfaceMIBConform = _CiscoLwappU3InterfaceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 2)
)
_CiscoLwappU3InterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappU3InterfaceMIBCompliances = _CiscoLwappU3InterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 2, 1)
)
_CiscoLwappU3InterfaceMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappU3InterfaceMIBGroups = _CiscoLwappU3InterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 2, 2)
)

# Managed Objects groups

cLU3InterfaceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 2, 2, 1)
)
cLU3InterfaceConfigGroup.setObjects(
      *(("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceWlanStatus"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceReportingInterval"))
)
if mibBuilder.loadTexts:
    cLU3InterfaceConfigGroup.setStatus("current")

cLU3InterfaceClientMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 2, 2, 2)
)
cLU3InterfaceClientMonitorGroup.setObjects(
      *(("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientSkipCount"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientKeepAliveCount"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientEstimatePeriod"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientBackoffTimer"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientThroughput"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientThreshold"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientEarlyLift"))
)
if mibBuilder.loadTexts:
    cLU3InterfaceClientMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappU3InterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 852, 2, 1, 1)
)
ciscoLwappU3InterfaceMIBCompliance.setObjects(
      *(("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceConfigGroup"),
        ("CISCO-LWAPP-U3INTERFACE-MIB", "cLU3InterfaceClientMonitorGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappU3InterfaceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-U3INTERFACE-MIB",
    **{"ciscoLwappU3InterfaceMIB": ciscoLwappU3InterfaceMIB,
       "ciscoLwappU3InterfaceMIBNotifs": ciscoLwappU3InterfaceMIBNotifs,
       "ciscoLwappU3InterfaceMIBObjects": ciscoLwappU3InterfaceMIBObjects,
       "ciscoLwappU3InterfaceMIBTableObjects": ciscoLwappU3InterfaceMIBTableObjects,
       "cLU3InterfaceWlanTable": cLU3InterfaceWlanTable,
       "cLU3InterfaceWlanEntry": cLU3InterfaceWlanEntry,
       "cLU3InterfaceWlanStatus": cLU3InterfaceWlanStatus,
       "cLU3InterfaceReportingInterval": cLU3InterfaceReportingInterval,
       "cLU3InterfaceClientTable": cLU3InterfaceClientTable,
       "cLU3InterfaceClientEntry": cLU3InterfaceClientEntry,
       "cLU3InterfaceClientSkipCount": cLU3InterfaceClientSkipCount,
       "cLU3InterfaceClientKeepAliveCount": cLU3InterfaceClientKeepAliveCount,
       "cLU3InterfaceClientEstimatePeriod": cLU3InterfaceClientEstimatePeriod,
       "cLU3InterfaceClientBackoffTimer": cLU3InterfaceClientBackoffTimer,
       "cLU3InterfaceClientThroughput": cLU3InterfaceClientThroughput,
       "cLU3InterfaceClientThreshold": cLU3InterfaceClientThreshold,
       "cLU3InterfaceClientEarlyLift": cLU3InterfaceClientEarlyLift,
       "ciscoLwappU3InterfaceMIBConform": ciscoLwappU3InterfaceMIBConform,
       "ciscoLwappU3InterfaceMIBCompliances": ciscoLwappU3InterfaceMIBCompliances,
       "ciscoLwappU3InterfaceMIBCompliance": ciscoLwappU3InterfaceMIBCompliance,
       "ciscoLwappU3InterfaceMIBGroups": ciscoLwappU3InterfaceMIBGroups,
       "cLU3InterfaceConfigGroup": cLU3InterfaceConfigGroup,
       "cLU3InterfaceClientMonitorGroup": cLU3InterfaceClientMonitorGroup}
)
