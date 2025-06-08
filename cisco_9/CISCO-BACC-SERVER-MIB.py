# SNMP MIB module (CISCO-BACC-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-BACC-SERVER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:08:31 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

ciscoBaccServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 349)
)
if mibBuilder.loadTexts:
    ciscoBaccServerMIB.setRevisions(
        ("2005-09-02 00:00",
         "2003-08-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoBaccServerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("initializing", 2),
          ("disconnected", 3),
          ("shuttingDown", 4),
          ("readyOverloaded", 5),
          ("ready", 6),
          ("offline", 7),
          ("unlicensed", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoBaccServerMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoBaccServerMIBNotifs = _CiscoBaccServerMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 0)
)
_CiscoBaccServerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBaccServerMIBObjects = _CiscoBaccServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1)
)
_CiscoBaccServerSystem_ObjectIdentity = ObjectIdentity
ciscoBaccServerSystem = _CiscoBaccServerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1)
)
_CbsServerTable_Object = MibTable
cbsServerTable = _CbsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cbsServerTable.setStatus("current")
_CbsServerEntry_Object = MibTableRow
cbsServerEntry = _CbsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1, 1)
)
cbsServerEntry.setIndexNames(
    (0, "CISCO-BACC-SERVER-MIB", "cbsServerIndex"),
)
if mibBuilder.loadTexts:
    cbsServerEntry.setStatus("current")


class _CbsServerIndex_Type(Unsigned32):
    """Custom type cbsServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CbsServerIndex_Type.__name__ = "Unsigned32"
_CbsServerIndex_Object = MibTableColumn
cbsServerIndex = _CbsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1, 1, 1),
    _CbsServerIndex_Type()
)
cbsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsServerIndex.setStatus("current")
_CbsUptime_Type = TimeTicks
_CbsUptime_Object = MibTableColumn
cbsUptime = _CbsUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1, 1, 2),
    _CbsUptime_Type()
)
cbsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsUptime.setStatus("current")
_CbsState_Type = CiscoBaccServerState
_CbsState_Object = MibTableColumn
cbsState = _CbsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1, 1, 3),
    _CbsState_Type()
)
cbsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsState.setStatus("current")
_CbsVersion_Type = SnmpAdminString
_CbsVersion_Object = MibTableColumn
cbsVersion = _CbsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1, 1, 4),
    _CbsVersion_Type()
)
cbsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVersion.setStatus("current")


class _CbsNotifEnableFlags_Type(Bits):
    """Custom type cbsNotifEnableFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("cbsStateNotifEnabled", 0)
    )

_CbsNotifEnableFlags_Type.__name__ = "Bits"
_CbsNotifEnableFlags_Object = MibTableColumn
cbsNotifEnableFlags = _CbsNotifEnableFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1, 1, 5),
    _CbsNotifEnableFlags_Type()
)
cbsNotifEnableFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbsNotifEnableFlags.setStatus("current")
_CbsServerType_Type = SnmpAdminString
_CbsServerType_Object = MibTableColumn
cbsServerType = _CbsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 1, 1, 1, 1, 6),
    _CbsServerType_Type()
)
cbsServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsServerType.setStatus("current")
_CiscoBaccServerMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBaccServerMIBConformance = _CiscoBaccServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 2)
)
_CiscoBaccServerMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBaccServerMIBCompliances = _CiscoBaccServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 2, 1)
)
_CiscoBaccServerMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBaccServerMIBGroups = _CiscoBaccServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 2, 2)
)

# Managed Objects groups

ciscoBaccServerBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 2, 2, 1)
)
ciscoBaccServerBasicGroup.setObjects(
      *(("CISCO-BACC-SERVER-MIB", "cbsState"),
        ("CISCO-BACC-SERVER-MIB", "cbsUptime"),
        ("CISCO-BACC-SERVER-MIB", "cbsVersion"),
        ("CISCO-BACC-SERVER-MIB", "cbsServerType"))
)
if mibBuilder.loadTexts:
    ciscoBaccServerBasicGroup.setStatus("current")

ciscoBaccServerNotifObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 2, 2, 2)
)
ciscoBaccServerNotifObjGroup.setObjects(
    ("CISCO-BACC-SERVER-MIB", "cbsNotifEnableFlags")
)
if mibBuilder.loadTexts:
    ciscoBaccServerNotifObjGroup.setStatus("current")


# Notification objects

ciscoBaccServerStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 0, 1)
)
ciscoBaccServerStateChanged.setObjects(
      *(("CISCO-BACC-SERVER-MIB", "cbsState"),
        ("CISCO-BACC-SERVER-MIB", "cbsServerType"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    ciscoBaccServerStateChanged.setStatus(
        "current"
    )


# Notifications groups

ciscoBaccServerEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 2, 2, 3)
)
ciscoBaccServerEventGroup.setObjects(
    ("CISCO-BACC-SERVER-MIB", "ciscoBaccServerStateChanged")
)
if mibBuilder.loadTexts:
    ciscoBaccServerEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoBaccServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 349, 2, 1, 1)
)
ciscoBaccServerMIBCompliance.setObjects(
      *(("CISCO-BACC-SERVER-MIB", "ciscoBaccServerBasicGroup"),
        ("CISCO-BACC-SERVER-MIB", "ciscoBaccServerNotifObjGroup"),
        ("CISCO-BACC-SERVER-MIB", "ciscoBaccServerEventGroup"))
)
if mibBuilder.loadTexts:
    ciscoBaccServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BACC-SERVER-MIB",
    **{"CiscoBaccServerState": CiscoBaccServerState,
       "ciscoBaccServerMIB": ciscoBaccServerMIB,
       "ciscoBaccServerMIBNotifs": ciscoBaccServerMIBNotifs,
       "ciscoBaccServerStateChanged": ciscoBaccServerStateChanged,
       "ciscoBaccServerMIBObjects": ciscoBaccServerMIBObjects,
       "ciscoBaccServerSystem": ciscoBaccServerSystem,
       "cbsServerTable": cbsServerTable,
       "cbsServerEntry": cbsServerEntry,
       "cbsServerIndex": cbsServerIndex,
       "cbsUptime": cbsUptime,
       "cbsState": cbsState,
       "cbsVersion": cbsVersion,
       "cbsNotifEnableFlags": cbsNotifEnableFlags,
       "cbsServerType": cbsServerType,
       "ciscoBaccServerMIBConformance": ciscoBaccServerMIBConformance,
       "ciscoBaccServerMIBCompliances": ciscoBaccServerMIBCompliances,
       "ciscoBaccServerMIBCompliance": ciscoBaccServerMIBCompliance,
       "ciscoBaccServerMIBGroups": ciscoBaccServerMIBGroups,
       "ciscoBaccServerBasicGroup": ciscoBaccServerBasicGroup,
       "ciscoBaccServerNotifObjGroup": ciscoBaccServerNotifObjGroup,
       "ciscoBaccServerEventGroup": ciscoBaccServerEventGroup}
)
