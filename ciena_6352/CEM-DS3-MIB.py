# SNMP MIB module (CEM-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-DS3-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(dsx3ConfigEntry,
 dsx3CurrentEntry,
 dsx3FarEndCurrentEntry,
 dsx3FarEndIntervalEntry,
 dsx3IntervalEntry) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3ConfigEntry",
    "dsx3CurrentEntry",
    "dsx3FarEndCurrentEntry",
    "dsx3FarEndIntervalEntry",
    "dsx3IntervalEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cnDs3Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 19)
)
if mibBuilder.loadTexts:
    cnDs3Module.setRevisions(
        ("2003-02-21 14:23",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DS3ActiveTimeSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("freeRun", -1),
          ("t1TimeSourceNotProvisioned", 0),
          ("t1Interface1", 1),
          ("t1Interface2", 2),
          ("t1Interface3", 3),
          ("t1Interface4", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CnDsx3NearEndCurrentTable_Object = MibTable
cnDsx3NearEndCurrentTable = _CnDsx3NearEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 1)
)
if mibBuilder.loadTexts:
    cnDsx3NearEndCurrentTable.setStatus("obsolete")
_CnDsx3NearEndCurrentEntry_Object = MibTableRow
cnDsx3NearEndCurrentEntry = _CnDsx3NearEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 1, 1)
)
if mibBuilder.loadTexts:
    cnDsx3NearEndCurrentEntry.setStatus("obsolete")
_CnDsx3NearEndPlcpCodingViolation_Type = DS3ActiveTimeSource
_CnDsx3NearEndPlcpCodingViolation_Object = MibTableColumn
cnDsx3NearEndPlcpCodingViolation = _CnDsx3NearEndPlcpCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 1, 1, 1),
    _CnDsx3NearEndPlcpCodingViolation_Type()
)
cnDsx3NearEndPlcpCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndPlcpCodingViolation.setStatus("obsolete")
_CnDsx3NearEndPlcpESs_Type = Integer32
_CnDsx3NearEndPlcpESs_Object = MibTableColumn
cnDsx3NearEndPlcpESs = _CnDsx3NearEndPlcpESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 1, 1, 2),
    _CnDsx3NearEndPlcpESs_Type()
)
cnDsx3NearEndPlcpESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndPlcpESs.setStatus("obsolete")
_CnDsx3NearEndPlcpSESs_Type = Integer32
_CnDsx3NearEndPlcpSESs_Object = MibTableColumn
cnDsx3NearEndPlcpSESs = _CnDsx3NearEndPlcpSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 1, 1, 3),
    _CnDsx3NearEndPlcpSESs_Type()
)
cnDsx3NearEndPlcpSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndPlcpSESs.setStatus("obsolete")
_CnDsx3NearEndPlcpSEFSs_Type = Integer32
_CnDsx3NearEndPlcpSEFSs_Object = MibTableColumn
cnDsx3NearEndPlcpSEFSs = _CnDsx3NearEndPlcpSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 1, 1, 4),
    _CnDsx3NearEndPlcpSEFSs_Type()
)
cnDsx3NearEndPlcpSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndPlcpSEFSs.setStatus("obsolete")
_CnDsx3NearEndPlcpUASs_Type = Integer32
_CnDsx3NearEndPlcpUASs_Object = MibTableColumn
cnDsx3NearEndPlcpUASs = _CnDsx3NearEndPlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 1, 1, 5),
    _CnDsx3NearEndPlcpUASs_Type()
)
cnDsx3NearEndPlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndPlcpUASs.setStatus("obsolete")
_CnDsx3NearEndIntervalTable_Object = MibTable
cnDsx3NearEndIntervalTable = _CnDsx3NearEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 2)
)
if mibBuilder.loadTexts:
    cnDsx3NearEndIntervalTable.setStatus("obsolete")
_CnDsx3NearEndIntervalEntry_Object = MibTableRow
cnDsx3NearEndIntervalEntry = _CnDsx3NearEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 2, 1)
)
if mibBuilder.loadTexts:
    cnDsx3NearEndIntervalEntry.setStatus("obsolete")
