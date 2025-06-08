# SNMP MIB module (TROPIC-DIAGNOSTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-DIAGNOSTIC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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

(tnDiagnosticMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnDiagnosticMIB",
    "tnSystemModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")


# MODULE-IDENTITY

tnDiagnosticMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnDiagnosticMibModule.setRevisions(
        ("2010-07-15 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnEquipDiagDescription(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )



# MIB Managed Objects in the order of their OIDs

_TnDiagnosticConf_ObjectIdentity = ObjectIdentity
tnDiagnosticConf = _TnDiagnosticConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1)
)
_TnDiagnosticGroups_ObjectIdentity = ObjectIdentity
tnDiagnosticGroups = _TnDiagnosticGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 1)
)
_TnDiagnosticCompliances_ObjectIdentity = ObjectIdentity
tnDiagnosticCompliances = _TnDiagnosticCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 2)
)
_TnDiagnosticObjs_ObjectIdentity = ObjectIdentity
tnDiagnosticObjs = _TnDiagnosticObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2)
)
_TnEquipmentDiagnosticStatusTable_Object = MibTable
tnEquipmentDiagnosticStatusTable = _TnEquipmentDiagnosticStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tnEquipmentDiagnosticStatusTable.setStatus("current")
_TnEquipDiagStatusEntry_Object = MibTableRow
tnEquipDiagStatusEntry = _TnEquipDiagStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1)
)
tnEquipDiagStatusEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagPort"),
    (0, "TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagId"),
    (0, "TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagUnit"),
)
if mibBuilder.loadTexts:
    tnEquipDiagStatusEntry.setStatus("current")
_TnEquipDiagPort_Type = Unsigned32
_TnEquipDiagPort_Object = MibTableColumn
tnEquipDiagPort = _TnEquipDiagPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 1),
    _TnEquipDiagPort_Type()
)
tnEquipDiagPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEquipDiagPort.setStatus("current")
_TnEquipDiagId_Type = Unsigned32
_TnEquipDiagId_Object = MibTableColumn
tnEquipDiagId = _TnEquipDiagId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 2),
    _TnEquipDiagId_Type()
)
tnEquipDiagId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEquipDiagId.setStatus("current")
_TnEquipDiagUnit_Type = Unsigned32
_TnEquipDiagUnit_Object = MibTableColumn
tnEquipDiagUnit = _TnEquipDiagUnit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 3),
    _TnEquipDiagUnit_Type()
)
tnEquipDiagUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEquipDiagUnit.setStatus("current")
_TnEquipDiagStatusDescr_Type = TnEquipDiagDescription
_TnEquipDiagStatusDescr_Object = MibTableColumn
tnEquipDiagStatusDescr = _TnEquipDiagStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 4),
    _TnEquipDiagStatusDescr_Type()
)
tnEquipDiagStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEquipDiagStatusDescr.setStatus("current")


class _TnEquipDiagStatusResult_Type(Integer32):
    """Custom type tnEquipDiagStatusResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2),
          ("willNotRun", 3),
          ("notExecuted", 4))
    )


_TnEquipDiagStatusResult_Type.__name__ = "Integer32"
_TnEquipDiagStatusResult_Object = MibTableColumn
tnEquipDiagStatusResult = _TnEquipDiagStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 5),
    _TnEquipDiagStatusResult_Type()
)
tnEquipDiagStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEquipDiagStatusResult.setStatus("current")

# Managed Objects groups

tnEquipDiagStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 1, 1)
)
tnEquipDiagStatusGroup.setObjects(
      *(("TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagStatusDescr"),
        ("TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagStatusResult"))
)
if mibBuilder.loadTexts:
    tnEquipDiagStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnDiagnosticCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 2, 1)
)
tnDiagnosticCompliance.setObjects(
    ("TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagStatusGroup")
)
if mibBuilder.loadTexts:
    tnDiagnosticCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-DIAGNOSTIC-MIB",
    **{"TnEquipDiagDescription": TnEquipDiagDescription,
       "tnDiagnosticMibModule": tnDiagnosticMibModule,
       "tnDiagnosticConf": tnDiagnosticConf,
       "tnDiagnosticGroups": tnDiagnosticGroups,
       "tnEquipDiagStatusGroup": tnEquipDiagStatusGroup,
       "tnDiagnosticCompliances": tnDiagnosticCompliances,
       "tnDiagnosticCompliance": tnDiagnosticCompliance,
       "tnDiagnosticObjs": tnDiagnosticObjs,
       "tnEquipmentDiagnosticStatusTable": tnEquipmentDiagnosticStatusTable,
       "tnEquipDiagStatusEntry": tnEquipDiagStatusEntry,
       "tnEquipDiagPort": tnEquipDiagPort,
       "tnEquipDiagId": tnEquipDiagId,
       "tnEquipDiagUnit": tnEquipDiagUnit,
       "tnEquipDiagStatusDescr": tnEquipDiagStatusDescr,
       "tnEquipDiagStatusResult": tnEquipDiagStatusResult}
)
