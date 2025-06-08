# SNMP MIB module (CISCO-LPTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LPTS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:34 2025
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

ciscoLptsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 812)
)
if mibBuilder.loadTexts:
    ciscoLptsMIB.setRevisions(
        ("2013-09-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("global", 2),
          ("local", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLptsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLptsMIBNotifs = _CiscoLptsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 0)
)
_CiscoLptsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLptsMIBObjects = _CiscoLptsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1)
)
_ClGlobalFlowTable_Object = MibTable
clGlobalFlowTable = _ClGlobalFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1)
)
if mibBuilder.loadTexts:
    clGlobalFlowTable.setStatus("current")
_ClGlobalFlowEntry_Object = MibTableRow
clGlobalFlowEntry = _ClGlobalFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1)
)
clGlobalFlowEntry.setIndexNames(
    (0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"),
)
if mibBuilder.loadTexts:
    clGlobalFlowEntry.setStatus("current")


class _ClGlobalFlowIndex_Type(Unsigned32):
    """Custom type clGlobalFlowIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClGlobalFlowIndex_Type.__name__ = "Unsigned32"
_ClGlobalFlowIndex_Object = MibTableColumn
clGlobalFlowIndex = _ClGlobalFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 1),
    _ClGlobalFlowIndex_Type()
)
clGlobalFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGlobalFlowIndex.setStatus("current")


class _ClGlobalFlowType_Type(SnmpAdminString):
    """Custom type clGlobalFlowType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_ClGlobalFlowType_Type.__name__ = "SnmpAdminString"
_ClGlobalFlowType_Object = MibTableColumn
clGlobalFlowType = _ClGlobalFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 2),
    _ClGlobalFlowType_Type()
)
clGlobalFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGlobalFlowType.setStatus("current")
_ClGlobalType_Type = ClFlowType
_ClGlobalType_Object = MibTableColumn
clGlobalType = _ClGlobalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 3),
    _ClGlobalType_Type()
)
clGlobalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGlobalType.setStatus("current")
_ClGlobalCurrentRate_Type = Unsigned32
_ClGlobalCurrentRate_Object = MibTableColumn
clGlobalCurrentRate = _ClGlobalCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 4),
    _ClGlobalCurrentRate_Type()
)
clGlobalCurrentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGlobalCurrentRate.setStatus("current")
if mibBuilder.loadTexts:
    clGlobalCurrentRate.setUnits("PPS")
_ClLocalFlowTable_Object = MibTable
clLocalFlowTable = _ClLocalFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2)
)
if mibBuilder.loadTexts:
    clLocalFlowTable.setStatus("current")
