# SNMP MIB module (TROPIC-OTUODU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-OTUODU-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(tnOtuOduMIB,
 tnPortModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnOtuOduMIB",
    "tnPortModules")

(AluWdmEnabledDisabled,
 AluWdmFecMode,
 AluWdmOdukStatus,
 AluWdmPortOchOtuRate,
 AluWdmTtiStatus,
 TnCommand,
 TropicOperationalCapabilityType,
 TropicStateQualifierType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmEnabledDisabled",
    "AluWdmFecMode",
    "AluWdmOdukStatus",
    "AluWdmPortOchOtuRate",
    "AluWdmTtiStatus",
    "TnCommand",
    "TropicOperationalCapabilityType",
    "TropicStateQualifierType")


# MODULE-IDENTITY

tnOtuOduMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tnOtuOduMibModule.setRevisions(
        ("2010-11-14 12:00",
         "2010-11-22 12:00",
         "2010-11-24 12:00",
         "2011-02-23 12:00",
         "2011-03-04 12:00",
         "2011-03-30 12:00",
         "2011-04-25 12:00",
         "2011-07-22 12:00",
         "2012-04-10 12:00",
         "2012-08-22 12:00",
         "2012-09-24 12:00",
         "2012-09-28 12:00",
         "2012-10-22 12:00",
         "2012-12-05 12:00",
         "2013-03-14 12:00",
         "2013-04-16 12:00",
         "2014-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnOtuOduConf_ObjectIdentity = ObjectIdentity
tnOtuOduConf = _TnOtuOduConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1)
)
_TnOtuOduGroups_ObjectIdentity = ObjectIdentity
tnOtuOduGroups = _TnOtuOduGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1)
)
_TnOtuOduCompliances_ObjectIdentity = ObjectIdentity
tnOtuOduCompliances = _TnOtuOduCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 2)
)
_TnOtuOduObjs_ObjectIdentity = ObjectIdentity
tnOtuOduObjs = _TnOtuOduObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2)
)
_TnOtuOduBasics_ObjectIdentity = ObjectIdentity
tnOtuOduBasics = _TnOtuOduBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1)
)
_TnOtukTable_Object = MibTable
tnOtukTable = _TnOtukTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnOtukTable.setStatus("current")
_TnOtukEntry_Object = MibTableRow
tnOtukEntry = _TnOtukEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1)
)
tnOtukEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOtukEntry.setStatus("current")


class _TnOtukTtiStatus_Type(AluWdmTtiStatus):
    """Custom type tnOtukTtiStatus based on AluWdmTtiStatus"""
    defaultValue = 4


_TnOtukTtiStatus_Type.__name__ = "AluWdmTtiStatus"
_TnOtukTtiStatus_Object = MibTableColumn
tnOtukTtiStatus = _TnOtukTtiStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 1),
    _TnOtukTtiStatus_Type()
)
tnOtukTtiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukTtiStatus.setStatus("current")


class _TnOtukFecMode_Type(AluWdmFecMode):
    """Custom type tnOtukFecMode based on AluWdmFecMode"""
    defaultValue = 3


_TnOtukFecMode_Type.__name__ = "AluWdmFecMode"
_TnOtukFecMode_Object = MibTableColumn
tnOtukFecMode = _TnOtukFecMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 2),
    _TnOtukFecMode_Type()
)
tnOtukFecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukFecMode.setStatus("current")


class _TnOtukRate_Type(AluWdmPortOchOtuRate):
    """Custom type tnOtukRate based on AluWdmPortOchOtuRate"""
    defaultValue = 1


_TnOtukRate_Type.__name__ = "AluWdmPortOchOtuRate"
_TnOtukRate_Object = MibTableColumn
tnOtukRate = _TnOtukRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 3),
    _TnOtukRate_Type()
)
tnOtukRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukRate.setStatus("current")


class _TnOtukIncRes_Type(OctetString):
    """Custom type tnOtukIncRes based on OctetString"""
    defaultValue = OctetString("")


