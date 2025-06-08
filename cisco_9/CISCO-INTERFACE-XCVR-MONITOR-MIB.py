# SNMP MIB module (CISCO-INTERFACE-XCVR-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-INTERFACE-XCVR-MONITOR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:31:28 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoInterfaceXcvrMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 706)
)
if mibBuilder.loadTexts:
    ciscoInterfaceXcvrMonitorMIB.setRevisions(
        ("2009-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoInterfaceXcvrMonitorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("highSet", 1),
          ("lowSet", 2),
          ("highClear", 3),
          ("lowClear", 4),
          ("normal", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoInterfaceXcvrMonMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoInterfaceXcvrMonMIBNotifs = _CiscoInterfaceXcvrMonMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 0)
)
_CiscoInterfaceXcvrMonMIBObjects_ObjectIdentity = ObjectIdentity
ciscoInterfaceXcvrMonMIBObjects = _CiscoInterfaceXcvrMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1)
)
_CIfXcvrMonDigitalDiagTempAlarm_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTempAlarm_Object = MibScalar
cIfXcvrMonDigitalDiagTempAlarm = _CIfXcvrMonDigitalDiagTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 1),
    _CIfXcvrMonDigitalDiagTempAlarm_Type()
)
cIfXcvrMonDigitalDiagTempAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagTempAlarm.setStatus("current")
_CIfXcvrMonDigitalDiagTempWarning_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTempWarning_Object = MibScalar
cIfXcvrMonDigitalDiagTempWarning = _CIfXcvrMonDigitalDiagTempWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 2),
    _CIfXcvrMonDigitalDiagTempWarning_Type()
)
cIfXcvrMonDigitalDiagTempWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagTempWarning.setStatus("current")
_CIfXcvrMonDigitalDiagVoltAlarm_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagVoltAlarm_Object = MibScalar
cIfXcvrMonDigitalDiagVoltAlarm = _CIfXcvrMonDigitalDiagVoltAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 3),
    _CIfXcvrMonDigitalDiagVoltAlarm_Type()
)
cIfXcvrMonDigitalDiagVoltAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagVoltAlarm.setStatus("current")
_CIfXcvrMonDigitalDiagVoltWarning_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagVoltWarning_Object = MibScalar
cIfXcvrMonDigitalDiagVoltWarning = _CIfXcvrMonDigitalDiagVoltWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 4),
    _CIfXcvrMonDigitalDiagVoltWarning_Type()
)
cIfXcvrMonDigitalDiagVoltWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagVoltWarning.setStatus("current")
_CIfXcvrMonDigitalDiagCurrAlarm_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagCurrAlarm_Object = MibScalar
cIfXcvrMonDigitalDiagCurrAlarm = _CIfXcvrMonDigitalDiagCurrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 5),
    _CIfXcvrMonDigitalDiagCurrAlarm_Type()
)
cIfXcvrMonDigitalDiagCurrAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagCurrAlarm.setStatus("current")
_CIfXcvrMonDigitalDiagCurrWarning_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagCurrWarning_Object = MibScalar
cIfXcvrMonDigitalDiagCurrWarning = _CIfXcvrMonDigitalDiagCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 6),
    _CIfXcvrMonDigitalDiagCurrWarning_Type()
)
cIfXcvrMonDigitalDiagCurrWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagCurrWarning.setStatus("current")
_CIfXcvrMonDigitalDiagRxPwrAlarm_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagRxPwrAlarm_Object = MibScalar
cIfXcvrMonDigitalDiagRxPwrAlarm = _CIfXcvrMonDigitalDiagRxPwrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 7),
    _CIfXcvrMonDigitalDiagRxPwrAlarm_Type()
)
cIfXcvrMonDigitalDiagRxPwrAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagRxPwrAlarm.setStatus("current")
_CIfXcvrMonDigitalDiagRxPwrWarning_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagRxPwrWarning_Object = MibScalar
cIfXcvrMonDigitalDiagRxPwrWarning = _CIfXcvrMonDigitalDiagRxPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 8),
    _CIfXcvrMonDigitalDiagRxPwrWarning_Type()
)
cIfXcvrMonDigitalDiagRxPwrWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagRxPwrWarning.setStatus("current")
_CIfXcvrMonDigitalDiagTxPwrAlarm_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTxPwrAlarm_Object = MibScalar
cIfXcvrMonDigitalDiagTxPwrAlarm = _CIfXcvrMonDigitalDiagTxPwrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 9),
    _CIfXcvrMonDigitalDiagTxPwrAlarm_Type()
)
cIfXcvrMonDigitalDiagTxPwrAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagTxPwrAlarm.setStatus("current")
_CIfXcvrMonDigitalDiagTxPwrWarning_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTxPwrWarning_Object = MibScalar
cIfXcvrMonDigitalDiagTxPwrWarning = _CIfXcvrMonDigitalDiagTxPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 10),
    _CIfXcvrMonDigitalDiagTxPwrWarning_Type()
)
cIfXcvrMonDigitalDiagTxPwrWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagTxPwrWarning.setStatus("current")
_CIfXcvrMonDigitalDiagTxFaultAlarm_Type = CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTxFaultAlarm_Object = MibScalar
cIfXcvrMonDigitalDiagTxFaultAlarm = _CIfXcvrMonDigitalDiagTxFaultAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 11),
    _CIfXcvrMonDigitalDiagTxFaultAlarm_Type()
)
cIfXcvrMonDigitalDiagTxFaultAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cIfXcvrMonDigitalDiagTxFaultAlarm.setStatus("current")


