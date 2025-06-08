# SNMP MIB module (GATESAIR-DAB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gatesair_43768/GATESAIR-DAB-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:36 2025
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

(eventCount,
 eventDescription,
 eventPriority,
 eventTimeStamp) = mibBuilder.importSymbols(
    "GATESAIR-COMMONVARBINDS-MIB",
    "eventCount",
    "eventDescription",
    "eventPriority",
    "eventTimeStamp")

(modulations,
 transmissionMibs) = mibBuilder.importSymbols(
    "GATESAIR-SMI",
    "modulations",
    "transmissionMibs")

(OnOff,
 PresentMissing) = mibBuilder.importSymbols(
    "GATESAIR-TC",
    "OnOff",
    "PresentMissing")

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

dabMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dabMibModule.setRevisions(
        ("2016-02-01 13:13",
         "2015-05-11 10:00",
         "2015-02-24 17:12",
         "2014-12-16 14:14",
         "2014-11-21 13:50",
         "2014-11-04 16:27",
         "2014-07-30 12:13")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DabInputType(TextualConvention, Integer32):
    status = "current"
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
        *(("eti1", 1),
          ("eti2", 2),
          ("edi1", 3),
          ("edi2", 4))
    )



class EtiState(TextualConvention, Integer32):
    status = "current"
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
        *(("niPresent", 1),
          ("naPresent", 2),
          ("inputLost", 3),
          ("notActive", 4))
    )



# MIB Managed Objects in the order of their OIDs

_DabMib_ObjectIdentity = ObjectIdentity
dabMib = _DabMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dabMib.setStatus("current")
_DabEvents_ObjectIdentity = ObjectIdentity
dabEvents = _DabEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 1)
)
_DabEventsV2_ObjectIdentity = ObjectIdentity
dabEventsV2 = _DabEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 1, 1)
)
_DabObjects_ObjectIdentity = ObjectIdentity
dabObjects = _DabObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2)
)
_DabMibRevision_Type = DisplayString
_DabMibRevision_Object = MibScalar
dabMibRevision = _DabMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 1),
    _DabMibRevision_Type()
)
dabMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabMibRevision.setStatus("current")
_DabETI1Status_ObjectIdentity = ObjectIdentity
dabETI1Status = _DabETI1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 2)
)
_DabETI1State_Type = EtiState
_DabETI1State_Object = MibScalar
dabETI1State = _DabETI1State_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 2, 1),
    _DabETI1State_Type()
)
dabETI1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI1State.setStatus("current")
_DabETI1TimeStamp_Type = PresentMissing
_DabETI1TimeStamp_Object = MibScalar
dabETI1TimeStamp = _DabETI1TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 2, 2),
    _DabETI1TimeStamp_Type()
)
dabETI1TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI1TimeStamp.setStatus("current")
_DabETI1ByteError10Secs_Type = Integer32
_DabETI1ByteError10Secs_Object = MibScalar
dabETI1ByteError10Secs = _DabETI1ByteError10Secs_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 2, 3),
    _DabETI1ByteError10Secs_Type()
)
dabETI1ByteError10Secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI1ByteError10Secs.setStatus("current")
_DabETI1ByteError1000secs_Type = Integer32
_DabETI1ByteError1000secs_Object = MibScalar
dabETI1ByteError1000secs = _DabETI1ByteError1000secs_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 2, 4),
    _DabETI1ByteError1000secs_Type()
)
dabETI1ByteError1000secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI1ByteError1000secs.setStatus("current")
_DabETI2Status_ObjectIdentity = ObjectIdentity
dabETI2Status = _DabETI2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 3)
)
_DabETI2State_Type = EtiState
_DabETI2State_Object = MibScalar
dabETI2State = _DabETI2State_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 3, 1),
    _DabETI2State_Type()
)
dabETI2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI2State.setStatus("current")
_DabETI2TimeStamp_Type = PresentMissing
_DabETI2TimeStamp_Object = MibScalar
dabETI2TimeStamp = _DabETI2TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 3, 2),
    _DabETI2TimeStamp_Type()
)
dabETI2TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI2TimeStamp.setStatus("current")
_DabETI2ByteError10Secs_Type = Integer32
_DabETI2ByteError10Secs_Object = MibScalar
dabETI2ByteError10Secs = _DabETI2ByteError10Secs_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 3, 3),
    _DabETI2ByteError10Secs_Type()
)
dabETI2ByteError10Secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI2ByteError10Secs.setStatus("current")
_DabETI2ByteError1000Secs_Type = Integer32
_DabETI2ByteError1000Secs_Object = MibScalar
dabETI2ByteError1000Secs = _DabETI2ByteError1000Secs_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 3, 4),
    _DabETI2ByteError1000Secs_Type()
)
dabETI2ByteError1000Secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabETI2ByteError1000Secs.setStatus("current")
_DabGeneral_ObjectIdentity = ObjectIdentity
dabGeneral = _DabGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4)
)
_DabActiveInput_Type = DabInputType
_DabActiveInput_Object = MibScalar
dabActiveInput = _DabActiveInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4, 1),
    _DabActiveInput_Type()
)
dabActiveInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabActiveInput.setStatus("current")