_TnOtukIncRes_Type.__name__ = "OctetString"
_TnOtukIncRes_Object = MibTableColumn
tnOtukIncRes = _TnOtukIncRes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 4),
    _TnOtukIncRes_Type()
)
tnOtukIncRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukIncRes.setStatus("current")


class _TnOtukAdminStatus_Type(AluWdmOdukStatus):
    """Custom type tnOtukAdminStatus based on AluWdmOdukStatus"""
    defaultValue = 2


_TnOtukAdminStatus_Type.__name__ = "AluWdmOdukStatus"
_TnOtukAdminStatus_Object = MibTableColumn
tnOtukAdminStatus = _TnOtukAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 5),
    _TnOtukAdminStatus_Type()
)
tnOtukAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukAdminStatus.setStatus("current")


class _TnOtukStateAINS_Type(TruthValue):
    """Custom type tnOtukStateAINS based on TruthValue"""
    defaultValue = 2


_TnOtukStateAINS_Type.__name__ = "TruthValue"
_TnOtukStateAINS_Object = MibTableColumn
tnOtukStateAINS = _TnOtukStateAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 6),
    _TnOtukStateAINS_Type()
)
tnOtukStateAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukStateAINS.setStatus("current")


class _TnOtukOperStatus_Type(AluWdmOdukStatus):
    """Custom type tnOtukOperStatus based on AluWdmOdukStatus"""
    defaultValue = 2


_TnOtukOperStatus_Type.__name__ = "AluWdmOdukStatus"
_TnOtukOperStatus_Object = MibTableColumn
tnOtukOperStatus = _TnOtukOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 7),
    _TnOtukOperStatus_Type()
)
tnOtukOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukOperStatus.setStatus("current")
_TnOtukStateQualifier_Type = TropicStateQualifierType
_TnOtukStateQualifier_Object = MibTableColumn
tnOtukStateQualifier = _TnOtukStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 8),
    _TnOtukStateQualifier_Type()
)
tnOtukStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukStateQualifier.setStatus("current")


class _TnOtukOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnOtukOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnOtukOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnOtukOperationalCapability_Object = MibTableColumn
tnOtukOperationalCapability = _TnOtukOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 9),
    _TnOtukOperationalCapability_Type()
)
tnOtukOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukOperationalCapability.setStatus("current")
_TnOtukAINSDebounceTime_Type = Integer32
_TnOtukAINSDebounceTime_Object = MibTableColumn
tnOtukAINSDebounceTime = _TnOtukAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 10),
    _TnOtukAINSDebounceTime_Type()
)
tnOtukAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukAINSDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tnOtukAINSDebounceTime.setUnits("Seconds")
_TnOtukUsingSysAINSDebounceTime_Type = TruthValue
_TnOtukUsingSysAINSDebounceTime_Object = MibTableColumn
tnOtukUsingSysAINSDebounceTime = _TnOtukUsingSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 11),
    _TnOtukUsingSysAINSDebounceTime_Type()
)
tnOtukUsingSysAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukUsingSysAINSDebounceTime.setStatus("current")


class _TnOtukAINSDebounceTimeRemaining_Type(Unsigned32):
    """Custom type tnOtukAINSDebounceTimeRemaining based on Unsigned32"""
    defaultValue = 0


_TnOtukAINSDebounceTimeRemaining_Type.__name__ = "Unsigned32"
_TnOtukAINSDebounceTimeRemaining_Object = MibTableColumn
tnOtukAINSDebounceTimeRemaining = _TnOtukAINSDebounceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 12),
    _TnOtukAINSDebounceTimeRemaining_Type()
)
tnOtukAINSDebounceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukAINSDebounceTimeRemaining.setStatus("current")
_TnOtukPreFec_Type = Counter64
_TnOtukPreFec_Object = MibTableColumn
tnOtukPreFec = _TnOtukPreFec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 14),
    _TnOtukPreFec_Type()
)
tnOtukPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukPreFec.setStatus("current")
_TnOtukPostFec_Type = Counter64
_TnOtukPostFec_Object = MibTableColumn
tnOtukPostFec = _TnOtukPostFec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 15),
    _TnOtukPostFec_Type()
)
tnOtukPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukPostFec.setStatus("current")


