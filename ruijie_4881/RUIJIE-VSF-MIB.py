# SNMP MIB module (RUIJIE-VSF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VSF-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieVsfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140)
)
if mibBuilder.loadTexts:
    ruijieVsfMIB.setRevisions(
        ("2015-06-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieVsfMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVsfMIBObjects = _RuijieVsfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1)
)
_RuijieVsfDeviceInfo_ObjectIdentity = ObjectIdentity
ruijieVsfDeviceInfo = _RuijieVsfDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 1)
)
_RuijieVsfDeviceTable_Object = MibTable
ruijieVsfDeviceTable = _RuijieVsfDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieVsfDeviceTable.setStatus("current")
_RuijieVsfDeviceEntry_Object = MibTableRow
ruijieVsfDeviceEntry = _RuijieVsfDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 1, 1, 1)
)
ruijieVsfDeviceEntry.setIndexNames(
    (0, "RUIJIE-VSF-MIB", "ruijieVsfDeviceID"),
)
if mibBuilder.loadTexts:
    ruijieVsfDeviceEntry.setStatus("current")
_RuijieVsfDeviceID_Type = Integer32
_RuijieVsfDeviceID_Object = MibTableColumn
ruijieVsfDeviceID = _RuijieVsfDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 1, 1, 1, 1),
    _RuijieVsfDeviceID_Type()
)
ruijieVsfDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfDeviceID.setStatus("current")
_RuijieVsfDeviceMac_Type = MacAddress
_RuijieVsfDeviceMac_Object = MibTableColumn
ruijieVsfDeviceMac = _RuijieVsfDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 1, 1, 1, 2),
    _RuijieVsfDeviceMac_Type()
)
ruijieVsfDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfDeviceMac.setStatus("current")
_RuijieVsfDeviceDescr_Type = DisplayString
_RuijieVsfDeviceDescr_Object = MibTableColumn
ruijieVsfDeviceDescr = _RuijieVsfDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 1, 1, 1, 3),
    _RuijieVsfDeviceDescr_Type()
)
ruijieVsfDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfDeviceDescr.setStatus("current")