class _DabAuxInput_Type(Integer32):
    """Custom type dabAuxInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eti", 2),
          ("edi", 3))
    )


_DabAuxInput_Type.__name__ = "Integer32"
_DabAuxInput_Object = MibScalar
dabAuxInput = _DabAuxInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4, 2),
    _DabAuxInput_Type()
)
dabAuxInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabAuxInput.setStatus("current")
_DabPowerOnInput_Type = DabInputType
_DabPowerOnInput_Object = MibScalar
dabPowerOnInput = _DabPowerOnInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4, 3),
    _DabPowerOnInput_Type()
)
dabPowerOnInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabPowerOnInput.setStatus("current")


class _DabSwitchingMode_Type(Integer32):
    """Custom type dabSwitchingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_DabSwitchingMode_Type.__name__ = "Integer32"
_DabSwitchingMode_Object = MibScalar
dabSwitchingMode = _DabSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4, 4),
    _DabSwitchingMode_Type()
)
dabSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabSwitchingMode.setStatus("current")


class _DabOFE660Compliance_Type(Integer32):
    """Custom type dabOFE660Compliance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hcast1", 1),
          ("hcast2", 2))
    )


_DabOFE660Compliance_Type.__name__ = "Integer32"
_DabOFE660Compliance_Object = MibScalar
dabOFE660Compliance = _DabOFE660Compliance_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4, 5),
    _DabOFE660Compliance_Type()
)
dabOFE660Compliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabOFE660Compliance.setStatus("current")


class _DabCurrentActiveInput_Type(Integer32):
    """Custom type dabCurrentActiveInput based on Integer32"""
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
        *(("eti1", 1),
          ("eti2", 2),
          ("edi1", 3),
          ("none", 4),
          ("edi2", 5))
    )


_DabCurrentActiveInput_Type.__name__ = "Integer32"
_DabCurrentActiveInput_Object = MibScalar
dabCurrentActiveInput = _DabCurrentActiveInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4, 6),
    _DabCurrentActiveInput_Type()
)
dabCurrentActiveInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabCurrentActiveInput.setStatus("current")


class _DabPrimaryInput_Type(Integer32):
    """Custom type dabPrimaryInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eti", 1),
          ("edi", 2))
    )