class _TnOtukAsymInterworking_Type(TruthValue):
    """Custom type tnOtukAsymInterworking based on TruthValue"""
    defaultValue = 2


_TnOtukAsymInterworking_Type.__name__ = "TruthValue"
_TnOtukAsymInterworking_Object = MibTableColumn
tnOtukAsymInterworking = _TnOtukAsymInterworking_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 17),
    _TnOtukAsymInterworking_Type()
)
tnOtukAsymInterworking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukAsymInterworking.setStatus("current")

# Managed Objects groups

tnOtukGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1, 1)
)
tnOtukGroup.setObjects(
      *(("TROPIC-OTUODU-MIB", "tnOtukTtiStatus"),
        ("TROPIC-OTUODU-MIB", "tnOtukFecMode"),
        ("TROPIC-OTUODU-MIB", "tnOtukRate"),
        ("TROPIC-OTUODU-MIB", "tnOtukIncRes"),
        ("TROPIC-OTUODU-MIB", "tnOtukAdminStatus"),
        ("TROPIC-OTUODU-MIB", "tnOtukStateAINS"),
        ("TROPIC-OTUODU-MIB", "tnOtukOperStatus"),
        ("TROPIC-OTUODU-MIB", "tnOtukStateQualifier"),
        ("TROPIC-OTUODU-MIB", "tnOtukOperationalCapability"),
        ("TROPIC-OTUODU-MIB", "tnOtukAINSDebounceTime"),
        ("TROPIC-OTUODU-MIB", "tnOtukUsingSysAINSDebounceTime"),
        ("TROPIC-OTUODU-MIB", "tnOtukAINSDebounceTimeRemaining"),
        ("TROPIC-OTUODU-MIB", "tnOtukPreFec"),
        ("TROPIC-OTUODU-MIB", "tnOtukPostFec"),
        ("TROPIC-OTUODU-MIB", "tnOtukAsymInterworking"))
)
if mibBuilder.loadTexts:
    tnOtukGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnOdukCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 2, 1)
)
tnOdukCompliance.setObjects(
    ("TROPIC-OTUODU-MIB", "tnOtukGroup")
)
if mibBuilder.loadTexts:
    tnOdukCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-OTUODU-MIB",
    **{"tnOtuOduMibModule": tnOtuOduMibModule,
       "tnOtuOduConf": tnOtuOduConf,
       "tnOtuOduGroups": tnOtuOduGroups,
       "tnOtukGroup": tnOtukGroup,
       "tnOtuOduCompliances": tnOtuOduCompliances,
       "tnOdukCompliance": tnOdukCompliance,
       "tnOtuOduObjs": tnOtuOduObjs,
       "tnOtuOduBasics": tnOtuOduBasics,
       "tnOtukTable": tnOtukTable,
       "tnOtukEntry": tnOtukEntry,
       "tnOtukTtiStatus": tnOtukTtiStatus,
       "tnOtukFecMode": tnOtukFecMode,
       "tnOtukRate": tnOtukRate,
       "tnOtukIncRes": tnOtukIncRes,
       "tnOtukAdminStatus": tnOtukAdminStatus,
       "tnOtukStateAINS": tnOtukStateAINS,
       "tnOtukOperStatus": tnOtukOperStatus,
       "tnOtukStateQualifier": tnOtukStateQualifier,
       "tnOtukOperationalCapability": tnOtukOperationalCapability,
       "tnOtukAINSDebounceTime": tnOtukAINSDebounceTime,
       "tnOtukUsingSysAINSDebounceTime": tnOtukUsingSysAINSDebounceTime,
       "tnOtukAINSDebounceTimeRemaining": tnOtukAINSDebounceTimeRemaining,
       "tnOtukPreFec": tnOtukPreFec,
       "tnOtukPostFec": tnOtukPostFec,
       "tnOtukAsymInterworking": tnOtukAsymInterworking}
)