_CnDsx3NearEndIntervalPlcpCodingViolation_Type = Integer32
_CnDsx3NearEndIntervalPlcpCodingViolation_Object = MibTableColumn
cnDsx3NearEndIntervalPlcpCodingViolation = _CnDsx3NearEndIntervalPlcpCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 2, 1, 1),
    _CnDsx3NearEndIntervalPlcpCodingViolation_Type()
)
cnDsx3NearEndIntervalPlcpCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndIntervalPlcpCodingViolation.setStatus("obsolete")
_CnDsx3NearEndIntervalPlcpESs_Type = Integer32
_CnDsx3NearEndIntervalPlcpESs_Object = MibTableColumn
cnDsx3NearEndIntervalPlcpESs = _CnDsx3NearEndIntervalPlcpESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 2, 1, 2),
    _CnDsx3NearEndIntervalPlcpESs_Type()
)
cnDsx3NearEndIntervalPlcpESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndIntervalPlcpESs.setStatus("obsolete")
_CnDsx3NearEndIntervalPlcpSESs_Type = Integer32
_CnDsx3NearEndIntervalPlcpSESs_Object = MibTableColumn
cnDsx3NearEndIntervalPlcpSESs = _CnDsx3NearEndIntervalPlcpSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 2, 1, 3),
    _CnDsx3NearEndIntervalPlcpSESs_Type()
)
cnDsx3NearEndIntervalPlcpSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndIntervalPlcpSESs.setStatus("obsolete")
_CnDsx3NearEndIntervalPlcpSEFSs_Type = Integer32
_CnDsx3NearEndIntervalPlcpSEFSs_Object = MibTableColumn
cnDsx3NearEndIntervalPlcpSEFSs = _CnDsx3NearEndIntervalPlcpSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 2, 1, 4),
    _CnDsx3NearEndIntervalPlcpSEFSs_Type()
)
cnDsx3NearEndIntervalPlcpSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndIntervalPlcpSEFSs.setStatus("obsolete")
_CnDsx3NearEndIntervalPlcpUASs_Type = Integer32
_CnDsx3NearEndIntervalPlcpUASs_Object = MibTableColumn
cnDsx3NearEndIntervalPlcpUASs = _CnDsx3NearEndIntervalPlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 2, 1, 5),
    _CnDsx3NearEndIntervalPlcpUASs_Type()
)
cnDsx3NearEndIntervalPlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3NearEndIntervalPlcpUASs.setStatus("obsolete")
_CnDsx3FarEndCurrentTable_Object = MibTable
cnDsx3FarEndCurrentTable = _CnDsx3FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 3)
)
if mibBuilder.loadTexts:
    cnDsx3FarEndCurrentTable.setStatus("obsolete")
_CnDsx3FarEndCurrentEntry_Object = MibTableRow
cnDsx3FarEndCurrentEntry = _CnDsx3FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 3, 1)
)
if mibBuilder.loadTexts:
    cnDsx3FarEndCurrentEntry.setStatus("obsolete")
_CnDsx3FarEndPlcpFebe_Type = Integer32
_CnDsx3FarEndPlcpFebe_Object = MibTableColumn
cnDsx3FarEndPlcpFebe = _CnDsx3FarEndPlcpFebe_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 3, 1, 1),
    _CnDsx3FarEndPlcpFebe_Type()
)
cnDsx3FarEndPlcpFebe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3FarEndPlcpFebe.setStatus("obsolete")
_CnDsx3FarEndPlcpESs_Type = Integer32
_CnDsx3FarEndPlcpESs_Object = MibTableColumn
cnDsx3FarEndPlcpESs = _CnDsx3FarEndPlcpESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 3, 1, 2),
    _CnDsx3FarEndPlcpESs_Type()
)
cnDsx3FarEndPlcpESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3FarEndPlcpESs.setStatus("obsolete")
_CnDsx3FarEndPlcpSESs_Type = Integer32
_CnDsx3FarEndPlcpSESs_Object = MibTableColumn
cnDsx3FarEndPlcpSESs = _CnDsx3FarEndPlcpSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 3, 1, 3),
    _CnDsx3FarEndPlcpSESs_Type()
)
cnDsx3FarEndPlcpSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3FarEndPlcpSESs.setStatus("obsolete")
_CnDsx3FarEndIntervalTable_Object = MibTable
cnDsx3FarEndIntervalTable = _CnDsx3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 4)
)
if mibBuilder.loadTexts:
    cnDsx3FarEndIntervalTable.setStatus("obsolete")
_CnDsx3FarEndIntervalEntry_Object = MibTableRow
cnDsx3FarEndIntervalEntry = _CnDsx3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 4, 1)
)
if mibBuilder.loadTexts:
    cnDsx3FarEndIntervalEntry.setStatus("obsolete")
