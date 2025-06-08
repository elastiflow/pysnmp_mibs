# SNMP MIB module (PEAKVGU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKVGU-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(OnOffType,
 YesNoType,
 converters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "OnOffType",
    "YesNoType",
    "converters")

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

peakVGUModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14)
)
if mibBuilder.loadTexts:
    peakVGUModule.setRevisions(
        ("2015-09-15 10:00",
         "2014-08-22 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VGUChannelStateType(TextualConvention, Integer32):
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
        *(("present", 1),
          ("initialising", 2),
          ("missing", 3))
    )



class VGUBypassStateType(TextualConvention, Integer32):
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
        *(("off", 1),
          ("on", 2),
          ("missing", 3))
    )



# MIB Managed Objects in the order of their OIDs

_VguCTable_Object = MibTable
vguCTable = _VguCTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    vguCTable.setStatus("current")
_VguCTableEntry_Object = MibTableRow
vguCTableEntry = _VguCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1, 1)
)
vguCTableEntry.setIndexNames(
    (0, "PEAKVGU-MIB", "vguCIndex"),
)
if mibBuilder.loadTexts:
    vguCTableEntry.setStatus("current")


class _VguCIndex_Type(Integer32):
    """Custom type vguCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VguCIndex_Type.__name__ = "Integer32"
_VguCIndex_Object = MibTableColumn
vguCIndex = _VguCIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1, 1, 1),
    _VguCIndex_Type()
)
vguCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vguCIndex.setStatus("current")
_VguCChannelNo_Type = Integer32
_VguCChannelNo_Object = MibTableColumn
vguCChannelNo = _VguCChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1, 1, 2),
    _VguCChannelNo_Type()
)
vguCChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vguCChannelNo.setStatus("current")
_VguCState_Type = VGUChannelStateType
_VguCState_Object = MibTableColumn
vguCState = _VguCState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1, 1, 3),
    _VguCState_Type()
)
vguCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vguCState.setStatus("current")
_VguCAttenuation_Type = OctetString
_VguCAttenuation_Object = MibTableColumn
vguCAttenuation = _VguCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1, 1, 4),
    _VguCAttenuation_Type()
)
vguCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vguCAttenuation.setStatus("current")
_VguCReqAttenuation_Type = OctetString
_VguCReqAttenuation_Object = MibTableColumn
vguCReqAttenuation = _VguCReqAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1, 1, 5),
    _VguCReqAttenuation_Type()
)
vguCReqAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vguCReqAttenuation.setStatus("current")
_VguCBypass_Type = VGUBypassStateType
_VguCBypass_Object = MibTableColumn
vguCBypass = _VguCBypass_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 1, 1, 6),
    _VguCBypass_Type()
)
vguCBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vguCBypass.setStatus("current")
_VguPTable_Object = MibTable
vguPTable = _VguPTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    vguPTable.setStatus("current")
_VguPTableEntry_Object = MibTableRow
vguPTableEntry = _VguPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 2, 1)
)
vguPTableEntry.setIndexNames(
    (0, "PEAKVGU-MIB", "vguPIndex"),
)
if mibBuilder.loadTexts:
    vguPTableEntry.setStatus("current")


class _VguPIndex_Type(Integer32):
    """Custom type vguPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VguPIndex_Type.__name__ = "Integer32"
_VguPIndex_Object = MibTableColumn
vguPIndex = _VguPIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 2, 1, 1),
    _VguPIndex_Type()
)
vguPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vguPIndex.setStatus("current")
_VguPPresent_Type = YesNoType
_VguPPresent_Object = MibTableColumn
vguPPresent = _VguPPresent_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 2, 1, 2),
    _VguPPresent_Type()
)
vguPPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vguPPresent.setStatus("current")
_VguPPowered_Type = YesNoType
_VguPPowered_Object = MibTableColumn
vguPPowered = _VguPPowered_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 2, 1, 3),
    _VguPPowered_Type()
)
vguPPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vguPPowered.setStatus("current")
_VguIntegers_ObjectIdentity = ObjectIdentity
vguIntegers = _VguIntegers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 109)
)
_VguConvGroups_ObjectIdentity = ObjectIdentity
vguConvGroups = _VguConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 110)
)
_VguConvConformance_ObjectIdentity = ObjectIdentity
vguConvConformance = _VguConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 111)
)

# Managed Objects groups

vguCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 110, 1)
)
vguCNFReqGrp.setObjects(
      *(("PEAKVGU-MIB", "vguPPresent"),
        ("PEAKVGU-MIB", "vguPPowered"),
        ("PEAKVGU-MIB", "vguCChannelNo"),
        ("PEAKVGU-MIB", "vguCState"))
)
if mibBuilder.loadTexts:
    vguCNFReqGrp.setStatus("current")

vguCNFAttenuationGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 110, 2)
)
vguCNFAttenuationGrp.setObjects(
      *(("PEAKVGU-MIB", "vguCAttenuation"),
        ("PEAKVGU-MIB", "vguCReqAttenuation"))
)
if mibBuilder.loadTexts:
    vguCNFAttenuationGrp.setStatus("current")

vguCNFBypassGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 110, 3)
)
vguCNFBypassGrp.setObjects(
    ("PEAKVGU-MIB", "vguCBypass")
)
if mibBuilder.loadTexts:
    vguCNFBypassGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vguCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 14, 111, 1)
)
vguCNFCompliance.setObjects(
      *(("PEAKVGU-MIB", "vguCNFReqGrp"),
        ("PEAKVGU-MIB", "vguCNFAttenuationGrp"),
        ("PEAKVGU-MIB", "vguCNFBypassGrp"))
)
if mibBuilder.loadTexts:
    vguCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKVGU-MIB",
    **{"VGUChannelStateType": VGUChannelStateType,
       "VGUBypassStateType": VGUBypassStateType,
       "peakVGUModule": peakVGUModule,
       "vguCTable": vguCTable,
       "vguCTableEntry": vguCTableEntry,
       "vguCIndex": vguCIndex,
       "vguCChannelNo": vguCChannelNo,
       "vguCState": vguCState,
       "vguCAttenuation": vguCAttenuation,
       "vguCReqAttenuation": vguCReqAttenuation,
       "vguCBypass": vguCBypass,
       "vguPTable": vguPTable,
       "vguPTableEntry": vguPTableEntry,
       "vguPIndex": vguPIndex,
       "vguPPresent": vguPPresent,
       "vguPPowered": vguPPowered,
       "vguIntegers": vguIntegers,
       "vguConvGroups": vguConvGroups,
       "vguCNFReqGrp": vguCNFReqGrp,
       "vguCNFAttenuationGrp": vguCNFAttenuationGrp,
       "vguCNFBypassGrp": vguCNFBypassGrp,
       "vguConvConformance": vguConvConformance,
       "vguCNFCompliance": vguCNFCompliance}
)
