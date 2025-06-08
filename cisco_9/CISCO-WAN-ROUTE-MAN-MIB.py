# SNMP MIB module (CISCO-WAN-ROUTE-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-WAN-ROUTE-MAN-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:15 2025
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

(AtmServiceCategory,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoWanRouteManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352)
)
if mibBuilder.loadTexts:
    ciscoWanRouteManMIB.setRevisions(
        ("2003-05-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanRouteManMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWanRouteManMIBNotifs = _CiscoWanRouteManMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 0)
)
_CiscoWanRouteManMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanRouteManMIBObjects = _CiscoWanRouteManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1)
)
_CwrmAlarm_ObjectIdentity = ObjectIdentity
cwrmAlarm = _CwrmAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 1)
)


class _CwrmAlarmDelayTimer_Type(Unsigned32):
    """Custom type cwrmAlarmDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CwrmAlarmDelayTimer_Type.__name__ = "Unsigned32"
_CwrmAlarmDelayTimer_Object = MibScalar
cwrmAlarmDelayTimer = _CwrmAlarmDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 1, 1),
    _CwrmAlarmDelayTimer_Type()
)
cwrmAlarmDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmAlarmDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    cwrmAlarmDelayTimer.setUnits("seconds")
_CwrmDerouteDelay_ObjectIdentity = ObjectIdentity
cwrmDerouteDelay = _CwrmDerouteDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 2)
)
_CwrmDerouteDelayTable_Object = MibTable
cwrmDerouteDelayTable = _CwrmDerouteDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwrmDerouteDelayTable.setStatus("current")
_CwrmDerouteDelayEntry_Object = MibTableRow
cwrmDerouteDelayEntry = _CwrmDerouteDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 2, 1, 1)
)
cwrmDerouteDelayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrmDerouteDelayEntry.setStatus("current")


class _CwrmDerouteDelayEnable_Type(TruthValue):
    """Custom type cwrmDerouteDelayEnable based on TruthValue"""
    defaultValue = 2


_CwrmDerouteDelayEnable_Type.__name__ = "TruthValue"
_CwrmDerouteDelayEnable_Object = MibTableColumn
cwrmDerouteDelayEnable = _CwrmDerouteDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 2, 1, 1, 1),
    _CwrmDerouteDelayEnable_Type()
)
cwrmDerouteDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmDerouteDelayEnable.setStatus("current")


class _CwrmDerouteDelayTimer_Type(Unsigned32):
    """Custom type cwrmDerouteDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CwrmDerouteDelayTimer_Type.__name__ = "Unsigned32"
_CwrmDerouteDelayTimer_Object = MibTableColumn
cwrmDerouteDelayTimer = _CwrmDerouteDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 2, 1, 1, 2),
    _CwrmDerouteDelayTimer_Type()
)
cwrmDerouteDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmDerouteDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    cwrmDerouteDelayTimer.setUnits("seconds")
_CwrmThreshold_ObjectIdentity = ObjectIdentity
cwrmThreshold = _CwrmThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3)
)
_CwrmThreshTable_Object = MibTable
cwrmThreshTable = _CwrmThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwrmThreshTable.setStatus("current")
_CwrmThreshEntry_Object = MibTableRow
cwrmThreshEntry = _CwrmThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1)
)
cwrmThreshEntry.setIndexNames(
    (0, "CISCO-WAN-ROUTE-MAN-MIB", "cwrmServiceCategory"),
)
if mibBuilder.loadTexts:
    cwrmThreshEntry.setStatus("current")
_CwrmServiceCategory_Type = AtmServiceCategory
_CwrmServiceCategory_Object = MibTableColumn
cwrmServiceCategory = _CwrmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1, 1),
    _CwrmServiceCategory_Type()
)
cwrmServiceCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrmServiceCategory.setStatus("current")


class _CwrmAWAbsolute_Type(Unsigned32):
    """Custom type cwrmAWAbsolute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwrmAWAbsolute_Type.__name__ = "Unsigned32"
_CwrmAWAbsolute_Object = MibTableColumn
cwrmAWAbsolute = _CwrmAWAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1, 2),
    _CwrmAWAbsolute_Type()
)
cwrmAWAbsolute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmAWAbsolute.setStatus("current")


class _CwrmAWPercent_Type(Unsigned32):
    """Custom type cwrmAWPercent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwrmAWPercent_Type.__name__ = "Unsigned32"
_CwrmAWPercent_Object = MibTableColumn
cwrmAWPercent = _CwrmAWPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1, 3),
    _CwrmAWPercent_Type()
)
cwrmAWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmAWPercent.setStatus("current")


class _CwrmCTDAbsolute_Type(Unsigned32):
    """Custom type cwrmCTDAbsolute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwrmCTDAbsolute_Type.__name__ = "Unsigned32"
_CwrmCTDAbsolute_Object = MibTableColumn
cwrmCTDAbsolute = _CwrmCTDAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1, 4),
    _CwrmCTDAbsolute_Type()
)
cwrmCTDAbsolute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmCTDAbsolute.setStatus("current")


class _CwrmCTDPercent_Type(Unsigned32):
    """Custom type cwrmCTDPercent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwrmCTDPercent_Type.__name__ = "Unsigned32"