_CnDsx3FarEndIntervalPlcpFebe_Type = Integer32
_CnDsx3FarEndIntervalPlcpFebe_Object = MibTableColumn
cnDsx3FarEndIntervalPlcpFebe = _CnDsx3FarEndIntervalPlcpFebe_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 4, 1, 1),
    _CnDsx3FarEndIntervalPlcpFebe_Type()
)
cnDsx3FarEndIntervalPlcpFebe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3FarEndIntervalPlcpFebe.setStatus("obsolete")
_CnDsx3FarEndIntervalPlcpESs_Type = Integer32
_CnDsx3FarEndIntervalPlcpESs_Object = MibTableColumn
cnDsx3FarEndIntervalPlcpESs = _CnDsx3FarEndIntervalPlcpESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 4, 1, 2),
    _CnDsx3FarEndIntervalPlcpESs_Type()
)
cnDsx3FarEndIntervalPlcpESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3FarEndIntervalPlcpESs.setStatus("obsolete")
_CnDsx3FarEndIntervalPlcpSESs_Type = Integer32
_CnDsx3FarEndIntervalPlcpSESs_Object = MibTableColumn
cnDsx3FarEndIntervalPlcpSESs = _CnDsx3FarEndIntervalPlcpSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 4, 1, 3),
    _CnDsx3FarEndIntervalPlcpSESs_Type()
)
cnDsx3FarEndIntervalPlcpSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDsx3FarEndIntervalPlcpSESs.setStatus("obsolete")
_CnDsx3ConfigTable_Object = MibTable
cnDsx3ConfigTable = _CnDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 5)
)
if mibBuilder.loadTexts:
    cnDsx3ConfigTable.setStatus("current")
_CnDsx3ConfigEntry_Object = MibTableRow
cnDsx3ConfigEntry = _CnDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 5, 1)
)
if mibBuilder.loadTexts:
    cnDsx3ConfigEntry.setStatus("current")