class _CIfXcvrMonStatusChangeNotifEnable_Type(Integer32):
    """Custom type cIfXcvrMonStatusChangeNotifEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CIfXcvrMonStatusChangeNotifEnable_Type.__name__ = "Integer32"
_CIfXcvrMonStatusChangeNotifEnable_Object = MibScalar
cIfXcvrMonStatusChangeNotifEnable = _CIfXcvrMonStatusChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 12),
    _CIfXcvrMonStatusChangeNotifEnable_Type()
)
cIfXcvrMonStatusChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIfXcvrMonStatusChangeNotifEnable.setStatus("current")
_CiscoInterfaceXcvrMonMIBConform_ObjectIdentity = ObjectIdentity
ciscoInterfaceXcvrMonMIBConform = _CiscoInterfaceXcvrMonMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 2)
)
_CiscoInterfaceXcvrMonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoInterfaceXcvrMonMIBCompliances = _CiscoInterfaceXcvrMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 1)
)
_CiscoInterfaceXcvrMonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoInterfaceXcvrMonMIBGroups = _CiscoInterfaceXcvrMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2)
)

# Managed Objects groups

cIfXcvrDigitalDiagMonStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2, 1)
)
cIfXcvrDigitalDiagMonStatusGroup.setObjects(
      *(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxFaultAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotifEnable"))
)
if mibBuilder.loadTexts:
    cIfXcvrDigitalDiagMonStatusGroup.setStatus("current")


# Notification objects

cIfXcvrMonStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 0, 1)
)
cIfXcvrMonStatusChangeNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrAlarm"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrWarning"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxFaultAlarm"))
)
if mibBuilder.loadTexts:
    cIfXcvrMonStatusChangeNotif.setStatus(
        "current"
    )


# Notifications groups

cIfXcvrMonStatusChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2, 2)
)
cIfXcvrMonStatusChangeNotifGroup.setObjects(
    ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotif")
)
if mibBuilder.loadTexts:
    cIfXcvrMonStatusChangeNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cIfXcvrMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 1, 1)
)
cIfXcvrMonMIBCompliance.setObjects(
      *(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrDigitalDiagMonStatusGroup"),
        ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    cIfXcvrMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-INTERFACE-XCVR-MONITOR-MIB",
    **{"CiscoInterfaceXcvrMonitorStatus": CiscoInterfaceXcvrMonitorStatus,
       "ciscoInterfaceXcvrMonitorMIB": ciscoInterfaceXcvrMonitorMIB,
       "ciscoInterfaceXcvrMonMIBNotifs": ciscoInterfaceXcvrMonMIBNotifs,
       "cIfXcvrMonStatusChangeNotif": cIfXcvrMonStatusChangeNotif,
       "ciscoInterfaceXcvrMonMIBObjects": ciscoInterfaceXcvrMonMIBObjects,
       "cIfXcvrMonDigitalDiagTempAlarm": cIfXcvrMonDigitalDiagTempAlarm,
       "cIfXcvrMonDigitalDiagTempWarning": cIfXcvrMonDigitalDiagTempWarning,
       "cIfXcvrMonDigitalDiagVoltAlarm": cIfXcvrMonDigitalDiagVoltAlarm,
       "cIfXcvrMonDigitalDiagVoltWarning": cIfXcvrMonDigitalDiagVoltWarning,
       "cIfXcvrMonDigitalDiagCurrAlarm": cIfXcvrMonDigitalDiagCurrAlarm,
       "cIfXcvrMonDigitalDiagCurrWarning": cIfXcvrMonDigitalDiagCurrWarning,
       "cIfXcvrMonDigitalDiagRxPwrAlarm": cIfXcvrMonDigitalDiagRxPwrAlarm,
       "cIfXcvrMonDigitalDiagRxPwrWarning": cIfXcvrMonDigitalDiagRxPwrWarning,
       "cIfXcvrMonDigitalDiagTxPwrAlarm": cIfXcvrMonDigitalDiagTxPwrAlarm,
       "cIfXcvrMonDigitalDiagTxPwrWarning": cIfXcvrMonDigitalDiagTxPwrWarning,
       "cIfXcvrMonDigitalDiagTxFaultAlarm": cIfXcvrMonDigitalDiagTxFaultAlarm,
       "cIfXcvrMonStatusChangeNotifEnable": cIfXcvrMonStatusChangeNotifEnable,
       "ciscoInterfaceXcvrMonMIBConform": ciscoInterfaceXcvrMonMIBConform,
       "ciscoInterfaceXcvrMonMIBCompliances": ciscoInterfaceXcvrMonMIBCompliances,
       "cIfXcvrMonMIBCompliance": cIfXcvrMonMIBCompliance,
       "ciscoInterfaceXcvrMonMIBGroups": ciscoInterfaceXcvrMonMIBGroups,
       "cIfXcvrDigitalDiagMonStatusGroup": cIfXcvrDigitalDiagMonStatusGroup,
       "cIfXcvrMonStatusChangeNotifGroup": cIfXcvrMonStatusChangeNotifGroup}
)
