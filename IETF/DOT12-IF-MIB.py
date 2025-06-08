# SNMP MIB module (DOT12-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/DOT12-IF-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:30:43 2025
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dot12MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot12MIBObjects_ObjectIdentity = ObjectIdentity
dot12MIBObjects = _Dot12MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 45, 1)
)
_Dot12ConfigTable_Object = MibTable
dot12ConfigTable = _Dot12ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1)
)
if mibBuilder.loadTexts:
    dot12ConfigTable.setStatus("current")
_Dot12ConfigEntry_Object = MibTableRow
dot12ConfigEntry = _Dot12ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1)
)
dot12ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot12ConfigEntry.setStatus("current")


class _Dot12CurrentFramingType_Type(Integer32):
    """Custom type dot12CurrentFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2),
          ("frameTypeUnknown", 3))
    )


_Dot12CurrentFramingType_Type.__name__ = "Integer32"
_Dot12CurrentFramingType_Object = MibTableColumn
dot12CurrentFramingType = _Dot12CurrentFramingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 1),
    _Dot12CurrentFramingType_Type()
)
dot12CurrentFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12CurrentFramingType.setStatus("current")


class _Dot12DesiredFramingType_Type(Integer32):
    """Custom type dot12DesiredFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2),
          ("frameTypeEither", 3))
    )


_Dot12DesiredFramingType_Type.__name__ = "Integer32"
_Dot12DesiredFramingType_Object = MibTableColumn
dot12DesiredFramingType = _Dot12DesiredFramingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 2),
    _Dot12DesiredFramingType_Type()
)
dot12DesiredFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot12DesiredFramingType.setStatus("current")


class _Dot12FramingCapability_Type(Integer32):
    """Custom type dot12FramingCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2),
          ("frameTypeEither", 3))
    )


_Dot12FramingCapability_Type.__name__ = "Integer32"
_Dot12FramingCapability_Object = MibTableColumn
dot12FramingCapability = _Dot12FramingCapability_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 3),
    _Dot12FramingCapability_Type()
)
dot12FramingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12FramingCapability.setStatus("current")


class _Dot12DesiredPromiscStatus_Type(Integer32):
    """Custom type dot12DesiredPromiscStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleAddressMode", 1),
          ("promiscuousMode", 2))
    )


_Dot12DesiredPromiscStatus_Type.__name__ = "Integer32"
_Dot12DesiredPromiscStatus_Object = MibTableColumn
dot12DesiredPromiscStatus = _Dot12DesiredPromiscStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 4),
    _Dot12DesiredPromiscStatus_Type()
)
dot12DesiredPromiscStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot12DesiredPromiscStatus.setStatus("current")


class _Dot12TrainingVersion_Type(Integer32):
    """Custom type dot12TrainingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot12TrainingVersion_Type.__name__ = "Integer32"
_Dot12TrainingVersion_Object = MibTableColumn
dot12TrainingVersion = _Dot12TrainingVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 5),
    _Dot12TrainingVersion_Type()
)
dot12TrainingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12TrainingVersion.setStatus("current")


class _Dot12LastTrainingConfig_Type(OctetString):
    """Custom type dot12LastTrainingConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_Dot12LastTrainingConfig_Type.__name__ = "OctetString"
_Dot12LastTrainingConfig_Object = MibTableColumn
dot12LastTrainingConfig = _Dot12LastTrainingConfig_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 6),
    _Dot12LastTrainingConfig_Type()
)
dot12LastTrainingConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12LastTrainingConfig.setStatus("current")


class _Dot12Commands_Type(Integer32):
    """Custom type dot12Commands based on Integer32"""
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
        *(("noOp", 1),
          ("open", 2),
          ("reset", 3),
          ("close", 4))
    )


_Dot12Commands_Type.__name__ = "Integer32"
_Dot12Commands_Object = MibTableColumn
dot12Commands = _Dot12Commands_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 7),
    _Dot12Commands_Type()
)
dot12Commands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot12Commands.setStatus("current")


class _Dot12Status_Type(Integer32):
    """Custom type dot12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("closed", 2),
          ("opening", 3),
          ("openFailure", 5),
          ("linkFailure", 6))
    )


_Dot12Status_Type.__name__ = "Integer32"
_Dot12Status_Object = MibTableColumn
dot12Status = _Dot12Status_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 8),
    _Dot12Status_Type()
)
dot12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12Status.setStatus("current")


class _Dot12ControlMode_Type(Integer32):
    """Custom type dot12ControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("masterMode", 1),
          ("slaveMode", 2),
          ("learn", 3))
    )


_Dot12ControlMode_Type.__name__ = "Integer32"
_Dot12ControlMode_Object = MibTableColumn
dot12ControlMode = _Dot12ControlMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 9),
    _Dot12ControlMode_Type()
)
dot12ControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot12ControlMode.setStatus("current")
_Dot12StatTable_Object = MibTable
dot12StatTable = _Dot12StatTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2)
)
if mibBuilder.loadTexts:
    dot12StatTable.setStatus("current")