_DabPrimaryInput_Type.__name__ = "Integer32"
_DabPrimaryInput_Object = MibScalar
dabPrimaryInput = _DabPrimaryInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 4, 7),
    _DabPrimaryInput_Type()
)
dabPrimaryInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabPrimaryInput.setStatus("current")
_DabNetwork_ObjectIdentity = ObjectIdentity
dabNetwork = _DabNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 5)
)
_DabNetworkStaticDelayComp_Type = Integer32
_DabNetworkStaticDelayComp_Object = MibScalar
dabNetworkStaticDelayComp = _DabNetworkStaticDelayComp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 5, 1),
    _DabNetworkStaticDelayComp_Type()
)
dabNetworkStaticDelayComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dabNetworkStaticDelayComp.setStatus("current")
if mibBuilder.loadTexts:
    dabNetworkStaticDelayComp.setUnits("milliseconds")
_DabETIConfig_ObjectIdentity = ObjectIdentity
dabETIConfig = _DabETIConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 6)
)


class _DabETIDABMode_Type(Integer32):
    """Custom type dabETIDABMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("eti", 2))
    )


_DabETIDABMode_Type.__name__ = "Integer32"
_DabETIDABMode_Object = MibScalar
dabETIDABMode = _DabETIDABMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 6, 1),
    _DabETIDABMode_Type()
)
dabETIDABMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabETIDABMode.setStatus("current")
_DabTII_ObjectIdentity = ObjectIdentity
dabTII = _DabTII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 7)
)
_DabTIIInsertionMode_Type = OnOff
_DabTIIInsertionMode_Object = MibScalar
dabTIIInsertionMode = _DabTIIInsertionMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 7, 1),
    _DabTIIInsertionMode_Type()
)
dabTIIInsertionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabTIIInsertionMode.setStatus("current")
_DabTIIETSICompliance_Type = OnOff
_DabTIIETSICompliance_Object = MibScalar
dabTIIETSICompliance = _DabTIIETSICompliance_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 7, 2),
    _DabTIIETSICompliance_Type()
)
dabTIIETSICompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabTIIETSICompliance.setStatus("current")
_DabEventEnable_ObjectIdentity = ObjectIdentity
dabEventEnable = _DabEventEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 8)
)


class _DabAllEventsEnable_Type(Integer32):
    """Custom type dabAllEventsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("individualEnable", 0),
          ("enableAllEvents", 1),
          ("disableAllEvents", 2))
    )


_DabAllEventsEnable_Type.__name__ = "Integer32"
_DabAllEventsEnable_Object = MibScalar
dabAllEventsEnable = _DabAllEventsEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 8, 1),
    _DabAllEventsEnable_Type()
)
dabAllEventsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabAllEventsEnable.setStatus("current")
_DabETI1PresentEventEnable_Type = TruthValue
_DabETI1PresentEventEnable_Object = MibScalar
dabETI1PresentEventEnable = _DabETI1PresentEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 8, 2),
    _DabETI1PresentEventEnable_Type()
)
dabETI1PresentEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabETI1PresentEventEnable.setStatus("current")
_DabETI1MissingNotActiveEventEnable_Type = TruthValue
_DabETI1MissingNotActiveEventEnable_Object = MibScalar
dabETI1MissingNotActiveEventEnable = _DabETI1MissingNotActiveEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 8, 3),
    _DabETI1MissingNotActiveEventEnable_Type()
)
dabETI1MissingNotActiveEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabETI1MissingNotActiveEventEnable.setStatus("current")
_DabETI2PresentEventEnable_Type = TruthValue
_DabETI2PresentEventEnable_Object = MibScalar
dabETI2PresentEventEnable = _DabETI2PresentEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 8, 4),
    _DabETI2PresentEventEnable_Type()
)
dabETI2PresentEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabETI2PresentEventEnable.setStatus("current")
_DabETI2MissingNotActiveEventEnable_Type = TruthValue
_DabETI2MissingNotActiveEventEnable_Object = MibScalar
dabETI2MissingNotActiveEventEnable = _DabETI2MissingNotActiveEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 8, 5),
    _DabETI2MissingNotActiveEventEnable_Type()
)
dabETI2MissingNotActiveEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabETI2MissingNotActiveEventEnable.setStatus("current")
_DabCurrentActiveInputSwitchEventEnable_Type = TruthValue
_DabCurrentActiveInputSwitchEventEnable_Object = MibScalar
dabCurrentActiveInputSwitchEventEnable = _DabCurrentActiveInputSwitchEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 2, 8, 6),
    _DabCurrentActiveInputSwitchEventEnable_Type()
)
dabCurrentActiveInputSwitchEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dabCurrentActiveInputSwitchEventEnable.setStatus("current")
_DabConformance_ObjectIdentity = ObjectIdentity
dabConformance = _DabConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 4)
)

