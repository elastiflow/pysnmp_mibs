# SNMP MIB module (RUIJIE-EG-BSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-EG-BSP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

ruijieEgBspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147)
)
if mibBuilder.loadTexts:
    ruijieEgBspMIB.setRevisions(
        ("2016-02-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieEgBspMIBObjects_ObjectIdentity = ObjectIdentity
ruijieEgBspMIBObjects = _RuijieEgBspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1)
)
_RuijieEgBspMaxNumber_Type = Integer32
_RuijieEgBspMaxNumber_Object = MibScalar
ruijieEgBspMaxNumber = _RuijieEgBspMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1, 1),
    _RuijieEgBspMaxNumber_Type()
)
ruijieEgBspMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEgBspMaxNumber.setStatus("current")
_RuijieEgBspInfoTable_Object = MibTable
ruijieEgBspInfoTable = _RuijieEgBspInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieEgBspInfoTable.setStatus("current")
_RuijieEgBspInfoEntry_Object = MibTableRow
ruijieEgBspInfoEntry = _RuijieEgBspInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1, 2, 1)
)
ruijieEgBspInfoEntry.setIndexNames(
    (0, "RUIJIE-EG-BSP-MIB", "ruijieEgBspInfoMacAddress"),
    (0, "RUIJIE-EG-BSP-MIB", "ruijieEgBspInfoVlanID"),
    (0, "RUIJIE-EG-BSP-MIB", "ruijieEgBspInfoPort"),
)
if mibBuilder.loadTexts:
    ruijieEgBspInfoEntry.setStatus("current")
_RuijieEgBspInfoMacAddress_Type = MacAddress
_RuijieEgBspInfoMacAddress_Object = MibTableColumn
ruijieEgBspInfoMacAddress = _RuijieEgBspInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1, 2, 1, 1),
    _RuijieEgBspInfoMacAddress_Type()
)
ruijieEgBspInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEgBspInfoMacAddress.setStatus("current")
_RuijieEgBspInfoVlanID_Type = Integer32
_RuijieEgBspInfoVlanID_Object = MibTableColumn
ruijieEgBspInfoVlanID = _RuijieEgBspInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1, 2, 1, 2),
    _RuijieEgBspInfoVlanID_Type()
)
ruijieEgBspInfoVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEgBspInfoVlanID.setStatus("current")
_RuijieEgBspInfoPort_Type = Integer32
_RuijieEgBspInfoPort_Object = MibTableColumn
ruijieEgBspInfoPort = _RuijieEgBspInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1, 2, 1, 3),
    _RuijieEgBspInfoPort_Type()
)
ruijieEgBspInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEgBspInfoPort.setStatus("current")
_RuijieEgBspInfoAge_Type = Integer32
_RuijieEgBspInfoAge_Object = MibTableColumn
ruijieEgBspInfoAge = _RuijieEgBspInfoAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 1, 2, 1, 4),
    _RuijieEgBspInfoAge_Type()
)
ruijieEgBspInfoAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEgBspInfoAge.setStatus("current")
_RuijieEgBspMIBConformance_ObjectIdentity = ObjectIdentity
ruijieEgBspMIBConformance = _RuijieEgBspMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 2)
)
_RuijieEgBspMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieEgBspMIBCompliances = _RuijieEgBspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 2, 1)
)
_RuijieEgBspMIBGroups_ObjectIdentity = ObjectIdentity
ruijieEgBspMIBGroups = _RuijieEgBspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 2, 2)
)

# Managed Objects groups

ruijieEgBspMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 2, 2, 1)
)
ruijieEgBspMIBGroup.setObjects(
      *(("RUIJIE-EG-BSP-MIB", "ruijieEgBspMaxNumber"),
        ("RUIJIE-EG-BSP-MIB", "ruijieEgBspInfoMacAddress"),
        ("RUIJIE-EG-BSP-MIB", "ruijieEgBspInfoVlanID"),
        ("RUIJIE-EG-BSP-MIB", "ruijieEgBspInfoPort"),
        ("RUIJIE-EG-BSP-MIB", "ruijieEgBspInfoAge"))
)
if mibBuilder.loadTexts:
    ruijieEgBspMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieEgBspMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 147, 2, 1, 1)
)
ruijieEgBspMIBCompliance.setObjects(
    ("RUIJIE-EG-BSP-MIB", "ruijieEgBspMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieEgBspMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-EG-BSP-MIB",
    **{"ruijieEgBspMIB": ruijieEgBspMIB,
       "ruijieEgBspMIBObjects": ruijieEgBspMIBObjects,
       "ruijieEgBspMaxNumber": ruijieEgBspMaxNumber,
       "ruijieEgBspInfoTable": ruijieEgBspInfoTable,
       "ruijieEgBspInfoEntry": ruijieEgBspInfoEntry,
       "ruijieEgBspInfoMacAddress": ruijieEgBspInfoMacAddress,
       "ruijieEgBspInfoVlanID": ruijieEgBspInfoVlanID,
       "ruijieEgBspInfoPort": ruijieEgBspInfoPort,
       "ruijieEgBspInfoAge": ruijieEgBspInfoAge,
       "ruijieEgBspMIBConformance": ruijieEgBspMIBConformance,
       "ruijieEgBspMIBCompliances": ruijieEgBspMIBCompliances,
       "ruijieEgBspMIBCompliance": ruijieEgBspMIBCompliance,
       "ruijieEgBspMIBGroups": ruijieEgBspMIBGroups,
       "ruijieEgBspMIBGroup": ruijieEgBspMIBGroup}
)