_Dot12StatEntry_Object = MibTableRow
dot12StatEntry = _Dot12StatEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1)
)
dot12StatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot12StatEntry.setStatus("current")
_Dot12InHighPriorityFrames_Type = Counter32
_Dot12InHighPriorityFrames_Object = MibTableColumn
dot12InHighPriorityFrames = _Dot12InHighPriorityFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 1),
    _Dot12InHighPriorityFrames_Type()
)
dot12InHighPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InHighPriorityFrames.setStatus("current")
_Dot12InHighPriorityOctets_Type = Counter32
_Dot12InHighPriorityOctets_Object = MibTableColumn
dot12InHighPriorityOctets = _Dot12InHighPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 2),
    _Dot12InHighPriorityOctets_Type()
)
dot12InHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InHighPriorityOctets.setStatus("current")
_Dot12InNormPriorityFrames_Type = Counter32
_Dot12InNormPriorityFrames_Object = MibTableColumn
dot12InNormPriorityFrames = _Dot12InNormPriorityFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 3),
    _Dot12InNormPriorityFrames_Type()
)
dot12InNormPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InNormPriorityFrames.setStatus("current")
_Dot12InNormPriorityOctets_Type = Counter32
_Dot12InNormPriorityOctets_Object = MibTableColumn
dot12InNormPriorityOctets = _Dot12InNormPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 4),
    _Dot12InNormPriorityOctets_Type()
)
dot12InNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InNormPriorityOctets.setStatus("current")
_Dot12InIPMErrors_Type = Counter32
_Dot12InIPMErrors_Object = MibTableColumn
dot12InIPMErrors = _Dot12InIPMErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 5),
    _Dot12InIPMErrors_Type()
)
dot12InIPMErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InIPMErrors.setStatus("current")
_Dot12InOversizeFrameErrors_Type = Counter32
_Dot12InOversizeFrameErrors_Object = MibTableColumn
dot12InOversizeFrameErrors = _Dot12InOversizeFrameErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 6),
    _Dot12InOversizeFrameErrors_Type()
)
dot12InOversizeFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InOversizeFrameErrors.setStatus("current")
_Dot12InDataErrors_Type = Counter32
_Dot12InDataErrors_Object = MibTableColumn
dot12InDataErrors = _Dot12InDataErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 7),
    _Dot12InDataErrors_Type()
)
dot12InDataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InDataErrors.setStatus("current")
_Dot12InNullAddressedFrames_Type = Counter32
_Dot12InNullAddressedFrames_Object = MibTableColumn
dot12InNullAddressedFrames = _Dot12InNullAddressedFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 8),
    _Dot12InNullAddressedFrames_Type()
)
dot12InNullAddressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12InNullAddressedFrames.setStatus("current")
_Dot12OutHighPriorityFrames_Type = Counter32
_Dot12OutHighPriorityFrames_Object = MibTableColumn
dot12OutHighPriorityFrames = _Dot12OutHighPriorityFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 9),
    _Dot12OutHighPriorityFrames_Type()
)
dot12OutHighPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12OutHighPriorityFrames.setStatus("current")
_Dot12OutHighPriorityOctets_Type = Counter32
_Dot12OutHighPriorityOctets_Object = MibTableColumn
dot12OutHighPriorityOctets = _Dot12OutHighPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 10),
    _Dot12OutHighPriorityOctets_Type()
)
dot12OutHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12OutHighPriorityOctets.setStatus("current")
_Dot12TransitionIntoTrainings_Type = Counter32
_Dot12TransitionIntoTrainings_Object = MibTableColumn
dot12TransitionIntoTrainings = _Dot12TransitionIntoTrainings_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 11),
    _Dot12TransitionIntoTrainings_Type()
)
dot12TransitionIntoTrainings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12TransitionIntoTrainings.setStatus("current")
_Dot12HCInHighPriorityOctets_Type = Counter64
_Dot12HCInHighPriorityOctets_Object = MibTableColumn
dot12HCInHighPriorityOctets = _Dot12HCInHighPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 12),
    _Dot12HCInHighPriorityOctets_Type()
)
dot12HCInHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12HCInHighPriorityOctets.setStatus("current")
_Dot12HCInNormPriorityOctets_Type = Counter64
_Dot12HCInNormPriorityOctets_Object = MibTableColumn
dot12HCInNormPriorityOctets = _Dot12HCInNormPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 13),
    _Dot12HCInNormPriorityOctets_Type()
)
dot12HCInNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12HCInNormPriorityOctets.setStatus("current")
_Dot12HCOutHighPriorityOctets_Type = Counter64
_Dot12HCOutHighPriorityOctets_Object = MibTableColumn
dot12HCOutHighPriorityOctets = _Dot12HCOutHighPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 14),
    _Dot12HCOutHighPriorityOctets_Type()
)
dot12HCOutHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot12HCOutHighPriorityOctets.setStatus("current")
_Dot12Conformance_ObjectIdentity = ObjectIdentity
dot12Conformance = _Dot12Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 45, 2)
)
_Dot12Compliances_ObjectIdentity = ObjectIdentity
dot12Compliances = _Dot12Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 45, 2, 1)
)
_Dot12Groups_ObjectIdentity = ObjectIdentity
dot12Groups = _Dot12Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 45, 2, 2)
)