_CwrmCTDPercent_Object = MibTableColumn
cwrmCTDPercent = _CwrmCTDPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1, 5),
    _CwrmCTDPercent_Type()
)
cwrmCTDPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmCTDPercent.setStatus("current")


class _CwrmCDVAbsolute_Type(Unsigned32):
    """Custom type cwrmCDVAbsolute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwrmCDVAbsolute_Type.__name__ = "Unsigned32"
_CwrmCDVAbsolute_Object = MibTableColumn
cwrmCDVAbsolute = _CwrmCDVAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1, 6),
    _CwrmCDVAbsolute_Type()
)
cwrmCDVAbsolute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmCDVAbsolute.setStatus("current")


class _CwrmCDVPercent_Type(Unsigned32):
    """Custom type cwrmCDVPercent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwrmCDVPercent_Type.__name__ = "Unsigned32"
_CwrmCDVPercent_Object = MibTableColumn
cwrmCDVPercent = _CwrmCDVPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 1, 3, 1, 1, 7),
    _CwrmCDVPercent_Type()
)
cwrmCDVPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrmCDVPercent.setStatus("current")
_CiscoWanRouteManMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanRouteManMIBConformance = _CiscoWanRouteManMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 2)
)
_CiscoWanRouteManMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanRouteManMIBCompliances = _CiscoWanRouteManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 2, 1)
)
_CiscoWanRouteManMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanRouteManMIBGroups = _CiscoWanRouteManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 2, 2)
)

# Managed Objects groups

ciscoWanAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 2, 2, 1)
)
ciscoWanAlarmGroup.setObjects(
    ("CISCO-WAN-ROUTE-MAN-MIB", "cwrmAlarmDelayTimer")
)
if mibBuilder.loadTexts:
    ciscoWanAlarmGroup.setStatus("current")

ciscoWanDerouteDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 2, 2, 2)
)
ciscoWanDerouteDelayGroup.setObjects(
      *(("CISCO-WAN-ROUTE-MAN-MIB", "cwrmDerouteDelayEnable"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "cwrmDerouteDelayTimer"))
)
if mibBuilder.loadTexts:
    ciscoWanDerouteDelayGroup.setStatus("current")

ciscoWanThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 2, 2, 3)
)
ciscoWanThresholdGroup.setObjects(
      *(("CISCO-WAN-ROUTE-MAN-MIB", "cwrmAWAbsolute"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "cwrmAWPercent"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "cwrmCTDAbsolute"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "cwrmCTDPercent"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "cwrmCDVAbsolute"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "cwrmCDVPercent"))
)
if mibBuilder.loadTexts:
    ciscoWanThresholdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanRouteManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 352, 2, 1, 1)
)
ciscoWanRouteManMIBCompliance.setObjects(
      *(("CISCO-WAN-ROUTE-MAN-MIB", "ciscoWanAlarmGroup"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "ciscoWanDerouteDelayGroup"),
        ("CISCO-WAN-ROUTE-MAN-MIB", "ciscoWanThresholdGroup"))
)
if mibBuilder.loadTexts:
    ciscoWanRouteManMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ROUTE-MAN-MIB",
    **{"ciscoWanRouteManMIB": ciscoWanRouteManMIB,
       "ciscoWanRouteManMIBNotifs": ciscoWanRouteManMIBNotifs,
       "ciscoWanRouteManMIBObjects": ciscoWanRouteManMIBObjects,
       "cwrmAlarm": cwrmAlarm,
       "cwrmAlarmDelayTimer": cwrmAlarmDelayTimer,
       "cwrmDerouteDelay": cwrmDerouteDelay,
       "cwrmDerouteDelayTable": cwrmDerouteDelayTable,
       "cwrmDerouteDelayEntry": cwrmDerouteDelayEntry,
       "cwrmDerouteDelayEnable": cwrmDerouteDelayEnable,
       "cwrmDerouteDelayTimer": cwrmDerouteDelayTimer,
       "cwrmThreshold": cwrmThreshold,
       "cwrmThreshTable": cwrmThreshTable,
       "cwrmThreshEntry": cwrmThreshEntry,
       "cwrmServiceCategory": cwrmServiceCategory,
       "cwrmAWAbsolute": cwrmAWAbsolute,
       "cwrmAWPercent": cwrmAWPercent,
       "cwrmCTDAbsolute": cwrmCTDAbsolute,
       "cwrmCTDPercent": cwrmCTDPercent,
       "cwrmCDVAbsolute": cwrmCDVAbsolute,
       "cwrmCDVPercent": cwrmCDVPercent,
       "ciscoWanRouteManMIBConformance": ciscoWanRouteManMIBConformance,
       "ciscoWanRouteManMIBCompliances": ciscoWanRouteManMIBCompliances,
       "ciscoWanRouteManMIBCompliance": ciscoWanRouteManMIBCompliance,
       "ciscoWanRouteManMIBGroups": ciscoWanRouteManMIBGroups,
       "ciscoWanAlarmGroup": ciscoWanAlarmGroup,
       "ciscoWanDerouteDelayGroup": ciscoWanDerouteDelayGroup,
       "ciscoWanThresholdGroup": ciscoWanThresholdGroup}
)