# Managed Objects groups

dabObjectGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 4, 1)
)
dabObjectGroups.setObjects(
      *(("GATESAIR-DAB-MIB", "dabSwitchingMode"),
        ("GATESAIR-DAB-MIB", "dabAllEventsEnable"),
        ("GATESAIR-DAB-MIB", "dabETI1PresentEventEnable"),
        ("GATESAIR-DAB-MIB", "dabETI2PresentEventEnable"),
        ("GATESAIR-DAB-MIB", "dabMibRevision"),
        ("GATESAIR-DAB-MIB", "dabNetworkStaticDelayComp"),
        ("GATESAIR-DAB-MIB", "dabOFE660Compliance"),
        ("GATESAIR-DAB-MIB", "dabETIDABMode"),
        ("GATESAIR-DAB-MIB", "dabETI1State"),
        ("GATESAIR-DAB-MIB", "dabCurrentActiveInput"),
        ("GATESAIR-DAB-MIB", "dabCurrentActiveInputSwitchEventEnable"),
        ("GATESAIR-DAB-MIB", "dabPrimaryInput"),
        ("GATESAIR-DAB-MIB", "dabETI2State"),
        ("GATESAIR-DAB-MIB", "dabETI1TimeStamp"),
        ("GATESAIR-DAB-MIB", "dabETI1ByteError10Secs"),
        ("GATESAIR-DAB-MIB", "dabETI1ByteError1000secs"),
        ("GATESAIR-DAB-MIB", "dabETI2TimeStamp"),
        ("GATESAIR-DAB-MIB", "dabETI2ByteError10Secs"),
        ("GATESAIR-DAB-MIB", "dabETI2ByteError1000Secs"),
        ("GATESAIR-DAB-MIB", "dabActiveInput"),
        ("GATESAIR-DAB-MIB", "dabAuxInput"),
        ("GATESAIR-DAB-MIB", "dabPowerOnInput"),
        ("GATESAIR-DAB-MIB", "dabTIIInsertionMode"),
        ("GATESAIR-DAB-MIB", "dabTIIETSICompliance"),
        ("GATESAIR-DAB-MIB", "dabETI1MissingNotActiveEventEnable"),
        ("GATESAIR-DAB-MIB", "dabETI2MissingNotActiveEventEnable"))
)
if mibBuilder.loadTexts:
    dabObjectGroups.setStatus("current")


# Notification objects