class _RuijieVsfDeviceStatus_Type(Integer32):
    """Custom type ruijieVsfDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("recovery", 2))
    )


_RuijieVsfDeviceStatus_Type.__name__ = "Integer32"
_RuijieVsfDeviceStatus_Object = MibTableColumn
ruijieVsfDeviceStatus = _RuijieVsfDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 1, 1, 1, 4),
    _RuijieVsfDeviceStatus_Type()
)
ruijieVsfDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfDeviceStatus.setStatus("current")
_RuijieVsf_ObjectIdentity = ObjectIdentity
ruijieVsf = _RuijieVsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2)
)
_RuijieVsfPortTable_Object = MibTable
ruijieVsfPortTable = _RuijieVsfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieVsfPortTable.setStatus("current")
_RuijieVsfPortEntry_Object = MibTableRow
ruijieVsfPortEntry = _RuijieVsfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 1, 1)
)
ruijieVsfPortEntry.setIndexNames(
    (0, "RUIJIE-VSF-MIB", "ruijieVsfPortIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVsfPortEntry.setStatus("current")
_RuijieVsfPortIfIndex_Type = Integer32
_RuijieVsfPortIfIndex_Object = MibTableColumn
ruijieVsfPortIfIndex = _RuijieVsfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 1, 1, 1),
    _RuijieVsfPortIfIndex_Type()
)
ruijieVsfPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfPortIfIndex.setStatus("current")
_RuijieVsfApIf_Type = DisplayString
_RuijieVsfApIf_Object = MibTableColumn
ruijieVsfApIf = _RuijieVsfApIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 1, 1, 2),
    _RuijieVsfApIf_Type()
)
ruijieVsfApIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfApIf.setStatus("current")


class _RuijieVsfPortState_Type(Integer32):
    """Custom type ruijieVsfPortState based on Integer32"""
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
        *(("down", 1),
          ("up", 2),
          ("ok", 3),
          ("disable", 4),
          ("aged", 5))
    )


_RuijieVsfPortState_Type.__name__ = "Integer32"
_RuijieVsfPortState_Object = MibTableColumn
ruijieVsfPortState = _RuijieVsfPortState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 1, 1, 3),
    _RuijieVsfPortState_Type()
)
ruijieVsfPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfPortState.setStatus("current")
_RuijieVsfPortPeerIfIndex_Type = Integer32
_RuijieVsfPortPeerIfIndex_Object = MibTableColumn
ruijieVsfPortPeerIfIndex = _RuijieVsfPortPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 1, 1, 4),
    _RuijieVsfPortPeerIfIndex_Type()
)
ruijieVsfPortPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfPortPeerIfIndex.setStatus("current")
_RuijieVsfApTable_Object = MibTable
ruijieVsfApTable = _RuijieVsfApTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieVsfApTable.setStatus("current")
_RuijieVsfApEntry_Object = MibTableRow
ruijieVsfApEntry = _RuijieVsfApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 2, 1)
)
ruijieVsfApEntry.setIndexNames(
    (0, "RUIJIE-VSF-MIB", "ruijieVsfApIndex"),
)
if mibBuilder.loadTexts:
    ruijieVsfApEntry.setStatus("current")
_RuijieVsfApIndex_Type = Integer32
_RuijieVsfApIndex_Object = MibTableColumn
ruijieVsfApIndex = _RuijieVsfApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 2, 1, 1),
    _RuijieVsfApIndex_Type()
)
ruijieVsfApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfApIndex.setStatus("current")
_RuijieVsfApUptime_Type = DisplayString
_RuijieVsfApUptime_Object = MibTableColumn
ruijieVsfApUptime = _RuijieVsfApUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 1, 2, 2, 1, 2),
    _RuijieVsfApUptime_Type()
)
ruijieVsfApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsfApUptime.setStatus("current")
_RuijieVsfMIBConformance_ObjectIdentity = ObjectIdentity
ruijieVsfMIBConformance = _RuijieVsfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 3)
)
_RuijieVsfMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieVsfMIBCompliances = _RuijieVsfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 3, 1)
)
_RuijieVsfMIBGroups_ObjectIdentity = ObjectIdentity
ruijieVsfMIBGroups = _RuijieVsfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 3, 2)
)

# Managed Objects groups

ruijieVsfMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 3, 2, 1)
)
ruijieVsfMIBObjectsGroup.setObjects(
      *(("RUIJIE-VSF-MIB", "ruijieVsfDeviceID"),
        ("RUIJIE-VSF-MIB", "ruijieVsfDeviceMac"),
        ("RUIJIE-VSF-MIB", "ruijieVsfDeviceDescr"),
        ("RUIJIE-VSF-MIB", "ruijieVsfDeviceStatus"),
        ("RUIJIE-VSF-MIB", "ruijieVsfPortIfIndex"),
        ("RUIJIE-VSF-MIB", "ruijieVsfApIf"),
        ("RUIJIE-VSF-MIB", "ruijieVsfPortState"),
        ("RUIJIE-VSF-MIB", "ruijieVsfPortPeerIfIndex"),
        ("RUIJIE-VSF-MIB", "ruijieVsfApIndex"),
        ("RUIJIE-VSF-MIB", "ruijieVsfApUptime"))
)
if mibBuilder.loadTexts:
    ruijieVsfMIBObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieVsfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 140, 3, 1, 1)
)
ruijieVsfMIBCompliance.setObjects(
    ("RUIJIE-VSF-MIB", "ruijieVsfMIBObjectsGroup")
)
if mibBuilder.loadTexts:
    ruijieVsfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VSF-MIB",
    **{"ruijieVsfMIB": ruijieVsfMIB,
       "ruijieVsfMIBObjects": ruijieVsfMIBObjects,
       "ruijieVsfDeviceInfo": ruijieVsfDeviceInfo,
       "ruijieVsfDeviceTable": ruijieVsfDeviceTable,
       "ruijieVsfDeviceEntry": ruijieVsfDeviceEntry,
       "ruijieVsfDeviceID": ruijieVsfDeviceID,
       "ruijieVsfDeviceMac": ruijieVsfDeviceMac,
       "ruijieVsfDeviceDescr": ruijieVsfDeviceDescr,
       "ruijieVsfDeviceStatus": ruijieVsfDeviceStatus,
       "ruijieVsf": ruijieVsf,
       "ruijieVsfPortTable": ruijieVsfPortTable,
       "ruijieVsfPortEntry": ruijieVsfPortEntry,
       "ruijieVsfPortIfIndex": ruijieVsfPortIfIndex,
       "ruijieVsfApIf": ruijieVsfApIf,
       "ruijieVsfPortState": ruijieVsfPortState,
       "ruijieVsfPortPeerIfIndex": ruijieVsfPortPeerIfIndex,
       "ruijieVsfApTable": ruijieVsfApTable,
       "ruijieVsfApEntry": ruijieVsfApEntry,
       "ruijieVsfApIndex": ruijieVsfApIndex,
       "ruijieVsfApUptime": ruijieVsfApUptime,
       "ruijieVsfMIBConformance": ruijieVsfMIBConformance,
       "ruijieVsfMIBCompliances": ruijieVsfMIBCompliances,
       "ruijieVsfMIBCompliance": ruijieVsfMIBCompliance,
       "ruijieVsfMIBGroups": ruijieVsfMIBGroups,
       "ruijieVsfMIBObjectsGroup": ruijieVsfMIBObjectsGroup}
)