# Managed Objects groups

dot12ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 45, 2, 2, 1)
)
dot12ConfigGroup.setObjects(
      *(("DOT12-IF-MIB", "dot12DesiredFramingType"),
        ("DOT12-IF-MIB", "dot12FramingCapability"),
        ("DOT12-IF-MIB", "dot12DesiredPromiscStatus"),
        ("DOT12-IF-MIB", "dot12TrainingVersion"),
        ("DOT12-IF-MIB", "dot12LastTrainingConfig"),
        ("DOT12-IF-MIB", "dot12Commands"),
        ("DOT12-IF-MIB", "dot12Status"),
        ("DOT12-IF-MIB", "dot12CurrentFramingType"),
        ("DOT12-IF-MIB", "dot12ControlMode"))
)
if mibBuilder.loadTexts:
    dot12ConfigGroup.setStatus("current")

dot12StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 45, 2, 2, 2)
)
dot12StatsGroup.setObjects(
      *(("DOT12-IF-MIB", "dot12InHighPriorityFrames"),
        ("DOT12-IF-MIB", "dot12InHighPriorityOctets"),
        ("DOT12-IF-MIB", "dot12InNormPriorityFrames"),
        ("DOT12-IF-MIB", "dot12InNormPriorityOctets"),
        ("DOT12-IF-MIB", "dot12InIPMErrors"),
        ("DOT12-IF-MIB", "dot12InOversizeFrameErrors"),
        ("DOT12-IF-MIB", "dot12InDataErrors"),
        ("DOT12-IF-MIB", "dot12InNullAddressedFrames"),
        ("DOT12-IF-MIB", "dot12OutHighPriorityFrames"),
        ("DOT12-IF-MIB", "dot12OutHighPriorityOctets"),
        ("DOT12-IF-MIB", "dot12TransitionIntoTrainings"),
        ("DOT12-IF-MIB", "dot12HCInHighPriorityOctets"),
        ("DOT12-IF-MIB", "dot12HCInNormPriorityOctets"),
        ("DOT12-IF-MIB", "dot12HCOutHighPriorityOctets"))
)
if mibBuilder.loadTexts:
    dot12StatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot12Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 45, 2, 1, 1)
)
dot12Compliance.setObjects(
      *(("DOT12-IF-MIB", "dot12ConfigGroup"),
        ("DOT12-IF-MIB", "dot12StatsGroup"))
)
if mibBuilder.loadTexts:
    dot12Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOT12-IF-MIB",
    **{"dot12MIB": dot12MIB,
       "dot12MIBObjects": dot12MIBObjects,
       "dot12ConfigTable": dot12ConfigTable,
       "dot12ConfigEntry": dot12ConfigEntry,
       "dot12CurrentFramingType": dot12CurrentFramingType,
       "dot12DesiredFramingType": dot12DesiredFramingType,
       "dot12FramingCapability": dot12FramingCapability,
       "dot12DesiredPromiscStatus": dot12DesiredPromiscStatus,
       "dot12TrainingVersion": dot12TrainingVersion,
       "dot12LastTrainingConfig": dot12LastTrainingConfig,
       "dot12Commands": dot12Commands,
       "dot12Status": dot12Status,
       "dot12ControlMode": dot12ControlMode,
       "dot12StatTable": dot12StatTable,
       "dot12StatEntry": dot12StatEntry,
       "dot12InHighPriorityFrames": dot12InHighPriorityFrames,
       "dot12InHighPriorityOctets": dot12InHighPriorityOctets,
       "dot12InNormPriorityFrames": dot12InNormPriorityFrames,
       "dot12InNormPriorityOctets": dot12InNormPriorityOctets,
       "dot12InIPMErrors": dot12InIPMErrors,
       "dot12InOversizeFrameErrors": dot12InOversizeFrameErrors,
       "dot12InDataErrors": dot12InDataErrors,
       "dot12InNullAddressedFrames": dot12InNullAddressedFrames,
       "dot12OutHighPriorityFrames": dot12OutHighPriorityFrames,
       "dot12OutHighPriorityOctets": dot12OutHighPriorityOctets,
       "dot12TransitionIntoTrainings": dot12TransitionIntoTrainings,
       "dot12HCInHighPriorityOctets": dot12HCInHighPriorityOctets,
       "dot12HCInNormPriorityOctets": dot12HCInNormPriorityOctets,
       "dot12HCOutHighPriorityOctets": dot12HCOutHighPriorityOctets,
       "dot12Conformance": dot12Conformance,
       "dot12Compliances": dot12Compliances,
       "dot12Compliance": dot12Compliance,
       "dot12Groups": dot12Groups,
       "dot12ConfigGroup": dot12ConfigGroup,
       "dot12StatsGroup": dot12StatsGroup}
)