dabETI1Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 1, 1, 1)
)
dabETI1Present.setObjects(
      *(("GATESAIR-DAB-MIB", "dabETI1State"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    dabETI1Present.setStatus(
        "current"
    )

dabETI1MissingNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 1, 1, 2)
)
dabETI1MissingNotActive.setObjects(
      *(("GATESAIR-DAB-MIB", "dabETI1State"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    dabETI1MissingNotActive.setStatus(
        "current"
    )

dabETI2Present = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 1, 1, 3)
)
dabETI2Present.setObjects(
      *(("GATESAIR-DAB-MIB", "dabETI2State"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    dabETI2Present.setStatus(
        "current"
    )

dabETI2MissingNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 1, 1, 4)
)
dabETI2MissingNotActive.setObjects(
      *(("GATESAIR-DAB-MIB", "dabETI2State"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    dabETI2MissingNotActive.setStatus(
        "current"
    )

dabCurrentActiveInputSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 1, 1, 5)
)
dabCurrentActiveInputSwitch.setObjects(
      *(("GATESAIR-DAB-MIB", "dabCurrentActiveInput"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    dabCurrentActiveInputSwitch.setStatus(
        "current"
    )


# Notifications groups

dabEventsGroups = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 4, 2)
)
dabEventsGroups.setObjects(
      *(("GATESAIR-DAB-MIB", "dabETI1Present"),
        ("GATESAIR-DAB-MIB", "dabETI2Present"),
        ("GATESAIR-DAB-MIB", "dabETI1MissingNotActive"),
        ("GATESAIR-DAB-MIB", "dabETI2MissingNotActive"),
        ("GATESAIR-DAB-MIB", "dabCurrentActiveInputSwitch"))
)
if mibBuilder.loadTexts:
    dabEventsGroups.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dabCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1, 1, 4, 3)
)
dabCompliances.setObjects(
      *(("GATESAIR-DAB-MIB", "dabObjectGroups"),
        ("GATESAIR-DAB-MIB", "dabEventsGroups"))
)
if mibBuilder.loadTexts:
    dabCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GATESAIR-DAB-MIB",
    **{"DabInputType": DabInputType,
       "EtiState": EtiState,
       "dabMibModule": dabMibModule,
       "dabMib": dabMib,
       "dabEvents": dabEvents,
       "dabEventsV2": dabEventsV2,
       "dabETI1Present": dabETI1Present,
       "dabETI1MissingNotActive": dabETI1MissingNotActive,
       "dabETI2Present": dabETI2Present,
       "dabETI2MissingNotActive": dabETI2MissingNotActive,
       "dabCurrentActiveInputSwitch": dabCurrentActiveInputSwitch,
       "dabObjects": dabObjects,
       "dabMibRevision": dabMibRevision,
       "dabETI1Status": dabETI1Status,
       "dabETI1State": dabETI1State,
       "dabETI1TimeStamp": dabETI1TimeStamp,
       "dabETI1ByteError10Secs": dabETI1ByteError10Secs,
       "dabETI1ByteError1000secs": dabETI1ByteError1000secs,
       "dabETI2Status": dabETI2Status,
       "dabETI2State": dabETI2State,
       "dabETI2TimeStamp": dabETI2TimeStamp,
       "dabETI2ByteError10Secs": dabETI2ByteError10Secs,
       "dabETI2ByteError1000Secs": dabETI2ByteError1000Secs,
       "dabGeneral": dabGeneral,
       "dabActiveInput": dabActiveInput,
       "dabAuxInput": dabAuxInput,
       "dabPowerOnInput": dabPowerOnInput,
       "dabSwitchingMode": dabSwitchingMode,
       "dabOFE660Compliance": dabOFE660Compliance,
       "dabCurrentActiveInput": dabCurrentActiveInput,
       "dabPrimaryInput": dabPrimaryInput,
       "dabNetwork": dabNetwork,
       "dabNetworkStaticDelayComp": dabNetworkStaticDelayComp,
       "dabETIConfig": dabETIConfig,
       "dabETIDABMode": dabETIDABMode,
       "dabTII": dabTII,
       "dabTIIInsertionMode": dabTIIInsertionMode,
       "dabTIIETSICompliance": dabTIIETSICompliance,
       "dabEventEnable": dabEventEnable,
       "dabAllEventsEnable": dabAllEventsEnable,
       "dabETI1PresentEventEnable": dabETI1PresentEventEnable,
       "dabETI1MissingNotActiveEventEnable": dabETI1MissingNotActiveEventEnable,
       "dabETI2PresentEventEnable": dabETI2PresentEventEnable,
       "dabETI2MissingNotActiveEventEnable": dabETI2MissingNotActiveEventEnable,
       "dabCurrentActiveInputSwitchEventEnable": dabCurrentActiveInputSwitchEventEnable,
       "dabConformance": dabConformance,
       "dabObjectGroups": dabObjectGroups,
       "dabEventsGroups": dabEventsGroups,
       "dabCompliances": dabCompliances}
)