_ClLocalFlowEntry_Object = MibTableRow
clLocalFlowEntry = _ClLocalFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1)
)
clLocalFlowEntry.setIndexNames(
    (0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"),
    (0, "CISCO-LPTS-MIB", "clLocalNodeID"),
)
if mibBuilder.loadTexts:
    clLocalFlowEntry.setStatus("current")


class _ClLocalNodeID_Type(Unsigned32):
    """Custom type clLocalNodeID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClLocalNodeID_Type.__name__ = "Unsigned32"
_ClLocalNodeID_Object = MibTableColumn
clLocalNodeID = _ClLocalNodeID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 1),
    _ClLocalNodeID_Type()
)
clLocalNodeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clLocalNodeID.setStatus("current")
_ClLocalType_Type = ClFlowType
_ClLocalType_Object = MibTableColumn
clLocalType = _ClLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 2),
    _ClLocalType_Type()
)
clLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clLocalType.setStatus("current")
_ClLocalCurrentRate_Type = Unsigned32
_ClLocalCurrentRate_Object = MibTableColumn
clLocalCurrentRate = _ClLocalCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 3),
    _ClLocalCurrentRate_Type()
)
clLocalCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clLocalCurrentRate.setStatus("current")
if mibBuilder.loadTexts:
    clLocalCurrentRate.setUnits("PPS")
_ClLocalAccepted_Type = Counter64
_ClLocalAccepted_Object = MibTableColumn
clLocalAccepted = _ClLocalAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 4),
    _ClLocalAccepted_Type()
)
clLocalAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clLocalAccepted.setStatus("current")
_ClLocalDropped_Type = Counter64
_ClLocalDropped_Object = MibTableColumn
clLocalDropped = _ClLocalDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 5),
    _ClLocalDropped_Type()
)
clLocalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clLocalDropped.setStatus("current")
_ClLocalTosValue_Type = Unsigned32
_ClLocalTosValue_Object = MibTableColumn
clLocalTosValue = _ClLocalTosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 6),
    _ClLocalTosValue_Type()
)
clLocalTosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clLocalTosValue.setStatus("current")
_CiscoLptsMIBConform_ObjectIdentity = ObjectIdentity
ciscoLptsMIBConform = _CiscoLptsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 2)
)
_CiscoLptsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLptsMIBCompliances = _CiscoLptsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1)
)
_CiscoLptsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLptsMIBGroups = _CiscoLptsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2)
)

# Managed Objects groups

clGlobalFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 1)
)
clGlobalFlowGroup.setObjects(
      *(("CISCO-LPTS-MIB", "clGlobalFlowType"),
        ("CISCO-LPTS-MIB", "clGlobalCurrentRate"),
        ("CISCO-LPTS-MIB", "clGlobalType"))
)
if mibBuilder.loadTexts:
    clGlobalFlowGroup.setStatus("current")

clLocalFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 2)
)
clLocalFlowGroup.setObjects(
      *(("CISCO-LPTS-MIB", "clLocalCurrentRate"),
        ("CISCO-LPTS-MIB", "clLocalAccepted"),
        ("CISCO-LPTS-MIB", "clLocalDropped"),
        ("CISCO-LPTS-MIB", "clLocalType"),
        ("CISCO-LPTS-MIB", "clLocalTosValue"))
)
if mibBuilder.loadTexts:
    clLocalFlowGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLptsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1, 1)
)
ciscoLptsMIBCompliance.setObjects(
      *(("CISCO-LPTS-MIB", "clLocalFlowGroup"),
        ("CISCO-LPTS-MIB", "clGlobalFlowGroup"))
)
if mibBuilder.loadTexts:
    ciscoLptsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LPTS-MIB",
    **{"ClFlowType": ClFlowType,
       "ciscoLptsMIB": ciscoLptsMIB,
       "ciscoLptsMIBNotifs": ciscoLptsMIBNotifs,
       "ciscoLptsMIBObjects": ciscoLptsMIBObjects,
       "clGlobalFlowTable": clGlobalFlowTable,
       "clGlobalFlowEntry": clGlobalFlowEntry,
       "clGlobalFlowIndex": clGlobalFlowIndex,
       "clGlobalFlowType": clGlobalFlowType,
       "clGlobalType": clGlobalType,
       "clGlobalCurrentRate": clGlobalCurrentRate,
       "clLocalFlowTable": clLocalFlowTable,
       "clLocalFlowEntry": clLocalFlowEntry,
       "clLocalNodeID": clLocalNodeID,
       "clLocalType": clLocalType,
       "clLocalCurrentRate": clLocalCurrentRate,
       "clLocalAccepted": clLocalAccepted,
       "clLocalDropped": clLocalDropped,
       "clLocalTosValue": clLocalTosValue,
       "ciscoLptsMIBConform": ciscoLptsMIBConform,
       "ciscoLptsMIBCompliances": ciscoLptsMIBCompliances,
       "ciscoLptsMIBCompliance": ciscoLptsMIBCompliance,
       "ciscoLptsMIBGroups": ciscoLptsMIBGroups,
       "clGlobalFlowGroup": clGlobalFlowGroup,
       "clLocalFlowGroup": clLocalFlowGroup}
)