class _CnDsx3ConfigMappingMethod_Type(Integer32):
    """Custom type cnDsx3ConfigMappingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plcp", 1),
          ("adm", 2))
    )


_CnDsx3ConfigMappingMethod_Type.__name__ = "Integer32"
_CnDsx3ConfigMappingMethod_Object = MibTableColumn
cnDsx3ConfigMappingMethod = _CnDsx3ConfigMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 6352, 19, 5, 1, 1),
    _CnDsx3ConfigMappingMethod_Type()
)
cnDsx3ConfigMappingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDsx3ConfigMappingMethod.setStatus("current")
_CnDs3ModuleConformance_ObjectIdentity = ObjectIdentity
cnDs3ModuleConformance = _CnDs3ModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 19, 6)
)
dsx3CurrentEntry.registerAugmentions(
    ("CEM-DS3-MIB",
     "cnDsx3NearEndCurrentEntry")
)
cnDsx3NearEndCurrentEntry.setIndexNames(*dsx3CurrentEntry.getIndexNames())
dsx3IntervalEntry.registerAugmentions(
    ("CEM-DS3-MIB",
     "cnDsx3NearEndIntervalEntry")
)
cnDsx3NearEndIntervalEntry.setIndexNames(*dsx3IntervalEntry.getIndexNames())
dsx3FarEndCurrentEntry.registerAugmentions(
    ("CEM-DS3-MIB",
     "cnDsx3FarEndCurrentEntry")
)
cnDsx3FarEndCurrentEntry.setIndexNames(*dsx3FarEndCurrentEntry.getIndexNames())
dsx3FarEndIntervalEntry.registerAugmentions(
    ("CEM-DS3-MIB",
     "cnDsx3FarEndIntervalEntry")
)
cnDsx3FarEndIntervalEntry.setIndexNames(*dsx3FarEndIntervalEntry.getIndexNames())
dsx3ConfigEntry.registerAugmentions(
    ("CEM-DS3-MIB",
     "cnDsx3ConfigEntry")
)
cnDsx3ConfigEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())

# Managed Objects groups

cnDs3GeneralDS3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 19, 6, 1)
)
cnDs3GeneralDS3Group.setObjects(
      *(("CEM-DS3-MIB", "cnDsx3NearEndPlcpCodingViolation"),
        ("CEM-DS3-MIB", "cnDsx3NearEndPlcpESs"),
        ("CEM-DS3-MIB", "cnDsx3NearEndPlcpSESs"),
        ("CEM-DS3-MIB", "cnDsx3NearEndPlcpSEFSs"),
        ("CEM-DS3-MIB", "cnDsx3FarEndPlcpFebe"),
        ("CEM-DS3-MIB", "cnDsx3FarEndPlcpESs"),
        ("CEM-DS3-MIB", "cnDsx3ConfigMappingMethod"),
        ("CEM-DS3-MIB", "cnDsx3FarEndPlcpSESs"),
        ("CEM-DS3-MIB", "cnDsx3NearEndIntervalPlcpUASs"),
        ("CEM-DS3-MIB", "cnDsx3NearEndPlcpUASs"),
        ("CEM-DS3-MIB", "cnDsx3NearEndIntervalPlcpCodingViolation"),
        ("CEM-DS3-MIB", "cnDsx3NearEndIntervalPlcpESs"),
        ("CEM-DS3-MIB", "cnDsx3NearEndIntervalPlcpSESs"),
        ("CEM-DS3-MIB", "cnDsx3NearEndIntervalPlcpSEFSs"),
        ("CEM-DS3-MIB", "cnDsx3FarEndIntervalPlcpFebe"),
        ("CEM-DS3-MIB", "cnDsx3FarEndIntervalPlcpESs"),
        ("CEM-DS3-MIB", "cnDsx3FarEndIntervalPlcpSESs"))
)
if mibBuilder.loadTexts:
    cnDs3GeneralDS3Group.setStatus("obsolete")

cnDs3CN1000Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 19, 6, 3)
)
cnDs3CN1000Group.setObjects(
    ("CEM-DS3-MIB", "cnDsx3ConfigMappingMethod")
)
if mibBuilder.loadTexts:
    cnDs3CN1000Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-DS3-MIB",
    **{"DS3ActiveTimeSource": DS3ActiveTimeSource,
       "cnDs3Module": cnDs3Module,
       "cnDsx3NearEndCurrentTable": cnDsx3NearEndCurrentTable,
       "cnDsx3NearEndCurrentEntry": cnDsx3NearEndCurrentEntry,
       "cnDsx3NearEndPlcpCodingViolation": cnDsx3NearEndPlcpCodingViolation,
       "cnDsx3NearEndPlcpESs": cnDsx3NearEndPlcpESs,
       "cnDsx3NearEndPlcpSESs": cnDsx3NearEndPlcpSESs,
       "cnDsx3NearEndPlcpSEFSs": cnDsx3NearEndPlcpSEFSs,
       "cnDsx3NearEndPlcpUASs": cnDsx3NearEndPlcpUASs,
       "cnDsx3NearEndIntervalTable": cnDsx3NearEndIntervalTable,
       "cnDsx3NearEndIntervalEntry": cnDsx3NearEndIntervalEntry,
       "cnDsx3NearEndIntervalPlcpCodingViolation": cnDsx3NearEndIntervalPlcpCodingViolation,
       "cnDsx3NearEndIntervalPlcpESs": cnDsx3NearEndIntervalPlcpESs,
       "cnDsx3NearEndIntervalPlcpSESs": cnDsx3NearEndIntervalPlcpSESs,
       "cnDsx3NearEndIntervalPlcpSEFSs": cnDsx3NearEndIntervalPlcpSEFSs,
       "cnDsx3NearEndIntervalPlcpUASs": cnDsx3NearEndIntervalPlcpUASs,
       "cnDsx3FarEndCurrentTable": cnDsx3FarEndCurrentTable,
       "cnDsx3FarEndCurrentEntry": cnDsx3FarEndCurrentEntry,
       "cnDsx3FarEndPlcpFebe": cnDsx3FarEndPlcpFebe,
       "cnDsx3FarEndPlcpESs": cnDsx3FarEndPlcpESs,
       "cnDsx3FarEndPlcpSESs": cnDsx3FarEndPlcpSESs,
       "cnDsx3FarEndIntervalTable": cnDsx3FarEndIntervalTable,
       "cnDsx3FarEndIntervalEntry": cnDsx3FarEndIntervalEntry,
       "cnDsx3FarEndIntervalPlcpFebe": cnDsx3FarEndIntervalPlcpFebe,
       "cnDsx3FarEndIntervalPlcpESs": cnDsx3FarEndIntervalPlcpESs,
       "cnDsx3FarEndIntervalPlcpSESs": cnDsx3FarEndIntervalPlcpSESs,
       "cnDsx3ConfigTable": cnDsx3ConfigTable,
       "cnDsx3ConfigEntry": cnDsx3ConfigEntry,
       "cnDsx3ConfigMappingMethod": cnDsx3ConfigMappingMethod,
       "cnDs3ModuleConformance": cnDs3ModuleConformance,
       "cnDs3GeneralDS3Group": cnDs3GeneralDS3Group,
       "cnDs3CN1000Group": cnDs3CN1000Group}
)
