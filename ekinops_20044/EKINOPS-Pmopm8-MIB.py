# SNMP MIB module (EKINOPS-Pmopm8-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmopm8-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:49 2025
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

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

modulePmopm8 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66)
)
if mibBuilder.loadTexts:
    modulePmopm8.setRevisions(
        ("2014-07-28 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmopm8Grid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("grid50", 50),
          ("grid100", 100),
          ("grid200", 200))
    )



class Pmopm8MultiRate(TextualConvention, Integer32):
    status = "current"


class Pmopm8OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pmopm8AdjustValue(TextualConvention, Integer32):
    status = "current"


class Pmopm8OtxMode(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pmopm8alarms_ObjectIdentity = ObjectIdentity
pmopm8alarms = _Pmopm8alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2)
)
_Pmopm8AlmOther_ObjectIdentity = ObjectIdentity
pmopm8AlmOther = _Pmopm8AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1)
)
_Pmopm8AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmopm8AlmOtherNurg = _Pmopm8AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 1)
)
_Pmopm8AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmopm8AlmsynthAlm2 = _Pmopm8AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 1, 2)
)
_Pmopm8AlmConfTableSave_Type = EkiOnOff
_Pmopm8AlmConfTableSave_Object = MibScalar
pmopm8AlmConfTableSave = _Pmopm8AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 1, 2, 1),
    _Pmopm8AlmConfTableSave_Type()
)
pmopm8AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmConfTableSave.setStatus("current")
_Pmopm8AlmInvUpload_Type = EkiOnOff
_Pmopm8AlmInvUpload_Object = MibScalar
pmopm8AlmInvUpload = _Pmopm8AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 1, 2, 2),
    _Pmopm8AlmInvUpload_Type()
)
pmopm8AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmInvUpload.setStatus("current")
_Pmopm8AlmConfTableLoad_Type = EkiOnOff
_Pmopm8AlmConfTableLoad_Object = MibScalar
pmopm8AlmConfTableLoad = _Pmopm8AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 1, 2, 3),
    _Pmopm8AlmConfTableLoad_Type()
)
pmopm8AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmConfTableLoad.setStatus("current")
_Pmopm8AlmCorrelatOff_Type = EkiOnOff
_Pmopm8AlmCorrelatOff_Object = MibScalar
pmopm8AlmCorrelatOff = _Pmopm8AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 1, 2, 4),
    _Pmopm8AlmCorrelatOff_Type()
)
pmopm8AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmCorrelatOff.setStatus("current")
_Pmopm8AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmopm8AlmOtherUrg = _Pmopm8AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 2)
)
_Pmopm8AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmopm8AlmOtherCrit = _Pmopm8AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 3)
)
_Pmopm8AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmopm8AlmsynthAlm0 = _Pmopm8AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 3, 0)
)
_Pmopm8AlmModGlobFail_Type = EkiOnOff
_Pmopm8AlmModGlobFail_Object = MibScalar
pmopm8AlmModGlobFail = _Pmopm8AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 3, 0, 9),
    _Pmopm8AlmModGlobFail_Type()
)
pmopm8AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmModGlobFail.setStatus("current")
_Pmopm8AlmDefFuseA_Type = EkiOnOff
_Pmopm8AlmDefFuseA_Object = MibScalar
pmopm8AlmDefFuseA = _Pmopm8AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 3, 0, 15),
    _Pmopm8AlmDefFuseA_Type()
)
pmopm8AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmDefFuseA.setStatus("current")
_Pmopm8AlmDefFuseB_Type = EkiOnOff
_Pmopm8AlmDefFuseB_Object = MibScalar
pmopm8AlmDefFuseB = _Pmopm8AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 1, 3, 0, 16),
    _Pmopm8AlmDefFuseB_Type()
)
pmopm8AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmDefFuseB.setStatus("current")
_Pmopm8AlmClient_ObjectIdentity = ObjectIdentity
pmopm8AlmClient = _Pmopm8AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2)
)
_Pmopm8AlmClientNurg_ObjectIdentity = ObjectIdentity
pmopm8AlmClientNurg = _Pmopm8AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 1)
)
_Pmopm8AlmClientUrg_ObjectIdentity = ObjectIdentity
pmopm8AlmClientUrg = _Pmopm8AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 2)
)
_Pmopm8AlmClientCrit_ObjectIdentity = ObjectIdentity
pmopm8AlmClientCrit = _Pmopm8AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3)
)
_Pmopm8AlmsynthAlmPortTable_Object = MibTable
pmopm8AlmsynthAlmPortTable = _Pmopm8AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmopm8AlmsynthAlmPortTable.setStatus("current")
_Pmopm8AlmsynthAlmPortEntry_Object = MibTableRow
pmopm8AlmsynthAlmPortEntry = _Pmopm8AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 8, 1)
)
pmopm8AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8AlmsynthAlmPortEntry.setStatus("current")


class _Pmopm8AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pmopm8AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pmopm8AlmsynthAlmPortIndex_Object = MibTableColumn
pmopm8AlmsynthAlmPortIndex = _Pmopm8AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 8, 1, 1),
    _Pmopm8AlmsynthAlmPortIndex_Type()
)
pmopm8AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmsynthAlmPortIndex.setStatus("current")
_Pmopm8AlmSpectrumAbsentPortn_Type = EkiOnOff
_Pmopm8AlmSpectrumAbsentPortn_Object = MibTableColumn
pmopm8AlmSpectrumAbsentPortn = _Pmopm8AlmSpectrumAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 8, 1, 2),
    _Pmopm8AlmSpectrumAbsentPortn_Type()
)
pmopm8AlmSpectrumAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmSpectrumAbsentPortn.setStatus("current")
_Pmopm8AlmSpectrumOosPortn_Type = EkiOnOff
_Pmopm8AlmSpectrumOosPortn_Object = MibTableColumn
pmopm8AlmSpectrumOosPortn = _Pmopm8AlmSpectrumOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 8, 1, 3),
    _Pmopm8AlmSpectrumOosPortn_Type()
)
pmopm8AlmSpectrumOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmSpectrumOosPortn.setStatus("current")
_Pmopm8AlmSpectrumInvalidDataPortn_Type = EkiOnOff
_Pmopm8AlmSpectrumInvalidDataPortn_Object = MibTableColumn
pmopm8AlmSpectrumInvalidDataPortn = _Pmopm8AlmSpectrumInvalidDataPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 8, 1, 4),
    _Pmopm8AlmSpectrumInvalidDataPortn_Type()
)
pmopm8AlmSpectrumInvalidDataPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmSpectrumInvalidDataPortn.setStatus("current")
_Pmopm8Almchannel1PortTable_Object = MibTable
pmopm8Almchannel1PortTable = _Pmopm8Almchannel1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel1PortTable.setStatus("current")
_Pmopm8Almchannel1PortEntry_Object = MibTableRow
pmopm8Almchannel1PortEntry = _Pmopm8Almchannel1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1)
)
pmopm8Almchannel1PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel1PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel1PortEntry.setStatus("current")


class _Pmopm8Almchannel1PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel1PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel1PortIndex_Object = MibTableColumn
pmopm8Almchannel1PortIndex = _Pmopm8Almchannel1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1, 1),
    _Pmopm8Almchannel1PortIndex_Type()
)
pmopm8Almchannel1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel1PortIndex.setStatus("current")
_Pmopm8AlmChannel1AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel1AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel1AbsentPortn = _Pmopm8AlmChannel1AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1, 2),
    _Pmopm8AlmChannel1AbsentPortn_Type()
)
pmopm8AlmChannel1AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel1AbsentPortn.setStatus("current")
_Pmopm8AlmChannel1MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel1MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel1MismatchPortn = _Pmopm8AlmChannel1MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1, 3),
    _Pmopm8AlmChannel1MismatchPortn_Type()
)
pmopm8AlmChannel1MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel1MismatchPortn.setStatus("current")
_Pmopm8AlmChannel1BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel1BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel1BalancedPortn = _Pmopm8AlmChannel1BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1, 4),
    _Pmopm8AlmChannel1BalancedPortn_Type()
)
pmopm8AlmChannel1BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel1BalancedPortn.setStatus("current")
_Pmopm8AlmChannel1PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel1PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel1PowerLowPortn = _Pmopm8AlmChannel1PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1, 5),
    _Pmopm8AlmChannel1PowerLowPortn_Type()
)
pmopm8AlmChannel1PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel1PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel1PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel1PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel1PowerHighPortn = _Pmopm8AlmChannel1PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1, 6),
    _Pmopm8AlmChannel1PowerHighPortn_Type()
)
pmopm8AlmChannel1PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel1PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel1OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel1OosPortn_Object = MibTableColumn
pmopm8AlmChannel1OosPortn = _Pmopm8AlmChannel1OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 16, 1, 7),
    _Pmopm8AlmChannel1OosPortn_Type()
)
pmopm8AlmChannel1OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel1OosPortn.setStatus("current")
_Pmopm8Almchannel2PortTable_Object = MibTable
pmopm8Almchannel2PortTable = _Pmopm8Almchannel2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel2PortTable.setStatus("current")
_Pmopm8Almchannel2PortEntry_Object = MibTableRow
pmopm8Almchannel2PortEntry = _Pmopm8Almchannel2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1)
)
pmopm8Almchannel2PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel2PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel2PortEntry.setStatus("current")


class _Pmopm8Almchannel2PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel2PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel2PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel2PortIndex_Object = MibTableColumn
pmopm8Almchannel2PortIndex = _Pmopm8Almchannel2PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1, 1),
    _Pmopm8Almchannel2PortIndex_Type()
)
pmopm8Almchannel2PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel2PortIndex.setStatus("current")
_Pmopm8AlmChannel2AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel2AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel2AbsentPortn = _Pmopm8AlmChannel2AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1, 2),
    _Pmopm8AlmChannel2AbsentPortn_Type()
)
pmopm8AlmChannel2AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel2AbsentPortn.setStatus("current")
_Pmopm8AlmChannel2MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel2MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel2MismatchPortn = _Pmopm8AlmChannel2MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1, 3),
    _Pmopm8AlmChannel2MismatchPortn_Type()
)
pmopm8AlmChannel2MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel2MismatchPortn.setStatus("current")
_Pmopm8AlmChannel2BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel2BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel2BalancedPortn = _Pmopm8AlmChannel2BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1, 4),
    _Pmopm8AlmChannel2BalancedPortn_Type()
)
pmopm8AlmChannel2BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel2BalancedPortn.setStatus("current")
_Pmopm8AlmChannel2PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel2PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel2PowerLowPortn = _Pmopm8AlmChannel2PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1, 5),
    _Pmopm8AlmChannel2PowerLowPortn_Type()
)
pmopm8AlmChannel2PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel2PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel2PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel2PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel2PowerHighPortn = _Pmopm8AlmChannel2PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1, 6),
    _Pmopm8AlmChannel2PowerHighPortn_Type()
)
pmopm8AlmChannel2PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel2PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel2OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel2OosPortn_Object = MibTableColumn
pmopm8AlmChannel2OosPortn = _Pmopm8AlmChannel2OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 24, 1, 7),
    _Pmopm8AlmChannel2OosPortn_Type()
)
pmopm8AlmChannel2OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel2OosPortn.setStatus("current")
_Pmopm8Almchannel3PortTable_Object = MibTable
pmopm8Almchannel3PortTable = _Pmopm8Almchannel3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel3PortTable.setStatus("current")
_Pmopm8Almchannel3PortEntry_Object = MibTableRow
pmopm8Almchannel3PortEntry = _Pmopm8Almchannel3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1)
)
pmopm8Almchannel3PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel3PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel3PortEntry.setStatus("current")


class _Pmopm8Almchannel3PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel3PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel3PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel3PortIndex_Object = MibTableColumn
pmopm8Almchannel3PortIndex = _Pmopm8Almchannel3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1, 1),
    _Pmopm8Almchannel3PortIndex_Type()
)
pmopm8Almchannel3PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel3PortIndex.setStatus("current")
_Pmopm8AlmChannel3AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel3AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel3AbsentPortn = _Pmopm8AlmChannel3AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1, 2),
    _Pmopm8AlmChannel3AbsentPortn_Type()
)
pmopm8AlmChannel3AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel3AbsentPortn.setStatus("current")
_Pmopm8AlmChannel3MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel3MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel3MismatchPortn = _Pmopm8AlmChannel3MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1, 3),
    _Pmopm8AlmChannel3MismatchPortn_Type()
)
pmopm8AlmChannel3MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel3MismatchPortn.setStatus("current")
_Pmopm8AlmChannel3BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel3BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel3BalancedPortn = _Pmopm8AlmChannel3BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1, 4),
    _Pmopm8AlmChannel3BalancedPortn_Type()
)
pmopm8AlmChannel3BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel3BalancedPortn.setStatus("current")
_Pmopm8AlmChannel3PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel3PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel3PowerLowPortn = _Pmopm8AlmChannel3PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1, 5),
    _Pmopm8AlmChannel3PowerLowPortn_Type()
)
pmopm8AlmChannel3PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel3PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel3PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel3PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel3PowerHighPortn = _Pmopm8AlmChannel3PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1, 6),
    _Pmopm8AlmChannel3PowerHighPortn_Type()
)
pmopm8AlmChannel3PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel3PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel3OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel3OosPortn_Object = MibTableColumn
pmopm8AlmChannel3OosPortn = _Pmopm8AlmChannel3OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 32, 1, 7),
    _Pmopm8AlmChannel3OosPortn_Type()
)
pmopm8AlmChannel3OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel3OosPortn.setStatus("current")
_Pmopm8Almchannel4PortTable_Object = MibTable
pmopm8Almchannel4PortTable = _Pmopm8Almchannel4PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel4PortTable.setStatus("current")
_Pmopm8Almchannel4PortEntry_Object = MibTableRow
pmopm8Almchannel4PortEntry = _Pmopm8Almchannel4PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1)
)
pmopm8Almchannel4PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel4PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel4PortEntry.setStatus("current")


class _Pmopm8Almchannel4PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel4PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel4PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel4PortIndex_Object = MibTableColumn
pmopm8Almchannel4PortIndex = _Pmopm8Almchannel4PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1, 1),
    _Pmopm8Almchannel4PortIndex_Type()
)
pmopm8Almchannel4PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel4PortIndex.setStatus("current")
_Pmopm8AlmChannel4AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel4AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel4AbsentPortn = _Pmopm8AlmChannel4AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1, 2),
    _Pmopm8AlmChannel4AbsentPortn_Type()
)
pmopm8AlmChannel4AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel4AbsentPortn.setStatus("current")
_Pmopm8AlmChannel4MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel4MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel4MismatchPortn = _Pmopm8AlmChannel4MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1, 3),
    _Pmopm8AlmChannel4MismatchPortn_Type()
)
pmopm8AlmChannel4MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel4MismatchPortn.setStatus("current")
_Pmopm8AlmChannel4BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel4BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel4BalancedPortn = _Pmopm8AlmChannel4BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1, 4),
    _Pmopm8AlmChannel4BalancedPortn_Type()
)
pmopm8AlmChannel4BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel4BalancedPortn.setStatus("current")
_Pmopm8AlmChannel4PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel4PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel4PowerLowPortn = _Pmopm8AlmChannel4PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1, 5),
    _Pmopm8AlmChannel4PowerLowPortn_Type()
)
pmopm8AlmChannel4PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel4PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel4PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel4PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel4PowerHighPortn = _Pmopm8AlmChannel4PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1, 6),
    _Pmopm8AlmChannel4PowerHighPortn_Type()
)
pmopm8AlmChannel4PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel4PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel4OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel4OosPortn_Object = MibTableColumn
pmopm8AlmChannel4OosPortn = _Pmopm8AlmChannel4OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 40, 1, 7),
    _Pmopm8AlmChannel4OosPortn_Type()
)
pmopm8AlmChannel4OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel4OosPortn.setStatus("current")
_Pmopm8Almchannel5PortTable_Object = MibTable
pmopm8Almchannel5PortTable = _Pmopm8Almchannel5PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel5PortTable.setStatus("current")
_Pmopm8Almchannel5PortEntry_Object = MibTableRow
pmopm8Almchannel5PortEntry = _Pmopm8Almchannel5PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1)
)
pmopm8Almchannel5PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel5PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel5PortEntry.setStatus("current")


class _Pmopm8Almchannel5PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel5PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel5PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel5PortIndex_Object = MibTableColumn
pmopm8Almchannel5PortIndex = _Pmopm8Almchannel5PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1, 1),
    _Pmopm8Almchannel5PortIndex_Type()
)
pmopm8Almchannel5PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel5PortIndex.setStatus("current")
_Pmopm8AlmChannel5AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel5AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel5AbsentPortn = _Pmopm8AlmChannel5AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1, 2),
    _Pmopm8AlmChannel5AbsentPortn_Type()
)
pmopm8AlmChannel5AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel5AbsentPortn.setStatus("current")
_Pmopm8AlmChannel5MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel5MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel5MismatchPortn = _Pmopm8AlmChannel5MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1, 3),
    _Pmopm8AlmChannel5MismatchPortn_Type()
)
pmopm8AlmChannel5MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel5MismatchPortn.setStatus("current")
_Pmopm8AlmChannel5BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel5BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel5BalancedPortn = _Pmopm8AlmChannel5BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1, 4),
    _Pmopm8AlmChannel5BalancedPortn_Type()
)
pmopm8AlmChannel5BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel5BalancedPortn.setStatus("current")
_Pmopm8AlmChannel5PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel5PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel5PowerLowPortn = _Pmopm8AlmChannel5PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1, 5),
    _Pmopm8AlmChannel5PowerLowPortn_Type()
)
pmopm8AlmChannel5PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel5PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel5PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel5PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel5PowerHighPortn = _Pmopm8AlmChannel5PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1, 6),
    _Pmopm8AlmChannel5PowerHighPortn_Type()
)
pmopm8AlmChannel5PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel5PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel5OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel5OosPortn_Object = MibTableColumn
pmopm8AlmChannel5OosPortn = _Pmopm8AlmChannel5OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 48, 1, 7),
    _Pmopm8AlmChannel5OosPortn_Type()
)
pmopm8AlmChannel5OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel5OosPortn.setStatus("current")
_Pmopm8Almchannel6PortTable_Object = MibTable
pmopm8Almchannel6PortTable = _Pmopm8Almchannel6PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel6PortTable.setStatus("current")
_Pmopm8Almchannel6PortEntry_Object = MibTableRow
pmopm8Almchannel6PortEntry = _Pmopm8Almchannel6PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1)
)
pmopm8Almchannel6PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel6PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel6PortEntry.setStatus("current")


class _Pmopm8Almchannel6PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel6PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel6PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel6PortIndex_Object = MibTableColumn
pmopm8Almchannel6PortIndex = _Pmopm8Almchannel6PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1, 1),
    _Pmopm8Almchannel6PortIndex_Type()
)
pmopm8Almchannel6PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel6PortIndex.setStatus("current")
_Pmopm8AlmChannel6AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel6AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel6AbsentPortn = _Pmopm8AlmChannel6AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1, 2),
    _Pmopm8AlmChannel6AbsentPortn_Type()
)
pmopm8AlmChannel6AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel6AbsentPortn.setStatus("current")
_Pmopm8AlmChannel6MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel6MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel6MismatchPortn = _Pmopm8AlmChannel6MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1, 3),
    _Pmopm8AlmChannel6MismatchPortn_Type()
)
pmopm8AlmChannel6MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel6MismatchPortn.setStatus("current")
_Pmopm8AlmChannel6BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel6BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel6BalancedPortn = _Pmopm8AlmChannel6BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1, 4),
    _Pmopm8AlmChannel6BalancedPortn_Type()
)
pmopm8AlmChannel6BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel6BalancedPortn.setStatus("current")
_Pmopm8AlmChannel6PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel6PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel6PowerLowPortn = _Pmopm8AlmChannel6PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1, 5),
    _Pmopm8AlmChannel6PowerLowPortn_Type()
)
pmopm8AlmChannel6PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel6PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel6PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel6PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel6PowerHighPortn = _Pmopm8AlmChannel6PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1, 6),
    _Pmopm8AlmChannel6PowerHighPortn_Type()
)
pmopm8AlmChannel6PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel6PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel6OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel6OosPortn_Object = MibTableColumn
pmopm8AlmChannel6OosPortn = _Pmopm8AlmChannel6OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 56, 1, 7),
    _Pmopm8AlmChannel6OosPortn_Type()
)
pmopm8AlmChannel6OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel6OosPortn.setStatus("current")
_Pmopm8Almchannel7PortTable_Object = MibTable
pmopm8Almchannel7PortTable = _Pmopm8Almchannel7PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel7PortTable.setStatus("current")
_Pmopm8Almchannel7PortEntry_Object = MibTableRow
pmopm8Almchannel7PortEntry = _Pmopm8Almchannel7PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1)
)
pmopm8Almchannel7PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel7PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel7PortEntry.setStatus("current")


class _Pmopm8Almchannel7PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel7PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel7PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel7PortIndex_Object = MibTableColumn
pmopm8Almchannel7PortIndex = _Pmopm8Almchannel7PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1, 1),
    _Pmopm8Almchannel7PortIndex_Type()
)
pmopm8Almchannel7PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel7PortIndex.setStatus("current")
_Pmopm8AlmChannel7AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel7AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel7AbsentPortn = _Pmopm8AlmChannel7AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1, 2),
    _Pmopm8AlmChannel7AbsentPortn_Type()
)
pmopm8AlmChannel7AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel7AbsentPortn.setStatus("current")
_Pmopm8AlmChannel7MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel7MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel7MismatchPortn = _Pmopm8AlmChannel7MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1, 3),
    _Pmopm8AlmChannel7MismatchPortn_Type()
)
pmopm8AlmChannel7MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel7MismatchPortn.setStatus("current")
_Pmopm8AlmChannel7BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel7BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel7BalancedPortn = _Pmopm8AlmChannel7BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1, 4),
    _Pmopm8AlmChannel7BalancedPortn_Type()
)
pmopm8AlmChannel7BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel7BalancedPortn.setStatus("current")
_Pmopm8AlmChannel7PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel7PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel7PowerLowPortn = _Pmopm8AlmChannel7PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1, 5),
    _Pmopm8AlmChannel7PowerLowPortn_Type()
)
pmopm8AlmChannel7PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel7PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel7PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel7PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel7PowerHighPortn = _Pmopm8AlmChannel7PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1, 6),
    _Pmopm8AlmChannel7PowerHighPortn_Type()
)
pmopm8AlmChannel7PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel7PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel7OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel7OosPortn_Object = MibTableColumn
pmopm8AlmChannel7OosPortn = _Pmopm8AlmChannel7OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 64, 1, 7),
    _Pmopm8AlmChannel7OosPortn_Type()
)
pmopm8AlmChannel7OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel7OosPortn.setStatus("current")
_Pmopm8Almchannel8PortTable_Object = MibTable
pmopm8Almchannel8PortTable = _Pmopm8Almchannel8PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel8PortTable.setStatus("current")
_Pmopm8Almchannel8PortEntry_Object = MibTableRow
pmopm8Almchannel8PortEntry = _Pmopm8Almchannel8PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1)
)
pmopm8Almchannel8PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel8PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel8PortEntry.setStatus("current")


class _Pmopm8Almchannel8PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel8PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel8PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel8PortIndex_Object = MibTableColumn
pmopm8Almchannel8PortIndex = _Pmopm8Almchannel8PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1, 1),
    _Pmopm8Almchannel8PortIndex_Type()
)
pmopm8Almchannel8PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel8PortIndex.setStatus("current")
_Pmopm8AlmChannel8AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel8AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel8AbsentPortn = _Pmopm8AlmChannel8AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1, 2),
    _Pmopm8AlmChannel8AbsentPortn_Type()
)
pmopm8AlmChannel8AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel8AbsentPortn.setStatus("current")
_Pmopm8AlmChannel8MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel8MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel8MismatchPortn = _Pmopm8AlmChannel8MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1, 3),
    _Pmopm8AlmChannel8MismatchPortn_Type()
)
pmopm8AlmChannel8MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel8MismatchPortn.setStatus("current")
_Pmopm8AlmChannel8BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel8BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel8BalancedPortn = _Pmopm8AlmChannel8BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1, 4),
    _Pmopm8AlmChannel8BalancedPortn_Type()
)
pmopm8AlmChannel8BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel8BalancedPortn.setStatus("current")
_Pmopm8AlmChannel8PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel8PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel8PowerLowPortn = _Pmopm8AlmChannel8PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1, 5),
    _Pmopm8AlmChannel8PowerLowPortn_Type()
)
pmopm8AlmChannel8PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel8PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel8PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel8PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel8PowerHighPortn = _Pmopm8AlmChannel8PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1, 6),
    _Pmopm8AlmChannel8PowerHighPortn_Type()
)
pmopm8AlmChannel8PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel8PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel8OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel8OosPortn_Object = MibTableColumn
pmopm8AlmChannel8OosPortn = _Pmopm8AlmChannel8OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 72, 1, 7),
    _Pmopm8AlmChannel8OosPortn_Type()
)
pmopm8AlmChannel8OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel8OosPortn.setStatus("current")
_Pmopm8Almchannel9PortTable_Object = MibTable
pmopm8Almchannel9PortTable = _Pmopm8Almchannel9PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel9PortTable.setStatus("current")
_Pmopm8Almchannel9PortEntry_Object = MibTableRow
pmopm8Almchannel9PortEntry = _Pmopm8Almchannel9PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1)
)
pmopm8Almchannel9PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel9PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel9PortEntry.setStatus("current")


class _Pmopm8Almchannel9PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel9PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel9PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel9PortIndex_Object = MibTableColumn
pmopm8Almchannel9PortIndex = _Pmopm8Almchannel9PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1, 1),
    _Pmopm8Almchannel9PortIndex_Type()
)
pmopm8Almchannel9PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel9PortIndex.setStatus("current")
_Pmopm8AlmChannel9AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel9AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel9AbsentPortn = _Pmopm8AlmChannel9AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1, 2),
    _Pmopm8AlmChannel9AbsentPortn_Type()
)
pmopm8AlmChannel9AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel9AbsentPortn.setStatus("current")
_Pmopm8AlmChannel9MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel9MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel9MismatchPortn = _Pmopm8AlmChannel9MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1, 3),
    _Pmopm8AlmChannel9MismatchPortn_Type()
)
pmopm8AlmChannel9MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel9MismatchPortn.setStatus("current")
_Pmopm8AlmChannel9BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel9BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel9BalancedPortn = _Pmopm8AlmChannel9BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1, 4),
    _Pmopm8AlmChannel9BalancedPortn_Type()
)
pmopm8AlmChannel9BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel9BalancedPortn.setStatus("current")
_Pmopm8AlmChannel9PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel9PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel9PowerLowPortn = _Pmopm8AlmChannel9PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1, 5),
    _Pmopm8AlmChannel9PowerLowPortn_Type()
)
pmopm8AlmChannel9PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel9PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel9PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel9PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel9PowerHighPortn = _Pmopm8AlmChannel9PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1, 6),
    _Pmopm8AlmChannel9PowerHighPortn_Type()
)
pmopm8AlmChannel9PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel9PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel9OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel9OosPortn_Object = MibTableColumn
pmopm8AlmChannel9OosPortn = _Pmopm8AlmChannel9OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 80, 1, 7),
    _Pmopm8AlmChannel9OosPortn_Type()
)
pmopm8AlmChannel9OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel9OosPortn.setStatus("current")
_Pmopm8Almchannel10PortTable_Object = MibTable
pmopm8Almchannel10PortTable = _Pmopm8Almchannel10PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel10PortTable.setStatus("current")
_Pmopm8Almchannel10PortEntry_Object = MibTableRow
pmopm8Almchannel10PortEntry = _Pmopm8Almchannel10PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1)
)
pmopm8Almchannel10PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel10PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel10PortEntry.setStatus("current")


class _Pmopm8Almchannel10PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel10PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel10PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel10PortIndex_Object = MibTableColumn
pmopm8Almchannel10PortIndex = _Pmopm8Almchannel10PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1, 1),
    _Pmopm8Almchannel10PortIndex_Type()
)
pmopm8Almchannel10PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel10PortIndex.setStatus("current")
_Pmopm8AlmChannel10AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel10AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel10AbsentPortn = _Pmopm8AlmChannel10AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1, 2),
    _Pmopm8AlmChannel10AbsentPortn_Type()
)
pmopm8AlmChannel10AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel10AbsentPortn.setStatus("current")
_Pmopm8AlmChannel10MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel10MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel10MismatchPortn = _Pmopm8AlmChannel10MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1, 3),
    _Pmopm8AlmChannel10MismatchPortn_Type()
)
pmopm8AlmChannel10MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel10MismatchPortn.setStatus("current")
_Pmopm8AlmChannel10BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel10BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel10BalancedPortn = _Pmopm8AlmChannel10BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1, 4),
    _Pmopm8AlmChannel10BalancedPortn_Type()
)
pmopm8AlmChannel10BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel10BalancedPortn.setStatus("current")
_Pmopm8AlmChannel10PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel10PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel10PowerLowPortn = _Pmopm8AlmChannel10PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1, 5),
    _Pmopm8AlmChannel10PowerLowPortn_Type()
)
pmopm8AlmChannel10PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel10PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel10PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel10PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel10PowerHighPortn = _Pmopm8AlmChannel10PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1, 6),
    _Pmopm8AlmChannel10PowerHighPortn_Type()
)
pmopm8AlmChannel10PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel10PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel10OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel10OosPortn_Object = MibTableColumn
pmopm8AlmChannel10OosPortn = _Pmopm8AlmChannel10OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 88, 1, 7),
    _Pmopm8AlmChannel10OosPortn_Type()
)
pmopm8AlmChannel10OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel10OosPortn.setStatus("current")
_Pmopm8Almchannel11PortTable_Object = MibTable
pmopm8Almchannel11PortTable = _Pmopm8Almchannel11PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel11PortTable.setStatus("current")
_Pmopm8Almchannel11PortEntry_Object = MibTableRow
pmopm8Almchannel11PortEntry = _Pmopm8Almchannel11PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1)
)
pmopm8Almchannel11PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel11PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel11PortEntry.setStatus("current")


class _Pmopm8Almchannel11PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel11PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel11PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel11PortIndex_Object = MibTableColumn
pmopm8Almchannel11PortIndex = _Pmopm8Almchannel11PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1, 1),
    _Pmopm8Almchannel11PortIndex_Type()
)
pmopm8Almchannel11PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel11PortIndex.setStatus("current")
_Pmopm8AlmChannel11AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel11AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel11AbsentPortn = _Pmopm8AlmChannel11AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1, 2),
    _Pmopm8AlmChannel11AbsentPortn_Type()
)
pmopm8AlmChannel11AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel11AbsentPortn.setStatus("current")
_Pmopm8AlmChannel11MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel11MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel11MismatchPortn = _Pmopm8AlmChannel11MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1, 3),
    _Pmopm8AlmChannel11MismatchPortn_Type()
)
pmopm8AlmChannel11MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel11MismatchPortn.setStatus("current")
_Pmopm8AlmChannel11BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel11BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel11BalancedPortn = _Pmopm8AlmChannel11BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1, 4),
    _Pmopm8AlmChannel11BalancedPortn_Type()
)
pmopm8AlmChannel11BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel11BalancedPortn.setStatus("current")
_Pmopm8AlmChannel11PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel11PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel11PowerLowPortn = _Pmopm8AlmChannel11PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1, 5),
    _Pmopm8AlmChannel11PowerLowPortn_Type()
)
pmopm8AlmChannel11PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel11PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel11PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel11PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel11PowerHighPortn = _Pmopm8AlmChannel11PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1, 6),
    _Pmopm8AlmChannel11PowerHighPortn_Type()
)
pmopm8AlmChannel11PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel11PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel11OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel11OosPortn_Object = MibTableColumn
pmopm8AlmChannel11OosPortn = _Pmopm8AlmChannel11OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 96, 1, 7),
    _Pmopm8AlmChannel11OosPortn_Type()
)
pmopm8AlmChannel11OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel11OosPortn.setStatus("current")
_Pmopm8Almchannel12PortTable_Object = MibTable
pmopm8Almchannel12PortTable = _Pmopm8Almchannel12PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel12PortTable.setStatus("current")
_Pmopm8Almchannel12PortEntry_Object = MibTableRow
pmopm8Almchannel12PortEntry = _Pmopm8Almchannel12PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1)
)
pmopm8Almchannel12PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel12PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel12PortEntry.setStatus("current")


class _Pmopm8Almchannel12PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel12PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel12PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel12PortIndex_Object = MibTableColumn
pmopm8Almchannel12PortIndex = _Pmopm8Almchannel12PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1, 1),
    _Pmopm8Almchannel12PortIndex_Type()
)
pmopm8Almchannel12PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel12PortIndex.setStatus("current")
_Pmopm8AlmChannel12AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel12AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel12AbsentPortn = _Pmopm8AlmChannel12AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1, 2),
    _Pmopm8AlmChannel12AbsentPortn_Type()
)
pmopm8AlmChannel12AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel12AbsentPortn.setStatus("current")
_Pmopm8AlmChannel12MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel12MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel12MismatchPortn = _Pmopm8AlmChannel12MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1, 3),
    _Pmopm8AlmChannel12MismatchPortn_Type()
)
pmopm8AlmChannel12MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel12MismatchPortn.setStatus("current")
_Pmopm8AlmChannel12BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel12BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel12BalancedPortn = _Pmopm8AlmChannel12BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1, 4),
    _Pmopm8AlmChannel12BalancedPortn_Type()
)
pmopm8AlmChannel12BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel12BalancedPortn.setStatus("current")
_Pmopm8AlmChannel12PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel12PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel12PowerLowPortn = _Pmopm8AlmChannel12PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1, 5),
    _Pmopm8AlmChannel12PowerLowPortn_Type()
)
pmopm8AlmChannel12PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel12PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel12PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel12PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel12PowerHighPortn = _Pmopm8AlmChannel12PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1, 6),
    _Pmopm8AlmChannel12PowerHighPortn_Type()
)
pmopm8AlmChannel12PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel12PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel12OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel12OosPortn_Object = MibTableColumn
pmopm8AlmChannel12OosPortn = _Pmopm8AlmChannel12OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 104, 1, 7),
    _Pmopm8AlmChannel12OosPortn_Type()
)
pmopm8AlmChannel12OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel12OosPortn.setStatus("current")
_Pmopm8Almchannel13PortTable_Object = MibTable
pmopm8Almchannel13PortTable = _Pmopm8Almchannel13PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel13PortTable.setStatus("current")
_Pmopm8Almchannel13PortEntry_Object = MibTableRow
pmopm8Almchannel13PortEntry = _Pmopm8Almchannel13PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1)
)
pmopm8Almchannel13PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel13PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel13PortEntry.setStatus("current")


class _Pmopm8Almchannel13PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel13PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel13PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel13PortIndex_Object = MibTableColumn
pmopm8Almchannel13PortIndex = _Pmopm8Almchannel13PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1, 1),
    _Pmopm8Almchannel13PortIndex_Type()
)
pmopm8Almchannel13PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel13PortIndex.setStatus("current")
_Pmopm8AlmChannel13AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel13AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel13AbsentPortn = _Pmopm8AlmChannel13AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1, 2),
    _Pmopm8AlmChannel13AbsentPortn_Type()
)
pmopm8AlmChannel13AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel13AbsentPortn.setStatus("current")
_Pmopm8AlmChannel13MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel13MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel13MismatchPortn = _Pmopm8AlmChannel13MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1, 3),
    _Pmopm8AlmChannel13MismatchPortn_Type()
)
pmopm8AlmChannel13MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel13MismatchPortn.setStatus("current")
_Pmopm8AlmChannel13BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel13BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel13BalancedPortn = _Pmopm8AlmChannel13BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1, 4),
    _Pmopm8AlmChannel13BalancedPortn_Type()
)
pmopm8AlmChannel13BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel13BalancedPortn.setStatus("current")
_Pmopm8AlmChannel13PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel13PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel13PowerLowPortn = _Pmopm8AlmChannel13PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1, 5),
    _Pmopm8AlmChannel13PowerLowPortn_Type()
)
pmopm8AlmChannel13PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel13PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel13PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel13PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel13PowerHighPortn = _Pmopm8AlmChannel13PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1, 6),
    _Pmopm8AlmChannel13PowerHighPortn_Type()
)
pmopm8AlmChannel13PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel13PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel13OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel13OosPortn_Object = MibTableColumn
pmopm8AlmChannel13OosPortn = _Pmopm8AlmChannel13OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 112, 1, 7),
    _Pmopm8AlmChannel13OosPortn_Type()
)
pmopm8AlmChannel13OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel13OosPortn.setStatus("current")
_Pmopm8Almchannel14PortTable_Object = MibTable
pmopm8Almchannel14PortTable = _Pmopm8Almchannel14PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel14PortTable.setStatus("current")
_Pmopm8Almchannel14PortEntry_Object = MibTableRow
pmopm8Almchannel14PortEntry = _Pmopm8Almchannel14PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1)
)
pmopm8Almchannel14PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel14PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel14PortEntry.setStatus("current")


class _Pmopm8Almchannel14PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel14PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel14PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel14PortIndex_Object = MibTableColumn
pmopm8Almchannel14PortIndex = _Pmopm8Almchannel14PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1, 1),
    _Pmopm8Almchannel14PortIndex_Type()
)
pmopm8Almchannel14PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel14PortIndex.setStatus("current")
_Pmopm8AlmChannel14AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel14AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel14AbsentPortn = _Pmopm8AlmChannel14AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1, 2),
    _Pmopm8AlmChannel14AbsentPortn_Type()
)
pmopm8AlmChannel14AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel14AbsentPortn.setStatus("current")
_Pmopm8AlmChannel14MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel14MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel14MismatchPortn = _Pmopm8AlmChannel14MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1, 3),
    _Pmopm8AlmChannel14MismatchPortn_Type()
)
pmopm8AlmChannel14MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel14MismatchPortn.setStatus("current")
_Pmopm8AlmChannel14BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel14BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel14BalancedPortn = _Pmopm8AlmChannel14BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1, 4),
    _Pmopm8AlmChannel14BalancedPortn_Type()
)
pmopm8AlmChannel14BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel14BalancedPortn.setStatus("current")
_Pmopm8AlmChannel14PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel14PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel14PowerLowPortn = _Pmopm8AlmChannel14PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1, 5),
    _Pmopm8AlmChannel14PowerLowPortn_Type()
)
pmopm8AlmChannel14PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel14PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel14PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel14PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel14PowerHighPortn = _Pmopm8AlmChannel14PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1, 6),
    _Pmopm8AlmChannel14PowerHighPortn_Type()
)
pmopm8AlmChannel14PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel14PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel14OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel14OosPortn_Object = MibTableColumn
pmopm8AlmChannel14OosPortn = _Pmopm8AlmChannel14OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 120, 1, 7),
    _Pmopm8AlmChannel14OosPortn_Type()
)
pmopm8AlmChannel14OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel14OosPortn.setStatus("current")
_Pmopm8Almchannel15PortTable_Object = MibTable
pmopm8Almchannel15PortTable = _Pmopm8Almchannel15PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel15PortTable.setStatus("current")
_Pmopm8Almchannel15PortEntry_Object = MibTableRow
pmopm8Almchannel15PortEntry = _Pmopm8Almchannel15PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1)
)
pmopm8Almchannel15PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel15PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel15PortEntry.setStatus("current")


class _Pmopm8Almchannel15PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel15PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel15PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel15PortIndex_Object = MibTableColumn
pmopm8Almchannel15PortIndex = _Pmopm8Almchannel15PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1, 1),
    _Pmopm8Almchannel15PortIndex_Type()
)
pmopm8Almchannel15PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel15PortIndex.setStatus("current")
_Pmopm8AlmChannel15AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel15AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel15AbsentPortn = _Pmopm8AlmChannel15AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1, 2),
    _Pmopm8AlmChannel15AbsentPortn_Type()
)
pmopm8AlmChannel15AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel15AbsentPortn.setStatus("current")
_Pmopm8AlmChannel15MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel15MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel15MismatchPortn = _Pmopm8AlmChannel15MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1, 3),
    _Pmopm8AlmChannel15MismatchPortn_Type()
)
pmopm8AlmChannel15MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel15MismatchPortn.setStatus("current")
_Pmopm8AlmChannel15BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel15BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel15BalancedPortn = _Pmopm8AlmChannel15BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1, 4),
    _Pmopm8AlmChannel15BalancedPortn_Type()
)
pmopm8AlmChannel15BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel15BalancedPortn.setStatus("current")
_Pmopm8AlmChannel15PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel15PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel15PowerLowPortn = _Pmopm8AlmChannel15PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1, 5),
    _Pmopm8AlmChannel15PowerLowPortn_Type()
)
pmopm8AlmChannel15PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel15PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel15PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel15PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel15PowerHighPortn = _Pmopm8AlmChannel15PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1, 6),
    _Pmopm8AlmChannel15PowerHighPortn_Type()
)
pmopm8AlmChannel15PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel15PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel15OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel15OosPortn_Object = MibTableColumn
pmopm8AlmChannel15OosPortn = _Pmopm8AlmChannel15OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 128, 1, 7),
    _Pmopm8AlmChannel15OosPortn_Type()
)
pmopm8AlmChannel15OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel15OosPortn.setStatus("current")
_Pmopm8Almchannel16PortTable_Object = MibTable
pmopm8Almchannel16PortTable = _Pmopm8Almchannel16PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel16PortTable.setStatus("current")
_Pmopm8Almchannel16PortEntry_Object = MibTableRow
pmopm8Almchannel16PortEntry = _Pmopm8Almchannel16PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1)
)
pmopm8Almchannel16PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel16PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel16PortEntry.setStatus("current")


class _Pmopm8Almchannel16PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel16PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel16PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel16PortIndex_Object = MibTableColumn
pmopm8Almchannel16PortIndex = _Pmopm8Almchannel16PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1, 1),
    _Pmopm8Almchannel16PortIndex_Type()
)
pmopm8Almchannel16PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel16PortIndex.setStatus("current")
_Pmopm8AlmChannel16AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel16AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel16AbsentPortn = _Pmopm8AlmChannel16AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1, 2),
    _Pmopm8AlmChannel16AbsentPortn_Type()
)
pmopm8AlmChannel16AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel16AbsentPortn.setStatus("current")
_Pmopm8AlmChannel16MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel16MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel16MismatchPortn = _Pmopm8AlmChannel16MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1, 3),
    _Pmopm8AlmChannel16MismatchPortn_Type()
)
pmopm8AlmChannel16MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel16MismatchPortn.setStatus("current")
_Pmopm8AlmChannel16BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel16BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel16BalancedPortn = _Pmopm8AlmChannel16BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1, 4),
    _Pmopm8AlmChannel16BalancedPortn_Type()
)
pmopm8AlmChannel16BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel16BalancedPortn.setStatus("current")
_Pmopm8AlmChannel16PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel16PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel16PowerLowPortn = _Pmopm8AlmChannel16PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1, 5),
    _Pmopm8AlmChannel16PowerLowPortn_Type()
)
pmopm8AlmChannel16PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel16PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel16PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel16PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel16PowerHighPortn = _Pmopm8AlmChannel16PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1, 6),
    _Pmopm8AlmChannel16PowerHighPortn_Type()
)
pmopm8AlmChannel16PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel16PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel16OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel16OosPortn_Object = MibTableColumn
pmopm8AlmChannel16OosPortn = _Pmopm8AlmChannel16OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 136, 1, 7),
    _Pmopm8AlmChannel16OosPortn_Type()
)
pmopm8AlmChannel16OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel16OosPortn.setStatus("current")
_Pmopm8Almchannel17PortTable_Object = MibTable
pmopm8Almchannel17PortTable = _Pmopm8Almchannel17PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel17PortTable.setStatus("current")
_Pmopm8Almchannel17PortEntry_Object = MibTableRow
pmopm8Almchannel17PortEntry = _Pmopm8Almchannel17PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1)
)
pmopm8Almchannel17PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel17PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel17PortEntry.setStatus("current")


class _Pmopm8Almchannel17PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel17PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel17PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel17PortIndex_Object = MibTableColumn
pmopm8Almchannel17PortIndex = _Pmopm8Almchannel17PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1, 1),
    _Pmopm8Almchannel17PortIndex_Type()
)
pmopm8Almchannel17PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel17PortIndex.setStatus("current")
_Pmopm8AlmChannel17AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel17AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel17AbsentPortn = _Pmopm8AlmChannel17AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1, 2),
    _Pmopm8AlmChannel17AbsentPortn_Type()
)
pmopm8AlmChannel17AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel17AbsentPortn.setStatus("current")
_Pmopm8AlmChannel17MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel17MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel17MismatchPortn = _Pmopm8AlmChannel17MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1, 3),
    _Pmopm8AlmChannel17MismatchPortn_Type()
)
pmopm8AlmChannel17MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel17MismatchPortn.setStatus("current")
_Pmopm8AlmChannel17BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel17BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel17BalancedPortn = _Pmopm8AlmChannel17BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1, 4),
    _Pmopm8AlmChannel17BalancedPortn_Type()
)
pmopm8AlmChannel17BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel17BalancedPortn.setStatus("current")
_Pmopm8AlmChannel17PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel17PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel17PowerLowPortn = _Pmopm8AlmChannel17PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1, 5),
    _Pmopm8AlmChannel17PowerLowPortn_Type()
)
pmopm8AlmChannel17PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel17PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel17PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel17PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel17PowerHighPortn = _Pmopm8AlmChannel17PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1, 6),
    _Pmopm8AlmChannel17PowerHighPortn_Type()
)
pmopm8AlmChannel17PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel17PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel17OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel17OosPortn_Object = MibTableColumn
pmopm8AlmChannel17OosPortn = _Pmopm8AlmChannel17OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 144, 1, 7),
    _Pmopm8AlmChannel17OosPortn_Type()
)
pmopm8AlmChannel17OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel17OosPortn.setStatus("current")
_Pmopm8Almchannel18PortTable_Object = MibTable
pmopm8Almchannel18PortTable = _Pmopm8Almchannel18PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel18PortTable.setStatus("current")
_Pmopm8Almchannel18PortEntry_Object = MibTableRow
pmopm8Almchannel18PortEntry = _Pmopm8Almchannel18PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1)
)
pmopm8Almchannel18PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel18PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel18PortEntry.setStatus("current")


class _Pmopm8Almchannel18PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel18PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel18PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel18PortIndex_Object = MibTableColumn
pmopm8Almchannel18PortIndex = _Pmopm8Almchannel18PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1, 1),
    _Pmopm8Almchannel18PortIndex_Type()
)
pmopm8Almchannel18PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel18PortIndex.setStatus("current")
_Pmopm8AlmChannel18AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel18AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel18AbsentPortn = _Pmopm8AlmChannel18AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1, 2),
    _Pmopm8AlmChannel18AbsentPortn_Type()
)
pmopm8AlmChannel18AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel18AbsentPortn.setStatus("current")
_Pmopm8AlmChannel18MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel18MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel18MismatchPortn = _Pmopm8AlmChannel18MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1, 3),
    _Pmopm8AlmChannel18MismatchPortn_Type()
)
pmopm8AlmChannel18MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel18MismatchPortn.setStatus("current")
_Pmopm8AlmChannel18BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel18BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel18BalancedPortn = _Pmopm8AlmChannel18BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1, 4),
    _Pmopm8AlmChannel18BalancedPortn_Type()
)
pmopm8AlmChannel18BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel18BalancedPortn.setStatus("current")
_Pmopm8AlmChannel18PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel18PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel18PowerLowPortn = _Pmopm8AlmChannel18PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1, 5),
    _Pmopm8AlmChannel18PowerLowPortn_Type()
)
pmopm8AlmChannel18PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel18PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel18PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel18PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel18PowerHighPortn = _Pmopm8AlmChannel18PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1, 6),
    _Pmopm8AlmChannel18PowerHighPortn_Type()
)
pmopm8AlmChannel18PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel18PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel18OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel18OosPortn_Object = MibTableColumn
pmopm8AlmChannel18OosPortn = _Pmopm8AlmChannel18OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 152, 1, 7),
    _Pmopm8AlmChannel18OosPortn_Type()
)
pmopm8AlmChannel18OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel18OosPortn.setStatus("current")
_Pmopm8Almchannel19PortTable_Object = MibTable
pmopm8Almchannel19PortTable = _Pmopm8Almchannel19PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel19PortTable.setStatus("current")
_Pmopm8Almchannel19PortEntry_Object = MibTableRow
pmopm8Almchannel19PortEntry = _Pmopm8Almchannel19PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1)
)
pmopm8Almchannel19PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel19PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel19PortEntry.setStatus("current")


class _Pmopm8Almchannel19PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel19PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel19PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel19PortIndex_Object = MibTableColumn
pmopm8Almchannel19PortIndex = _Pmopm8Almchannel19PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1, 1),
    _Pmopm8Almchannel19PortIndex_Type()
)
pmopm8Almchannel19PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel19PortIndex.setStatus("current")
_Pmopm8AlmChannel19AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel19AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel19AbsentPortn = _Pmopm8AlmChannel19AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1, 2),
    _Pmopm8AlmChannel19AbsentPortn_Type()
)
pmopm8AlmChannel19AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel19AbsentPortn.setStatus("current")
_Pmopm8AlmChannel19MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel19MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel19MismatchPortn = _Pmopm8AlmChannel19MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1, 3),
    _Pmopm8AlmChannel19MismatchPortn_Type()
)
pmopm8AlmChannel19MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel19MismatchPortn.setStatus("current")
_Pmopm8AlmChannel19BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel19BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel19BalancedPortn = _Pmopm8AlmChannel19BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1, 4),
    _Pmopm8AlmChannel19BalancedPortn_Type()
)
pmopm8AlmChannel19BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel19BalancedPortn.setStatus("current")
_Pmopm8AlmChannel19PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel19PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel19PowerLowPortn = _Pmopm8AlmChannel19PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1, 5),
    _Pmopm8AlmChannel19PowerLowPortn_Type()
)
pmopm8AlmChannel19PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel19PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel19PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel19PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel19PowerHighPortn = _Pmopm8AlmChannel19PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1, 6),
    _Pmopm8AlmChannel19PowerHighPortn_Type()
)
pmopm8AlmChannel19PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel19PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel19OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel19OosPortn_Object = MibTableColumn
pmopm8AlmChannel19OosPortn = _Pmopm8AlmChannel19OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 160, 1, 7),
    _Pmopm8AlmChannel19OosPortn_Type()
)
pmopm8AlmChannel19OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel19OosPortn.setStatus("current")
_Pmopm8Almchannel20PortTable_Object = MibTable
pmopm8Almchannel20PortTable = _Pmopm8Almchannel20PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel20PortTable.setStatus("current")
_Pmopm8Almchannel20PortEntry_Object = MibTableRow
pmopm8Almchannel20PortEntry = _Pmopm8Almchannel20PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1)
)
pmopm8Almchannel20PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel20PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel20PortEntry.setStatus("current")


class _Pmopm8Almchannel20PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel20PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel20PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel20PortIndex_Object = MibTableColumn
pmopm8Almchannel20PortIndex = _Pmopm8Almchannel20PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1, 1),
    _Pmopm8Almchannel20PortIndex_Type()
)
pmopm8Almchannel20PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel20PortIndex.setStatus("current")
_Pmopm8AlmChannel20AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel20AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel20AbsentPortn = _Pmopm8AlmChannel20AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1, 2),
    _Pmopm8AlmChannel20AbsentPortn_Type()
)
pmopm8AlmChannel20AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel20AbsentPortn.setStatus("current")
_Pmopm8AlmChannel20MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel20MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel20MismatchPortn = _Pmopm8AlmChannel20MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1, 3),
    _Pmopm8AlmChannel20MismatchPortn_Type()
)
pmopm8AlmChannel20MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel20MismatchPortn.setStatus("current")
_Pmopm8AlmChannel20BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel20BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel20BalancedPortn = _Pmopm8AlmChannel20BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1, 4),
    _Pmopm8AlmChannel20BalancedPortn_Type()
)
pmopm8AlmChannel20BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel20BalancedPortn.setStatus("current")
_Pmopm8AlmChannel20PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel20PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel20PowerLowPortn = _Pmopm8AlmChannel20PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1, 5),
    _Pmopm8AlmChannel20PowerLowPortn_Type()
)
pmopm8AlmChannel20PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel20PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel20PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel20PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel20PowerHighPortn = _Pmopm8AlmChannel20PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1, 6),
    _Pmopm8AlmChannel20PowerHighPortn_Type()
)
pmopm8AlmChannel20PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel20PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel20OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel20OosPortn_Object = MibTableColumn
pmopm8AlmChannel20OosPortn = _Pmopm8AlmChannel20OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 168, 1, 7),
    _Pmopm8AlmChannel20OosPortn_Type()
)
pmopm8AlmChannel20OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel20OosPortn.setStatus("current")
_Pmopm8Almchannel21PortTable_Object = MibTable
pmopm8Almchannel21PortTable = _Pmopm8Almchannel21PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel21PortTable.setStatus("current")
_Pmopm8Almchannel21PortEntry_Object = MibTableRow
pmopm8Almchannel21PortEntry = _Pmopm8Almchannel21PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1)
)
pmopm8Almchannel21PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel21PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel21PortEntry.setStatus("current")


class _Pmopm8Almchannel21PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel21PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel21PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel21PortIndex_Object = MibTableColumn
pmopm8Almchannel21PortIndex = _Pmopm8Almchannel21PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1, 1),
    _Pmopm8Almchannel21PortIndex_Type()
)
pmopm8Almchannel21PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel21PortIndex.setStatus("current")
_Pmopm8AlmChannel21AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel21AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel21AbsentPortn = _Pmopm8AlmChannel21AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1, 2),
    _Pmopm8AlmChannel21AbsentPortn_Type()
)
pmopm8AlmChannel21AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel21AbsentPortn.setStatus("current")
_Pmopm8AlmChannel21MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel21MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel21MismatchPortn = _Pmopm8AlmChannel21MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1, 3),
    _Pmopm8AlmChannel21MismatchPortn_Type()
)
pmopm8AlmChannel21MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel21MismatchPortn.setStatus("current")
_Pmopm8AlmChannel21BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel21BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel21BalancedPortn = _Pmopm8AlmChannel21BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1, 4),
    _Pmopm8AlmChannel21BalancedPortn_Type()
)
pmopm8AlmChannel21BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel21BalancedPortn.setStatus("current")
_Pmopm8AlmChannel21PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel21PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel21PowerLowPortn = _Pmopm8AlmChannel21PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1, 5),
    _Pmopm8AlmChannel21PowerLowPortn_Type()
)
pmopm8AlmChannel21PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel21PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel21PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel21PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel21PowerHighPortn = _Pmopm8AlmChannel21PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1, 6),
    _Pmopm8AlmChannel21PowerHighPortn_Type()
)
pmopm8AlmChannel21PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel21PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel21OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel21OosPortn_Object = MibTableColumn
pmopm8AlmChannel21OosPortn = _Pmopm8AlmChannel21OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 176, 1, 7),
    _Pmopm8AlmChannel21OosPortn_Type()
)
pmopm8AlmChannel21OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel21OosPortn.setStatus("current")
_Pmopm8Almchannel22PortTable_Object = MibTable
pmopm8Almchannel22PortTable = _Pmopm8Almchannel22PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel22PortTable.setStatus("current")
_Pmopm8Almchannel22PortEntry_Object = MibTableRow
pmopm8Almchannel22PortEntry = _Pmopm8Almchannel22PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1)
)
pmopm8Almchannel22PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel22PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel22PortEntry.setStatus("current")


class _Pmopm8Almchannel22PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel22PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel22PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel22PortIndex_Object = MibTableColumn
pmopm8Almchannel22PortIndex = _Pmopm8Almchannel22PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1, 1),
    _Pmopm8Almchannel22PortIndex_Type()
)
pmopm8Almchannel22PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel22PortIndex.setStatus("current")
_Pmopm8AlmChannel22AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel22AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel22AbsentPortn = _Pmopm8AlmChannel22AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1, 2),
    _Pmopm8AlmChannel22AbsentPortn_Type()
)
pmopm8AlmChannel22AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel22AbsentPortn.setStatus("current")
_Pmopm8AlmChannel22MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel22MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel22MismatchPortn = _Pmopm8AlmChannel22MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1, 3),
    _Pmopm8AlmChannel22MismatchPortn_Type()
)
pmopm8AlmChannel22MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel22MismatchPortn.setStatus("current")
_Pmopm8AlmChannel22BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel22BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel22BalancedPortn = _Pmopm8AlmChannel22BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1, 4),
    _Pmopm8AlmChannel22BalancedPortn_Type()
)
pmopm8AlmChannel22BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel22BalancedPortn.setStatus("current")
_Pmopm8AlmChannel22PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel22PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel22PowerLowPortn = _Pmopm8AlmChannel22PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1, 5),
    _Pmopm8AlmChannel22PowerLowPortn_Type()
)
pmopm8AlmChannel22PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel22PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel22PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel22PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel22PowerHighPortn = _Pmopm8AlmChannel22PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1, 6),
    _Pmopm8AlmChannel22PowerHighPortn_Type()
)
pmopm8AlmChannel22PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel22PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel22OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel22OosPortn_Object = MibTableColumn
pmopm8AlmChannel22OosPortn = _Pmopm8AlmChannel22OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 184, 1, 7),
    _Pmopm8AlmChannel22OosPortn_Type()
)
pmopm8AlmChannel22OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel22OosPortn.setStatus("current")
_Pmopm8Almchannel23PortTable_Object = MibTable
pmopm8Almchannel23PortTable = _Pmopm8Almchannel23PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel23PortTable.setStatus("current")
_Pmopm8Almchannel23PortEntry_Object = MibTableRow
pmopm8Almchannel23PortEntry = _Pmopm8Almchannel23PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1)
)
pmopm8Almchannel23PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel23PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel23PortEntry.setStatus("current")


class _Pmopm8Almchannel23PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel23PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel23PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel23PortIndex_Object = MibTableColumn
pmopm8Almchannel23PortIndex = _Pmopm8Almchannel23PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1, 1),
    _Pmopm8Almchannel23PortIndex_Type()
)
pmopm8Almchannel23PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel23PortIndex.setStatus("current")
_Pmopm8AlmChannel23AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel23AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel23AbsentPortn = _Pmopm8AlmChannel23AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1, 2),
    _Pmopm8AlmChannel23AbsentPortn_Type()
)
pmopm8AlmChannel23AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel23AbsentPortn.setStatus("current")
_Pmopm8AlmChannel23MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel23MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel23MismatchPortn = _Pmopm8AlmChannel23MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1, 3),
    _Pmopm8AlmChannel23MismatchPortn_Type()
)
pmopm8AlmChannel23MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel23MismatchPortn.setStatus("current")
_Pmopm8AlmChannel23BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel23BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel23BalancedPortn = _Pmopm8AlmChannel23BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1, 4),
    _Pmopm8AlmChannel23BalancedPortn_Type()
)
pmopm8AlmChannel23BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel23BalancedPortn.setStatus("current")
_Pmopm8AlmChannel23PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel23PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel23PowerLowPortn = _Pmopm8AlmChannel23PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1, 5),
    _Pmopm8AlmChannel23PowerLowPortn_Type()
)
pmopm8AlmChannel23PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel23PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel23PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel23PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel23PowerHighPortn = _Pmopm8AlmChannel23PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1, 6),
    _Pmopm8AlmChannel23PowerHighPortn_Type()
)
pmopm8AlmChannel23PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel23PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel23OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel23OosPortn_Object = MibTableColumn
pmopm8AlmChannel23OosPortn = _Pmopm8AlmChannel23OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 192, 1, 7),
    _Pmopm8AlmChannel23OosPortn_Type()
)
pmopm8AlmChannel23OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel23OosPortn.setStatus("current")
_Pmopm8Almchannel24PortTable_Object = MibTable
pmopm8Almchannel24PortTable = _Pmopm8Almchannel24PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel24PortTable.setStatus("current")
_Pmopm8Almchannel24PortEntry_Object = MibTableRow
pmopm8Almchannel24PortEntry = _Pmopm8Almchannel24PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1)
)
pmopm8Almchannel24PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel24PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel24PortEntry.setStatus("current")


class _Pmopm8Almchannel24PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel24PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel24PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel24PortIndex_Object = MibTableColumn
pmopm8Almchannel24PortIndex = _Pmopm8Almchannel24PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1, 1),
    _Pmopm8Almchannel24PortIndex_Type()
)
pmopm8Almchannel24PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel24PortIndex.setStatus("current")
_Pmopm8AlmChannel24AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel24AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel24AbsentPortn = _Pmopm8AlmChannel24AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1, 2),
    _Pmopm8AlmChannel24AbsentPortn_Type()
)
pmopm8AlmChannel24AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel24AbsentPortn.setStatus("current")
_Pmopm8AlmChannel24MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel24MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel24MismatchPortn = _Pmopm8AlmChannel24MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1, 3),
    _Pmopm8AlmChannel24MismatchPortn_Type()
)
pmopm8AlmChannel24MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel24MismatchPortn.setStatus("current")
_Pmopm8AlmChannel24BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel24BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel24BalancedPortn = _Pmopm8AlmChannel24BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1, 4),
    _Pmopm8AlmChannel24BalancedPortn_Type()
)
pmopm8AlmChannel24BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel24BalancedPortn.setStatus("current")
_Pmopm8AlmChannel24PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel24PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel24PowerLowPortn = _Pmopm8AlmChannel24PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1, 5),
    _Pmopm8AlmChannel24PowerLowPortn_Type()
)
pmopm8AlmChannel24PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel24PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel24PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel24PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel24PowerHighPortn = _Pmopm8AlmChannel24PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1, 6),
    _Pmopm8AlmChannel24PowerHighPortn_Type()
)
pmopm8AlmChannel24PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel24PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel24OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel24OosPortn_Object = MibTableColumn
pmopm8AlmChannel24OosPortn = _Pmopm8AlmChannel24OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 200, 1, 7),
    _Pmopm8AlmChannel24OosPortn_Type()
)
pmopm8AlmChannel24OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel24OosPortn.setStatus("current")
_Pmopm8Almchannel25PortTable_Object = MibTable
pmopm8Almchannel25PortTable = _Pmopm8Almchannel25PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel25PortTable.setStatus("current")
_Pmopm8Almchannel25PortEntry_Object = MibTableRow
pmopm8Almchannel25PortEntry = _Pmopm8Almchannel25PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1)
)
pmopm8Almchannel25PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel25PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel25PortEntry.setStatus("current")


class _Pmopm8Almchannel25PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel25PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel25PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel25PortIndex_Object = MibTableColumn
pmopm8Almchannel25PortIndex = _Pmopm8Almchannel25PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1, 1),
    _Pmopm8Almchannel25PortIndex_Type()
)
pmopm8Almchannel25PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel25PortIndex.setStatus("current")
_Pmopm8AlmChannel25AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel25AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel25AbsentPortn = _Pmopm8AlmChannel25AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1, 2),
    _Pmopm8AlmChannel25AbsentPortn_Type()
)
pmopm8AlmChannel25AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel25AbsentPortn.setStatus("current")
_Pmopm8AlmChannel25MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel25MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel25MismatchPortn = _Pmopm8AlmChannel25MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1, 3),
    _Pmopm8AlmChannel25MismatchPortn_Type()
)
pmopm8AlmChannel25MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel25MismatchPortn.setStatus("current")
_Pmopm8AlmChannel25BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel25BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel25BalancedPortn = _Pmopm8AlmChannel25BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1, 4),
    _Pmopm8AlmChannel25BalancedPortn_Type()
)
pmopm8AlmChannel25BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel25BalancedPortn.setStatus("current")
_Pmopm8AlmChannel25PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel25PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel25PowerLowPortn = _Pmopm8AlmChannel25PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1, 5),
    _Pmopm8AlmChannel25PowerLowPortn_Type()
)
pmopm8AlmChannel25PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel25PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel25PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel25PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel25PowerHighPortn = _Pmopm8AlmChannel25PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1, 6),
    _Pmopm8AlmChannel25PowerHighPortn_Type()
)
pmopm8AlmChannel25PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel25PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel25OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel25OosPortn_Object = MibTableColumn
pmopm8AlmChannel25OosPortn = _Pmopm8AlmChannel25OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 208, 1, 7),
    _Pmopm8AlmChannel25OosPortn_Type()
)
pmopm8AlmChannel25OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel25OosPortn.setStatus("current")
_Pmopm8Almchannel26PortTable_Object = MibTable
pmopm8Almchannel26PortTable = _Pmopm8Almchannel26PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel26PortTable.setStatus("current")
_Pmopm8Almchannel26PortEntry_Object = MibTableRow
pmopm8Almchannel26PortEntry = _Pmopm8Almchannel26PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1)
)
pmopm8Almchannel26PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel26PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel26PortEntry.setStatus("current")


class _Pmopm8Almchannel26PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel26PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel26PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel26PortIndex_Object = MibTableColumn
pmopm8Almchannel26PortIndex = _Pmopm8Almchannel26PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1, 1),
    _Pmopm8Almchannel26PortIndex_Type()
)
pmopm8Almchannel26PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel26PortIndex.setStatus("current")
_Pmopm8AlmChannel26AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel26AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel26AbsentPortn = _Pmopm8AlmChannel26AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1, 2),
    _Pmopm8AlmChannel26AbsentPortn_Type()
)
pmopm8AlmChannel26AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel26AbsentPortn.setStatus("current")
_Pmopm8AlmChannel26MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel26MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel26MismatchPortn = _Pmopm8AlmChannel26MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1, 3),
    _Pmopm8AlmChannel26MismatchPortn_Type()
)
pmopm8AlmChannel26MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel26MismatchPortn.setStatus("current")
_Pmopm8AlmChannel26BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel26BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel26BalancedPortn = _Pmopm8AlmChannel26BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1, 4),
    _Pmopm8AlmChannel26BalancedPortn_Type()
)
pmopm8AlmChannel26BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel26BalancedPortn.setStatus("current")
_Pmopm8AlmChannel26PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel26PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel26PowerLowPortn = _Pmopm8AlmChannel26PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1, 5),
    _Pmopm8AlmChannel26PowerLowPortn_Type()
)
pmopm8AlmChannel26PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel26PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel26PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel26PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel26PowerHighPortn = _Pmopm8AlmChannel26PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1, 6),
    _Pmopm8AlmChannel26PowerHighPortn_Type()
)
pmopm8AlmChannel26PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel26PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel26OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel26OosPortn_Object = MibTableColumn
pmopm8AlmChannel26OosPortn = _Pmopm8AlmChannel26OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 216, 1, 7),
    _Pmopm8AlmChannel26OosPortn_Type()
)
pmopm8AlmChannel26OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel26OosPortn.setStatus("current")
_Pmopm8Almchannel27PortTable_Object = MibTable
pmopm8Almchannel27PortTable = _Pmopm8Almchannel27PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel27PortTable.setStatus("current")
_Pmopm8Almchannel27PortEntry_Object = MibTableRow
pmopm8Almchannel27PortEntry = _Pmopm8Almchannel27PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1)
)
pmopm8Almchannel27PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel27PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel27PortEntry.setStatus("current")


class _Pmopm8Almchannel27PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel27PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel27PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel27PortIndex_Object = MibTableColumn
pmopm8Almchannel27PortIndex = _Pmopm8Almchannel27PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1, 1),
    _Pmopm8Almchannel27PortIndex_Type()
)
pmopm8Almchannel27PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel27PortIndex.setStatus("current")
_Pmopm8AlmChannel27AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel27AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel27AbsentPortn = _Pmopm8AlmChannel27AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1, 2),
    _Pmopm8AlmChannel27AbsentPortn_Type()
)
pmopm8AlmChannel27AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel27AbsentPortn.setStatus("current")
_Pmopm8AlmChannel27MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel27MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel27MismatchPortn = _Pmopm8AlmChannel27MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1, 3),
    _Pmopm8AlmChannel27MismatchPortn_Type()
)
pmopm8AlmChannel27MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel27MismatchPortn.setStatus("current")
_Pmopm8AlmChannel27BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel27BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel27BalancedPortn = _Pmopm8AlmChannel27BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1, 4),
    _Pmopm8AlmChannel27BalancedPortn_Type()
)
pmopm8AlmChannel27BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel27BalancedPortn.setStatus("current")
_Pmopm8AlmChannel27PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel27PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel27PowerLowPortn = _Pmopm8AlmChannel27PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1, 5),
    _Pmopm8AlmChannel27PowerLowPortn_Type()
)
pmopm8AlmChannel27PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel27PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel27PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel27PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel27PowerHighPortn = _Pmopm8AlmChannel27PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1, 6),
    _Pmopm8AlmChannel27PowerHighPortn_Type()
)
pmopm8AlmChannel27PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel27PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel27OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel27OosPortn_Object = MibTableColumn
pmopm8AlmChannel27OosPortn = _Pmopm8AlmChannel27OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 224, 1, 7),
    _Pmopm8AlmChannel27OosPortn_Type()
)
pmopm8AlmChannel27OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel27OosPortn.setStatus("current")
_Pmopm8Almchannel28PortTable_Object = MibTable
pmopm8Almchannel28PortTable = _Pmopm8Almchannel28PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel28PortTable.setStatus("current")
_Pmopm8Almchannel28PortEntry_Object = MibTableRow
pmopm8Almchannel28PortEntry = _Pmopm8Almchannel28PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1)
)
pmopm8Almchannel28PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel28PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel28PortEntry.setStatus("current")


class _Pmopm8Almchannel28PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel28PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel28PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel28PortIndex_Object = MibTableColumn
pmopm8Almchannel28PortIndex = _Pmopm8Almchannel28PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1, 1),
    _Pmopm8Almchannel28PortIndex_Type()
)
pmopm8Almchannel28PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel28PortIndex.setStatus("current")
_Pmopm8AlmChannel28AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel28AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel28AbsentPortn = _Pmopm8AlmChannel28AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1, 2),
    _Pmopm8AlmChannel28AbsentPortn_Type()
)
pmopm8AlmChannel28AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel28AbsentPortn.setStatus("current")
_Pmopm8AlmChannel28MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel28MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel28MismatchPortn = _Pmopm8AlmChannel28MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1, 3),
    _Pmopm8AlmChannel28MismatchPortn_Type()
)
pmopm8AlmChannel28MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel28MismatchPortn.setStatus("current")
_Pmopm8AlmChannel28BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel28BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel28BalancedPortn = _Pmopm8AlmChannel28BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1, 4),
    _Pmopm8AlmChannel28BalancedPortn_Type()
)
pmopm8AlmChannel28BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel28BalancedPortn.setStatus("current")
_Pmopm8AlmChannel28PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel28PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel28PowerLowPortn = _Pmopm8AlmChannel28PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1, 5),
    _Pmopm8AlmChannel28PowerLowPortn_Type()
)
pmopm8AlmChannel28PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel28PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel28PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel28PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel28PowerHighPortn = _Pmopm8AlmChannel28PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1, 6),
    _Pmopm8AlmChannel28PowerHighPortn_Type()
)
pmopm8AlmChannel28PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel28PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel28OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel28OosPortn_Object = MibTableColumn
pmopm8AlmChannel28OosPortn = _Pmopm8AlmChannel28OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 232, 1, 7),
    _Pmopm8AlmChannel28OosPortn_Type()
)
pmopm8AlmChannel28OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel28OosPortn.setStatus("current")
_Pmopm8Almchannel29PortTable_Object = MibTable
pmopm8Almchannel29PortTable = _Pmopm8Almchannel29PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel29PortTable.setStatus("current")
_Pmopm8Almchannel29PortEntry_Object = MibTableRow
pmopm8Almchannel29PortEntry = _Pmopm8Almchannel29PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1)
)
pmopm8Almchannel29PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel29PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel29PortEntry.setStatus("current")


class _Pmopm8Almchannel29PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel29PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel29PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel29PortIndex_Object = MibTableColumn
pmopm8Almchannel29PortIndex = _Pmopm8Almchannel29PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1, 1),
    _Pmopm8Almchannel29PortIndex_Type()
)
pmopm8Almchannel29PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel29PortIndex.setStatus("current")
_Pmopm8AlmChannel29AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel29AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel29AbsentPortn = _Pmopm8AlmChannel29AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1, 2),
    _Pmopm8AlmChannel29AbsentPortn_Type()
)
pmopm8AlmChannel29AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel29AbsentPortn.setStatus("current")
_Pmopm8AlmChannel29MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel29MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel29MismatchPortn = _Pmopm8AlmChannel29MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1, 3),
    _Pmopm8AlmChannel29MismatchPortn_Type()
)
pmopm8AlmChannel29MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel29MismatchPortn.setStatus("current")
_Pmopm8AlmChannel29BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel29BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel29BalancedPortn = _Pmopm8AlmChannel29BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1, 4),
    _Pmopm8AlmChannel29BalancedPortn_Type()
)
pmopm8AlmChannel29BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel29BalancedPortn.setStatus("current")
_Pmopm8AlmChannel29PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel29PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel29PowerLowPortn = _Pmopm8AlmChannel29PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1, 5),
    _Pmopm8AlmChannel29PowerLowPortn_Type()
)
pmopm8AlmChannel29PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel29PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel29PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel29PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel29PowerHighPortn = _Pmopm8AlmChannel29PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1, 6),
    _Pmopm8AlmChannel29PowerHighPortn_Type()
)
pmopm8AlmChannel29PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel29PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel29OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel29OosPortn_Object = MibTableColumn
pmopm8AlmChannel29OosPortn = _Pmopm8AlmChannel29OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 240, 1, 7),
    _Pmopm8AlmChannel29OosPortn_Type()
)
pmopm8AlmChannel29OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel29OosPortn.setStatus("current")
_Pmopm8Almchannel30PortTable_Object = MibTable
pmopm8Almchannel30PortTable = _Pmopm8Almchannel30PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel30PortTable.setStatus("current")
_Pmopm8Almchannel30PortEntry_Object = MibTableRow
pmopm8Almchannel30PortEntry = _Pmopm8Almchannel30PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1)
)
pmopm8Almchannel30PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel30PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel30PortEntry.setStatus("current")


class _Pmopm8Almchannel30PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel30PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel30PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel30PortIndex_Object = MibTableColumn
pmopm8Almchannel30PortIndex = _Pmopm8Almchannel30PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1, 1),
    _Pmopm8Almchannel30PortIndex_Type()
)
pmopm8Almchannel30PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel30PortIndex.setStatus("current")
_Pmopm8AlmChannel30AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel30AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel30AbsentPortn = _Pmopm8AlmChannel30AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1, 2),
    _Pmopm8AlmChannel30AbsentPortn_Type()
)
pmopm8AlmChannel30AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel30AbsentPortn.setStatus("current")
_Pmopm8AlmChannel30MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel30MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel30MismatchPortn = _Pmopm8AlmChannel30MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1, 3),
    _Pmopm8AlmChannel30MismatchPortn_Type()
)
pmopm8AlmChannel30MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel30MismatchPortn.setStatus("current")
_Pmopm8AlmChannel30BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel30BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel30BalancedPortn = _Pmopm8AlmChannel30BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1, 4),
    _Pmopm8AlmChannel30BalancedPortn_Type()
)
pmopm8AlmChannel30BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel30BalancedPortn.setStatus("current")
_Pmopm8AlmChannel30PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel30PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel30PowerLowPortn = _Pmopm8AlmChannel30PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1, 5),
    _Pmopm8AlmChannel30PowerLowPortn_Type()
)
pmopm8AlmChannel30PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel30PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel30PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel30PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel30PowerHighPortn = _Pmopm8AlmChannel30PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1, 6),
    _Pmopm8AlmChannel30PowerHighPortn_Type()
)
pmopm8AlmChannel30PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel30PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel30OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel30OosPortn_Object = MibTableColumn
pmopm8AlmChannel30OosPortn = _Pmopm8AlmChannel30OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 248, 1, 7),
    _Pmopm8AlmChannel30OosPortn_Type()
)
pmopm8AlmChannel30OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel30OosPortn.setStatus("current")
_Pmopm8Almchannel31PortTable_Object = MibTable
pmopm8Almchannel31PortTable = _Pmopm8Almchannel31PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel31PortTable.setStatus("current")
_Pmopm8Almchannel31PortEntry_Object = MibTableRow
pmopm8Almchannel31PortEntry = _Pmopm8Almchannel31PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1)
)
pmopm8Almchannel31PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel31PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel31PortEntry.setStatus("current")


class _Pmopm8Almchannel31PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel31PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel31PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel31PortIndex_Object = MibTableColumn
pmopm8Almchannel31PortIndex = _Pmopm8Almchannel31PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1, 1),
    _Pmopm8Almchannel31PortIndex_Type()
)
pmopm8Almchannel31PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel31PortIndex.setStatus("current")
_Pmopm8AlmChannel31AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel31AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel31AbsentPortn = _Pmopm8AlmChannel31AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1, 2),
    _Pmopm8AlmChannel31AbsentPortn_Type()
)
pmopm8AlmChannel31AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel31AbsentPortn.setStatus("current")
_Pmopm8AlmChannel31MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel31MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel31MismatchPortn = _Pmopm8AlmChannel31MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1, 3),
    _Pmopm8AlmChannel31MismatchPortn_Type()
)
pmopm8AlmChannel31MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel31MismatchPortn.setStatus("current")
_Pmopm8AlmChannel31BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel31BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel31BalancedPortn = _Pmopm8AlmChannel31BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1, 4),
    _Pmopm8AlmChannel31BalancedPortn_Type()
)
pmopm8AlmChannel31BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel31BalancedPortn.setStatus("current")
_Pmopm8AlmChannel31PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel31PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel31PowerLowPortn = _Pmopm8AlmChannel31PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1, 5),
    _Pmopm8AlmChannel31PowerLowPortn_Type()
)
pmopm8AlmChannel31PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel31PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel31PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel31PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel31PowerHighPortn = _Pmopm8AlmChannel31PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1, 6),
    _Pmopm8AlmChannel31PowerHighPortn_Type()
)
pmopm8AlmChannel31PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel31PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel31OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel31OosPortn_Object = MibTableColumn
pmopm8AlmChannel31OosPortn = _Pmopm8AlmChannel31OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 256, 1, 7),
    _Pmopm8AlmChannel31OosPortn_Type()
)
pmopm8AlmChannel31OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel31OosPortn.setStatus("current")
_Pmopm8Almchannel32PortTable_Object = MibTable
pmopm8Almchannel32PortTable = _Pmopm8Almchannel32PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel32PortTable.setStatus("current")
_Pmopm8Almchannel32PortEntry_Object = MibTableRow
pmopm8Almchannel32PortEntry = _Pmopm8Almchannel32PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1)
)
pmopm8Almchannel32PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel32PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel32PortEntry.setStatus("current")


class _Pmopm8Almchannel32PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel32PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel32PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel32PortIndex_Object = MibTableColumn
pmopm8Almchannel32PortIndex = _Pmopm8Almchannel32PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1, 1),
    _Pmopm8Almchannel32PortIndex_Type()
)
pmopm8Almchannel32PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel32PortIndex.setStatus("current")
_Pmopm8AlmChannel32AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel32AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel32AbsentPortn = _Pmopm8AlmChannel32AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1, 2),
    _Pmopm8AlmChannel32AbsentPortn_Type()
)
pmopm8AlmChannel32AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel32AbsentPortn.setStatus("current")
_Pmopm8AlmChannel32MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel32MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel32MismatchPortn = _Pmopm8AlmChannel32MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1, 3),
    _Pmopm8AlmChannel32MismatchPortn_Type()
)
pmopm8AlmChannel32MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel32MismatchPortn.setStatus("current")
_Pmopm8AlmChannel32BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel32BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel32BalancedPortn = _Pmopm8AlmChannel32BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1, 4),
    _Pmopm8AlmChannel32BalancedPortn_Type()
)
pmopm8AlmChannel32BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel32BalancedPortn.setStatus("current")
_Pmopm8AlmChannel32PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel32PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel32PowerLowPortn = _Pmopm8AlmChannel32PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1, 5),
    _Pmopm8AlmChannel32PowerLowPortn_Type()
)
pmopm8AlmChannel32PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel32PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel32PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel32PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel32PowerHighPortn = _Pmopm8AlmChannel32PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1, 6),
    _Pmopm8AlmChannel32PowerHighPortn_Type()
)
pmopm8AlmChannel32PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel32PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel32OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel32OosPortn_Object = MibTableColumn
pmopm8AlmChannel32OosPortn = _Pmopm8AlmChannel32OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 264, 1, 7),
    _Pmopm8AlmChannel32OosPortn_Type()
)
pmopm8AlmChannel32OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel32OosPortn.setStatus("current")
_Pmopm8Almchannel33PortTable_Object = MibTable
pmopm8Almchannel33PortTable = _Pmopm8Almchannel33PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel33PortTable.setStatus("current")
_Pmopm8Almchannel33PortEntry_Object = MibTableRow
pmopm8Almchannel33PortEntry = _Pmopm8Almchannel33PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1)
)
pmopm8Almchannel33PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel33PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel33PortEntry.setStatus("current")


class _Pmopm8Almchannel33PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel33PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel33PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel33PortIndex_Object = MibTableColumn
pmopm8Almchannel33PortIndex = _Pmopm8Almchannel33PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1, 1),
    _Pmopm8Almchannel33PortIndex_Type()
)
pmopm8Almchannel33PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel33PortIndex.setStatus("current")
_Pmopm8AlmChannel33AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel33AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel33AbsentPortn = _Pmopm8AlmChannel33AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1, 2),
    _Pmopm8AlmChannel33AbsentPortn_Type()
)
pmopm8AlmChannel33AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel33AbsentPortn.setStatus("current")
_Pmopm8AlmChannel33MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel33MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel33MismatchPortn = _Pmopm8AlmChannel33MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1, 3),
    _Pmopm8AlmChannel33MismatchPortn_Type()
)
pmopm8AlmChannel33MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel33MismatchPortn.setStatus("current")
_Pmopm8AlmChannel33BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel33BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel33BalancedPortn = _Pmopm8AlmChannel33BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1, 4),
    _Pmopm8AlmChannel33BalancedPortn_Type()
)
pmopm8AlmChannel33BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel33BalancedPortn.setStatus("current")
_Pmopm8AlmChannel33PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel33PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel33PowerLowPortn = _Pmopm8AlmChannel33PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1, 5),
    _Pmopm8AlmChannel33PowerLowPortn_Type()
)
pmopm8AlmChannel33PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel33PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel33PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel33PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel33PowerHighPortn = _Pmopm8AlmChannel33PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1, 6),
    _Pmopm8AlmChannel33PowerHighPortn_Type()
)
pmopm8AlmChannel33PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel33PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel33OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel33OosPortn_Object = MibTableColumn
pmopm8AlmChannel33OosPortn = _Pmopm8AlmChannel33OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 272, 1, 7),
    _Pmopm8AlmChannel33OosPortn_Type()
)
pmopm8AlmChannel33OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel33OosPortn.setStatus("current")
_Pmopm8Almchannel34PortTable_Object = MibTable
pmopm8Almchannel34PortTable = _Pmopm8Almchannel34PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel34PortTable.setStatus("current")
_Pmopm8Almchannel34PortEntry_Object = MibTableRow
pmopm8Almchannel34PortEntry = _Pmopm8Almchannel34PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1)
)
pmopm8Almchannel34PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel34PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel34PortEntry.setStatus("current")


class _Pmopm8Almchannel34PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel34PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel34PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel34PortIndex_Object = MibTableColumn
pmopm8Almchannel34PortIndex = _Pmopm8Almchannel34PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1, 1),
    _Pmopm8Almchannel34PortIndex_Type()
)
pmopm8Almchannel34PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel34PortIndex.setStatus("current")
_Pmopm8AlmChannel34AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel34AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel34AbsentPortn = _Pmopm8AlmChannel34AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1, 2),
    _Pmopm8AlmChannel34AbsentPortn_Type()
)
pmopm8AlmChannel34AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel34AbsentPortn.setStatus("current")
_Pmopm8AlmChannel34MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel34MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel34MismatchPortn = _Pmopm8AlmChannel34MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1, 3),
    _Pmopm8AlmChannel34MismatchPortn_Type()
)
pmopm8AlmChannel34MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel34MismatchPortn.setStatus("current")
_Pmopm8AlmChannel34BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel34BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel34BalancedPortn = _Pmopm8AlmChannel34BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1, 4),
    _Pmopm8AlmChannel34BalancedPortn_Type()
)
pmopm8AlmChannel34BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel34BalancedPortn.setStatus("current")
_Pmopm8AlmChannel34PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel34PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel34PowerLowPortn = _Pmopm8AlmChannel34PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1, 5),
    _Pmopm8AlmChannel34PowerLowPortn_Type()
)
pmopm8AlmChannel34PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel34PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel34PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel34PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel34PowerHighPortn = _Pmopm8AlmChannel34PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1, 6),
    _Pmopm8AlmChannel34PowerHighPortn_Type()
)
pmopm8AlmChannel34PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel34PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel34OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel34OosPortn_Object = MibTableColumn
pmopm8AlmChannel34OosPortn = _Pmopm8AlmChannel34OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 280, 1, 7),
    _Pmopm8AlmChannel34OosPortn_Type()
)
pmopm8AlmChannel34OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel34OosPortn.setStatus("current")
_Pmopm8Almchannel35PortTable_Object = MibTable
pmopm8Almchannel35PortTable = _Pmopm8Almchannel35PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel35PortTable.setStatus("current")
_Pmopm8Almchannel35PortEntry_Object = MibTableRow
pmopm8Almchannel35PortEntry = _Pmopm8Almchannel35PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1)
)
pmopm8Almchannel35PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel35PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel35PortEntry.setStatus("current")


class _Pmopm8Almchannel35PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel35PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel35PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel35PortIndex_Object = MibTableColumn
pmopm8Almchannel35PortIndex = _Pmopm8Almchannel35PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1, 1),
    _Pmopm8Almchannel35PortIndex_Type()
)
pmopm8Almchannel35PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel35PortIndex.setStatus("current")
_Pmopm8AlmChannel35AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel35AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel35AbsentPortn = _Pmopm8AlmChannel35AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1, 2),
    _Pmopm8AlmChannel35AbsentPortn_Type()
)
pmopm8AlmChannel35AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel35AbsentPortn.setStatus("current")
_Pmopm8AlmChannel35MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel35MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel35MismatchPortn = _Pmopm8AlmChannel35MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1, 3),
    _Pmopm8AlmChannel35MismatchPortn_Type()
)
pmopm8AlmChannel35MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel35MismatchPortn.setStatus("current")
_Pmopm8AlmChannel35BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel35BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel35BalancedPortn = _Pmopm8AlmChannel35BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1, 4),
    _Pmopm8AlmChannel35BalancedPortn_Type()
)
pmopm8AlmChannel35BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel35BalancedPortn.setStatus("current")
_Pmopm8AlmChannel35PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel35PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel35PowerLowPortn = _Pmopm8AlmChannel35PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1, 5),
    _Pmopm8AlmChannel35PowerLowPortn_Type()
)
pmopm8AlmChannel35PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel35PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel35PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel35PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel35PowerHighPortn = _Pmopm8AlmChannel35PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1, 6),
    _Pmopm8AlmChannel35PowerHighPortn_Type()
)
pmopm8AlmChannel35PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel35PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel35OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel35OosPortn_Object = MibTableColumn
pmopm8AlmChannel35OosPortn = _Pmopm8AlmChannel35OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 288, 1, 7),
    _Pmopm8AlmChannel35OosPortn_Type()
)
pmopm8AlmChannel35OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel35OosPortn.setStatus("current")
_Pmopm8Almchannel36PortTable_Object = MibTable
pmopm8Almchannel36PortTable = _Pmopm8Almchannel36PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel36PortTable.setStatus("current")
_Pmopm8Almchannel36PortEntry_Object = MibTableRow
pmopm8Almchannel36PortEntry = _Pmopm8Almchannel36PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1)
)
pmopm8Almchannel36PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel36PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel36PortEntry.setStatus("current")


class _Pmopm8Almchannel36PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel36PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel36PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel36PortIndex_Object = MibTableColumn
pmopm8Almchannel36PortIndex = _Pmopm8Almchannel36PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1, 1),
    _Pmopm8Almchannel36PortIndex_Type()
)
pmopm8Almchannel36PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel36PortIndex.setStatus("current")
_Pmopm8AlmChannel36AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel36AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel36AbsentPortn = _Pmopm8AlmChannel36AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1, 2),
    _Pmopm8AlmChannel36AbsentPortn_Type()
)
pmopm8AlmChannel36AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel36AbsentPortn.setStatus("current")
_Pmopm8AlmChannel36MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel36MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel36MismatchPortn = _Pmopm8AlmChannel36MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1, 3),
    _Pmopm8AlmChannel36MismatchPortn_Type()
)
pmopm8AlmChannel36MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel36MismatchPortn.setStatus("current")
_Pmopm8AlmChannel36BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel36BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel36BalancedPortn = _Pmopm8AlmChannel36BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1, 4),
    _Pmopm8AlmChannel36BalancedPortn_Type()
)
pmopm8AlmChannel36BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel36BalancedPortn.setStatus("current")
_Pmopm8AlmChannel36PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel36PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel36PowerLowPortn = _Pmopm8AlmChannel36PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1, 5),
    _Pmopm8AlmChannel36PowerLowPortn_Type()
)
pmopm8AlmChannel36PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel36PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel36PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel36PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel36PowerHighPortn = _Pmopm8AlmChannel36PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1, 6),
    _Pmopm8AlmChannel36PowerHighPortn_Type()
)
pmopm8AlmChannel36PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel36PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel36OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel36OosPortn_Object = MibTableColumn
pmopm8AlmChannel36OosPortn = _Pmopm8AlmChannel36OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 296, 1, 7),
    _Pmopm8AlmChannel36OosPortn_Type()
)
pmopm8AlmChannel36OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel36OosPortn.setStatus("current")
_Pmopm8Almchannel37PortTable_Object = MibTable
pmopm8Almchannel37PortTable = _Pmopm8Almchannel37PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel37PortTable.setStatus("current")
_Pmopm8Almchannel37PortEntry_Object = MibTableRow
pmopm8Almchannel37PortEntry = _Pmopm8Almchannel37PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1)
)
pmopm8Almchannel37PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel37PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel37PortEntry.setStatus("current")


class _Pmopm8Almchannel37PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel37PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel37PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel37PortIndex_Object = MibTableColumn
pmopm8Almchannel37PortIndex = _Pmopm8Almchannel37PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1, 1),
    _Pmopm8Almchannel37PortIndex_Type()
)
pmopm8Almchannel37PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel37PortIndex.setStatus("current")
_Pmopm8AlmChannel37AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel37AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel37AbsentPortn = _Pmopm8AlmChannel37AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1, 2),
    _Pmopm8AlmChannel37AbsentPortn_Type()
)
pmopm8AlmChannel37AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel37AbsentPortn.setStatus("current")
_Pmopm8AlmChannel37MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel37MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel37MismatchPortn = _Pmopm8AlmChannel37MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1, 3),
    _Pmopm8AlmChannel37MismatchPortn_Type()
)
pmopm8AlmChannel37MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel37MismatchPortn.setStatus("current")
_Pmopm8AlmChannel37BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel37BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel37BalancedPortn = _Pmopm8AlmChannel37BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1, 4),
    _Pmopm8AlmChannel37BalancedPortn_Type()
)
pmopm8AlmChannel37BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel37BalancedPortn.setStatus("current")
_Pmopm8AlmChannel37PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel37PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel37PowerLowPortn = _Pmopm8AlmChannel37PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1, 5),
    _Pmopm8AlmChannel37PowerLowPortn_Type()
)
pmopm8AlmChannel37PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel37PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel37PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel37PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel37PowerHighPortn = _Pmopm8AlmChannel37PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1, 6),
    _Pmopm8AlmChannel37PowerHighPortn_Type()
)
pmopm8AlmChannel37PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel37PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel37OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel37OosPortn_Object = MibTableColumn
pmopm8AlmChannel37OosPortn = _Pmopm8AlmChannel37OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 304, 1, 7),
    _Pmopm8AlmChannel37OosPortn_Type()
)
pmopm8AlmChannel37OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel37OosPortn.setStatus("current")
_Pmopm8Almchannel38PortTable_Object = MibTable
pmopm8Almchannel38PortTable = _Pmopm8Almchannel38PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel38PortTable.setStatus("current")
_Pmopm8Almchannel38PortEntry_Object = MibTableRow
pmopm8Almchannel38PortEntry = _Pmopm8Almchannel38PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1)
)
pmopm8Almchannel38PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel38PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel38PortEntry.setStatus("current")


class _Pmopm8Almchannel38PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel38PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel38PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel38PortIndex_Object = MibTableColumn
pmopm8Almchannel38PortIndex = _Pmopm8Almchannel38PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1, 1),
    _Pmopm8Almchannel38PortIndex_Type()
)
pmopm8Almchannel38PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel38PortIndex.setStatus("current")
_Pmopm8AlmChannel38AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel38AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel38AbsentPortn = _Pmopm8AlmChannel38AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1, 2),
    _Pmopm8AlmChannel38AbsentPortn_Type()
)
pmopm8AlmChannel38AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel38AbsentPortn.setStatus("current")
_Pmopm8AlmChannel38MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel38MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel38MismatchPortn = _Pmopm8AlmChannel38MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1, 3),
    _Pmopm8AlmChannel38MismatchPortn_Type()
)
pmopm8AlmChannel38MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel38MismatchPortn.setStatus("current")
_Pmopm8AlmChannel38BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel38BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel38BalancedPortn = _Pmopm8AlmChannel38BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1, 4),
    _Pmopm8AlmChannel38BalancedPortn_Type()
)
pmopm8AlmChannel38BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel38BalancedPortn.setStatus("current")
_Pmopm8AlmChannel38PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel38PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel38PowerLowPortn = _Pmopm8AlmChannel38PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1, 5),
    _Pmopm8AlmChannel38PowerLowPortn_Type()
)
pmopm8AlmChannel38PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel38PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel38PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel38PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel38PowerHighPortn = _Pmopm8AlmChannel38PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1, 6),
    _Pmopm8AlmChannel38PowerHighPortn_Type()
)
pmopm8AlmChannel38PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel38PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel38OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel38OosPortn_Object = MibTableColumn
pmopm8AlmChannel38OosPortn = _Pmopm8AlmChannel38OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 312, 1, 7),
    _Pmopm8AlmChannel38OosPortn_Type()
)
pmopm8AlmChannel38OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel38OosPortn.setStatus("current")
_Pmopm8Almchannel39PortTable_Object = MibTable
pmopm8Almchannel39PortTable = _Pmopm8Almchannel39PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel39PortTable.setStatus("current")
_Pmopm8Almchannel39PortEntry_Object = MibTableRow
pmopm8Almchannel39PortEntry = _Pmopm8Almchannel39PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1)
)
pmopm8Almchannel39PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel39PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel39PortEntry.setStatus("current")


class _Pmopm8Almchannel39PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel39PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel39PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel39PortIndex_Object = MibTableColumn
pmopm8Almchannel39PortIndex = _Pmopm8Almchannel39PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1, 1),
    _Pmopm8Almchannel39PortIndex_Type()
)
pmopm8Almchannel39PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel39PortIndex.setStatus("current")
_Pmopm8AlmChannel39AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel39AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel39AbsentPortn = _Pmopm8AlmChannel39AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1, 2),
    _Pmopm8AlmChannel39AbsentPortn_Type()
)
pmopm8AlmChannel39AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel39AbsentPortn.setStatus("current")
_Pmopm8AlmChannel39MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel39MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel39MismatchPortn = _Pmopm8AlmChannel39MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1, 3),
    _Pmopm8AlmChannel39MismatchPortn_Type()
)
pmopm8AlmChannel39MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel39MismatchPortn.setStatus("current")
_Pmopm8AlmChannel39BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel39BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel39BalancedPortn = _Pmopm8AlmChannel39BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1, 4),
    _Pmopm8AlmChannel39BalancedPortn_Type()
)
pmopm8AlmChannel39BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel39BalancedPortn.setStatus("current")
_Pmopm8AlmChannel39PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel39PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel39PowerLowPortn = _Pmopm8AlmChannel39PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1, 5),
    _Pmopm8AlmChannel39PowerLowPortn_Type()
)
pmopm8AlmChannel39PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel39PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel39PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel39PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel39PowerHighPortn = _Pmopm8AlmChannel39PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1, 6),
    _Pmopm8AlmChannel39PowerHighPortn_Type()
)
pmopm8AlmChannel39PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel39PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel39OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel39OosPortn_Object = MibTableColumn
pmopm8AlmChannel39OosPortn = _Pmopm8AlmChannel39OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 320, 1, 7),
    _Pmopm8AlmChannel39OosPortn_Type()
)
pmopm8AlmChannel39OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel39OosPortn.setStatus("current")
_Pmopm8Almchannel40PortTable_Object = MibTable
pmopm8Almchannel40PortTable = _Pmopm8Almchannel40PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel40PortTable.setStatus("current")
_Pmopm8Almchannel40PortEntry_Object = MibTableRow
pmopm8Almchannel40PortEntry = _Pmopm8Almchannel40PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1)
)
pmopm8Almchannel40PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel40PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel40PortEntry.setStatus("current")


class _Pmopm8Almchannel40PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel40PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel40PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel40PortIndex_Object = MibTableColumn
pmopm8Almchannel40PortIndex = _Pmopm8Almchannel40PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1, 1),
    _Pmopm8Almchannel40PortIndex_Type()
)
pmopm8Almchannel40PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel40PortIndex.setStatus("current")
_Pmopm8AlmChannel40AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel40AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel40AbsentPortn = _Pmopm8AlmChannel40AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1, 2),
    _Pmopm8AlmChannel40AbsentPortn_Type()
)
pmopm8AlmChannel40AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel40AbsentPortn.setStatus("current")
_Pmopm8AlmChannel40MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel40MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel40MismatchPortn = _Pmopm8AlmChannel40MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1, 3),
    _Pmopm8AlmChannel40MismatchPortn_Type()
)
pmopm8AlmChannel40MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel40MismatchPortn.setStatus("current")
_Pmopm8AlmChannel40BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel40BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel40BalancedPortn = _Pmopm8AlmChannel40BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1, 4),
    _Pmopm8AlmChannel40BalancedPortn_Type()
)
pmopm8AlmChannel40BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel40BalancedPortn.setStatus("current")
_Pmopm8AlmChannel40PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel40PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel40PowerLowPortn = _Pmopm8AlmChannel40PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1, 5),
    _Pmopm8AlmChannel40PowerLowPortn_Type()
)
pmopm8AlmChannel40PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel40PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel40PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel40PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel40PowerHighPortn = _Pmopm8AlmChannel40PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1, 6),
    _Pmopm8AlmChannel40PowerHighPortn_Type()
)
pmopm8AlmChannel40PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel40PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel40OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel40OosPortn_Object = MibTableColumn
pmopm8AlmChannel40OosPortn = _Pmopm8AlmChannel40OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 328, 1, 7),
    _Pmopm8AlmChannel40OosPortn_Type()
)
pmopm8AlmChannel40OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel40OosPortn.setStatus("current")
_Pmopm8Almchannel41PortTable_Object = MibTable
pmopm8Almchannel41PortTable = _Pmopm8Almchannel41PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel41PortTable.setStatus("current")
_Pmopm8Almchannel41PortEntry_Object = MibTableRow
pmopm8Almchannel41PortEntry = _Pmopm8Almchannel41PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1)
)
pmopm8Almchannel41PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel41PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel41PortEntry.setStatus("current")


class _Pmopm8Almchannel41PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel41PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel41PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel41PortIndex_Object = MibTableColumn
pmopm8Almchannel41PortIndex = _Pmopm8Almchannel41PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1, 1),
    _Pmopm8Almchannel41PortIndex_Type()
)
pmopm8Almchannel41PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel41PortIndex.setStatus("current")
_Pmopm8AlmChannel41AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel41AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel41AbsentPortn = _Pmopm8AlmChannel41AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1, 2),
    _Pmopm8AlmChannel41AbsentPortn_Type()
)
pmopm8AlmChannel41AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel41AbsentPortn.setStatus("current")
_Pmopm8AlmChannel41MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel41MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel41MismatchPortn = _Pmopm8AlmChannel41MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1, 3),
    _Pmopm8AlmChannel41MismatchPortn_Type()
)
pmopm8AlmChannel41MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel41MismatchPortn.setStatus("current")
_Pmopm8AlmChannel41BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel41BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel41BalancedPortn = _Pmopm8AlmChannel41BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1, 4),
    _Pmopm8AlmChannel41BalancedPortn_Type()
)
pmopm8AlmChannel41BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel41BalancedPortn.setStatus("current")
_Pmopm8AlmChannel41PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel41PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel41PowerLowPortn = _Pmopm8AlmChannel41PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1, 5),
    _Pmopm8AlmChannel41PowerLowPortn_Type()
)
pmopm8AlmChannel41PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel41PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel41PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel41PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel41PowerHighPortn = _Pmopm8AlmChannel41PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1, 6),
    _Pmopm8AlmChannel41PowerHighPortn_Type()
)
pmopm8AlmChannel41PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel41PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel41OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel41OosPortn_Object = MibTableColumn
pmopm8AlmChannel41OosPortn = _Pmopm8AlmChannel41OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 336, 1, 7),
    _Pmopm8AlmChannel41OosPortn_Type()
)
pmopm8AlmChannel41OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel41OosPortn.setStatus("current")
_Pmopm8Almchannel42PortTable_Object = MibTable
pmopm8Almchannel42PortTable = _Pmopm8Almchannel42PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel42PortTable.setStatus("current")
_Pmopm8Almchannel42PortEntry_Object = MibTableRow
pmopm8Almchannel42PortEntry = _Pmopm8Almchannel42PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1)
)
pmopm8Almchannel42PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel42PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel42PortEntry.setStatus("current")


class _Pmopm8Almchannel42PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel42PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel42PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel42PortIndex_Object = MibTableColumn
pmopm8Almchannel42PortIndex = _Pmopm8Almchannel42PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1, 1),
    _Pmopm8Almchannel42PortIndex_Type()
)
pmopm8Almchannel42PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel42PortIndex.setStatus("current")
_Pmopm8AlmChannel42AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel42AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel42AbsentPortn = _Pmopm8AlmChannel42AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1, 2),
    _Pmopm8AlmChannel42AbsentPortn_Type()
)
pmopm8AlmChannel42AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel42AbsentPortn.setStatus("current")
_Pmopm8AlmChannel42MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel42MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel42MismatchPortn = _Pmopm8AlmChannel42MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1, 3),
    _Pmopm8AlmChannel42MismatchPortn_Type()
)
pmopm8AlmChannel42MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel42MismatchPortn.setStatus("current")
_Pmopm8AlmChannel42BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel42BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel42BalancedPortn = _Pmopm8AlmChannel42BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1, 4),
    _Pmopm8AlmChannel42BalancedPortn_Type()
)
pmopm8AlmChannel42BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel42BalancedPortn.setStatus("current")
_Pmopm8AlmChannel42PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel42PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel42PowerLowPortn = _Pmopm8AlmChannel42PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1, 5),
    _Pmopm8AlmChannel42PowerLowPortn_Type()
)
pmopm8AlmChannel42PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel42PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel42PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel42PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel42PowerHighPortn = _Pmopm8AlmChannel42PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1, 6),
    _Pmopm8AlmChannel42PowerHighPortn_Type()
)
pmopm8AlmChannel42PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel42PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel42OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel42OosPortn_Object = MibTableColumn
pmopm8AlmChannel42OosPortn = _Pmopm8AlmChannel42OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 344, 1, 7),
    _Pmopm8AlmChannel42OosPortn_Type()
)
pmopm8AlmChannel42OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel42OosPortn.setStatus("current")
_Pmopm8Almchannel43PortTable_Object = MibTable
pmopm8Almchannel43PortTable = _Pmopm8Almchannel43PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel43PortTable.setStatus("current")
_Pmopm8Almchannel43PortEntry_Object = MibTableRow
pmopm8Almchannel43PortEntry = _Pmopm8Almchannel43PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1)
)
pmopm8Almchannel43PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel43PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel43PortEntry.setStatus("current")


class _Pmopm8Almchannel43PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel43PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel43PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel43PortIndex_Object = MibTableColumn
pmopm8Almchannel43PortIndex = _Pmopm8Almchannel43PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1, 1),
    _Pmopm8Almchannel43PortIndex_Type()
)
pmopm8Almchannel43PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel43PortIndex.setStatus("current")
_Pmopm8AlmChannel43AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel43AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel43AbsentPortn = _Pmopm8AlmChannel43AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1, 2),
    _Pmopm8AlmChannel43AbsentPortn_Type()
)
pmopm8AlmChannel43AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel43AbsentPortn.setStatus("current")
_Pmopm8AlmChannel43MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel43MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel43MismatchPortn = _Pmopm8AlmChannel43MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1, 3),
    _Pmopm8AlmChannel43MismatchPortn_Type()
)
pmopm8AlmChannel43MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel43MismatchPortn.setStatus("current")
_Pmopm8AlmChannel43BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel43BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel43BalancedPortn = _Pmopm8AlmChannel43BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1, 4),
    _Pmopm8AlmChannel43BalancedPortn_Type()
)
pmopm8AlmChannel43BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel43BalancedPortn.setStatus("current")
_Pmopm8AlmChannel43PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel43PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel43PowerLowPortn = _Pmopm8AlmChannel43PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1, 5),
    _Pmopm8AlmChannel43PowerLowPortn_Type()
)
pmopm8AlmChannel43PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel43PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel43PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel43PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel43PowerHighPortn = _Pmopm8AlmChannel43PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1, 6),
    _Pmopm8AlmChannel43PowerHighPortn_Type()
)
pmopm8AlmChannel43PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel43PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel43OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel43OosPortn_Object = MibTableColumn
pmopm8AlmChannel43OosPortn = _Pmopm8AlmChannel43OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 352, 1, 7),
    _Pmopm8AlmChannel43OosPortn_Type()
)
pmopm8AlmChannel43OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel43OosPortn.setStatus("current")
_Pmopm8Almchannel44PortTable_Object = MibTable
pmopm8Almchannel44PortTable = _Pmopm8Almchannel44PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel44PortTable.setStatus("current")
_Pmopm8Almchannel44PortEntry_Object = MibTableRow
pmopm8Almchannel44PortEntry = _Pmopm8Almchannel44PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1)
)
pmopm8Almchannel44PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel44PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel44PortEntry.setStatus("current")


class _Pmopm8Almchannel44PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel44PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel44PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel44PortIndex_Object = MibTableColumn
pmopm8Almchannel44PortIndex = _Pmopm8Almchannel44PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1, 1),
    _Pmopm8Almchannel44PortIndex_Type()
)
pmopm8Almchannel44PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel44PortIndex.setStatus("current")
_Pmopm8AlmChannel44AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel44AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel44AbsentPortn = _Pmopm8AlmChannel44AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1, 2),
    _Pmopm8AlmChannel44AbsentPortn_Type()
)
pmopm8AlmChannel44AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel44AbsentPortn.setStatus("current")
_Pmopm8AlmChannel44MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel44MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel44MismatchPortn = _Pmopm8AlmChannel44MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1, 3),
    _Pmopm8AlmChannel44MismatchPortn_Type()
)
pmopm8AlmChannel44MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel44MismatchPortn.setStatus("current")
_Pmopm8AlmChannel44BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel44BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel44BalancedPortn = _Pmopm8AlmChannel44BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1, 4),
    _Pmopm8AlmChannel44BalancedPortn_Type()
)
pmopm8AlmChannel44BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel44BalancedPortn.setStatus("current")
_Pmopm8AlmChannel44PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel44PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel44PowerLowPortn = _Pmopm8AlmChannel44PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1, 5),
    _Pmopm8AlmChannel44PowerLowPortn_Type()
)
pmopm8AlmChannel44PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel44PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel44PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel44PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel44PowerHighPortn = _Pmopm8AlmChannel44PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1, 6),
    _Pmopm8AlmChannel44PowerHighPortn_Type()
)
pmopm8AlmChannel44PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel44PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel44OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel44OosPortn_Object = MibTableColumn
pmopm8AlmChannel44OosPortn = _Pmopm8AlmChannel44OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 360, 1, 7),
    _Pmopm8AlmChannel44OosPortn_Type()
)
pmopm8AlmChannel44OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel44OosPortn.setStatus("current")
_Pmopm8Almchannel45PortTable_Object = MibTable
pmopm8Almchannel45PortTable = _Pmopm8Almchannel45PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel45PortTable.setStatus("current")
_Pmopm8Almchannel45PortEntry_Object = MibTableRow
pmopm8Almchannel45PortEntry = _Pmopm8Almchannel45PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1)
)
pmopm8Almchannel45PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel45PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel45PortEntry.setStatus("current")


class _Pmopm8Almchannel45PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel45PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel45PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel45PortIndex_Object = MibTableColumn
pmopm8Almchannel45PortIndex = _Pmopm8Almchannel45PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1, 1),
    _Pmopm8Almchannel45PortIndex_Type()
)
pmopm8Almchannel45PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel45PortIndex.setStatus("current")
_Pmopm8AlmChannel45AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel45AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel45AbsentPortn = _Pmopm8AlmChannel45AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1, 2),
    _Pmopm8AlmChannel45AbsentPortn_Type()
)
pmopm8AlmChannel45AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel45AbsentPortn.setStatus("current")
_Pmopm8AlmChannel45MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel45MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel45MismatchPortn = _Pmopm8AlmChannel45MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1, 3),
    _Pmopm8AlmChannel45MismatchPortn_Type()
)
pmopm8AlmChannel45MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel45MismatchPortn.setStatus("current")
_Pmopm8AlmChannel45BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel45BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel45BalancedPortn = _Pmopm8AlmChannel45BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1, 4),
    _Pmopm8AlmChannel45BalancedPortn_Type()
)
pmopm8AlmChannel45BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel45BalancedPortn.setStatus("current")
_Pmopm8AlmChannel45PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel45PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel45PowerLowPortn = _Pmopm8AlmChannel45PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1, 5),
    _Pmopm8AlmChannel45PowerLowPortn_Type()
)
pmopm8AlmChannel45PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel45PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel45PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel45PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel45PowerHighPortn = _Pmopm8AlmChannel45PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1, 6),
    _Pmopm8AlmChannel45PowerHighPortn_Type()
)
pmopm8AlmChannel45PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel45PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel45OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel45OosPortn_Object = MibTableColumn
pmopm8AlmChannel45OosPortn = _Pmopm8AlmChannel45OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 368, 1, 7),
    _Pmopm8AlmChannel45OosPortn_Type()
)
pmopm8AlmChannel45OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel45OosPortn.setStatus("current")
_Pmopm8Almchannel46PortTable_Object = MibTable
pmopm8Almchannel46PortTable = _Pmopm8Almchannel46PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel46PortTable.setStatus("current")
_Pmopm8Almchannel46PortEntry_Object = MibTableRow
pmopm8Almchannel46PortEntry = _Pmopm8Almchannel46PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1)
)
pmopm8Almchannel46PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel46PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel46PortEntry.setStatus("current")


class _Pmopm8Almchannel46PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel46PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel46PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel46PortIndex_Object = MibTableColumn
pmopm8Almchannel46PortIndex = _Pmopm8Almchannel46PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1, 1),
    _Pmopm8Almchannel46PortIndex_Type()
)
pmopm8Almchannel46PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel46PortIndex.setStatus("current")
_Pmopm8AlmChannel46AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel46AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel46AbsentPortn = _Pmopm8AlmChannel46AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1, 2),
    _Pmopm8AlmChannel46AbsentPortn_Type()
)
pmopm8AlmChannel46AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel46AbsentPortn.setStatus("current")
_Pmopm8AlmChannel46MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel46MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel46MismatchPortn = _Pmopm8AlmChannel46MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1, 3),
    _Pmopm8AlmChannel46MismatchPortn_Type()
)
pmopm8AlmChannel46MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel46MismatchPortn.setStatus("current")
_Pmopm8AlmChannel46BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel46BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel46BalancedPortn = _Pmopm8AlmChannel46BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1, 4),
    _Pmopm8AlmChannel46BalancedPortn_Type()
)
pmopm8AlmChannel46BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel46BalancedPortn.setStatus("current")
_Pmopm8AlmChannel46PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel46PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel46PowerLowPortn = _Pmopm8AlmChannel46PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1, 5),
    _Pmopm8AlmChannel46PowerLowPortn_Type()
)
pmopm8AlmChannel46PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel46PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel46PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel46PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel46PowerHighPortn = _Pmopm8AlmChannel46PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1, 6),
    _Pmopm8AlmChannel46PowerHighPortn_Type()
)
pmopm8AlmChannel46PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel46PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel46OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel46OosPortn_Object = MibTableColumn
pmopm8AlmChannel46OosPortn = _Pmopm8AlmChannel46OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 376, 1, 7),
    _Pmopm8AlmChannel46OosPortn_Type()
)
pmopm8AlmChannel46OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel46OosPortn.setStatus("current")
_Pmopm8Almchannel47PortTable_Object = MibTable
pmopm8Almchannel47PortTable = _Pmopm8Almchannel47PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel47PortTable.setStatus("current")
_Pmopm8Almchannel47PortEntry_Object = MibTableRow
pmopm8Almchannel47PortEntry = _Pmopm8Almchannel47PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1)
)
pmopm8Almchannel47PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel47PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel47PortEntry.setStatus("current")


class _Pmopm8Almchannel47PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel47PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel47PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel47PortIndex_Object = MibTableColumn
pmopm8Almchannel47PortIndex = _Pmopm8Almchannel47PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1, 1),
    _Pmopm8Almchannel47PortIndex_Type()
)
pmopm8Almchannel47PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel47PortIndex.setStatus("current")
_Pmopm8AlmChannel47AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel47AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel47AbsentPortn = _Pmopm8AlmChannel47AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1, 2),
    _Pmopm8AlmChannel47AbsentPortn_Type()
)
pmopm8AlmChannel47AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel47AbsentPortn.setStatus("current")
_Pmopm8AlmChannel47MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel47MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel47MismatchPortn = _Pmopm8AlmChannel47MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1, 3),
    _Pmopm8AlmChannel47MismatchPortn_Type()
)
pmopm8AlmChannel47MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel47MismatchPortn.setStatus("current")
_Pmopm8AlmChannel47BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel47BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel47BalancedPortn = _Pmopm8AlmChannel47BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1, 4),
    _Pmopm8AlmChannel47BalancedPortn_Type()
)
pmopm8AlmChannel47BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel47BalancedPortn.setStatus("current")
_Pmopm8AlmChannel47PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel47PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel47PowerLowPortn = _Pmopm8AlmChannel47PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1, 5),
    _Pmopm8AlmChannel47PowerLowPortn_Type()
)
pmopm8AlmChannel47PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel47PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel47PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel47PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel47PowerHighPortn = _Pmopm8AlmChannel47PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1, 6),
    _Pmopm8AlmChannel47PowerHighPortn_Type()
)
pmopm8AlmChannel47PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel47PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel47OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel47OosPortn_Object = MibTableColumn
pmopm8AlmChannel47OosPortn = _Pmopm8AlmChannel47OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 384, 1, 7),
    _Pmopm8AlmChannel47OosPortn_Type()
)
pmopm8AlmChannel47OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel47OosPortn.setStatus("current")
_Pmopm8Almchannel48PortTable_Object = MibTable
pmopm8Almchannel48PortTable = _Pmopm8Almchannel48PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel48PortTable.setStatus("current")
_Pmopm8Almchannel48PortEntry_Object = MibTableRow
pmopm8Almchannel48PortEntry = _Pmopm8Almchannel48PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1)
)
pmopm8Almchannel48PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel48PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel48PortEntry.setStatus("current")


class _Pmopm8Almchannel48PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel48PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel48PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel48PortIndex_Object = MibTableColumn
pmopm8Almchannel48PortIndex = _Pmopm8Almchannel48PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1, 1),
    _Pmopm8Almchannel48PortIndex_Type()
)
pmopm8Almchannel48PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel48PortIndex.setStatus("current")
_Pmopm8AlmChannel48AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel48AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel48AbsentPortn = _Pmopm8AlmChannel48AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1, 2),
    _Pmopm8AlmChannel48AbsentPortn_Type()
)
pmopm8AlmChannel48AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel48AbsentPortn.setStatus("current")
_Pmopm8AlmChannel48MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel48MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel48MismatchPortn = _Pmopm8AlmChannel48MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1, 3),
    _Pmopm8AlmChannel48MismatchPortn_Type()
)
pmopm8AlmChannel48MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel48MismatchPortn.setStatus("current")
_Pmopm8AlmChannel48BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel48BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel48BalancedPortn = _Pmopm8AlmChannel48BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1, 4),
    _Pmopm8AlmChannel48BalancedPortn_Type()
)
pmopm8AlmChannel48BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel48BalancedPortn.setStatus("current")
_Pmopm8AlmChannel48PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel48PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel48PowerLowPortn = _Pmopm8AlmChannel48PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1, 5),
    _Pmopm8AlmChannel48PowerLowPortn_Type()
)
pmopm8AlmChannel48PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel48PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel48PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel48PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel48PowerHighPortn = _Pmopm8AlmChannel48PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1, 6),
    _Pmopm8AlmChannel48PowerHighPortn_Type()
)
pmopm8AlmChannel48PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel48PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel48OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel48OosPortn_Object = MibTableColumn
pmopm8AlmChannel48OosPortn = _Pmopm8AlmChannel48OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 392, 1, 7),
    _Pmopm8AlmChannel48OosPortn_Type()
)
pmopm8AlmChannel48OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel48OosPortn.setStatus("current")
_Pmopm8Almchannel49PortTable_Object = MibTable
pmopm8Almchannel49PortTable = _Pmopm8Almchannel49PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel49PortTable.setStatus("current")
_Pmopm8Almchannel49PortEntry_Object = MibTableRow
pmopm8Almchannel49PortEntry = _Pmopm8Almchannel49PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1)
)
pmopm8Almchannel49PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel49PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel49PortEntry.setStatus("current")


class _Pmopm8Almchannel49PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel49PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel49PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel49PortIndex_Object = MibTableColumn
pmopm8Almchannel49PortIndex = _Pmopm8Almchannel49PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1, 1),
    _Pmopm8Almchannel49PortIndex_Type()
)
pmopm8Almchannel49PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel49PortIndex.setStatus("current")
_Pmopm8AlmChannel49AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel49AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel49AbsentPortn = _Pmopm8AlmChannel49AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1, 2),
    _Pmopm8AlmChannel49AbsentPortn_Type()
)
pmopm8AlmChannel49AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel49AbsentPortn.setStatus("current")
_Pmopm8AlmChannel49MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel49MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel49MismatchPortn = _Pmopm8AlmChannel49MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1, 3),
    _Pmopm8AlmChannel49MismatchPortn_Type()
)
pmopm8AlmChannel49MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel49MismatchPortn.setStatus("current")
_Pmopm8AlmChannel49BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel49BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel49BalancedPortn = _Pmopm8AlmChannel49BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1, 4),
    _Pmopm8AlmChannel49BalancedPortn_Type()
)
pmopm8AlmChannel49BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel49BalancedPortn.setStatus("current")
_Pmopm8AlmChannel49PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel49PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel49PowerLowPortn = _Pmopm8AlmChannel49PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1, 5),
    _Pmopm8AlmChannel49PowerLowPortn_Type()
)
pmopm8AlmChannel49PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel49PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel49PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel49PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel49PowerHighPortn = _Pmopm8AlmChannel49PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1, 6),
    _Pmopm8AlmChannel49PowerHighPortn_Type()
)
pmopm8AlmChannel49PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel49PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel49OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel49OosPortn_Object = MibTableColumn
pmopm8AlmChannel49OosPortn = _Pmopm8AlmChannel49OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 400, 1, 7),
    _Pmopm8AlmChannel49OosPortn_Type()
)
pmopm8AlmChannel49OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel49OosPortn.setStatus("current")
_Pmopm8Almchannel50PortTable_Object = MibTable
pmopm8Almchannel50PortTable = _Pmopm8Almchannel50PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel50PortTable.setStatus("current")
_Pmopm8Almchannel50PortEntry_Object = MibTableRow
pmopm8Almchannel50PortEntry = _Pmopm8Almchannel50PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1)
)
pmopm8Almchannel50PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel50PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel50PortEntry.setStatus("current")


class _Pmopm8Almchannel50PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel50PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel50PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel50PortIndex_Object = MibTableColumn
pmopm8Almchannel50PortIndex = _Pmopm8Almchannel50PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1, 1),
    _Pmopm8Almchannel50PortIndex_Type()
)
pmopm8Almchannel50PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel50PortIndex.setStatus("current")
_Pmopm8AlmChannel50AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel50AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel50AbsentPortn = _Pmopm8AlmChannel50AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1, 2),
    _Pmopm8AlmChannel50AbsentPortn_Type()
)
pmopm8AlmChannel50AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel50AbsentPortn.setStatus("current")
_Pmopm8AlmChannel50MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel50MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel50MismatchPortn = _Pmopm8AlmChannel50MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1, 3),
    _Pmopm8AlmChannel50MismatchPortn_Type()
)
pmopm8AlmChannel50MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel50MismatchPortn.setStatus("current")
_Pmopm8AlmChannel50BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel50BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel50BalancedPortn = _Pmopm8AlmChannel50BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1, 4),
    _Pmopm8AlmChannel50BalancedPortn_Type()
)
pmopm8AlmChannel50BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel50BalancedPortn.setStatus("current")
_Pmopm8AlmChannel50PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel50PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel50PowerLowPortn = _Pmopm8AlmChannel50PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1, 5),
    _Pmopm8AlmChannel50PowerLowPortn_Type()
)
pmopm8AlmChannel50PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel50PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel50PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel50PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel50PowerHighPortn = _Pmopm8AlmChannel50PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1, 6),
    _Pmopm8AlmChannel50PowerHighPortn_Type()
)
pmopm8AlmChannel50PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel50PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel50OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel50OosPortn_Object = MibTableColumn
pmopm8AlmChannel50OosPortn = _Pmopm8AlmChannel50OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 408, 1, 7),
    _Pmopm8AlmChannel50OosPortn_Type()
)
pmopm8AlmChannel50OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel50OosPortn.setStatus("current")
_Pmopm8Almchannel51PortTable_Object = MibTable
pmopm8Almchannel51PortTable = _Pmopm8Almchannel51PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel51PortTable.setStatus("current")
_Pmopm8Almchannel51PortEntry_Object = MibTableRow
pmopm8Almchannel51PortEntry = _Pmopm8Almchannel51PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1)
)
pmopm8Almchannel51PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel51PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel51PortEntry.setStatus("current")


class _Pmopm8Almchannel51PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel51PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel51PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel51PortIndex_Object = MibTableColumn
pmopm8Almchannel51PortIndex = _Pmopm8Almchannel51PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1, 1),
    _Pmopm8Almchannel51PortIndex_Type()
)
pmopm8Almchannel51PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel51PortIndex.setStatus("current")
_Pmopm8AlmChannel51AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel51AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel51AbsentPortn = _Pmopm8AlmChannel51AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1, 2),
    _Pmopm8AlmChannel51AbsentPortn_Type()
)
pmopm8AlmChannel51AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel51AbsentPortn.setStatus("current")
_Pmopm8AlmChannel51MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel51MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel51MismatchPortn = _Pmopm8AlmChannel51MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1, 3),
    _Pmopm8AlmChannel51MismatchPortn_Type()
)
pmopm8AlmChannel51MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel51MismatchPortn.setStatus("current")
_Pmopm8AlmChannel51BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel51BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel51BalancedPortn = _Pmopm8AlmChannel51BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1, 4),
    _Pmopm8AlmChannel51BalancedPortn_Type()
)
pmopm8AlmChannel51BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel51BalancedPortn.setStatus("current")
_Pmopm8AlmChannel51PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel51PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel51PowerLowPortn = _Pmopm8AlmChannel51PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1, 5),
    _Pmopm8AlmChannel51PowerLowPortn_Type()
)
pmopm8AlmChannel51PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel51PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel51PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel51PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel51PowerHighPortn = _Pmopm8AlmChannel51PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1, 6),
    _Pmopm8AlmChannel51PowerHighPortn_Type()
)
pmopm8AlmChannel51PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel51PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel51OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel51OosPortn_Object = MibTableColumn
pmopm8AlmChannel51OosPortn = _Pmopm8AlmChannel51OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 416, 1, 7),
    _Pmopm8AlmChannel51OosPortn_Type()
)
pmopm8AlmChannel51OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel51OosPortn.setStatus("current")
_Pmopm8Almchannel52PortTable_Object = MibTable
pmopm8Almchannel52PortTable = _Pmopm8Almchannel52PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel52PortTable.setStatus("current")
_Pmopm8Almchannel52PortEntry_Object = MibTableRow
pmopm8Almchannel52PortEntry = _Pmopm8Almchannel52PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1)
)
pmopm8Almchannel52PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel52PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel52PortEntry.setStatus("current")


class _Pmopm8Almchannel52PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel52PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel52PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel52PortIndex_Object = MibTableColumn
pmopm8Almchannel52PortIndex = _Pmopm8Almchannel52PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1, 1),
    _Pmopm8Almchannel52PortIndex_Type()
)
pmopm8Almchannel52PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel52PortIndex.setStatus("current")
_Pmopm8AlmChannel52AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel52AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel52AbsentPortn = _Pmopm8AlmChannel52AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1, 2),
    _Pmopm8AlmChannel52AbsentPortn_Type()
)
pmopm8AlmChannel52AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel52AbsentPortn.setStatus("current")
_Pmopm8AlmChannel52MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel52MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel52MismatchPortn = _Pmopm8AlmChannel52MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1, 3),
    _Pmopm8AlmChannel52MismatchPortn_Type()
)
pmopm8AlmChannel52MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel52MismatchPortn.setStatus("current")
_Pmopm8AlmChannel52BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel52BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel52BalancedPortn = _Pmopm8AlmChannel52BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1, 4),
    _Pmopm8AlmChannel52BalancedPortn_Type()
)
pmopm8AlmChannel52BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel52BalancedPortn.setStatus("current")
_Pmopm8AlmChannel52PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel52PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel52PowerLowPortn = _Pmopm8AlmChannel52PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1, 5),
    _Pmopm8AlmChannel52PowerLowPortn_Type()
)
pmopm8AlmChannel52PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel52PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel52PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel52PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel52PowerHighPortn = _Pmopm8AlmChannel52PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1, 6),
    _Pmopm8AlmChannel52PowerHighPortn_Type()
)
pmopm8AlmChannel52PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel52PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel52OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel52OosPortn_Object = MibTableColumn
pmopm8AlmChannel52OosPortn = _Pmopm8AlmChannel52OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 424, 1, 7),
    _Pmopm8AlmChannel52OosPortn_Type()
)
pmopm8AlmChannel52OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel52OosPortn.setStatus("current")
_Pmopm8Almchannel53PortTable_Object = MibTable
pmopm8Almchannel53PortTable = _Pmopm8Almchannel53PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel53PortTable.setStatus("current")
_Pmopm8Almchannel53PortEntry_Object = MibTableRow
pmopm8Almchannel53PortEntry = _Pmopm8Almchannel53PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1)
)
pmopm8Almchannel53PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel53PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel53PortEntry.setStatus("current")


class _Pmopm8Almchannel53PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel53PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel53PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel53PortIndex_Object = MibTableColumn
pmopm8Almchannel53PortIndex = _Pmopm8Almchannel53PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1, 1),
    _Pmopm8Almchannel53PortIndex_Type()
)
pmopm8Almchannel53PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel53PortIndex.setStatus("current")
_Pmopm8AlmChannel53AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel53AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel53AbsentPortn = _Pmopm8AlmChannel53AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1, 2),
    _Pmopm8AlmChannel53AbsentPortn_Type()
)
pmopm8AlmChannel53AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel53AbsentPortn.setStatus("current")
_Pmopm8AlmChannel53MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel53MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel53MismatchPortn = _Pmopm8AlmChannel53MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1, 3),
    _Pmopm8AlmChannel53MismatchPortn_Type()
)
pmopm8AlmChannel53MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel53MismatchPortn.setStatus("current")
_Pmopm8AlmChannel53BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel53BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel53BalancedPortn = _Pmopm8AlmChannel53BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1, 4),
    _Pmopm8AlmChannel53BalancedPortn_Type()
)
pmopm8AlmChannel53BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel53BalancedPortn.setStatus("current")
_Pmopm8AlmChannel53PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel53PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel53PowerLowPortn = _Pmopm8AlmChannel53PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1, 5),
    _Pmopm8AlmChannel53PowerLowPortn_Type()
)
pmopm8AlmChannel53PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel53PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel53PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel53PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel53PowerHighPortn = _Pmopm8AlmChannel53PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1, 6),
    _Pmopm8AlmChannel53PowerHighPortn_Type()
)
pmopm8AlmChannel53PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel53PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel53OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel53OosPortn_Object = MibTableColumn
pmopm8AlmChannel53OosPortn = _Pmopm8AlmChannel53OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 432, 1, 7),
    _Pmopm8AlmChannel53OosPortn_Type()
)
pmopm8AlmChannel53OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel53OosPortn.setStatus("current")
_Pmopm8Almchannel54PortTable_Object = MibTable
pmopm8Almchannel54PortTable = _Pmopm8Almchannel54PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel54PortTable.setStatus("current")
_Pmopm8Almchannel54PortEntry_Object = MibTableRow
pmopm8Almchannel54PortEntry = _Pmopm8Almchannel54PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1)
)
pmopm8Almchannel54PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel54PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel54PortEntry.setStatus("current")


class _Pmopm8Almchannel54PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel54PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel54PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel54PortIndex_Object = MibTableColumn
pmopm8Almchannel54PortIndex = _Pmopm8Almchannel54PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1, 1),
    _Pmopm8Almchannel54PortIndex_Type()
)
pmopm8Almchannel54PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel54PortIndex.setStatus("current")
_Pmopm8AlmChannel54AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel54AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel54AbsentPortn = _Pmopm8AlmChannel54AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1, 2),
    _Pmopm8AlmChannel54AbsentPortn_Type()
)
pmopm8AlmChannel54AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel54AbsentPortn.setStatus("current")
_Pmopm8AlmChannel54MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel54MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel54MismatchPortn = _Pmopm8AlmChannel54MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1, 3),
    _Pmopm8AlmChannel54MismatchPortn_Type()
)
pmopm8AlmChannel54MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel54MismatchPortn.setStatus("current")
_Pmopm8AlmChannel54BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel54BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel54BalancedPortn = _Pmopm8AlmChannel54BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1, 4),
    _Pmopm8AlmChannel54BalancedPortn_Type()
)
pmopm8AlmChannel54BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel54BalancedPortn.setStatus("current")
_Pmopm8AlmChannel54PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel54PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel54PowerLowPortn = _Pmopm8AlmChannel54PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1, 5),
    _Pmopm8AlmChannel54PowerLowPortn_Type()
)
pmopm8AlmChannel54PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel54PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel54PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel54PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel54PowerHighPortn = _Pmopm8AlmChannel54PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1, 6),
    _Pmopm8AlmChannel54PowerHighPortn_Type()
)
pmopm8AlmChannel54PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel54PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel54OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel54OosPortn_Object = MibTableColumn
pmopm8AlmChannel54OosPortn = _Pmopm8AlmChannel54OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 440, 1, 7),
    _Pmopm8AlmChannel54OosPortn_Type()
)
pmopm8AlmChannel54OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel54OosPortn.setStatus("current")
_Pmopm8Almchannel55PortTable_Object = MibTable
pmopm8Almchannel55PortTable = _Pmopm8Almchannel55PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel55PortTable.setStatus("current")
_Pmopm8Almchannel55PortEntry_Object = MibTableRow
pmopm8Almchannel55PortEntry = _Pmopm8Almchannel55PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1)
)
pmopm8Almchannel55PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel55PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel55PortEntry.setStatus("current")


class _Pmopm8Almchannel55PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel55PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel55PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel55PortIndex_Object = MibTableColumn
pmopm8Almchannel55PortIndex = _Pmopm8Almchannel55PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1, 1),
    _Pmopm8Almchannel55PortIndex_Type()
)
pmopm8Almchannel55PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel55PortIndex.setStatus("current")
_Pmopm8AlmChannel55AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel55AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel55AbsentPortn = _Pmopm8AlmChannel55AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1, 2),
    _Pmopm8AlmChannel55AbsentPortn_Type()
)
pmopm8AlmChannel55AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel55AbsentPortn.setStatus("current")
_Pmopm8AlmChannel55MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel55MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel55MismatchPortn = _Pmopm8AlmChannel55MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1, 3),
    _Pmopm8AlmChannel55MismatchPortn_Type()
)
pmopm8AlmChannel55MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel55MismatchPortn.setStatus("current")
_Pmopm8AlmChannel55BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel55BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel55BalancedPortn = _Pmopm8AlmChannel55BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1, 4),
    _Pmopm8AlmChannel55BalancedPortn_Type()
)
pmopm8AlmChannel55BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel55BalancedPortn.setStatus("current")
_Pmopm8AlmChannel55PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel55PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel55PowerLowPortn = _Pmopm8AlmChannel55PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1, 5),
    _Pmopm8AlmChannel55PowerLowPortn_Type()
)
pmopm8AlmChannel55PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel55PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel55PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel55PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel55PowerHighPortn = _Pmopm8AlmChannel55PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1, 6),
    _Pmopm8AlmChannel55PowerHighPortn_Type()
)
pmopm8AlmChannel55PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel55PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel55OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel55OosPortn_Object = MibTableColumn
pmopm8AlmChannel55OosPortn = _Pmopm8AlmChannel55OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 448, 1, 7),
    _Pmopm8AlmChannel55OosPortn_Type()
)
pmopm8AlmChannel55OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel55OosPortn.setStatus("current")
_Pmopm8Almchannel56PortTable_Object = MibTable
pmopm8Almchannel56PortTable = _Pmopm8Almchannel56PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel56PortTable.setStatus("current")
_Pmopm8Almchannel56PortEntry_Object = MibTableRow
pmopm8Almchannel56PortEntry = _Pmopm8Almchannel56PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1)
)
pmopm8Almchannel56PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel56PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel56PortEntry.setStatus("current")


class _Pmopm8Almchannel56PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel56PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel56PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel56PortIndex_Object = MibTableColumn
pmopm8Almchannel56PortIndex = _Pmopm8Almchannel56PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1, 1),
    _Pmopm8Almchannel56PortIndex_Type()
)
pmopm8Almchannel56PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel56PortIndex.setStatus("current")
_Pmopm8AlmChannel56AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel56AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel56AbsentPortn = _Pmopm8AlmChannel56AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1, 2),
    _Pmopm8AlmChannel56AbsentPortn_Type()
)
pmopm8AlmChannel56AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel56AbsentPortn.setStatus("current")
_Pmopm8AlmChannel56MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel56MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel56MismatchPortn = _Pmopm8AlmChannel56MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1, 3),
    _Pmopm8AlmChannel56MismatchPortn_Type()
)
pmopm8AlmChannel56MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel56MismatchPortn.setStatus("current")
_Pmopm8AlmChannel56BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel56BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel56BalancedPortn = _Pmopm8AlmChannel56BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1, 4),
    _Pmopm8AlmChannel56BalancedPortn_Type()
)
pmopm8AlmChannel56BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel56BalancedPortn.setStatus("current")
_Pmopm8AlmChannel56PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel56PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel56PowerLowPortn = _Pmopm8AlmChannel56PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1, 5),
    _Pmopm8AlmChannel56PowerLowPortn_Type()
)
pmopm8AlmChannel56PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel56PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel56PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel56PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel56PowerHighPortn = _Pmopm8AlmChannel56PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1, 6),
    _Pmopm8AlmChannel56PowerHighPortn_Type()
)
pmopm8AlmChannel56PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel56PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel56OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel56OosPortn_Object = MibTableColumn
pmopm8AlmChannel56OosPortn = _Pmopm8AlmChannel56OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 456, 1, 7),
    _Pmopm8AlmChannel56OosPortn_Type()
)
pmopm8AlmChannel56OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel56OosPortn.setStatus("current")
_Pmopm8Almchannel57PortTable_Object = MibTable
pmopm8Almchannel57PortTable = _Pmopm8Almchannel57PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel57PortTable.setStatus("current")
_Pmopm8Almchannel57PortEntry_Object = MibTableRow
pmopm8Almchannel57PortEntry = _Pmopm8Almchannel57PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1)
)
pmopm8Almchannel57PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel57PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel57PortEntry.setStatus("current")


class _Pmopm8Almchannel57PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel57PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel57PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel57PortIndex_Object = MibTableColumn
pmopm8Almchannel57PortIndex = _Pmopm8Almchannel57PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1, 1),
    _Pmopm8Almchannel57PortIndex_Type()
)
pmopm8Almchannel57PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel57PortIndex.setStatus("current")
_Pmopm8AlmChannel57AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel57AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel57AbsentPortn = _Pmopm8AlmChannel57AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1, 2),
    _Pmopm8AlmChannel57AbsentPortn_Type()
)
pmopm8AlmChannel57AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel57AbsentPortn.setStatus("current")
_Pmopm8AlmChannel57MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel57MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel57MismatchPortn = _Pmopm8AlmChannel57MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1, 3),
    _Pmopm8AlmChannel57MismatchPortn_Type()
)
pmopm8AlmChannel57MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel57MismatchPortn.setStatus("current")
_Pmopm8AlmChannel57BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel57BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel57BalancedPortn = _Pmopm8AlmChannel57BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1, 4),
    _Pmopm8AlmChannel57BalancedPortn_Type()
)
pmopm8AlmChannel57BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel57BalancedPortn.setStatus("current")
_Pmopm8AlmChannel57PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel57PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel57PowerLowPortn = _Pmopm8AlmChannel57PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1, 5),
    _Pmopm8AlmChannel57PowerLowPortn_Type()
)
pmopm8AlmChannel57PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel57PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel57PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel57PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel57PowerHighPortn = _Pmopm8AlmChannel57PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1, 6),
    _Pmopm8AlmChannel57PowerHighPortn_Type()
)
pmopm8AlmChannel57PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel57PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel57OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel57OosPortn_Object = MibTableColumn
pmopm8AlmChannel57OosPortn = _Pmopm8AlmChannel57OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 464, 1, 7),
    _Pmopm8AlmChannel57OosPortn_Type()
)
pmopm8AlmChannel57OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel57OosPortn.setStatus("current")
_Pmopm8Almchannel58PortTable_Object = MibTable
pmopm8Almchannel58PortTable = _Pmopm8Almchannel58PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel58PortTable.setStatus("current")
_Pmopm8Almchannel58PortEntry_Object = MibTableRow
pmopm8Almchannel58PortEntry = _Pmopm8Almchannel58PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1)
)
pmopm8Almchannel58PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel58PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel58PortEntry.setStatus("current")


class _Pmopm8Almchannel58PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel58PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel58PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel58PortIndex_Object = MibTableColumn
pmopm8Almchannel58PortIndex = _Pmopm8Almchannel58PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1, 1),
    _Pmopm8Almchannel58PortIndex_Type()
)
pmopm8Almchannel58PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel58PortIndex.setStatus("current")
_Pmopm8AlmChannel58AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel58AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel58AbsentPortn = _Pmopm8AlmChannel58AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1, 2),
    _Pmopm8AlmChannel58AbsentPortn_Type()
)
pmopm8AlmChannel58AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel58AbsentPortn.setStatus("current")
_Pmopm8AlmChannel58MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel58MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel58MismatchPortn = _Pmopm8AlmChannel58MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1, 3),
    _Pmopm8AlmChannel58MismatchPortn_Type()
)
pmopm8AlmChannel58MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel58MismatchPortn.setStatus("current")
_Pmopm8AlmChannel58BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel58BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel58BalancedPortn = _Pmopm8AlmChannel58BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1, 4),
    _Pmopm8AlmChannel58BalancedPortn_Type()
)
pmopm8AlmChannel58BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel58BalancedPortn.setStatus("current")
_Pmopm8AlmChannel58PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel58PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel58PowerLowPortn = _Pmopm8AlmChannel58PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1, 5),
    _Pmopm8AlmChannel58PowerLowPortn_Type()
)
pmopm8AlmChannel58PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel58PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel58PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel58PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel58PowerHighPortn = _Pmopm8AlmChannel58PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1, 6),
    _Pmopm8AlmChannel58PowerHighPortn_Type()
)
pmopm8AlmChannel58PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel58PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel58OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel58OosPortn_Object = MibTableColumn
pmopm8AlmChannel58OosPortn = _Pmopm8AlmChannel58OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 472, 1, 7),
    _Pmopm8AlmChannel58OosPortn_Type()
)
pmopm8AlmChannel58OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel58OosPortn.setStatus("current")
_Pmopm8Almchannel59PortTable_Object = MibTable
pmopm8Almchannel59PortTable = _Pmopm8Almchannel59PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel59PortTable.setStatus("current")
_Pmopm8Almchannel59PortEntry_Object = MibTableRow
pmopm8Almchannel59PortEntry = _Pmopm8Almchannel59PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1)
)
pmopm8Almchannel59PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel59PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel59PortEntry.setStatus("current")


class _Pmopm8Almchannel59PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel59PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel59PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel59PortIndex_Object = MibTableColumn
pmopm8Almchannel59PortIndex = _Pmopm8Almchannel59PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1, 1),
    _Pmopm8Almchannel59PortIndex_Type()
)
pmopm8Almchannel59PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel59PortIndex.setStatus("current")
_Pmopm8AlmChannel59AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel59AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel59AbsentPortn = _Pmopm8AlmChannel59AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1, 2),
    _Pmopm8AlmChannel59AbsentPortn_Type()
)
pmopm8AlmChannel59AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel59AbsentPortn.setStatus("current")
_Pmopm8AlmChannel59MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel59MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel59MismatchPortn = _Pmopm8AlmChannel59MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1, 3),
    _Pmopm8AlmChannel59MismatchPortn_Type()
)
pmopm8AlmChannel59MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel59MismatchPortn.setStatus("current")
_Pmopm8AlmChannel59BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel59BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel59BalancedPortn = _Pmopm8AlmChannel59BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1, 4),
    _Pmopm8AlmChannel59BalancedPortn_Type()
)
pmopm8AlmChannel59BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel59BalancedPortn.setStatus("current")
_Pmopm8AlmChannel59PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel59PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel59PowerLowPortn = _Pmopm8AlmChannel59PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1, 5),
    _Pmopm8AlmChannel59PowerLowPortn_Type()
)
pmopm8AlmChannel59PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel59PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel59PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel59PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel59PowerHighPortn = _Pmopm8AlmChannel59PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1, 6),
    _Pmopm8AlmChannel59PowerHighPortn_Type()
)
pmopm8AlmChannel59PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel59PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel59OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel59OosPortn_Object = MibTableColumn
pmopm8AlmChannel59OosPortn = _Pmopm8AlmChannel59OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 480, 1, 7),
    _Pmopm8AlmChannel59OosPortn_Type()
)
pmopm8AlmChannel59OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel59OosPortn.setStatus("current")
_Pmopm8Almchannel60PortTable_Object = MibTable
pmopm8Almchannel60PortTable = _Pmopm8Almchannel60PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel60PortTable.setStatus("current")
_Pmopm8Almchannel60PortEntry_Object = MibTableRow
pmopm8Almchannel60PortEntry = _Pmopm8Almchannel60PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1)
)
pmopm8Almchannel60PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel60PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel60PortEntry.setStatus("current")


class _Pmopm8Almchannel60PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel60PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel60PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel60PortIndex_Object = MibTableColumn
pmopm8Almchannel60PortIndex = _Pmopm8Almchannel60PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1, 1),
    _Pmopm8Almchannel60PortIndex_Type()
)
pmopm8Almchannel60PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel60PortIndex.setStatus("current")
_Pmopm8AlmChannel60AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel60AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel60AbsentPortn = _Pmopm8AlmChannel60AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1, 2),
    _Pmopm8AlmChannel60AbsentPortn_Type()
)
pmopm8AlmChannel60AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel60AbsentPortn.setStatus("current")
_Pmopm8AlmChannel60MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel60MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel60MismatchPortn = _Pmopm8AlmChannel60MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1, 3),
    _Pmopm8AlmChannel60MismatchPortn_Type()
)
pmopm8AlmChannel60MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel60MismatchPortn.setStatus("current")
_Pmopm8AlmChannel60BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel60BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel60BalancedPortn = _Pmopm8AlmChannel60BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1, 4),
    _Pmopm8AlmChannel60BalancedPortn_Type()
)
pmopm8AlmChannel60BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel60BalancedPortn.setStatus("current")
_Pmopm8AlmChannel60PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel60PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel60PowerLowPortn = _Pmopm8AlmChannel60PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1, 5),
    _Pmopm8AlmChannel60PowerLowPortn_Type()
)
pmopm8AlmChannel60PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel60PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel60PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel60PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel60PowerHighPortn = _Pmopm8AlmChannel60PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1, 6),
    _Pmopm8AlmChannel60PowerHighPortn_Type()
)
pmopm8AlmChannel60PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel60PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel60OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel60OosPortn_Object = MibTableColumn
pmopm8AlmChannel60OosPortn = _Pmopm8AlmChannel60OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 488, 1, 7),
    _Pmopm8AlmChannel60OosPortn_Type()
)
pmopm8AlmChannel60OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel60OosPortn.setStatus("current")
_Pmopm8Almchannel61PortTable_Object = MibTable
pmopm8Almchannel61PortTable = _Pmopm8Almchannel61PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel61PortTable.setStatus("current")
_Pmopm8Almchannel61PortEntry_Object = MibTableRow
pmopm8Almchannel61PortEntry = _Pmopm8Almchannel61PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1)
)
pmopm8Almchannel61PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel61PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel61PortEntry.setStatus("current")


class _Pmopm8Almchannel61PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel61PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel61PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel61PortIndex_Object = MibTableColumn
pmopm8Almchannel61PortIndex = _Pmopm8Almchannel61PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1, 1),
    _Pmopm8Almchannel61PortIndex_Type()
)
pmopm8Almchannel61PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel61PortIndex.setStatus("current")
_Pmopm8AlmChannel61AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel61AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel61AbsentPortn = _Pmopm8AlmChannel61AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1, 2),
    _Pmopm8AlmChannel61AbsentPortn_Type()
)
pmopm8AlmChannel61AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel61AbsentPortn.setStatus("current")
_Pmopm8AlmChannel61MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel61MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel61MismatchPortn = _Pmopm8AlmChannel61MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1, 3),
    _Pmopm8AlmChannel61MismatchPortn_Type()
)
pmopm8AlmChannel61MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel61MismatchPortn.setStatus("current")
_Pmopm8AlmChannel61BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel61BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel61BalancedPortn = _Pmopm8AlmChannel61BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1, 4),
    _Pmopm8AlmChannel61BalancedPortn_Type()
)
pmopm8AlmChannel61BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel61BalancedPortn.setStatus("current")
_Pmopm8AlmChannel61PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel61PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel61PowerLowPortn = _Pmopm8AlmChannel61PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1, 5),
    _Pmopm8AlmChannel61PowerLowPortn_Type()
)
pmopm8AlmChannel61PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel61PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel61PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel61PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel61PowerHighPortn = _Pmopm8AlmChannel61PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1, 6),
    _Pmopm8AlmChannel61PowerHighPortn_Type()
)
pmopm8AlmChannel61PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel61PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel61OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel61OosPortn_Object = MibTableColumn
pmopm8AlmChannel61OosPortn = _Pmopm8AlmChannel61OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 496, 1, 7),
    _Pmopm8AlmChannel61OosPortn_Type()
)
pmopm8AlmChannel61OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel61OosPortn.setStatus("current")
_Pmopm8Almchannel62PortTable_Object = MibTable
pmopm8Almchannel62PortTable = _Pmopm8Almchannel62PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel62PortTable.setStatus("current")
_Pmopm8Almchannel62PortEntry_Object = MibTableRow
pmopm8Almchannel62PortEntry = _Pmopm8Almchannel62PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1)
)
pmopm8Almchannel62PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel62PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel62PortEntry.setStatus("current")


class _Pmopm8Almchannel62PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel62PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel62PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel62PortIndex_Object = MibTableColumn
pmopm8Almchannel62PortIndex = _Pmopm8Almchannel62PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1, 1),
    _Pmopm8Almchannel62PortIndex_Type()
)
pmopm8Almchannel62PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel62PortIndex.setStatus("current")
_Pmopm8AlmChannel62AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel62AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel62AbsentPortn = _Pmopm8AlmChannel62AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1, 2),
    _Pmopm8AlmChannel62AbsentPortn_Type()
)
pmopm8AlmChannel62AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel62AbsentPortn.setStatus("current")
_Pmopm8AlmChannel62MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel62MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel62MismatchPortn = _Pmopm8AlmChannel62MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1, 3),
    _Pmopm8AlmChannel62MismatchPortn_Type()
)
pmopm8AlmChannel62MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel62MismatchPortn.setStatus("current")
_Pmopm8AlmChannel62BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel62BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel62BalancedPortn = _Pmopm8AlmChannel62BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1, 4),
    _Pmopm8AlmChannel62BalancedPortn_Type()
)
pmopm8AlmChannel62BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel62BalancedPortn.setStatus("current")
_Pmopm8AlmChannel62PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel62PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel62PowerLowPortn = _Pmopm8AlmChannel62PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1, 5),
    _Pmopm8AlmChannel62PowerLowPortn_Type()
)
pmopm8AlmChannel62PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel62PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel62PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel62PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel62PowerHighPortn = _Pmopm8AlmChannel62PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1, 6),
    _Pmopm8AlmChannel62PowerHighPortn_Type()
)
pmopm8AlmChannel62PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel62PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel62OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel62OosPortn_Object = MibTableColumn
pmopm8AlmChannel62OosPortn = _Pmopm8AlmChannel62OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 504, 1, 7),
    _Pmopm8AlmChannel62OosPortn_Type()
)
pmopm8AlmChannel62OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel62OosPortn.setStatus("current")
_Pmopm8Almchannel63PortTable_Object = MibTable
pmopm8Almchannel63PortTable = _Pmopm8Almchannel63PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel63PortTable.setStatus("current")
_Pmopm8Almchannel63PortEntry_Object = MibTableRow
pmopm8Almchannel63PortEntry = _Pmopm8Almchannel63PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1)
)
pmopm8Almchannel63PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel63PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel63PortEntry.setStatus("current")


class _Pmopm8Almchannel63PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel63PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel63PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel63PortIndex_Object = MibTableColumn
pmopm8Almchannel63PortIndex = _Pmopm8Almchannel63PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1, 1),
    _Pmopm8Almchannel63PortIndex_Type()
)
pmopm8Almchannel63PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel63PortIndex.setStatus("current")
_Pmopm8AlmChannel63AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel63AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel63AbsentPortn = _Pmopm8AlmChannel63AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1, 2),
    _Pmopm8AlmChannel63AbsentPortn_Type()
)
pmopm8AlmChannel63AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel63AbsentPortn.setStatus("current")
_Pmopm8AlmChannel63MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel63MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel63MismatchPortn = _Pmopm8AlmChannel63MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1, 3),
    _Pmopm8AlmChannel63MismatchPortn_Type()
)
pmopm8AlmChannel63MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel63MismatchPortn.setStatus("current")
_Pmopm8AlmChannel63BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel63BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel63BalancedPortn = _Pmopm8AlmChannel63BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1, 4),
    _Pmopm8AlmChannel63BalancedPortn_Type()
)
pmopm8AlmChannel63BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel63BalancedPortn.setStatus("current")
_Pmopm8AlmChannel63PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel63PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel63PowerLowPortn = _Pmopm8AlmChannel63PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1, 5),
    _Pmopm8AlmChannel63PowerLowPortn_Type()
)
pmopm8AlmChannel63PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel63PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel63PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel63PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel63PowerHighPortn = _Pmopm8AlmChannel63PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1, 6),
    _Pmopm8AlmChannel63PowerHighPortn_Type()
)
pmopm8AlmChannel63PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel63PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel63OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel63OosPortn_Object = MibTableColumn
pmopm8AlmChannel63OosPortn = _Pmopm8AlmChannel63OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 512, 1, 7),
    _Pmopm8AlmChannel63OosPortn_Type()
)
pmopm8AlmChannel63OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel63OosPortn.setStatus("current")
_Pmopm8Almchannel64PortTable_Object = MibTable
pmopm8Almchannel64PortTable = _Pmopm8Almchannel64PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel64PortTable.setStatus("current")
_Pmopm8Almchannel64PortEntry_Object = MibTableRow
pmopm8Almchannel64PortEntry = _Pmopm8Almchannel64PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1)
)
pmopm8Almchannel64PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel64PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel64PortEntry.setStatus("current")


class _Pmopm8Almchannel64PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel64PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel64PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel64PortIndex_Object = MibTableColumn
pmopm8Almchannel64PortIndex = _Pmopm8Almchannel64PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1, 1),
    _Pmopm8Almchannel64PortIndex_Type()
)
pmopm8Almchannel64PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel64PortIndex.setStatus("current")
_Pmopm8AlmChannel64AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel64AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel64AbsentPortn = _Pmopm8AlmChannel64AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1, 2),
    _Pmopm8AlmChannel64AbsentPortn_Type()
)
pmopm8AlmChannel64AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel64AbsentPortn.setStatus("current")
_Pmopm8AlmChannel64MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel64MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel64MismatchPortn = _Pmopm8AlmChannel64MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1, 3),
    _Pmopm8AlmChannel64MismatchPortn_Type()
)
pmopm8AlmChannel64MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel64MismatchPortn.setStatus("current")
_Pmopm8AlmChannel64BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel64BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel64BalancedPortn = _Pmopm8AlmChannel64BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1, 4),
    _Pmopm8AlmChannel64BalancedPortn_Type()
)
pmopm8AlmChannel64BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel64BalancedPortn.setStatus("current")
_Pmopm8AlmChannel64PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel64PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel64PowerLowPortn = _Pmopm8AlmChannel64PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1, 5),
    _Pmopm8AlmChannel64PowerLowPortn_Type()
)
pmopm8AlmChannel64PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel64PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel64PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel64PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel64PowerHighPortn = _Pmopm8AlmChannel64PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1, 6),
    _Pmopm8AlmChannel64PowerHighPortn_Type()
)
pmopm8AlmChannel64PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel64PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel64OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel64OosPortn_Object = MibTableColumn
pmopm8AlmChannel64OosPortn = _Pmopm8AlmChannel64OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 520, 1, 7),
    _Pmopm8AlmChannel64OosPortn_Type()
)
pmopm8AlmChannel64OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel64OosPortn.setStatus("current")
_Pmopm8Almchannel65PortTable_Object = MibTable
pmopm8Almchannel65PortTable = _Pmopm8Almchannel65PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel65PortTable.setStatus("current")
_Pmopm8Almchannel65PortEntry_Object = MibTableRow
pmopm8Almchannel65PortEntry = _Pmopm8Almchannel65PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1)
)
pmopm8Almchannel65PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel65PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel65PortEntry.setStatus("current")


class _Pmopm8Almchannel65PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel65PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel65PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel65PortIndex_Object = MibTableColumn
pmopm8Almchannel65PortIndex = _Pmopm8Almchannel65PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1, 1),
    _Pmopm8Almchannel65PortIndex_Type()
)
pmopm8Almchannel65PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel65PortIndex.setStatus("current")
_Pmopm8AlmChannel65AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel65AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel65AbsentPortn = _Pmopm8AlmChannel65AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1, 2),
    _Pmopm8AlmChannel65AbsentPortn_Type()
)
pmopm8AlmChannel65AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel65AbsentPortn.setStatus("current")
_Pmopm8AlmChannel65MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel65MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel65MismatchPortn = _Pmopm8AlmChannel65MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1, 3),
    _Pmopm8AlmChannel65MismatchPortn_Type()
)
pmopm8AlmChannel65MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel65MismatchPortn.setStatus("current")
_Pmopm8AlmChannel65BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel65BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel65BalancedPortn = _Pmopm8AlmChannel65BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1, 4),
    _Pmopm8AlmChannel65BalancedPortn_Type()
)
pmopm8AlmChannel65BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel65BalancedPortn.setStatus("current")
_Pmopm8AlmChannel65PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel65PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel65PowerLowPortn = _Pmopm8AlmChannel65PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1, 5),
    _Pmopm8AlmChannel65PowerLowPortn_Type()
)
pmopm8AlmChannel65PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel65PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel65PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel65PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel65PowerHighPortn = _Pmopm8AlmChannel65PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1, 6),
    _Pmopm8AlmChannel65PowerHighPortn_Type()
)
pmopm8AlmChannel65PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel65PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel65OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel65OosPortn_Object = MibTableColumn
pmopm8AlmChannel65OosPortn = _Pmopm8AlmChannel65OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 528, 1, 7),
    _Pmopm8AlmChannel65OosPortn_Type()
)
pmopm8AlmChannel65OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel65OosPortn.setStatus("current")
_Pmopm8Almchannel66PortTable_Object = MibTable
pmopm8Almchannel66PortTable = _Pmopm8Almchannel66PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel66PortTable.setStatus("current")
_Pmopm8Almchannel66PortEntry_Object = MibTableRow
pmopm8Almchannel66PortEntry = _Pmopm8Almchannel66PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1)
)
pmopm8Almchannel66PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel66PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel66PortEntry.setStatus("current")


class _Pmopm8Almchannel66PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel66PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel66PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel66PortIndex_Object = MibTableColumn
pmopm8Almchannel66PortIndex = _Pmopm8Almchannel66PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1, 1),
    _Pmopm8Almchannel66PortIndex_Type()
)
pmopm8Almchannel66PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel66PortIndex.setStatus("current")
_Pmopm8AlmChannel66AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel66AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel66AbsentPortn = _Pmopm8AlmChannel66AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1, 2),
    _Pmopm8AlmChannel66AbsentPortn_Type()
)
pmopm8AlmChannel66AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel66AbsentPortn.setStatus("current")
_Pmopm8AlmChannel66MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel66MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel66MismatchPortn = _Pmopm8AlmChannel66MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1, 3),
    _Pmopm8AlmChannel66MismatchPortn_Type()
)
pmopm8AlmChannel66MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel66MismatchPortn.setStatus("current")
_Pmopm8AlmChannel66BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel66BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel66BalancedPortn = _Pmopm8AlmChannel66BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1, 4),
    _Pmopm8AlmChannel66BalancedPortn_Type()
)
pmopm8AlmChannel66BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel66BalancedPortn.setStatus("current")
_Pmopm8AlmChannel66PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel66PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel66PowerLowPortn = _Pmopm8AlmChannel66PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1, 5),
    _Pmopm8AlmChannel66PowerLowPortn_Type()
)
pmopm8AlmChannel66PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel66PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel66PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel66PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel66PowerHighPortn = _Pmopm8AlmChannel66PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1, 6),
    _Pmopm8AlmChannel66PowerHighPortn_Type()
)
pmopm8AlmChannel66PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel66PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel66OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel66OosPortn_Object = MibTableColumn
pmopm8AlmChannel66OosPortn = _Pmopm8AlmChannel66OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 536, 1, 7),
    _Pmopm8AlmChannel66OosPortn_Type()
)
pmopm8AlmChannel66OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel66OosPortn.setStatus("current")
_Pmopm8Almchannel67PortTable_Object = MibTable
pmopm8Almchannel67PortTable = _Pmopm8Almchannel67PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel67PortTable.setStatus("current")
_Pmopm8Almchannel67PortEntry_Object = MibTableRow
pmopm8Almchannel67PortEntry = _Pmopm8Almchannel67PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1)
)
pmopm8Almchannel67PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel67PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel67PortEntry.setStatus("current")


class _Pmopm8Almchannel67PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel67PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel67PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel67PortIndex_Object = MibTableColumn
pmopm8Almchannel67PortIndex = _Pmopm8Almchannel67PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1, 1),
    _Pmopm8Almchannel67PortIndex_Type()
)
pmopm8Almchannel67PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel67PortIndex.setStatus("current")
_Pmopm8AlmChannel67AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel67AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel67AbsentPortn = _Pmopm8AlmChannel67AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1, 2),
    _Pmopm8AlmChannel67AbsentPortn_Type()
)
pmopm8AlmChannel67AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel67AbsentPortn.setStatus("current")
_Pmopm8AlmChannel67MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel67MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel67MismatchPortn = _Pmopm8AlmChannel67MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1, 3),
    _Pmopm8AlmChannel67MismatchPortn_Type()
)
pmopm8AlmChannel67MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel67MismatchPortn.setStatus("current")
_Pmopm8AlmChannel67BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel67BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel67BalancedPortn = _Pmopm8AlmChannel67BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1, 4),
    _Pmopm8AlmChannel67BalancedPortn_Type()
)
pmopm8AlmChannel67BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel67BalancedPortn.setStatus("current")
_Pmopm8AlmChannel67PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel67PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel67PowerLowPortn = _Pmopm8AlmChannel67PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1, 5),
    _Pmopm8AlmChannel67PowerLowPortn_Type()
)
pmopm8AlmChannel67PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel67PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel67PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel67PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel67PowerHighPortn = _Pmopm8AlmChannel67PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1, 6),
    _Pmopm8AlmChannel67PowerHighPortn_Type()
)
pmopm8AlmChannel67PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel67PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel67OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel67OosPortn_Object = MibTableColumn
pmopm8AlmChannel67OosPortn = _Pmopm8AlmChannel67OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 544, 1, 7),
    _Pmopm8AlmChannel67OosPortn_Type()
)
pmopm8AlmChannel67OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel67OosPortn.setStatus("current")
_Pmopm8Almchannel68PortTable_Object = MibTable
pmopm8Almchannel68PortTable = _Pmopm8Almchannel68PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel68PortTable.setStatus("current")
_Pmopm8Almchannel68PortEntry_Object = MibTableRow
pmopm8Almchannel68PortEntry = _Pmopm8Almchannel68PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1)
)
pmopm8Almchannel68PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel68PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel68PortEntry.setStatus("current")


class _Pmopm8Almchannel68PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel68PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel68PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel68PortIndex_Object = MibTableColumn
pmopm8Almchannel68PortIndex = _Pmopm8Almchannel68PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1, 1),
    _Pmopm8Almchannel68PortIndex_Type()
)
pmopm8Almchannel68PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel68PortIndex.setStatus("current")
_Pmopm8AlmChannel68AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel68AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel68AbsentPortn = _Pmopm8AlmChannel68AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1, 2),
    _Pmopm8AlmChannel68AbsentPortn_Type()
)
pmopm8AlmChannel68AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel68AbsentPortn.setStatus("current")
_Pmopm8AlmChannel68MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel68MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel68MismatchPortn = _Pmopm8AlmChannel68MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1, 3),
    _Pmopm8AlmChannel68MismatchPortn_Type()
)
pmopm8AlmChannel68MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel68MismatchPortn.setStatus("current")
_Pmopm8AlmChannel68BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel68BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel68BalancedPortn = _Pmopm8AlmChannel68BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1, 4),
    _Pmopm8AlmChannel68BalancedPortn_Type()
)
pmopm8AlmChannel68BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel68BalancedPortn.setStatus("current")
_Pmopm8AlmChannel68PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel68PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel68PowerLowPortn = _Pmopm8AlmChannel68PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1, 5),
    _Pmopm8AlmChannel68PowerLowPortn_Type()
)
pmopm8AlmChannel68PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel68PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel68PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel68PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel68PowerHighPortn = _Pmopm8AlmChannel68PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1, 6),
    _Pmopm8AlmChannel68PowerHighPortn_Type()
)
pmopm8AlmChannel68PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel68PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel68OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel68OosPortn_Object = MibTableColumn
pmopm8AlmChannel68OosPortn = _Pmopm8AlmChannel68OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 552, 1, 7),
    _Pmopm8AlmChannel68OosPortn_Type()
)
pmopm8AlmChannel68OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel68OosPortn.setStatus("current")
_Pmopm8Almchannel69PortTable_Object = MibTable
pmopm8Almchannel69PortTable = _Pmopm8Almchannel69PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel69PortTable.setStatus("current")
_Pmopm8Almchannel69PortEntry_Object = MibTableRow
pmopm8Almchannel69PortEntry = _Pmopm8Almchannel69PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1)
)
pmopm8Almchannel69PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel69PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel69PortEntry.setStatus("current")


class _Pmopm8Almchannel69PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel69PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel69PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel69PortIndex_Object = MibTableColumn
pmopm8Almchannel69PortIndex = _Pmopm8Almchannel69PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1, 1),
    _Pmopm8Almchannel69PortIndex_Type()
)
pmopm8Almchannel69PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel69PortIndex.setStatus("current")
_Pmopm8AlmChannel69AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel69AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel69AbsentPortn = _Pmopm8AlmChannel69AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1, 2),
    _Pmopm8AlmChannel69AbsentPortn_Type()
)
pmopm8AlmChannel69AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel69AbsentPortn.setStatus("current")
_Pmopm8AlmChannel69MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel69MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel69MismatchPortn = _Pmopm8AlmChannel69MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1, 3),
    _Pmopm8AlmChannel69MismatchPortn_Type()
)
pmopm8AlmChannel69MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel69MismatchPortn.setStatus("current")
_Pmopm8AlmChannel69BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel69BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel69BalancedPortn = _Pmopm8AlmChannel69BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1, 4),
    _Pmopm8AlmChannel69BalancedPortn_Type()
)
pmopm8AlmChannel69BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel69BalancedPortn.setStatus("current")
_Pmopm8AlmChannel69PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel69PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel69PowerLowPortn = _Pmopm8AlmChannel69PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1, 5),
    _Pmopm8AlmChannel69PowerLowPortn_Type()
)
pmopm8AlmChannel69PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel69PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel69PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel69PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel69PowerHighPortn = _Pmopm8AlmChannel69PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1, 6),
    _Pmopm8AlmChannel69PowerHighPortn_Type()
)
pmopm8AlmChannel69PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel69PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel69OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel69OosPortn_Object = MibTableColumn
pmopm8AlmChannel69OosPortn = _Pmopm8AlmChannel69OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 560, 1, 7),
    _Pmopm8AlmChannel69OosPortn_Type()
)
pmopm8AlmChannel69OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel69OosPortn.setStatus("current")
_Pmopm8Almchannel70PortTable_Object = MibTable
pmopm8Almchannel70PortTable = _Pmopm8Almchannel70PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel70PortTable.setStatus("current")
_Pmopm8Almchannel70PortEntry_Object = MibTableRow
pmopm8Almchannel70PortEntry = _Pmopm8Almchannel70PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1)
)
pmopm8Almchannel70PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel70PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel70PortEntry.setStatus("current")


class _Pmopm8Almchannel70PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel70PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel70PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel70PortIndex_Object = MibTableColumn
pmopm8Almchannel70PortIndex = _Pmopm8Almchannel70PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1, 1),
    _Pmopm8Almchannel70PortIndex_Type()
)
pmopm8Almchannel70PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel70PortIndex.setStatus("current")
_Pmopm8AlmChannel70AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel70AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel70AbsentPortn = _Pmopm8AlmChannel70AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1, 2),
    _Pmopm8AlmChannel70AbsentPortn_Type()
)
pmopm8AlmChannel70AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel70AbsentPortn.setStatus("current")
_Pmopm8AlmChannel70MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel70MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel70MismatchPortn = _Pmopm8AlmChannel70MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1, 3),
    _Pmopm8AlmChannel70MismatchPortn_Type()
)
pmopm8AlmChannel70MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel70MismatchPortn.setStatus("current")
_Pmopm8AlmChannel70BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel70BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel70BalancedPortn = _Pmopm8AlmChannel70BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1, 4),
    _Pmopm8AlmChannel70BalancedPortn_Type()
)
pmopm8AlmChannel70BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel70BalancedPortn.setStatus("current")
_Pmopm8AlmChannel70PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel70PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel70PowerLowPortn = _Pmopm8AlmChannel70PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1, 5),
    _Pmopm8AlmChannel70PowerLowPortn_Type()
)
pmopm8AlmChannel70PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel70PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel70PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel70PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel70PowerHighPortn = _Pmopm8AlmChannel70PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1, 6),
    _Pmopm8AlmChannel70PowerHighPortn_Type()
)
pmopm8AlmChannel70PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel70PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel70OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel70OosPortn_Object = MibTableColumn
pmopm8AlmChannel70OosPortn = _Pmopm8AlmChannel70OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 568, 1, 7),
    _Pmopm8AlmChannel70OosPortn_Type()
)
pmopm8AlmChannel70OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel70OosPortn.setStatus("current")
_Pmopm8Almchannel71PortTable_Object = MibTable
pmopm8Almchannel71PortTable = _Pmopm8Almchannel71PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel71PortTable.setStatus("current")
_Pmopm8Almchannel71PortEntry_Object = MibTableRow
pmopm8Almchannel71PortEntry = _Pmopm8Almchannel71PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1)
)
pmopm8Almchannel71PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel71PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel71PortEntry.setStatus("current")


class _Pmopm8Almchannel71PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel71PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel71PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel71PortIndex_Object = MibTableColumn
pmopm8Almchannel71PortIndex = _Pmopm8Almchannel71PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1, 1),
    _Pmopm8Almchannel71PortIndex_Type()
)
pmopm8Almchannel71PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel71PortIndex.setStatus("current")
_Pmopm8AlmChannel71AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel71AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel71AbsentPortn = _Pmopm8AlmChannel71AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1, 2),
    _Pmopm8AlmChannel71AbsentPortn_Type()
)
pmopm8AlmChannel71AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel71AbsentPortn.setStatus("current")
_Pmopm8AlmChannel71MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel71MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel71MismatchPortn = _Pmopm8AlmChannel71MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1, 3),
    _Pmopm8AlmChannel71MismatchPortn_Type()
)
pmopm8AlmChannel71MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel71MismatchPortn.setStatus("current")
_Pmopm8AlmChannel71BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel71BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel71BalancedPortn = _Pmopm8AlmChannel71BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1, 4),
    _Pmopm8AlmChannel71BalancedPortn_Type()
)
pmopm8AlmChannel71BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel71BalancedPortn.setStatus("current")
_Pmopm8AlmChannel71PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel71PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel71PowerLowPortn = _Pmopm8AlmChannel71PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1, 5),
    _Pmopm8AlmChannel71PowerLowPortn_Type()
)
pmopm8AlmChannel71PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel71PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel71PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel71PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel71PowerHighPortn = _Pmopm8AlmChannel71PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1, 6),
    _Pmopm8AlmChannel71PowerHighPortn_Type()
)
pmopm8AlmChannel71PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel71PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel71OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel71OosPortn_Object = MibTableColumn
pmopm8AlmChannel71OosPortn = _Pmopm8AlmChannel71OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 576, 1, 7),
    _Pmopm8AlmChannel71OosPortn_Type()
)
pmopm8AlmChannel71OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel71OosPortn.setStatus("current")
_Pmopm8Almchannel72PortTable_Object = MibTable
pmopm8Almchannel72PortTable = _Pmopm8Almchannel72PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel72PortTable.setStatus("current")
_Pmopm8Almchannel72PortEntry_Object = MibTableRow
pmopm8Almchannel72PortEntry = _Pmopm8Almchannel72PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1)
)
pmopm8Almchannel72PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel72PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel72PortEntry.setStatus("current")


class _Pmopm8Almchannel72PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel72PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel72PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel72PortIndex_Object = MibTableColumn
pmopm8Almchannel72PortIndex = _Pmopm8Almchannel72PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1, 1),
    _Pmopm8Almchannel72PortIndex_Type()
)
pmopm8Almchannel72PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel72PortIndex.setStatus("current")
_Pmopm8AlmChannel72AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel72AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel72AbsentPortn = _Pmopm8AlmChannel72AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1, 2),
    _Pmopm8AlmChannel72AbsentPortn_Type()
)
pmopm8AlmChannel72AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel72AbsentPortn.setStatus("current")
_Pmopm8AlmChannel72MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel72MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel72MismatchPortn = _Pmopm8AlmChannel72MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1, 3),
    _Pmopm8AlmChannel72MismatchPortn_Type()
)
pmopm8AlmChannel72MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel72MismatchPortn.setStatus("current")
_Pmopm8AlmChannel72BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel72BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel72BalancedPortn = _Pmopm8AlmChannel72BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1, 4),
    _Pmopm8AlmChannel72BalancedPortn_Type()
)
pmopm8AlmChannel72BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel72BalancedPortn.setStatus("current")
_Pmopm8AlmChannel72PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel72PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel72PowerLowPortn = _Pmopm8AlmChannel72PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1, 5),
    _Pmopm8AlmChannel72PowerLowPortn_Type()
)
pmopm8AlmChannel72PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel72PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel72PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel72PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel72PowerHighPortn = _Pmopm8AlmChannel72PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1, 6),
    _Pmopm8AlmChannel72PowerHighPortn_Type()
)
pmopm8AlmChannel72PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel72PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel72OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel72OosPortn_Object = MibTableColumn
pmopm8AlmChannel72OosPortn = _Pmopm8AlmChannel72OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 584, 1, 7),
    _Pmopm8AlmChannel72OosPortn_Type()
)
pmopm8AlmChannel72OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel72OosPortn.setStatus("current")
_Pmopm8Almchannel73PortTable_Object = MibTable
pmopm8Almchannel73PortTable = _Pmopm8Almchannel73PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel73PortTable.setStatus("current")
_Pmopm8Almchannel73PortEntry_Object = MibTableRow
pmopm8Almchannel73PortEntry = _Pmopm8Almchannel73PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1)
)
pmopm8Almchannel73PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel73PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel73PortEntry.setStatus("current")


class _Pmopm8Almchannel73PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel73PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel73PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel73PortIndex_Object = MibTableColumn
pmopm8Almchannel73PortIndex = _Pmopm8Almchannel73PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1, 1),
    _Pmopm8Almchannel73PortIndex_Type()
)
pmopm8Almchannel73PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel73PortIndex.setStatus("current")
_Pmopm8AlmChannel73AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel73AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel73AbsentPortn = _Pmopm8AlmChannel73AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1, 2),
    _Pmopm8AlmChannel73AbsentPortn_Type()
)
pmopm8AlmChannel73AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel73AbsentPortn.setStatus("current")
_Pmopm8AlmChannel73MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel73MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel73MismatchPortn = _Pmopm8AlmChannel73MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1, 3),
    _Pmopm8AlmChannel73MismatchPortn_Type()
)
pmopm8AlmChannel73MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel73MismatchPortn.setStatus("current")
_Pmopm8AlmChannel73BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel73BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel73BalancedPortn = _Pmopm8AlmChannel73BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1, 4),
    _Pmopm8AlmChannel73BalancedPortn_Type()
)
pmopm8AlmChannel73BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel73BalancedPortn.setStatus("current")
_Pmopm8AlmChannel73PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel73PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel73PowerLowPortn = _Pmopm8AlmChannel73PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1, 5),
    _Pmopm8AlmChannel73PowerLowPortn_Type()
)
pmopm8AlmChannel73PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel73PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel73PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel73PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel73PowerHighPortn = _Pmopm8AlmChannel73PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1, 6),
    _Pmopm8AlmChannel73PowerHighPortn_Type()
)
pmopm8AlmChannel73PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel73PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel73OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel73OosPortn_Object = MibTableColumn
pmopm8AlmChannel73OosPortn = _Pmopm8AlmChannel73OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 592, 1, 7),
    _Pmopm8AlmChannel73OosPortn_Type()
)
pmopm8AlmChannel73OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel73OosPortn.setStatus("current")
_Pmopm8Almchannel74PortTable_Object = MibTable
pmopm8Almchannel74PortTable = _Pmopm8Almchannel74PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel74PortTable.setStatus("current")
_Pmopm8Almchannel74PortEntry_Object = MibTableRow
pmopm8Almchannel74PortEntry = _Pmopm8Almchannel74PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1)
)
pmopm8Almchannel74PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel74PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel74PortEntry.setStatus("current")


class _Pmopm8Almchannel74PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel74PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel74PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel74PortIndex_Object = MibTableColumn
pmopm8Almchannel74PortIndex = _Pmopm8Almchannel74PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1, 1),
    _Pmopm8Almchannel74PortIndex_Type()
)
pmopm8Almchannel74PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel74PortIndex.setStatus("current")
_Pmopm8AlmChannel74AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel74AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel74AbsentPortn = _Pmopm8AlmChannel74AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1, 2),
    _Pmopm8AlmChannel74AbsentPortn_Type()
)
pmopm8AlmChannel74AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel74AbsentPortn.setStatus("current")
_Pmopm8AlmChannel74MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel74MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel74MismatchPortn = _Pmopm8AlmChannel74MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1, 3),
    _Pmopm8AlmChannel74MismatchPortn_Type()
)
pmopm8AlmChannel74MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel74MismatchPortn.setStatus("current")
_Pmopm8AlmChannel74BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel74BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel74BalancedPortn = _Pmopm8AlmChannel74BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1, 4),
    _Pmopm8AlmChannel74BalancedPortn_Type()
)
pmopm8AlmChannel74BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel74BalancedPortn.setStatus("current")
_Pmopm8AlmChannel74PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel74PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel74PowerLowPortn = _Pmopm8AlmChannel74PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1, 5),
    _Pmopm8AlmChannel74PowerLowPortn_Type()
)
pmopm8AlmChannel74PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel74PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel74PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel74PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel74PowerHighPortn = _Pmopm8AlmChannel74PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1, 6),
    _Pmopm8AlmChannel74PowerHighPortn_Type()
)
pmopm8AlmChannel74PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel74PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel74OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel74OosPortn_Object = MibTableColumn
pmopm8AlmChannel74OosPortn = _Pmopm8AlmChannel74OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 600, 1, 7),
    _Pmopm8AlmChannel74OosPortn_Type()
)
pmopm8AlmChannel74OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel74OosPortn.setStatus("current")
_Pmopm8Almchannel75PortTable_Object = MibTable
pmopm8Almchannel75PortTable = _Pmopm8Almchannel75PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel75PortTable.setStatus("current")
_Pmopm8Almchannel75PortEntry_Object = MibTableRow
pmopm8Almchannel75PortEntry = _Pmopm8Almchannel75PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1)
)
pmopm8Almchannel75PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel75PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel75PortEntry.setStatus("current")


class _Pmopm8Almchannel75PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel75PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel75PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel75PortIndex_Object = MibTableColumn
pmopm8Almchannel75PortIndex = _Pmopm8Almchannel75PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1, 1),
    _Pmopm8Almchannel75PortIndex_Type()
)
pmopm8Almchannel75PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel75PortIndex.setStatus("current")
_Pmopm8AlmChannel75AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel75AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel75AbsentPortn = _Pmopm8AlmChannel75AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1, 2),
    _Pmopm8AlmChannel75AbsentPortn_Type()
)
pmopm8AlmChannel75AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel75AbsentPortn.setStatus("current")
_Pmopm8AlmChannel75MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel75MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel75MismatchPortn = _Pmopm8AlmChannel75MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1, 3),
    _Pmopm8AlmChannel75MismatchPortn_Type()
)
pmopm8AlmChannel75MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel75MismatchPortn.setStatus("current")
_Pmopm8AlmChannel75BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel75BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel75BalancedPortn = _Pmopm8AlmChannel75BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1, 4),
    _Pmopm8AlmChannel75BalancedPortn_Type()
)
pmopm8AlmChannel75BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel75BalancedPortn.setStatus("current")
_Pmopm8AlmChannel75PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel75PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel75PowerLowPortn = _Pmopm8AlmChannel75PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1, 5),
    _Pmopm8AlmChannel75PowerLowPortn_Type()
)
pmopm8AlmChannel75PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel75PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel75PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel75PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel75PowerHighPortn = _Pmopm8AlmChannel75PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1, 6),
    _Pmopm8AlmChannel75PowerHighPortn_Type()
)
pmopm8AlmChannel75PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel75PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel75OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel75OosPortn_Object = MibTableColumn
pmopm8AlmChannel75OosPortn = _Pmopm8AlmChannel75OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 608, 1, 7),
    _Pmopm8AlmChannel75OosPortn_Type()
)
pmopm8AlmChannel75OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel75OosPortn.setStatus("current")
_Pmopm8Almchannel76PortTable_Object = MibTable
pmopm8Almchannel76PortTable = _Pmopm8Almchannel76PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel76PortTable.setStatus("current")
_Pmopm8Almchannel76PortEntry_Object = MibTableRow
pmopm8Almchannel76PortEntry = _Pmopm8Almchannel76PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1)
)
pmopm8Almchannel76PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel76PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel76PortEntry.setStatus("current")


class _Pmopm8Almchannel76PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel76PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel76PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel76PortIndex_Object = MibTableColumn
pmopm8Almchannel76PortIndex = _Pmopm8Almchannel76PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1, 1),
    _Pmopm8Almchannel76PortIndex_Type()
)
pmopm8Almchannel76PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel76PortIndex.setStatus("current")
_Pmopm8AlmChannel76AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel76AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel76AbsentPortn = _Pmopm8AlmChannel76AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1, 2),
    _Pmopm8AlmChannel76AbsentPortn_Type()
)
pmopm8AlmChannel76AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel76AbsentPortn.setStatus("current")
_Pmopm8AlmChannel76MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel76MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel76MismatchPortn = _Pmopm8AlmChannel76MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1, 3),
    _Pmopm8AlmChannel76MismatchPortn_Type()
)
pmopm8AlmChannel76MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel76MismatchPortn.setStatus("current")
_Pmopm8AlmChannel76BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel76BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel76BalancedPortn = _Pmopm8AlmChannel76BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1, 4),
    _Pmopm8AlmChannel76BalancedPortn_Type()
)
pmopm8AlmChannel76BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel76BalancedPortn.setStatus("current")
_Pmopm8AlmChannel76PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel76PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel76PowerLowPortn = _Pmopm8AlmChannel76PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1, 5),
    _Pmopm8AlmChannel76PowerLowPortn_Type()
)
pmopm8AlmChannel76PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel76PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel76PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel76PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel76PowerHighPortn = _Pmopm8AlmChannel76PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1, 6),
    _Pmopm8AlmChannel76PowerHighPortn_Type()
)
pmopm8AlmChannel76PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel76PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel76OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel76OosPortn_Object = MibTableColumn
pmopm8AlmChannel76OosPortn = _Pmopm8AlmChannel76OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 616, 1, 7),
    _Pmopm8AlmChannel76OosPortn_Type()
)
pmopm8AlmChannel76OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel76OosPortn.setStatus("current")
_Pmopm8Almchannel77PortTable_Object = MibTable
pmopm8Almchannel77PortTable = _Pmopm8Almchannel77PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel77PortTable.setStatus("current")
_Pmopm8Almchannel77PortEntry_Object = MibTableRow
pmopm8Almchannel77PortEntry = _Pmopm8Almchannel77PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1)
)
pmopm8Almchannel77PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel77PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel77PortEntry.setStatus("current")


class _Pmopm8Almchannel77PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel77PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel77PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel77PortIndex_Object = MibTableColumn
pmopm8Almchannel77PortIndex = _Pmopm8Almchannel77PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1, 1),
    _Pmopm8Almchannel77PortIndex_Type()
)
pmopm8Almchannel77PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel77PortIndex.setStatus("current")
_Pmopm8AlmChannel77AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel77AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel77AbsentPortn = _Pmopm8AlmChannel77AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1, 2),
    _Pmopm8AlmChannel77AbsentPortn_Type()
)
pmopm8AlmChannel77AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel77AbsentPortn.setStatus("current")
_Pmopm8AlmChannel77MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel77MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel77MismatchPortn = _Pmopm8AlmChannel77MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1, 3),
    _Pmopm8AlmChannel77MismatchPortn_Type()
)
pmopm8AlmChannel77MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel77MismatchPortn.setStatus("current")
_Pmopm8AlmChannel77BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel77BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel77BalancedPortn = _Pmopm8AlmChannel77BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1, 4),
    _Pmopm8AlmChannel77BalancedPortn_Type()
)
pmopm8AlmChannel77BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel77BalancedPortn.setStatus("current")
_Pmopm8AlmChannel77PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel77PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel77PowerLowPortn = _Pmopm8AlmChannel77PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1, 5),
    _Pmopm8AlmChannel77PowerLowPortn_Type()
)
pmopm8AlmChannel77PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel77PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel77PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel77PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel77PowerHighPortn = _Pmopm8AlmChannel77PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1, 6),
    _Pmopm8AlmChannel77PowerHighPortn_Type()
)
pmopm8AlmChannel77PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel77PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel77OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel77OosPortn_Object = MibTableColumn
pmopm8AlmChannel77OosPortn = _Pmopm8AlmChannel77OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 624, 1, 7),
    _Pmopm8AlmChannel77OosPortn_Type()
)
pmopm8AlmChannel77OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel77OosPortn.setStatus("current")
_Pmopm8Almchannel78PortTable_Object = MibTable
pmopm8Almchannel78PortTable = _Pmopm8Almchannel78PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel78PortTable.setStatus("current")
_Pmopm8Almchannel78PortEntry_Object = MibTableRow
pmopm8Almchannel78PortEntry = _Pmopm8Almchannel78PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1)
)
pmopm8Almchannel78PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel78PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel78PortEntry.setStatus("current")


class _Pmopm8Almchannel78PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel78PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel78PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel78PortIndex_Object = MibTableColumn
pmopm8Almchannel78PortIndex = _Pmopm8Almchannel78PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1, 1),
    _Pmopm8Almchannel78PortIndex_Type()
)
pmopm8Almchannel78PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel78PortIndex.setStatus("current")
_Pmopm8AlmChannel78AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel78AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel78AbsentPortn = _Pmopm8AlmChannel78AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1, 2),
    _Pmopm8AlmChannel78AbsentPortn_Type()
)
pmopm8AlmChannel78AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel78AbsentPortn.setStatus("current")
_Pmopm8AlmChannel78MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel78MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel78MismatchPortn = _Pmopm8AlmChannel78MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1, 3),
    _Pmopm8AlmChannel78MismatchPortn_Type()
)
pmopm8AlmChannel78MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel78MismatchPortn.setStatus("current")
_Pmopm8AlmChannel78BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel78BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel78BalancedPortn = _Pmopm8AlmChannel78BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1, 4),
    _Pmopm8AlmChannel78BalancedPortn_Type()
)
pmopm8AlmChannel78BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel78BalancedPortn.setStatus("current")
_Pmopm8AlmChannel78PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel78PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel78PowerLowPortn = _Pmopm8AlmChannel78PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1, 5),
    _Pmopm8AlmChannel78PowerLowPortn_Type()
)
pmopm8AlmChannel78PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel78PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel78PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel78PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel78PowerHighPortn = _Pmopm8AlmChannel78PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1, 6),
    _Pmopm8AlmChannel78PowerHighPortn_Type()
)
pmopm8AlmChannel78PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel78PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel78OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel78OosPortn_Object = MibTableColumn
pmopm8AlmChannel78OosPortn = _Pmopm8AlmChannel78OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 632, 1, 7),
    _Pmopm8AlmChannel78OosPortn_Type()
)
pmopm8AlmChannel78OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel78OosPortn.setStatus("current")
_Pmopm8Almchannel79PortTable_Object = MibTable
pmopm8Almchannel79PortTable = _Pmopm8Almchannel79PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel79PortTable.setStatus("current")
_Pmopm8Almchannel79PortEntry_Object = MibTableRow
pmopm8Almchannel79PortEntry = _Pmopm8Almchannel79PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1)
)
pmopm8Almchannel79PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel79PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel79PortEntry.setStatus("current")


class _Pmopm8Almchannel79PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel79PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel79PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel79PortIndex_Object = MibTableColumn
pmopm8Almchannel79PortIndex = _Pmopm8Almchannel79PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1, 1),
    _Pmopm8Almchannel79PortIndex_Type()
)
pmopm8Almchannel79PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel79PortIndex.setStatus("current")
_Pmopm8AlmChannel79AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel79AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel79AbsentPortn = _Pmopm8AlmChannel79AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1, 2),
    _Pmopm8AlmChannel79AbsentPortn_Type()
)
pmopm8AlmChannel79AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel79AbsentPortn.setStatus("current")
_Pmopm8AlmChannel79MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel79MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel79MismatchPortn = _Pmopm8AlmChannel79MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1, 3),
    _Pmopm8AlmChannel79MismatchPortn_Type()
)
pmopm8AlmChannel79MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel79MismatchPortn.setStatus("current")
_Pmopm8AlmChannel79BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel79BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel79BalancedPortn = _Pmopm8AlmChannel79BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1, 4),
    _Pmopm8AlmChannel79BalancedPortn_Type()
)
pmopm8AlmChannel79BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel79BalancedPortn.setStatus("current")
_Pmopm8AlmChannel79PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel79PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel79PowerLowPortn = _Pmopm8AlmChannel79PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1, 5),
    _Pmopm8AlmChannel79PowerLowPortn_Type()
)
pmopm8AlmChannel79PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel79PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel79PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel79PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel79PowerHighPortn = _Pmopm8AlmChannel79PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1, 6),
    _Pmopm8AlmChannel79PowerHighPortn_Type()
)
pmopm8AlmChannel79PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel79PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel79OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel79OosPortn_Object = MibTableColumn
pmopm8AlmChannel79OosPortn = _Pmopm8AlmChannel79OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 640, 1, 7),
    _Pmopm8AlmChannel79OosPortn_Type()
)
pmopm8AlmChannel79OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel79OosPortn.setStatus("current")
_Pmopm8Almchannel80PortTable_Object = MibTable
pmopm8Almchannel80PortTable = _Pmopm8Almchannel80PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel80PortTable.setStatus("current")
_Pmopm8Almchannel80PortEntry_Object = MibTableRow
pmopm8Almchannel80PortEntry = _Pmopm8Almchannel80PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1)
)
pmopm8Almchannel80PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel80PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel80PortEntry.setStatus("current")


class _Pmopm8Almchannel80PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel80PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel80PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel80PortIndex_Object = MibTableColumn
pmopm8Almchannel80PortIndex = _Pmopm8Almchannel80PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1, 1),
    _Pmopm8Almchannel80PortIndex_Type()
)
pmopm8Almchannel80PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel80PortIndex.setStatus("current")
_Pmopm8AlmChannel80AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel80AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel80AbsentPortn = _Pmopm8AlmChannel80AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1, 2),
    _Pmopm8AlmChannel80AbsentPortn_Type()
)
pmopm8AlmChannel80AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel80AbsentPortn.setStatus("current")
_Pmopm8AlmChannel80MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel80MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel80MismatchPortn = _Pmopm8AlmChannel80MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1, 3),
    _Pmopm8AlmChannel80MismatchPortn_Type()
)
pmopm8AlmChannel80MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel80MismatchPortn.setStatus("current")
_Pmopm8AlmChannel80BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel80BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel80BalancedPortn = _Pmopm8AlmChannel80BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1, 4),
    _Pmopm8AlmChannel80BalancedPortn_Type()
)
pmopm8AlmChannel80BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel80BalancedPortn.setStatus("current")
_Pmopm8AlmChannel80PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel80PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel80PowerLowPortn = _Pmopm8AlmChannel80PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1, 5),
    _Pmopm8AlmChannel80PowerLowPortn_Type()
)
pmopm8AlmChannel80PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel80PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel80PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel80PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel80PowerHighPortn = _Pmopm8AlmChannel80PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1, 6),
    _Pmopm8AlmChannel80PowerHighPortn_Type()
)
pmopm8AlmChannel80PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel80PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel80OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel80OosPortn_Object = MibTableColumn
pmopm8AlmChannel80OosPortn = _Pmopm8AlmChannel80OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 648, 1, 7),
    _Pmopm8AlmChannel80OosPortn_Type()
)
pmopm8AlmChannel80OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel80OosPortn.setStatus("current")
_Pmopm8Almchannel81PortTable_Object = MibTable
pmopm8Almchannel81PortTable = _Pmopm8Almchannel81PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel81PortTable.setStatus("current")
_Pmopm8Almchannel81PortEntry_Object = MibTableRow
pmopm8Almchannel81PortEntry = _Pmopm8Almchannel81PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1)
)
pmopm8Almchannel81PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel81PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel81PortEntry.setStatus("current")


class _Pmopm8Almchannel81PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel81PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel81PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel81PortIndex_Object = MibTableColumn
pmopm8Almchannel81PortIndex = _Pmopm8Almchannel81PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1, 1),
    _Pmopm8Almchannel81PortIndex_Type()
)
pmopm8Almchannel81PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel81PortIndex.setStatus("current")
_Pmopm8AlmChannel81AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel81AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel81AbsentPortn = _Pmopm8AlmChannel81AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1, 2),
    _Pmopm8AlmChannel81AbsentPortn_Type()
)
pmopm8AlmChannel81AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel81AbsentPortn.setStatus("current")
_Pmopm8AlmChannel81MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel81MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel81MismatchPortn = _Pmopm8AlmChannel81MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1, 3),
    _Pmopm8AlmChannel81MismatchPortn_Type()
)
pmopm8AlmChannel81MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel81MismatchPortn.setStatus("current")
_Pmopm8AlmChannel81BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel81BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel81BalancedPortn = _Pmopm8AlmChannel81BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1, 4),
    _Pmopm8AlmChannel81BalancedPortn_Type()
)
pmopm8AlmChannel81BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel81BalancedPortn.setStatus("current")
_Pmopm8AlmChannel81PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel81PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel81PowerLowPortn = _Pmopm8AlmChannel81PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1, 5),
    _Pmopm8AlmChannel81PowerLowPortn_Type()
)
pmopm8AlmChannel81PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel81PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel81PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel81PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel81PowerHighPortn = _Pmopm8AlmChannel81PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1, 6),
    _Pmopm8AlmChannel81PowerHighPortn_Type()
)
pmopm8AlmChannel81PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel81PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel81OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel81OosPortn_Object = MibTableColumn
pmopm8AlmChannel81OosPortn = _Pmopm8AlmChannel81OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 656, 1, 7),
    _Pmopm8AlmChannel81OosPortn_Type()
)
pmopm8AlmChannel81OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel81OosPortn.setStatus("current")
_Pmopm8Almchannel82PortTable_Object = MibTable
pmopm8Almchannel82PortTable = _Pmopm8Almchannel82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel82PortTable.setStatus("current")
_Pmopm8Almchannel82PortEntry_Object = MibTableRow
pmopm8Almchannel82PortEntry = _Pmopm8Almchannel82PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1)
)
pmopm8Almchannel82PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel82PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel82PortEntry.setStatus("current")


class _Pmopm8Almchannel82PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel82PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel82PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel82PortIndex_Object = MibTableColumn
pmopm8Almchannel82PortIndex = _Pmopm8Almchannel82PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1, 1),
    _Pmopm8Almchannel82PortIndex_Type()
)
pmopm8Almchannel82PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel82PortIndex.setStatus("current")
_Pmopm8AlmChannel82AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel82AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel82AbsentPortn = _Pmopm8AlmChannel82AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1, 2),
    _Pmopm8AlmChannel82AbsentPortn_Type()
)
pmopm8AlmChannel82AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel82AbsentPortn.setStatus("current")
_Pmopm8AlmChannel82MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel82MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel82MismatchPortn = _Pmopm8AlmChannel82MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1, 3),
    _Pmopm8AlmChannel82MismatchPortn_Type()
)
pmopm8AlmChannel82MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel82MismatchPortn.setStatus("current")
_Pmopm8AlmChannel82BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel82BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel82BalancedPortn = _Pmopm8AlmChannel82BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1, 4),
    _Pmopm8AlmChannel82BalancedPortn_Type()
)
pmopm8AlmChannel82BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel82BalancedPortn.setStatus("current")
_Pmopm8AlmChannel82PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel82PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel82PowerLowPortn = _Pmopm8AlmChannel82PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1, 5),
    _Pmopm8AlmChannel82PowerLowPortn_Type()
)
pmopm8AlmChannel82PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel82PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel82PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel82PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel82PowerHighPortn = _Pmopm8AlmChannel82PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1, 6),
    _Pmopm8AlmChannel82PowerHighPortn_Type()
)
pmopm8AlmChannel82PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel82PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel82OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel82OosPortn_Object = MibTableColumn
pmopm8AlmChannel82OosPortn = _Pmopm8AlmChannel82OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 664, 1, 7),
    _Pmopm8AlmChannel82OosPortn_Type()
)
pmopm8AlmChannel82OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel82OosPortn.setStatus("current")
_Pmopm8Almchannel83PortTable_Object = MibTable
pmopm8Almchannel83PortTable = _Pmopm8Almchannel83PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel83PortTable.setStatus("current")
_Pmopm8Almchannel83PortEntry_Object = MibTableRow
pmopm8Almchannel83PortEntry = _Pmopm8Almchannel83PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1)
)
pmopm8Almchannel83PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel83PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel83PortEntry.setStatus("current")


class _Pmopm8Almchannel83PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel83PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel83PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel83PortIndex_Object = MibTableColumn
pmopm8Almchannel83PortIndex = _Pmopm8Almchannel83PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1, 1),
    _Pmopm8Almchannel83PortIndex_Type()
)
pmopm8Almchannel83PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel83PortIndex.setStatus("current")
_Pmopm8AlmChannel83AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel83AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel83AbsentPortn = _Pmopm8AlmChannel83AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1, 2),
    _Pmopm8AlmChannel83AbsentPortn_Type()
)
pmopm8AlmChannel83AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel83AbsentPortn.setStatus("current")
_Pmopm8AlmChannel83MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel83MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel83MismatchPortn = _Pmopm8AlmChannel83MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1, 3),
    _Pmopm8AlmChannel83MismatchPortn_Type()
)
pmopm8AlmChannel83MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel83MismatchPortn.setStatus("current")
_Pmopm8AlmChannel83BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel83BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel83BalancedPortn = _Pmopm8AlmChannel83BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1, 4),
    _Pmopm8AlmChannel83BalancedPortn_Type()
)
pmopm8AlmChannel83BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel83BalancedPortn.setStatus("current")
_Pmopm8AlmChannel83PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel83PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel83PowerLowPortn = _Pmopm8AlmChannel83PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1, 5),
    _Pmopm8AlmChannel83PowerLowPortn_Type()
)
pmopm8AlmChannel83PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel83PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel83PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel83PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel83PowerHighPortn = _Pmopm8AlmChannel83PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1, 6),
    _Pmopm8AlmChannel83PowerHighPortn_Type()
)
pmopm8AlmChannel83PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel83PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel83OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel83OosPortn_Object = MibTableColumn
pmopm8AlmChannel83OosPortn = _Pmopm8AlmChannel83OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 672, 1, 7),
    _Pmopm8AlmChannel83OosPortn_Type()
)
pmopm8AlmChannel83OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel83OosPortn.setStatus("current")
_Pmopm8Almchannel84PortTable_Object = MibTable
pmopm8Almchannel84PortTable = _Pmopm8Almchannel84PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel84PortTable.setStatus("current")
_Pmopm8Almchannel84PortEntry_Object = MibTableRow
pmopm8Almchannel84PortEntry = _Pmopm8Almchannel84PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1)
)
pmopm8Almchannel84PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel84PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel84PortEntry.setStatus("current")


class _Pmopm8Almchannel84PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel84PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel84PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel84PortIndex_Object = MibTableColumn
pmopm8Almchannel84PortIndex = _Pmopm8Almchannel84PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1, 1),
    _Pmopm8Almchannel84PortIndex_Type()
)
pmopm8Almchannel84PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel84PortIndex.setStatus("current")
_Pmopm8AlmChannel84AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel84AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel84AbsentPortn = _Pmopm8AlmChannel84AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1, 2),
    _Pmopm8AlmChannel84AbsentPortn_Type()
)
pmopm8AlmChannel84AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel84AbsentPortn.setStatus("current")
_Pmopm8AlmChannel84MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel84MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel84MismatchPortn = _Pmopm8AlmChannel84MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1, 3),
    _Pmopm8AlmChannel84MismatchPortn_Type()
)
pmopm8AlmChannel84MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel84MismatchPortn.setStatus("current")
_Pmopm8AlmChannel84BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel84BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel84BalancedPortn = _Pmopm8AlmChannel84BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1, 4),
    _Pmopm8AlmChannel84BalancedPortn_Type()
)
pmopm8AlmChannel84BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel84BalancedPortn.setStatus("current")
_Pmopm8AlmChannel84PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel84PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel84PowerLowPortn = _Pmopm8AlmChannel84PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1, 5),
    _Pmopm8AlmChannel84PowerLowPortn_Type()
)
pmopm8AlmChannel84PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel84PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel84PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel84PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel84PowerHighPortn = _Pmopm8AlmChannel84PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1, 6),
    _Pmopm8AlmChannel84PowerHighPortn_Type()
)
pmopm8AlmChannel84PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel84PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel84OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel84OosPortn_Object = MibTableColumn
pmopm8AlmChannel84OosPortn = _Pmopm8AlmChannel84OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 680, 1, 7),
    _Pmopm8AlmChannel84OosPortn_Type()
)
pmopm8AlmChannel84OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel84OosPortn.setStatus("current")
_Pmopm8Almchannel85PortTable_Object = MibTable
pmopm8Almchannel85PortTable = _Pmopm8Almchannel85PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel85PortTable.setStatus("current")
_Pmopm8Almchannel85PortEntry_Object = MibTableRow
pmopm8Almchannel85PortEntry = _Pmopm8Almchannel85PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1)
)
pmopm8Almchannel85PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel85PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel85PortEntry.setStatus("current")


class _Pmopm8Almchannel85PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel85PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel85PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel85PortIndex_Object = MibTableColumn
pmopm8Almchannel85PortIndex = _Pmopm8Almchannel85PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1, 1),
    _Pmopm8Almchannel85PortIndex_Type()
)
pmopm8Almchannel85PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel85PortIndex.setStatus("current")
_Pmopm8AlmChannel85AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel85AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel85AbsentPortn = _Pmopm8AlmChannel85AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1, 2),
    _Pmopm8AlmChannel85AbsentPortn_Type()
)
pmopm8AlmChannel85AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel85AbsentPortn.setStatus("current")
_Pmopm8AlmChannel85MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel85MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel85MismatchPortn = _Pmopm8AlmChannel85MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1, 3),
    _Pmopm8AlmChannel85MismatchPortn_Type()
)
pmopm8AlmChannel85MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel85MismatchPortn.setStatus("current")
_Pmopm8AlmChannel85BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel85BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel85BalancedPortn = _Pmopm8AlmChannel85BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1, 4),
    _Pmopm8AlmChannel85BalancedPortn_Type()
)
pmopm8AlmChannel85BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel85BalancedPortn.setStatus("current")
_Pmopm8AlmChannel85PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel85PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel85PowerLowPortn = _Pmopm8AlmChannel85PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1, 5),
    _Pmopm8AlmChannel85PowerLowPortn_Type()
)
pmopm8AlmChannel85PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel85PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel85PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel85PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel85PowerHighPortn = _Pmopm8AlmChannel85PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1, 6),
    _Pmopm8AlmChannel85PowerHighPortn_Type()
)
pmopm8AlmChannel85PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel85PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel85OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel85OosPortn_Object = MibTableColumn
pmopm8AlmChannel85OosPortn = _Pmopm8AlmChannel85OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 688, 1, 7),
    _Pmopm8AlmChannel85OosPortn_Type()
)
pmopm8AlmChannel85OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel85OosPortn.setStatus("current")
_Pmopm8Almchannel86PortTable_Object = MibTable
pmopm8Almchannel86PortTable = _Pmopm8Almchannel86PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel86PortTable.setStatus("current")
_Pmopm8Almchannel86PortEntry_Object = MibTableRow
pmopm8Almchannel86PortEntry = _Pmopm8Almchannel86PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1)
)
pmopm8Almchannel86PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel86PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel86PortEntry.setStatus("current")


class _Pmopm8Almchannel86PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel86PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel86PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel86PortIndex_Object = MibTableColumn
pmopm8Almchannel86PortIndex = _Pmopm8Almchannel86PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1, 1),
    _Pmopm8Almchannel86PortIndex_Type()
)
pmopm8Almchannel86PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel86PortIndex.setStatus("current")
_Pmopm8AlmChannel86AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel86AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel86AbsentPortn = _Pmopm8AlmChannel86AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1, 2),
    _Pmopm8AlmChannel86AbsentPortn_Type()
)
pmopm8AlmChannel86AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel86AbsentPortn.setStatus("current")
_Pmopm8AlmChannel86MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel86MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel86MismatchPortn = _Pmopm8AlmChannel86MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1, 3),
    _Pmopm8AlmChannel86MismatchPortn_Type()
)
pmopm8AlmChannel86MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel86MismatchPortn.setStatus("current")
_Pmopm8AlmChannel86BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel86BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel86BalancedPortn = _Pmopm8AlmChannel86BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1, 4),
    _Pmopm8AlmChannel86BalancedPortn_Type()
)
pmopm8AlmChannel86BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel86BalancedPortn.setStatus("current")
_Pmopm8AlmChannel86PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel86PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel86PowerLowPortn = _Pmopm8AlmChannel86PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1, 5),
    _Pmopm8AlmChannel86PowerLowPortn_Type()
)
pmopm8AlmChannel86PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel86PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel86PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel86PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel86PowerHighPortn = _Pmopm8AlmChannel86PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1, 6),
    _Pmopm8AlmChannel86PowerHighPortn_Type()
)
pmopm8AlmChannel86PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel86PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel86OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel86OosPortn_Object = MibTableColumn
pmopm8AlmChannel86OosPortn = _Pmopm8AlmChannel86OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 696, 1, 7),
    _Pmopm8AlmChannel86OosPortn_Type()
)
pmopm8AlmChannel86OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel86OosPortn.setStatus("current")
_Pmopm8Almchannel87PortTable_Object = MibTable
pmopm8Almchannel87PortTable = _Pmopm8Almchannel87PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel87PortTable.setStatus("current")
_Pmopm8Almchannel87PortEntry_Object = MibTableRow
pmopm8Almchannel87PortEntry = _Pmopm8Almchannel87PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1)
)
pmopm8Almchannel87PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel87PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel87PortEntry.setStatus("current")


class _Pmopm8Almchannel87PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel87PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel87PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel87PortIndex_Object = MibTableColumn
pmopm8Almchannel87PortIndex = _Pmopm8Almchannel87PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1, 1),
    _Pmopm8Almchannel87PortIndex_Type()
)
pmopm8Almchannel87PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel87PortIndex.setStatus("current")
_Pmopm8AlmChannel87AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel87AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel87AbsentPortn = _Pmopm8AlmChannel87AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1, 2),
    _Pmopm8AlmChannel87AbsentPortn_Type()
)
pmopm8AlmChannel87AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel87AbsentPortn.setStatus("current")
_Pmopm8AlmChannel87MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel87MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel87MismatchPortn = _Pmopm8AlmChannel87MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1, 3),
    _Pmopm8AlmChannel87MismatchPortn_Type()
)
pmopm8AlmChannel87MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel87MismatchPortn.setStatus("current")
_Pmopm8AlmChannel87BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel87BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel87BalancedPortn = _Pmopm8AlmChannel87BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1, 4),
    _Pmopm8AlmChannel87BalancedPortn_Type()
)
pmopm8AlmChannel87BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel87BalancedPortn.setStatus("current")
_Pmopm8AlmChannel87PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel87PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel87PowerLowPortn = _Pmopm8AlmChannel87PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1, 5),
    _Pmopm8AlmChannel87PowerLowPortn_Type()
)
pmopm8AlmChannel87PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel87PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel87PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel87PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel87PowerHighPortn = _Pmopm8AlmChannel87PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1, 6),
    _Pmopm8AlmChannel87PowerHighPortn_Type()
)
pmopm8AlmChannel87PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel87PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel87OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel87OosPortn_Object = MibTableColumn
pmopm8AlmChannel87OosPortn = _Pmopm8AlmChannel87OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 704, 1, 7),
    _Pmopm8AlmChannel87OosPortn_Type()
)
pmopm8AlmChannel87OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel87OosPortn.setStatus("current")
_Pmopm8Almchannel88PortTable_Object = MibTable
pmopm8Almchannel88PortTable = _Pmopm8Almchannel88PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel88PortTable.setStatus("current")
_Pmopm8Almchannel88PortEntry_Object = MibTableRow
pmopm8Almchannel88PortEntry = _Pmopm8Almchannel88PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1)
)
pmopm8Almchannel88PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel88PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel88PortEntry.setStatus("current")


class _Pmopm8Almchannel88PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel88PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel88PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel88PortIndex_Object = MibTableColumn
pmopm8Almchannel88PortIndex = _Pmopm8Almchannel88PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1, 1),
    _Pmopm8Almchannel88PortIndex_Type()
)
pmopm8Almchannel88PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel88PortIndex.setStatus("current")
_Pmopm8AlmChannel88AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel88AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel88AbsentPortn = _Pmopm8AlmChannel88AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1, 2),
    _Pmopm8AlmChannel88AbsentPortn_Type()
)
pmopm8AlmChannel88AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel88AbsentPortn.setStatus("current")
_Pmopm8AlmChannel88MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel88MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel88MismatchPortn = _Pmopm8AlmChannel88MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1, 3),
    _Pmopm8AlmChannel88MismatchPortn_Type()
)
pmopm8AlmChannel88MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel88MismatchPortn.setStatus("current")
_Pmopm8AlmChannel88BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel88BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel88BalancedPortn = _Pmopm8AlmChannel88BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1, 4),
    _Pmopm8AlmChannel88BalancedPortn_Type()
)
pmopm8AlmChannel88BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel88BalancedPortn.setStatus("current")
_Pmopm8AlmChannel88PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel88PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel88PowerLowPortn = _Pmopm8AlmChannel88PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1, 5),
    _Pmopm8AlmChannel88PowerLowPortn_Type()
)
pmopm8AlmChannel88PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel88PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel88PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel88PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel88PowerHighPortn = _Pmopm8AlmChannel88PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1, 6),
    _Pmopm8AlmChannel88PowerHighPortn_Type()
)
pmopm8AlmChannel88PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel88PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel88OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel88OosPortn_Object = MibTableColumn
pmopm8AlmChannel88OosPortn = _Pmopm8AlmChannel88OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 712, 1, 7),
    _Pmopm8AlmChannel88OosPortn_Type()
)
pmopm8AlmChannel88OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel88OosPortn.setStatus("current")
_Pmopm8Almchannel89PortTable_Object = MibTable
pmopm8Almchannel89PortTable = _Pmopm8Almchannel89PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel89PortTable.setStatus("current")
_Pmopm8Almchannel89PortEntry_Object = MibTableRow
pmopm8Almchannel89PortEntry = _Pmopm8Almchannel89PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1)
)
pmopm8Almchannel89PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel89PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel89PortEntry.setStatus("current")


class _Pmopm8Almchannel89PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel89PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel89PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel89PortIndex_Object = MibTableColumn
pmopm8Almchannel89PortIndex = _Pmopm8Almchannel89PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1, 1),
    _Pmopm8Almchannel89PortIndex_Type()
)
pmopm8Almchannel89PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel89PortIndex.setStatus("current")
_Pmopm8AlmChannel89AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel89AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel89AbsentPortn = _Pmopm8AlmChannel89AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1, 2),
    _Pmopm8AlmChannel89AbsentPortn_Type()
)
pmopm8AlmChannel89AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel89AbsentPortn.setStatus("current")
_Pmopm8AlmChannel89MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel89MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel89MismatchPortn = _Pmopm8AlmChannel89MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1, 3),
    _Pmopm8AlmChannel89MismatchPortn_Type()
)
pmopm8AlmChannel89MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel89MismatchPortn.setStatus("current")
_Pmopm8AlmChannel89BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel89BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel89BalancedPortn = _Pmopm8AlmChannel89BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1, 4),
    _Pmopm8AlmChannel89BalancedPortn_Type()
)
pmopm8AlmChannel89BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel89BalancedPortn.setStatus("current")
_Pmopm8AlmChannel89PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel89PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel89PowerLowPortn = _Pmopm8AlmChannel89PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1, 5),
    _Pmopm8AlmChannel89PowerLowPortn_Type()
)
pmopm8AlmChannel89PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel89PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel89PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel89PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel89PowerHighPortn = _Pmopm8AlmChannel89PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1, 6),
    _Pmopm8AlmChannel89PowerHighPortn_Type()
)
pmopm8AlmChannel89PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel89PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel89OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel89OosPortn_Object = MibTableColumn
pmopm8AlmChannel89OosPortn = _Pmopm8AlmChannel89OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 720, 1, 7),
    _Pmopm8AlmChannel89OosPortn_Type()
)
pmopm8AlmChannel89OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel89OosPortn.setStatus("current")
_Pmopm8Almchannel90PortTable_Object = MibTable
pmopm8Almchannel90PortTable = _Pmopm8Almchannel90PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel90PortTable.setStatus("current")
_Pmopm8Almchannel90PortEntry_Object = MibTableRow
pmopm8Almchannel90PortEntry = _Pmopm8Almchannel90PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1)
)
pmopm8Almchannel90PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel90PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel90PortEntry.setStatus("current")


class _Pmopm8Almchannel90PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel90PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel90PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel90PortIndex_Object = MibTableColumn
pmopm8Almchannel90PortIndex = _Pmopm8Almchannel90PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1, 1),
    _Pmopm8Almchannel90PortIndex_Type()
)
pmopm8Almchannel90PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel90PortIndex.setStatus("current")
_Pmopm8AlmChannel90AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel90AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel90AbsentPortn = _Pmopm8AlmChannel90AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1, 2),
    _Pmopm8AlmChannel90AbsentPortn_Type()
)
pmopm8AlmChannel90AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel90AbsentPortn.setStatus("current")
_Pmopm8AlmChannel90MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel90MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel90MismatchPortn = _Pmopm8AlmChannel90MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1, 3),
    _Pmopm8AlmChannel90MismatchPortn_Type()
)
pmopm8AlmChannel90MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel90MismatchPortn.setStatus("current")
_Pmopm8AlmChannel90BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel90BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel90BalancedPortn = _Pmopm8AlmChannel90BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1, 4),
    _Pmopm8AlmChannel90BalancedPortn_Type()
)
pmopm8AlmChannel90BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel90BalancedPortn.setStatus("current")
_Pmopm8AlmChannel90PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel90PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel90PowerLowPortn = _Pmopm8AlmChannel90PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1, 5),
    _Pmopm8AlmChannel90PowerLowPortn_Type()
)
pmopm8AlmChannel90PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel90PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel90PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel90PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel90PowerHighPortn = _Pmopm8AlmChannel90PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1, 6),
    _Pmopm8AlmChannel90PowerHighPortn_Type()
)
pmopm8AlmChannel90PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel90PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel90OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel90OosPortn_Object = MibTableColumn
pmopm8AlmChannel90OosPortn = _Pmopm8AlmChannel90OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 728, 1, 7),
    _Pmopm8AlmChannel90OosPortn_Type()
)
pmopm8AlmChannel90OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel90OosPortn.setStatus("current")
_Pmopm8Almchannel91PortTable_Object = MibTable
pmopm8Almchannel91PortTable = _Pmopm8Almchannel91PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel91PortTable.setStatus("current")
_Pmopm8Almchannel91PortEntry_Object = MibTableRow
pmopm8Almchannel91PortEntry = _Pmopm8Almchannel91PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1)
)
pmopm8Almchannel91PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel91PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel91PortEntry.setStatus("current")


class _Pmopm8Almchannel91PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel91PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel91PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel91PortIndex_Object = MibTableColumn
pmopm8Almchannel91PortIndex = _Pmopm8Almchannel91PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1, 1),
    _Pmopm8Almchannel91PortIndex_Type()
)
pmopm8Almchannel91PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel91PortIndex.setStatus("current")
_Pmopm8AlmChannel91AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel91AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel91AbsentPortn = _Pmopm8AlmChannel91AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1, 2),
    _Pmopm8AlmChannel91AbsentPortn_Type()
)
pmopm8AlmChannel91AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel91AbsentPortn.setStatus("current")
_Pmopm8AlmChannel91MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel91MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel91MismatchPortn = _Pmopm8AlmChannel91MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1, 3),
    _Pmopm8AlmChannel91MismatchPortn_Type()
)
pmopm8AlmChannel91MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel91MismatchPortn.setStatus("current")
_Pmopm8AlmChannel91BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel91BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel91BalancedPortn = _Pmopm8AlmChannel91BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1, 4),
    _Pmopm8AlmChannel91BalancedPortn_Type()
)
pmopm8AlmChannel91BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel91BalancedPortn.setStatus("current")
_Pmopm8AlmChannel91PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel91PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel91PowerLowPortn = _Pmopm8AlmChannel91PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1, 5),
    _Pmopm8AlmChannel91PowerLowPortn_Type()
)
pmopm8AlmChannel91PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel91PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel91PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel91PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel91PowerHighPortn = _Pmopm8AlmChannel91PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1, 6),
    _Pmopm8AlmChannel91PowerHighPortn_Type()
)
pmopm8AlmChannel91PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel91PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel91OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel91OosPortn_Object = MibTableColumn
pmopm8AlmChannel91OosPortn = _Pmopm8AlmChannel91OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 736, 1, 7),
    _Pmopm8AlmChannel91OosPortn_Type()
)
pmopm8AlmChannel91OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel91OosPortn.setStatus("current")
_Pmopm8Almchannel92PortTable_Object = MibTable
pmopm8Almchannel92PortTable = _Pmopm8Almchannel92PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel92PortTable.setStatus("current")
_Pmopm8Almchannel92PortEntry_Object = MibTableRow
pmopm8Almchannel92PortEntry = _Pmopm8Almchannel92PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1)
)
pmopm8Almchannel92PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel92PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel92PortEntry.setStatus("current")


class _Pmopm8Almchannel92PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel92PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel92PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel92PortIndex_Object = MibTableColumn
pmopm8Almchannel92PortIndex = _Pmopm8Almchannel92PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1, 1),
    _Pmopm8Almchannel92PortIndex_Type()
)
pmopm8Almchannel92PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel92PortIndex.setStatus("current")
_Pmopm8AlmChannel92AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel92AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel92AbsentPortn = _Pmopm8AlmChannel92AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1, 2),
    _Pmopm8AlmChannel92AbsentPortn_Type()
)
pmopm8AlmChannel92AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel92AbsentPortn.setStatus("current")
_Pmopm8AlmChannel92MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel92MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel92MismatchPortn = _Pmopm8AlmChannel92MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1, 3),
    _Pmopm8AlmChannel92MismatchPortn_Type()
)
pmopm8AlmChannel92MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel92MismatchPortn.setStatus("current")
_Pmopm8AlmChannel92BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel92BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel92BalancedPortn = _Pmopm8AlmChannel92BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1, 4),
    _Pmopm8AlmChannel92BalancedPortn_Type()
)
pmopm8AlmChannel92BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel92BalancedPortn.setStatus("current")
_Pmopm8AlmChannel92PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel92PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel92PowerLowPortn = _Pmopm8AlmChannel92PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1, 5),
    _Pmopm8AlmChannel92PowerLowPortn_Type()
)
pmopm8AlmChannel92PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel92PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel92PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel92PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel92PowerHighPortn = _Pmopm8AlmChannel92PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1, 6),
    _Pmopm8AlmChannel92PowerHighPortn_Type()
)
pmopm8AlmChannel92PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel92PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel92OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel92OosPortn_Object = MibTableColumn
pmopm8AlmChannel92OosPortn = _Pmopm8AlmChannel92OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 744, 1, 7),
    _Pmopm8AlmChannel92OosPortn_Type()
)
pmopm8AlmChannel92OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel92OosPortn.setStatus("current")
_Pmopm8Almchannel93PortTable_Object = MibTable
pmopm8Almchannel93PortTable = _Pmopm8Almchannel93PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel93PortTable.setStatus("current")
_Pmopm8Almchannel93PortEntry_Object = MibTableRow
pmopm8Almchannel93PortEntry = _Pmopm8Almchannel93PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1)
)
pmopm8Almchannel93PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel93PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel93PortEntry.setStatus("current")


class _Pmopm8Almchannel93PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel93PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel93PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel93PortIndex_Object = MibTableColumn
pmopm8Almchannel93PortIndex = _Pmopm8Almchannel93PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1, 1),
    _Pmopm8Almchannel93PortIndex_Type()
)
pmopm8Almchannel93PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel93PortIndex.setStatus("current")
_Pmopm8AlmChannel93AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel93AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel93AbsentPortn = _Pmopm8AlmChannel93AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1, 2),
    _Pmopm8AlmChannel93AbsentPortn_Type()
)
pmopm8AlmChannel93AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel93AbsentPortn.setStatus("current")
_Pmopm8AlmChannel93MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel93MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel93MismatchPortn = _Pmopm8AlmChannel93MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1, 3),
    _Pmopm8AlmChannel93MismatchPortn_Type()
)
pmopm8AlmChannel93MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel93MismatchPortn.setStatus("current")
_Pmopm8AlmChannel93BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel93BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel93BalancedPortn = _Pmopm8AlmChannel93BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1, 4),
    _Pmopm8AlmChannel93BalancedPortn_Type()
)
pmopm8AlmChannel93BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel93BalancedPortn.setStatus("current")
_Pmopm8AlmChannel93PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel93PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel93PowerLowPortn = _Pmopm8AlmChannel93PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1, 5),
    _Pmopm8AlmChannel93PowerLowPortn_Type()
)
pmopm8AlmChannel93PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel93PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel93PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel93PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel93PowerHighPortn = _Pmopm8AlmChannel93PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1, 6),
    _Pmopm8AlmChannel93PowerHighPortn_Type()
)
pmopm8AlmChannel93PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel93PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel93OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel93OosPortn_Object = MibTableColumn
pmopm8AlmChannel93OosPortn = _Pmopm8AlmChannel93OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 752, 1, 7),
    _Pmopm8AlmChannel93OosPortn_Type()
)
pmopm8AlmChannel93OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel93OosPortn.setStatus("current")
_Pmopm8Almchannel94PortTable_Object = MibTable
pmopm8Almchannel94PortTable = _Pmopm8Almchannel94PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel94PortTable.setStatus("current")
_Pmopm8Almchannel94PortEntry_Object = MibTableRow
pmopm8Almchannel94PortEntry = _Pmopm8Almchannel94PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1)
)
pmopm8Almchannel94PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel94PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel94PortEntry.setStatus("current")


class _Pmopm8Almchannel94PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel94PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel94PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel94PortIndex_Object = MibTableColumn
pmopm8Almchannel94PortIndex = _Pmopm8Almchannel94PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1, 1),
    _Pmopm8Almchannel94PortIndex_Type()
)
pmopm8Almchannel94PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel94PortIndex.setStatus("current")
_Pmopm8AlmChannel94AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel94AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel94AbsentPortn = _Pmopm8AlmChannel94AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1, 2),
    _Pmopm8AlmChannel94AbsentPortn_Type()
)
pmopm8AlmChannel94AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel94AbsentPortn.setStatus("current")
_Pmopm8AlmChannel94MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel94MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel94MismatchPortn = _Pmopm8AlmChannel94MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1, 3),
    _Pmopm8AlmChannel94MismatchPortn_Type()
)
pmopm8AlmChannel94MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel94MismatchPortn.setStatus("current")
_Pmopm8AlmChannel94BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel94BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel94BalancedPortn = _Pmopm8AlmChannel94BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1, 4),
    _Pmopm8AlmChannel94BalancedPortn_Type()
)
pmopm8AlmChannel94BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel94BalancedPortn.setStatus("current")
_Pmopm8AlmChannel94PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel94PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel94PowerLowPortn = _Pmopm8AlmChannel94PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1, 5),
    _Pmopm8AlmChannel94PowerLowPortn_Type()
)
pmopm8AlmChannel94PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel94PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel94PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel94PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel94PowerHighPortn = _Pmopm8AlmChannel94PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1, 6),
    _Pmopm8AlmChannel94PowerHighPortn_Type()
)
pmopm8AlmChannel94PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel94PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel94OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel94OosPortn_Object = MibTableColumn
pmopm8AlmChannel94OosPortn = _Pmopm8AlmChannel94OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 760, 1, 7),
    _Pmopm8AlmChannel94OosPortn_Type()
)
pmopm8AlmChannel94OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel94OosPortn.setStatus("current")
_Pmopm8Almchannel95PortTable_Object = MibTable
pmopm8Almchannel95PortTable = _Pmopm8Almchannel95PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel95PortTable.setStatus("current")
_Pmopm8Almchannel95PortEntry_Object = MibTableRow
pmopm8Almchannel95PortEntry = _Pmopm8Almchannel95PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1)
)
pmopm8Almchannel95PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel95PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel95PortEntry.setStatus("current")


class _Pmopm8Almchannel95PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel95PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel95PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel95PortIndex_Object = MibTableColumn
pmopm8Almchannel95PortIndex = _Pmopm8Almchannel95PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1, 1),
    _Pmopm8Almchannel95PortIndex_Type()
)
pmopm8Almchannel95PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel95PortIndex.setStatus("current")
_Pmopm8AlmChannel95AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel95AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel95AbsentPortn = _Pmopm8AlmChannel95AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1, 2),
    _Pmopm8AlmChannel95AbsentPortn_Type()
)
pmopm8AlmChannel95AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel95AbsentPortn.setStatus("current")
_Pmopm8AlmChannel95MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel95MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel95MismatchPortn = _Pmopm8AlmChannel95MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1, 3),
    _Pmopm8AlmChannel95MismatchPortn_Type()
)
pmopm8AlmChannel95MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel95MismatchPortn.setStatus("current")
_Pmopm8AlmChannel95BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel95BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel95BalancedPortn = _Pmopm8AlmChannel95BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1, 4),
    _Pmopm8AlmChannel95BalancedPortn_Type()
)
pmopm8AlmChannel95BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel95BalancedPortn.setStatus("current")
_Pmopm8AlmChannel95PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel95PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel95PowerLowPortn = _Pmopm8AlmChannel95PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1, 5),
    _Pmopm8AlmChannel95PowerLowPortn_Type()
)
pmopm8AlmChannel95PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel95PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel95PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel95PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel95PowerHighPortn = _Pmopm8AlmChannel95PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1, 6),
    _Pmopm8AlmChannel95PowerHighPortn_Type()
)
pmopm8AlmChannel95PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel95PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel95OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel95OosPortn_Object = MibTableColumn
pmopm8AlmChannel95OosPortn = _Pmopm8AlmChannel95OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 768, 1, 7),
    _Pmopm8AlmChannel95OosPortn_Type()
)
pmopm8AlmChannel95OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel95OosPortn.setStatus("current")
_Pmopm8Almchannel96PortTable_Object = MibTable
pmopm8Almchannel96PortTable = _Pmopm8Almchannel96PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776)
)
if mibBuilder.loadTexts:
    pmopm8Almchannel96PortTable.setStatus("current")
_Pmopm8Almchannel96PortEntry_Object = MibTableRow
pmopm8Almchannel96PortEntry = _Pmopm8Almchannel96PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1)
)
pmopm8Almchannel96PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Almchannel96PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm8Almchannel96PortEntry.setStatus("current")


class _Pmopm8Almchannel96PortIndex_Type(Integer32):
    """Custom type pmopm8Almchannel96PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Almchannel96PortIndex_Type.__name__ = "Integer32"
_Pmopm8Almchannel96PortIndex_Object = MibTableColumn
pmopm8Almchannel96PortIndex = _Pmopm8Almchannel96PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1, 1),
    _Pmopm8Almchannel96PortIndex_Type()
)
pmopm8Almchannel96PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Almchannel96PortIndex.setStatus("current")
_Pmopm8AlmChannel96AbsentPortn_Type = EkiOnOff
_Pmopm8AlmChannel96AbsentPortn_Object = MibTableColumn
pmopm8AlmChannel96AbsentPortn = _Pmopm8AlmChannel96AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1, 2),
    _Pmopm8AlmChannel96AbsentPortn_Type()
)
pmopm8AlmChannel96AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel96AbsentPortn.setStatus("current")
_Pmopm8AlmChannel96MismatchPortn_Type = EkiOnOff
_Pmopm8AlmChannel96MismatchPortn_Object = MibTableColumn
pmopm8AlmChannel96MismatchPortn = _Pmopm8AlmChannel96MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1, 3),
    _Pmopm8AlmChannel96MismatchPortn_Type()
)
pmopm8AlmChannel96MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel96MismatchPortn.setStatus("current")
_Pmopm8AlmChannel96BalancedPortn_Type = EkiOnOff
_Pmopm8AlmChannel96BalancedPortn_Object = MibTableColumn
pmopm8AlmChannel96BalancedPortn = _Pmopm8AlmChannel96BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1, 4),
    _Pmopm8AlmChannel96BalancedPortn_Type()
)
pmopm8AlmChannel96BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel96BalancedPortn.setStatus("current")
_Pmopm8AlmChannel96PowerLowPortn_Type = EkiOnOff
_Pmopm8AlmChannel96PowerLowPortn_Object = MibTableColumn
pmopm8AlmChannel96PowerLowPortn = _Pmopm8AlmChannel96PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1, 5),
    _Pmopm8AlmChannel96PowerLowPortn_Type()
)
pmopm8AlmChannel96PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel96PowerLowPortn.setStatus("current")
_Pmopm8AlmChannel96PowerHighPortn_Type = EkiOnOff
_Pmopm8AlmChannel96PowerHighPortn_Object = MibTableColumn
pmopm8AlmChannel96PowerHighPortn = _Pmopm8AlmChannel96PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1, 6),
    _Pmopm8AlmChannel96PowerHighPortn_Type()
)
pmopm8AlmChannel96PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel96PowerHighPortn.setStatus("current")
_Pmopm8AlmChannel96OosPortn_Type = EkiOnOff
_Pmopm8AlmChannel96OosPortn_Object = MibTableColumn
pmopm8AlmChannel96OosPortn = _Pmopm8AlmChannel96OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 2, 3, 776, 1, 7),
    _Pmopm8AlmChannel96OosPortn_Type()
)
pmopm8AlmChannel96OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8AlmChannel96OosPortn.setStatus("current")
_Pmopm8AlmLine_ObjectIdentity = ObjectIdentity
pmopm8AlmLine = _Pmopm8AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 3)
)
_Pmopm8AlmLineNurg_ObjectIdentity = ObjectIdentity
pmopm8AlmLineNurg = _Pmopm8AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 3, 1)
)
_Pmopm8AlmLineUrg_ObjectIdentity = ObjectIdentity
pmopm8AlmLineUrg = _Pmopm8AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 3, 2)
)
_Pmopm8AlmLineCrit_ObjectIdentity = ObjectIdentity
pmopm8AlmLineCrit = _Pmopm8AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 2, 3, 3)
)
_Pmopm8measures_ObjectIdentity = ObjectIdentity
pmopm8measures = _Pmopm8measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3)
)
_Pmopm8MesrOther_ObjectIdentity = ObjectIdentity
pmopm8MesrOther = _Pmopm8MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 1)
)


class _Pmopm8MesropmTemp_Type(Unsigned32):
    """Custom type pmopm8MesropmTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8MesropmTemp_Type.__name__ = "Unsigned32"
_Pmopm8MesropmTemp_Object = MibScalar
pmopm8MesropmTemp = _Pmopm8MesropmTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 1, 808),
    _Pmopm8MesropmTemp_Type()
)
pmopm8MesropmTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8MesropmTemp.setStatus("current")
_Pmopm8MesrClient_ObjectIdentity = ObjectIdentity
pmopm8MesrClient = _Pmopm8MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2)
)
_Pmopm8Mesrchannel1Table_Object = MibTable
pmopm8Mesrchannel1Table = _Pmopm8Mesrchannel1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel1Table.setStatus("current")
_Pmopm8Mesrchannel1Entry_Object = MibTableRow
pmopm8Mesrchannel1Entry = _Pmopm8Mesrchannel1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 16, 1)
)
pmopm8Mesrchannel1Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel1Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel1Entry.setStatus("current")


class _Pmopm8Mesrchannel1Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel1Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel1Index_Object = MibTableColumn
pmopm8Mesrchannel1Index = _Pmopm8Mesrchannel1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 16, 1, 1),
    _Pmopm8Mesrchannel1Index_Type()
)
pmopm8Mesrchannel1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel1Index.setStatus("current")


class _Pmopm8Mesrchannel1Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel1Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel1Portn_Object = MibTableColumn
pmopm8Mesrchannel1Portn = _Pmopm8Mesrchannel1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 16, 1, 2),
    _Pmopm8Mesrchannel1Portn_Type()
)
pmopm8Mesrchannel1Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel1Portn.setStatus("current")
_Pmopm8Mesrchannel2Table_Object = MibTable
pmopm8Mesrchannel2Table = _Pmopm8Mesrchannel2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel2Table.setStatus("current")
_Pmopm8Mesrchannel2Entry_Object = MibTableRow
pmopm8Mesrchannel2Entry = _Pmopm8Mesrchannel2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 24, 1)
)
pmopm8Mesrchannel2Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel2Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel2Entry.setStatus("current")


class _Pmopm8Mesrchannel2Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel2Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel2Index_Object = MibTableColumn
pmopm8Mesrchannel2Index = _Pmopm8Mesrchannel2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 24, 1, 1),
    _Pmopm8Mesrchannel2Index_Type()
)
pmopm8Mesrchannel2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel2Index.setStatus("current")


class _Pmopm8Mesrchannel2Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel2Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel2Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel2Portn_Object = MibTableColumn
pmopm8Mesrchannel2Portn = _Pmopm8Mesrchannel2Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 24, 1, 2),
    _Pmopm8Mesrchannel2Portn_Type()
)
pmopm8Mesrchannel2Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel2Portn.setStatus("current")
_Pmopm8Mesrchannel3Table_Object = MibTable
pmopm8Mesrchannel3Table = _Pmopm8Mesrchannel3Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel3Table.setStatus("current")
_Pmopm8Mesrchannel3Entry_Object = MibTableRow
pmopm8Mesrchannel3Entry = _Pmopm8Mesrchannel3Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 32, 1)
)
pmopm8Mesrchannel3Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel3Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel3Entry.setStatus("current")


class _Pmopm8Mesrchannel3Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel3Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel3Index_Object = MibTableColumn
pmopm8Mesrchannel3Index = _Pmopm8Mesrchannel3Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 32, 1, 1),
    _Pmopm8Mesrchannel3Index_Type()
)
pmopm8Mesrchannel3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel3Index.setStatus("current")


class _Pmopm8Mesrchannel3Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel3Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel3Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel3Portn_Object = MibTableColumn
pmopm8Mesrchannel3Portn = _Pmopm8Mesrchannel3Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 32, 1, 2),
    _Pmopm8Mesrchannel3Portn_Type()
)
pmopm8Mesrchannel3Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel3Portn.setStatus("current")
_Pmopm8Mesrchannel4Table_Object = MibTable
pmopm8Mesrchannel4Table = _Pmopm8Mesrchannel4Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel4Table.setStatus("current")
_Pmopm8Mesrchannel4Entry_Object = MibTableRow
pmopm8Mesrchannel4Entry = _Pmopm8Mesrchannel4Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 40, 1)
)
pmopm8Mesrchannel4Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel4Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel4Entry.setStatus("current")


class _Pmopm8Mesrchannel4Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel4Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel4Index_Object = MibTableColumn
pmopm8Mesrchannel4Index = _Pmopm8Mesrchannel4Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 40, 1, 1),
    _Pmopm8Mesrchannel4Index_Type()
)
pmopm8Mesrchannel4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel4Index.setStatus("current")


class _Pmopm8Mesrchannel4Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel4Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel4Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel4Portn_Object = MibTableColumn
pmopm8Mesrchannel4Portn = _Pmopm8Mesrchannel4Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 40, 1, 2),
    _Pmopm8Mesrchannel4Portn_Type()
)
pmopm8Mesrchannel4Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel4Portn.setStatus("current")
_Pmopm8Mesrchannel5Table_Object = MibTable
pmopm8Mesrchannel5Table = _Pmopm8Mesrchannel5Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel5Table.setStatus("current")
_Pmopm8Mesrchannel5Entry_Object = MibTableRow
pmopm8Mesrchannel5Entry = _Pmopm8Mesrchannel5Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 48, 1)
)
pmopm8Mesrchannel5Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel5Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel5Entry.setStatus("current")


class _Pmopm8Mesrchannel5Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel5Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel5Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel5Index_Object = MibTableColumn
pmopm8Mesrchannel5Index = _Pmopm8Mesrchannel5Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 48, 1, 1),
    _Pmopm8Mesrchannel5Index_Type()
)
pmopm8Mesrchannel5Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel5Index.setStatus("current")


class _Pmopm8Mesrchannel5Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel5Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel5Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel5Portn_Object = MibTableColumn
pmopm8Mesrchannel5Portn = _Pmopm8Mesrchannel5Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 48, 1, 2),
    _Pmopm8Mesrchannel5Portn_Type()
)
pmopm8Mesrchannel5Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel5Portn.setStatus("current")
_Pmopm8Mesrchannel6Table_Object = MibTable
pmopm8Mesrchannel6Table = _Pmopm8Mesrchannel6Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 56)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel6Table.setStatus("current")
_Pmopm8Mesrchannel6Entry_Object = MibTableRow
pmopm8Mesrchannel6Entry = _Pmopm8Mesrchannel6Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 56, 1)
)
pmopm8Mesrchannel6Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel6Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel6Entry.setStatus("current")


class _Pmopm8Mesrchannel6Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel6Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel6Index_Object = MibTableColumn
pmopm8Mesrchannel6Index = _Pmopm8Mesrchannel6Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 56, 1, 1),
    _Pmopm8Mesrchannel6Index_Type()
)
pmopm8Mesrchannel6Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel6Index.setStatus("current")


class _Pmopm8Mesrchannel6Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel6Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel6Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel6Portn_Object = MibTableColumn
pmopm8Mesrchannel6Portn = _Pmopm8Mesrchannel6Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 56, 1, 2),
    _Pmopm8Mesrchannel6Portn_Type()
)
pmopm8Mesrchannel6Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel6Portn.setStatus("current")
_Pmopm8Mesrchannel7Table_Object = MibTable
pmopm8Mesrchannel7Table = _Pmopm8Mesrchannel7Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel7Table.setStatus("current")
_Pmopm8Mesrchannel7Entry_Object = MibTableRow
pmopm8Mesrchannel7Entry = _Pmopm8Mesrchannel7Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 64, 1)
)
pmopm8Mesrchannel7Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel7Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel7Entry.setStatus("current")


class _Pmopm8Mesrchannel7Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel7Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel7Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel7Index_Object = MibTableColumn
pmopm8Mesrchannel7Index = _Pmopm8Mesrchannel7Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 64, 1, 1),
    _Pmopm8Mesrchannel7Index_Type()
)
pmopm8Mesrchannel7Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel7Index.setStatus("current")


class _Pmopm8Mesrchannel7Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel7Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel7Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel7Portn_Object = MibTableColumn
pmopm8Mesrchannel7Portn = _Pmopm8Mesrchannel7Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 64, 1, 2),
    _Pmopm8Mesrchannel7Portn_Type()
)
pmopm8Mesrchannel7Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel7Portn.setStatus("current")
_Pmopm8Mesrchannel8Table_Object = MibTable
pmopm8Mesrchannel8Table = _Pmopm8Mesrchannel8Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 72)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel8Table.setStatus("current")
_Pmopm8Mesrchannel8Entry_Object = MibTableRow
pmopm8Mesrchannel8Entry = _Pmopm8Mesrchannel8Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 72, 1)
)
pmopm8Mesrchannel8Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel8Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel8Entry.setStatus("current")


class _Pmopm8Mesrchannel8Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel8Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel8Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel8Index_Object = MibTableColumn
pmopm8Mesrchannel8Index = _Pmopm8Mesrchannel8Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 72, 1, 1),
    _Pmopm8Mesrchannel8Index_Type()
)
pmopm8Mesrchannel8Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel8Index.setStatus("current")


class _Pmopm8Mesrchannel8Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel8Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel8Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel8Portn_Object = MibTableColumn
pmopm8Mesrchannel8Portn = _Pmopm8Mesrchannel8Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 72, 1, 2),
    _Pmopm8Mesrchannel8Portn_Type()
)
pmopm8Mesrchannel8Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel8Portn.setStatus("current")
_Pmopm8Mesrchannel9Table_Object = MibTable
pmopm8Mesrchannel9Table = _Pmopm8Mesrchannel9Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 80)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel9Table.setStatus("current")
_Pmopm8Mesrchannel9Entry_Object = MibTableRow
pmopm8Mesrchannel9Entry = _Pmopm8Mesrchannel9Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 80, 1)
)
pmopm8Mesrchannel9Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel9Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel9Entry.setStatus("current")


class _Pmopm8Mesrchannel9Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel9Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel9Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel9Index_Object = MibTableColumn
pmopm8Mesrchannel9Index = _Pmopm8Mesrchannel9Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 80, 1, 1),
    _Pmopm8Mesrchannel9Index_Type()
)
pmopm8Mesrchannel9Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel9Index.setStatus("current")


class _Pmopm8Mesrchannel9Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel9Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel9Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel9Portn_Object = MibTableColumn
pmopm8Mesrchannel9Portn = _Pmopm8Mesrchannel9Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 80, 1, 2),
    _Pmopm8Mesrchannel9Portn_Type()
)
pmopm8Mesrchannel9Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel9Portn.setStatus("current")
_Pmopm8Mesrchannel10Table_Object = MibTable
pmopm8Mesrchannel10Table = _Pmopm8Mesrchannel10Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 88)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel10Table.setStatus("current")
_Pmopm8Mesrchannel10Entry_Object = MibTableRow
pmopm8Mesrchannel10Entry = _Pmopm8Mesrchannel10Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 88, 1)
)
pmopm8Mesrchannel10Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel10Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel10Entry.setStatus("current")


class _Pmopm8Mesrchannel10Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel10Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel10Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel10Index_Object = MibTableColumn
pmopm8Mesrchannel10Index = _Pmopm8Mesrchannel10Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 88, 1, 1),
    _Pmopm8Mesrchannel10Index_Type()
)
pmopm8Mesrchannel10Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel10Index.setStatus("current")


class _Pmopm8Mesrchannel10Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel10Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel10Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel10Portn_Object = MibTableColumn
pmopm8Mesrchannel10Portn = _Pmopm8Mesrchannel10Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 88, 1, 2),
    _Pmopm8Mesrchannel10Portn_Type()
)
pmopm8Mesrchannel10Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel10Portn.setStatus("current")
_Pmopm8Mesrchannel11Table_Object = MibTable
pmopm8Mesrchannel11Table = _Pmopm8Mesrchannel11Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 96)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel11Table.setStatus("current")
_Pmopm8Mesrchannel11Entry_Object = MibTableRow
pmopm8Mesrchannel11Entry = _Pmopm8Mesrchannel11Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 96, 1)
)
pmopm8Mesrchannel11Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel11Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel11Entry.setStatus("current")


class _Pmopm8Mesrchannel11Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel11Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel11Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel11Index_Object = MibTableColumn
pmopm8Mesrchannel11Index = _Pmopm8Mesrchannel11Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 96, 1, 1),
    _Pmopm8Mesrchannel11Index_Type()
)
pmopm8Mesrchannel11Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel11Index.setStatus("current")


class _Pmopm8Mesrchannel11Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel11Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel11Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel11Portn_Object = MibTableColumn
pmopm8Mesrchannel11Portn = _Pmopm8Mesrchannel11Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 96, 1, 2),
    _Pmopm8Mesrchannel11Portn_Type()
)
pmopm8Mesrchannel11Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel11Portn.setStatus("current")
_Pmopm8Mesrchannel12Table_Object = MibTable
pmopm8Mesrchannel12Table = _Pmopm8Mesrchannel12Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 104)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel12Table.setStatus("current")
_Pmopm8Mesrchannel12Entry_Object = MibTableRow
pmopm8Mesrchannel12Entry = _Pmopm8Mesrchannel12Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 104, 1)
)
pmopm8Mesrchannel12Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel12Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel12Entry.setStatus("current")


class _Pmopm8Mesrchannel12Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel12Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel12Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel12Index_Object = MibTableColumn
pmopm8Mesrchannel12Index = _Pmopm8Mesrchannel12Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 104, 1, 1),
    _Pmopm8Mesrchannel12Index_Type()
)
pmopm8Mesrchannel12Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel12Index.setStatus("current")


class _Pmopm8Mesrchannel12Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel12Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel12Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel12Portn_Object = MibTableColumn
pmopm8Mesrchannel12Portn = _Pmopm8Mesrchannel12Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 104, 1, 2),
    _Pmopm8Mesrchannel12Portn_Type()
)
pmopm8Mesrchannel12Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel12Portn.setStatus("current")
_Pmopm8Mesrchannel13Table_Object = MibTable
pmopm8Mesrchannel13Table = _Pmopm8Mesrchannel13Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 112)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel13Table.setStatus("current")
_Pmopm8Mesrchannel13Entry_Object = MibTableRow
pmopm8Mesrchannel13Entry = _Pmopm8Mesrchannel13Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 112, 1)
)
pmopm8Mesrchannel13Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel13Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel13Entry.setStatus("current")


class _Pmopm8Mesrchannel13Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel13Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel13Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel13Index_Object = MibTableColumn
pmopm8Mesrchannel13Index = _Pmopm8Mesrchannel13Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 112, 1, 1),
    _Pmopm8Mesrchannel13Index_Type()
)
pmopm8Mesrchannel13Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel13Index.setStatus("current")


class _Pmopm8Mesrchannel13Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel13Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel13Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel13Portn_Object = MibTableColumn
pmopm8Mesrchannel13Portn = _Pmopm8Mesrchannel13Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 112, 1, 2),
    _Pmopm8Mesrchannel13Portn_Type()
)
pmopm8Mesrchannel13Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel13Portn.setStatus("current")
_Pmopm8Mesrchannel14Table_Object = MibTable
pmopm8Mesrchannel14Table = _Pmopm8Mesrchannel14Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 120)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel14Table.setStatus("current")
_Pmopm8Mesrchannel14Entry_Object = MibTableRow
pmopm8Mesrchannel14Entry = _Pmopm8Mesrchannel14Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 120, 1)
)
pmopm8Mesrchannel14Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel14Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel14Entry.setStatus("current")


class _Pmopm8Mesrchannel14Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel14Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel14Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel14Index_Object = MibTableColumn
pmopm8Mesrchannel14Index = _Pmopm8Mesrchannel14Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 120, 1, 1),
    _Pmopm8Mesrchannel14Index_Type()
)
pmopm8Mesrchannel14Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel14Index.setStatus("current")


class _Pmopm8Mesrchannel14Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel14Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel14Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel14Portn_Object = MibTableColumn
pmopm8Mesrchannel14Portn = _Pmopm8Mesrchannel14Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 120, 1, 2),
    _Pmopm8Mesrchannel14Portn_Type()
)
pmopm8Mesrchannel14Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel14Portn.setStatus("current")
_Pmopm8Mesrchannel15Table_Object = MibTable
pmopm8Mesrchannel15Table = _Pmopm8Mesrchannel15Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 128)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel15Table.setStatus("current")
_Pmopm8Mesrchannel15Entry_Object = MibTableRow
pmopm8Mesrchannel15Entry = _Pmopm8Mesrchannel15Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 128, 1)
)
pmopm8Mesrchannel15Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel15Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel15Entry.setStatus("current")


class _Pmopm8Mesrchannel15Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel15Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel15Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel15Index_Object = MibTableColumn
pmopm8Mesrchannel15Index = _Pmopm8Mesrchannel15Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 128, 1, 1),
    _Pmopm8Mesrchannel15Index_Type()
)
pmopm8Mesrchannel15Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel15Index.setStatus("current")


class _Pmopm8Mesrchannel15Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel15Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel15Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel15Portn_Object = MibTableColumn
pmopm8Mesrchannel15Portn = _Pmopm8Mesrchannel15Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 128, 1, 2),
    _Pmopm8Mesrchannel15Portn_Type()
)
pmopm8Mesrchannel15Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel15Portn.setStatus("current")
_Pmopm8Mesrchannel16Table_Object = MibTable
pmopm8Mesrchannel16Table = _Pmopm8Mesrchannel16Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 136)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel16Table.setStatus("current")
_Pmopm8Mesrchannel16Entry_Object = MibTableRow
pmopm8Mesrchannel16Entry = _Pmopm8Mesrchannel16Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 136, 1)
)
pmopm8Mesrchannel16Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel16Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel16Entry.setStatus("current")


class _Pmopm8Mesrchannel16Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel16Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel16Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel16Index_Object = MibTableColumn
pmopm8Mesrchannel16Index = _Pmopm8Mesrchannel16Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 136, 1, 1),
    _Pmopm8Mesrchannel16Index_Type()
)
pmopm8Mesrchannel16Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel16Index.setStatus("current")


class _Pmopm8Mesrchannel16Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel16Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel16Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel16Portn_Object = MibTableColumn
pmopm8Mesrchannel16Portn = _Pmopm8Mesrchannel16Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 136, 1, 2),
    _Pmopm8Mesrchannel16Portn_Type()
)
pmopm8Mesrchannel16Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel16Portn.setStatus("current")
_Pmopm8Mesrchannel17Table_Object = MibTable
pmopm8Mesrchannel17Table = _Pmopm8Mesrchannel17Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 144)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel17Table.setStatus("current")
_Pmopm8Mesrchannel17Entry_Object = MibTableRow
pmopm8Mesrchannel17Entry = _Pmopm8Mesrchannel17Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 144, 1)
)
pmopm8Mesrchannel17Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel17Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel17Entry.setStatus("current")


class _Pmopm8Mesrchannel17Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel17Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel17Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel17Index_Object = MibTableColumn
pmopm8Mesrchannel17Index = _Pmopm8Mesrchannel17Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 144, 1, 1),
    _Pmopm8Mesrchannel17Index_Type()
)
pmopm8Mesrchannel17Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel17Index.setStatus("current")


class _Pmopm8Mesrchannel17Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel17Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel17Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel17Portn_Object = MibTableColumn
pmopm8Mesrchannel17Portn = _Pmopm8Mesrchannel17Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 144, 1, 2),
    _Pmopm8Mesrchannel17Portn_Type()
)
pmopm8Mesrchannel17Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel17Portn.setStatus("current")
_Pmopm8Mesrchannel18Table_Object = MibTable
pmopm8Mesrchannel18Table = _Pmopm8Mesrchannel18Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel18Table.setStatus("current")
_Pmopm8Mesrchannel18Entry_Object = MibTableRow
pmopm8Mesrchannel18Entry = _Pmopm8Mesrchannel18Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 152, 1)
)
pmopm8Mesrchannel18Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel18Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel18Entry.setStatus("current")


class _Pmopm8Mesrchannel18Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel18Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel18Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel18Index_Object = MibTableColumn
pmopm8Mesrchannel18Index = _Pmopm8Mesrchannel18Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 152, 1, 1),
    _Pmopm8Mesrchannel18Index_Type()
)
pmopm8Mesrchannel18Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel18Index.setStatus("current")


class _Pmopm8Mesrchannel18Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel18Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel18Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel18Portn_Object = MibTableColumn
pmopm8Mesrchannel18Portn = _Pmopm8Mesrchannel18Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 152, 1, 2),
    _Pmopm8Mesrchannel18Portn_Type()
)
pmopm8Mesrchannel18Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel18Portn.setStatus("current")
_Pmopm8Mesrchannel19Table_Object = MibTable
pmopm8Mesrchannel19Table = _Pmopm8Mesrchannel19Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 160)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel19Table.setStatus("current")
_Pmopm8Mesrchannel19Entry_Object = MibTableRow
pmopm8Mesrchannel19Entry = _Pmopm8Mesrchannel19Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 160, 1)
)
pmopm8Mesrchannel19Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel19Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel19Entry.setStatus("current")


class _Pmopm8Mesrchannel19Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel19Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel19Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel19Index_Object = MibTableColumn
pmopm8Mesrchannel19Index = _Pmopm8Mesrchannel19Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 160, 1, 1),
    _Pmopm8Mesrchannel19Index_Type()
)
pmopm8Mesrchannel19Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel19Index.setStatus("current")


class _Pmopm8Mesrchannel19Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel19Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel19Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel19Portn_Object = MibTableColumn
pmopm8Mesrchannel19Portn = _Pmopm8Mesrchannel19Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 160, 1, 2),
    _Pmopm8Mesrchannel19Portn_Type()
)
pmopm8Mesrchannel19Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel19Portn.setStatus("current")
_Pmopm8Mesrchannel20Table_Object = MibTable
pmopm8Mesrchannel20Table = _Pmopm8Mesrchannel20Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 168)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel20Table.setStatus("current")
_Pmopm8Mesrchannel20Entry_Object = MibTableRow
pmopm8Mesrchannel20Entry = _Pmopm8Mesrchannel20Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 168, 1)
)
pmopm8Mesrchannel20Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel20Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel20Entry.setStatus("current")


class _Pmopm8Mesrchannel20Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel20Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel20Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel20Index_Object = MibTableColumn
pmopm8Mesrchannel20Index = _Pmopm8Mesrchannel20Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 168, 1, 1),
    _Pmopm8Mesrchannel20Index_Type()
)
pmopm8Mesrchannel20Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel20Index.setStatus("current")


class _Pmopm8Mesrchannel20Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel20Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel20Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel20Portn_Object = MibTableColumn
pmopm8Mesrchannel20Portn = _Pmopm8Mesrchannel20Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 168, 1, 2),
    _Pmopm8Mesrchannel20Portn_Type()
)
pmopm8Mesrchannel20Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel20Portn.setStatus("current")
_Pmopm8Mesrchannel21Table_Object = MibTable
pmopm8Mesrchannel21Table = _Pmopm8Mesrchannel21Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 176)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel21Table.setStatus("current")
_Pmopm8Mesrchannel21Entry_Object = MibTableRow
pmopm8Mesrchannel21Entry = _Pmopm8Mesrchannel21Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 176, 1)
)
pmopm8Mesrchannel21Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel21Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel21Entry.setStatus("current")


class _Pmopm8Mesrchannel21Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel21Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel21Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel21Index_Object = MibTableColumn
pmopm8Mesrchannel21Index = _Pmopm8Mesrchannel21Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 176, 1, 1),
    _Pmopm8Mesrchannel21Index_Type()
)
pmopm8Mesrchannel21Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel21Index.setStatus("current")


class _Pmopm8Mesrchannel21Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel21Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel21Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel21Portn_Object = MibTableColumn
pmopm8Mesrchannel21Portn = _Pmopm8Mesrchannel21Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 176, 1, 2),
    _Pmopm8Mesrchannel21Portn_Type()
)
pmopm8Mesrchannel21Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel21Portn.setStatus("current")
_Pmopm8Mesrchannel22Table_Object = MibTable
pmopm8Mesrchannel22Table = _Pmopm8Mesrchannel22Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 184)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel22Table.setStatus("current")
_Pmopm8Mesrchannel22Entry_Object = MibTableRow
pmopm8Mesrchannel22Entry = _Pmopm8Mesrchannel22Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 184, 1)
)
pmopm8Mesrchannel22Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel22Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel22Entry.setStatus("current")


class _Pmopm8Mesrchannel22Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel22Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel22Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel22Index_Object = MibTableColumn
pmopm8Mesrchannel22Index = _Pmopm8Mesrchannel22Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 184, 1, 1),
    _Pmopm8Mesrchannel22Index_Type()
)
pmopm8Mesrchannel22Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel22Index.setStatus("current")


class _Pmopm8Mesrchannel22Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel22Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel22Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel22Portn_Object = MibTableColumn
pmopm8Mesrchannel22Portn = _Pmopm8Mesrchannel22Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 184, 1, 2),
    _Pmopm8Mesrchannel22Portn_Type()
)
pmopm8Mesrchannel22Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel22Portn.setStatus("current")
_Pmopm8Mesrchannel23Table_Object = MibTable
pmopm8Mesrchannel23Table = _Pmopm8Mesrchannel23Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 192)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel23Table.setStatus("current")
_Pmopm8Mesrchannel23Entry_Object = MibTableRow
pmopm8Mesrchannel23Entry = _Pmopm8Mesrchannel23Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 192, 1)
)
pmopm8Mesrchannel23Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel23Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel23Entry.setStatus("current")


class _Pmopm8Mesrchannel23Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel23Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel23Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel23Index_Object = MibTableColumn
pmopm8Mesrchannel23Index = _Pmopm8Mesrchannel23Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 192, 1, 1),
    _Pmopm8Mesrchannel23Index_Type()
)
pmopm8Mesrchannel23Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel23Index.setStatus("current")


class _Pmopm8Mesrchannel23Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel23Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel23Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel23Portn_Object = MibTableColumn
pmopm8Mesrchannel23Portn = _Pmopm8Mesrchannel23Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 192, 1, 2),
    _Pmopm8Mesrchannel23Portn_Type()
)
pmopm8Mesrchannel23Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel23Portn.setStatus("current")
_Pmopm8Mesrchannel24Table_Object = MibTable
pmopm8Mesrchannel24Table = _Pmopm8Mesrchannel24Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 200)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel24Table.setStatus("current")
_Pmopm8Mesrchannel24Entry_Object = MibTableRow
pmopm8Mesrchannel24Entry = _Pmopm8Mesrchannel24Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 200, 1)
)
pmopm8Mesrchannel24Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel24Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel24Entry.setStatus("current")


class _Pmopm8Mesrchannel24Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel24Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel24Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel24Index_Object = MibTableColumn
pmopm8Mesrchannel24Index = _Pmopm8Mesrchannel24Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 200, 1, 1),
    _Pmopm8Mesrchannel24Index_Type()
)
pmopm8Mesrchannel24Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel24Index.setStatus("current")


class _Pmopm8Mesrchannel24Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel24Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel24Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel24Portn_Object = MibTableColumn
pmopm8Mesrchannel24Portn = _Pmopm8Mesrchannel24Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 200, 1, 2),
    _Pmopm8Mesrchannel24Portn_Type()
)
pmopm8Mesrchannel24Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel24Portn.setStatus("current")
_Pmopm8Mesrchannel25Table_Object = MibTable
pmopm8Mesrchannel25Table = _Pmopm8Mesrchannel25Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel25Table.setStatus("current")
_Pmopm8Mesrchannel25Entry_Object = MibTableRow
pmopm8Mesrchannel25Entry = _Pmopm8Mesrchannel25Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 208, 1)
)
pmopm8Mesrchannel25Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel25Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel25Entry.setStatus("current")


class _Pmopm8Mesrchannel25Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel25Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel25Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel25Index_Object = MibTableColumn
pmopm8Mesrchannel25Index = _Pmopm8Mesrchannel25Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 208, 1, 1),
    _Pmopm8Mesrchannel25Index_Type()
)
pmopm8Mesrchannel25Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel25Index.setStatus("current")


class _Pmopm8Mesrchannel25Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel25Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel25Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel25Portn_Object = MibTableColumn
pmopm8Mesrchannel25Portn = _Pmopm8Mesrchannel25Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 208, 1, 2),
    _Pmopm8Mesrchannel25Portn_Type()
)
pmopm8Mesrchannel25Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel25Portn.setStatus("current")
_Pmopm8Mesrchannel26Table_Object = MibTable
pmopm8Mesrchannel26Table = _Pmopm8Mesrchannel26Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 216)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel26Table.setStatus("current")
_Pmopm8Mesrchannel26Entry_Object = MibTableRow
pmopm8Mesrchannel26Entry = _Pmopm8Mesrchannel26Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 216, 1)
)
pmopm8Mesrchannel26Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel26Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel26Entry.setStatus("current")


class _Pmopm8Mesrchannel26Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel26Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel26Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel26Index_Object = MibTableColumn
pmopm8Mesrchannel26Index = _Pmopm8Mesrchannel26Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 216, 1, 1),
    _Pmopm8Mesrchannel26Index_Type()
)
pmopm8Mesrchannel26Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel26Index.setStatus("current")


class _Pmopm8Mesrchannel26Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel26Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel26Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel26Portn_Object = MibTableColumn
pmopm8Mesrchannel26Portn = _Pmopm8Mesrchannel26Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 216, 1, 2),
    _Pmopm8Mesrchannel26Portn_Type()
)
pmopm8Mesrchannel26Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel26Portn.setStatus("current")
_Pmopm8Mesrchannel27Table_Object = MibTable
pmopm8Mesrchannel27Table = _Pmopm8Mesrchannel27Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel27Table.setStatus("current")
_Pmopm8Mesrchannel27Entry_Object = MibTableRow
pmopm8Mesrchannel27Entry = _Pmopm8Mesrchannel27Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 224, 1)
)
pmopm8Mesrchannel27Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel27Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel27Entry.setStatus("current")


class _Pmopm8Mesrchannel27Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel27Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel27Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel27Index_Object = MibTableColumn
pmopm8Mesrchannel27Index = _Pmopm8Mesrchannel27Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 224, 1, 1),
    _Pmopm8Mesrchannel27Index_Type()
)
pmopm8Mesrchannel27Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel27Index.setStatus("current")


class _Pmopm8Mesrchannel27Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel27Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel27Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel27Portn_Object = MibTableColumn
pmopm8Mesrchannel27Portn = _Pmopm8Mesrchannel27Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 224, 1, 2),
    _Pmopm8Mesrchannel27Portn_Type()
)
pmopm8Mesrchannel27Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel27Portn.setStatus("current")
_Pmopm8Mesrchannel28Table_Object = MibTable
pmopm8Mesrchannel28Table = _Pmopm8Mesrchannel28Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 232)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel28Table.setStatus("current")
_Pmopm8Mesrchannel28Entry_Object = MibTableRow
pmopm8Mesrchannel28Entry = _Pmopm8Mesrchannel28Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 232, 1)
)
pmopm8Mesrchannel28Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel28Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel28Entry.setStatus("current")


class _Pmopm8Mesrchannel28Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel28Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel28Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel28Index_Object = MibTableColumn
pmopm8Mesrchannel28Index = _Pmopm8Mesrchannel28Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 232, 1, 1),
    _Pmopm8Mesrchannel28Index_Type()
)
pmopm8Mesrchannel28Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel28Index.setStatus("current")


class _Pmopm8Mesrchannel28Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel28Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel28Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel28Portn_Object = MibTableColumn
pmopm8Mesrchannel28Portn = _Pmopm8Mesrchannel28Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 232, 1, 2),
    _Pmopm8Mesrchannel28Portn_Type()
)
pmopm8Mesrchannel28Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel28Portn.setStatus("current")
_Pmopm8Mesrchannel29Table_Object = MibTable
pmopm8Mesrchannel29Table = _Pmopm8Mesrchannel29Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 240)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel29Table.setStatus("current")
_Pmopm8Mesrchannel29Entry_Object = MibTableRow
pmopm8Mesrchannel29Entry = _Pmopm8Mesrchannel29Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 240, 1)
)
pmopm8Mesrchannel29Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel29Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel29Entry.setStatus("current")


class _Pmopm8Mesrchannel29Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel29Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel29Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel29Index_Object = MibTableColumn
pmopm8Mesrchannel29Index = _Pmopm8Mesrchannel29Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 240, 1, 1),
    _Pmopm8Mesrchannel29Index_Type()
)
pmopm8Mesrchannel29Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel29Index.setStatus("current")


class _Pmopm8Mesrchannel29Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel29Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel29Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel29Portn_Object = MibTableColumn
pmopm8Mesrchannel29Portn = _Pmopm8Mesrchannel29Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 240, 1, 2),
    _Pmopm8Mesrchannel29Portn_Type()
)
pmopm8Mesrchannel29Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel29Portn.setStatus("current")
_Pmopm8Mesrchannel30Table_Object = MibTable
pmopm8Mesrchannel30Table = _Pmopm8Mesrchannel30Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 248)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel30Table.setStatus("current")
_Pmopm8Mesrchannel30Entry_Object = MibTableRow
pmopm8Mesrchannel30Entry = _Pmopm8Mesrchannel30Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 248, 1)
)
pmopm8Mesrchannel30Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel30Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel30Entry.setStatus("current")


class _Pmopm8Mesrchannel30Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel30Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel30Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel30Index_Object = MibTableColumn
pmopm8Mesrchannel30Index = _Pmopm8Mesrchannel30Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 248, 1, 1),
    _Pmopm8Mesrchannel30Index_Type()
)
pmopm8Mesrchannel30Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel30Index.setStatus("current")


class _Pmopm8Mesrchannel30Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel30Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel30Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel30Portn_Object = MibTableColumn
pmopm8Mesrchannel30Portn = _Pmopm8Mesrchannel30Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 248, 1, 2),
    _Pmopm8Mesrchannel30Portn_Type()
)
pmopm8Mesrchannel30Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel30Portn.setStatus("current")
_Pmopm8Mesrchannel31Table_Object = MibTable
pmopm8Mesrchannel31Table = _Pmopm8Mesrchannel31Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 256)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel31Table.setStatus("current")
_Pmopm8Mesrchannel31Entry_Object = MibTableRow
pmopm8Mesrchannel31Entry = _Pmopm8Mesrchannel31Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 256, 1)
)
pmopm8Mesrchannel31Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel31Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel31Entry.setStatus("current")


class _Pmopm8Mesrchannel31Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel31Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel31Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel31Index_Object = MibTableColumn
pmopm8Mesrchannel31Index = _Pmopm8Mesrchannel31Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 256, 1, 1),
    _Pmopm8Mesrchannel31Index_Type()
)
pmopm8Mesrchannel31Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel31Index.setStatus("current")


class _Pmopm8Mesrchannel31Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel31Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel31Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel31Portn_Object = MibTableColumn
pmopm8Mesrchannel31Portn = _Pmopm8Mesrchannel31Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 256, 1, 2),
    _Pmopm8Mesrchannel31Portn_Type()
)
pmopm8Mesrchannel31Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel31Portn.setStatus("current")
_Pmopm8Mesrchannel32Table_Object = MibTable
pmopm8Mesrchannel32Table = _Pmopm8Mesrchannel32Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 264)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel32Table.setStatus("current")
_Pmopm8Mesrchannel32Entry_Object = MibTableRow
pmopm8Mesrchannel32Entry = _Pmopm8Mesrchannel32Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 264, 1)
)
pmopm8Mesrchannel32Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel32Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel32Entry.setStatus("current")


class _Pmopm8Mesrchannel32Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel32Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel32Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel32Index_Object = MibTableColumn
pmopm8Mesrchannel32Index = _Pmopm8Mesrchannel32Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 264, 1, 1),
    _Pmopm8Mesrchannel32Index_Type()
)
pmopm8Mesrchannel32Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel32Index.setStatus("current")


class _Pmopm8Mesrchannel32Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel32Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel32Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel32Portn_Object = MibTableColumn
pmopm8Mesrchannel32Portn = _Pmopm8Mesrchannel32Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 264, 1, 2),
    _Pmopm8Mesrchannel32Portn_Type()
)
pmopm8Mesrchannel32Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel32Portn.setStatus("current")
_Pmopm8Mesrchannel33Table_Object = MibTable
pmopm8Mesrchannel33Table = _Pmopm8Mesrchannel33Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 272)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel33Table.setStatus("current")
_Pmopm8Mesrchannel33Entry_Object = MibTableRow
pmopm8Mesrchannel33Entry = _Pmopm8Mesrchannel33Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 272, 1)
)
pmopm8Mesrchannel33Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel33Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel33Entry.setStatus("current")


class _Pmopm8Mesrchannel33Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel33Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel33Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel33Index_Object = MibTableColumn
pmopm8Mesrchannel33Index = _Pmopm8Mesrchannel33Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 272, 1, 1),
    _Pmopm8Mesrchannel33Index_Type()
)
pmopm8Mesrchannel33Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel33Index.setStatus("current")


class _Pmopm8Mesrchannel33Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel33Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel33Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel33Portn_Object = MibTableColumn
pmopm8Mesrchannel33Portn = _Pmopm8Mesrchannel33Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 272, 1, 2),
    _Pmopm8Mesrchannel33Portn_Type()
)
pmopm8Mesrchannel33Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel33Portn.setStatus("current")
_Pmopm8Mesrchannel34Table_Object = MibTable
pmopm8Mesrchannel34Table = _Pmopm8Mesrchannel34Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 280)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel34Table.setStatus("current")
_Pmopm8Mesrchannel34Entry_Object = MibTableRow
pmopm8Mesrchannel34Entry = _Pmopm8Mesrchannel34Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 280, 1)
)
pmopm8Mesrchannel34Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel34Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel34Entry.setStatus("current")


class _Pmopm8Mesrchannel34Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel34Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel34Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel34Index_Object = MibTableColumn
pmopm8Mesrchannel34Index = _Pmopm8Mesrchannel34Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 280, 1, 1),
    _Pmopm8Mesrchannel34Index_Type()
)
pmopm8Mesrchannel34Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel34Index.setStatus("current")


class _Pmopm8Mesrchannel34Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel34Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel34Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel34Portn_Object = MibTableColumn
pmopm8Mesrchannel34Portn = _Pmopm8Mesrchannel34Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 280, 1, 2),
    _Pmopm8Mesrchannel34Portn_Type()
)
pmopm8Mesrchannel34Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel34Portn.setStatus("current")
_Pmopm8Mesrchannel35Table_Object = MibTable
pmopm8Mesrchannel35Table = _Pmopm8Mesrchannel35Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 288)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel35Table.setStatus("current")
_Pmopm8Mesrchannel35Entry_Object = MibTableRow
pmopm8Mesrchannel35Entry = _Pmopm8Mesrchannel35Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 288, 1)
)
pmopm8Mesrchannel35Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel35Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel35Entry.setStatus("current")


class _Pmopm8Mesrchannel35Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel35Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel35Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel35Index_Object = MibTableColumn
pmopm8Mesrchannel35Index = _Pmopm8Mesrchannel35Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 288, 1, 1),
    _Pmopm8Mesrchannel35Index_Type()
)
pmopm8Mesrchannel35Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel35Index.setStatus("current")


class _Pmopm8Mesrchannel35Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel35Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel35Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel35Portn_Object = MibTableColumn
pmopm8Mesrchannel35Portn = _Pmopm8Mesrchannel35Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 288, 1, 2),
    _Pmopm8Mesrchannel35Portn_Type()
)
pmopm8Mesrchannel35Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel35Portn.setStatus("current")
_Pmopm8Mesrchannel36Table_Object = MibTable
pmopm8Mesrchannel36Table = _Pmopm8Mesrchannel36Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 296)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel36Table.setStatus("current")
_Pmopm8Mesrchannel36Entry_Object = MibTableRow
pmopm8Mesrchannel36Entry = _Pmopm8Mesrchannel36Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 296, 1)
)
pmopm8Mesrchannel36Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel36Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel36Entry.setStatus("current")


class _Pmopm8Mesrchannel36Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel36Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel36Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel36Index_Object = MibTableColumn
pmopm8Mesrchannel36Index = _Pmopm8Mesrchannel36Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 296, 1, 1),
    _Pmopm8Mesrchannel36Index_Type()
)
pmopm8Mesrchannel36Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel36Index.setStatus("current")


class _Pmopm8Mesrchannel36Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel36Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel36Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel36Portn_Object = MibTableColumn
pmopm8Mesrchannel36Portn = _Pmopm8Mesrchannel36Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 296, 1, 2),
    _Pmopm8Mesrchannel36Portn_Type()
)
pmopm8Mesrchannel36Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel36Portn.setStatus("current")
_Pmopm8Mesrchannel37Table_Object = MibTable
pmopm8Mesrchannel37Table = _Pmopm8Mesrchannel37Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 304)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel37Table.setStatus("current")
_Pmopm8Mesrchannel37Entry_Object = MibTableRow
pmopm8Mesrchannel37Entry = _Pmopm8Mesrchannel37Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 304, 1)
)
pmopm8Mesrchannel37Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel37Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel37Entry.setStatus("current")


class _Pmopm8Mesrchannel37Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel37Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel37Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel37Index_Object = MibTableColumn
pmopm8Mesrchannel37Index = _Pmopm8Mesrchannel37Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 304, 1, 1),
    _Pmopm8Mesrchannel37Index_Type()
)
pmopm8Mesrchannel37Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel37Index.setStatus("current")


class _Pmopm8Mesrchannel37Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel37Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel37Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel37Portn_Object = MibTableColumn
pmopm8Mesrchannel37Portn = _Pmopm8Mesrchannel37Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 304, 1, 2),
    _Pmopm8Mesrchannel37Portn_Type()
)
pmopm8Mesrchannel37Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel37Portn.setStatus("current")
_Pmopm8Mesrchannel38Table_Object = MibTable
pmopm8Mesrchannel38Table = _Pmopm8Mesrchannel38Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 312)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel38Table.setStatus("current")
_Pmopm8Mesrchannel38Entry_Object = MibTableRow
pmopm8Mesrchannel38Entry = _Pmopm8Mesrchannel38Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 312, 1)
)
pmopm8Mesrchannel38Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel38Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel38Entry.setStatus("current")


class _Pmopm8Mesrchannel38Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel38Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel38Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel38Index_Object = MibTableColumn
pmopm8Mesrchannel38Index = _Pmopm8Mesrchannel38Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 312, 1, 1),
    _Pmopm8Mesrchannel38Index_Type()
)
pmopm8Mesrchannel38Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel38Index.setStatus("current")


class _Pmopm8Mesrchannel38Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel38Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel38Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel38Portn_Object = MibTableColumn
pmopm8Mesrchannel38Portn = _Pmopm8Mesrchannel38Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 312, 1, 2),
    _Pmopm8Mesrchannel38Portn_Type()
)
pmopm8Mesrchannel38Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel38Portn.setStatus("current")
_Pmopm8Mesrchannel39Table_Object = MibTable
pmopm8Mesrchannel39Table = _Pmopm8Mesrchannel39Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 320)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel39Table.setStatus("current")
_Pmopm8Mesrchannel39Entry_Object = MibTableRow
pmopm8Mesrchannel39Entry = _Pmopm8Mesrchannel39Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 320, 1)
)
pmopm8Mesrchannel39Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel39Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel39Entry.setStatus("current")


class _Pmopm8Mesrchannel39Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel39Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel39Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel39Index_Object = MibTableColumn
pmopm8Mesrchannel39Index = _Pmopm8Mesrchannel39Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 320, 1, 1),
    _Pmopm8Mesrchannel39Index_Type()
)
pmopm8Mesrchannel39Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel39Index.setStatus("current")


class _Pmopm8Mesrchannel39Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel39Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel39Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel39Portn_Object = MibTableColumn
pmopm8Mesrchannel39Portn = _Pmopm8Mesrchannel39Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 320, 1, 2),
    _Pmopm8Mesrchannel39Portn_Type()
)
pmopm8Mesrchannel39Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel39Portn.setStatus("current")
_Pmopm8Mesrchannel40Table_Object = MibTable
pmopm8Mesrchannel40Table = _Pmopm8Mesrchannel40Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 328)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel40Table.setStatus("current")
_Pmopm8Mesrchannel40Entry_Object = MibTableRow
pmopm8Mesrchannel40Entry = _Pmopm8Mesrchannel40Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 328, 1)
)
pmopm8Mesrchannel40Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel40Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel40Entry.setStatus("current")


class _Pmopm8Mesrchannel40Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel40Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel40Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel40Index_Object = MibTableColumn
pmopm8Mesrchannel40Index = _Pmopm8Mesrchannel40Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 328, 1, 1),
    _Pmopm8Mesrchannel40Index_Type()
)
pmopm8Mesrchannel40Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel40Index.setStatus("current")


class _Pmopm8Mesrchannel40Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel40Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel40Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel40Portn_Object = MibTableColumn
pmopm8Mesrchannel40Portn = _Pmopm8Mesrchannel40Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 328, 1, 2),
    _Pmopm8Mesrchannel40Portn_Type()
)
pmopm8Mesrchannel40Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel40Portn.setStatus("current")
_Pmopm8Mesrchannel41Table_Object = MibTable
pmopm8Mesrchannel41Table = _Pmopm8Mesrchannel41Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 336)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel41Table.setStatus("current")
_Pmopm8Mesrchannel41Entry_Object = MibTableRow
pmopm8Mesrchannel41Entry = _Pmopm8Mesrchannel41Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 336, 1)
)
pmopm8Mesrchannel41Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel41Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel41Entry.setStatus("current")


class _Pmopm8Mesrchannel41Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel41Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel41Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel41Index_Object = MibTableColumn
pmopm8Mesrchannel41Index = _Pmopm8Mesrchannel41Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 336, 1, 1),
    _Pmopm8Mesrchannel41Index_Type()
)
pmopm8Mesrchannel41Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel41Index.setStatus("current")


class _Pmopm8Mesrchannel41Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel41Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel41Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel41Portn_Object = MibTableColumn
pmopm8Mesrchannel41Portn = _Pmopm8Mesrchannel41Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 336, 1, 2),
    _Pmopm8Mesrchannel41Portn_Type()
)
pmopm8Mesrchannel41Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel41Portn.setStatus("current")
_Pmopm8Mesrchannel42Table_Object = MibTable
pmopm8Mesrchannel42Table = _Pmopm8Mesrchannel42Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 344)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel42Table.setStatus("current")
_Pmopm8Mesrchannel42Entry_Object = MibTableRow
pmopm8Mesrchannel42Entry = _Pmopm8Mesrchannel42Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 344, 1)
)
pmopm8Mesrchannel42Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel42Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel42Entry.setStatus("current")


class _Pmopm8Mesrchannel42Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel42Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel42Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel42Index_Object = MibTableColumn
pmopm8Mesrchannel42Index = _Pmopm8Mesrchannel42Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 344, 1, 1),
    _Pmopm8Mesrchannel42Index_Type()
)
pmopm8Mesrchannel42Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel42Index.setStatus("current")


class _Pmopm8Mesrchannel42Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel42Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel42Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel42Portn_Object = MibTableColumn
pmopm8Mesrchannel42Portn = _Pmopm8Mesrchannel42Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 344, 1, 2),
    _Pmopm8Mesrchannel42Portn_Type()
)
pmopm8Mesrchannel42Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel42Portn.setStatus("current")
_Pmopm8Mesrchannel43Table_Object = MibTable
pmopm8Mesrchannel43Table = _Pmopm8Mesrchannel43Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 352)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel43Table.setStatus("current")
_Pmopm8Mesrchannel43Entry_Object = MibTableRow
pmopm8Mesrchannel43Entry = _Pmopm8Mesrchannel43Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 352, 1)
)
pmopm8Mesrchannel43Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel43Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel43Entry.setStatus("current")


class _Pmopm8Mesrchannel43Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel43Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel43Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel43Index_Object = MibTableColumn
pmopm8Mesrchannel43Index = _Pmopm8Mesrchannel43Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 352, 1, 1),
    _Pmopm8Mesrchannel43Index_Type()
)
pmopm8Mesrchannel43Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel43Index.setStatus("current")


class _Pmopm8Mesrchannel43Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel43Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel43Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel43Portn_Object = MibTableColumn
pmopm8Mesrchannel43Portn = _Pmopm8Mesrchannel43Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 352, 1, 2),
    _Pmopm8Mesrchannel43Portn_Type()
)
pmopm8Mesrchannel43Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel43Portn.setStatus("current")
_Pmopm8Mesrchannel44Table_Object = MibTable
pmopm8Mesrchannel44Table = _Pmopm8Mesrchannel44Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 360)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel44Table.setStatus("current")
_Pmopm8Mesrchannel44Entry_Object = MibTableRow
pmopm8Mesrchannel44Entry = _Pmopm8Mesrchannel44Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 360, 1)
)
pmopm8Mesrchannel44Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel44Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel44Entry.setStatus("current")


class _Pmopm8Mesrchannel44Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel44Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel44Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel44Index_Object = MibTableColumn
pmopm8Mesrchannel44Index = _Pmopm8Mesrchannel44Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 360, 1, 1),
    _Pmopm8Mesrchannel44Index_Type()
)
pmopm8Mesrchannel44Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel44Index.setStatus("current")


class _Pmopm8Mesrchannel44Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel44Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel44Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel44Portn_Object = MibTableColumn
pmopm8Mesrchannel44Portn = _Pmopm8Mesrchannel44Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 360, 1, 2),
    _Pmopm8Mesrchannel44Portn_Type()
)
pmopm8Mesrchannel44Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel44Portn.setStatus("current")
_Pmopm8Mesrchannel45Table_Object = MibTable
pmopm8Mesrchannel45Table = _Pmopm8Mesrchannel45Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 368)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel45Table.setStatus("current")
_Pmopm8Mesrchannel45Entry_Object = MibTableRow
pmopm8Mesrchannel45Entry = _Pmopm8Mesrchannel45Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 368, 1)
)
pmopm8Mesrchannel45Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel45Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel45Entry.setStatus("current")


class _Pmopm8Mesrchannel45Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel45Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel45Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel45Index_Object = MibTableColumn
pmopm8Mesrchannel45Index = _Pmopm8Mesrchannel45Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 368, 1, 1),
    _Pmopm8Mesrchannel45Index_Type()
)
pmopm8Mesrchannel45Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel45Index.setStatus("current")


class _Pmopm8Mesrchannel45Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel45Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel45Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel45Portn_Object = MibTableColumn
pmopm8Mesrchannel45Portn = _Pmopm8Mesrchannel45Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 368, 1, 2),
    _Pmopm8Mesrchannel45Portn_Type()
)
pmopm8Mesrchannel45Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel45Portn.setStatus("current")
_Pmopm8Mesrchannel46Table_Object = MibTable
pmopm8Mesrchannel46Table = _Pmopm8Mesrchannel46Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 376)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel46Table.setStatus("current")
_Pmopm8Mesrchannel46Entry_Object = MibTableRow
pmopm8Mesrchannel46Entry = _Pmopm8Mesrchannel46Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 376, 1)
)
pmopm8Mesrchannel46Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel46Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel46Entry.setStatus("current")


class _Pmopm8Mesrchannel46Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel46Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel46Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel46Index_Object = MibTableColumn
pmopm8Mesrchannel46Index = _Pmopm8Mesrchannel46Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 376, 1, 1),
    _Pmopm8Mesrchannel46Index_Type()
)
pmopm8Mesrchannel46Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel46Index.setStatus("current")


class _Pmopm8Mesrchannel46Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel46Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel46Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel46Portn_Object = MibTableColumn
pmopm8Mesrchannel46Portn = _Pmopm8Mesrchannel46Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 376, 1, 2),
    _Pmopm8Mesrchannel46Portn_Type()
)
pmopm8Mesrchannel46Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel46Portn.setStatus("current")
_Pmopm8Mesrchannel47Table_Object = MibTable
pmopm8Mesrchannel47Table = _Pmopm8Mesrchannel47Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 384)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel47Table.setStatus("current")
_Pmopm8Mesrchannel47Entry_Object = MibTableRow
pmopm8Mesrchannel47Entry = _Pmopm8Mesrchannel47Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 384, 1)
)
pmopm8Mesrchannel47Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel47Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel47Entry.setStatus("current")


class _Pmopm8Mesrchannel47Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel47Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel47Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel47Index_Object = MibTableColumn
pmopm8Mesrchannel47Index = _Pmopm8Mesrchannel47Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 384, 1, 1),
    _Pmopm8Mesrchannel47Index_Type()
)
pmopm8Mesrchannel47Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel47Index.setStatus("current")


class _Pmopm8Mesrchannel47Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel47Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel47Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel47Portn_Object = MibTableColumn
pmopm8Mesrchannel47Portn = _Pmopm8Mesrchannel47Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 384, 1, 2),
    _Pmopm8Mesrchannel47Portn_Type()
)
pmopm8Mesrchannel47Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel47Portn.setStatus("current")
_Pmopm8Mesrchannel48Table_Object = MibTable
pmopm8Mesrchannel48Table = _Pmopm8Mesrchannel48Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 392)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel48Table.setStatus("current")
_Pmopm8Mesrchannel48Entry_Object = MibTableRow
pmopm8Mesrchannel48Entry = _Pmopm8Mesrchannel48Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 392, 1)
)
pmopm8Mesrchannel48Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel48Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel48Entry.setStatus("current")


class _Pmopm8Mesrchannel48Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel48Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel48Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel48Index_Object = MibTableColumn
pmopm8Mesrchannel48Index = _Pmopm8Mesrchannel48Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 392, 1, 1),
    _Pmopm8Mesrchannel48Index_Type()
)
pmopm8Mesrchannel48Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel48Index.setStatus("current")


class _Pmopm8Mesrchannel48Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel48Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel48Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel48Portn_Object = MibTableColumn
pmopm8Mesrchannel48Portn = _Pmopm8Mesrchannel48Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 392, 1, 2),
    _Pmopm8Mesrchannel48Portn_Type()
)
pmopm8Mesrchannel48Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel48Portn.setStatus("current")
_Pmopm8Mesrchannel49Table_Object = MibTable
pmopm8Mesrchannel49Table = _Pmopm8Mesrchannel49Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 400)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel49Table.setStatus("current")
_Pmopm8Mesrchannel49Entry_Object = MibTableRow
pmopm8Mesrchannel49Entry = _Pmopm8Mesrchannel49Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 400, 1)
)
pmopm8Mesrchannel49Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel49Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel49Entry.setStatus("current")


class _Pmopm8Mesrchannel49Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel49Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel49Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel49Index_Object = MibTableColumn
pmopm8Mesrchannel49Index = _Pmopm8Mesrchannel49Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 400, 1, 1),
    _Pmopm8Mesrchannel49Index_Type()
)
pmopm8Mesrchannel49Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel49Index.setStatus("current")


class _Pmopm8Mesrchannel49Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel49Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel49Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel49Portn_Object = MibTableColumn
pmopm8Mesrchannel49Portn = _Pmopm8Mesrchannel49Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 400, 1, 2),
    _Pmopm8Mesrchannel49Portn_Type()
)
pmopm8Mesrchannel49Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel49Portn.setStatus("current")
_Pmopm8Mesrchannel50Table_Object = MibTable
pmopm8Mesrchannel50Table = _Pmopm8Mesrchannel50Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 408)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel50Table.setStatus("current")
_Pmopm8Mesrchannel50Entry_Object = MibTableRow
pmopm8Mesrchannel50Entry = _Pmopm8Mesrchannel50Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 408, 1)
)
pmopm8Mesrchannel50Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel50Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel50Entry.setStatus("current")


class _Pmopm8Mesrchannel50Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel50Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel50Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel50Index_Object = MibTableColumn
pmopm8Mesrchannel50Index = _Pmopm8Mesrchannel50Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 408, 1, 1),
    _Pmopm8Mesrchannel50Index_Type()
)
pmopm8Mesrchannel50Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel50Index.setStatus("current")


class _Pmopm8Mesrchannel50Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel50Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel50Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel50Portn_Object = MibTableColumn
pmopm8Mesrchannel50Portn = _Pmopm8Mesrchannel50Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 408, 1, 2),
    _Pmopm8Mesrchannel50Portn_Type()
)
pmopm8Mesrchannel50Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel50Portn.setStatus("current")
_Pmopm8Mesrchannel51Table_Object = MibTable
pmopm8Mesrchannel51Table = _Pmopm8Mesrchannel51Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 416)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel51Table.setStatus("current")
_Pmopm8Mesrchannel51Entry_Object = MibTableRow
pmopm8Mesrchannel51Entry = _Pmopm8Mesrchannel51Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 416, 1)
)
pmopm8Mesrchannel51Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel51Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel51Entry.setStatus("current")


class _Pmopm8Mesrchannel51Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel51Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel51Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel51Index_Object = MibTableColumn
pmopm8Mesrchannel51Index = _Pmopm8Mesrchannel51Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 416, 1, 1),
    _Pmopm8Mesrchannel51Index_Type()
)
pmopm8Mesrchannel51Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel51Index.setStatus("current")


class _Pmopm8Mesrchannel51Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel51Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel51Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel51Portn_Object = MibTableColumn
pmopm8Mesrchannel51Portn = _Pmopm8Mesrchannel51Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 416, 1, 2),
    _Pmopm8Mesrchannel51Portn_Type()
)
pmopm8Mesrchannel51Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel51Portn.setStatus("current")
_Pmopm8Mesrchannel52Table_Object = MibTable
pmopm8Mesrchannel52Table = _Pmopm8Mesrchannel52Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 424)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel52Table.setStatus("current")
_Pmopm8Mesrchannel52Entry_Object = MibTableRow
pmopm8Mesrchannel52Entry = _Pmopm8Mesrchannel52Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 424, 1)
)
pmopm8Mesrchannel52Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel52Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel52Entry.setStatus("current")


class _Pmopm8Mesrchannel52Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel52Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel52Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel52Index_Object = MibTableColumn
pmopm8Mesrchannel52Index = _Pmopm8Mesrchannel52Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 424, 1, 1),
    _Pmopm8Mesrchannel52Index_Type()
)
pmopm8Mesrchannel52Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel52Index.setStatus("current")


class _Pmopm8Mesrchannel52Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel52Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel52Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel52Portn_Object = MibTableColumn
pmopm8Mesrchannel52Portn = _Pmopm8Mesrchannel52Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 424, 1, 2),
    _Pmopm8Mesrchannel52Portn_Type()
)
pmopm8Mesrchannel52Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel52Portn.setStatus("current")
_Pmopm8Mesrchannel53Table_Object = MibTable
pmopm8Mesrchannel53Table = _Pmopm8Mesrchannel53Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 432)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel53Table.setStatus("current")
_Pmopm8Mesrchannel53Entry_Object = MibTableRow
pmopm8Mesrchannel53Entry = _Pmopm8Mesrchannel53Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 432, 1)
)
pmopm8Mesrchannel53Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel53Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel53Entry.setStatus("current")


class _Pmopm8Mesrchannel53Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel53Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel53Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel53Index_Object = MibTableColumn
pmopm8Mesrchannel53Index = _Pmopm8Mesrchannel53Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 432, 1, 1),
    _Pmopm8Mesrchannel53Index_Type()
)
pmopm8Mesrchannel53Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel53Index.setStatus("current")


class _Pmopm8Mesrchannel53Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel53Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel53Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel53Portn_Object = MibTableColumn
pmopm8Mesrchannel53Portn = _Pmopm8Mesrchannel53Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 432, 1, 2),
    _Pmopm8Mesrchannel53Portn_Type()
)
pmopm8Mesrchannel53Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel53Portn.setStatus("current")
_Pmopm8Mesrchannel54Table_Object = MibTable
pmopm8Mesrchannel54Table = _Pmopm8Mesrchannel54Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 440)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel54Table.setStatus("current")
_Pmopm8Mesrchannel54Entry_Object = MibTableRow
pmopm8Mesrchannel54Entry = _Pmopm8Mesrchannel54Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 440, 1)
)
pmopm8Mesrchannel54Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel54Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel54Entry.setStatus("current")


class _Pmopm8Mesrchannel54Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel54Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel54Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel54Index_Object = MibTableColumn
pmopm8Mesrchannel54Index = _Pmopm8Mesrchannel54Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 440, 1, 1),
    _Pmopm8Mesrchannel54Index_Type()
)
pmopm8Mesrchannel54Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel54Index.setStatus("current")


class _Pmopm8Mesrchannel54Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel54Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel54Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel54Portn_Object = MibTableColumn
pmopm8Mesrchannel54Portn = _Pmopm8Mesrchannel54Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 440, 1, 2),
    _Pmopm8Mesrchannel54Portn_Type()
)
pmopm8Mesrchannel54Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel54Portn.setStatus("current")
_Pmopm8Mesrchannel55Table_Object = MibTable
pmopm8Mesrchannel55Table = _Pmopm8Mesrchannel55Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 448)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel55Table.setStatus("current")
_Pmopm8Mesrchannel55Entry_Object = MibTableRow
pmopm8Mesrchannel55Entry = _Pmopm8Mesrchannel55Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 448, 1)
)
pmopm8Mesrchannel55Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel55Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel55Entry.setStatus("current")


class _Pmopm8Mesrchannel55Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel55Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel55Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel55Index_Object = MibTableColumn
pmopm8Mesrchannel55Index = _Pmopm8Mesrchannel55Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 448, 1, 1),
    _Pmopm8Mesrchannel55Index_Type()
)
pmopm8Mesrchannel55Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel55Index.setStatus("current")


class _Pmopm8Mesrchannel55Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel55Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel55Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel55Portn_Object = MibTableColumn
pmopm8Mesrchannel55Portn = _Pmopm8Mesrchannel55Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 448, 1, 2),
    _Pmopm8Mesrchannel55Portn_Type()
)
pmopm8Mesrchannel55Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel55Portn.setStatus("current")
_Pmopm8Mesrchannel56Table_Object = MibTable
pmopm8Mesrchannel56Table = _Pmopm8Mesrchannel56Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 456)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel56Table.setStatus("current")
_Pmopm8Mesrchannel56Entry_Object = MibTableRow
pmopm8Mesrchannel56Entry = _Pmopm8Mesrchannel56Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 456, 1)
)
pmopm8Mesrchannel56Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel56Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel56Entry.setStatus("current")


class _Pmopm8Mesrchannel56Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel56Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel56Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel56Index_Object = MibTableColumn
pmopm8Mesrchannel56Index = _Pmopm8Mesrchannel56Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 456, 1, 1),
    _Pmopm8Mesrchannel56Index_Type()
)
pmopm8Mesrchannel56Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel56Index.setStatus("current")


class _Pmopm8Mesrchannel56Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel56Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel56Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel56Portn_Object = MibTableColumn
pmopm8Mesrchannel56Portn = _Pmopm8Mesrchannel56Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 456, 1, 2),
    _Pmopm8Mesrchannel56Portn_Type()
)
pmopm8Mesrchannel56Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel56Portn.setStatus("current")
_Pmopm8Mesrchannel57Table_Object = MibTable
pmopm8Mesrchannel57Table = _Pmopm8Mesrchannel57Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 464)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel57Table.setStatus("current")
_Pmopm8Mesrchannel57Entry_Object = MibTableRow
pmopm8Mesrchannel57Entry = _Pmopm8Mesrchannel57Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 464, 1)
)
pmopm8Mesrchannel57Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel57Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel57Entry.setStatus("current")


class _Pmopm8Mesrchannel57Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel57Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel57Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel57Index_Object = MibTableColumn
pmopm8Mesrchannel57Index = _Pmopm8Mesrchannel57Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 464, 1, 1),
    _Pmopm8Mesrchannel57Index_Type()
)
pmopm8Mesrchannel57Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel57Index.setStatus("current")


class _Pmopm8Mesrchannel57Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel57Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel57Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel57Portn_Object = MibTableColumn
pmopm8Mesrchannel57Portn = _Pmopm8Mesrchannel57Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 464, 1, 2),
    _Pmopm8Mesrchannel57Portn_Type()
)
pmopm8Mesrchannel57Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel57Portn.setStatus("current")
_Pmopm8Mesrchannel58Table_Object = MibTable
pmopm8Mesrchannel58Table = _Pmopm8Mesrchannel58Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 472)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel58Table.setStatus("current")
_Pmopm8Mesrchannel58Entry_Object = MibTableRow
pmopm8Mesrchannel58Entry = _Pmopm8Mesrchannel58Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 472, 1)
)
pmopm8Mesrchannel58Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel58Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel58Entry.setStatus("current")


class _Pmopm8Mesrchannel58Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel58Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel58Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel58Index_Object = MibTableColumn
pmopm8Mesrchannel58Index = _Pmopm8Mesrchannel58Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 472, 1, 1),
    _Pmopm8Mesrchannel58Index_Type()
)
pmopm8Mesrchannel58Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel58Index.setStatus("current")


class _Pmopm8Mesrchannel58Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel58Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel58Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel58Portn_Object = MibTableColumn
pmopm8Mesrchannel58Portn = _Pmopm8Mesrchannel58Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 472, 1, 2),
    _Pmopm8Mesrchannel58Portn_Type()
)
pmopm8Mesrchannel58Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel58Portn.setStatus("current")
_Pmopm8Mesrchannel59Table_Object = MibTable
pmopm8Mesrchannel59Table = _Pmopm8Mesrchannel59Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 480)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel59Table.setStatus("current")
_Pmopm8Mesrchannel59Entry_Object = MibTableRow
pmopm8Mesrchannel59Entry = _Pmopm8Mesrchannel59Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 480, 1)
)
pmopm8Mesrchannel59Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel59Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel59Entry.setStatus("current")


class _Pmopm8Mesrchannel59Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel59Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel59Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel59Index_Object = MibTableColumn
pmopm8Mesrchannel59Index = _Pmopm8Mesrchannel59Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 480, 1, 1),
    _Pmopm8Mesrchannel59Index_Type()
)
pmopm8Mesrchannel59Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel59Index.setStatus("current")


class _Pmopm8Mesrchannel59Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel59Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel59Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel59Portn_Object = MibTableColumn
pmopm8Mesrchannel59Portn = _Pmopm8Mesrchannel59Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 480, 1, 2),
    _Pmopm8Mesrchannel59Portn_Type()
)
pmopm8Mesrchannel59Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel59Portn.setStatus("current")
_Pmopm8Mesrchannel60Table_Object = MibTable
pmopm8Mesrchannel60Table = _Pmopm8Mesrchannel60Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 488)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel60Table.setStatus("current")
_Pmopm8Mesrchannel60Entry_Object = MibTableRow
pmopm8Mesrchannel60Entry = _Pmopm8Mesrchannel60Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 488, 1)
)
pmopm8Mesrchannel60Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel60Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel60Entry.setStatus("current")


class _Pmopm8Mesrchannel60Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel60Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel60Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel60Index_Object = MibTableColumn
pmopm8Mesrchannel60Index = _Pmopm8Mesrchannel60Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 488, 1, 1),
    _Pmopm8Mesrchannel60Index_Type()
)
pmopm8Mesrchannel60Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel60Index.setStatus("current")


class _Pmopm8Mesrchannel60Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel60Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel60Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel60Portn_Object = MibTableColumn
pmopm8Mesrchannel60Portn = _Pmopm8Mesrchannel60Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 488, 1, 2),
    _Pmopm8Mesrchannel60Portn_Type()
)
pmopm8Mesrchannel60Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel60Portn.setStatus("current")
_Pmopm8Mesrchannel61Table_Object = MibTable
pmopm8Mesrchannel61Table = _Pmopm8Mesrchannel61Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 496)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel61Table.setStatus("current")
_Pmopm8Mesrchannel61Entry_Object = MibTableRow
pmopm8Mesrchannel61Entry = _Pmopm8Mesrchannel61Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 496, 1)
)
pmopm8Mesrchannel61Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel61Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel61Entry.setStatus("current")


class _Pmopm8Mesrchannel61Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel61Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel61Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel61Index_Object = MibTableColumn
pmopm8Mesrchannel61Index = _Pmopm8Mesrchannel61Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 496, 1, 1),
    _Pmopm8Mesrchannel61Index_Type()
)
pmopm8Mesrchannel61Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel61Index.setStatus("current")


class _Pmopm8Mesrchannel61Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel61Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel61Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel61Portn_Object = MibTableColumn
pmopm8Mesrchannel61Portn = _Pmopm8Mesrchannel61Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 496, 1, 2),
    _Pmopm8Mesrchannel61Portn_Type()
)
pmopm8Mesrchannel61Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel61Portn.setStatus("current")
_Pmopm8Mesrchannel62Table_Object = MibTable
pmopm8Mesrchannel62Table = _Pmopm8Mesrchannel62Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 504)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel62Table.setStatus("current")
_Pmopm8Mesrchannel62Entry_Object = MibTableRow
pmopm8Mesrchannel62Entry = _Pmopm8Mesrchannel62Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 504, 1)
)
pmopm8Mesrchannel62Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel62Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel62Entry.setStatus("current")


class _Pmopm8Mesrchannel62Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel62Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel62Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel62Index_Object = MibTableColumn
pmopm8Mesrchannel62Index = _Pmopm8Mesrchannel62Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 504, 1, 1),
    _Pmopm8Mesrchannel62Index_Type()
)
pmopm8Mesrchannel62Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel62Index.setStatus("current")


class _Pmopm8Mesrchannel62Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel62Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel62Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel62Portn_Object = MibTableColumn
pmopm8Mesrchannel62Portn = _Pmopm8Mesrchannel62Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 504, 1, 2),
    _Pmopm8Mesrchannel62Portn_Type()
)
pmopm8Mesrchannel62Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel62Portn.setStatus("current")
_Pmopm8Mesrchannel63Table_Object = MibTable
pmopm8Mesrchannel63Table = _Pmopm8Mesrchannel63Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 512)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel63Table.setStatus("current")
_Pmopm8Mesrchannel63Entry_Object = MibTableRow
pmopm8Mesrchannel63Entry = _Pmopm8Mesrchannel63Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 512, 1)
)
pmopm8Mesrchannel63Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel63Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel63Entry.setStatus("current")


class _Pmopm8Mesrchannel63Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel63Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel63Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel63Index_Object = MibTableColumn
pmopm8Mesrchannel63Index = _Pmopm8Mesrchannel63Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 512, 1, 1),
    _Pmopm8Mesrchannel63Index_Type()
)
pmopm8Mesrchannel63Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel63Index.setStatus("current")


class _Pmopm8Mesrchannel63Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel63Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel63Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel63Portn_Object = MibTableColumn
pmopm8Mesrchannel63Portn = _Pmopm8Mesrchannel63Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 512, 1, 2),
    _Pmopm8Mesrchannel63Portn_Type()
)
pmopm8Mesrchannel63Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel63Portn.setStatus("current")
_Pmopm8Mesrchannel64Table_Object = MibTable
pmopm8Mesrchannel64Table = _Pmopm8Mesrchannel64Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 520)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel64Table.setStatus("current")
_Pmopm8Mesrchannel64Entry_Object = MibTableRow
pmopm8Mesrchannel64Entry = _Pmopm8Mesrchannel64Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 520, 1)
)
pmopm8Mesrchannel64Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel64Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel64Entry.setStatus("current")


class _Pmopm8Mesrchannel64Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel64Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel64Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel64Index_Object = MibTableColumn
pmopm8Mesrchannel64Index = _Pmopm8Mesrchannel64Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 520, 1, 1),
    _Pmopm8Mesrchannel64Index_Type()
)
pmopm8Mesrchannel64Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel64Index.setStatus("current")


class _Pmopm8Mesrchannel64Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel64Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel64Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel64Portn_Object = MibTableColumn
pmopm8Mesrchannel64Portn = _Pmopm8Mesrchannel64Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 520, 1, 2),
    _Pmopm8Mesrchannel64Portn_Type()
)
pmopm8Mesrchannel64Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel64Portn.setStatus("current")
_Pmopm8Mesrchannel65Table_Object = MibTable
pmopm8Mesrchannel65Table = _Pmopm8Mesrchannel65Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 528)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel65Table.setStatus("current")
_Pmopm8Mesrchannel65Entry_Object = MibTableRow
pmopm8Mesrchannel65Entry = _Pmopm8Mesrchannel65Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 528, 1)
)
pmopm8Mesrchannel65Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel65Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel65Entry.setStatus("current")


class _Pmopm8Mesrchannel65Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel65Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel65Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel65Index_Object = MibTableColumn
pmopm8Mesrchannel65Index = _Pmopm8Mesrchannel65Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 528, 1, 1),
    _Pmopm8Mesrchannel65Index_Type()
)
pmopm8Mesrchannel65Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel65Index.setStatus("current")


class _Pmopm8Mesrchannel65Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel65Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel65Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel65Portn_Object = MibTableColumn
pmopm8Mesrchannel65Portn = _Pmopm8Mesrchannel65Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 528, 1, 2),
    _Pmopm8Mesrchannel65Portn_Type()
)
pmopm8Mesrchannel65Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel65Portn.setStatus("current")
_Pmopm8Mesrchannel66Table_Object = MibTable
pmopm8Mesrchannel66Table = _Pmopm8Mesrchannel66Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 536)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel66Table.setStatus("current")
_Pmopm8Mesrchannel66Entry_Object = MibTableRow
pmopm8Mesrchannel66Entry = _Pmopm8Mesrchannel66Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 536, 1)
)
pmopm8Mesrchannel66Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel66Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel66Entry.setStatus("current")


class _Pmopm8Mesrchannel66Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel66Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel66Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel66Index_Object = MibTableColumn
pmopm8Mesrchannel66Index = _Pmopm8Mesrchannel66Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 536, 1, 1),
    _Pmopm8Mesrchannel66Index_Type()
)
pmopm8Mesrchannel66Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel66Index.setStatus("current")


class _Pmopm8Mesrchannel66Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel66Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel66Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel66Portn_Object = MibTableColumn
pmopm8Mesrchannel66Portn = _Pmopm8Mesrchannel66Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 536, 1, 2),
    _Pmopm8Mesrchannel66Portn_Type()
)
pmopm8Mesrchannel66Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel66Portn.setStatus("current")
_Pmopm8Mesrchannel67Table_Object = MibTable
pmopm8Mesrchannel67Table = _Pmopm8Mesrchannel67Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 544)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel67Table.setStatus("current")
_Pmopm8Mesrchannel67Entry_Object = MibTableRow
pmopm8Mesrchannel67Entry = _Pmopm8Mesrchannel67Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 544, 1)
)
pmopm8Mesrchannel67Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel67Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel67Entry.setStatus("current")


class _Pmopm8Mesrchannel67Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel67Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel67Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel67Index_Object = MibTableColumn
pmopm8Mesrchannel67Index = _Pmopm8Mesrchannel67Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 544, 1, 1),
    _Pmopm8Mesrchannel67Index_Type()
)
pmopm8Mesrchannel67Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel67Index.setStatus("current")


class _Pmopm8Mesrchannel67Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel67Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel67Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel67Portn_Object = MibTableColumn
pmopm8Mesrchannel67Portn = _Pmopm8Mesrchannel67Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 544, 1, 2),
    _Pmopm8Mesrchannel67Portn_Type()
)
pmopm8Mesrchannel67Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel67Portn.setStatus("current")
_Pmopm8Mesrchannel68Table_Object = MibTable
pmopm8Mesrchannel68Table = _Pmopm8Mesrchannel68Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 552)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel68Table.setStatus("current")
_Pmopm8Mesrchannel68Entry_Object = MibTableRow
pmopm8Mesrchannel68Entry = _Pmopm8Mesrchannel68Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 552, 1)
)
pmopm8Mesrchannel68Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel68Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel68Entry.setStatus("current")


class _Pmopm8Mesrchannel68Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel68Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel68Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel68Index_Object = MibTableColumn
pmopm8Mesrchannel68Index = _Pmopm8Mesrchannel68Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 552, 1, 1),
    _Pmopm8Mesrchannel68Index_Type()
)
pmopm8Mesrchannel68Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel68Index.setStatus("current")


class _Pmopm8Mesrchannel68Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel68Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel68Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel68Portn_Object = MibTableColumn
pmopm8Mesrchannel68Portn = _Pmopm8Mesrchannel68Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 552, 1, 2),
    _Pmopm8Mesrchannel68Portn_Type()
)
pmopm8Mesrchannel68Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel68Portn.setStatus("current")
_Pmopm8Mesrchannel69Table_Object = MibTable
pmopm8Mesrchannel69Table = _Pmopm8Mesrchannel69Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 560)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel69Table.setStatus("current")
_Pmopm8Mesrchannel69Entry_Object = MibTableRow
pmopm8Mesrchannel69Entry = _Pmopm8Mesrchannel69Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 560, 1)
)
pmopm8Mesrchannel69Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel69Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel69Entry.setStatus("current")


class _Pmopm8Mesrchannel69Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel69Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel69Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel69Index_Object = MibTableColumn
pmopm8Mesrchannel69Index = _Pmopm8Mesrchannel69Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 560, 1, 1),
    _Pmopm8Mesrchannel69Index_Type()
)
pmopm8Mesrchannel69Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel69Index.setStatus("current")


class _Pmopm8Mesrchannel69Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel69Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel69Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel69Portn_Object = MibTableColumn
pmopm8Mesrchannel69Portn = _Pmopm8Mesrchannel69Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 560, 1, 2),
    _Pmopm8Mesrchannel69Portn_Type()
)
pmopm8Mesrchannel69Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel69Portn.setStatus("current")
_Pmopm8Mesrchannel70Table_Object = MibTable
pmopm8Mesrchannel70Table = _Pmopm8Mesrchannel70Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 568)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel70Table.setStatus("current")
_Pmopm8Mesrchannel70Entry_Object = MibTableRow
pmopm8Mesrchannel70Entry = _Pmopm8Mesrchannel70Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 568, 1)
)
pmopm8Mesrchannel70Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel70Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel70Entry.setStatus("current")


class _Pmopm8Mesrchannel70Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel70Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel70Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel70Index_Object = MibTableColumn
pmopm8Mesrchannel70Index = _Pmopm8Mesrchannel70Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 568, 1, 1),
    _Pmopm8Mesrchannel70Index_Type()
)
pmopm8Mesrchannel70Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel70Index.setStatus("current")


class _Pmopm8Mesrchannel70Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel70Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel70Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel70Portn_Object = MibTableColumn
pmopm8Mesrchannel70Portn = _Pmopm8Mesrchannel70Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 568, 1, 2),
    _Pmopm8Mesrchannel70Portn_Type()
)
pmopm8Mesrchannel70Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel70Portn.setStatus("current")
_Pmopm8Mesrchannel71Table_Object = MibTable
pmopm8Mesrchannel71Table = _Pmopm8Mesrchannel71Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 576)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel71Table.setStatus("current")
_Pmopm8Mesrchannel71Entry_Object = MibTableRow
pmopm8Mesrchannel71Entry = _Pmopm8Mesrchannel71Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 576, 1)
)
pmopm8Mesrchannel71Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel71Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel71Entry.setStatus("current")


class _Pmopm8Mesrchannel71Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel71Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel71Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel71Index_Object = MibTableColumn
pmopm8Mesrchannel71Index = _Pmopm8Mesrchannel71Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 576, 1, 1),
    _Pmopm8Mesrchannel71Index_Type()
)
pmopm8Mesrchannel71Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel71Index.setStatus("current")


class _Pmopm8Mesrchannel71Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel71Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel71Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel71Portn_Object = MibTableColumn
pmopm8Mesrchannel71Portn = _Pmopm8Mesrchannel71Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 576, 1, 2),
    _Pmopm8Mesrchannel71Portn_Type()
)
pmopm8Mesrchannel71Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel71Portn.setStatus("current")
_Pmopm8Mesrchannel72Table_Object = MibTable
pmopm8Mesrchannel72Table = _Pmopm8Mesrchannel72Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 584)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel72Table.setStatus("current")
_Pmopm8Mesrchannel72Entry_Object = MibTableRow
pmopm8Mesrchannel72Entry = _Pmopm8Mesrchannel72Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 584, 1)
)
pmopm8Mesrchannel72Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel72Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel72Entry.setStatus("current")


class _Pmopm8Mesrchannel72Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel72Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel72Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel72Index_Object = MibTableColumn
pmopm8Mesrchannel72Index = _Pmopm8Mesrchannel72Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 584, 1, 1),
    _Pmopm8Mesrchannel72Index_Type()
)
pmopm8Mesrchannel72Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel72Index.setStatus("current")


class _Pmopm8Mesrchannel72Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel72Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel72Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel72Portn_Object = MibTableColumn
pmopm8Mesrchannel72Portn = _Pmopm8Mesrchannel72Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 584, 1, 2),
    _Pmopm8Mesrchannel72Portn_Type()
)
pmopm8Mesrchannel72Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel72Portn.setStatus("current")
_Pmopm8Mesrchannel73Table_Object = MibTable
pmopm8Mesrchannel73Table = _Pmopm8Mesrchannel73Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 592)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel73Table.setStatus("current")
_Pmopm8Mesrchannel73Entry_Object = MibTableRow
pmopm8Mesrchannel73Entry = _Pmopm8Mesrchannel73Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 592, 1)
)
pmopm8Mesrchannel73Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel73Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel73Entry.setStatus("current")


class _Pmopm8Mesrchannel73Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel73Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel73Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel73Index_Object = MibTableColumn
pmopm8Mesrchannel73Index = _Pmopm8Mesrchannel73Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 592, 1, 1),
    _Pmopm8Mesrchannel73Index_Type()
)
pmopm8Mesrchannel73Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel73Index.setStatus("current")


class _Pmopm8Mesrchannel73Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel73Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel73Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel73Portn_Object = MibTableColumn
pmopm8Mesrchannel73Portn = _Pmopm8Mesrchannel73Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 592, 1, 2),
    _Pmopm8Mesrchannel73Portn_Type()
)
pmopm8Mesrchannel73Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel73Portn.setStatus("current")
_Pmopm8Mesrchannel74Table_Object = MibTable
pmopm8Mesrchannel74Table = _Pmopm8Mesrchannel74Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 600)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel74Table.setStatus("current")
_Pmopm8Mesrchannel74Entry_Object = MibTableRow
pmopm8Mesrchannel74Entry = _Pmopm8Mesrchannel74Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 600, 1)
)
pmopm8Mesrchannel74Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel74Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel74Entry.setStatus("current")


class _Pmopm8Mesrchannel74Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel74Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel74Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel74Index_Object = MibTableColumn
pmopm8Mesrchannel74Index = _Pmopm8Mesrchannel74Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 600, 1, 1),
    _Pmopm8Mesrchannel74Index_Type()
)
pmopm8Mesrchannel74Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel74Index.setStatus("current")


class _Pmopm8Mesrchannel74Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel74Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel74Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel74Portn_Object = MibTableColumn
pmopm8Mesrchannel74Portn = _Pmopm8Mesrchannel74Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 600, 1, 2),
    _Pmopm8Mesrchannel74Portn_Type()
)
pmopm8Mesrchannel74Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel74Portn.setStatus("current")
_Pmopm8Mesrchannel75Table_Object = MibTable
pmopm8Mesrchannel75Table = _Pmopm8Mesrchannel75Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 608)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel75Table.setStatus("current")
_Pmopm8Mesrchannel75Entry_Object = MibTableRow
pmopm8Mesrchannel75Entry = _Pmopm8Mesrchannel75Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 608, 1)
)
pmopm8Mesrchannel75Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel75Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel75Entry.setStatus("current")


class _Pmopm8Mesrchannel75Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel75Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel75Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel75Index_Object = MibTableColumn
pmopm8Mesrchannel75Index = _Pmopm8Mesrchannel75Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 608, 1, 1),
    _Pmopm8Mesrchannel75Index_Type()
)
pmopm8Mesrchannel75Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel75Index.setStatus("current")


class _Pmopm8Mesrchannel75Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel75Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel75Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel75Portn_Object = MibTableColumn
pmopm8Mesrchannel75Portn = _Pmopm8Mesrchannel75Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 608, 1, 2),
    _Pmopm8Mesrchannel75Portn_Type()
)
pmopm8Mesrchannel75Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel75Portn.setStatus("current")
_Pmopm8Mesrchannel76Table_Object = MibTable
pmopm8Mesrchannel76Table = _Pmopm8Mesrchannel76Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 616)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel76Table.setStatus("current")
_Pmopm8Mesrchannel76Entry_Object = MibTableRow
pmopm8Mesrchannel76Entry = _Pmopm8Mesrchannel76Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 616, 1)
)
pmopm8Mesrchannel76Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel76Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel76Entry.setStatus("current")


class _Pmopm8Mesrchannel76Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel76Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel76Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel76Index_Object = MibTableColumn
pmopm8Mesrchannel76Index = _Pmopm8Mesrchannel76Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 616, 1, 1),
    _Pmopm8Mesrchannel76Index_Type()
)
pmopm8Mesrchannel76Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel76Index.setStatus("current")


class _Pmopm8Mesrchannel76Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel76Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel76Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel76Portn_Object = MibTableColumn
pmopm8Mesrchannel76Portn = _Pmopm8Mesrchannel76Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 616, 1, 2),
    _Pmopm8Mesrchannel76Portn_Type()
)
pmopm8Mesrchannel76Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel76Portn.setStatus("current")
_Pmopm8Mesrchannel77Table_Object = MibTable
pmopm8Mesrchannel77Table = _Pmopm8Mesrchannel77Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 624)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel77Table.setStatus("current")
_Pmopm8Mesrchannel77Entry_Object = MibTableRow
pmopm8Mesrchannel77Entry = _Pmopm8Mesrchannel77Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 624, 1)
)
pmopm8Mesrchannel77Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel77Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel77Entry.setStatus("current")


class _Pmopm8Mesrchannel77Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel77Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel77Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel77Index_Object = MibTableColumn
pmopm8Mesrchannel77Index = _Pmopm8Mesrchannel77Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 624, 1, 1),
    _Pmopm8Mesrchannel77Index_Type()
)
pmopm8Mesrchannel77Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel77Index.setStatus("current")


class _Pmopm8Mesrchannel77Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel77Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel77Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel77Portn_Object = MibTableColumn
pmopm8Mesrchannel77Portn = _Pmopm8Mesrchannel77Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 624, 1, 2),
    _Pmopm8Mesrchannel77Portn_Type()
)
pmopm8Mesrchannel77Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel77Portn.setStatus("current")
_Pmopm8Mesrchannel78Table_Object = MibTable
pmopm8Mesrchannel78Table = _Pmopm8Mesrchannel78Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 632)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel78Table.setStatus("current")
_Pmopm8Mesrchannel78Entry_Object = MibTableRow
pmopm8Mesrchannel78Entry = _Pmopm8Mesrchannel78Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 632, 1)
)
pmopm8Mesrchannel78Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel78Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel78Entry.setStatus("current")


class _Pmopm8Mesrchannel78Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel78Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel78Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel78Index_Object = MibTableColumn
pmopm8Mesrchannel78Index = _Pmopm8Mesrchannel78Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 632, 1, 1),
    _Pmopm8Mesrchannel78Index_Type()
)
pmopm8Mesrchannel78Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel78Index.setStatus("current")


class _Pmopm8Mesrchannel78Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel78Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel78Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel78Portn_Object = MibTableColumn
pmopm8Mesrchannel78Portn = _Pmopm8Mesrchannel78Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 632, 1, 2),
    _Pmopm8Mesrchannel78Portn_Type()
)
pmopm8Mesrchannel78Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel78Portn.setStatus("current")
_Pmopm8Mesrchannel79Table_Object = MibTable
pmopm8Mesrchannel79Table = _Pmopm8Mesrchannel79Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 640)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel79Table.setStatus("current")
_Pmopm8Mesrchannel79Entry_Object = MibTableRow
pmopm8Mesrchannel79Entry = _Pmopm8Mesrchannel79Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 640, 1)
)
pmopm8Mesrchannel79Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel79Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel79Entry.setStatus("current")


class _Pmopm8Mesrchannel79Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel79Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel79Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel79Index_Object = MibTableColumn
pmopm8Mesrchannel79Index = _Pmopm8Mesrchannel79Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 640, 1, 1),
    _Pmopm8Mesrchannel79Index_Type()
)
pmopm8Mesrchannel79Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel79Index.setStatus("current")


class _Pmopm8Mesrchannel79Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel79Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel79Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel79Portn_Object = MibTableColumn
pmopm8Mesrchannel79Portn = _Pmopm8Mesrchannel79Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 640, 1, 2),
    _Pmopm8Mesrchannel79Portn_Type()
)
pmopm8Mesrchannel79Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel79Portn.setStatus("current")
_Pmopm8Mesrchannel80Table_Object = MibTable
pmopm8Mesrchannel80Table = _Pmopm8Mesrchannel80Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 648)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel80Table.setStatus("current")
_Pmopm8Mesrchannel80Entry_Object = MibTableRow
pmopm8Mesrchannel80Entry = _Pmopm8Mesrchannel80Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 648, 1)
)
pmopm8Mesrchannel80Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel80Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel80Entry.setStatus("current")


class _Pmopm8Mesrchannel80Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel80Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel80Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel80Index_Object = MibTableColumn
pmopm8Mesrchannel80Index = _Pmopm8Mesrchannel80Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 648, 1, 1),
    _Pmopm8Mesrchannel80Index_Type()
)
pmopm8Mesrchannel80Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel80Index.setStatus("current")


class _Pmopm8Mesrchannel80Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel80Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel80Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel80Portn_Object = MibTableColumn
pmopm8Mesrchannel80Portn = _Pmopm8Mesrchannel80Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 648, 1, 2),
    _Pmopm8Mesrchannel80Portn_Type()
)
pmopm8Mesrchannel80Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel80Portn.setStatus("current")
_Pmopm8Mesrchannel81Table_Object = MibTable
pmopm8Mesrchannel81Table = _Pmopm8Mesrchannel81Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 656)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel81Table.setStatus("current")
_Pmopm8Mesrchannel81Entry_Object = MibTableRow
pmopm8Mesrchannel81Entry = _Pmopm8Mesrchannel81Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 656, 1)
)
pmopm8Mesrchannel81Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel81Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel81Entry.setStatus("current")


class _Pmopm8Mesrchannel81Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel81Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel81Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel81Index_Object = MibTableColumn
pmopm8Mesrchannel81Index = _Pmopm8Mesrchannel81Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 656, 1, 1),
    _Pmopm8Mesrchannel81Index_Type()
)
pmopm8Mesrchannel81Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel81Index.setStatus("current")


class _Pmopm8Mesrchannel81Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel81Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel81Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel81Portn_Object = MibTableColumn
pmopm8Mesrchannel81Portn = _Pmopm8Mesrchannel81Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 656, 1, 2),
    _Pmopm8Mesrchannel81Portn_Type()
)
pmopm8Mesrchannel81Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel81Portn.setStatus("current")
_Pmopm8Mesrchannel82Table_Object = MibTable
pmopm8Mesrchannel82Table = _Pmopm8Mesrchannel82Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 664)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel82Table.setStatus("current")
_Pmopm8Mesrchannel82Entry_Object = MibTableRow
pmopm8Mesrchannel82Entry = _Pmopm8Mesrchannel82Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 664, 1)
)
pmopm8Mesrchannel82Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel82Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel82Entry.setStatus("current")


class _Pmopm8Mesrchannel82Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel82Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel82Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel82Index_Object = MibTableColumn
pmopm8Mesrchannel82Index = _Pmopm8Mesrchannel82Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 664, 1, 1),
    _Pmopm8Mesrchannel82Index_Type()
)
pmopm8Mesrchannel82Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel82Index.setStatus("current")


class _Pmopm8Mesrchannel82Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel82Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel82Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel82Portn_Object = MibTableColumn
pmopm8Mesrchannel82Portn = _Pmopm8Mesrchannel82Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 664, 1, 2),
    _Pmopm8Mesrchannel82Portn_Type()
)
pmopm8Mesrchannel82Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel82Portn.setStatus("current")
_Pmopm8Mesrchannel83Table_Object = MibTable
pmopm8Mesrchannel83Table = _Pmopm8Mesrchannel83Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 672)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel83Table.setStatus("current")
_Pmopm8Mesrchannel83Entry_Object = MibTableRow
pmopm8Mesrchannel83Entry = _Pmopm8Mesrchannel83Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 672, 1)
)
pmopm8Mesrchannel83Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel83Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel83Entry.setStatus("current")


class _Pmopm8Mesrchannel83Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel83Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel83Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel83Index_Object = MibTableColumn
pmopm8Mesrchannel83Index = _Pmopm8Mesrchannel83Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 672, 1, 1),
    _Pmopm8Mesrchannel83Index_Type()
)
pmopm8Mesrchannel83Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel83Index.setStatus("current")


class _Pmopm8Mesrchannel83Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel83Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel83Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel83Portn_Object = MibTableColumn
pmopm8Mesrchannel83Portn = _Pmopm8Mesrchannel83Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 672, 1, 2),
    _Pmopm8Mesrchannel83Portn_Type()
)
pmopm8Mesrchannel83Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel83Portn.setStatus("current")
_Pmopm8Mesrchannel84Table_Object = MibTable
pmopm8Mesrchannel84Table = _Pmopm8Mesrchannel84Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 680)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel84Table.setStatus("current")
_Pmopm8Mesrchannel84Entry_Object = MibTableRow
pmopm8Mesrchannel84Entry = _Pmopm8Mesrchannel84Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 680, 1)
)
pmopm8Mesrchannel84Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel84Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel84Entry.setStatus("current")


class _Pmopm8Mesrchannel84Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel84Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel84Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel84Index_Object = MibTableColumn
pmopm8Mesrchannel84Index = _Pmopm8Mesrchannel84Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 680, 1, 1),
    _Pmopm8Mesrchannel84Index_Type()
)
pmopm8Mesrchannel84Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel84Index.setStatus("current")


class _Pmopm8Mesrchannel84Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel84Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel84Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel84Portn_Object = MibTableColumn
pmopm8Mesrchannel84Portn = _Pmopm8Mesrchannel84Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 680, 1, 2),
    _Pmopm8Mesrchannel84Portn_Type()
)
pmopm8Mesrchannel84Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel84Portn.setStatus("current")
_Pmopm8Mesrchannel85Table_Object = MibTable
pmopm8Mesrchannel85Table = _Pmopm8Mesrchannel85Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 688)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel85Table.setStatus("current")
_Pmopm8Mesrchannel85Entry_Object = MibTableRow
pmopm8Mesrchannel85Entry = _Pmopm8Mesrchannel85Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 688, 1)
)
pmopm8Mesrchannel85Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel85Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel85Entry.setStatus("current")


class _Pmopm8Mesrchannel85Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel85Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel85Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel85Index_Object = MibTableColumn
pmopm8Mesrchannel85Index = _Pmopm8Mesrchannel85Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 688, 1, 1),
    _Pmopm8Mesrchannel85Index_Type()
)
pmopm8Mesrchannel85Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel85Index.setStatus("current")


class _Pmopm8Mesrchannel85Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel85Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel85Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel85Portn_Object = MibTableColumn
pmopm8Mesrchannel85Portn = _Pmopm8Mesrchannel85Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 688, 1, 2),
    _Pmopm8Mesrchannel85Portn_Type()
)
pmopm8Mesrchannel85Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel85Portn.setStatus("current")
_Pmopm8Mesrchannel86Table_Object = MibTable
pmopm8Mesrchannel86Table = _Pmopm8Mesrchannel86Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 696)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel86Table.setStatus("current")
_Pmopm8Mesrchannel86Entry_Object = MibTableRow
pmopm8Mesrchannel86Entry = _Pmopm8Mesrchannel86Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 696, 1)
)
pmopm8Mesrchannel86Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel86Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel86Entry.setStatus("current")


class _Pmopm8Mesrchannel86Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel86Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel86Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel86Index_Object = MibTableColumn
pmopm8Mesrchannel86Index = _Pmopm8Mesrchannel86Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 696, 1, 1),
    _Pmopm8Mesrchannel86Index_Type()
)
pmopm8Mesrchannel86Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel86Index.setStatus("current")


class _Pmopm8Mesrchannel86Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel86Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel86Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel86Portn_Object = MibTableColumn
pmopm8Mesrchannel86Portn = _Pmopm8Mesrchannel86Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 696, 1, 2),
    _Pmopm8Mesrchannel86Portn_Type()
)
pmopm8Mesrchannel86Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel86Portn.setStatus("current")
_Pmopm8Mesrchannel87Table_Object = MibTable
pmopm8Mesrchannel87Table = _Pmopm8Mesrchannel87Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 704)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel87Table.setStatus("current")
_Pmopm8Mesrchannel87Entry_Object = MibTableRow
pmopm8Mesrchannel87Entry = _Pmopm8Mesrchannel87Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 704, 1)
)
pmopm8Mesrchannel87Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel87Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel87Entry.setStatus("current")


class _Pmopm8Mesrchannel87Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel87Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel87Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel87Index_Object = MibTableColumn
pmopm8Mesrchannel87Index = _Pmopm8Mesrchannel87Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 704, 1, 1),
    _Pmopm8Mesrchannel87Index_Type()
)
pmopm8Mesrchannel87Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel87Index.setStatus("current")


class _Pmopm8Mesrchannel87Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel87Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel87Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel87Portn_Object = MibTableColumn
pmopm8Mesrchannel87Portn = _Pmopm8Mesrchannel87Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 704, 1, 2),
    _Pmopm8Mesrchannel87Portn_Type()
)
pmopm8Mesrchannel87Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel87Portn.setStatus("current")
_Pmopm8Mesrchannel88Table_Object = MibTable
pmopm8Mesrchannel88Table = _Pmopm8Mesrchannel88Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 712)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel88Table.setStatus("current")
_Pmopm8Mesrchannel88Entry_Object = MibTableRow
pmopm8Mesrchannel88Entry = _Pmopm8Mesrchannel88Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 712, 1)
)
pmopm8Mesrchannel88Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel88Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel88Entry.setStatus("current")


class _Pmopm8Mesrchannel88Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel88Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel88Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel88Index_Object = MibTableColumn
pmopm8Mesrchannel88Index = _Pmopm8Mesrchannel88Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 712, 1, 1),
    _Pmopm8Mesrchannel88Index_Type()
)
pmopm8Mesrchannel88Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel88Index.setStatus("current")


class _Pmopm8Mesrchannel88Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel88Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel88Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel88Portn_Object = MibTableColumn
pmopm8Mesrchannel88Portn = _Pmopm8Mesrchannel88Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 712, 1, 2),
    _Pmopm8Mesrchannel88Portn_Type()
)
pmopm8Mesrchannel88Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel88Portn.setStatus("current")
_Pmopm8Mesrchannel89Table_Object = MibTable
pmopm8Mesrchannel89Table = _Pmopm8Mesrchannel89Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 720)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel89Table.setStatus("current")
_Pmopm8Mesrchannel89Entry_Object = MibTableRow
pmopm8Mesrchannel89Entry = _Pmopm8Mesrchannel89Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 720, 1)
)
pmopm8Mesrchannel89Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel89Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel89Entry.setStatus("current")


class _Pmopm8Mesrchannel89Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel89Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel89Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel89Index_Object = MibTableColumn
pmopm8Mesrchannel89Index = _Pmopm8Mesrchannel89Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 720, 1, 1),
    _Pmopm8Mesrchannel89Index_Type()
)
pmopm8Mesrchannel89Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel89Index.setStatus("current")


class _Pmopm8Mesrchannel89Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel89Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel89Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel89Portn_Object = MibTableColumn
pmopm8Mesrchannel89Portn = _Pmopm8Mesrchannel89Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 720, 1, 2),
    _Pmopm8Mesrchannel89Portn_Type()
)
pmopm8Mesrchannel89Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel89Portn.setStatus("current")
_Pmopm8Mesrchannel90Table_Object = MibTable
pmopm8Mesrchannel90Table = _Pmopm8Mesrchannel90Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 728)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel90Table.setStatus("current")
_Pmopm8Mesrchannel90Entry_Object = MibTableRow
pmopm8Mesrchannel90Entry = _Pmopm8Mesrchannel90Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 728, 1)
)
pmopm8Mesrchannel90Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel90Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel90Entry.setStatus("current")


class _Pmopm8Mesrchannel90Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel90Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel90Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel90Index_Object = MibTableColumn
pmopm8Mesrchannel90Index = _Pmopm8Mesrchannel90Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 728, 1, 1),
    _Pmopm8Mesrchannel90Index_Type()
)
pmopm8Mesrchannel90Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel90Index.setStatus("current")


class _Pmopm8Mesrchannel90Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel90Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel90Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel90Portn_Object = MibTableColumn
pmopm8Mesrchannel90Portn = _Pmopm8Mesrchannel90Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 728, 1, 2),
    _Pmopm8Mesrchannel90Portn_Type()
)
pmopm8Mesrchannel90Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel90Portn.setStatus("current")
_Pmopm8Mesrchannel91Table_Object = MibTable
pmopm8Mesrchannel91Table = _Pmopm8Mesrchannel91Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 736)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel91Table.setStatus("current")
_Pmopm8Mesrchannel91Entry_Object = MibTableRow
pmopm8Mesrchannel91Entry = _Pmopm8Mesrchannel91Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 736, 1)
)
pmopm8Mesrchannel91Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel91Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel91Entry.setStatus("current")


class _Pmopm8Mesrchannel91Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel91Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel91Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel91Index_Object = MibTableColumn
pmopm8Mesrchannel91Index = _Pmopm8Mesrchannel91Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 736, 1, 1),
    _Pmopm8Mesrchannel91Index_Type()
)
pmopm8Mesrchannel91Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel91Index.setStatus("current")


class _Pmopm8Mesrchannel91Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel91Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel91Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel91Portn_Object = MibTableColumn
pmopm8Mesrchannel91Portn = _Pmopm8Mesrchannel91Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 736, 1, 2),
    _Pmopm8Mesrchannel91Portn_Type()
)
pmopm8Mesrchannel91Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel91Portn.setStatus("current")
_Pmopm8Mesrchannel92Table_Object = MibTable
pmopm8Mesrchannel92Table = _Pmopm8Mesrchannel92Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 744)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel92Table.setStatus("current")
_Pmopm8Mesrchannel92Entry_Object = MibTableRow
pmopm8Mesrchannel92Entry = _Pmopm8Mesrchannel92Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 744, 1)
)
pmopm8Mesrchannel92Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel92Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel92Entry.setStatus("current")


class _Pmopm8Mesrchannel92Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel92Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel92Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel92Index_Object = MibTableColumn
pmopm8Mesrchannel92Index = _Pmopm8Mesrchannel92Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 744, 1, 1),
    _Pmopm8Mesrchannel92Index_Type()
)
pmopm8Mesrchannel92Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel92Index.setStatus("current")


class _Pmopm8Mesrchannel92Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel92Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel92Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel92Portn_Object = MibTableColumn
pmopm8Mesrchannel92Portn = _Pmopm8Mesrchannel92Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 744, 1, 2),
    _Pmopm8Mesrchannel92Portn_Type()
)
pmopm8Mesrchannel92Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel92Portn.setStatus("current")
_Pmopm8Mesrchannel93Table_Object = MibTable
pmopm8Mesrchannel93Table = _Pmopm8Mesrchannel93Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 752)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel93Table.setStatus("current")
_Pmopm8Mesrchannel93Entry_Object = MibTableRow
pmopm8Mesrchannel93Entry = _Pmopm8Mesrchannel93Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 752, 1)
)
pmopm8Mesrchannel93Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel93Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel93Entry.setStatus("current")


class _Pmopm8Mesrchannel93Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel93Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel93Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel93Index_Object = MibTableColumn
pmopm8Mesrchannel93Index = _Pmopm8Mesrchannel93Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 752, 1, 1),
    _Pmopm8Mesrchannel93Index_Type()
)
pmopm8Mesrchannel93Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel93Index.setStatus("current")


class _Pmopm8Mesrchannel93Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel93Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel93Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel93Portn_Object = MibTableColumn
pmopm8Mesrchannel93Portn = _Pmopm8Mesrchannel93Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 752, 1, 2),
    _Pmopm8Mesrchannel93Portn_Type()
)
pmopm8Mesrchannel93Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel93Portn.setStatus("current")
_Pmopm8Mesrchannel94Table_Object = MibTable
pmopm8Mesrchannel94Table = _Pmopm8Mesrchannel94Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 760)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel94Table.setStatus("current")
_Pmopm8Mesrchannel94Entry_Object = MibTableRow
pmopm8Mesrchannel94Entry = _Pmopm8Mesrchannel94Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 760, 1)
)
pmopm8Mesrchannel94Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel94Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel94Entry.setStatus("current")


class _Pmopm8Mesrchannel94Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel94Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel94Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel94Index_Object = MibTableColumn
pmopm8Mesrchannel94Index = _Pmopm8Mesrchannel94Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 760, 1, 1),
    _Pmopm8Mesrchannel94Index_Type()
)
pmopm8Mesrchannel94Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel94Index.setStatus("current")


class _Pmopm8Mesrchannel94Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel94Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel94Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel94Portn_Object = MibTableColumn
pmopm8Mesrchannel94Portn = _Pmopm8Mesrchannel94Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 760, 1, 2),
    _Pmopm8Mesrchannel94Portn_Type()
)
pmopm8Mesrchannel94Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel94Portn.setStatus("current")
_Pmopm8Mesrchannel95Table_Object = MibTable
pmopm8Mesrchannel95Table = _Pmopm8Mesrchannel95Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 768)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel95Table.setStatus("current")
_Pmopm8Mesrchannel95Entry_Object = MibTableRow
pmopm8Mesrchannel95Entry = _Pmopm8Mesrchannel95Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 768, 1)
)
pmopm8Mesrchannel95Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel95Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel95Entry.setStatus("current")


class _Pmopm8Mesrchannel95Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel95Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel95Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel95Index_Object = MibTableColumn
pmopm8Mesrchannel95Index = _Pmopm8Mesrchannel95Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 768, 1, 1),
    _Pmopm8Mesrchannel95Index_Type()
)
pmopm8Mesrchannel95Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel95Index.setStatus("current")


class _Pmopm8Mesrchannel95Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel95Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel95Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel95Portn_Object = MibTableColumn
pmopm8Mesrchannel95Portn = _Pmopm8Mesrchannel95Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 768, 1, 2),
    _Pmopm8Mesrchannel95Portn_Type()
)
pmopm8Mesrchannel95Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel95Portn.setStatus("current")
_Pmopm8Mesrchannel96Table_Object = MibTable
pmopm8Mesrchannel96Table = _Pmopm8Mesrchannel96Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 776)
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel96Table.setStatus("current")
_Pmopm8Mesrchannel96Entry_Object = MibTableRow
pmopm8Mesrchannel96Entry = _Pmopm8Mesrchannel96Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 776, 1)
)
pmopm8Mesrchannel96Entry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8Mesrchannel96Index"),
)
if mibBuilder.loadTexts:
    pmopm8Mesrchannel96Entry.setStatus("current")


class _Pmopm8Mesrchannel96Index_Type(Integer32):
    """Custom type pmopm8Mesrchannel96Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8Mesrchannel96Index_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel96Index_Object = MibTableColumn
pmopm8Mesrchannel96Index = _Pmopm8Mesrchannel96Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 776, 1, 1),
    _Pmopm8Mesrchannel96Index_Type()
)
pmopm8Mesrchannel96Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel96Index.setStatus("current")


class _Pmopm8Mesrchannel96Portn_Type(Integer32):
    """Custom type pmopm8Mesrchannel96Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8Mesrchannel96Portn_Type.__name__ = "Integer32"
_Pmopm8Mesrchannel96Portn_Object = MibTableColumn
pmopm8Mesrchannel96Portn = _Pmopm8Mesrchannel96Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 776, 1, 2),
    _Pmopm8Mesrchannel96Portn_Type()
)
pmopm8Mesrchannel96Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Mesrchannel96Portn.setStatus("current")
_Pmopm8MesrportInputPwrTable_Object = MibTable
pmopm8MesrportInputPwrTable = _Pmopm8MesrportInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 784)
)
if mibBuilder.loadTexts:
    pmopm8MesrportInputPwrTable.setStatus("current")
_Pmopm8MesrportInputPwrEntry_Object = MibTableRow
pmopm8MesrportInputPwrEntry = _Pmopm8MesrportInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 784, 1)
)
pmopm8MesrportInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8MesrportInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pmopm8MesrportInputPwrEntry.setStatus("current")


class _Pmopm8MesrportInputPwrIndex_Type(Integer32):
    """Custom type pmopm8MesrportInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8MesrportInputPwrIndex_Type.__name__ = "Integer32"
_Pmopm8MesrportInputPwrIndex_Object = MibTableColumn
pmopm8MesrportInputPwrIndex = _Pmopm8MesrportInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 784, 1, 1),
    _Pmopm8MesrportInputPwrIndex_Type()
)
pmopm8MesrportInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8MesrportInputPwrIndex.setStatus("current")


class _Pmopm8MesrportInputPwrPortn_Type(Integer32):
    """Custom type pmopm8MesrportInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8MesrportInputPwrPortn_Type.__name__ = "Integer32"
_Pmopm8MesrportInputPwrPortn_Object = MibTableColumn
pmopm8MesrportInputPwrPortn = _Pmopm8MesrportInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 784, 1, 2),
    _Pmopm8MesrportInputPwrPortn_Type()
)
pmopm8MesrportInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8MesrportInputPwrPortn.setStatus("current")
_Pmopm8MesrchannelMaxPwrTable_Object = MibTable
pmopm8MesrchannelMaxPwrTable = _Pmopm8MesrchannelMaxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 792)
)
if mibBuilder.loadTexts:
    pmopm8MesrchannelMaxPwrTable.setStatus("current")
_Pmopm8MesrchannelMaxPwrEntry_Object = MibTableRow
pmopm8MesrchannelMaxPwrEntry = _Pmopm8MesrchannelMaxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 792, 1)
)
pmopm8MesrchannelMaxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8MesrchannelMaxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmopm8MesrchannelMaxPwrEntry.setStatus("current")


class _Pmopm8MesrchannelMaxPwrIndex_Type(Integer32):
    """Custom type pmopm8MesrchannelMaxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8MesrchannelMaxPwrIndex_Type.__name__ = "Integer32"
_Pmopm8MesrchannelMaxPwrIndex_Object = MibTableColumn
pmopm8MesrchannelMaxPwrIndex = _Pmopm8MesrchannelMaxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 792, 1, 1),
    _Pmopm8MesrchannelMaxPwrIndex_Type()
)
pmopm8MesrchannelMaxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8MesrchannelMaxPwrIndex.setStatus("current")


class _Pmopm8MesrchannelMaxPwrPortn_Type(Integer32):
    """Custom type pmopm8MesrchannelMaxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8MesrchannelMaxPwrPortn_Type.__name__ = "Integer32"
_Pmopm8MesrchannelMaxPwrPortn_Object = MibTableColumn
pmopm8MesrchannelMaxPwrPortn = _Pmopm8MesrchannelMaxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 792, 1, 2),
    _Pmopm8MesrchannelMaxPwrPortn_Type()
)
pmopm8MesrchannelMaxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8MesrchannelMaxPwrPortn.setStatus("current")
_Pmopm8MesrchannelMinPwrTable_Object = MibTable
pmopm8MesrchannelMinPwrTable = _Pmopm8MesrchannelMinPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 800)
)
if mibBuilder.loadTexts:
    pmopm8MesrchannelMinPwrTable.setStatus("current")
_Pmopm8MesrchannelMinPwrEntry_Object = MibTableRow
pmopm8MesrchannelMinPwrEntry = _Pmopm8MesrchannelMinPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 800, 1)
)
pmopm8MesrchannelMinPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8MesrchannelMinPwrIndex"),
)
if mibBuilder.loadTexts:
    pmopm8MesrchannelMinPwrEntry.setStatus("current")


class _Pmopm8MesrchannelMinPwrIndex_Type(Integer32):
    """Custom type pmopm8MesrchannelMinPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8MesrchannelMinPwrIndex_Type.__name__ = "Integer32"
_Pmopm8MesrchannelMinPwrIndex_Object = MibTableColumn
pmopm8MesrchannelMinPwrIndex = _Pmopm8MesrchannelMinPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 800, 1, 1),
    _Pmopm8MesrchannelMinPwrIndex_Type()
)
pmopm8MesrchannelMinPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8MesrchannelMinPwrIndex.setStatus("current")


class _Pmopm8MesrchannelMinPwrPortn_Type(Integer32):
    """Custom type pmopm8MesrchannelMinPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8MesrchannelMinPwrPortn_Type.__name__ = "Integer32"
_Pmopm8MesrchannelMinPwrPortn_Object = MibTableColumn
pmopm8MesrchannelMinPwrPortn = _Pmopm8MesrchannelMinPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 2, 800, 1, 2),
    _Pmopm8MesrchannelMinPwrPortn_Type()
)
pmopm8MesrchannelMinPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8MesrchannelMinPwrPortn.setStatus("current")
_Pmopm8MesrLine_ObjectIdentity = ObjectIdentity
pmopm8MesrLine = _Pmopm8MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 3, 3)
)
_Pmopm8controlsWrite_ObjectIdentity = ObjectIdentity
pmopm8controlsWrite = _Pmopm8controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6)
)
_Pmopm8CtrlOther_ObjectIdentity = ObjectIdentity
pmopm8CtrlOther = _Pmopm8CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1)
)
_Pmopm8CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmopm8CtrlconfMgnt1 = _Pmopm8CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 1)
)
_Pmopm8CtrlConf1Load1_Type = EkiOnOff
_Pmopm8CtrlConf1Load1_Object = MibScalar
pmopm8CtrlConf1Load1 = _Pmopm8CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 1, 1),
    _Pmopm8CtrlConf1Load1_Type()
)
pmopm8CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlConf1Load1.setStatus("current")
_Pmopm8CtrlConf2Load1_Type = EkiOnOff
_Pmopm8CtrlConf2Load1_Object = MibScalar
pmopm8CtrlConf2Load1 = _Pmopm8CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 1, 2),
    _Pmopm8CtrlConf2Load1_Type()
)
pmopm8CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlConf2Load1.setStatus("current")
_Pmopm8CtrlConf2Flash1_Type = EkiOnOff
_Pmopm8CtrlConf2Flash1_Object = MibScalar
pmopm8CtrlConf2Flash1 = _Pmopm8CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 1, 10),
    _Pmopm8CtrlConf2Flash1_Type()
)
pmopm8CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlConf2Flash1.setStatus("current")
_Pmopm8CtrlConf2Clear1_Type = EkiOnOff
_Pmopm8CtrlConf2Clear1_Object = MibScalar
pmopm8CtrlConf2Clear1 = _Pmopm8CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 1, 14),
    _Pmopm8CtrlConf2Clear1_Type()
)
pmopm8CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlConf2Clear1.setStatus("current")
_Pmopm8Ctrlsynth4_ObjectIdentity = ObjectIdentity
pmopm8Ctrlsynth4 = _Pmopm8Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 4)
)
_Pmopm8CtrlCorrelatOn_Type = EkiOnOff
_Pmopm8CtrlCorrelatOn_Object = MibScalar
pmopm8CtrlCorrelatOn = _Pmopm8CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 4, 1),
    _Pmopm8CtrlCorrelatOn_Type()
)
pmopm8CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlCorrelatOn.setStatus("current")
_Pmopm8CtrlCorrelatOff_Type = EkiOnOff
_Pmopm8CtrlCorrelatOff_Object = MibScalar
pmopm8CtrlCorrelatOff = _Pmopm8CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 4, 2),
    _Pmopm8CtrlCorrelatOff_Type()
)
pmopm8CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlCorrelatOff.setStatus("current")
_Pmopm8CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmopm8CtrlswMgnt = _Pmopm8CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 5)
)
_Pmopm8CtrlColdReset_Type = EkiOnOff
_Pmopm8CtrlColdReset_Object = MibScalar
pmopm8CtrlColdReset = _Pmopm8CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 5, 2),
    _Pmopm8CtrlColdReset_Type()
)
pmopm8CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlColdReset.setStatus("current")
_Pmopm8CtrlWarmReset_Type = EkiOnOff
_Pmopm8CtrlWarmReset_Object = MibScalar
pmopm8CtrlWarmReset = _Pmopm8CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 5, 3),
    _Pmopm8CtrlWarmReset_Type()
)
pmopm8CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlWarmReset.setStatus("current")
_Pmopm8CtrlLoadSwBank1_Type = EkiOnOff
_Pmopm8CtrlLoadSwBank1_Object = MibScalar
pmopm8CtrlLoadSwBank1 = _Pmopm8CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 5, 5),
    _Pmopm8CtrlLoadSwBank1_Type()
)
pmopm8CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlLoadSwBank1.setStatus("current")
_Pmopm8CtrlLoadSwBank2_Type = EkiOnOff
_Pmopm8CtrlLoadSwBank2_Object = MibScalar
pmopm8CtrlLoadSwBank2 = _Pmopm8CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 5, 6),
    _Pmopm8CtrlLoadSwBank2_Type()
)
pmopm8CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlLoadSwBank2.setStatus("current")
_Pmopm8CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmopm8CtrlgwMgnt = _Pmopm8CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 6)
)
_Pmopm8CtrlCurrentGwReset_Type = EkiOnOff
_Pmopm8CtrlCurrentGwReset_Object = MibScalar
pmopm8CtrlCurrentGwReset = _Pmopm8CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 6, 1),
    _Pmopm8CtrlCurrentGwReset_Type()
)
pmopm8CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlCurrentGwReset.setStatus("current")
_Pmopm8CtrlLoadGwBank1_Type = EkiOnOff
_Pmopm8CtrlLoadGwBank1_Object = MibScalar
pmopm8CtrlLoadGwBank1 = _Pmopm8CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 6, 5),
    _Pmopm8CtrlLoadGwBank1_Type()
)
pmopm8CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlLoadGwBank1.setStatus("current")
_Pmopm8CtrlLoadGwBank2_Type = EkiOnOff
_Pmopm8CtrlLoadGwBank2_Object = MibScalar
pmopm8CtrlLoadGwBank2 = _Pmopm8CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 6, 6),
    _Pmopm8CtrlLoadGwBank2_Type()
)
pmopm8CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlLoadGwBank2.setStatus("current")
_Pmopm8CtrlLoadGwBank3_Type = EkiOnOff
_Pmopm8CtrlLoadGwBank3_Object = MibScalar
pmopm8CtrlLoadGwBank3 = _Pmopm8CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 6, 7),
    _Pmopm8CtrlLoadGwBank3_Type()
)
pmopm8CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlLoadGwBank3.setStatus("current")
_Pmopm8CtrlLoadGwBank4_Type = EkiOnOff
_Pmopm8CtrlLoadGwBank4_Object = MibScalar
pmopm8CtrlLoadGwBank4 = _Pmopm8CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 6, 8),
    _Pmopm8CtrlLoadGwBank4_Type()
)
pmopm8CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlLoadGwBank4.setStatus("current")
_Pmopm8CtrlledTest_ObjectIdentity = ObjectIdentity
pmopm8CtrlledTest = _Pmopm8CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 192)
)
_Pmopm8CtrlGreenLed_Type = EkiOnOff
_Pmopm8CtrlGreenLed_Object = MibScalar
pmopm8CtrlGreenLed = _Pmopm8CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 192, 1),
    _Pmopm8CtrlGreenLed_Type()
)
pmopm8CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlGreenLed.setStatus("current")
_Pmopm8CtrlRedLed_Type = EkiOnOff
_Pmopm8CtrlRedLed_Object = MibScalar
pmopm8CtrlRedLed = _Pmopm8CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 192, 2),
    _Pmopm8CtrlRedLed_Type()
)
pmopm8CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlRedLed.setStatus("current")
_Pmopm8CtrlLedOff_Type = EkiOnOff
_Pmopm8CtrlLedOff_Object = MibScalar
pmopm8CtrlLedOff = _Pmopm8CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 1, 192, 3),
    _Pmopm8CtrlLedOff_Type()
)
pmopm8CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlLedOff.setStatus("current")
_Pmopm8CtrlClient_ObjectIdentity = ObjectIdentity
pmopm8CtrlClient = _Pmopm8CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2)
)
_Pmopm8CtrlcalibrationTable_Object = MibTable
pmopm8CtrlcalibrationTable = _Pmopm8CtrlcalibrationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pmopm8CtrlcalibrationTable.setStatus("current")
_Pmopm8CtrlcalibrationEntry_Object = MibTableRow
pmopm8CtrlcalibrationEntry = _Pmopm8CtrlcalibrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 16, 1)
)
pmopm8CtrlcalibrationEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CtrlcalibrationIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CtrlcalibrationEntry.setStatus("current")


class _Pmopm8CtrlcalibrationIndex_Type(Integer32):
    """Custom type pmopm8CtrlcalibrationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CtrlcalibrationIndex_Type.__name__ = "Integer32"
_Pmopm8CtrlcalibrationIndex_Object = MibTableColumn
pmopm8CtrlcalibrationIndex = _Pmopm8CtrlcalibrationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 16, 1, 1),
    _Pmopm8CtrlcalibrationIndex_Type()
)
pmopm8CtrlcalibrationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CtrlcalibrationIndex.setStatus("current")
_Pmopm8CtrlcalibrationPortn_Type = EkiState
_Pmopm8CtrlcalibrationPortn_Object = MibTableColumn
pmopm8CtrlcalibrationPortn = _Pmopm8CtrlcalibrationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 16, 1, 2),
    _Pmopm8CtrlcalibrationPortn_Type()
)
pmopm8CtrlcalibrationPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlcalibrationPortn.setStatus("current")
_Pmopm8CtrlspectrumAutodiscoveryTable_Object = MibTable
pmopm8CtrlspectrumAutodiscoveryTable = _Pmopm8CtrlspectrumAutodiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pmopm8CtrlspectrumAutodiscoveryTable.setStatus("current")
_Pmopm8CtrlspectrumAutodiscoveryEntry_Object = MibTableRow
pmopm8CtrlspectrumAutodiscoveryEntry = _Pmopm8CtrlspectrumAutodiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 17, 1)
)
pmopm8CtrlspectrumAutodiscoveryEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CtrlspectrumAutodiscoveryIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CtrlspectrumAutodiscoveryEntry.setStatus("current")


class _Pmopm8CtrlspectrumAutodiscoveryIndex_Type(Integer32):
    """Custom type pmopm8CtrlspectrumAutodiscoveryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CtrlspectrumAutodiscoveryIndex_Type.__name__ = "Integer32"
_Pmopm8CtrlspectrumAutodiscoveryIndex_Object = MibTableColumn
pmopm8CtrlspectrumAutodiscoveryIndex = _Pmopm8CtrlspectrumAutodiscoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 17, 1, 1),
    _Pmopm8CtrlspectrumAutodiscoveryIndex_Type()
)
pmopm8CtrlspectrumAutodiscoveryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CtrlspectrumAutodiscoveryIndex.setStatus("current")
_Pmopm8CtrlspectrumAutodiscoveryPortn_Type = EkiState
_Pmopm8CtrlspectrumAutodiscoveryPortn_Object = MibTableColumn
pmopm8CtrlspectrumAutodiscoveryPortn = _Pmopm8CtrlspectrumAutodiscoveryPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 17, 1, 2),
    _Pmopm8CtrlspectrumAutodiscoveryPortn_Type()
)
pmopm8CtrlspectrumAutodiscoveryPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlspectrumAutodiscoveryPortn.setStatus("current")
_Pmopm8CtrlthresholdsAutoconfigTable_Object = MibTable
pmopm8CtrlthresholdsAutoconfigTable = _Pmopm8CtrlthresholdsAutoconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pmopm8CtrlthresholdsAutoconfigTable.setStatus("current")
_Pmopm8CtrlthresholdsAutoconfigEntry_Object = MibTableRow
pmopm8CtrlthresholdsAutoconfigEntry = _Pmopm8CtrlthresholdsAutoconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 18, 1)
)
pmopm8CtrlthresholdsAutoconfigEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CtrlthresholdsAutoconfigIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CtrlthresholdsAutoconfigEntry.setStatus("current")


class _Pmopm8CtrlthresholdsAutoconfigIndex_Type(Integer32):
    """Custom type pmopm8CtrlthresholdsAutoconfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CtrlthresholdsAutoconfigIndex_Type.__name__ = "Integer32"
_Pmopm8CtrlthresholdsAutoconfigIndex_Object = MibTableColumn
pmopm8CtrlthresholdsAutoconfigIndex = _Pmopm8CtrlthresholdsAutoconfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 18, 1, 1),
    _Pmopm8CtrlthresholdsAutoconfigIndex_Type()
)
pmopm8CtrlthresholdsAutoconfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CtrlthresholdsAutoconfigIndex.setStatus("current")
_Pmopm8CtrlthresholdsAutoconfigPortn_Type = EkiState
_Pmopm8CtrlthresholdsAutoconfigPortn_Object = MibTableColumn
pmopm8CtrlthresholdsAutoconfigPortn = _Pmopm8CtrlthresholdsAutoconfigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 18, 1, 2),
    _Pmopm8CtrlthresholdsAutoconfigPortn_Type()
)
pmopm8CtrlthresholdsAutoconfigPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlthresholdsAutoconfigPortn.setStatus("current")
_Pmopm8CtrlpowerLossDeltaTable_Object = MibTable
pmopm8CtrlpowerLossDeltaTable = _Pmopm8CtrlpowerLossDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 32)
)
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLossDeltaTable.setStatus("current")
_Pmopm8CtrlpowerLossDeltaEntry_Object = MibTableRow
pmopm8CtrlpowerLossDeltaEntry = _Pmopm8CtrlpowerLossDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 32, 1)
)
pmopm8CtrlpowerLossDeltaEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CtrlpowerLossDeltaIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLossDeltaEntry.setStatus("current")


class _Pmopm8CtrlpowerLossDeltaIndex_Type(Integer32):
    """Custom type pmopm8CtrlpowerLossDeltaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CtrlpowerLossDeltaIndex_Type.__name__ = "Integer32"
_Pmopm8CtrlpowerLossDeltaIndex_Object = MibTableColumn
pmopm8CtrlpowerLossDeltaIndex = _Pmopm8CtrlpowerLossDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 32, 1, 1),
    _Pmopm8CtrlpowerLossDeltaIndex_Type()
)
pmopm8CtrlpowerLossDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLossDeltaIndex.setStatus("current")


class _Pmopm8CtrlpowerLossDeltaPortn_Type(Integer32):
    """Custom type pmopm8CtrlpowerLossDeltaPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8CtrlpowerLossDeltaPortn_Type.__name__ = "Integer32"
_Pmopm8CtrlpowerLossDeltaPortn_Object = MibTableColumn
pmopm8CtrlpowerLossDeltaPortn = _Pmopm8CtrlpowerLossDeltaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 32, 1, 2),
    _Pmopm8CtrlpowerLossDeltaPortn_Type()
)
pmopm8CtrlpowerLossDeltaPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLossDeltaPortn.setStatus("current")
_Pmopm8CtrlpowerHighDeltaTable_Object = MibTable
pmopm8CtrlpowerHighDeltaTable = _Pmopm8CtrlpowerHighDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 40)
)
if mibBuilder.loadTexts:
    pmopm8CtrlpowerHighDeltaTable.setStatus("current")
_Pmopm8CtrlpowerHighDeltaEntry_Object = MibTableRow
pmopm8CtrlpowerHighDeltaEntry = _Pmopm8CtrlpowerHighDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 40, 1)
)
pmopm8CtrlpowerHighDeltaEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CtrlpowerHighDeltaIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CtrlpowerHighDeltaEntry.setStatus("current")


class _Pmopm8CtrlpowerHighDeltaIndex_Type(Integer32):
    """Custom type pmopm8CtrlpowerHighDeltaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CtrlpowerHighDeltaIndex_Type.__name__ = "Integer32"
_Pmopm8CtrlpowerHighDeltaIndex_Object = MibTableColumn
pmopm8CtrlpowerHighDeltaIndex = _Pmopm8CtrlpowerHighDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 40, 1, 1),
    _Pmopm8CtrlpowerHighDeltaIndex_Type()
)
pmopm8CtrlpowerHighDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CtrlpowerHighDeltaIndex.setStatus("current")


class _Pmopm8CtrlpowerHighDeltaPortn_Type(Integer32):
    """Custom type pmopm8CtrlpowerHighDeltaPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8CtrlpowerHighDeltaPortn_Type.__name__ = "Integer32"
_Pmopm8CtrlpowerHighDeltaPortn_Object = MibTableColumn
pmopm8CtrlpowerHighDeltaPortn = _Pmopm8CtrlpowerHighDeltaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 40, 1, 2),
    _Pmopm8CtrlpowerHighDeltaPortn_Type()
)
pmopm8CtrlpowerHighDeltaPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlpowerHighDeltaPortn.setStatus("current")
_Pmopm8CtrlpowerLowDeltaTable_Object = MibTable
pmopm8CtrlpowerLowDeltaTable = _Pmopm8CtrlpowerLowDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 48)
)
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLowDeltaTable.setStatus("current")
_Pmopm8CtrlpowerLowDeltaEntry_Object = MibTableRow
pmopm8CtrlpowerLowDeltaEntry = _Pmopm8CtrlpowerLowDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 48, 1)
)
pmopm8CtrlpowerLowDeltaEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CtrlpowerLowDeltaIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLowDeltaEntry.setStatus("current")


class _Pmopm8CtrlpowerLowDeltaIndex_Type(Integer32):
    """Custom type pmopm8CtrlpowerLowDeltaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CtrlpowerLowDeltaIndex_Type.__name__ = "Integer32"
_Pmopm8CtrlpowerLowDeltaIndex_Object = MibTableColumn
pmopm8CtrlpowerLowDeltaIndex = _Pmopm8CtrlpowerLowDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 48, 1, 1),
    _Pmopm8CtrlpowerLowDeltaIndex_Type()
)
pmopm8CtrlpowerLowDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLowDeltaIndex.setStatus("current")


class _Pmopm8CtrlpowerLowDeltaPortn_Type(Integer32):
    """Custom type pmopm8CtrlpowerLowDeltaPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8CtrlpowerLowDeltaPortn_Type.__name__ = "Integer32"
_Pmopm8CtrlpowerLowDeltaPortn_Object = MibTableColumn
pmopm8CtrlpowerLowDeltaPortn = _Pmopm8CtrlpowerLowDeltaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 48, 1, 2),
    _Pmopm8CtrlpowerLowDeltaPortn_Type()
)
pmopm8CtrlpowerLowDeltaPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlpowerLowDeltaPortn.setStatus("current")
_Pmopm8CtrlinputPowerRefTable_Object = MibTable
pmopm8CtrlinputPowerRefTable = _Pmopm8CtrlinputPowerRefTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 64)
)
if mibBuilder.loadTexts:
    pmopm8CtrlinputPowerRefTable.setStatus("current")
_Pmopm8CtrlinputPowerRefEntry_Object = MibTableRow
pmopm8CtrlinputPowerRefEntry = _Pmopm8CtrlinputPowerRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 64, 1)
)
pmopm8CtrlinputPowerRefEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CtrlinputPowerRefIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CtrlinputPowerRefEntry.setStatus("current")


class _Pmopm8CtrlinputPowerRefIndex_Type(Integer32):
    """Custom type pmopm8CtrlinputPowerRefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CtrlinputPowerRefIndex_Type.__name__ = "Integer32"
_Pmopm8CtrlinputPowerRefIndex_Object = MibTableColumn
pmopm8CtrlinputPowerRefIndex = _Pmopm8CtrlinputPowerRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 64, 1, 1),
    _Pmopm8CtrlinputPowerRefIndex_Type()
)
pmopm8CtrlinputPowerRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CtrlinputPowerRefIndex.setStatus("current")


class _Pmopm8CtrlinputPowerRefPortn_Type(Integer32):
    """Custom type pmopm8CtrlinputPowerRefPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm8CtrlinputPowerRefPortn_Type.__name__ = "Integer32"
_Pmopm8CtrlinputPowerRefPortn_Object = MibTableColumn
pmopm8CtrlinputPowerRefPortn = _Pmopm8CtrlinputPowerRefPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 2, 64, 1, 2),
    _Pmopm8CtrlinputPowerRefPortn_Type()
)
pmopm8CtrlinputPowerRefPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CtrlinputPowerRefPortn.setStatus("current")
_Pmopm8CtrlLine_ObjectIdentity = ObjectIdentity
pmopm8CtrlLine = _Pmopm8CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 6, 3)
)
_Pmopm8ri_ObjectIdentity = ObjectIdentity
pmopm8ri = _Pmopm8ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7)
)
_Pmopm8riTable_ObjectIdentity = ObjectIdentity
pmopm8riTable = _Pmopm8riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1)
)
_Pmopm8RinvSfpTable_Object = MibTable
pmopm8RinvSfpTable = _Pmopm8RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmopm8RinvSfpTable.setStatus("current")
_Pmopm8RinvSfpEntry_Object = MibTableRow
pmopm8RinvSfpEntry = _Pmopm8RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 1, 1)
)
pmopm8RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pmopm8RinvSfpEntry.setStatus("current")


class _Pmopm8RinvSfpIndex_Type(Integer32):
    """Custom type pmopm8RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmopm8RinvSfpIndex_Type.__name__ = "Integer32"
_Pmopm8RinvSfpIndex_Object = MibTableColumn
pmopm8RinvSfpIndex = _Pmopm8RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 1, 1, 1),
    _Pmopm8RinvSfpIndex_Type()
)
pmopm8RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8RinvSfpIndex.setStatus("current")
_Pmopm8Rinvsfp_Type = DisplayString
_Pmopm8Rinvsfp_Object = MibTableColumn
pmopm8Rinvsfp = _Pmopm8Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 1, 1, 2),
    _Pmopm8Rinvsfp_Type()
)
pmopm8Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Rinvsfp.setStatus("current")
_Pmopm8RinvLineTable_Object = MibTable
pmopm8RinvLineTable = _Pmopm8RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmopm8RinvLineTable.setStatus("current")
_Pmopm8RinvLineEntry_Object = MibTableRow
pmopm8RinvLineEntry = _Pmopm8RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 2, 1)
)
pmopm8RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmopm8RinvLineEntry.setStatus("current")


class _Pmopm8RinvLineIndex_Type(Integer32):
    """Custom type pmopm8RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmopm8RinvLineIndex_Type.__name__ = "Integer32"
_Pmopm8RinvLineIndex_Object = MibTableColumn
pmopm8RinvLineIndex = _Pmopm8RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 2, 1, 1),
    _Pmopm8RinvLineIndex_Type()
)
pmopm8RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8RinvLineIndex.setStatus("current")
_Pmopm8RinvxfpLine_Type = DisplayString
_Pmopm8RinvxfpLine_Object = MibTableColumn
pmopm8RinvxfpLine = _Pmopm8RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 1, 2, 1, 2),
    _Pmopm8RinvxfpLine_Type()
)
pmopm8RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8RinvxfpLine.setStatus("current")
_Pmopm8RinvReloadInventory_Type = EkiOnOff
_Pmopm8RinvReloadInventory_Object = MibScalar
pmopm8RinvReloadInventory = _Pmopm8RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 2),
    _Pmopm8RinvReloadInventory_Type()
)
pmopm8RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8RinvReloadInventory.setStatus("current")
_Pmopm8RinvHwPlatform_Type = DisplayString
_Pmopm8RinvHwPlatform_Object = MibScalar
pmopm8RinvHwPlatform = _Pmopm8RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 3),
    _Pmopm8RinvHwPlatform_Type()
)
pmopm8RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8RinvHwPlatform.setStatus("current")
_Pmopm8RinvModulePlatform_Type = DisplayString
_Pmopm8RinvModulePlatform_Object = MibScalar
pmopm8RinvModulePlatform = _Pmopm8RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 4),
    _Pmopm8RinvModulePlatform_Type()
)
pmopm8RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8RinvModulePlatform.setStatus("current")
_Pmopm8RinvSwPlatform_Type = DisplayString
_Pmopm8RinvSwPlatform_Object = MibScalar
pmopm8RinvSwPlatform = _Pmopm8RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 5),
    _Pmopm8RinvSwPlatform_Type()
)
pmopm8RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8RinvSwPlatform.setStatus("current")
_Pmopm8RinvGwPlatform_Type = DisplayString
_Pmopm8RinvGwPlatform_Object = MibScalar
pmopm8RinvGwPlatform = _Pmopm8RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 7, 6),
    _Pmopm8RinvGwPlatform_Type()
)
pmopm8RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8RinvGwPlatform.setStatus("current")
_Pmopm8download_ObjectIdentity = ObjectIdentity
pmopm8download = _Pmopm8download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8)
)
_Pmopm8DwlOther_ObjectIdentity = ObjectIdentity
pmopm8DwlOther = _Pmopm8DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1)
)
_Pmopm8DwlrestartProcess_ObjectIdentity = ObjectIdentity
pmopm8DwlrestartProcess = _Pmopm8DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 0)
)
_Pmopm8DwlWarmRestartProcessed_Type = EkiOnOff
_Pmopm8DwlWarmRestartProcessed_Object = MibScalar
pmopm8DwlWarmRestartProcessed = _Pmopm8DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 0, 1),
    _Pmopm8DwlWarmRestartProcessed_Type()
)
pmopm8DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlWarmRestartProcessed.setStatus("current")
_Pmopm8DwlColdRestartProcessed_Type = EkiOnOff
_Pmopm8DwlColdRestartProcessed_Object = MibScalar
pmopm8DwlColdRestartProcessed = _Pmopm8DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 0, 2),
    _Pmopm8DwlColdRestartProcessed_Type()
)
pmopm8DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlColdRestartProcessed.setStatus("current")
_Pmopm8DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmopm8DwlswBanksUsed = _Pmopm8DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 1)
)
_Pmopm8DwlSwBank1Used_Type = EkiOnOff
_Pmopm8DwlSwBank1Used_Object = MibScalar
pmopm8DwlSwBank1Used = _Pmopm8DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 1, 1),
    _Pmopm8DwlSwBank1Used_Type()
)
pmopm8DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlSwBank1Used.setStatus("current")
_Pmopm8DwlSwBank2Used_Type = EkiOnOff
_Pmopm8DwlSwBank2Used_Object = MibScalar
pmopm8DwlSwBank2Used = _Pmopm8DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 1, 2),
    _Pmopm8DwlSwBank2Used_Type()
)
pmopm8DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlSwBank2Used.setStatus("current")
_Pmopm8DwlSwBank1Notempty_Type = EkiOnOff
_Pmopm8DwlSwBank1Notempty_Object = MibScalar
pmopm8DwlSwBank1Notempty = _Pmopm8DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 1, 5),
    _Pmopm8DwlSwBank1Notempty_Type()
)
pmopm8DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlSwBank1Notempty.setStatus("current")
_Pmopm8DwlSwBank2Notempty_Type = EkiOnOff
_Pmopm8DwlSwBank2Notempty_Object = MibScalar
pmopm8DwlSwBank2Notempty = _Pmopm8DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 1, 6),
    _Pmopm8DwlSwBank2Notempty_Type()
)
pmopm8DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlSwBank2Notempty.setStatus("current")
_Pmopm8DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmopm8DwlgwBanksUsed = _Pmopm8DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2)
)
_Pmopm8DwlGwBank1Used_Type = EkiOnOff
_Pmopm8DwlGwBank1Used_Object = MibScalar
pmopm8DwlGwBank1Used = _Pmopm8DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 1),
    _Pmopm8DwlGwBank1Used_Type()
)
pmopm8DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank1Used.setStatus("current")
_Pmopm8DwlGwBank2Used_Type = EkiOnOff
_Pmopm8DwlGwBank2Used_Object = MibScalar
pmopm8DwlGwBank2Used = _Pmopm8DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 2),
    _Pmopm8DwlGwBank2Used_Type()
)
pmopm8DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank2Used.setStatus("current")
_Pmopm8DwlGwBank3Used_Type = EkiOnOff
_Pmopm8DwlGwBank3Used_Object = MibScalar
pmopm8DwlGwBank3Used = _Pmopm8DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 3),
    _Pmopm8DwlGwBank3Used_Type()
)
pmopm8DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank3Used.setStatus("current")
_Pmopm8DwlGwBank4Used_Type = EkiOnOff
_Pmopm8DwlGwBank4Used_Object = MibScalar
pmopm8DwlGwBank4Used = _Pmopm8DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 4),
    _Pmopm8DwlGwBank4Used_Type()
)
pmopm8DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank4Used.setStatus("current")
_Pmopm8DwlGwBank1Notempty_Type = EkiOnOff
_Pmopm8DwlGwBank1Notempty_Object = MibScalar
pmopm8DwlGwBank1Notempty = _Pmopm8DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 5),
    _Pmopm8DwlGwBank1Notempty_Type()
)
pmopm8DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank1Notempty.setStatus("current")
_Pmopm8DwlGwBank2Notempty_Type = EkiOnOff
_Pmopm8DwlGwBank2Notempty_Object = MibScalar
pmopm8DwlGwBank2Notempty = _Pmopm8DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 6),
    _Pmopm8DwlGwBank2Notempty_Type()
)
pmopm8DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank2Notempty.setStatus("current")
_Pmopm8DwlGwBank3Notempty_Type = EkiOnOff
_Pmopm8DwlGwBank3Notempty_Object = MibScalar
pmopm8DwlGwBank3Notempty = _Pmopm8DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 7),
    _Pmopm8DwlGwBank3Notempty_Type()
)
pmopm8DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank3Notempty.setStatus("current")
_Pmopm8DwlGwBank4Notempty_Type = EkiOnOff
_Pmopm8DwlGwBank4Notempty_Object = MibScalar
pmopm8DwlGwBank4Notempty = _Pmopm8DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 1, 2, 8),
    _Pmopm8DwlGwBank4Notempty_Type()
)
pmopm8DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8DwlGwBank4Notempty.setStatus("current")
_Pmopm8DwlClient_ObjectIdentity = ObjectIdentity
pmopm8DwlClient = _Pmopm8DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 2)
)
_Pmopm8DwlLine_ObjectIdentity = ObjectIdentity
pmopm8DwlLine = _Pmopm8DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 8, 3)
)
_Pmopm8Config_ObjectIdentity = ObjectIdentity
pmopm8Config = _Pmopm8Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9)
)
_Pmopm8CfgLsd_ObjectIdentity = ObjectIdentity
pmopm8CfgLsd = _Pmopm8CfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 1)
)
_Pmopm8tableclientcaiscsf_ObjectIdentity = ObjectIdentity
pmopm8tableclientcaiscsf = _Pmopm8tableclientcaiscsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 1, 1)
)
_Pmopm8CfgStartup_ObjectIdentity = ObjectIdentity
pmopm8CfgStartup = _Pmopm8CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2)
)
_Pmopm8tableother_ObjectIdentity = ObjectIdentity
pmopm8tableother = _Pmopm8tableother_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 1)
)


class _Pmopm8CfgcomponentType_Type(Unsigned32):
    """Custom type pmopm8CfgcomponentType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgcomponentType_Type.__name__ = "Unsigned32"
_Pmopm8CfgcomponentType_Object = MibScalar
pmopm8CfgcomponentType = _Pmopm8CfgcomponentType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 1, 2),
    _Pmopm8CfgcomponentType_Type()
)
pmopm8CfgcomponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgcomponentType.setStatus("current")


class _Pmopm8Cfgmiscellaneous_Type(Unsigned32):
    """Custom type pmopm8Cfgmiscellaneous based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8Cfgmiscellaneous_Type.__name__ = "Unsigned32"
_Pmopm8Cfgmiscellaneous_Object = MibScalar
pmopm8Cfgmiscellaneous = _Pmopm8Cfgmiscellaneous_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 1, 3),
    _Pmopm8Cfgmiscellaneous_Type()
)
pmopm8Cfgmiscellaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Cfgmiscellaneous.setStatus("current")


class _Pmopm8CfgfirstChannel_Type(Unsigned32):
    """Custom type pmopm8CfgfirstChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgfirstChannel_Type.__name__ = "Unsigned32"
_Pmopm8CfgfirstChannel_Object = MibScalar
pmopm8CfgfirstChannel = _Pmopm8CfgfirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 1, 4),
    _Pmopm8CfgfirstChannel_Type()
)
pmopm8CfgfirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgfirstChannel.setStatus("current")


class _Pmopm8CfglastChannel_Type(Unsigned32):
    """Custom type pmopm8CfglastChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfglastChannel_Type.__name__ = "Unsigned32"
_Pmopm8CfglastChannel_Object = MibScalar
pmopm8CfglastChannel = _Pmopm8CfglastChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 1, 5),
    _Pmopm8CfglastChannel_Type()
)
pmopm8CfglastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfglastChannel.setStatus("current")


class _Pmopm8Cfggrid_Type(Unsigned32):
    """Custom type pmopm8Cfggrid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8Cfggrid_Type.__name__ = "Unsigned32"
_Pmopm8Cfggrid_Object = MibScalar
pmopm8Cfggrid = _Pmopm8Cfggrid_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 1, 6),
    _Pmopm8Cfggrid_Type()
)
pmopm8Cfggrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8Cfggrid.setStatus("current")
_Pmopm8CfgClientStartupOosTable_Object = MibTable
pmopm8CfgClientStartupOosTable = _Pmopm8CfgClientStartupOosTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupOosTable.setStatus("current")
_Pmopm8CfgClientStartupOosEntry_Object = MibTableRow
pmopm8CfgClientStartupOosEntry = _Pmopm8CfgClientStartupOosEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1)
)
pmopm8CfgClientStartupOosEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CfgClientStartupOosIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupOosEntry.setStatus("current")


class _Pmopm8CfgClientStartupOosIndex_Type(Integer32):
    """Custom type pmopm8CfgClientStartupOosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CfgClientStartupOosIndex_Type.__name__ = "Integer32"
_Pmopm8CfgClientStartupOosIndex_Object = MibTableColumn
pmopm8CfgClientStartupOosIndex = _Pmopm8CfgClientStartupOosIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 1),
    _Pmopm8CfgClientStartupOosIndex_Type()
)
pmopm8CfgClientStartupOosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupOosIndex.setStatus("current")


class _Pmopm8CfgSpectrumOosPortn_Type(Unsigned32):
    """Custom type pmopm8CfgSpectrumOosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgSpectrumOosPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgSpectrumOosPortn_Object = MibTableColumn
pmopm8CfgSpectrumOosPortn = _Pmopm8CfgSpectrumOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 3),
    _Pmopm8CfgSpectrumOosPortn_Type()
)
pmopm8CfgSpectrumOosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgSpectrumOosPortn.setStatus("current")


class _Pmopm8CfgSpectrumOffsetPortn_Type(Unsigned32):
    """Custom type pmopm8CfgSpectrumOffsetPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgSpectrumOffsetPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgSpectrumOffsetPortn_Object = MibTableColumn
pmopm8CfgSpectrumOffsetPortn = _Pmopm8CfgSpectrumOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 4),
    _Pmopm8CfgSpectrumOffsetPortn_Type()
)
pmopm8CfgSpectrumOffsetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgSpectrumOffsetPortn.setStatus("current")


class _Pmopm8CfgCh1Ch16OosPortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh1Ch16OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh1Ch16OosPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh1Ch16OosPortn_Object = MibTableColumn
pmopm8CfgCh1Ch16OosPortn = _Pmopm8CfgCh1Ch16OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 5),
    _Pmopm8CfgCh1Ch16OosPortn_Type()
)
pmopm8CfgCh1Ch16OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh1Ch16OosPortn.setStatus("current")


class _Pmopm8CfgCh17Ch32OosPortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh17Ch32OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh17Ch32OosPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh17Ch32OosPortn_Object = MibTableColumn
pmopm8CfgCh17Ch32OosPortn = _Pmopm8CfgCh17Ch32OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 6),
    _Pmopm8CfgCh17Ch32OosPortn_Type()
)
pmopm8CfgCh17Ch32OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh17Ch32OosPortn.setStatus("current")


class _Pmopm8CfgCh33Ch48OosPortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh33Ch48OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh33Ch48OosPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh33Ch48OosPortn_Object = MibTableColumn
pmopm8CfgCh33Ch48OosPortn = _Pmopm8CfgCh33Ch48OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 7),
    _Pmopm8CfgCh33Ch48OosPortn_Type()
)
pmopm8CfgCh33Ch48OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh33Ch48OosPortn.setStatus("current")


class _Pmopm8CfgCh49Ch64OosPortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh49Ch64OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh49Ch64OosPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh49Ch64OosPortn_Object = MibTableColumn
pmopm8CfgCh49Ch64OosPortn = _Pmopm8CfgCh49Ch64OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 8),
    _Pmopm8CfgCh49Ch64OosPortn_Type()
)
pmopm8CfgCh49Ch64OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh49Ch64OosPortn.setStatus("current")


class _Pmopm8CfgCh65Ch80OosPortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh65Ch80OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh65Ch80OosPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh65Ch80OosPortn_Object = MibTableColumn
pmopm8CfgCh65Ch80OosPortn = _Pmopm8CfgCh65Ch80OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 9),
    _Pmopm8CfgCh65Ch80OosPortn_Type()
)
pmopm8CfgCh65Ch80OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh65Ch80OosPortn.setStatus("current")


class _Pmopm8CfgCh81Ch96OosPortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh81Ch96OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh81Ch96OosPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh81Ch96OosPortn_Object = MibTableColumn
pmopm8CfgCh81Ch96OosPortn = _Pmopm8CfgCh81Ch96OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 2, 1, 10),
    _Pmopm8CfgCh81Ch96OosPortn_Type()
)
pmopm8CfgCh81Ch96OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh81Ch96OosPortn.setStatus("current")
_Pmopm8CfgClientStartupBalanceTable_Object = MibTable
pmopm8CfgClientStartupBalanceTable = _Pmopm8CfgClientStartupBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupBalanceTable.setStatus("current")
_Pmopm8CfgClientStartupBalanceEntry_Object = MibTableRow
pmopm8CfgClientStartupBalanceEntry = _Pmopm8CfgClientStartupBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1)
)
pmopm8CfgClientStartupBalanceEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CfgClientStartupBalanceIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupBalanceEntry.setStatus("current")


class _Pmopm8CfgClientStartupBalanceIndex_Type(Integer32):
    """Custom type pmopm8CfgClientStartupBalanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CfgClientStartupBalanceIndex_Type.__name__ = "Integer32"
_Pmopm8CfgClientStartupBalanceIndex_Object = MibTableColumn
pmopm8CfgClientStartupBalanceIndex = _Pmopm8CfgClientStartupBalanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1, 1),
    _Pmopm8CfgClientStartupBalanceIndex_Type()
)
pmopm8CfgClientStartupBalanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupBalanceIndex.setStatus("current")


class _Pmopm8CfgCh1Ch16BalancePortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh1Ch16BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh1Ch16BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh1Ch16BalancePortn_Object = MibTableColumn
pmopm8CfgCh1Ch16BalancePortn = _Pmopm8CfgCh1Ch16BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1, 3),
    _Pmopm8CfgCh1Ch16BalancePortn_Type()
)
pmopm8CfgCh1Ch16BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh1Ch16BalancePortn.setStatus("current")


class _Pmopm8CfgCh17Ch32BalancePortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh17Ch32BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh17Ch32BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh17Ch32BalancePortn_Object = MibTableColumn
pmopm8CfgCh17Ch32BalancePortn = _Pmopm8CfgCh17Ch32BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1, 4),
    _Pmopm8CfgCh17Ch32BalancePortn_Type()
)
pmopm8CfgCh17Ch32BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh17Ch32BalancePortn.setStatus("current")


class _Pmopm8CfgCh33Ch48BalancePortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh33Ch48BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh33Ch48BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh33Ch48BalancePortn_Object = MibTableColumn
pmopm8CfgCh33Ch48BalancePortn = _Pmopm8CfgCh33Ch48BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1, 5),
    _Pmopm8CfgCh33Ch48BalancePortn_Type()
)
pmopm8CfgCh33Ch48BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh33Ch48BalancePortn.setStatus("current")


class _Pmopm8CfgCh49Ch64BalancePortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh49Ch64BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh49Ch64BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh49Ch64BalancePortn_Object = MibTableColumn
pmopm8CfgCh49Ch64BalancePortn = _Pmopm8CfgCh49Ch64BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1, 6),
    _Pmopm8CfgCh49Ch64BalancePortn_Type()
)
pmopm8CfgCh49Ch64BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh49Ch64BalancePortn.setStatus("current")


class _Pmopm8CfgCh65Ch80BalancePortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh65Ch80BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh65Ch80BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh65Ch80BalancePortn_Object = MibTableColumn
pmopm8CfgCh65Ch80BalancePortn = _Pmopm8CfgCh65Ch80BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1, 7),
    _Pmopm8CfgCh65Ch80BalancePortn_Type()
)
pmopm8CfgCh65Ch80BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh65Ch80BalancePortn.setStatus("current")


class _Pmopm8CfgCh81Ch96BalancePortn_Type(Unsigned32):
    """Custom type pmopm8CfgCh81Ch96BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgCh81Ch96BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgCh81Ch96BalancePortn_Object = MibTableColumn
pmopm8CfgCh81Ch96BalancePortn = _Pmopm8CfgCh81Ch96BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 3, 1, 8),
    _Pmopm8CfgCh81Ch96BalancePortn_Type()
)
pmopm8CfgCh81Ch96BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgCh81Ch96BalancePortn.setStatus("current")
_Pmopm8CfgClientStartupAbsthreshTable_Object = MibTable
pmopm8CfgClientStartupAbsthreshTable = _Pmopm8CfgClientStartupAbsthreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4)
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupAbsthreshTable.setStatus("current")
_Pmopm8CfgClientStartupAbsthreshEntry_Object = MibTableRow
pmopm8CfgClientStartupAbsthreshEntry = _Pmopm8CfgClientStartupAbsthreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1)
)
pmopm8CfgClientStartupAbsthreshEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CfgClientStartupAbsthreshIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupAbsthreshEntry.setStatus("current")


class _Pmopm8CfgClientStartupAbsthreshIndex_Type(Integer32):
    """Custom type pmopm8CfgClientStartupAbsthreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CfgClientStartupAbsthreshIndex_Type.__name__ = "Integer32"
_Pmopm8CfgClientStartupAbsthreshIndex_Object = MibTableColumn
pmopm8CfgClientStartupAbsthreshIndex = _Pmopm8CfgClientStartupAbsthreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 1),
    _Pmopm8CfgClientStartupAbsthreshIndex_Type()
)
pmopm8CfgClientStartupAbsthreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupAbsthreshIndex.setStatus("current")


class _Pmopm8CfgChannel1AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel1AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel1AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel1AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel1AbsthreshPortn = _Pmopm8CfgChannel1AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 3),
    _Pmopm8CfgChannel1AbsthreshPortn_Type()
)
pmopm8CfgChannel1AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel1AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel2AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel2AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel2AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel2AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel2AbsthreshPortn = _Pmopm8CfgChannel2AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 4),
    _Pmopm8CfgChannel2AbsthreshPortn_Type()
)
pmopm8CfgChannel2AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel2AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel3AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel3AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel3AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel3AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel3AbsthreshPortn = _Pmopm8CfgChannel3AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 5),
    _Pmopm8CfgChannel3AbsthreshPortn_Type()
)
pmopm8CfgChannel3AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel3AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel4AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel4AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel4AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel4AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel4AbsthreshPortn = _Pmopm8CfgChannel4AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 6),
    _Pmopm8CfgChannel4AbsthreshPortn_Type()
)
pmopm8CfgChannel4AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel4AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel5AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel5AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel5AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel5AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel5AbsthreshPortn = _Pmopm8CfgChannel5AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 7),
    _Pmopm8CfgChannel5AbsthreshPortn_Type()
)
pmopm8CfgChannel5AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel5AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel6AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel6AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel6AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel6AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel6AbsthreshPortn = _Pmopm8CfgChannel6AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 8),
    _Pmopm8CfgChannel6AbsthreshPortn_Type()
)
pmopm8CfgChannel6AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel6AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel7AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel7AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel7AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel7AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel7AbsthreshPortn = _Pmopm8CfgChannel7AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 9),
    _Pmopm8CfgChannel7AbsthreshPortn_Type()
)
pmopm8CfgChannel7AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel7AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel8AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel8AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel8AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel8AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel8AbsthreshPortn = _Pmopm8CfgChannel8AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 10),
    _Pmopm8CfgChannel8AbsthreshPortn_Type()
)
pmopm8CfgChannel8AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel8AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel9AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel9AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel9AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel9AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel9AbsthreshPortn = _Pmopm8CfgChannel9AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 11),
    _Pmopm8CfgChannel9AbsthreshPortn_Type()
)
pmopm8CfgChannel9AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel9AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel10AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel10AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel10AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel10AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel10AbsthreshPortn = _Pmopm8CfgChannel10AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 12),
    _Pmopm8CfgChannel10AbsthreshPortn_Type()
)
pmopm8CfgChannel10AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel10AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel11AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel11AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel11AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel11AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel11AbsthreshPortn = _Pmopm8CfgChannel11AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 13),
    _Pmopm8CfgChannel11AbsthreshPortn_Type()
)
pmopm8CfgChannel11AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel11AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel12AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel12AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel12AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel12AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel12AbsthreshPortn = _Pmopm8CfgChannel12AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 14),
    _Pmopm8CfgChannel12AbsthreshPortn_Type()
)
pmopm8CfgChannel12AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel12AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel13AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel13AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel13AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel13AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel13AbsthreshPortn = _Pmopm8CfgChannel13AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 15),
    _Pmopm8CfgChannel13AbsthreshPortn_Type()
)
pmopm8CfgChannel13AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel13AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel14AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel14AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel14AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel14AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel14AbsthreshPortn = _Pmopm8CfgChannel14AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 16),
    _Pmopm8CfgChannel14AbsthreshPortn_Type()
)
pmopm8CfgChannel14AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel14AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel15AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel15AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel15AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel15AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel15AbsthreshPortn = _Pmopm8CfgChannel15AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 17),
    _Pmopm8CfgChannel15AbsthreshPortn_Type()
)
pmopm8CfgChannel15AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel15AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel16AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel16AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel16AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel16AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel16AbsthreshPortn = _Pmopm8CfgChannel16AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 18),
    _Pmopm8CfgChannel16AbsthreshPortn_Type()
)
pmopm8CfgChannel16AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel16AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel17AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel17AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel17AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel17AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel17AbsthreshPortn = _Pmopm8CfgChannel17AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 19),
    _Pmopm8CfgChannel17AbsthreshPortn_Type()
)
pmopm8CfgChannel17AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel17AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel18AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel18AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel18AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel18AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel18AbsthreshPortn = _Pmopm8CfgChannel18AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 20),
    _Pmopm8CfgChannel18AbsthreshPortn_Type()
)
pmopm8CfgChannel18AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel18AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel19AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel19AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel19AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel19AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel19AbsthreshPortn = _Pmopm8CfgChannel19AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 21),
    _Pmopm8CfgChannel19AbsthreshPortn_Type()
)
pmopm8CfgChannel19AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel19AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel20AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel20AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel20AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel20AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel20AbsthreshPortn = _Pmopm8CfgChannel20AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 22),
    _Pmopm8CfgChannel20AbsthreshPortn_Type()
)
pmopm8CfgChannel20AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel20AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel21AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel21AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel21AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel21AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel21AbsthreshPortn = _Pmopm8CfgChannel21AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 23),
    _Pmopm8CfgChannel21AbsthreshPortn_Type()
)
pmopm8CfgChannel21AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel21AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel22AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel22AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel22AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel22AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel22AbsthreshPortn = _Pmopm8CfgChannel22AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 24),
    _Pmopm8CfgChannel22AbsthreshPortn_Type()
)
pmopm8CfgChannel22AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel22AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel23AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel23AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel23AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel23AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel23AbsthreshPortn = _Pmopm8CfgChannel23AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 25),
    _Pmopm8CfgChannel23AbsthreshPortn_Type()
)
pmopm8CfgChannel23AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel23AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel24AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel24AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel24AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel24AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel24AbsthreshPortn = _Pmopm8CfgChannel24AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 26),
    _Pmopm8CfgChannel24AbsthreshPortn_Type()
)
pmopm8CfgChannel24AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel24AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel25AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel25AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel25AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel25AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel25AbsthreshPortn = _Pmopm8CfgChannel25AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 27),
    _Pmopm8CfgChannel25AbsthreshPortn_Type()
)
pmopm8CfgChannel25AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel25AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel26AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel26AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel26AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel26AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel26AbsthreshPortn = _Pmopm8CfgChannel26AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 28),
    _Pmopm8CfgChannel26AbsthreshPortn_Type()
)
pmopm8CfgChannel26AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel26AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel27AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel27AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel27AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel27AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel27AbsthreshPortn = _Pmopm8CfgChannel27AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 29),
    _Pmopm8CfgChannel27AbsthreshPortn_Type()
)
pmopm8CfgChannel27AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel27AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel28AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel28AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel28AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel28AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel28AbsthreshPortn = _Pmopm8CfgChannel28AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 30),
    _Pmopm8CfgChannel28AbsthreshPortn_Type()
)
pmopm8CfgChannel28AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel28AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel29AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel29AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel29AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel29AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel29AbsthreshPortn = _Pmopm8CfgChannel29AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 31),
    _Pmopm8CfgChannel29AbsthreshPortn_Type()
)
pmopm8CfgChannel29AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel29AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel30AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel30AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel30AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel30AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel30AbsthreshPortn = _Pmopm8CfgChannel30AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 32),
    _Pmopm8CfgChannel30AbsthreshPortn_Type()
)
pmopm8CfgChannel30AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel30AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel31AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel31AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel31AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel31AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel31AbsthreshPortn = _Pmopm8CfgChannel31AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 33),
    _Pmopm8CfgChannel31AbsthreshPortn_Type()
)
pmopm8CfgChannel31AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel31AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel32AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel32AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel32AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel32AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel32AbsthreshPortn = _Pmopm8CfgChannel32AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 34),
    _Pmopm8CfgChannel32AbsthreshPortn_Type()
)
pmopm8CfgChannel32AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel32AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel33AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel33AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel33AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel33AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel33AbsthreshPortn = _Pmopm8CfgChannel33AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 35),
    _Pmopm8CfgChannel33AbsthreshPortn_Type()
)
pmopm8CfgChannel33AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel33AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel34AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel34AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel34AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel34AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel34AbsthreshPortn = _Pmopm8CfgChannel34AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 36),
    _Pmopm8CfgChannel34AbsthreshPortn_Type()
)
pmopm8CfgChannel34AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel34AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel35AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel35AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel35AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel35AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel35AbsthreshPortn = _Pmopm8CfgChannel35AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 37),
    _Pmopm8CfgChannel35AbsthreshPortn_Type()
)
pmopm8CfgChannel35AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel35AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel36AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel36AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel36AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel36AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel36AbsthreshPortn = _Pmopm8CfgChannel36AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 38),
    _Pmopm8CfgChannel36AbsthreshPortn_Type()
)
pmopm8CfgChannel36AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel36AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel37AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel37AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel37AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel37AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel37AbsthreshPortn = _Pmopm8CfgChannel37AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 39),
    _Pmopm8CfgChannel37AbsthreshPortn_Type()
)
pmopm8CfgChannel37AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel37AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel38AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel38AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel38AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel38AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel38AbsthreshPortn = _Pmopm8CfgChannel38AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 40),
    _Pmopm8CfgChannel38AbsthreshPortn_Type()
)
pmopm8CfgChannel38AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel38AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel39AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel39AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel39AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel39AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel39AbsthreshPortn = _Pmopm8CfgChannel39AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 41),
    _Pmopm8CfgChannel39AbsthreshPortn_Type()
)
pmopm8CfgChannel39AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel39AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel40AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel40AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel40AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel40AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel40AbsthreshPortn = _Pmopm8CfgChannel40AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 42),
    _Pmopm8CfgChannel40AbsthreshPortn_Type()
)
pmopm8CfgChannel40AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel40AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel41AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel41AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel41AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel41AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel41AbsthreshPortn = _Pmopm8CfgChannel41AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 43),
    _Pmopm8CfgChannel41AbsthreshPortn_Type()
)
pmopm8CfgChannel41AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel41AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel42AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel42AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel42AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel42AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel42AbsthreshPortn = _Pmopm8CfgChannel42AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 44),
    _Pmopm8CfgChannel42AbsthreshPortn_Type()
)
pmopm8CfgChannel42AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel42AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel43AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel43AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel43AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel43AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel43AbsthreshPortn = _Pmopm8CfgChannel43AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 45),
    _Pmopm8CfgChannel43AbsthreshPortn_Type()
)
pmopm8CfgChannel43AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel43AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel44AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel44AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel44AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel44AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel44AbsthreshPortn = _Pmopm8CfgChannel44AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 46),
    _Pmopm8CfgChannel44AbsthreshPortn_Type()
)
pmopm8CfgChannel44AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel44AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel45AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel45AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel45AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel45AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel45AbsthreshPortn = _Pmopm8CfgChannel45AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 47),
    _Pmopm8CfgChannel45AbsthreshPortn_Type()
)
pmopm8CfgChannel45AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel45AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel46AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel46AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel46AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel46AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel46AbsthreshPortn = _Pmopm8CfgChannel46AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 48),
    _Pmopm8CfgChannel46AbsthreshPortn_Type()
)
pmopm8CfgChannel46AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel46AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel47AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel47AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel47AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel47AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel47AbsthreshPortn = _Pmopm8CfgChannel47AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 49),
    _Pmopm8CfgChannel47AbsthreshPortn_Type()
)
pmopm8CfgChannel47AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel47AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel48AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel48AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel48AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel48AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel48AbsthreshPortn = _Pmopm8CfgChannel48AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 50),
    _Pmopm8CfgChannel48AbsthreshPortn_Type()
)
pmopm8CfgChannel48AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel48AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel49AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel49AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel49AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel49AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel49AbsthreshPortn = _Pmopm8CfgChannel49AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 51),
    _Pmopm8CfgChannel49AbsthreshPortn_Type()
)
pmopm8CfgChannel49AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel49AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel50AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel50AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel50AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel50AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel50AbsthreshPortn = _Pmopm8CfgChannel50AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 52),
    _Pmopm8CfgChannel50AbsthreshPortn_Type()
)
pmopm8CfgChannel50AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel50AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel51AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel51AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel51AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel51AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel51AbsthreshPortn = _Pmopm8CfgChannel51AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 53),
    _Pmopm8CfgChannel51AbsthreshPortn_Type()
)
pmopm8CfgChannel51AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel51AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel52AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel52AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel52AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel52AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel52AbsthreshPortn = _Pmopm8CfgChannel52AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 54),
    _Pmopm8CfgChannel52AbsthreshPortn_Type()
)
pmopm8CfgChannel52AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel52AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel53AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel53AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel53AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel53AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel53AbsthreshPortn = _Pmopm8CfgChannel53AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 55),
    _Pmopm8CfgChannel53AbsthreshPortn_Type()
)
pmopm8CfgChannel53AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel53AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel54AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel54AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel54AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel54AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel54AbsthreshPortn = _Pmopm8CfgChannel54AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 56),
    _Pmopm8CfgChannel54AbsthreshPortn_Type()
)
pmopm8CfgChannel54AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel54AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel55AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel55AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel55AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel55AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel55AbsthreshPortn = _Pmopm8CfgChannel55AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 57),
    _Pmopm8CfgChannel55AbsthreshPortn_Type()
)
pmopm8CfgChannel55AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel55AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel56AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel56AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel56AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel56AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel56AbsthreshPortn = _Pmopm8CfgChannel56AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 58),
    _Pmopm8CfgChannel56AbsthreshPortn_Type()
)
pmopm8CfgChannel56AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel56AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel57AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel57AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel57AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel57AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel57AbsthreshPortn = _Pmopm8CfgChannel57AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 59),
    _Pmopm8CfgChannel57AbsthreshPortn_Type()
)
pmopm8CfgChannel57AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel57AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel58AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel58AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel58AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel58AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel58AbsthreshPortn = _Pmopm8CfgChannel58AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 60),
    _Pmopm8CfgChannel58AbsthreshPortn_Type()
)
pmopm8CfgChannel58AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel58AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel59AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel59AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel59AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel59AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel59AbsthreshPortn = _Pmopm8CfgChannel59AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 61),
    _Pmopm8CfgChannel59AbsthreshPortn_Type()
)
pmopm8CfgChannel59AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel59AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel60AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel60AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel60AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel60AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel60AbsthreshPortn = _Pmopm8CfgChannel60AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 62),
    _Pmopm8CfgChannel60AbsthreshPortn_Type()
)
pmopm8CfgChannel60AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel60AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel61AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel61AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel61AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel61AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel61AbsthreshPortn = _Pmopm8CfgChannel61AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 63),
    _Pmopm8CfgChannel61AbsthreshPortn_Type()
)
pmopm8CfgChannel61AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel61AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel62AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel62AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel62AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel62AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel62AbsthreshPortn = _Pmopm8CfgChannel62AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 64),
    _Pmopm8CfgChannel62AbsthreshPortn_Type()
)
pmopm8CfgChannel62AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel62AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel63AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel63AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel63AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel63AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel63AbsthreshPortn = _Pmopm8CfgChannel63AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 65),
    _Pmopm8CfgChannel63AbsthreshPortn_Type()
)
pmopm8CfgChannel63AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel63AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel64AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel64AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel64AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel64AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel64AbsthreshPortn = _Pmopm8CfgChannel64AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 66),
    _Pmopm8CfgChannel64AbsthreshPortn_Type()
)
pmopm8CfgChannel64AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel64AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel65AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel65AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel65AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel65AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel65AbsthreshPortn = _Pmopm8CfgChannel65AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 67),
    _Pmopm8CfgChannel65AbsthreshPortn_Type()
)
pmopm8CfgChannel65AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel65AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel66AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel66AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel66AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel66AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel66AbsthreshPortn = _Pmopm8CfgChannel66AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 68),
    _Pmopm8CfgChannel66AbsthreshPortn_Type()
)
pmopm8CfgChannel66AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel66AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel67AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel67AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel67AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel67AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel67AbsthreshPortn = _Pmopm8CfgChannel67AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 69),
    _Pmopm8CfgChannel67AbsthreshPortn_Type()
)
pmopm8CfgChannel67AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel67AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel68AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel68AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel68AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel68AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel68AbsthreshPortn = _Pmopm8CfgChannel68AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 70),
    _Pmopm8CfgChannel68AbsthreshPortn_Type()
)
pmopm8CfgChannel68AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel68AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel69AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel69AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel69AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel69AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel69AbsthreshPortn = _Pmopm8CfgChannel69AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 71),
    _Pmopm8CfgChannel69AbsthreshPortn_Type()
)
pmopm8CfgChannel69AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel69AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel70AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel70AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel70AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel70AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel70AbsthreshPortn = _Pmopm8CfgChannel70AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 72),
    _Pmopm8CfgChannel70AbsthreshPortn_Type()
)
pmopm8CfgChannel70AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel70AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel71AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel71AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel71AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel71AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel71AbsthreshPortn = _Pmopm8CfgChannel71AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 73),
    _Pmopm8CfgChannel71AbsthreshPortn_Type()
)
pmopm8CfgChannel71AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel71AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel72AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel72AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel72AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel72AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel72AbsthreshPortn = _Pmopm8CfgChannel72AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 74),
    _Pmopm8CfgChannel72AbsthreshPortn_Type()
)
pmopm8CfgChannel72AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel72AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel73AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel73AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel73AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel73AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel73AbsthreshPortn = _Pmopm8CfgChannel73AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 75),
    _Pmopm8CfgChannel73AbsthreshPortn_Type()
)
pmopm8CfgChannel73AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel73AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel74AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel74AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel74AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel74AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel74AbsthreshPortn = _Pmopm8CfgChannel74AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 76),
    _Pmopm8CfgChannel74AbsthreshPortn_Type()
)
pmopm8CfgChannel74AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel74AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel75AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel75AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel75AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel75AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel75AbsthreshPortn = _Pmopm8CfgChannel75AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 77),
    _Pmopm8CfgChannel75AbsthreshPortn_Type()
)
pmopm8CfgChannel75AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel75AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel76AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel76AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel76AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel76AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel76AbsthreshPortn = _Pmopm8CfgChannel76AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 78),
    _Pmopm8CfgChannel76AbsthreshPortn_Type()
)
pmopm8CfgChannel76AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel76AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel77AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel77AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel77AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel77AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel77AbsthreshPortn = _Pmopm8CfgChannel77AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 79),
    _Pmopm8CfgChannel77AbsthreshPortn_Type()
)
pmopm8CfgChannel77AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel77AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel78AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel78AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel78AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel78AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel78AbsthreshPortn = _Pmopm8CfgChannel78AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 80),
    _Pmopm8CfgChannel78AbsthreshPortn_Type()
)
pmopm8CfgChannel78AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel78AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel79AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel79AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel79AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel79AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel79AbsthreshPortn = _Pmopm8CfgChannel79AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 81),
    _Pmopm8CfgChannel79AbsthreshPortn_Type()
)
pmopm8CfgChannel79AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel79AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel80AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel80AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel80AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel80AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel80AbsthreshPortn = _Pmopm8CfgChannel80AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 82),
    _Pmopm8CfgChannel80AbsthreshPortn_Type()
)
pmopm8CfgChannel80AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel80AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel81AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel81AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel81AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel81AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel81AbsthreshPortn = _Pmopm8CfgChannel81AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 83),
    _Pmopm8CfgChannel81AbsthreshPortn_Type()
)
pmopm8CfgChannel81AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel81AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel82AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel82AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel82AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel82AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel82AbsthreshPortn = _Pmopm8CfgChannel82AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 84),
    _Pmopm8CfgChannel82AbsthreshPortn_Type()
)
pmopm8CfgChannel82AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel82AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel83AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel83AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel83AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel83AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel83AbsthreshPortn = _Pmopm8CfgChannel83AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 85),
    _Pmopm8CfgChannel83AbsthreshPortn_Type()
)
pmopm8CfgChannel83AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel83AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel84AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel84AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel84AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel84AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel84AbsthreshPortn = _Pmopm8CfgChannel84AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 86),
    _Pmopm8CfgChannel84AbsthreshPortn_Type()
)
pmopm8CfgChannel84AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel84AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel85AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel85AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel85AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel85AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel85AbsthreshPortn = _Pmopm8CfgChannel85AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 87),
    _Pmopm8CfgChannel85AbsthreshPortn_Type()
)
pmopm8CfgChannel85AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel85AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel86AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel86AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel86AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel86AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel86AbsthreshPortn = _Pmopm8CfgChannel86AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 88),
    _Pmopm8CfgChannel86AbsthreshPortn_Type()
)
pmopm8CfgChannel86AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel86AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel87AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel87AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel87AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel87AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel87AbsthreshPortn = _Pmopm8CfgChannel87AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 89),
    _Pmopm8CfgChannel87AbsthreshPortn_Type()
)
pmopm8CfgChannel87AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel87AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel88AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel88AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel88AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel88AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel88AbsthreshPortn = _Pmopm8CfgChannel88AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 90),
    _Pmopm8CfgChannel88AbsthreshPortn_Type()
)
pmopm8CfgChannel88AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel88AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel89AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel89AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel89AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel89AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel89AbsthreshPortn = _Pmopm8CfgChannel89AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 91),
    _Pmopm8CfgChannel89AbsthreshPortn_Type()
)
pmopm8CfgChannel89AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel89AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel90AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel90AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel90AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel90AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel90AbsthreshPortn = _Pmopm8CfgChannel90AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 92),
    _Pmopm8CfgChannel90AbsthreshPortn_Type()
)
pmopm8CfgChannel90AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel90AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel91AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel91AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel91AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel91AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel91AbsthreshPortn = _Pmopm8CfgChannel91AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 93),
    _Pmopm8CfgChannel91AbsthreshPortn_Type()
)
pmopm8CfgChannel91AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel91AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel92AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel92AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel92AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel92AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel92AbsthreshPortn = _Pmopm8CfgChannel92AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 94),
    _Pmopm8CfgChannel92AbsthreshPortn_Type()
)
pmopm8CfgChannel92AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel92AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel93AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel93AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel93AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel93AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel93AbsthreshPortn = _Pmopm8CfgChannel93AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 95),
    _Pmopm8CfgChannel93AbsthreshPortn_Type()
)
pmopm8CfgChannel93AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel93AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel94AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel94AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel94AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel94AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel94AbsthreshPortn = _Pmopm8CfgChannel94AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 96),
    _Pmopm8CfgChannel94AbsthreshPortn_Type()
)
pmopm8CfgChannel94AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel94AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel95AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel95AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel95AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel95AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel95AbsthreshPortn = _Pmopm8CfgChannel95AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 97),
    _Pmopm8CfgChannel95AbsthreshPortn_Type()
)
pmopm8CfgChannel95AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel95AbsthreshPortn.setStatus("current")


class _Pmopm8CfgChannel96AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel96AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel96AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel96AbsthreshPortn_Object = MibTableColumn
pmopm8CfgChannel96AbsthreshPortn = _Pmopm8CfgChannel96AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 4, 1, 98),
    _Pmopm8CfgChannel96AbsthreshPortn_Type()
)
pmopm8CfgChannel96AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel96AbsthreshPortn.setStatus("current")
_Pmopm8CfgClientStartupPwrHighTable_Object = MibTable
pmopm8CfgClientStartupPwrHighTable = _Pmopm8CfgClientStartupPwrHighTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5)
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupPwrHighTable.setStatus("current")
_Pmopm8CfgClientStartupPwrHighEntry_Object = MibTableRow
pmopm8CfgClientStartupPwrHighEntry = _Pmopm8CfgClientStartupPwrHighEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1)
)
pmopm8CfgClientStartupPwrHighEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CfgClientStartupPwrHighIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupPwrHighEntry.setStatus("current")


class _Pmopm8CfgClientStartupPwrHighIndex_Type(Integer32):
    """Custom type pmopm8CfgClientStartupPwrHighIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CfgClientStartupPwrHighIndex_Type.__name__ = "Integer32"
_Pmopm8CfgClientStartupPwrHighIndex_Object = MibTableColumn
pmopm8CfgClientStartupPwrHighIndex = _Pmopm8CfgClientStartupPwrHighIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 1),
    _Pmopm8CfgClientStartupPwrHighIndex_Type()
)
pmopm8CfgClientStartupPwrHighIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupPwrHighIndex.setStatus("current")


class _Pmopm8CfgChannel1PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel1PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel1PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel1PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel1PwrhighPortn = _Pmopm8CfgChannel1PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 3),
    _Pmopm8CfgChannel1PwrhighPortn_Type()
)
pmopm8CfgChannel1PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel1PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel2PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel2PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel2PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel2PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel2PwrhighPortn = _Pmopm8CfgChannel2PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 4),
    _Pmopm8CfgChannel2PwrhighPortn_Type()
)
pmopm8CfgChannel2PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel2PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel3PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel3PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel3PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel3PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel3PwrhighPortn = _Pmopm8CfgChannel3PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 5),
    _Pmopm8CfgChannel3PwrhighPortn_Type()
)
pmopm8CfgChannel3PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel3PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel4PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel4PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel4PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel4PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel4PwrhighPortn = _Pmopm8CfgChannel4PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 6),
    _Pmopm8CfgChannel4PwrhighPortn_Type()
)
pmopm8CfgChannel4PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel4PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel5PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel5PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel5PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel5PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel5PwrhighPortn = _Pmopm8CfgChannel5PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 7),
    _Pmopm8CfgChannel5PwrhighPortn_Type()
)
pmopm8CfgChannel5PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel5PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel6PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel6PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel6PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel6PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel6PwrhighPortn = _Pmopm8CfgChannel6PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 8),
    _Pmopm8CfgChannel6PwrhighPortn_Type()
)
pmopm8CfgChannel6PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel6PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel7PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel7PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel7PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel7PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel7PwrhighPortn = _Pmopm8CfgChannel7PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 9),
    _Pmopm8CfgChannel7PwrhighPortn_Type()
)
pmopm8CfgChannel7PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel7PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel8PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel8PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel8PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel8PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel8PwrhighPortn = _Pmopm8CfgChannel8PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 10),
    _Pmopm8CfgChannel8PwrhighPortn_Type()
)
pmopm8CfgChannel8PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel8PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel9PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel9PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel9PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel9PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel9PwrhighPortn = _Pmopm8CfgChannel9PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 11),
    _Pmopm8CfgChannel9PwrhighPortn_Type()
)
pmopm8CfgChannel9PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel9PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel10PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel10PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel10PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel10PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel10PwrhighPortn = _Pmopm8CfgChannel10PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 12),
    _Pmopm8CfgChannel10PwrhighPortn_Type()
)
pmopm8CfgChannel10PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel10PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel11PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel11PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel11PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel11PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel11PwrhighPortn = _Pmopm8CfgChannel11PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 13),
    _Pmopm8CfgChannel11PwrhighPortn_Type()
)
pmopm8CfgChannel11PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel11PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel12PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel12PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel12PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel12PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel12PwrhighPortn = _Pmopm8CfgChannel12PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 14),
    _Pmopm8CfgChannel12PwrhighPortn_Type()
)
pmopm8CfgChannel12PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel12PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel13PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel13PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel13PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel13PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel13PwrhighPortn = _Pmopm8CfgChannel13PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 15),
    _Pmopm8CfgChannel13PwrhighPortn_Type()
)
pmopm8CfgChannel13PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel13PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel14PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel14PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel14PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel14PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel14PwrhighPortn = _Pmopm8CfgChannel14PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 16),
    _Pmopm8CfgChannel14PwrhighPortn_Type()
)
pmopm8CfgChannel14PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel14PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel15PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel15PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel15PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel15PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel15PwrhighPortn = _Pmopm8CfgChannel15PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 17),
    _Pmopm8CfgChannel15PwrhighPortn_Type()
)
pmopm8CfgChannel15PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel15PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel16PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel16PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel16PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel16PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel16PwrhighPortn = _Pmopm8CfgChannel16PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 18),
    _Pmopm8CfgChannel16PwrhighPortn_Type()
)
pmopm8CfgChannel16PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel16PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel17PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel17PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel17PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel17PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel17PwrhighPortn = _Pmopm8CfgChannel17PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 19),
    _Pmopm8CfgChannel17PwrhighPortn_Type()
)
pmopm8CfgChannel17PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel17PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel18PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel18PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel18PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel18PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel18PwrhighPortn = _Pmopm8CfgChannel18PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 20),
    _Pmopm8CfgChannel18PwrhighPortn_Type()
)
pmopm8CfgChannel18PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel18PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel19PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel19PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel19PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel19PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel19PwrhighPortn = _Pmopm8CfgChannel19PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 21),
    _Pmopm8CfgChannel19PwrhighPortn_Type()
)
pmopm8CfgChannel19PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel19PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel20PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel20PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel20PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel20PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel20PwrhighPortn = _Pmopm8CfgChannel20PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 22),
    _Pmopm8CfgChannel20PwrhighPortn_Type()
)
pmopm8CfgChannel20PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel20PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel21PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel21PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel21PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel21PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel21PwrhighPortn = _Pmopm8CfgChannel21PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 23),
    _Pmopm8CfgChannel21PwrhighPortn_Type()
)
pmopm8CfgChannel21PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel21PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel22PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel22PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel22PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel22PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel22PwrhighPortn = _Pmopm8CfgChannel22PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 24),
    _Pmopm8CfgChannel22PwrhighPortn_Type()
)
pmopm8CfgChannel22PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel22PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel23PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel23PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel23PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel23PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel23PwrhighPortn = _Pmopm8CfgChannel23PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 25),
    _Pmopm8CfgChannel23PwrhighPortn_Type()
)
pmopm8CfgChannel23PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel23PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel24PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel24PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel24PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel24PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel24PwrhighPortn = _Pmopm8CfgChannel24PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 26),
    _Pmopm8CfgChannel24PwrhighPortn_Type()
)
pmopm8CfgChannel24PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel24PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel25PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel25PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel25PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel25PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel25PwrhighPortn = _Pmopm8CfgChannel25PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 27),
    _Pmopm8CfgChannel25PwrhighPortn_Type()
)
pmopm8CfgChannel25PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel25PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel26PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel26PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel26PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel26PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel26PwrhighPortn = _Pmopm8CfgChannel26PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 28),
    _Pmopm8CfgChannel26PwrhighPortn_Type()
)
pmopm8CfgChannel26PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel26PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel27PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel27PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel27PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel27PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel27PwrhighPortn = _Pmopm8CfgChannel27PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 29),
    _Pmopm8CfgChannel27PwrhighPortn_Type()
)
pmopm8CfgChannel27PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel27PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel28PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel28PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel28PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel28PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel28PwrhighPortn = _Pmopm8CfgChannel28PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 30),
    _Pmopm8CfgChannel28PwrhighPortn_Type()
)
pmopm8CfgChannel28PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel28PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel29PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel29PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel29PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel29PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel29PwrhighPortn = _Pmopm8CfgChannel29PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 31),
    _Pmopm8CfgChannel29PwrhighPortn_Type()
)
pmopm8CfgChannel29PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel29PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel30PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel30PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel30PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel30PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel30PwrhighPortn = _Pmopm8CfgChannel30PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 32),
    _Pmopm8CfgChannel30PwrhighPortn_Type()
)
pmopm8CfgChannel30PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel30PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel31PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel31PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel31PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel31PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel31PwrhighPortn = _Pmopm8CfgChannel31PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 33),
    _Pmopm8CfgChannel31PwrhighPortn_Type()
)
pmopm8CfgChannel31PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel31PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel32PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel32PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel32PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel32PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel32PwrhighPortn = _Pmopm8CfgChannel32PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 34),
    _Pmopm8CfgChannel32PwrhighPortn_Type()
)
pmopm8CfgChannel32PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel32PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel33PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel33PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel33PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel33PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel33PwrhighPortn = _Pmopm8CfgChannel33PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 35),
    _Pmopm8CfgChannel33PwrhighPortn_Type()
)
pmopm8CfgChannel33PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel33PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel34PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel34PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel34PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel34PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel34PwrhighPortn = _Pmopm8CfgChannel34PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 36),
    _Pmopm8CfgChannel34PwrhighPortn_Type()
)
pmopm8CfgChannel34PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel34PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel35PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel35PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel35PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel35PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel35PwrhighPortn = _Pmopm8CfgChannel35PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 37),
    _Pmopm8CfgChannel35PwrhighPortn_Type()
)
pmopm8CfgChannel35PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel35PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel36PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel36PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel36PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel36PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel36PwrhighPortn = _Pmopm8CfgChannel36PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 38),
    _Pmopm8CfgChannel36PwrhighPortn_Type()
)
pmopm8CfgChannel36PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel36PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel37PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel37PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel37PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel37PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel37PwrhighPortn = _Pmopm8CfgChannel37PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 39),
    _Pmopm8CfgChannel37PwrhighPortn_Type()
)
pmopm8CfgChannel37PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel37PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel38PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel38PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel38PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel38PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel38PwrhighPortn = _Pmopm8CfgChannel38PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 40),
    _Pmopm8CfgChannel38PwrhighPortn_Type()
)
pmopm8CfgChannel38PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel38PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel39PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel39PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel39PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel39PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel39PwrhighPortn = _Pmopm8CfgChannel39PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 41),
    _Pmopm8CfgChannel39PwrhighPortn_Type()
)
pmopm8CfgChannel39PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel39PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel40PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel40PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel40PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel40PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel40PwrhighPortn = _Pmopm8CfgChannel40PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 42),
    _Pmopm8CfgChannel40PwrhighPortn_Type()
)
pmopm8CfgChannel40PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel40PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel41PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel41PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel41PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel41PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel41PwrhighPortn = _Pmopm8CfgChannel41PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 43),
    _Pmopm8CfgChannel41PwrhighPortn_Type()
)
pmopm8CfgChannel41PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel41PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel42PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel42PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel42PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel42PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel42PwrhighPortn = _Pmopm8CfgChannel42PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 44),
    _Pmopm8CfgChannel42PwrhighPortn_Type()
)
pmopm8CfgChannel42PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel42PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel43PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel43PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel43PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel43PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel43PwrhighPortn = _Pmopm8CfgChannel43PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 45),
    _Pmopm8CfgChannel43PwrhighPortn_Type()
)
pmopm8CfgChannel43PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel43PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel44PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel44PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel44PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel44PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel44PwrhighPortn = _Pmopm8CfgChannel44PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 46),
    _Pmopm8CfgChannel44PwrhighPortn_Type()
)
pmopm8CfgChannel44PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel44PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel45PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel45PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel45PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel45PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel45PwrhighPortn = _Pmopm8CfgChannel45PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 47),
    _Pmopm8CfgChannel45PwrhighPortn_Type()
)
pmopm8CfgChannel45PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel45PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel46PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel46PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel46PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel46PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel46PwrhighPortn = _Pmopm8CfgChannel46PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 48),
    _Pmopm8CfgChannel46PwrhighPortn_Type()
)
pmopm8CfgChannel46PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel46PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel47PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel47PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel47PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel47PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel47PwrhighPortn = _Pmopm8CfgChannel47PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 49),
    _Pmopm8CfgChannel47PwrhighPortn_Type()
)
pmopm8CfgChannel47PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel47PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel48PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel48PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel48PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel48PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel48PwrhighPortn = _Pmopm8CfgChannel48PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 50),
    _Pmopm8CfgChannel48PwrhighPortn_Type()
)
pmopm8CfgChannel48PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel48PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel49PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel49PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel49PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel49PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel49PwrhighPortn = _Pmopm8CfgChannel49PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 51),
    _Pmopm8CfgChannel49PwrhighPortn_Type()
)
pmopm8CfgChannel49PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel49PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel50PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel50PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel50PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel50PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel50PwrhighPortn = _Pmopm8CfgChannel50PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 52),
    _Pmopm8CfgChannel50PwrhighPortn_Type()
)
pmopm8CfgChannel50PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel50PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel51PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel51PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel51PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel51PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel51PwrhighPortn = _Pmopm8CfgChannel51PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 53),
    _Pmopm8CfgChannel51PwrhighPortn_Type()
)
pmopm8CfgChannel51PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel51PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel52PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel52PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel52PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel52PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel52PwrhighPortn = _Pmopm8CfgChannel52PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 54),
    _Pmopm8CfgChannel52PwrhighPortn_Type()
)
pmopm8CfgChannel52PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel52PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel53PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel53PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel53PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel53PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel53PwrhighPortn = _Pmopm8CfgChannel53PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 55),
    _Pmopm8CfgChannel53PwrhighPortn_Type()
)
pmopm8CfgChannel53PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel53PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel54PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel54PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel54PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel54PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel54PwrhighPortn = _Pmopm8CfgChannel54PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 56),
    _Pmopm8CfgChannel54PwrhighPortn_Type()
)
pmopm8CfgChannel54PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel54PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel55PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel55PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel55PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel55PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel55PwrhighPortn = _Pmopm8CfgChannel55PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 57),
    _Pmopm8CfgChannel55PwrhighPortn_Type()
)
pmopm8CfgChannel55PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel55PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel56PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel56PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel56PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel56PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel56PwrhighPortn = _Pmopm8CfgChannel56PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 58),
    _Pmopm8CfgChannel56PwrhighPortn_Type()
)
pmopm8CfgChannel56PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel56PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel57PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel57PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel57PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel57PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel57PwrhighPortn = _Pmopm8CfgChannel57PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 59),
    _Pmopm8CfgChannel57PwrhighPortn_Type()
)
pmopm8CfgChannel57PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel57PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel58PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel58PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel58PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel58PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel58PwrhighPortn = _Pmopm8CfgChannel58PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 60),
    _Pmopm8CfgChannel58PwrhighPortn_Type()
)
pmopm8CfgChannel58PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel58PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel59PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel59PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel59PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel59PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel59PwrhighPortn = _Pmopm8CfgChannel59PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 61),
    _Pmopm8CfgChannel59PwrhighPortn_Type()
)
pmopm8CfgChannel59PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel59PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel60PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel60PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel60PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel60PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel60PwrhighPortn = _Pmopm8CfgChannel60PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 62),
    _Pmopm8CfgChannel60PwrhighPortn_Type()
)
pmopm8CfgChannel60PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel60PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel61PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel61PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel61PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel61PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel61PwrhighPortn = _Pmopm8CfgChannel61PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 63),
    _Pmopm8CfgChannel61PwrhighPortn_Type()
)
pmopm8CfgChannel61PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel61PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel62PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel62PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel62PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel62PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel62PwrhighPortn = _Pmopm8CfgChannel62PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 64),
    _Pmopm8CfgChannel62PwrhighPortn_Type()
)
pmopm8CfgChannel62PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel62PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel63PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel63PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel63PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel63PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel63PwrhighPortn = _Pmopm8CfgChannel63PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 65),
    _Pmopm8CfgChannel63PwrhighPortn_Type()
)
pmopm8CfgChannel63PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel63PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel64PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel64PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel64PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel64PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel64PwrhighPortn = _Pmopm8CfgChannel64PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 66),
    _Pmopm8CfgChannel64PwrhighPortn_Type()
)
pmopm8CfgChannel64PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel64PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel65PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel65PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel65PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel65PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel65PwrhighPortn = _Pmopm8CfgChannel65PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 67),
    _Pmopm8CfgChannel65PwrhighPortn_Type()
)
pmopm8CfgChannel65PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel65PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel66PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel66PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel66PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel66PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel66PwrhighPortn = _Pmopm8CfgChannel66PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 68),
    _Pmopm8CfgChannel66PwrhighPortn_Type()
)
pmopm8CfgChannel66PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel66PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel67PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel67PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel67PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel67PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel67PwrhighPortn = _Pmopm8CfgChannel67PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 69),
    _Pmopm8CfgChannel67PwrhighPortn_Type()
)
pmopm8CfgChannel67PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel67PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel68PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel68PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel68PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel68PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel68PwrhighPortn = _Pmopm8CfgChannel68PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 70),
    _Pmopm8CfgChannel68PwrhighPortn_Type()
)
pmopm8CfgChannel68PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel68PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel69PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel69PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel69PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel69PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel69PwrhighPortn = _Pmopm8CfgChannel69PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 71),
    _Pmopm8CfgChannel69PwrhighPortn_Type()
)
pmopm8CfgChannel69PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel69PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel70PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel70PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel70PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel70PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel70PwrhighPortn = _Pmopm8CfgChannel70PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 72),
    _Pmopm8CfgChannel70PwrhighPortn_Type()
)
pmopm8CfgChannel70PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel70PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel71PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel71PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel71PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel71PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel71PwrhighPortn = _Pmopm8CfgChannel71PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 73),
    _Pmopm8CfgChannel71PwrhighPortn_Type()
)
pmopm8CfgChannel71PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel71PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel72PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel72PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel72PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel72PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel72PwrhighPortn = _Pmopm8CfgChannel72PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 74),
    _Pmopm8CfgChannel72PwrhighPortn_Type()
)
pmopm8CfgChannel72PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel72PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel73PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel73PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel73PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel73PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel73PwrhighPortn = _Pmopm8CfgChannel73PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 75),
    _Pmopm8CfgChannel73PwrhighPortn_Type()
)
pmopm8CfgChannel73PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel73PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel74PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel74PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel74PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel74PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel74PwrhighPortn = _Pmopm8CfgChannel74PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 76),
    _Pmopm8CfgChannel74PwrhighPortn_Type()
)
pmopm8CfgChannel74PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel74PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel75PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel75PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel75PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel75PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel75PwrhighPortn = _Pmopm8CfgChannel75PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 77),
    _Pmopm8CfgChannel75PwrhighPortn_Type()
)
pmopm8CfgChannel75PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel75PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel76PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel76PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel76PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel76PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel76PwrhighPortn = _Pmopm8CfgChannel76PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 78),
    _Pmopm8CfgChannel76PwrhighPortn_Type()
)
pmopm8CfgChannel76PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel76PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel77PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel77PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel77PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel77PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel77PwrhighPortn = _Pmopm8CfgChannel77PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 79),
    _Pmopm8CfgChannel77PwrhighPortn_Type()
)
pmopm8CfgChannel77PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel77PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel78PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel78PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel78PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel78PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel78PwrhighPortn = _Pmopm8CfgChannel78PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 80),
    _Pmopm8CfgChannel78PwrhighPortn_Type()
)
pmopm8CfgChannel78PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel78PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel79PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel79PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel79PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel79PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel79PwrhighPortn = _Pmopm8CfgChannel79PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 81),
    _Pmopm8CfgChannel79PwrhighPortn_Type()
)
pmopm8CfgChannel79PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel79PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel80PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel80PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel80PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel80PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel80PwrhighPortn = _Pmopm8CfgChannel80PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 82),
    _Pmopm8CfgChannel80PwrhighPortn_Type()
)
pmopm8CfgChannel80PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel80PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel81PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel81PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel81PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel81PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel81PwrhighPortn = _Pmopm8CfgChannel81PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 83),
    _Pmopm8CfgChannel81PwrhighPortn_Type()
)
pmopm8CfgChannel81PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel81PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel82PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel82PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel82PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel82PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel82PwrhighPortn = _Pmopm8CfgChannel82PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 84),
    _Pmopm8CfgChannel82PwrhighPortn_Type()
)
pmopm8CfgChannel82PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel82PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel83PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel83PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel83PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel83PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel83PwrhighPortn = _Pmopm8CfgChannel83PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 85),
    _Pmopm8CfgChannel83PwrhighPortn_Type()
)
pmopm8CfgChannel83PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel83PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel84PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel84PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel84PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel84PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel84PwrhighPortn = _Pmopm8CfgChannel84PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 86),
    _Pmopm8CfgChannel84PwrhighPortn_Type()
)
pmopm8CfgChannel84PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel84PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel85PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel85PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel85PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel85PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel85PwrhighPortn = _Pmopm8CfgChannel85PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 87),
    _Pmopm8CfgChannel85PwrhighPortn_Type()
)
pmopm8CfgChannel85PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel85PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel86PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel86PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel86PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel86PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel86PwrhighPortn = _Pmopm8CfgChannel86PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 88),
    _Pmopm8CfgChannel86PwrhighPortn_Type()
)
pmopm8CfgChannel86PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel86PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel87PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel87PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel87PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel87PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel87PwrhighPortn = _Pmopm8CfgChannel87PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 89),
    _Pmopm8CfgChannel87PwrhighPortn_Type()
)
pmopm8CfgChannel87PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel87PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel88PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel88PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel88PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel88PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel88PwrhighPortn = _Pmopm8CfgChannel88PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 90),
    _Pmopm8CfgChannel88PwrhighPortn_Type()
)
pmopm8CfgChannel88PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel88PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel89PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel89PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel89PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel89PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel89PwrhighPortn = _Pmopm8CfgChannel89PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 91),
    _Pmopm8CfgChannel89PwrhighPortn_Type()
)
pmopm8CfgChannel89PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel89PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel90PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel90PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel90PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel90PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel90PwrhighPortn = _Pmopm8CfgChannel90PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 92),
    _Pmopm8CfgChannel90PwrhighPortn_Type()
)
pmopm8CfgChannel90PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel90PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel91PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel91PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel91PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel91PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel91PwrhighPortn = _Pmopm8CfgChannel91PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 93),
    _Pmopm8CfgChannel91PwrhighPortn_Type()
)
pmopm8CfgChannel91PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel91PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel92PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel92PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel92PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel92PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel92PwrhighPortn = _Pmopm8CfgChannel92PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 94),
    _Pmopm8CfgChannel92PwrhighPortn_Type()
)
pmopm8CfgChannel92PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel92PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel93PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel93PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel93PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel93PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel93PwrhighPortn = _Pmopm8CfgChannel93PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 95),
    _Pmopm8CfgChannel93PwrhighPortn_Type()
)
pmopm8CfgChannel93PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel93PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel94PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel94PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel94PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel94PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel94PwrhighPortn = _Pmopm8CfgChannel94PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 96),
    _Pmopm8CfgChannel94PwrhighPortn_Type()
)
pmopm8CfgChannel94PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel94PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel95PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel95PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel95PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel95PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel95PwrhighPortn = _Pmopm8CfgChannel95PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 97),
    _Pmopm8CfgChannel95PwrhighPortn_Type()
)
pmopm8CfgChannel95PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel95PwrhighPortn.setStatus("current")


class _Pmopm8CfgChannel96PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel96PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel96PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel96PwrhighPortn_Object = MibTableColumn
pmopm8CfgChannel96PwrhighPortn = _Pmopm8CfgChannel96PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 5, 1, 98),
    _Pmopm8CfgChannel96PwrhighPortn_Type()
)
pmopm8CfgChannel96PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel96PwrhighPortn.setStatus("current")
_Pmopm8CfgClientStartupPwrLowTable_Object = MibTable
pmopm8CfgClientStartupPwrLowTable = _Pmopm8CfgClientStartupPwrLowTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6)
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupPwrLowTable.setStatus("current")
_Pmopm8CfgClientStartupPwrLowEntry_Object = MibTableRow
pmopm8CfgClientStartupPwrLowEntry = _Pmopm8CfgClientStartupPwrLowEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1)
)
pmopm8CfgClientStartupPwrLowEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CfgClientStartupPwrLowIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupPwrLowEntry.setStatus("current")


class _Pmopm8CfgClientStartupPwrLowIndex_Type(Integer32):
    """Custom type pmopm8CfgClientStartupPwrLowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CfgClientStartupPwrLowIndex_Type.__name__ = "Integer32"
_Pmopm8CfgClientStartupPwrLowIndex_Object = MibTableColumn
pmopm8CfgClientStartupPwrLowIndex = _Pmopm8CfgClientStartupPwrLowIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 1),
    _Pmopm8CfgClientStartupPwrLowIndex_Type()
)
pmopm8CfgClientStartupPwrLowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgClientStartupPwrLowIndex.setStatus("current")


class _Pmopm8CfgChannel1PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel1PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel1PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel1PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel1PwrlowPortn = _Pmopm8CfgChannel1PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 3),
    _Pmopm8CfgChannel1PwrlowPortn_Type()
)
pmopm8CfgChannel1PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel1PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel2PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel2PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel2PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel2PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel2PwrlowPortn = _Pmopm8CfgChannel2PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 4),
    _Pmopm8CfgChannel2PwrlowPortn_Type()
)
pmopm8CfgChannel2PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel2PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel3PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel3PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel3PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel3PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel3PwrlowPortn = _Pmopm8CfgChannel3PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 5),
    _Pmopm8CfgChannel3PwrlowPortn_Type()
)
pmopm8CfgChannel3PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel3PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel4PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel4PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel4PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel4PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel4PwrlowPortn = _Pmopm8CfgChannel4PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 6),
    _Pmopm8CfgChannel4PwrlowPortn_Type()
)
pmopm8CfgChannel4PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel4PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel5PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel5PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel5PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel5PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel5PwrlowPortn = _Pmopm8CfgChannel5PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 7),
    _Pmopm8CfgChannel5PwrlowPortn_Type()
)
pmopm8CfgChannel5PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel5PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel6PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel6PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel6PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel6PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel6PwrlowPortn = _Pmopm8CfgChannel6PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 8),
    _Pmopm8CfgChannel6PwrlowPortn_Type()
)
pmopm8CfgChannel6PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel6PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel7PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel7PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel7PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel7PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel7PwrlowPortn = _Pmopm8CfgChannel7PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 9),
    _Pmopm8CfgChannel7PwrlowPortn_Type()
)
pmopm8CfgChannel7PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel7PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel8PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel8PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel8PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel8PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel8PwrlowPortn = _Pmopm8CfgChannel8PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 10),
    _Pmopm8CfgChannel8PwrlowPortn_Type()
)
pmopm8CfgChannel8PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel8PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel9PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel9PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel9PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel9PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel9PwrlowPortn = _Pmopm8CfgChannel9PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 11),
    _Pmopm8CfgChannel9PwrlowPortn_Type()
)
pmopm8CfgChannel9PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel9PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel10PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel10PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel10PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel10PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel10PwrlowPortn = _Pmopm8CfgChannel10PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 12),
    _Pmopm8CfgChannel10PwrlowPortn_Type()
)
pmopm8CfgChannel10PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel10PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel11PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel11PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel11PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel11PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel11PwrlowPortn = _Pmopm8CfgChannel11PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 13),
    _Pmopm8CfgChannel11PwrlowPortn_Type()
)
pmopm8CfgChannel11PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel11PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel12PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel12PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel12PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel12PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel12PwrlowPortn = _Pmopm8CfgChannel12PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 14),
    _Pmopm8CfgChannel12PwrlowPortn_Type()
)
pmopm8CfgChannel12PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel12PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel13PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel13PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel13PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel13PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel13PwrlowPortn = _Pmopm8CfgChannel13PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 15),
    _Pmopm8CfgChannel13PwrlowPortn_Type()
)
pmopm8CfgChannel13PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel13PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel14PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel14PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel14PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel14PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel14PwrlowPortn = _Pmopm8CfgChannel14PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 16),
    _Pmopm8CfgChannel14PwrlowPortn_Type()
)
pmopm8CfgChannel14PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel14PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel15PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel15PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel15PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel15PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel15PwrlowPortn = _Pmopm8CfgChannel15PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 17),
    _Pmopm8CfgChannel15PwrlowPortn_Type()
)
pmopm8CfgChannel15PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel15PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel16PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel16PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel16PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel16PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel16PwrlowPortn = _Pmopm8CfgChannel16PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 18),
    _Pmopm8CfgChannel16PwrlowPortn_Type()
)
pmopm8CfgChannel16PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel16PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel17PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel17PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel17PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel17PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel17PwrlowPortn = _Pmopm8CfgChannel17PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 19),
    _Pmopm8CfgChannel17PwrlowPortn_Type()
)
pmopm8CfgChannel17PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel17PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel18PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel18PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel18PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel18PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel18PwrlowPortn = _Pmopm8CfgChannel18PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 20),
    _Pmopm8CfgChannel18PwrlowPortn_Type()
)
pmopm8CfgChannel18PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel18PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel19PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel19PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel19PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel19PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel19PwrlowPortn = _Pmopm8CfgChannel19PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 21),
    _Pmopm8CfgChannel19PwrlowPortn_Type()
)
pmopm8CfgChannel19PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel19PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel20PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel20PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel20PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel20PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel20PwrlowPortn = _Pmopm8CfgChannel20PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 22),
    _Pmopm8CfgChannel20PwrlowPortn_Type()
)
pmopm8CfgChannel20PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel20PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel21PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel21PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel21PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel21PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel21PwrlowPortn = _Pmopm8CfgChannel21PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 23),
    _Pmopm8CfgChannel21PwrlowPortn_Type()
)
pmopm8CfgChannel21PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel21PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel22PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel22PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel22PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel22PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel22PwrlowPortn = _Pmopm8CfgChannel22PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 24),
    _Pmopm8CfgChannel22PwrlowPortn_Type()
)
pmopm8CfgChannel22PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel22PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel23PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel23PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel23PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel23PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel23PwrlowPortn = _Pmopm8CfgChannel23PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 25),
    _Pmopm8CfgChannel23PwrlowPortn_Type()
)
pmopm8CfgChannel23PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel23PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel24PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel24PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel24PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel24PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel24PwrlowPortn = _Pmopm8CfgChannel24PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 26),
    _Pmopm8CfgChannel24PwrlowPortn_Type()
)
pmopm8CfgChannel24PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel24PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel25PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel25PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel25PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel25PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel25PwrlowPortn = _Pmopm8CfgChannel25PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 27),
    _Pmopm8CfgChannel25PwrlowPortn_Type()
)
pmopm8CfgChannel25PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel25PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel26PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel26PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel26PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel26PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel26PwrlowPortn = _Pmopm8CfgChannel26PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 28),
    _Pmopm8CfgChannel26PwrlowPortn_Type()
)
pmopm8CfgChannel26PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel26PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel27PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel27PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel27PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel27PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel27PwrlowPortn = _Pmopm8CfgChannel27PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 29),
    _Pmopm8CfgChannel27PwrlowPortn_Type()
)
pmopm8CfgChannel27PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel27PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel28PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel28PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel28PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel28PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel28PwrlowPortn = _Pmopm8CfgChannel28PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 30),
    _Pmopm8CfgChannel28PwrlowPortn_Type()
)
pmopm8CfgChannel28PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel28PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel29PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel29PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel29PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel29PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel29PwrlowPortn = _Pmopm8CfgChannel29PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 31),
    _Pmopm8CfgChannel29PwrlowPortn_Type()
)
pmopm8CfgChannel29PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel29PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel30PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel30PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel30PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel30PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel30PwrlowPortn = _Pmopm8CfgChannel30PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 32),
    _Pmopm8CfgChannel30PwrlowPortn_Type()
)
pmopm8CfgChannel30PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel30PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel31PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel31PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel31PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel31PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel31PwrlowPortn = _Pmopm8CfgChannel31PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 33),
    _Pmopm8CfgChannel31PwrlowPortn_Type()
)
pmopm8CfgChannel31PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel31PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel32PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel32PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel32PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel32PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel32PwrlowPortn = _Pmopm8CfgChannel32PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 34),
    _Pmopm8CfgChannel32PwrlowPortn_Type()
)
pmopm8CfgChannel32PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel32PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel33PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel33PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel33PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel33PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel33PwrlowPortn = _Pmopm8CfgChannel33PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 35),
    _Pmopm8CfgChannel33PwrlowPortn_Type()
)
pmopm8CfgChannel33PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel33PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel34PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel34PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel34PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel34PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel34PwrlowPortn = _Pmopm8CfgChannel34PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 36),
    _Pmopm8CfgChannel34PwrlowPortn_Type()
)
pmopm8CfgChannel34PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel34PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel35PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel35PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel35PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel35PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel35PwrlowPortn = _Pmopm8CfgChannel35PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 37),
    _Pmopm8CfgChannel35PwrlowPortn_Type()
)
pmopm8CfgChannel35PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel35PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel36PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel36PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel36PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel36PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel36PwrlowPortn = _Pmopm8CfgChannel36PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 38),
    _Pmopm8CfgChannel36PwrlowPortn_Type()
)
pmopm8CfgChannel36PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel36PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel37PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel37PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel37PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel37PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel37PwrlowPortn = _Pmopm8CfgChannel37PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 39),
    _Pmopm8CfgChannel37PwrlowPortn_Type()
)
pmopm8CfgChannel37PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel37PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel38PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel38PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel38PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel38PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel38PwrlowPortn = _Pmopm8CfgChannel38PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 40),
    _Pmopm8CfgChannel38PwrlowPortn_Type()
)
pmopm8CfgChannel38PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel38PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel39PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel39PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel39PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel39PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel39PwrlowPortn = _Pmopm8CfgChannel39PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 41),
    _Pmopm8CfgChannel39PwrlowPortn_Type()
)
pmopm8CfgChannel39PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel39PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel40PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel40PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel40PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel40PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel40PwrlowPortn = _Pmopm8CfgChannel40PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 42),
    _Pmopm8CfgChannel40PwrlowPortn_Type()
)
pmopm8CfgChannel40PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel40PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel41PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel41PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel41PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel41PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel41PwrlowPortn = _Pmopm8CfgChannel41PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 43),
    _Pmopm8CfgChannel41PwrlowPortn_Type()
)
pmopm8CfgChannel41PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel41PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel42PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel42PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel42PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel42PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel42PwrlowPortn = _Pmopm8CfgChannel42PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 44),
    _Pmopm8CfgChannel42PwrlowPortn_Type()
)
pmopm8CfgChannel42PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel42PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel43PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel43PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel43PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel43PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel43PwrlowPortn = _Pmopm8CfgChannel43PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 45),
    _Pmopm8CfgChannel43PwrlowPortn_Type()
)
pmopm8CfgChannel43PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel43PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel44PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel44PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel44PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel44PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel44PwrlowPortn = _Pmopm8CfgChannel44PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 46),
    _Pmopm8CfgChannel44PwrlowPortn_Type()
)
pmopm8CfgChannel44PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel44PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel45PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel45PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel45PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel45PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel45PwrlowPortn = _Pmopm8CfgChannel45PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 47),
    _Pmopm8CfgChannel45PwrlowPortn_Type()
)
pmopm8CfgChannel45PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel45PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel46PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel46PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel46PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel46PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel46PwrlowPortn = _Pmopm8CfgChannel46PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 48),
    _Pmopm8CfgChannel46PwrlowPortn_Type()
)
pmopm8CfgChannel46PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel46PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel47PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel47PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel47PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel47PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel47PwrlowPortn = _Pmopm8CfgChannel47PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 49),
    _Pmopm8CfgChannel47PwrlowPortn_Type()
)
pmopm8CfgChannel47PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel47PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel48PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel48PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel48PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel48PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel48PwrlowPortn = _Pmopm8CfgChannel48PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 50),
    _Pmopm8CfgChannel48PwrlowPortn_Type()
)
pmopm8CfgChannel48PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel48PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel49PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel49PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel49PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel49PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel49PwrlowPortn = _Pmopm8CfgChannel49PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 51),
    _Pmopm8CfgChannel49PwrlowPortn_Type()
)
pmopm8CfgChannel49PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel49PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel50PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel50PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel50PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel50PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel50PwrlowPortn = _Pmopm8CfgChannel50PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 52),
    _Pmopm8CfgChannel50PwrlowPortn_Type()
)
pmopm8CfgChannel50PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel50PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel51PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel51PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel51PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel51PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel51PwrlowPortn = _Pmopm8CfgChannel51PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 53),
    _Pmopm8CfgChannel51PwrlowPortn_Type()
)
pmopm8CfgChannel51PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel51PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel52PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel52PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel52PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel52PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel52PwrlowPortn = _Pmopm8CfgChannel52PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 54),
    _Pmopm8CfgChannel52PwrlowPortn_Type()
)
pmopm8CfgChannel52PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel52PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel53PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel53PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel53PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel53PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel53PwrlowPortn = _Pmopm8CfgChannel53PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 55),
    _Pmopm8CfgChannel53PwrlowPortn_Type()
)
pmopm8CfgChannel53PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel53PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel54PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel54PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel54PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel54PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel54PwrlowPortn = _Pmopm8CfgChannel54PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 56),
    _Pmopm8CfgChannel54PwrlowPortn_Type()
)
pmopm8CfgChannel54PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel54PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel55PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel55PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel55PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel55PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel55PwrlowPortn = _Pmopm8CfgChannel55PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 57),
    _Pmopm8CfgChannel55PwrlowPortn_Type()
)
pmopm8CfgChannel55PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel55PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel56PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel56PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel56PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel56PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel56PwrlowPortn = _Pmopm8CfgChannel56PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 58),
    _Pmopm8CfgChannel56PwrlowPortn_Type()
)
pmopm8CfgChannel56PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel56PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel57PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel57PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel57PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel57PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel57PwrlowPortn = _Pmopm8CfgChannel57PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 59),
    _Pmopm8CfgChannel57PwrlowPortn_Type()
)
pmopm8CfgChannel57PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel57PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel58PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel58PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel58PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel58PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel58PwrlowPortn = _Pmopm8CfgChannel58PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 60),
    _Pmopm8CfgChannel58PwrlowPortn_Type()
)
pmopm8CfgChannel58PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel58PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel59PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel59PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel59PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel59PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel59PwrlowPortn = _Pmopm8CfgChannel59PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 61),
    _Pmopm8CfgChannel59PwrlowPortn_Type()
)
pmopm8CfgChannel59PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel59PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel60PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel60PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel60PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel60PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel60PwrlowPortn = _Pmopm8CfgChannel60PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 62),
    _Pmopm8CfgChannel60PwrlowPortn_Type()
)
pmopm8CfgChannel60PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel60PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel61PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel61PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel61PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel61PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel61PwrlowPortn = _Pmopm8CfgChannel61PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 63),
    _Pmopm8CfgChannel61PwrlowPortn_Type()
)
pmopm8CfgChannel61PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel61PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel62PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel62PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel62PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel62PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel62PwrlowPortn = _Pmopm8CfgChannel62PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 64),
    _Pmopm8CfgChannel62PwrlowPortn_Type()
)
pmopm8CfgChannel62PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel62PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel63PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel63PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel63PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel63PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel63PwrlowPortn = _Pmopm8CfgChannel63PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 65),
    _Pmopm8CfgChannel63PwrlowPortn_Type()
)
pmopm8CfgChannel63PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel63PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel64PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel64PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel64PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel64PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel64PwrlowPortn = _Pmopm8CfgChannel64PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 66),
    _Pmopm8CfgChannel64PwrlowPortn_Type()
)
pmopm8CfgChannel64PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel64PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel65PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel65PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel65PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel65PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel65PwrlowPortn = _Pmopm8CfgChannel65PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 67),
    _Pmopm8CfgChannel65PwrlowPortn_Type()
)
pmopm8CfgChannel65PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel65PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel66PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel66PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel66PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel66PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel66PwrlowPortn = _Pmopm8CfgChannel66PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 68),
    _Pmopm8CfgChannel66PwrlowPortn_Type()
)
pmopm8CfgChannel66PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel66PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel67PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel67PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel67PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel67PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel67PwrlowPortn = _Pmopm8CfgChannel67PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 69),
    _Pmopm8CfgChannel67PwrlowPortn_Type()
)
pmopm8CfgChannel67PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel67PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel68PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel68PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel68PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel68PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel68PwrlowPortn = _Pmopm8CfgChannel68PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 70),
    _Pmopm8CfgChannel68PwrlowPortn_Type()
)
pmopm8CfgChannel68PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel68PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel69PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel69PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel69PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel69PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel69PwrlowPortn = _Pmopm8CfgChannel69PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 71),
    _Pmopm8CfgChannel69PwrlowPortn_Type()
)
pmopm8CfgChannel69PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel69PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel70PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel70PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel70PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel70PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel70PwrlowPortn = _Pmopm8CfgChannel70PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 72),
    _Pmopm8CfgChannel70PwrlowPortn_Type()
)
pmopm8CfgChannel70PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel70PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel71PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel71PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel71PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel71PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel71PwrlowPortn = _Pmopm8CfgChannel71PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 73),
    _Pmopm8CfgChannel71PwrlowPortn_Type()
)
pmopm8CfgChannel71PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel71PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel72PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel72PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel72PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel72PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel72PwrlowPortn = _Pmopm8CfgChannel72PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 74),
    _Pmopm8CfgChannel72PwrlowPortn_Type()
)
pmopm8CfgChannel72PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel72PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel73PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel73PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel73PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel73PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel73PwrlowPortn = _Pmopm8CfgChannel73PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 75),
    _Pmopm8CfgChannel73PwrlowPortn_Type()
)
pmopm8CfgChannel73PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel73PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel74PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel74PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel74PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel74PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel74PwrlowPortn = _Pmopm8CfgChannel74PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 76),
    _Pmopm8CfgChannel74PwrlowPortn_Type()
)
pmopm8CfgChannel74PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel74PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel75PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel75PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel75PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel75PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel75PwrlowPortn = _Pmopm8CfgChannel75PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 77),
    _Pmopm8CfgChannel75PwrlowPortn_Type()
)
pmopm8CfgChannel75PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel75PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel76PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel76PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel76PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel76PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel76PwrlowPortn = _Pmopm8CfgChannel76PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 78),
    _Pmopm8CfgChannel76PwrlowPortn_Type()
)
pmopm8CfgChannel76PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel76PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel77PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel77PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel77PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel77PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel77PwrlowPortn = _Pmopm8CfgChannel77PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 79),
    _Pmopm8CfgChannel77PwrlowPortn_Type()
)
pmopm8CfgChannel77PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel77PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel78PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel78PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel78PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel78PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel78PwrlowPortn = _Pmopm8CfgChannel78PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 80),
    _Pmopm8CfgChannel78PwrlowPortn_Type()
)
pmopm8CfgChannel78PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel78PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel79PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel79PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel79PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel79PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel79PwrlowPortn = _Pmopm8CfgChannel79PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 81),
    _Pmopm8CfgChannel79PwrlowPortn_Type()
)
pmopm8CfgChannel79PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel79PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel80PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel80PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel80PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel80PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel80PwrlowPortn = _Pmopm8CfgChannel80PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 82),
    _Pmopm8CfgChannel80PwrlowPortn_Type()
)
pmopm8CfgChannel80PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel80PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel81PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel81PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel81PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel81PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel81PwrlowPortn = _Pmopm8CfgChannel81PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 83),
    _Pmopm8CfgChannel81PwrlowPortn_Type()
)
pmopm8CfgChannel81PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel81PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel82PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel82PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel82PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel82PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel82PwrlowPortn = _Pmopm8CfgChannel82PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 84),
    _Pmopm8CfgChannel82PwrlowPortn_Type()
)
pmopm8CfgChannel82PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel82PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel83PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel83PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel83PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel83PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel83PwrlowPortn = _Pmopm8CfgChannel83PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 85),
    _Pmopm8CfgChannel83PwrlowPortn_Type()
)
pmopm8CfgChannel83PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel83PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel84PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel84PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel84PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel84PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel84PwrlowPortn = _Pmopm8CfgChannel84PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 86),
    _Pmopm8CfgChannel84PwrlowPortn_Type()
)
pmopm8CfgChannel84PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel84PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel85PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel85PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel85PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel85PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel85PwrlowPortn = _Pmopm8CfgChannel85PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 87),
    _Pmopm8CfgChannel85PwrlowPortn_Type()
)
pmopm8CfgChannel85PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel85PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel86PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel86PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel86PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel86PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel86PwrlowPortn = _Pmopm8CfgChannel86PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 88),
    _Pmopm8CfgChannel86PwrlowPortn_Type()
)
pmopm8CfgChannel86PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel86PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel87PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel87PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel87PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel87PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel87PwrlowPortn = _Pmopm8CfgChannel87PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 89),
    _Pmopm8CfgChannel87PwrlowPortn_Type()
)
pmopm8CfgChannel87PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel87PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel88PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel88PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel88PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel88PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel88PwrlowPortn = _Pmopm8CfgChannel88PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 90),
    _Pmopm8CfgChannel88PwrlowPortn_Type()
)
pmopm8CfgChannel88PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel88PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel89PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel89PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel89PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel89PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel89PwrlowPortn = _Pmopm8CfgChannel89PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 91),
    _Pmopm8CfgChannel89PwrlowPortn_Type()
)
pmopm8CfgChannel89PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel89PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel90PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel90PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel90PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel90PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel90PwrlowPortn = _Pmopm8CfgChannel90PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 92),
    _Pmopm8CfgChannel90PwrlowPortn_Type()
)
pmopm8CfgChannel90PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel90PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel91PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel91PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel91PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel91PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel91PwrlowPortn = _Pmopm8CfgChannel91PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 93),
    _Pmopm8CfgChannel91PwrlowPortn_Type()
)
pmopm8CfgChannel91PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel91PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel92PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel92PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel92PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel92PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel92PwrlowPortn = _Pmopm8CfgChannel92PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 94),
    _Pmopm8CfgChannel92PwrlowPortn_Type()
)
pmopm8CfgChannel92PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel92PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel93PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel93PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel93PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel93PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel93PwrlowPortn = _Pmopm8CfgChannel93PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 95),
    _Pmopm8CfgChannel93PwrlowPortn_Type()
)
pmopm8CfgChannel93PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel93PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel94PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel94PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel94PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel94PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel94PwrlowPortn = _Pmopm8CfgChannel94PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 96),
    _Pmopm8CfgChannel94PwrlowPortn_Type()
)
pmopm8CfgChannel94PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel94PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel95PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel95PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel95PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel95PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel95PwrlowPortn = _Pmopm8CfgChannel95PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 97),
    _Pmopm8CfgChannel95PwrlowPortn_Type()
)
pmopm8CfgChannel95PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel95PwrlowPortn.setStatus("current")


class _Pmopm8CfgChannel96PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm8CfgChannel96PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm8CfgChannel96PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm8CfgChannel96PwrlowPortn_Object = MibTableColumn
pmopm8CfgChannel96PwrlowPortn = _Pmopm8CfgChannel96PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 6, 1, 98),
    _Pmopm8CfgChannel96PwrlowPortn_Type()
)
pmopm8CfgChannel96PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgChannel96PwrlowPortn.setStatus("current")
_Pmopm8CfgLabelclientTable_Object = MibTable
pmopm8CfgLabelclientTable = _Pmopm8CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 7)
)
if mibBuilder.loadTexts:
    pmopm8CfgLabelclientTable.setStatus("current")
_Pmopm8CfgLabelclientEntry_Object = MibTableRow
pmopm8CfgLabelclientEntry = _Pmopm8CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 7, 1)
)
pmopm8CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CfgLabelclientEntry.setStatus("current")


class _Pmopm8CfgLabelclientIndex_Type(Integer32):
    """Custom type pmopm8CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmopm8CfgLabelclientIndex_Object = MibTableColumn
pmopm8CfgLabelclientIndex = _Pmopm8CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 7, 1, 1),
    _Pmopm8CfgLabelclientIndex_Type()
)
pmopm8CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgLabelclientIndex.setStatus("current")


class _Pmopm8CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmopm8CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmopm8CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmopm8CfgLabelclientPortn_Object = MibTableColumn
pmopm8CfgLabelclientPortn = _Pmopm8CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 7, 1, 3),
    _Pmopm8CfgLabelclientPortn_Type()
)
pmopm8CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgLabelclientPortn.setStatus("current")
_Pmopm8CfgLabellineTable_Object = MibTable
pmopm8CfgLabellineTable = _Pmopm8CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 8)
)
if mibBuilder.loadTexts:
    pmopm8CfgLabellineTable.setStatus("current")
_Pmopm8CfgLabellineEntry_Object = MibTableRow
pmopm8CfgLabellineEntry = _Pmopm8CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 8, 1)
)
pmopm8CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmopm8-MIB", "pmopm8CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmopm8CfgLabellineEntry.setStatus("current")


class _Pmopm8CfgLabellineIndex_Type(Integer32):
    """Custom type pmopm8CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm8CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmopm8CfgLabellineIndex_Object = MibTableColumn
pmopm8CfgLabellineIndex = _Pmopm8CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 8, 1, 1),
    _Pmopm8CfgLabellineIndex_Type()
)
pmopm8CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8CfgLabellineIndex.setStatus("current")


class _Pmopm8CfgLabellinePortn_Type(DisplayString):
    """Custom type pmopm8CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmopm8CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmopm8CfgLabellinePortn_Object = MibTableColumn
pmopm8CfgLabellinePortn = _Pmopm8CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 2, 8, 1, 3),
    _Pmopm8CfgLabellinePortn_Type()
)
pmopm8CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgLabellinePortn.setStatus("current")
_Pmopm8CfgWriteConfiguration_Type = EkiOnOff
_Pmopm8CfgWriteConfiguration_Object = MibScalar
pmopm8CfgWriteConfiguration = _Pmopm8CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 9, 257),
    _Pmopm8CfgWriteConfiguration_Type()
)
pmopm8CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm8CfgWriteConfiguration.setStatus("current")
_Pmopm8traps_ObjectIdentity = ObjectIdentity
pmopm8traps = _Pmopm8traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 66, 10)
)


class _Pmopm8trapPortNumber_Type(Integer32):
    """Custom type pmopm8trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmopm8trapPortNumber_Type.__name__ = "Integer32"
_Pmopm8trapPortNumber_Object = MibScalar
pmopm8trapPortNumber = _Pmopm8trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 10, 2),
    _Pmopm8trapPortNumber_Type()
)
pmopm8trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8trapPortNumber.setStatus("current")


class _Pmopm8trapLineNumber_Type(Integer32):
    """Custom type pmopm8trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmopm8trapLineNumber_Type.__name__ = "Integer32"
_Pmopm8trapLineNumber_Object = MibScalar
pmopm8trapLineNumber = _Pmopm8trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 10, 3),
    _Pmopm8trapLineNumber_Type()
)
pmopm8trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8trapLineNumber.setStatus("current")


class _Pmopm8trapBoardNumber_Type(Integer32):
    """Custom type pmopm8trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmopm8trapBoardNumber_Type.__name__ = "Integer32"
_Pmopm8trapBoardNumber_Object = MibScalar
pmopm8trapBoardNumber = _Pmopm8trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 66, 10, 4),
    _Pmopm8trapBoardNumber_Type()
)
pmopm8trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm8trapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmopm8PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 66, 10, 50)
)
pmopm8PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmopm8-MIB", "pmopm8AlmDefFuseB"),
        ("EKINOPS-Pmopm8-MIB", "pmopm8AlmDefFuseA"),
        ("EKINOPS-Pmopm8-MIB", "pmopm8trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopm8PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmopm8PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 66, 10, 51)
)
pmopm8PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmopm8-MIB", "pmopm8AlmDefFuseB"),
        ("EKINOPS-Pmopm8-MIB", "pmopm8AlmDefFuseA"),
        ("EKINOPS-Pmopm8-MIB", "pmopm8trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopm8PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmopm8-MIB",
    **{"Pmopm8Grid": Pmopm8Grid,
       "Pmopm8MultiRate": Pmopm8MultiRate,
       "Pmopm8OtxChannel": Pmopm8OtxChannel,
       "Pmopm8AdjustValue": Pmopm8AdjustValue,
       "Pmopm8OtxMode": Pmopm8OtxMode,
       "modulePmopm8": modulePmopm8,
       "pmopm8alarms": pmopm8alarms,
       "pmopm8AlmOther": pmopm8AlmOther,
       "pmopm8AlmOtherNurg": pmopm8AlmOtherNurg,
       "pmopm8AlmsynthAlm2": pmopm8AlmsynthAlm2,
       "pmopm8AlmConfTableSave": pmopm8AlmConfTableSave,
       "pmopm8AlmInvUpload": pmopm8AlmInvUpload,
       "pmopm8AlmConfTableLoad": pmopm8AlmConfTableLoad,
       "pmopm8AlmCorrelatOff": pmopm8AlmCorrelatOff,
       "pmopm8AlmOtherUrg": pmopm8AlmOtherUrg,
       "pmopm8AlmOtherCrit": pmopm8AlmOtherCrit,
       "pmopm8AlmsynthAlm0": pmopm8AlmsynthAlm0,
       "pmopm8AlmModGlobFail": pmopm8AlmModGlobFail,
       "pmopm8AlmDefFuseA": pmopm8AlmDefFuseA,
       "pmopm8AlmDefFuseB": pmopm8AlmDefFuseB,
       "pmopm8AlmClient": pmopm8AlmClient,
       "pmopm8AlmClientNurg": pmopm8AlmClientNurg,
       "pmopm8AlmClientUrg": pmopm8AlmClientUrg,
       "pmopm8AlmClientCrit": pmopm8AlmClientCrit,
       "pmopm8AlmsynthAlmPortTable": pmopm8AlmsynthAlmPortTable,
       "pmopm8AlmsynthAlmPortEntry": pmopm8AlmsynthAlmPortEntry,
       "pmopm8AlmsynthAlmPortIndex": pmopm8AlmsynthAlmPortIndex,
       "pmopm8AlmSpectrumAbsentPortn": pmopm8AlmSpectrumAbsentPortn,
       "pmopm8AlmSpectrumOosPortn": pmopm8AlmSpectrumOosPortn,
       "pmopm8AlmSpectrumInvalidDataPortn": pmopm8AlmSpectrumInvalidDataPortn,
       "pmopm8Almchannel1PortTable": pmopm8Almchannel1PortTable,
       "pmopm8Almchannel1PortEntry": pmopm8Almchannel1PortEntry,
       "pmopm8Almchannel1PortIndex": pmopm8Almchannel1PortIndex,
       "pmopm8AlmChannel1AbsentPortn": pmopm8AlmChannel1AbsentPortn,
       "pmopm8AlmChannel1MismatchPortn": pmopm8AlmChannel1MismatchPortn,
       "pmopm8AlmChannel1BalancedPortn": pmopm8AlmChannel1BalancedPortn,
       "pmopm8AlmChannel1PowerLowPortn": pmopm8AlmChannel1PowerLowPortn,
       "pmopm8AlmChannel1PowerHighPortn": pmopm8AlmChannel1PowerHighPortn,
       "pmopm8AlmChannel1OosPortn": pmopm8AlmChannel1OosPortn,
       "pmopm8Almchannel2PortTable": pmopm8Almchannel2PortTable,
       "pmopm8Almchannel2PortEntry": pmopm8Almchannel2PortEntry,
       "pmopm8Almchannel2PortIndex": pmopm8Almchannel2PortIndex,
       "pmopm8AlmChannel2AbsentPortn": pmopm8AlmChannel2AbsentPortn,
       "pmopm8AlmChannel2MismatchPortn": pmopm8AlmChannel2MismatchPortn,
       "pmopm8AlmChannel2BalancedPortn": pmopm8AlmChannel2BalancedPortn,
       "pmopm8AlmChannel2PowerLowPortn": pmopm8AlmChannel2PowerLowPortn,
       "pmopm8AlmChannel2PowerHighPortn": pmopm8AlmChannel2PowerHighPortn,
       "pmopm8AlmChannel2OosPortn": pmopm8AlmChannel2OosPortn,
       "pmopm8Almchannel3PortTable": pmopm8Almchannel3PortTable,
       "pmopm8Almchannel3PortEntry": pmopm8Almchannel3PortEntry,
       "pmopm8Almchannel3PortIndex": pmopm8Almchannel3PortIndex,
       "pmopm8AlmChannel3AbsentPortn": pmopm8AlmChannel3AbsentPortn,
       "pmopm8AlmChannel3MismatchPortn": pmopm8AlmChannel3MismatchPortn,
       "pmopm8AlmChannel3BalancedPortn": pmopm8AlmChannel3BalancedPortn,
       "pmopm8AlmChannel3PowerLowPortn": pmopm8AlmChannel3PowerLowPortn,
       "pmopm8AlmChannel3PowerHighPortn": pmopm8AlmChannel3PowerHighPortn,
       "pmopm8AlmChannel3OosPortn": pmopm8AlmChannel3OosPortn,
       "pmopm8Almchannel4PortTable": pmopm8Almchannel4PortTable,
       "pmopm8Almchannel4PortEntry": pmopm8Almchannel4PortEntry,
       "pmopm8Almchannel4PortIndex": pmopm8Almchannel4PortIndex,
       "pmopm8AlmChannel4AbsentPortn": pmopm8AlmChannel4AbsentPortn,
       "pmopm8AlmChannel4MismatchPortn": pmopm8AlmChannel4MismatchPortn,
       "pmopm8AlmChannel4BalancedPortn": pmopm8AlmChannel4BalancedPortn,
       "pmopm8AlmChannel4PowerLowPortn": pmopm8AlmChannel4PowerLowPortn,
       "pmopm8AlmChannel4PowerHighPortn": pmopm8AlmChannel4PowerHighPortn,
       "pmopm8AlmChannel4OosPortn": pmopm8AlmChannel4OosPortn,
       "pmopm8Almchannel5PortTable": pmopm8Almchannel5PortTable,
       "pmopm8Almchannel5PortEntry": pmopm8Almchannel5PortEntry,
       "pmopm8Almchannel5PortIndex": pmopm8Almchannel5PortIndex,
       "pmopm8AlmChannel5AbsentPortn": pmopm8AlmChannel5AbsentPortn,
       "pmopm8AlmChannel5MismatchPortn": pmopm8AlmChannel5MismatchPortn,
       "pmopm8AlmChannel5BalancedPortn": pmopm8AlmChannel5BalancedPortn,
       "pmopm8AlmChannel5PowerLowPortn": pmopm8AlmChannel5PowerLowPortn,
       "pmopm8AlmChannel5PowerHighPortn": pmopm8AlmChannel5PowerHighPortn,
       "pmopm8AlmChannel5OosPortn": pmopm8AlmChannel5OosPortn,
       "pmopm8Almchannel6PortTable": pmopm8Almchannel6PortTable,
       "pmopm8Almchannel6PortEntry": pmopm8Almchannel6PortEntry,
       "pmopm8Almchannel6PortIndex": pmopm8Almchannel6PortIndex,
       "pmopm8AlmChannel6AbsentPortn": pmopm8AlmChannel6AbsentPortn,
       "pmopm8AlmChannel6MismatchPortn": pmopm8AlmChannel6MismatchPortn,
       "pmopm8AlmChannel6BalancedPortn": pmopm8AlmChannel6BalancedPortn,
       "pmopm8AlmChannel6PowerLowPortn": pmopm8AlmChannel6PowerLowPortn,
       "pmopm8AlmChannel6PowerHighPortn": pmopm8AlmChannel6PowerHighPortn,
       "pmopm8AlmChannel6OosPortn": pmopm8AlmChannel6OosPortn,
       "pmopm8Almchannel7PortTable": pmopm8Almchannel7PortTable,
       "pmopm8Almchannel7PortEntry": pmopm8Almchannel7PortEntry,
       "pmopm8Almchannel7PortIndex": pmopm8Almchannel7PortIndex,
       "pmopm8AlmChannel7AbsentPortn": pmopm8AlmChannel7AbsentPortn,
       "pmopm8AlmChannel7MismatchPortn": pmopm8AlmChannel7MismatchPortn,
       "pmopm8AlmChannel7BalancedPortn": pmopm8AlmChannel7BalancedPortn,
       "pmopm8AlmChannel7PowerLowPortn": pmopm8AlmChannel7PowerLowPortn,
       "pmopm8AlmChannel7PowerHighPortn": pmopm8AlmChannel7PowerHighPortn,
       "pmopm8AlmChannel7OosPortn": pmopm8AlmChannel7OosPortn,
       "pmopm8Almchannel8PortTable": pmopm8Almchannel8PortTable,
       "pmopm8Almchannel8PortEntry": pmopm8Almchannel8PortEntry,
       "pmopm8Almchannel8PortIndex": pmopm8Almchannel8PortIndex,
       "pmopm8AlmChannel8AbsentPortn": pmopm8AlmChannel8AbsentPortn,
       "pmopm8AlmChannel8MismatchPortn": pmopm8AlmChannel8MismatchPortn,
       "pmopm8AlmChannel8BalancedPortn": pmopm8AlmChannel8BalancedPortn,
       "pmopm8AlmChannel8PowerLowPortn": pmopm8AlmChannel8PowerLowPortn,
       "pmopm8AlmChannel8PowerHighPortn": pmopm8AlmChannel8PowerHighPortn,
       "pmopm8AlmChannel8OosPortn": pmopm8AlmChannel8OosPortn,
       "pmopm8Almchannel9PortTable": pmopm8Almchannel9PortTable,
       "pmopm8Almchannel9PortEntry": pmopm8Almchannel9PortEntry,
       "pmopm8Almchannel9PortIndex": pmopm8Almchannel9PortIndex,
       "pmopm8AlmChannel9AbsentPortn": pmopm8AlmChannel9AbsentPortn,
       "pmopm8AlmChannel9MismatchPortn": pmopm8AlmChannel9MismatchPortn,
       "pmopm8AlmChannel9BalancedPortn": pmopm8AlmChannel9BalancedPortn,
       "pmopm8AlmChannel9PowerLowPortn": pmopm8AlmChannel9PowerLowPortn,
       "pmopm8AlmChannel9PowerHighPortn": pmopm8AlmChannel9PowerHighPortn,
       "pmopm8AlmChannel9OosPortn": pmopm8AlmChannel9OosPortn,
       "pmopm8Almchannel10PortTable": pmopm8Almchannel10PortTable,
       "pmopm8Almchannel10PortEntry": pmopm8Almchannel10PortEntry,
       "pmopm8Almchannel10PortIndex": pmopm8Almchannel10PortIndex,
       "pmopm8AlmChannel10AbsentPortn": pmopm8AlmChannel10AbsentPortn,
       "pmopm8AlmChannel10MismatchPortn": pmopm8AlmChannel10MismatchPortn,
       "pmopm8AlmChannel10BalancedPortn": pmopm8AlmChannel10BalancedPortn,
       "pmopm8AlmChannel10PowerLowPortn": pmopm8AlmChannel10PowerLowPortn,
       "pmopm8AlmChannel10PowerHighPortn": pmopm8AlmChannel10PowerHighPortn,
       "pmopm8AlmChannel10OosPortn": pmopm8AlmChannel10OosPortn,
       "pmopm8Almchannel11PortTable": pmopm8Almchannel11PortTable,
       "pmopm8Almchannel11PortEntry": pmopm8Almchannel11PortEntry,
       "pmopm8Almchannel11PortIndex": pmopm8Almchannel11PortIndex,
       "pmopm8AlmChannel11AbsentPortn": pmopm8AlmChannel11AbsentPortn,
       "pmopm8AlmChannel11MismatchPortn": pmopm8AlmChannel11MismatchPortn,
       "pmopm8AlmChannel11BalancedPortn": pmopm8AlmChannel11BalancedPortn,
       "pmopm8AlmChannel11PowerLowPortn": pmopm8AlmChannel11PowerLowPortn,
       "pmopm8AlmChannel11PowerHighPortn": pmopm8AlmChannel11PowerHighPortn,
       "pmopm8AlmChannel11OosPortn": pmopm8AlmChannel11OosPortn,
       "pmopm8Almchannel12PortTable": pmopm8Almchannel12PortTable,
       "pmopm8Almchannel12PortEntry": pmopm8Almchannel12PortEntry,
       "pmopm8Almchannel12PortIndex": pmopm8Almchannel12PortIndex,
       "pmopm8AlmChannel12AbsentPortn": pmopm8AlmChannel12AbsentPortn,
       "pmopm8AlmChannel12MismatchPortn": pmopm8AlmChannel12MismatchPortn,
       "pmopm8AlmChannel12BalancedPortn": pmopm8AlmChannel12BalancedPortn,
       "pmopm8AlmChannel12PowerLowPortn": pmopm8AlmChannel12PowerLowPortn,
       "pmopm8AlmChannel12PowerHighPortn": pmopm8AlmChannel12PowerHighPortn,
       "pmopm8AlmChannel12OosPortn": pmopm8AlmChannel12OosPortn,
       "pmopm8Almchannel13PortTable": pmopm8Almchannel13PortTable,
       "pmopm8Almchannel13PortEntry": pmopm8Almchannel13PortEntry,
       "pmopm8Almchannel13PortIndex": pmopm8Almchannel13PortIndex,
       "pmopm8AlmChannel13AbsentPortn": pmopm8AlmChannel13AbsentPortn,
       "pmopm8AlmChannel13MismatchPortn": pmopm8AlmChannel13MismatchPortn,
       "pmopm8AlmChannel13BalancedPortn": pmopm8AlmChannel13BalancedPortn,
       "pmopm8AlmChannel13PowerLowPortn": pmopm8AlmChannel13PowerLowPortn,
       "pmopm8AlmChannel13PowerHighPortn": pmopm8AlmChannel13PowerHighPortn,
       "pmopm8AlmChannel13OosPortn": pmopm8AlmChannel13OosPortn,
       "pmopm8Almchannel14PortTable": pmopm8Almchannel14PortTable,
       "pmopm8Almchannel14PortEntry": pmopm8Almchannel14PortEntry,
       "pmopm8Almchannel14PortIndex": pmopm8Almchannel14PortIndex,
       "pmopm8AlmChannel14AbsentPortn": pmopm8AlmChannel14AbsentPortn,
       "pmopm8AlmChannel14MismatchPortn": pmopm8AlmChannel14MismatchPortn,
       "pmopm8AlmChannel14BalancedPortn": pmopm8AlmChannel14BalancedPortn,
       "pmopm8AlmChannel14PowerLowPortn": pmopm8AlmChannel14PowerLowPortn,
       "pmopm8AlmChannel14PowerHighPortn": pmopm8AlmChannel14PowerHighPortn,
       "pmopm8AlmChannel14OosPortn": pmopm8AlmChannel14OosPortn,
       "pmopm8Almchannel15PortTable": pmopm8Almchannel15PortTable,
       "pmopm8Almchannel15PortEntry": pmopm8Almchannel15PortEntry,
       "pmopm8Almchannel15PortIndex": pmopm8Almchannel15PortIndex,
       "pmopm8AlmChannel15AbsentPortn": pmopm8AlmChannel15AbsentPortn,
       "pmopm8AlmChannel15MismatchPortn": pmopm8AlmChannel15MismatchPortn,
       "pmopm8AlmChannel15BalancedPortn": pmopm8AlmChannel15BalancedPortn,
       "pmopm8AlmChannel15PowerLowPortn": pmopm8AlmChannel15PowerLowPortn,
       "pmopm8AlmChannel15PowerHighPortn": pmopm8AlmChannel15PowerHighPortn,
       "pmopm8AlmChannel15OosPortn": pmopm8AlmChannel15OosPortn,
       "pmopm8Almchannel16PortTable": pmopm8Almchannel16PortTable,
       "pmopm8Almchannel16PortEntry": pmopm8Almchannel16PortEntry,
       "pmopm8Almchannel16PortIndex": pmopm8Almchannel16PortIndex,
       "pmopm8AlmChannel16AbsentPortn": pmopm8AlmChannel16AbsentPortn,
       "pmopm8AlmChannel16MismatchPortn": pmopm8AlmChannel16MismatchPortn,
       "pmopm8AlmChannel16BalancedPortn": pmopm8AlmChannel16BalancedPortn,
       "pmopm8AlmChannel16PowerLowPortn": pmopm8AlmChannel16PowerLowPortn,
       "pmopm8AlmChannel16PowerHighPortn": pmopm8AlmChannel16PowerHighPortn,
       "pmopm8AlmChannel16OosPortn": pmopm8AlmChannel16OosPortn,
       "pmopm8Almchannel17PortTable": pmopm8Almchannel17PortTable,
       "pmopm8Almchannel17PortEntry": pmopm8Almchannel17PortEntry,
       "pmopm8Almchannel17PortIndex": pmopm8Almchannel17PortIndex,
       "pmopm8AlmChannel17AbsentPortn": pmopm8AlmChannel17AbsentPortn,
       "pmopm8AlmChannel17MismatchPortn": pmopm8AlmChannel17MismatchPortn,
       "pmopm8AlmChannel17BalancedPortn": pmopm8AlmChannel17BalancedPortn,
       "pmopm8AlmChannel17PowerLowPortn": pmopm8AlmChannel17PowerLowPortn,
       "pmopm8AlmChannel17PowerHighPortn": pmopm8AlmChannel17PowerHighPortn,
       "pmopm8AlmChannel17OosPortn": pmopm8AlmChannel17OosPortn,
       "pmopm8Almchannel18PortTable": pmopm8Almchannel18PortTable,
       "pmopm8Almchannel18PortEntry": pmopm8Almchannel18PortEntry,
       "pmopm8Almchannel18PortIndex": pmopm8Almchannel18PortIndex,
       "pmopm8AlmChannel18AbsentPortn": pmopm8AlmChannel18AbsentPortn,
       "pmopm8AlmChannel18MismatchPortn": pmopm8AlmChannel18MismatchPortn,
       "pmopm8AlmChannel18BalancedPortn": pmopm8AlmChannel18BalancedPortn,
       "pmopm8AlmChannel18PowerLowPortn": pmopm8AlmChannel18PowerLowPortn,
       "pmopm8AlmChannel18PowerHighPortn": pmopm8AlmChannel18PowerHighPortn,
       "pmopm8AlmChannel18OosPortn": pmopm8AlmChannel18OosPortn,
       "pmopm8Almchannel19PortTable": pmopm8Almchannel19PortTable,
       "pmopm8Almchannel19PortEntry": pmopm8Almchannel19PortEntry,
       "pmopm8Almchannel19PortIndex": pmopm8Almchannel19PortIndex,
       "pmopm8AlmChannel19AbsentPortn": pmopm8AlmChannel19AbsentPortn,
       "pmopm8AlmChannel19MismatchPortn": pmopm8AlmChannel19MismatchPortn,
       "pmopm8AlmChannel19BalancedPortn": pmopm8AlmChannel19BalancedPortn,
       "pmopm8AlmChannel19PowerLowPortn": pmopm8AlmChannel19PowerLowPortn,
       "pmopm8AlmChannel19PowerHighPortn": pmopm8AlmChannel19PowerHighPortn,
       "pmopm8AlmChannel19OosPortn": pmopm8AlmChannel19OosPortn,
       "pmopm8Almchannel20PortTable": pmopm8Almchannel20PortTable,
       "pmopm8Almchannel20PortEntry": pmopm8Almchannel20PortEntry,
       "pmopm8Almchannel20PortIndex": pmopm8Almchannel20PortIndex,
       "pmopm8AlmChannel20AbsentPortn": pmopm8AlmChannel20AbsentPortn,
       "pmopm8AlmChannel20MismatchPortn": pmopm8AlmChannel20MismatchPortn,
       "pmopm8AlmChannel20BalancedPortn": pmopm8AlmChannel20BalancedPortn,
       "pmopm8AlmChannel20PowerLowPortn": pmopm8AlmChannel20PowerLowPortn,
       "pmopm8AlmChannel20PowerHighPortn": pmopm8AlmChannel20PowerHighPortn,
       "pmopm8AlmChannel20OosPortn": pmopm8AlmChannel20OosPortn,
       "pmopm8Almchannel21PortTable": pmopm8Almchannel21PortTable,
       "pmopm8Almchannel21PortEntry": pmopm8Almchannel21PortEntry,
       "pmopm8Almchannel21PortIndex": pmopm8Almchannel21PortIndex,
       "pmopm8AlmChannel21AbsentPortn": pmopm8AlmChannel21AbsentPortn,
       "pmopm8AlmChannel21MismatchPortn": pmopm8AlmChannel21MismatchPortn,
       "pmopm8AlmChannel21BalancedPortn": pmopm8AlmChannel21BalancedPortn,
       "pmopm8AlmChannel21PowerLowPortn": pmopm8AlmChannel21PowerLowPortn,
       "pmopm8AlmChannel21PowerHighPortn": pmopm8AlmChannel21PowerHighPortn,
       "pmopm8AlmChannel21OosPortn": pmopm8AlmChannel21OosPortn,
       "pmopm8Almchannel22PortTable": pmopm8Almchannel22PortTable,
       "pmopm8Almchannel22PortEntry": pmopm8Almchannel22PortEntry,
       "pmopm8Almchannel22PortIndex": pmopm8Almchannel22PortIndex,
       "pmopm8AlmChannel22AbsentPortn": pmopm8AlmChannel22AbsentPortn,
       "pmopm8AlmChannel22MismatchPortn": pmopm8AlmChannel22MismatchPortn,
       "pmopm8AlmChannel22BalancedPortn": pmopm8AlmChannel22BalancedPortn,
       "pmopm8AlmChannel22PowerLowPortn": pmopm8AlmChannel22PowerLowPortn,
       "pmopm8AlmChannel22PowerHighPortn": pmopm8AlmChannel22PowerHighPortn,
       "pmopm8AlmChannel22OosPortn": pmopm8AlmChannel22OosPortn,
       "pmopm8Almchannel23PortTable": pmopm8Almchannel23PortTable,
       "pmopm8Almchannel23PortEntry": pmopm8Almchannel23PortEntry,
       "pmopm8Almchannel23PortIndex": pmopm8Almchannel23PortIndex,
       "pmopm8AlmChannel23AbsentPortn": pmopm8AlmChannel23AbsentPortn,
       "pmopm8AlmChannel23MismatchPortn": pmopm8AlmChannel23MismatchPortn,
       "pmopm8AlmChannel23BalancedPortn": pmopm8AlmChannel23BalancedPortn,
       "pmopm8AlmChannel23PowerLowPortn": pmopm8AlmChannel23PowerLowPortn,
       "pmopm8AlmChannel23PowerHighPortn": pmopm8AlmChannel23PowerHighPortn,
       "pmopm8AlmChannel23OosPortn": pmopm8AlmChannel23OosPortn,
       "pmopm8Almchannel24PortTable": pmopm8Almchannel24PortTable,
       "pmopm8Almchannel24PortEntry": pmopm8Almchannel24PortEntry,
       "pmopm8Almchannel24PortIndex": pmopm8Almchannel24PortIndex,
       "pmopm8AlmChannel24AbsentPortn": pmopm8AlmChannel24AbsentPortn,
       "pmopm8AlmChannel24MismatchPortn": pmopm8AlmChannel24MismatchPortn,
       "pmopm8AlmChannel24BalancedPortn": pmopm8AlmChannel24BalancedPortn,
       "pmopm8AlmChannel24PowerLowPortn": pmopm8AlmChannel24PowerLowPortn,
       "pmopm8AlmChannel24PowerHighPortn": pmopm8AlmChannel24PowerHighPortn,
       "pmopm8AlmChannel24OosPortn": pmopm8AlmChannel24OosPortn,
       "pmopm8Almchannel25PortTable": pmopm8Almchannel25PortTable,
       "pmopm8Almchannel25PortEntry": pmopm8Almchannel25PortEntry,
       "pmopm8Almchannel25PortIndex": pmopm8Almchannel25PortIndex,
       "pmopm8AlmChannel25AbsentPortn": pmopm8AlmChannel25AbsentPortn,
       "pmopm8AlmChannel25MismatchPortn": pmopm8AlmChannel25MismatchPortn,
       "pmopm8AlmChannel25BalancedPortn": pmopm8AlmChannel25BalancedPortn,
       "pmopm8AlmChannel25PowerLowPortn": pmopm8AlmChannel25PowerLowPortn,
       "pmopm8AlmChannel25PowerHighPortn": pmopm8AlmChannel25PowerHighPortn,
       "pmopm8AlmChannel25OosPortn": pmopm8AlmChannel25OosPortn,
       "pmopm8Almchannel26PortTable": pmopm8Almchannel26PortTable,
       "pmopm8Almchannel26PortEntry": pmopm8Almchannel26PortEntry,
       "pmopm8Almchannel26PortIndex": pmopm8Almchannel26PortIndex,
       "pmopm8AlmChannel26AbsentPortn": pmopm8AlmChannel26AbsentPortn,
       "pmopm8AlmChannel26MismatchPortn": pmopm8AlmChannel26MismatchPortn,
       "pmopm8AlmChannel26BalancedPortn": pmopm8AlmChannel26BalancedPortn,
       "pmopm8AlmChannel26PowerLowPortn": pmopm8AlmChannel26PowerLowPortn,
       "pmopm8AlmChannel26PowerHighPortn": pmopm8AlmChannel26PowerHighPortn,
       "pmopm8AlmChannel26OosPortn": pmopm8AlmChannel26OosPortn,
       "pmopm8Almchannel27PortTable": pmopm8Almchannel27PortTable,
       "pmopm8Almchannel27PortEntry": pmopm8Almchannel27PortEntry,
       "pmopm8Almchannel27PortIndex": pmopm8Almchannel27PortIndex,
       "pmopm8AlmChannel27AbsentPortn": pmopm8AlmChannel27AbsentPortn,
       "pmopm8AlmChannel27MismatchPortn": pmopm8AlmChannel27MismatchPortn,
       "pmopm8AlmChannel27BalancedPortn": pmopm8AlmChannel27BalancedPortn,
       "pmopm8AlmChannel27PowerLowPortn": pmopm8AlmChannel27PowerLowPortn,
       "pmopm8AlmChannel27PowerHighPortn": pmopm8AlmChannel27PowerHighPortn,
       "pmopm8AlmChannel27OosPortn": pmopm8AlmChannel27OosPortn,
       "pmopm8Almchannel28PortTable": pmopm8Almchannel28PortTable,
       "pmopm8Almchannel28PortEntry": pmopm8Almchannel28PortEntry,
       "pmopm8Almchannel28PortIndex": pmopm8Almchannel28PortIndex,
       "pmopm8AlmChannel28AbsentPortn": pmopm8AlmChannel28AbsentPortn,
       "pmopm8AlmChannel28MismatchPortn": pmopm8AlmChannel28MismatchPortn,
       "pmopm8AlmChannel28BalancedPortn": pmopm8AlmChannel28BalancedPortn,
       "pmopm8AlmChannel28PowerLowPortn": pmopm8AlmChannel28PowerLowPortn,
       "pmopm8AlmChannel28PowerHighPortn": pmopm8AlmChannel28PowerHighPortn,
       "pmopm8AlmChannel28OosPortn": pmopm8AlmChannel28OosPortn,
       "pmopm8Almchannel29PortTable": pmopm8Almchannel29PortTable,
       "pmopm8Almchannel29PortEntry": pmopm8Almchannel29PortEntry,
       "pmopm8Almchannel29PortIndex": pmopm8Almchannel29PortIndex,
       "pmopm8AlmChannel29AbsentPortn": pmopm8AlmChannel29AbsentPortn,
       "pmopm8AlmChannel29MismatchPortn": pmopm8AlmChannel29MismatchPortn,
       "pmopm8AlmChannel29BalancedPortn": pmopm8AlmChannel29BalancedPortn,
       "pmopm8AlmChannel29PowerLowPortn": pmopm8AlmChannel29PowerLowPortn,
       "pmopm8AlmChannel29PowerHighPortn": pmopm8AlmChannel29PowerHighPortn,
       "pmopm8AlmChannel29OosPortn": pmopm8AlmChannel29OosPortn,
       "pmopm8Almchannel30PortTable": pmopm8Almchannel30PortTable,
       "pmopm8Almchannel30PortEntry": pmopm8Almchannel30PortEntry,
       "pmopm8Almchannel30PortIndex": pmopm8Almchannel30PortIndex,
       "pmopm8AlmChannel30AbsentPortn": pmopm8AlmChannel30AbsentPortn,
       "pmopm8AlmChannel30MismatchPortn": pmopm8AlmChannel30MismatchPortn,
       "pmopm8AlmChannel30BalancedPortn": pmopm8AlmChannel30BalancedPortn,
       "pmopm8AlmChannel30PowerLowPortn": pmopm8AlmChannel30PowerLowPortn,
       "pmopm8AlmChannel30PowerHighPortn": pmopm8AlmChannel30PowerHighPortn,
       "pmopm8AlmChannel30OosPortn": pmopm8AlmChannel30OosPortn,
       "pmopm8Almchannel31PortTable": pmopm8Almchannel31PortTable,
       "pmopm8Almchannel31PortEntry": pmopm8Almchannel31PortEntry,
       "pmopm8Almchannel31PortIndex": pmopm8Almchannel31PortIndex,
       "pmopm8AlmChannel31AbsentPortn": pmopm8AlmChannel31AbsentPortn,
       "pmopm8AlmChannel31MismatchPortn": pmopm8AlmChannel31MismatchPortn,
       "pmopm8AlmChannel31BalancedPortn": pmopm8AlmChannel31BalancedPortn,
       "pmopm8AlmChannel31PowerLowPortn": pmopm8AlmChannel31PowerLowPortn,
       "pmopm8AlmChannel31PowerHighPortn": pmopm8AlmChannel31PowerHighPortn,
       "pmopm8AlmChannel31OosPortn": pmopm8AlmChannel31OosPortn,
       "pmopm8Almchannel32PortTable": pmopm8Almchannel32PortTable,
       "pmopm8Almchannel32PortEntry": pmopm8Almchannel32PortEntry,
       "pmopm8Almchannel32PortIndex": pmopm8Almchannel32PortIndex,
       "pmopm8AlmChannel32AbsentPortn": pmopm8AlmChannel32AbsentPortn,
       "pmopm8AlmChannel32MismatchPortn": pmopm8AlmChannel32MismatchPortn,
       "pmopm8AlmChannel32BalancedPortn": pmopm8AlmChannel32BalancedPortn,
       "pmopm8AlmChannel32PowerLowPortn": pmopm8AlmChannel32PowerLowPortn,
       "pmopm8AlmChannel32PowerHighPortn": pmopm8AlmChannel32PowerHighPortn,
       "pmopm8AlmChannel32OosPortn": pmopm8AlmChannel32OosPortn,
       "pmopm8Almchannel33PortTable": pmopm8Almchannel33PortTable,
       "pmopm8Almchannel33PortEntry": pmopm8Almchannel33PortEntry,
       "pmopm8Almchannel33PortIndex": pmopm8Almchannel33PortIndex,
       "pmopm8AlmChannel33AbsentPortn": pmopm8AlmChannel33AbsentPortn,
       "pmopm8AlmChannel33MismatchPortn": pmopm8AlmChannel33MismatchPortn,
       "pmopm8AlmChannel33BalancedPortn": pmopm8AlmChannel33BalancedPortn,
       "pmopm8AlmChannel33PowerLowPortn": pmopm8AlmChannel33PowerLowPortn,
       "pmopm8AlmChannel33PowerHighPortn": pmopm8AlmChannel33PowerHighPortn,
       "pmopm8AlmChannel33OosPortn": pmopm8AlmChannel33OosPortn,
       "pmopm8Almchannel34PortTable": pmopm8Almchannel34PortTable,
       "pmopm8Almchannel34PortEntry": pmopm8Almchannel34PortEntry,
       "pmopm8Almchannel34PortIndex": pmopm8Almchannel34PortIndex,
       "pmopm8AlmChannel34AbsentPortn": pmopm8AlmChannel34AbsentPortn,
       "pmopm8AlmChannel34MismatchPortn": pmopm8AlmChannel34MismatchPortn,
       "pmopm8AlmChannel34BalancedPortn": pmopm8AlmChannel34BalancedPortn,
       "pmopm8AlmChannel34PowerLowPortn": pmopm8AlmChannel34PowerLowPortn,
       "pmopm8AlmChannel34PowerHighPortn": pmopm8AlmChannel34PowerHighPortn,
       "pmopm8AlmChannel34OosPortn": pmopm8AlmChannel34OosPortn,
       "pmopm8Almchannel35PortTable": pmopm8Almchannel35PortTable,
       "pmopm8Almchannel35PortEntry": pmopm8Almchannel35PortEntry,
       "pmopm8Almchannel35PortIndex": pmopm8Almchannel35PortIndex,
       "pmopm8AlmChannel35AbsentPortn": pmopm8AlmChannel35AbsentPortn,
       "pmopm8AlmChannel35MismatchPortn": pmopm8AlmChannel35MismatchPortn,
       "pmopm8AlmChannel35BalancedPortn": pmopm8AlmChannel35BalancedPortn,
       "pmopm8AlmChannel35PowerLowPortn": pmopm8AlmChannel35PowerLowPortn,
       "pmopm8AlmChannel35PowerHighPortn": pmopm8AlmChannel35PowerHighPortn,
       "pmopm8AlmChannel35OosPortn": pmopm8AlmChannel35OosPortn,
       "pmopm8Almchannel36PortTable": pmopm8Almchannel36PortTable,
       "pmopm8Almchannel36PortEntry": pmopm8Almchannel36PortEntry,
       "pmopm8Almchannel36PortIndex": pmopm8Almchannel36PortIndex,
       "pmopm8AlmChannel36AbsentPortn": pmopm8AlmChannel36AbsentPortn,
       "pmopm8AlmChannel36MismatchPortn": pmopm8AlmChannel36MismatchPortn,
       "pmopm8AlmChannel36BalancedPortn": pmopm8AlmChannel36BalancedPortn,
       "pmopm8AlmChannel36PowerLowPortn": pmopm8AlmChannel36PowerLowPortn,
       "pmopm8AlmChannel36PowerHighPortn": pmopm8AlmChannel36PowerHighPortn,
       "pmopm8AlmChannel36OosPortn": pmopm8AlmChannel36OosPortn,
       "pmopm8Almchannel37PortTable": pmopm8Almchannel37PortTable,
       "pmopm8Almchannel37PortEntry": pmopm8Almchannel37PortEntry,
       "pmopm8Almchannel37PortIndex": pmopm8Almchannel37PortIndex,
       "pmopm8AlmChannel37AbsentPortn": pmopm8AlmChannel37AbsentPortn,
       "pmopm8AlmChannel37MismatchPortn": pmopm8AlmChannel37MismatchPortn,
       "pmopm8AlmChannel37BalancedPortn": pmopm8AlmChannel37BalancedPortn,
       "pmopm8AlmChannel37PowerLowPortn": pmopm8AlmChannel37PowerLowPortn,
       "pmopm8AlmChannel37PowerHighPortn": pmopm8AlmChannel37PowerHighPortn,
       "pmopm8AlmChannel37OosPortn": pmopm8AlmChannel37OosPortn,
       "pmopm8Almchannel38PortTable": pmopm8Almchannel38PortTable,
       "pmopm8Almchannel38PortEntry": pmopm8Almchannel38PortEntry,
       "pmopm8Almchannel38PortIndex": pmopm8Almchannel38PortIndex,
       "pmopm8AlmChannel38AbsentPortn": pmopm8AlmChannel38AbsentPortn,
       "pmopm8AlmChannel38MismatchPortn": pmopm8AlmChannel38MismatchPortn,
       "pmopm8AlmChannel38BalancedPortn": pmopm8AlmChannel38BalancedPortn,
       "pmopm8AlmChannel38PowerLowPortn": pmopm8AlmChannel38PowerLowPortn,
       "pmopm8AlmChannel38PowerHighPortn": pmopm8AlmChannel38PowerHighPortn,
       "pmopm8AlmChannel38OosPortn": pmopm8AlmChannel38OosPortn,
       "pmopm8Almchannel39PortTable": pmopm8Almchannel39PortTable,
       "pmopm8Almchannel39PortEntry": pmopm8Almchannel39PortEntry,
       "pmopm8Almchannel39PortIndex": pmopm8Almchannel39PortIndex,
       "pmopm8AlmChannel39AbsentPortn": pmopm8AlmChannel39AbsentPortn,
       "pmopm8AlmChannel39MismatchPortn": pmopm8AlmChannel39MismatchPortn,
       "pmopm8AlmChannel39BalancedPortn": pmopm8AlmChannel39BalancedPortn,
       "pmopm8AlmChannel39PowerLowPortn": pmopm8AlmChannel39PowerLowPortn,
       "pmopm8AlmChannel39PowerHighPortn": pmopm8AlmChannel39PowerHighPortn,
       "pmopm8AlmChannel39OosPortn": pmopm8AlmChannel39OosPortn,
       "pmopm8Almchannel40PortTable": pmopm8Almchannel40PortTable,
       "pmopm8Almchannel40PortEntry": pmopm8Almchannel40PortEntry,
       "pmopm8Almchannel40PortIndex": pmopm8Almchannel40PortIndex,
       "pmopm8AlmChannel40AbsentPortn": pmopm8AlmChannel40AbsentPortn,
       "pmopm8AlmChannel40MismatchPortn": pmopm8AlmChannel40MismatchPortn,
       "pmopm8AlmChannel40BalancedPortn": pmopm8AlmChannel40BalancedPortn,
       "pmopm8AlmChannel40PowerLowPortn": pmopm8AlmChannel40PowerLowPortn,
       "pmopm8AlmChannel40PowerHighPortn": pmopm8AlmChannel40PowerHighPortn,
       "pmopm8AlmChannel40OosPortn": pmopm8AlmChannel40OosPortn,
       "pmopm8Almchannel41PortTable": pmopm8Almchannel41PortTable,
       "pmopm8Almchannel41PortEntry": pmopm8Almchannel41PortEntry,
       "pmopm8Almchannel41PortIndex": pmopm8Almchannel41PortIndex,
       "pmopm8AlmChannel41AbsentPortn": pmopm8AlmChannel41AbsentPortn,
       "pmopm8AlmChannel41MismatchPortn": pmopm8AlmChannel41MismatchPortn,
       "pmopm8AlmChannel41BalancedPortn": pmopm8AlmChannel41BalancedPortn,
       "pmopm8AlmChannel41PowerLowPortn": pmopm8AlmChannel41PowerLowPortn,
       "pmopm8AlmChannel41PowerHighPortn": pmopm8AlmChannel41PowerHighPortn,
       "pmopm8AlmChannel41OosPortn": pmopm8AlmChannel41OosPortn,
       "pmopm8Almchannel42PortTable": pmopm8Almchannel42PortTable,
       "pmopm8Almchannel42PortEntry": pmopm8Almchannel42PortEntry,
       "pmopm8Almchannel42PortIndex": pmopm8Almchannel42PortIndex,
       "pmopm8AlmChannel42AbsentPortn": pmopm8AlmChannel42AbsentPortn,
       "pmopm8AlmChannel42MismatchPortn": pmopm8AlmChannel42MismatchPortn,
       "pmopm8AlmChannel42BalancedPortn": pmopm8AlmChannel42BalancedPortn,
       "pmopm8AlmChannel42PowerLowPortn": pmopm8AlmChannel42PowerLowPortn,
       "pmopm8AlmChannel42PowerHighPortn": pmopm8AlmChannel42PowerHighPortn,
       "pmopm8AlmChannel42OosPortn": pmopm8AlmChannel42OosPortn,
       "pmopm8Almchannel43PortTable": pmopm8Almchannel43PortTable,
       "pmopm8Almchannel43PortEntry": pmopm8Almchannel43PortEntry,
       "pmopm8Almchannel43PortIndex": pmopm8Almchannel43PortIndex,
       "pmopm8AlmChannel43AbsentPortn": pmopm8AlmChannel43AbsentPortn,
       "pmopm8AlmChannel43MismatchPortn": pmopm8AlmChannel43MismatchPortn,
       "pmopm8AlmChannel43BalancedPortn": pmopm8AlmChannel43BalancedPortn,
       "pmopm8AlmChannel43PowerLowPortn": pmopm8AlmChannel43PowerLowPortn,
       "pmopm8AlmChannel43PowerHighPortn": pmopm8AlmChannel43PowerHighPortn,
       "pmopm8AlmChannel43OosPortn": pmopm8AlmChannel43OosPortn,
       "pmopm8Almchannel44PortTable": pmopm8Almchannel44PortTable,
       "pmopm8Almchannel44PortEntry": pmopm8Almchannel44PortEntry,
       "pmopm8Almchannel44PortIndex": pmopm8Almchannel44PortIndex,
       "pmopm8AlmChannel44AbsentPortn": pmopm8AlmChannel44AbsentPortn,
       "pmopm8AlmChannel44MismatchPortn": pmopm8AlmChannel44MismatchPortn,
       "pmopm8AlmChannel44BalancedPortn": pmopm8AlmChannel44BalancedPortn,
       "pmopm8AlmChannel44PowerLowPortn": pmopm8AlmChannel44PowerLowPortn,
       "pmopm8AlmChannel44PowerHighPortn": pmopm8AlmChannel44PowerHighPortn,
       "pmopm8AlmChannel44OosPortn": pmopm8AlmChannel44OosPortn,
       "pmopm8Almchannel45PortTable": pmopm8Almchannel45PortTable,
       "pmopm8Almchannel45PortEntry": pmopm8Almchannel45PortEntry,
       "pmopm8Almchannel45PortIndex": pmopm8Almchannel45PortIndex,
       "pmopm8AlmChannel45AbsentPortn": pmopm8AlmChannel45AbsentPortn,
       "pmopm8AlmChannel45MismatchPortn": pmopm8AlmChannel45MismatchPortn,
       "pmopm8AlmChannel45BalancedPortn": pmopm8AlmChannel45BalancedPortn,
       "pmopm8AlmChannel45PowerLowPortn": pmopm8AlmChannel45PowerLowPortn,
       "pmopm8AlmChannel45PowerHighPortn": pmopm8AlmChannel45PowerHighPortn,
       "pmopm8AlmChannel45OosPortn": pmopm8AlmChannel45OosPortn,
       "pmopm8Almchannel46PortTable": pmopm8Almchannel46PortTable,
       "pmopm8Almchannel46PortEntry": pmopm8Almchannel46PortEntry,
       "pmopm8Almchannel46PortIndex": pmopm8Almchannel46PortIndex,
       "pmopm8AlmChannel46AbsentPortn": pmopm8AlmChannel46AbsentPortn,
       "pmopm8AlmChannel46MismatchPortn": pmopm8AlmChannel46MismatchPortn,
       "pmopm8AlmChannel46BalancedPortn": pmopm8AlmChannel46BalancedPortn,
       "pmopm8AlmChannel46PowerLowPortn": pmopm8AlmChannel46PowerLowPortn,
       "pmopm8AlmChannel46PowerHighPortn": pmopm8AlmChannel46PowerHighPortn,
       "pmopm8AlmChannel46OosPortn": pmopm8AlmChannel46OosPortn,
       "pmopm8Almchannel47PortTable": pmopm8Almchannel47PortTable,
       "pmopm8Almchannel47PortEntry": pmopm8Almchannel47PortEntry,
       "pmopm8Almchannel47PortIndex": pmopm8Almchannel47PortIndex,
       "pmopm8AlmChannel47AbsentPortn": pmopm8AlmChannel47AbsentPortn,
       "pmopm8AlmChannel47MismatchPortn": pmopm8AlmChannel47MismatchPortn,
       "pmopm8AlmChannel47BalancedPortn": pmopm8AlmChannel47BalancedPortn,
       "pmopm8AlmChannel47PowerLowPortn": pmopm8AlmChannel47PowerLowPortn,
       "pmopm8AlmChannel47PowerHighPortn": pmopm8AlmChannel47PowerHighPortn,
       "pmopm8AlmChannel47OosPortn": pmopm8AlmChannel47OosPortn,
       "pmopm8Almchannel48PortTable": pmopm8Almchannel48PortTable,
       "pmopm8Almchannel48PortEntry": pmopm8Almchannel48PortEntry,
       "pmopm8Almchannel48PortIndex": pmopm8Almchannel48PortIndex,
       "pmopm8AlmChannel48AbsentPortn": pmopm8AlmChannel48AbsentPortn,
       "pmopm8AlmChannel48MismatchPortn": pmopm8AlmChannel48MismatchPortn,
       "pmopm8AlmChannel48BalancedPortn": pmopm8AlmChannel48BalancedPortn,
       "pmopm8AlmChannel48PowerLowPortn": pmopm8AlmChannel48PowerLowPortn,
       "pmopm8AlmChannel48PowerHighPortn": pmopm8AlmChannel48PowerHighPortn,
       "pmopm8AlmChannel48OosPortn": pmopm8AlmChannel48OosPortn,
       "pmopm8Almchannel49PortTable": pmopm8Almchannel49PortTable,
       "pmopm8Almchannel49PortEntry": pmopm8Almchannel49PortEntry,
       "pmopm8Almchannel49PortIndex": pmopm8Almchannel49PortIndex,
       "pmopm8AlmChannel49AbsentPortn": pmopm8AlmChannel49AbsentPortn,
       "pmopm8AlmChannel49MismatchPortn": pmopm8AlmChannel49MismatchPortn,
       "pmopm8AlmChannel49BalancedPortn": pmopm8AlmChannel49BalancedPortn,
       "pmopm8AlmChannel49PowerLowPortn": pmopm8AlmChannel49PowerLowPortn,
       "pmopm8AlmChannel49PowerHighPortn": pmopm8AlmChannel49PowerHighPortn,
       "pmopm8AlmChannel49OosPortn": pmopm8AlmChannel49OosPortn,
       "pmopm8Almchannel50PortTable": pmopm8Almchannel50PortTable,
       "pmopm8Almchannel50PortEntry": pmopm8Almchannel50PortEntry,
       "pmopm8Almchannel50PortIndex": pmopm8Almchannel50PortIndex,
       "pmopm8AlmChannel50AbsentPortn": pmopm8AlmChannel50AbsentPortn,
       "pmopm8AlmChannel50MismatchPortn": pmopm8AlmChannel50MismatchPortn,
       "pmopm8AlmChannel50BalancedPortn": pmopm8AlmChannel50BalancedPortn,
       "pmopm8AlmChannel50PowerLowPortn": pmopm8AlmChannel50PowerLowPortn,
       "pmopm8AlmChannel50PowerHighPortn": pmopm8AlmChannel50PowerHighPortn,
       "pmopm8AlmChannel50OosPortn": pmopm8AlmChannel50OosPortn,
       "pmopm8Almchannel51PortTable": pmopm8Almchannel51PortTable,
       "pmopm8Almchannel51PortEntry": pmopm8Almchannel51PortEntry,
       "pmopm8Almchannel51PortIndex": pmopm8Almchannel51PortIndex,
       "pmopm8AlmChannel51AbsentPortn": pmopm8AlmChannel51AbsentPortn,
       "pmopm8AlmChannel51MismatchPortn": pmopm8AlmChannel51MismatchPortn,
       "pmopm8AlmChannel51BalancedPortn": pmopm8AlmChannel51BalancedPortn,
       "pmopm8AlmChannel51PowerLowPortn": pmopm8AlmChannel51PowerLowPortn,
       "pmopm8AlmChannel51PowerHighPortn": pmopm8AlmChannel51PowerHighPortn,
       "pmopm8AlmChannel51OosPortn": pmopm8AlmChannel51OosPortn,
       "pmopm8Almchannel52PortTable": pmopm8Almchannel52PortTable,
       "pmopm8Almchannel52PortEntry": pmopm8Almchannel52PortEntry,
       "pmopm8Almchannel52PortIndex": pmopm8Almchannel52PortIndex,
       "pmopm8AlmChannel52AbsentPortn": pmopm8AlmChannel52AbsentPortn,
       "pmopm8AlmChannel52MismatchPortn": pmopm8AlmChannel52MismatchPortn,
       "pmopm8AlmChannel52BalancedPortn": pmopm8AlmChannel52BalancedPortn,
       "pmopm8AlmChannel52PowerLowPortn": pmopm8AlmChannel52PowerLowPortn,
       "pmopm8AlmChannel52PowerHighPortn": pmopm8AlmChannel52PowerHighPortn,
       "pmopm8AlmChannel52OosPortn": pmopm8AlmChannel52OosPortn,
       "pmopm8Almchannel53PortTable": pmopm8Almchannel53PortTable,
       "pmopm8Almchannel53PortEntry": pmopm8Almchannel53PortEntry,
       "pmopm8Almchannel53PortIndex": pmopm8Almchannel53PortIndex,
       "pmopm8AlmChannel53AbsentPortn": pmopm8AlmChannel53AbsentPortn,
       "pmopm8AlmChannel53MismatchPortn": pmopm8AlmChannel53MismatchPortn,
       "pmopm8AlmChannel53BalancedPortn": pmopm8AlmChannel53BalancedPortn,
       "pmopm8AlmChannel53PowerLowPortn": pmopm8AlmChannel53PowerLowPortn,
       "pmopm8AlmChannel53PowerHighPortn": pmopm8AlmChannel53PowerHighPortn,
       "pmopm8AlmChannel53OosPortn": pmopm8AlmChannel53OosPortn,
       "pmopm8Almchannel54PortTable": pmopm8Almchannel54PortTable,
       "pmopm8Almchannel54PortEntry": pmopm8Almchannel54PortEntry,
       "pmopm8Almchannel54PortIndex": pmopm8Almchannel54PortIndex,
       "pmopm8AlmChannel54AbsentPortn": pmopm8AlmChannel54AbsentPortn,
       "pmopm8AlmChannel54MismatchPortn": pmopm8AlmChannel54MismatchPortn,
       "pmopm8AlmChannel54BalancedPortn": pmopm8AlmChannel54BalancedPortn,
       "pmopm8AlmChannel54PowerLowPortn": pmopm8AlmChannel54PowerLowPortn,
       "pmopm8AlmChannel54PowerHighPortn": pmopm8AlmChannel54PowerHighPortn,
       "pmopm8AlmChannel54OosPortn": pmopm8AlmChannel54OosPortn,
       "pmopm8Almchannel55PortTable": pmopm8Almchannel55PortTable,
       "pmopm8Almchannel55PortEntry": pmopm8Almchannel55PortEntry,
       "pmopm8Almchannel55PortIndex": pmopm8Almchannel55PortIndex,
       "pmopm8AlmChannel55AbsentPortn": pmopm8AlmChannel55AbsentPortn,
       "pmopm8AlmChannel55MismatchPortn": pmopm8AlmChannel55MismatchPortn,
       "pmopm8AlmChannel55BalancedPortn": pmopm8AlmChannel55BalancedPortn,
       "pmopm8AlmChannel55PowerLowPortn": pmopm8AlmChannel55PowerLowPortn,
       "pmopm8AlmChannel55PowerHighPortn": pmopm8AlmChannel55PowerHighPortn,
       "pmopm8AlmChannel55OosPortn": pmopm8AlmChannel55OosPortn,
       "pmopm8Almchannel56PortTable": pmopm8Almchannel56PortTable,
       "pmopm8Almchannel56PortEntry": pmopm8Almchannel56PortEntry,
       "pmopm8Almchannel56PortIndex": pmopm8Almchannel56PortIndex,
       "pmopm8AlmChannel56AbsentPortn": pmopm8AlmChannel56AbsentPortn,
       "pmopm8AlmChannel56MismatchPortn": pmopm8AlmChannel56MismatchPortn,
       "pmopm8AlmChannel56BalancedPortn": pmopm8AlmChannel56BalancedPortn,
       "pmopm8AlmChannel56PowerLowPortn": pmopm8AlmChannel56PowerLowPortn,
       "pmopm8AlmChannel56PowerHighPortn": pmopm8AlmChannel56PowerHighPortn,
       "pmopm8AlmChannel56OosPortn": pmopm8AlmChannel56OosPortn,
       "pmopm8Almchannel57PortTable": pmopm8Almchannel57PortTable,
       "pmopm8Almchannel57PortEntry": pmopm8Almchannel57PortEntry,
       "pmopm8Almchannel57PortIndex": pmopm8Almchannel57PortIndex,
       "pmopm8AlmChannel57AbsentPortn": pmopm8AlmChannel57AbsentPortn,
       "pmopm8AlmChannel57MismatchPortn": pmopm8AlmChannel57MismatchPortn,
       "pmopm8AlmChannel57BalancedPortn": pmopm8AlmChannel57BalancedPortn,
       "pmopm8AlmChannel57PowerLowPortn": pmopm8AlmChannel57PowerLowPortn,
       "pmopm8AlmChannel57PowerHighPortn": pmopm8AlmChannel57PowerHighPortn,
       "pmopm8AlmChannel57OosPortn": pmopm8AlmChannel57OosPortn,
       "pmopm8Almchannel58PortTable": pmopm8Almchannel58PortTable,
       "pmopm8Almchannel58PortEntry": pmopm8Almchannel58PortEntry,
       "pmopm8Almchannel58PortIndex": pmopm8Almchannel58PortIndex,
       "pmopm8AlmChannel58AbsentPortn": pmopm8AlmChannel58AbsentPortn,
       "pmopm8AlmChannel58MismatchPortn": pmopm8AlmChannel58MismatchPortn,
       "pmopm8AlmChannel58BalancedPortn": pmopm8AlmChannel58BalancedPortn,
       "pmopm8AlmChannel58PowerLowPortn": pmopm8AlmChannel58PowerLowPortn,
       "pmopm8AlmChannel58PowerHighPortn": pmopm8AlmChannel58PowerHighPortn,
       "pmopm8AlmChannel58OosPortn": pmopm8AlmChannel58OosPortn,
       "pmopm8Almchannel59PortTable": pmopm8Almchannel59PortTable,
       "pmopm8Almchannel59PortEntry": pmopm8Almchannel59PortEntry,
       "pmopm8Almchannel59PortIndex": pmopm8Almchannel59PortIndex,
       "pmopm8AlmChannel59AbsentPortn": pmopm8AlmChannel59AbsentPortn,
       "pmopm8AlmChannel59MismatchPortn": pmopm8AlmChannel59MismatchPortn,
       "pmopm8AlmChannel59BalancedPortn": pmopm8AlmChannel59BalancedPortn,
       "pmopm8AlmChannel59PowerLowPortn": pmopm8AlmChannel59PowerLowPortn,
       "pmopm8AlmChannel59PowerHighPortn": pmopm8AlmChannel59PowerHighPortn,
       "pmopm8AlmChannel59OosPortn": pmopm8AlmChannel59OosPortn,
       "pmopm8Almchannel60PortTable": pmopm8Almchannel60PortTable,
       "pmopm8Almchannel60PortEntry": pmopm8Almchannel60PortEntry,
       "pmopm8Almchannel60PortIndex": pmopm8Almchannel60PortIndex,
       "pmopm8AlmChannel60AbsentPortn": pmopm8AlmChannel60AbsentPortn,
       "pmopm8AlmChannel60MismatchPortn": pmopm8AlmChannel60MismatchPortn,
       "pmopm8AlmChannel60BalancedPortn": pmopm8AlmChannel60BalancedPortn,
       "pmopm8AlmChannel60PowerLowPortn": pmopm8AlmChannel60PowerLowPortn,
       "pmopm8AlmChannel60PowerHighPortn": pmopm8AlmChannel60PowerHighPortn,
       "pmopm8AlmChannel60OosPortn": pmopm8AlmChannel60OosPortn,
       "pmopm8Almchannel61PortTable": pmopm8Almchannel61PortTable,
       "pmopm8Almchannel61PortEntry": pmopm8Almchannel61PortEntry,
       "pmopm8Almchannel61PortIndex": pmopm8Almchannel61PortIndex,
       "pmopm8AlmChannel61AbsentPortn": pmopm8AlmChannel61AbsentPortn,
       "pmopm8AlmChannel61MismatchPortn": pmopm8AlmChannel61MismatchPortn,
       "pmopm8AlmChannel61BalancedPortn": pmopm8AlmChannel61BalancedPortn,
       "pmopm8AlmChannel61PowerLowPortn": pmopm8AlmChannel61PowerLowPortn,
       "pmopm8AlmChannel61PowerHighPortn": pmopm8AlmChannel61PowerHighPortn,
       "pmopm8AlmChannel61OosPortn": pmopm8AlmChannel61OosPortn,
       "pmopm8Almchannel62PortTable": pmopm8Almchannel62PortTable,
       "pmopm8Almchannel62PortEntry": pmopm8Almchannel62PortEntry,
       "pmopm8Almchannel62PortIndex": pmopm8Almchannel62PortIndex,
       "pmopm8AlmChannel62AbsentPortn": pmopm8AlmChannel62AbsentPortn,
       "pmopm8AlmChannel62MismatchPortn": pmopm8AlmChannel62MismatchPortn,
       "pmopm8AlmChannel62BalancedPortn": pmopm8AlmChannel62BalancedPortn,
       "pmopm8AlmChannel62PowerLowPortn": pmopm8AlmChannel62PowerLowPortn,
       "pmopm8AlmChannel62PowerHighPortn": pmopm8AlmChannel62PowerHighPortn,
       "pmopm8AlmChannel62OosPortn": pmopm8AlmChannel62OosPortn,
       "pmopm8Almchannel63PortTable": pmopm8Almchannel63PortTable,
       "pmopm8Almchannel63PortEntry": pmopm8Almchannel63PortEntry,
       "pmopm8Almchannel63PortIndex": pmopm8Almchannel63PortIndex,
       "pmopm8AlmChannel63AbsentPortn": pmopm8AlmChannel63AbsentPortn,
       "pmopm8AlmChannel63MismatchPortn": pmopm8AlmChannel63MismatchPortn,
       "pmopm8AlmChannel63BalancedPortn": pmopm8AlmChannel63BalancedPortn,
       "pmopm8AlmChannel63PowerLowPortn": pmopm8AlmChannel63PowerLowPortn,
       "pmopm8AlmChannel63PowerHighPortn": pmopm8AlmChannel63PowerHighPortn,
       "pmopm8AlmChannel63OosPortn": pmopm8AlmChannel63OosPortn,
       "pmopm8Almchannel64PortTable": pmopm8Almchannel64PortTable,
       "pmopm8Almchannel64PortEntry": pmopm8Almchannel64PortEntry,
       "pmopm8Almchannel64PortIndex": pmopm8Almchannel64PortIndex,
       "pmopm8AlmChannel64AbsentPortn": pmopm8AlmChannel64AbsentPortn,
       "pmopm8AlmChannel64MismatchPortn": pmopm8AlmChannel64MismatchPortn,
       "pmopm8AlmChannel64BalancedPortn": pmopm8AlmChannel64BalancedPortn,
       "pmopm8AlmChannel64PowerLowPortn": pmopm8AlmChannel64PowerLowPortn,
       "pmopm8AlmChannel64PowerHighPortn": pmopm8AlmChannel64PowerHighPortn,
       "pmopm8AlmChannel64OosPortn": pmopm8AlmChannel64OosPortn,
       "pmopm8Almchannel65PortTable": pmopm8Almchannel65PortTable,
       "pmopm8Almchannel65PortEntry": pmopm8Almchannel65PortEntry,
       "pmopm8Almchannel65PortIndex": pmopm8Almchannel65PortIndex,
       "pmopm8AlmChannel65AbsentPortn": pmopm8AlmChannel65AbsentPortn,
       "pmopm8AlmChannel65MismatchPortn": pmopm8AlmChannel65MismatchPortn,
       "pmopm8AlmChannel65BalancedPortn": pmopm8AlmChannel65BalancedPortn,
       "pmopm8AlmChannel65PowerLowPortn": pmopm8AlmChannel65PowerLowPortn,
       "pmopm8AlmChannel65PowerHighPortn": pmopm8AlmChannel65PowerHighPortn,
       "pmopm8AlmChannel65OosPortn": pmopm8AlmChannel65OosPortn,
       "pmopm8Almchannel66PortTable": pmopm8Almchannel66PortTable,
       "pmopm8Almchannel66PortEntry": pmopm8Almchannel66PortEntry,
       "pmopm8Almchannel66PortIndex": pmopm8Almchannel66PortIndex,
       "pmopm8AlmChannel66AbsentPortn": pmopm8AlmChannel66AbsentPortn,
       "pmopm8AlmChannel66MismatchPortn": pmopm8AlmChannel66MismatchPortn,
       "pmopm8AlmChannel66BalancedPortn": pmopm8AlmChannel66BalancedPortn,
       "pmopm8AlmChannel66PowerLowPortn": pmopm8AlmChannel66PowerLowPortn,
       "pmopm8AlmChannel66PowerHighPortn": pmopm8AlmChannel66PowerHighPortn,
       "pmopm8AlmChannel66OosPortn": pmopm8AlmChannel66OosPortn,
       "pmopm8Almchannel67PortTable": pmopm8Almchannel67PortTable,
       "pmopm8Almchannel67PortEntry": pmopm8Almchannel67PortEntry,
       "pmopm8Almchannel67PortIndex": pmopm8Almchannel67PortIndex,
       "pmopm8AlmChannel67AbsentPortn": pmopm8AlmChannel67AbsentPortn,
       "pmopm8AlmChannel67MismatchPortn": pmopm8AlmChannel67MismatchPortn,
       "pmopm8AlmChannel67BalancedPortn": pmopm8AlmChannel67BalancedPortn,
       "pmopm8AlmChannel67PowerLowPortn": pmopm8AlmChannel67PowerLowPortn,
       "pmopm8AlmChannel67PowerHighPortn": pmopm8AlmChannel67PowerHighPortn,
       "pmopm8AlmChannel67OosPortn": pmopm8AlmChannel67OosPortn,
       "pmopm8Almchannel68PortTable": pmopm8Almchannel68PortTable,
       "pmopm8Almchannel68PortEntry": pmopm8Almchannel68PortEntry,
       "pmopm8Almchannel68PortIndex": pmopm8Almchannel68PortIndex,
       "pmopm8AlmChannel68AbsentPortn": pmopm8AlmChannel68AbsentPortn,
       "pmopm8AlmChannel68MismatchPortn": pmopm8AlmChannel68MismatchPortn,
       "pmopm8AlmChannel68BalancedPortn": pmopm8AlmChannel68BalancedPortn,
       "pmopm8AlmChannel68PowerLowPortn": pmopm8AlmChannel68PowerLowPortn,
       "pmopm8AlmChannel68PowerHighPortn": pmopm8AlmChannel68PowerHighPortn,
       "pmopm8AlmChannel68OosPortn": pmopm8AlmChannel68OosPortn,
       "pmopm8Almchannel69PortTable": pmopm8Almchannel69PortTable,
       "pmopm8Almchannel69PortEntry": pmopm8Almchannel69PortEntry,
       "pmopm8Almchannel69PortIndex": pmopm8Almchannel69PortIndex,
       "pmopm8AlmChannel69AbsentPortn": pmopm8AlmChannel69AbsentPortn,
       "pmopm8AlmChannel69MismatchPortn": pmopm8AlmChannel69MismatchPortn,
       "pmopm8AlmChannel69BalancedPortn": pmopm8AlmChannel69BalancedPortn,
       "pmopm8AlmChannel69PowerLowPortn": pmopm8AlmChannel69PowerLowPortn,
       "pmopm8AlmChannel69PowerHighPortn": pmopm8AlmChannel69PowerHighPortn,
       "pmopm8AlmChannel69OosPortn": pmopm8AlmChannel69OosPortn,
       "pmopm8Almchannel70PortTable": pmopm8Almchannel70PortTable,
       "pmopm8Almchannel70PortEntry": pmopm8Almchannel70PortEntry,
       "pmopm8Almchannel70PortIndex": pmopm8Almchannel70PortIndex,
       "pmopm8AlmChannel70AbsentPortn": pmopm8AlmChannel70AbsentPortn,
       "pmopm8AlmChannel70MismatchPortn": pmopm8AlmChannel70MismatchPortn,
       "pmopm8AlmChannel70BalancedPortn": pmopm8AlmChannel70BalancedPortn,
       "pmopm8AlmChannel70PowerLowPortn": pmopm8AlmChannel70PowerLowPortn,
       "pmopm8AlmChannel70PowerHighPortn": pmopm8AlmChannel70PowerHighPortn,
       "pmopm8AlmChannel70OosPortn": pmopm8AlmChannel70OosPortn,
       "pmopm8Almchannel71PortTable": pmopm8Almchannel71PortTable,
       "pmopm8Almchannel71PortEntry": pmopm8Almchannel71PortEntry,
       "pmopm8Almchannel71PortIndex": pmopm8Almchannel71PortIndex,
       "pmopm8AlmChannel71AbsentPortn": pmopm8AlmChannel71AbsentPortn,
       "pmopm8AlmChannel71MismatchPortn": pmopm8AlmChannel71MismatchPortn,
       "pmopm8AlmChannel71BalancedPortn": pmopm8AlmChannel71BalancedPortn,
       "pmopm8AlmChannel71PowerLowPortn": pmopm8AlmChannel71PowerLowPortn,
       "pmopm8AlmChannel71PowerHighPortn": pmopm8AlmChannel71PowerHighPortn,
       "pmopm8AlmChannel71OosPortn": pmopm8AlmChannel71OosPortn,
       "pmopm8Almchannel72PortTable": pmopm8Almchannel72PortTable,
       "pmopm8Almchannel72PortEntry": pmopm8Almchannel72PortEntry,
       "pmopm8Almchannel72PortIndex": pmopm8Almchannel72PortIndex,
       "pmopm8AlmChannel72AbsentPortn": pmopm8AlmChannel72AbsentPortn,
       "pmopm8AlmChannel72MismatchPortn": pmopm8AlmChannel72MismatchPortn,
       "pmopm8AlmChannel72BalancedPortn": pmopm8AlmChannel72BalancedPortn,
       "pmopm8AlmChannel72PowerLowPortn": pmopm8AlmChannel72PowerLowPortn,
       "pmopm8AlmChannel72PowerHighPortn": pmopm8AlmChannel72PowerHighPortn,
       "pmopm8AlmChannel72OosPortn": pmopm8AlmChannel72OosPortn,
       "pmopm8Almchannel73PortTable": pmopm8Almchannel73PortTable,
       "pmopm8Almchannel73PortEntry": pmopm8Almchannel73PortEntry,
       "pmopm8Almchannel73PortIndex": pmopm8Almchannel73PortIndex,
       "pmopm8AlmChannel73AbsentPortn": pmopm8AlmChannel73AbsentPortn,
       "pmopm8AlmChannel73MismatchPortn": pmopm8AlmChannel73MismatchPortn,
       "pmopm8AlmChannel73BalancedPortn": pmopm8AlmChannel73BalancedPortn,
       "pmopm8AlmChannel73PowerLowPortn": pmopm8AlmChannel73PowerLowPortn,
       "pmopm8AlmChannel73PowerHighPortn": pmopm8AlmChannel73PowerHighPortn,
       "pmopm8AlmChannel73OosPortn": pmopm8AlmChannel73OosPortn,
       "pmopm8Almchannel74PortTable": pmopm8Almchannel74PortTable,
       "pmopm8Almchannel74PortEntry": pmopm8Almchannel74PortEntry,
       "pmopm8Almchannel74PortIndex": pmopm8Almchannel74PortIndex,
       "pmopm8AlmChannel74AbsentPortn": pmopm8AlmChannel74AbsentPortn,
       "pmopm8AlmChannel74MismatchPortn": pmopm8AlmChannel74MismatchPortn,
       "pmopm8AlmChannel74BalancedPortn": pmopm8AlmChannel74BalancedPortn,
       "pmopm8AlmChannel74PowerLowPortn": pmopm8AlmChannel74PowerLowPortn,
       "pmopm8AlmChannel74PowerHighPortn": pmopm8AlmChannel74PowerHighPortn,
       "pmopm8AlmChannel74OosPortn": pmopm8AlmChannel74OosPortn,
       "pmopm8Almchannel75PortTable": pmopm8Almchannel75PortTable,
       "pmopm8Almchannel75PortEntry": pmopm8Almchannel75PortEntry,
       "pmopm8Almchannel75PortIndex": pmopm8Almchannel75PortIndex,
       "pmopm8AlmChannel75AbsentPortn": pmopm8AlmChannel75AbsentPortn,
       "pmopm8AlmChannel75MismatchPortn": pmopm8AlmChannel75MismatchPortn,
       "pmopm8AlmChannel75BalancedPortn": pmopm8AlmChannel75BalancedPortn,
       "pmopm8AlmChannel75PowerLowPortn": pmopm8AlmChannel75PowerLowPortn,
       "pmopm8AlmChannel75PowerHighPortn": pmopm8AlmChannel75PowerHighPortn,
       "pmopm8AlmChannel75OosPortn": pmopm8AlmChannel75OosPortn,
       "pmopm8Almchannel76PortTable": pmopm8Almchannel76PortTable,
       "pmopm8Almchannel76PortEntry": pmopm8Almchannel76PortEntry,
       "pmopm8Almchannel76PortIndex": pmopm8Almchannel76PortIndex,
       "pmopm8AlmChannel76AbsentPortn": pmopm8AlmChannel76AbsentPortn,
       "pmopm8AlmChannel76MismatchPortn": pmopm8AlmChannel76MismatchPortn,
       "pmopm8AlmChannel76BalancedPortn": pmopm8AlmChannel76BalancedPortn,
       "pmopm8AlmChannel76PowerLowPortn": pmopm8AlmChannel76PowerLowPortn,
       "pmopm8AlmChannel76PowerHighPortn": pmopm8AlmChannel76PowerHighPortn,
       "pmopm8AlmChannel76OosPortn": pmopm8AlmChannel76OosPortn,
       "pmopm8Almchannel77PortTable": pmopm8Almchannel77PortTable,
       "pmopm8Almchannel77PortEntry": pmopm8Almchannel77PortEntry,
       "pmopm8Almchannel77PortIndex": pmopm8Almchannel77PortIndex,
       "pmopm8AlmChannel77AbsentPortn": pmopm8AlmChannel77AbsentPortn,
       "pmopm8AlmChannel77MismatchPortn": pmopm8AlmChannel77MismatchPortn,
       "pmopm8AlmChannel77BalancedPortn": pmopm8AlmChannel77BalancedPortn,
       "pmopm8AlmChannel77PowerLowPortn": pmopm8AlmChannel77PowerLowPortn,
       "pmopm8AlmChannel77PowerHighPortn": pmopm8AlmChannel77PowerHighPortn,
       "pmopm8AlmChannel77OosPortn": pmopm8AlmChannel77OosPortn,
       "pmopm8Almchannel78PortTable": pmopm8Almchannel78PortTable,
       "pmopm8Almchannel78PortEntry": pmopm8Almchannel78PortEntry,
       "pmopm8Almchannel78PortIndex": pmopm8Almchannel78PortIndex,
       "pmopm8AlmChannel78AbsentPortn": pmopm8AlmChannel78AbsentPortn,
       "pmopm8AlmChannel78MismatchPortn": pmopm8AlmChannel78MismatchPortn,
       "pmopm8AlmChannel78BalancedPortn": pmopm8AlmChannel78BalancedPortn,
       "pmopm8AlmChannel78PowerLowPortn": pmopm8AlmChannel78PowerLowPortn,
       "pmopm8AlmChannel78PowerHighPortn": pmopm8AlmChannel78PowerHighPortn,
       "pmopm8AlmChannel78OosPortn": pmopm8AlmChannel78OosPortn,
       "pmopm8Almchannel79PortTable": pmopm8Almchannel79PortTable,
       "pmopm8Almchannel79PortEntry": pmopm8Almchannel79PortEntry,
       "pmopm8Almchannel79PortIndex": pmopm8Almchannel79PortIndex,
       "pmopm8AlmChannel79AbsentPortn": pmopm8AlmChannel79AbsentPortn,
       "pmopm8AlmChannel79MismatchPortn": pmopm8AlmChannel79MismatchPortn,
       "pmopm8AlmChannel79BalancedPortn": pmopm8AlmChannel79BalancedPortn,
       "pmopm8AlmChannel79PowerLowPortn": pmopm8AlmChannel79PowerLowPortn,
       "pmopm8AlmChannel79PowerHighPortn": pmopm8AlmChannel79PowerHighPortn,
       "pmopm8AlmChannel79OosPortn": pmopm8AlmChannel79OosPortn,
       "pmopm8Almchannel80PortTable": pmopm8Almchannel80PortTable,
       "pmopm8Almchannel80PortEntry": pmopm8Almchannel80PortEntry,
       "pmopm8Almchannel80PortIndex": pmopm8Almchannel80PortIndex,
       "pmopm8AlmChannel80AbsentPortn": pmopm8AlmChannel80AbsentPortn,
       "pmopm8AlmChannel80MismatchPortn": pmopm8AlmChannel80MismatchPortn,
       "pmopm8AlmChannel80BalancedPortn": pmopm8AlmChannel80BalancedPortn,
       "pmopm8AlmChannel80PowerLowPortn": pmopm8AlmChannel80PowerLowPortn,
       "pmopm8AlmChannel80PowerHighPortn": pmopm8AlmChannel80PowerHighPortn,
       "pmopm8AlmChannel80OosPortn": pmopm8AlmChannel80OosPortn,
       "pmopm8Almchannel81PortTable": pmopm8Almchannel81PortTable,
       "pmopm8Almchannel81PortEntry": pmopm8Almchannel81PortEntry,
       "pmopm8Almchannel81PortIndex": pmopm8Almchannel81PortIndex,
       "pmopm8AlmChannel81AbsentPortn": pmopm8AlmChannel81AbsentPortn,
       "pmopm8AlmChannel81MismatchPortn": pmopm8AlmChannel81MismatchPortn,
       "pmopm8AlmChannel81BalancedPortn": pmopm8AlmChannel81BalancedPortn,
       "pmopm8AlmChannel81PowerLowPortn": pmopm8AlmChannel81PowerLowPortn,
       "pmopm8AlmChannel81PowerHighPortn": pmopm8AlmChannel81PowerHighPortn,
       "pmopm8AlmChannel81OosPortn": pmopm8AlmChannel81OosPortn,
       "pmopm8Almchannel82PortTable": pmopm8Almchannel82PortTable,
       "pmopm8Almchannel82PortEntry": pmopm8Almchannel82PortEntry,
       "pmopm8Almchannel82PortIndex": pmopm8Almchannel82PortIndex,
       "pmopm8AlmChannel82AbsentPortn": pmopm8AlmChannel82AbsentPortn,
       "pmopm8AlmChannel82MismatchPortn": pmopm8AlmChannel82MismatchPortn,
       "pmopm8AlmChannel82BalancedPortn": pmopm8AlmChannel82BalancedPortn,
       "pmopm8AlmChannel82PowerLowPortn": pmopm8AlmChannel82PowerLowPortn,
       "pmopm8AlmChannel82PowerHighPortn": pmopm8AlmChannel82PowerHighPortn,
       "pmopm8AlmChannel82OosPortn": pmopm8AlmChannel82OosPortn,
       "pmopm8Almchannel83PortTable": pmopm8Almchannel83PortTable,
       "pmopm8Almchannel83PortEntry": pmopm8Almchannel83PortEntry,
       "pmopm8Almchannel83PortIndex": pmopm8Almchannel83PortIndex,
       "pmopm8AlmChannel83AbsentPortn": pmopm8AlmChannel83AbsentPortn,
       "pmopm8AlmChannel83MismatchPortn": pmopm8AlmChannel83MismatchPortn,
       "pmopm8AlmChannel83BalancedPortn": pmopm8AlmChannel83BalancedPortn,
       "pmopm8AlmChannel83PowerLowPortn": pmopm8AlmChannel83PowerLowPortn,
       "pmopm8AlmChannel83PowerHighPortn": pmopm8AlmChannel83PowerHighPortn,
       "pmopm8AlmChannel83OosPortn": pmopm8AlmChannel83OosPortn,
       "pmopm8Almchannel84PortTable": pmopm8Almchannel84PortTable,
       "pmopm8Almchannel84PortEntry": pmopm8Almchannel84PortEntry,
       "pmopm8Almchannel84PortIndex": pmopm8Almchannel84PortIndex,
       "pmopm8AlmChannel84AbsentPortn": pmopm8AlmChannel84AbsentPortn,
       "pmopm8AlmChannel84MismatchPortn": pmopm8AlmChannel84MismatchPortn,
       "pmopm8AlmChannel84BalancedPortn": pmopm8AlmChannel84BalancedPortn,
       "pmopm8AlmChannel84PowerLowPortn": pmopm8AlmChannel84PowerLowPortn,
       "pmopm8AlmChannel84PowerHighPortn": pmopm8AlmChannel84PowerHighPortn,
       "pmopm8AlmChannel84OosPortn": pmopm8AlmChannel84OosPortn,
       "pmopm8Almchannel85PortTable": pmopm8Almchannel85PortTable,
       "pmopm8Almchannel85PortEntry": pmopm8Almchannel85PortEntry,
       "pmopm8Almchannel85PortIndex": pmopm8Almchannel85PortIndex,
       "pmopm8AlmChannel85AbsentPortn": pmopm8AlmChannel85AbsentPortn,
       "pmopm8AlmChannel85MismatchPortn": pmopm8AlmChannel85MismatchPortn,
       "pmopm8AlmChannel85BalancedPortn": pmopm8AlmChannel85BalancedPortn,
       "pmopm8AlmChannel85PowerLowPortn": pmopm8AlmChannel85PowerLowPortn,
       "pmopm8AlmChannel85PowerHighPortn": pmopm8AlmChannel85PowerHighPortn,
       "pmopm8AlmChannel85OosPortn": pmopm8AlmChannel85OosPortn,
       "pmopm8Almchannel86PortTable": pmopm8Almchannel86PortTable,
       "pmopm8Almchannel86PortEntry": pmopm8Almchannel86PortEntry,
       "pmopm8Almchannel86PortIndex": pmopm8Almchannel86PortIndex,
       "pmopm8AlmChannel86AbsentPortn": pmopm8AlmChannel86AbsentPortn,
       "pmopm8AlmChannel86MismatchPortn": pmopm8AlmChannel86MismatchPortn,
       "pmopm8AlmChannel86BalancedPortn": pmopm8AlmChannel86BalancedPortn,
       "pmopm8AlmChannel86PowerLowPortn": pmopm8AlmChannel86PowerLowPortn,
       "pmopm8AlmChannel86PowerHighPortn": pmopm8AlmChannel86PowerHighPortn,
       "pmopm8AlmChannel86OosPortn": pmopm8AlmChannel86OosPortn,
       "pmopm8Almchannel87PortTable": pmopm8Almchannel87PortTable,
       "pmopm8Almchannel87PortEntry": pmopm8Almchannel87PortEntry,
       "pmopm8Almchannel87PortIndex": pmopm8Almchannel87PortIndex,
       "pmopm8AlmChannel87AbsentPortn": pmopm8AlmChannel87AbsentPortn,
       "pmopm8AlmChannel87MismatchPortn": pmopm8AlmChannel87MismatchPortn,
       "pmopm8AlmChannel87BalancedPortn": pmopm8AlmChannel87BalancedPortn,
       "pmopm8AlmChannel87PowerLowPortn": pmopm8AlmChannel87PowerLowPortn,
       "pmopm8AlmChannel87PowerHighPortn": pmopm8AlmChannel87PowerHighPortn,
       "pmopm8AlmChannel87OosPortn": pmopm8AlmChannel87OosPortn,
       "pmopm8Almchannel88PortTable": pmopm8Almchannel88PortTable,
       "pmopm8Almchannel88PortEntry": pmopm8Almchannel88PortEntry,
       "pmopm8Almchannel88PortIndex": pmopm8Almchannel88PortIndex,
       "pmopm8AlmChannel88AbsentPortn": pmopm8AlmChannel88AbsentPortn,
       "pmopm8AlmChannel88MismatchPortn": pmopm8AlmChannel88MismatchPortn,
       "pmopm8AlmChannel88BalancedPortn": pmopm8AlmChannel88BalancedPortn,
       "pmopm8AlmChannel88PowerLowPortn": pmopm8AlmChannel88PowerLowPortn,
       "pmopm8AlmChannel88PowerHighPortn": pmopm8AlmChannel88PowerHighPortn,
       "pmopm8AlmChannel88OosPortn": pmopm8AlmChannel88OosPortn,
       "pmopm8Almchannel89PortTable": pmopm8Almchannel89PortTable,
       "pmopm8Almchannel89PortEntry": pmopm8Almchannel89PortEntry,
       "pmopm8Almchannel89PortIndex": pmopm8Almchannel89PortIndex,
       "pmopm8AlmChannel89AbsentPortn": pmopm8AlmChannel89AbsentPortn,
       "pmopm8AlmChannel89MismatchPortn": pmopm8AlmChannel89MismatchPortn,
       "pmopm8AlmChannel89BalancedPortn": pmopm8AlmChannel89BalancedPortn,
       "pmopm8AlmChannel89PowerLowPortn": pmopm8AlmChannel89PowerLowPortn,
       "pmopm8AlmChannel89PowerHighPortn": pmopm8AlmChannel89PowerHighPortn,
       "pmopm8AlmChannel89OosPortn": pmopm8AlmChannel89OosPortn,
       "pmopm8Almchannel90PortTable": pmopm8Almchannel90PortTable,
       "pmopm8Almchannel90PortEntry": pmopm8Almchannel90PortEntry,
       "pmopm8Almchannel90PortIndex": pmopm8Almchannel90PortIndex,
       "pmopm8AlmChannel90AbsentPortn": pmopm8AlmChannel90AbsentPortn,
       "pmopm8AlmChannel90MismatchPortn": pmopm8AlmChannel90MismatchPortn,
       "pmopm8AlmChannel90BalancedPortn": pmopm8AlmChannel90BalancedPortn,
       "pmopm8AlmChannel90PowerLowPortn": pmopm8AlmChannel90PowerLowPortn,
       "pmopm8AlmChannel90PowerHighPortn": pmopm8AlmChannel90PowerHighPortn,
       "pmopm8AlmChannel90OosPortn": pmopm8AlmChannel90OosPortn,
       "pmopm8Almchannel91PortTable": pmopm8Almchannel91PortTable,
       "pmopm8Almchannel91PortEntry": pmopm8Almchannel91PortEntry,
       "pmopm8Almchannel91PortIndex": pmopm8Almchannel91PortIndex,
       "pmopm8AlmChannel91AbsentPortn": pmopm8AlmChannel91AbsentPortn,
       "pmopm8AlmChannel91MismatchPortn": pmopm8AlmChannel91MismatchPortn,
       "pmopm8AlmChannel91BalancedPortn": pmopm8AlmChannel91BalancedPortn,
       "pmopm8AlmChannel91PowerLowPortn": pmopm8AlmChannel91PowerLowPortn,
       "pmopm8AlmChannel91PowerHighPortn": pmopm8AlmChannel91PowerHighPortn,
       "pmopm8AlmChannel91OosPortn": pmopm8AlmChannel91OosPortn,
       "pmopm8Almchannel92PortTable": pmopm8Almchannel92PortTable,
       "pmopm8Almchannel92PortEntry": pmopm8Almchannel92PortEntry,
       "pmopm8Almchannel92PortIndex": pmopm8Almchannel92PortIndex,
       "pmopm8AlmChannel92AbsentPortn": pmopm8AlmChannel92AbsentPortn,
       "pmopm8AlmChannel92MismatchPortn": pmopm8AlmChannel92MismatchPortn,
       "pmopm8AlmChannel92BalancedPortn": pmopm8AlmChannel92BalancedPortn,
       "pmopm8AlmChannel92PowerLowPortn": pmopm8AlmChannel92PowerLowPortn,
       "pmopm8AlmChannel92PowerHighPortn": pmopm8AlmChannel92PowerHighPortn,
       "pmopm8AlmChannel92OosPortn": pmopm8AlmChannel92OosPortn,
       "pmopm8Almchannel93PortTable": pmopm8Almchannel93PortTable,
       "pmopm8Almchannel93PortEntry": pmopm8Almchannel93PortEntry,
       "pmopm8Almchannel93PortIndex": pmopm8Almchannel93PortIndex,
       "pmopm8AlmChannel93AbsentPortn": pmopm8AlmChannel93AbsentPortn,
       "pmopm8AlmChannel93MismatchPortn": pmopm8AlmChannel93MismatchPortn,
       "pmopm8AlmChannel93BalancedPortn": pmopm8AlmChannel93BalancedPortn,
       "pmopm8AlmChannel93PowerLowPortn": pmopm8AlmChannel93PowerLowPortn,
       "pmopm8AlmChannel93PowerHighPortn": pmopm8AlmChannel93PowerHighPortn,
       "pmopm8AlmChannel93OosPortn": pmopm8AlmChannel93OosPortn,
       "pmopm8Almchannel94PortTable": pmopm8Almchannel94PortTable,
       "pmopm8Almchannel94PortEntry": pmopm8Almchannel94PortEntry,
       "pmopm8Almchannel94PortIndex": pmopm8Almchannel94PortIndex,
       "pmopm8AlmChannel94AbsentPortn": pmopm8AlmChannel94AbsentPortn,
       "pmopm8AlmChannel94MismatchPortn": pmopm8AlmChannel94MismatchPortn,
       "pmopm8AlmChannel94BalancedPortn": pmopm8AlmChannel94BalancedPortn,
       "pmopm8AlmChannel94PowerLowPortn": pmopm8AlmChannel94PowerLowPortn,
       "pmopm8AlmChannel94PowerHighPortn": pmopm8AlmChannel94PowerHighPortn,
       "pmopm8AlmChannel94OosPortn": pmopm8AlmChannel94OosPortn,
       "pmopm8Almchannel95PortTable": pmopm8Almchannel95PortTable,
       "pmopm8Almchannel95PortEntry": pmopm8Almchannel95PortEntry,
       "pmopm8Almchannel95PortIndex": pmopm8Almchannel95PortIndex,
       "pmopm8AlmChannel95AbsentPortn": pmopm8AlmChannel95AbsentPortn,
       "pmopm8AlmChannel95MismatchPortn": pmopm8AlmChannel95MismatchPortn,
       "pmopm8AlmChannel95BalancedPortn": pmopm8AlmChannel95BalancedPortn,
       "pmopm8AlmChannel95PowerLowPortn": pmopm8AlmChannel95PowerLowPortn,
       "pmopm8AlmChannel95PowerHighPortn": pmopm8AlmChannel95PowerHighPortn,
       "pmopm8AlmChannel95OosPortn": pmopm8AlmChannel95OosPortn,
       "pmopm8Almchannel96PortTable": pmopm8Almchannel96PortTable,
       "pmopm8Almchannel96PortEntry": pmopm8Almchannel96PortEntry,
       "pmopm8Almchannel96PortIndex": pmopm8Almchannel96PortIndex,
       "pmopm8AlmChannel96AbsentPortn": pmopm8AlmChannel96AbsentPortn,
       "pmopm8AlmChannel96MismatchPortn": pmopm8AlmChannel96MismatchPortn,
       "pmopm8AlmChannel96BalancedPortn": pmopm8AlmChannel96BalancedPortn,
       "pmopm8AlmChannel96PowerLowPortn": pmopm8AlmChannel96PowerLowPortn,
       "pmopm8AlmChannel96PowerHighPortn": pmopm8AlmChannel96PowerHighPortn,
       "pmopm8AlmChannel96OosPortn": pmopm8AlmChannel96OosPortn,
       "pmopm8AlmLine": pmopm8AlmLine,
       "pmopm8AlmLineNurg": pmopm8AlmLineNurg,
       "pmopm8AlmLineUrg": pmopm8AlmLineUrg,
       "pmopm8AlmLineCrit": pmopm8AlmLineCrit,
       "pmopm8measures": pmopm8measures,
       "pmopm8MesrOther": pmopm8MesrOther,
       "pmopm8MesropmTemp": pmopm8MesropmTemp,
       "pmopm8MesrClient": pmopm8MesrClient,
       "pmopm8Mesrchannel1Table": pmopm8Mesrchannel1Table,
       "pmopm8Mesrchannel1Entry": pmopm8Mesrchannel1Entry,
       "pmopm8Mesrchannel1Index": pmopm8Mesrchannel1Index,
       "pmopm8Mesrchannel1Portn": pmopm8Mesrchannel1Portn,
       "pmopm8Mesrchannel2Table": pmopm8Mesrchannel2Table,
       "pmopm8Mesrchannel2Entry": pmopm8Mesrchannel2Entry,
       "pmopm8Mesrchannel2Index": pmopm8Mesrchannel2Index,
       "pmopm8Mesrchannel2Portn": pmopm8Mesrchannel2Portn,
       "pmopm8Mesrchannel3Table": pmopm8Mesrchannel3Table,
       "pmopm8Mesrchannel3Entry": pmopm8Mesrchannel3Entry,
       "pmopm8Mesrchannel3Index": pmopm8Mesrchannel3Index,
       "pmopm8Mesrchannel3Portn": pmopm8Mesrchannel3Portn,
       "pmopm8Mesrchannel4Table": pmopm8Mesrchannel4Table,
       "pmopm8Mesrchannel4Entry": pmopm8Mesrchannel4Entry,
       "pmopm8Mesrchannel4Index": pmopm8Mesrchannel4Index,
       "pmopm8Mesrchannel4Portn": pmopm8Mesrchannel4Portn,
       "pmopm8Mesrchannel5Table": pmopm8Mesrchannel5Table,
       "pmopm8Mesrchannel5Entry": pmopm8Mesrchannel5Entry,
       "pmopm8Mesrchannel5Index": pmopm8Mesrchannel5Index,
       "pmopm8Mesrchannel5Portn": pmopm8Mesrchannel5Portn,
       "pmopm8Mesrchannel6Table": pmopm8Mesrchannel6Table,
       "pmopm8Mesrchannel6Entry": pmopm8Mesrchannel6Entry,
       "pmopm8Mesrchannel6Index": pmopm8Mesrchannel6Index,
       "pmopm8Mesrchannel6Portn": pmopm8Mesrchannel6Portn,
       "pmopm8Mesrchannel7Table": pmopm8Mesrchannel7Table,
       "pmopm8Mesrchannel7Entry": pmopm8Mesrchannel7Entry,
       "pmopm8Mesrchannel7Index": pmopm8Mesrchannel7Index,
       "pmopm8Mesrchannel7Portn": pmopm8Mesrchannel7Portn,
       "pmopm8Mesrchannel8Table": pmopm8Mesrchannel8Table,
       "pmopm8Mesrchannel8Entry": pmopm8Mesrchannel8Entry,
       "pmopm8Mesrchannel8Index": pmopm8Mesrchannel8Index,
       "pmopm8Mesrchannel8Portn": pmopm8Mesrchannel8Portn,
       "pmopm8Mesrchannel9Table": pmopm8Mesrchannel9Table,
       "pmopm8Mesrchannel9Entry": pmopm8Mesrchannel9Entry,
       "pmopm8Mesrchannel9Index": pmopm8Mesrchannel9Index,
       "pmopm8Mesrchannel9Portn": pmopm8Mesrchannel9Portn,
       "pmopm8Mesrchannel10Table": pmopm8Mesrchannel10Table,
       "pmopm8Mesrchannel10Entry": pmopm8Mesrchannel10Entry,
       "pmopm8Mesrchannel10Index": pmopm8Mesrchannel10Index,
       "pmopm8Mesrchannel10Portn": pmopm8Mesrchannel10Portn,
       "pmopm8Mesrchannel11Table": pmopm8Mesrchannel11Table,
       "pmopm8Mesrchannel11Entry": pmopm8Mesrchannel11Entry,
       "pmopm8Mesrchannel11Index": pmopm8Mesrchannel11Index,
       "pmopm8Mesrchannel11Portn": pmopm8Mesrchannel11Portn,
       "pmopm8Mesrchannel12Table": pmopm8Mesrchannel12Table,
       "pmopm8Mesrchannel12Entry": pmopm8Mesrchannel12Entry,
       "pmopm8Mesrchannel12Index": pmopm8Mesrchannel12Index,
       "pmopm8Mesrchannel12Portn": pmopm8Mesrchannel12Portn,
       "pmopm8Mesrchannel13Table": pmopm8Mesrchannel13Table,
       "pmopm8Mesrchannel13Entry": pmopm8Mesrchannel13Entry,
       "pmopm8Mesrchannel13Index": pmopm8Mesrchannel13Index,
       "pmopm8Mesrchannel13Portn": pmopm8Mesrchannel13Portn,
       "pmopm8Mesrchannel14Table": pmopm8Mesrchannel14Table,
       "pmopm8Mesrchannel14Entry": pmopm8Mesrchannel14Entry,
       "pmopm8Mesrchannel14Index": pmopm8Mesrchannel14Index,
       "pmopm8Mesrchannel14Portn": pmopm8Mesrchannel14Portn,
       "pmopm8Mesrchannel15Table": pmopm8Mesrchannel15Table,
       "pmopm8Mesrchannel15Entry": pmopm8Mesrchannel15Entry,
       "pmopm8Mesrchannel15Index": pmopm8Mesrchannel15Index,
       "pmopm8Mesrchannel15Portn": pmopm8Mesrchannel15Portn,
       "pmopm8Mesrchannel16Table": pmopm8Mesrchannel16Table,
       "pmopm8Mesrchannel16Entry": pmopm8Mesrchannel16Entry,
       "pmopm8Mesrchannel16Index": pmopm8Mesrchannel16Index,
       "pmopm8Mesrchannel16Portn": pmopm8Mesrchannel16Portn,
       "pmopm8Mesrchannel17Table": pmopm8Mesrchannel17Table,
       "pmopm8Mesrchannel17Entry": pmopm8Mesrchannel17Entry,
       "pmopm8Mesrchannel17Index": pmopm8Mesrchannel17Index,
       "pmopm8Mesrchannel17Portn": pmopm8Mesrchannel17Portn,
       "pmopm8Mesrchannel18Table": pmopm8Mesrchannel18Table,
       "pmopm8Mesrchannel18Entry": pmopm8Mesrchannel18Entry,
       "pmopm8Mesrchannel18Index": pmopm8Mesrchannel18Index,
       "pmopm8Mesrchannel18Portn": pmopm8Mesrchannel18Portn,
       "pmopm8Mesrchannel19Table": pmopm8Mesrchannel19Table,
       "pmopm8Mesrchannel19Entry": pmopm8Mesrchannel19Entry,
       "pmopm8Mesrchannel19Index": pmopm8Mesrchannel19Index,
       "pmopm8Mesrchannel19Portn": pmopm8Mesrchannel19Portn,
       "pmopm8Mesrchannel20Table": pmopm8Mesrchannel20Table,
       "pmopm8Mesrchannel20Entry": pmopm8Mesrchannel20Entry,
       "pmopm8Mesrchannel20Index": pmopm8Mesrchannel20Index,
       "pmopm8Mesrchannel20Portn": pmopm8Mesrchannel20Portn,
       "pmopm8Mesrchannel21Table": pmopm8Mesrchannel21Table,
       "pmopm8Mesrchannel21Entry": pmopm8Mesrchannel21Entry,
       "pmopm8Mesrchannel21Index": pmopm8Mesrchannel21Index,
       "pmopm8Mesrchannel21Portn": pmopm8Mesrchannel21Portn,
       "pmopm8Mesrchannel22Table": pmopm8Mesrchannel22Table,
       "pmopm8Mesrchannel22Entry": pmopm8Mesrchannel22Entry,
       "pmopm8Mesrchannel22Index": pmopm8Mesrchannel22Index,
       "pmopm8Mesrchannel22Portn": pmopm8Mesrchannel22Portn,
       "pmopm8Mesrchannel23Table": pmopm8Mesrchannel23Table,
       "pmopm8Mesrchannel23Entry": pmopm8Mesrchannel23Entry,
       "pmopm8Mesrchannel23Index": pmopm8Mesrchannel23Index,
       "pmopm8Mesrchannel23Portn": pmopm8Mesrchannel23Portn,
       "pmopm8Mesrchannel24Table": pmopm8Mesrchannel24Table,
       "pmopm8Mesrchannel24Entry": pmopm8Mesrchannel24Entry,
       "pmopm8Mesrchannel24Index": pmopm8Mesrchannel24Index,
       "pmopm8Mesrchannel24Portn": pmopm8Mesrchannel24Portn,
       "pmopm8Mesrchannel25Table": pmopm8Mesrchannel25Table,
       "pmopm8Mesrchannel25Entry": pmopm8Mesrchannel25Entry,
       "pmopm8Mesrchannel25Index": pmopm8Mesrchannel25Index,
       "pmopm8Mesrchannel25Portn": pmopm8Mesrchannel25Portn,
       "pmopm8Mesrchannel26Table": pmopm8Mesrchannel26Table,
       "pmopm8Mesrchannel26Entry": pmopm8Mesrchannel26Entry,
       "pmopm8Mesrchannel26Index": pmopm8Mesrchannel26Index,
       "pmopm8Mesrchannel26Portn": pmopm8Mesrchannel26Portn,
       "pmopm8Mesrchannel27Table": pmopm8Mesrchannel27Table,
       "pmopm8Mesrchannel27Entry": pmopm8Mesrchannel27Entry,
       "pmopm8Mesrchannel27Index": pmopm8Mesrchannel27Index,
       "pmopm8Mesrchannel27Portn": pmopm8Mesrchannel27Portn,
       "pmopm8Mesrchannel28Table": pmopm8Mesrchannel28Table,
       "pmopm8Mesrchannel28Entry": pmopm8Mesrchannel28Entry,
       "pmopm8Mesrchannel28Index": pmopm8Mesrchannel28Index,
       "pmopm8Mesrchannel28Portn": pmopm8Mesrchannel28Portn,
       "pmopm8Mesrchannel29Table": pmopm8Mesrchannel29Table,
       "pmopm8Mesrchannel29Entry": pmopm8Mesrchannel29Entry,
       "pmopm8Mesrchannel29Index": pmopm8Mesrchannel29Index,
       "pmopm8Mesrchannel29Portn": pmopm8Mesrchannel29Portn,
       "pmopm8Mesrchannel30Table": pmopm8Mesrchannel30Table,
       "pmopm8Mesrchannel30Entry": pmopm8Mesrchannel30Entry,
       "pmopm8Mesrchannel30Index": pmopm8Mesrchannel30Index,
       "pmopm8Mesrchannel30Portn": pmopm8Mesrchannel30Portn,
       "pmopm8Mesrchannel31Table": pmopm8Mesrchannel31Table,
       "pmopm8Mesrchannel31Entry": pmopm8Mesrchannel31Entry,
       "pmopm8Mesrchannel31Index": pmopm8Mesrchannel31Index,
       "pmopm8Mesrchannel31Portn": pmopm8Mesrchannel31Portn,
       "pmopm8Mesrchannel32Table": pmopm8Mesrchannel32Table,
       "pmopm8Mesrchannel32Entry": pmopm8Mesrchannel32Entry,
       "pmopm8Mesrchannel32Index": pmopm8Mesrchannel32Index,
       "pmopm8Mesrchannel32Portn": pmopm8Mesrchannel32Portn,
       "pmopm8Mesrchannel33Table": pmopm8Mesrchannel33Table,
       "pmopm8Mesrchannel33Entry": pmopm8Mesrchannel33Entry,
       "pmopm8Mesrchannel33Index": pmopm8Mesrchannel33Index,
       "pmopm8Mesrchannel33Portn": pmopm8Mesrchannel33Portn,
       "pmopm8Mesrchannel34Table": pmopm8Mesrchannel34Table,
       "pmopm8Mesrchannel34Entry": pmopm8Mesrchannel34Entry,
       "pmopm8Mesrchannel34Index": pmopm8Mesrchannel34Index,
       "pmopm8Mesrchannel34Portn": pmopm8Mesrchannel34Portn,
       "pmopm8Mesrchannel35Table": pmopm8Mesrchannel35Table,
       "pmopm8Mesrchannel35Entry": pmopm8Mesrchannel35Entry,
       "pmopm8Mesrchannel35Index": pmopm8Mesrchannel35Index,
       "pmopm8Mesrchannel35Portn": pmopm8Mesrchannel35Portn,
       "pmopm8Mesrchannel36Table": pmopm8Mesrchannel36Table,
       "pmopm8Mesrchannel36Entry": pmopm8Mesrchannel36Entry,
       "pmopm8Mesrchannel36Index": pmopm8Mesrchannel36Index,
       "pmopm8Mesrchannel36Portn": pmopm8Mesrchannel36Portn,
       "pmopm8Mesrchannel37Table": pmopm8Mesrchannel37Table,
       "pmopm8Mesrchannel37Entry": pmopm8Mesrchannel37Entry,
       "pmopm8Mesrchannel37Index": pmopm8Mesrchannel37Index,
       "pmopm8Mesrchannel37Portn": pmopm8Mesrchannel37Portn,
       "pmopm8Mesrchannel38Table": pmopm8Mesrchannel38Table,
       "pmopm8Mesrchannel38Entry": pmopm8Mesrchannel38Entry,
       "pmopm8Mesrchannel38Index": pmopm8Mesrchannel38Index,
       "pmopm8Mesrchannel38Portn": pmopm8Mesrchannel38Portn,
       "pmopm8Mesrchannel39Table": pmopm8Mesrchannel39Table,
       "pmopm8Mesrchannel39Entry": pmopm8Mesrchannel39Entry,
       "pmopm8Mesrchannel39Index": pmopm8Mesrchannel39Index,
       "pmopm8Mesrchannel39Portn": pmopm8Mesrchannel39Portn,
       "pmopm8Mesrchannel40Table": pmopm8Mesrchannel40Table,
       "pmopm8Mesrchannel40Entry": pmopm8Mesrchannel40Entry,
       "pmopm8Mesrchannel40Index": pmopm8Mesrchannel40Index,
       "pmopm8Mesrchannel40Portn": pmopm8Mesrchannel40Portn,
       "pmopm8Mesrchannel41Table": pmopm8Mesrchannel41Table,
       "pmopm8Mesrchannel41Entry": pmopm8Mesrchannel41Entry,
       "pmopm8Mesrchannel41Index": pmopm8Mesrchannel41Index,
       "pmopm8Mesrchannel41Portn": pmopm8Mesrchannel41Portn,
       "pmopm8Mesrchannel42Table": pmopm8Mesrchannel42Table,
       "pmopm8Mesrchannel42Entry": pmopm8Mesrchannel42Entry,
       "pmopm8Mesrchannel42Index": pmopm8Mesrchannel42Index,
       "pmopm8Mesrchannel42Portn": pmopm8Mesrchannel42Portn,
       "pmopm8Mesrchannel43Table": pmopm8Mesrchannel43Table,
       "pmopm8Mesrchannel43Entry": pmopm8Mesrchannel43Entry,
       "pmopm8Mesrchannel43Index": pmopm8Mesrchannel43Index,
       "pmopm8Mesrchannel43Portn": pmopm8Mesrchannel43Portn,
       "pmopm8Mesrchannel44Table": pmopm8Mesrchannel44Table,
       "pmopm8Mesrchannel44Entry": pmopm8Mesrchannel44Entry,
       "pmopm8Mesrchannel44Index": pmopm8Mesrchannel44Index,
       "pmopm8Mesrchannel44Portn": pmopm8Mesrchannel44Portn,
       "pmopm8Mesrchannel45Table": pmopm8Mesrchannel45Table,
       "pmopm8Mesrchannel45Entry": pmopm8Mesrchannel45Entry,
       "pmopm8Mesrchannel45Index": pmopm8Mesrchannel45Index,
       "pmopm8Mesrchannel45Portn": pmopm8Mesrchannel45Portn,
       "pmopm8Mesrchannel46Table": pmopm8Mesrchannel46Table,
       "pmopm8Mesrchannel46Entry": pmopm8Mesrchannel46Entry,
       "pmopm8Mesrchannel46Index": pmopm8Mesrchannel46Index,
       "pmopm8Mesrchannel46Portn": pmopm8Mesrchannel46Portn,
       "pmopm8Mesrchannel47Table": pmopm8Mesrchannel47Table,
       "pmopm8Mesrchannel47Entry": pmopm8Mesrchannel47Entry,
       "pmopm8Mesrchannel47Index": pmopm8Mesrchannel47Index,
       "pmopm8Mesrchannel47Portn": pmopm8Mesrchannel47Portn,
       "pmopm8Mesrchannel48Table": pmopm8Mesrchannel48Table,
       "pmopm8Mesrchannel48Entry": pmopm8Mesrchannel48Entry,
       "pmopm8Mesrchannel48Index": pmopm8Mesrchannel48Index,
       "pmopm8Mesrchannel48Portn": pmopm8Mesrchannel48Portn,
       "pmopm8Mesrchannel49Table": pmopm8Mesrchannel49Table,
       "pmopm8Mesrchannel49Entry": pmopm8Mesrchannel49Entry,
       "pmopm8Mesrchannel49Index": pmopm8Mesrchannel49Index,
       "pmopm8Mesrchannel49Portn": pmopm8Mesrchannel49Portn,
       "pmopm8Mesrchannel50Table": pmopm8Mesrchannel50Table,
       "pmopm8Mesrchannel50Entry": pmopm8Mesrchannel50Entry,
       "pmopm8Mesrchannel50Index": pmopm8Mesrchannel50Index,
       "pmopm8Mesrchannel50Portn": pmopm8Mesrchannel50Portn,
       "pmopm8Mesrchannel51Table": pmopm8Mesrchannel51Table,
       "pmopm8Mesrchannel51Entry": pmopm8Mesrchannel51Entry,
       "pmopm8Mesrchannel51Index": pmopm8Mesrchannel51Index,
       "pmopm8Mesrchannel51Portn": pmopm8Mesrchannel51Portn,
       "pmopm8Mesrchannel52Table": pmopm8Mesrchannel52Table,
       "pmopm8Mesrchannel52Entry": pmopm8Mesrchannel52Entry,
       "pmopm8Mesrchannel52Index": pmopm8Mesrchannel52Index,
       "pmopm8Mesrchannel52Portn": pmopm8Mesrchannel52Portn,
       "pmopm8Mesrchannel53Table": pmopm8Mesrchannel53Table,
       "pmopm8Mesrchannel53Entry": pmopm8Mesrchannel53Entry,
       "pmopm8Mesrchannel53Index": pmopm8Mesrchannel53Index,
       "pmopm8Mesrchannel53Portn": pmopm8Mesrchannel53Portn,
       "pmopm8Mesrchannel54Table": pmopm8Mesrchannel54Table,
       "pmopm8Mesrchannel54Entry": pmopm8Mesrchannel54Entry,
       "pmopm8Mesrchannel54Index": pmopm8Mesrchannel54Index,
       "pmopm8Mesrchannel54Portn": pmopm8Mesrchannel54Portn,
       "pmopm8Mesrchannel55Table": pmopm8Mesrchannel55Table,
       "pmopm8Mesrchannel55Entry": pmopm8Mesrchannel55Entry,
       "pmopm8Mesrchannel55Index": pmopm8Mesrchannel55Index,
       "pmopm8Mesrchannel55Portn": pmopm8Mesrchannel55Portn,
       "pmopm8Mesrchannel56Table": pmopm8Mesrchannel56Table,
       "pmopm8Mesrchannel56Entry": pmopm8Mesrchannel56Entry,
       "pmopm8Mesrchannel56Index": pmopm8Mesrchannel56Index,
       "pmopm8Mesrchannel56Portn": pmopm8Mesrchannel56Portn,
       "pmopm8Mesrchannel57Table": pmopm8Mesrchannel57Table,
       "pmopm8Mesrchannel57Entry": pmopm8Mesrchannel57Entry,
       "pmopm8Mesrchannel57Index": pmopm8Mesrchannel57Index,
       "pmopm8Mesrchannel57Portn": pmopm8Mesrchannel57Portn,
       "pmopm8Mesrchannel58Table": pmopm8Mesrchannel58Table,
       "pmopm8Mesrchannel58Entry": pmopm8Mesrchannel58Entry,
       "pmopm8Mesrchannel58Index": pmopm8Mesrchannel58Index,
       "pmopm8Mesrchannel58Portn": pmopm8Mesrchannel58Portn,
       "pmopm8Mesrchannel59Table": pmopm8Mesrchannel59Table,
       "pmopm8Mesrchannel59Entry": pmopm8Mesrchannel59Entry,
       "pmopm8Mesrchannel59Index": pmopm8Mesrchannel59Index,
       "pmopm8Mesrchannel59Portn": pmopm8Mesrchannel59Portn,
       "pmopm8Mesrchannel60Table": pmopm8Mesrchannel60Table,
       "pmopm8Mesrchannel60Entry": pmopm8Mesrchannel60Entry,
       "pmopm8Mesrchannel60Index": pmopm8Mesrchannel60Index,
       "pmopm8Mesrchannel60Portn": pmopm8Mesrchannel60Portn,
       "pmopm8Mesrchannel61Table": pmopm8Mesrchannel61Table,
       "pmopm8Mesrchannel61Entry": pmopm8Mesrchannel61Entry,
       "pmopm8Mesrchannel61Index": pmopm8Mesrchannel61Index,
       "pmopm8Mesrchannel61Portn": pmopm8Mesrchannel61Portn,
       "pmopm8Mesrchannel62Table": pmopm8Mesrchannel62Table,
       "pmopm8Mesrchannel62Entry": pmopm8Mesrchannel62Entry,
       "pmopm8Mesrchannel62Index": pmopm8Mesrchannel62Index,
       "pmopm8Mesrchannel62Portn": pmopm8Mesrchannel62Portn,
       "pmopm8Mesrchannel63Table": pmopm8Mesrchannel63Table,
       "pmopm8Mesrchannel63Entry": pmopm8Mesrchannel63Entry,
       "pmopm8Mesrchannel63Index": pmopm8Mesrchannel63Index,
       "pmopm8Mesrchannel63Portn": pmopm8Mesrchannel63Portn,
       "pmopm8Mesrchannel64Table": pmopm8Mesrchannel64Table,
       "pmopm8Mesrchannel64Entry": pmopm8Mesrchannel64Entry,
       "pmopm8Mesrchannel64Index": pmopm8Mesrchannel64Index,
       "pmopm8Mesrchannel64Portn": pmopm8Mesrchannel64Portn,
       "pmopm8Mesrchannel65Table": pmopm8Mesrchannel65Table,
       "pmopm8Mesrchannel65Entry": pmopm8Mesrchannel65Entry,
       "pmopm8Mesrchannel65Index": pmopm8Mesrchannel65Index,
       "pmopm8Mesrchannel65Portn": pmopm8Mesrchannel65Portn,
       "pmopm8Mesrchannel66Table": pmopm8Mesrchannel66Table,
       "pmopm8Mesrchannel66Entry": pmopm8Mesrchannel66Entry,
       "pmopm8Mesrchannel66Index": pmopm8Mesrchannel66Index,
       "pmopm8Mesrchannel66Portn": pmopm8Mesrchannel66Portn,
       "pmopm8Mesrchannel67Table": pmopm8Mesrchannel67Table,
       "pmopm8Mesrchannel67Entry": pmopm8Mesrchannel67Entry,
       "pmopm8Mesrchannel67Index": pmopm8Mesrchannel67Index,
       "pmopm8Mesrchannel67Portn": pmopm8Mesrchannel67Portn,
       "pmopm8Mesrchannel68Table": pmopm8Mesrchannel68Table,
       "pmopm8Mesrchannel68Entry": pmopm8Mesrchannel68Entry,
       "pmopm8Mesrchannel68Index": pmopm8Mesrchannel68Index,
       "pmopm8Mesrchannel68Portn": pmopm8Mesrchannel68Portn,
       "pmopm8Mesrchannel69Table": pmopm8Mesrchannel69Table,
       "pmopm8Mesrchannel69Entry": pmopm8Mesrchannel69Entry,
       "pmopm8Mesrchannel69Index": pmopm8Mesrchannel69Index,
       "pmopm8Mesrchannel69Portn": pmopm8Mesrchannel69Portn,
       "pmopm8Mesrchannel70Table": pmopm8Mesrchannel70Table,
       "pmopm8Mesrchannel70Entry": pmopm8Mesrchannel70Entry,
       "pmopm8Mesrchannel70Index": pmopm8Mesrchannel70Index,
       "pmopm8Mesrchannel70Portn": pmopm8Mesrchannel70Portn,
       "pmopm8Mesrchannel71Table": pmopm8Mesrchannel71Table,
       "pmopm8Mesrchannel71Entry": pmopm8Mesrchannel71Entry,
       "pmopm8Mesrchannel71Index": pmopm8Mesrchannel71Index,
       "pmopm8Mesrchannel71Portn": pmopm8Mesrchannel71Portn,
       "pmopm8Mesrchannel72Table": pmopm8Mesrchannel72Table,
       "pmopm8Mesrchannel72Entry": pmopm8Mesrchannel72Entry,
       "pmopm8Mesrchannel72Index": pmopm8Mesrchannel72Index,
       "pmopm8Mesrchannel72Portn": pmopm8Mesrchannel72Portn,
       "pmopm8Mesrchannel73Table": pmopm8Mesrchannel73Table,
       "pmopm8Mesrchannel73Entry": pmopm8Mesrchannel73Entry,
       "pmopm8Mesrchannel73Index": pmopm8Mesrchannel73Index,
       "pmopm8Mesrchannel73Portn": pmopm8Mesrchannel73Portn,
       "pmopm8Mesrchannel74Table": pmopm8Mesrchannel74Table,
       "pmopm8Mesrchannel74Entry": pmopm8Mesrchannel74Entry,
       "pmopm8Mesrchannel74Index": pmopm8Mesrchannel74Index,
       "pmopm8Mesrchannel74Portn": pmopm8Mesrchannel74Portn,
       "pmopm8Mesrchannel75Table": pmopm8Mesrchannel75Table,
       "pmopm8Mesrchannel75Entry": pmopm8Mesrchannel75Entry,
       "pmopm8Mesrchannel75Index": pmopm8Mesrchannel75Index,
       "pmopm8Mesrchannel75Portn": pmopm8Mesrchannel75Portn,
       "pmopm8Mesrchannel76Table": pmopm8Mesrchannel76Table,
       "pmopm8Mesrchannel76Entry": pmopm8Mesrchannel76Entry,
       "pmopm8Mesrchannel76Index": pmopm8Mesrchannel76Index,
       "pmopm8Mesrchannel76Portn": pmopm8Mesrchannel76Portn,
       "pmopm8Mesrchannel77Table": pmopm8Mesrchannel77Table,
       "pmopm8Mesrchannel77Entry": pmopm8Mesrchannel77Entry,
       "pmopm8Mesrchannel77Index": pmopm8Mesrchannel77Index,
       "pmopm8Mesrchannel77Portn": pmopm8Mesrchannel77Portn,
       "pmopm8Mesrchannel78Table": pmopm8Mesrchannel78Table,
       "pmopm8Mesrchannel78Entry": pmopm8Mesrchannel78Entry,
       "pmopm8Mesrchannel78Index": pmopm8Mesrchannel78Index,
       "pmopm8Mesrchannel78Portn": pmopm8Mesrchannel78Portn,
       "pmopm8Mesrchannel79Table": pmopm8Mesrchannel79Table,
       "pmopm8Mesrchannel79Entry": pmopm8Mesrchannel79Entry,
       "pmopm8Mesrchannel79Index": pmopm8Mesrchannel79Index,
       "pmopm8Mesrchannel79Portn": pmopm8Mesrchannel79Portn,
       "pmopm8Mesrchannel80Table": pmopm8Mesrchannel80Table,
       "pmopm8Mesrchannel80Entry": pmopm8Mesrchannel80Entry,
       "pmopm8Mesrchannel80Index": pmopm8Mesrchannel80Index,
       "pmopm8Mesrchannel80Portn": pmopm8Mesrchannel80Portn,
       "pmopm8Mesrchannel81Table": pmopm8Mesrchannel81Table,
       "pmopm8Mesrchannel81Entry": pmopm8Mesrchannel81Entry,
       "pmopm8Mesrchannel81Index": pmopm8Mesrchannel81Index,
       "pmopm8Mesrchannel81Portn": pmopm8Mesrchannel81Portn,
       "pmopm8Mesrchannel82Table": pmopm8Mesrchannel82Table,
       "pmopm8Mesrchannel82Entry": pmopm8Mesrchannel82Entry,
       "pmopm8Mesrchannel82Index": pmopm8Mesrchannel82Index,
       "pmopm8Mesrchannel82Portn": pmopm8Mesrchannel82Portn,
       "pmopm8Mesrchannel83Table": pmopm8Mesrchannel83Table,
       "pmopm8Mesrchannel83Entry": pmopm8Mesrchannel83Entry,
       "pmopm8Mesrchannel83Index": pmopm8Mesrchannel83Index,
       "pmopm8Mesrchannel83Portn": pmopm8Mesrchannel83Portn,
       "pmopm8Mesrchannel84Table": pmopm8Mesrchannel84Table,
       "pmopm8Mesrchannel84Entry": pmopm8Mesrchannel84Entry,
       "pmopm8Mesrchannel84Index": pmopm8Mesrchannel84Index,
       "pmopm8Mesrchannel84Portn": pmopm8Mesrchannel84Portn,
       "pmopm8Mesrchannel85Table": pmopm8Mesrchannel85Table,
       "pmopm8Mesrchannel85Entry": pmopm8Mesrchannel85Entry,
       "pmopm8Mesrchannel85Index": pmopm8Mesrchannel85Index,
       "pmopm8Mesrchannel85Portn": pmopm8Mesrchannel85Portn,
       "pmopm8Mesrchannel86Table": pmopm8Mesrchannel86Table,
       "pmopm8Mesrchannel86Entry": pmopm8Mesrchannel86Entry,
       "pmopm8Mesrchannel86Index": pmopm8Mesrchannel86Index,
       "pmopm8Mesrchannel86Portn": pmopm8Mesrchannel86Portn,
       "pmopm8Mesrchannel87Table": pmopm8Mesrchannel87Table,
       "pmopm8Mesrchannel87Entry": pmopm8Mesrchannel87Entry,
       "pmopm8Mesrchannel87Index": pmopm8Mesrchannel87Index,
       "pmopm8Mesrchannel87Portn": pmopm8Mesrchannel87Portn,
       "pmopm8Mesrchannel88Table": pmopm8Mesrchannel88Table,
       "pmopm8Mesrchannel88Entry": pmopm8Mesrchannel88Entry,
       "pmopm8Mesrchannel88Index": pmopm8Mesrchannel88Index,
       "pmopm8Mesrchannel88Portn": pmopm8Mesrchannel88Portn,
       "pmopm8Mesrchannel89Table": pmopm8Mesrchannel89Table,
       "pmopm8Mesrchannel89Entry": pmopm8Mesrchannel89Entry,
       "pmopm8Mesrchannel89Index": pmopm8Mesrchannel89Index,
       "pmopm8Mesrchannel89Portn": pmopm8Mesrchannel89Portn,
       "pmopm8Mesrchannel90Table": pmopm8Mesrchannel90Table,
       "pmopm8Mesrchannel90Entry": pmopm8Mesrchannel90Entry,
       "pmopm8Mesrchannel90Index": pmopm8Mesrchannel90Index,
       "pmopm8Mesrchannel90Portn": pmopm8Mesrchannel90Portn,
       "pmopm8Mesrchannel91Table": pmopm8Mesrchannel91Table,
       "pmopm8Mesrchannel91Entry": pmopm8Mesrchannel91Entry,
       "pmopm8Mesrchannel91Index": pmopm8Mesrchannel91Index,
       "pmopm8Mesrchannel91Portn": pmopm8Mesrchannel91Portn,
       "pmopm8Mesrchannel92Table": pmopm8Mesrchannel92Table,
       "pmopm8Mesrchannel92Entry": pmopm8Mesrchannel92Entry,
       "pmopm8Mesrchannel92Index": pmopm8Mesrchannel92Index,
       "pmopm8Mesrchannel92Portn": pmopm8Mesrchannel92Portn,
       "pmopm8Mesrchannel93Table": pmopm8Mesrchannel93Table,
       "pmopm8Mesrchannel93Entry": pmopm8Mesrchannel93Entry,
       "pmopm8Mesrchannel93Index": pmopm8Mesrchannel93Index,
       "pmopm8Mesrchannel93Portn": pmopm8Mesrchannel93Portn,
       "pmopm8Mesrchannel94Table": pmopm8Mesrchannel94Table,
       "pmopm8Mesrchannel94Entry": pmopm8Mesrchannel94Entry,
       "pmopm8Mesrchannel94Index": pmopm8Mesrchannel94Index,
       "pmopm8Mesrchannel94Portn": pmopm8Mesrchannel94Portn,
       "pmopm8Mesrchannel95Table": pmopm8Mesrchannel95Table,
       "pmopm8Mesrchannel95Entry": pmopm8Mesrchannel95Entry,
       "pmopm8Mesrchannel95Index": pmopm8Mesrchannel95Index,
       "pmopm8Mesrchannel95Portn": pmopm8Mesrchannel95Portn,
       "pmopm8Mesrchannel96Table": pmopm8Mesrchannel96Table,
       "pmopm8Mesrchannel96Entry": pmopm8Mesrchannel96Entry,
       "pmopm8Mesrchannel96Index": pmopm8Mesrchannel96Index,
       "pmopm8Mesrchannel96Portn": pmopm8Mesrchannel96Portn,
       "pmopm8MesrportInputPwrTable": pmopm8MesrportInputPwrTable,
       "pmopm8MesrportInputPwrEntry": pmopm8MesrportInputPwrEntry,
       "pmopm8MesrportInputPwrIndex": pmopm8MesrportInputPwrIndex,
       "pmopm8MesrportInputPwrPortn": pmopm8MesrportInputPwrPortn,
       "pmopm8MesrchannelMaxPwrTable": pmopm8MesrchannelMaxPwrTable,
       "pmopm8MesrchannelMaxPwrEntry": pmopm8MesrchannelMaxPwrEntry,
       "pmopm8MesrchannelMaxPwrIndex": pmopm8MesrchannelMaxPwrIndex,
       "pmopm8MesrchannelMaxPwrPortn": pmopm8MesrchannelMaxPwrPortn,
       "pmopm8MesrchannelMinPwrTable": pmopm8MesrchannelMinPwrTable,
       "pmopm8MesrchannelMinPwrEntry": pmopm8MesrchannelMinPwrEntry,
       "pmopm8MesrchannelMinPwrIndex": pmopm8MesrchannelMinPwrIndex,
       "pmopm8MesrchannelMinPwrPortn": pmopm8MesrchannelMinPwrPortn,
       "pmopm8MesrLine": pmopm8MesrLine,
       "pmopm8controlsWrite": pmopm8controlsWrite,
       "pmopm8CtrlOther": pmopm8CtrlOther,
       "pmopm8CtrlconfMgnt1": pmopm8CtrlconfMgnt1,
       "pmopm8CtrlConf1Load1": pmopm8CtrlConf1Load1,
       "pmopm8CtrlConf2Load1": pmopm8CtrlConf2Load1,
       "pmopm8CtrlConf2Flash1": pmopm8CtrlConf2Flash1,
       "pmopm8CtrlConf2Clear1": pmopm8CtrlConf2Clear1,
       "pmopm8Ctrlsynth4": pmopm8Ctrlsynth4,
       "pmopm8CtrlCorrelatOn": pmopm8CtrlCorrelatOn,
       "pmopm8CtrlCorrelatOff": pmopm8CtrlCorrelatOff,
       "pmopm8CtrlswMgnt": pmopm8CtrlswMgnt,
       "pmopm8CtrlColdReset": pmopm8CtrlColdReset,
       "pmopm8CtrlWarmReset": pmopm8CtrlWarmReset,
       "pmopm8CtrlLoadSwBank1": pmopm8CtrlLoadSwBank1,
       "pmopm8CtrlLoadSwBank2": pmopm8CtrlLoadSwBank2,
       "pmopm8CtrlgwMgnt": pmopm8CtrlgwMgnt,
       "pmopm8CtrlCurrentGwReset": pmopm8CtrlCurrentGwReset,
       "pmopm8CtrlLoadGwBank1": pmopm8CtrlLoadGwBank1,
       "pmopm8CtrlLoadGwBank2": pmopm8CtrlLoadGwBank2,
       "pmopm8CtrlLoadGwBank3": pmopm8CtrlLoadGwBank3,
       "pmopm8CtrlLoadGwBank4": pmopm8CtrlLoadGwBank4,
       "pmopm8CtrlledTest": pmopm8CtrlledTest,
       "pmopm8CtrlGreenLed": pmopm8CtrlGreenLed,
       "pmopm8CtrlRedLed": pmopm8CtrlRedLed,
       "pmopm8CtrlLedOff": pmopm8CtrlLedOff,
       "pmopm8CtrlClient": pmopm8CtrlClient,
       "pmopm8CtrlcalibrationTable": pmopm8CtrlcalibrationTable,
       "pmopm8CtrlcalibrationEntry": pmopm8CtrlcalibrationEntry,
       "pmopm8CtrlcalibrationIndex": pmopm8CtrlcalibrationIndex,
       "pmopm8CtrlcalibrationPortn": pmopm8CtrlcalibrationPortn,
       "pmopm8CtrlspectrumAutodiscoveryTable": pmopm8CtrlspectrumAutodiscoveryTable,
       "pmopm8CtrlspectrumAutodiscoveryEntry": pmopm8CtrlspectrumAutodiscoveryEntry,
       "pmopm8CtrlspectrumAutodiscoveryIndex": pmopm8CtrlspectrumAutodiscoveryIndex,
       "pmopm8CtrlspectrumAutodiscoveryPortn": pmopm8CtrlspectrumAutodiscoveryPortn,
       "pmopm8CtrlthresholdsAutoconfigTable": pmopm8CtrlthresholdsAutoconfigTable,
       "pmopm8CtrlthresholdsAutoconfigEntry": pmopm8CtrlthresholdsAutoconfigEntry,
       "pmopm8CtrlthresholdsAutoconfigIndex": pmopm8CtrlthresholdsAutoconfigIndex,
       "pmopm8CtrlthresholdsAutoconfigPortn": pmopm8CtrlthresholdsAutoconfigPortn,
       "pmopm8CtrlpowerLossDeltaTable": pmopm8CtrlpowerLossDeltaTable,
       "pmopm8CtrlpowerLossDeltaEntry": pmopm8CtrlpowerLossDeltaEntry,
       "pmopm8CtrlpowerLossDeltaIndex": pmopm8CtrlpowerLossDeltaIndex,
       "pmopm8CtrlpowerLossDeltaPortn": pmopm8CtrlpowerLossDeltaPortn,
       "pmopm8CtrlpowerHighDeltaTable": pmopm8CtrlpowerHighDeltaTable,
       "pmopm8CtrlpowerHighDeltaEntry": pmopm8CtrlpowerHighDeltaEntry,
       "pmopm8CtrlpowerHighDeltaIndex": pmopm8CtrlpowerHighDeltaIndex,
       "pmopm8CtrlpowerHighDeltaPortn": pmopm8CtrlpowerHighDeltaPortn,
       "pmopm8CtrlpowerLowDeltaTable": pmopm8CtrlpowerLowDeltaTable,
       "pmopm8CtrlpowerLowDeltaEntry": pmopm8CtrlpowerLowDeltaEntry,
       "pmopm8CtrlpowerLowDeltaIndex": pmopm8CtrlpowerLowDeltaIndex,
       "pmopm8CtrlpowerLowDeltaPortn": pmopm8CtrlpowerLowDeltaPortn,
       "pmopm8CtrlinputPowerRefTable": pmopm8CtrlinputPowerRefTable,
       "pmopm8CtrlinputPowerRefEntry": pmopm8CtrlinputPowerRefEntry,
       "pmopm8CtrlinputPowerRefIndex": pmopm8CtrlinputPowerRefIndex,
       "pmopm8CtrlinputPowerRefPortn": pmopm8CtrlinputPowerRefPortn,
       "pmopm8CtrlLine": pmopm8CtrlLine,
       "pmopm8ri": pmopm8ri,
       "pmopm8riTable": pmopm8riTable,
       "pmopm8RinvSfpTable": pmopm8RinvSfpTable,
       "pmopm8RinvSfpEntry": pmopm8RinvSfpEntry,
       "pmopm8RinvSfpIndex": pmopm8RinvSfpIndex,
       "pmopm8Rinvsfp": pmopm8Rinvsfp,
       "pmopm8RinvLineTable": pmopm8RinvLineTable,
       "pmopm8RinvLineEntry": pmopm8RinvLineEntry,
       "pmopm8RinvLineIndex": pmopm8RinvLineIndex,
       "pmopm8RinvxfpLine": pmopm8RinvxfpLine,
       "pmopm8RinvReloadInventory": pmopm8RinvReloadInventory,
       "pmopm8RinvHwPlatform": pmopm8RinvHwPlatform,
       "pmopm8RinvModulePlatform": pmopm8RinvModulePlatform,
       "pmopm8RinvSwPlatform": pmopm8RinvSwPlatform,
       "pmopm8RinvGwPlatform": pmopm8RinvGwPlatform,
       "pmopm8download": pmopm8download,
       "pmopm8DwlOther": pmopm8DwlOther,
       "pmopm8DwlrestartProcess": pmopm8DwlrestartProcess,
       "pmopm8DwlWarmRestartProcessed": pmopm8DwlWarmRestartProcessed,
       "pmopm8DwlColdRestartProcessed": pmopm8DwlColdRestartProcessed,
       "pmopm8DwlswBanksUsed": pmopm8DwlswBanksUsed,
       "pmopm8DwlSwBank1Used": pmopm8DwlSwBank1Used,
       "pmopm8DwlSwBank2Used": pmopm8DwlSwBank2Used,
       "pmopm8DwlSwBank1Notempty": pmopm8DwlSwBank1Notempty,
       "pmopm8DwlSwBank2Notempty": pmopm8DwlSwBank2Notempty,
       "pmopm8DwlgwBanksUsed": pmopm8DwlgwBanksUsed,
       "pmopm8DwlGwBank1Used": pmopm8DwlGwBank1Used,
       "pmopm8DwlGwBank2Used": pmopm8DwlGwBank2Used,
       "pmopm8DwlGwBank3Used": pmopm8DwlGwBank3Used,
       "pmopm8DwlGwBank4Used": pmopm8DwlGwBank4Used,
       "pmopm8DwlGwBank1Notempty": pmopm8DwlGwBank1Notempty,
       "pmopm8DwlGwBank2Notempty": pmopm8DwlGwBank2Notempty,
       "pmopm8DwlGwBank3Notempty": pmopm8DwlGwBank3Notempty,
       "pmopm8DwlGwBank4Notempty": pmopm8DwlGwBank4Notempty,
       "pmopm8DwlClient": pmopm8DwlClient,
       "pmopm8DwlLine": pmopm8DwlLine,
       "pmopm8Config": pmopm8Config,
       "pmopm8CfgLsd": pmopm8CfgLsd,
       "pmopm8tableclientcaiscsf": pmopm8tableclientcaiscsf,
       "pmopm8CfgStartup": pmopm8CfgStartup,
       "pmopm8tableother": pmopm8tableother,
       "pmopm8CfgcomponentType": pmopm8CfgcomponentType,
       "pmopm8Cfgmiscellaneous": pmopm8Cfgmiscellaneous,
       "pmopm8CfgfirstChannel": pmopm8CfgfirstChannel,
       "pmopm8CfglastChannel": pmopm8CfglastChannel,
       "pmopm8Cfggrid": pmopm8Cfggrid,
       "pmopm8CfgClientStartupOosTable": pmopm8CfgClientStartupOosTable,
       "pmopm8CfgClientStartupOosEntry": pmopm8CfgClientStartupOosEntry,
       "pmopm8CfgClientStartupOosIndex": pmopm8CfgClientStartupOosIndex,
       "pmopm8CfgSpectrumOosPortn": pmopm8CfgSpectrumOosPortn,
       "pmopm8CfgSpectrumOffsetPortn": pmopm8CfgSpectrumOffsetPortn,
       "pmopm8CfgCh1Ch16OosPortn": pmopm8CfgCh1Ch16OosPortn,
       "pmopm8CfgCh17Ch32OosPortn": pmopm8CfgCh17Ch32OosPortn,
       "pmopm8CfgCh33Ch48OosPortn": pmopm8CfgCh33Ch48OosPortn,
       "pmopm8CfgCh49Ch64OosPortn": pmopm8CfgCh49Ch64OosPortn,
       "pmopm8CfgCh65Ch80OosPortn": pmopm8CfgCh65Ch80OosPortn,
       "pmopm8CfgCh81Ch96OosPortn": pmopm8CfgCh81Ch96OosPortn,
       "pmopm8CfgClientStartupBalanceTable": pmopm8CfgClientStartupBalanceTable,
       "pmopm8CfgClientStartupBalanceEntry": pmopm8CfgClientStartupBalanceEntry,
       "pmopm8CfgClientStartupBalanceIndex": pmopm8CfgClientStartupBalanceIndex,
       "pmopm8CfgCh1Ch16BalancePortn": pmopm8CfgCh1Ch16BalancePortn,
       "pmopm8CfgCh17Ch32BalancePortn": pmopm8CfgCh17Ch32BalancePortn,
       "pmopm8CfgCh33Ch48BalancePortn": pmopm8CfgCh33Ch48BalancePortn,
       "pmopm8CfgCh49Ch64BalancePortn": pmopm8CfgCh49Ch64BalancePortn,
       "pmopm8CfgCh65Ch80BalancePortn": pmopm8CfgCh65Ch80BalancePortn,
       "pmopm8CfgCh81Ch96BalancePortn": pmopm8CfgCh81Ch96BalancePortn,
       "pmopm8CfgClientStartupAbsthreshTable": pmopm8CfgClientStartupAbsthreshTable,
       "pmopm8CfgClientStartupAbsthreshEntry": pmopm8CfgClientStartupAbsthreshEntry,
       "pmopm8CfgClientStartupAbsthreshIndex": pmopm8CfgClientStartupAbsthreshIndex,
       "pmopm8CfgChannel1AbsthreshPortn": pmopm8CfgChannel1AbsthreshPortn,
       "pmopm8CfgChannel2AbsthreshPortn": pmopm8CfgChannel2AbsthreshPortn,
       "pmopm8CfgChannel3AbsthreshPortn": pmopm8CfgChannel3AbsthreshPortn,
       "pmopm8CfgChannel4AbsthreshPortn": pmopm8CfgChannel4AbsthreshPortn,
       "pmopm8CfgChannel5AbsthreshPortn": pmopm8CfgChannel5AbsthreshPortn,
       "pmopm8CfgChannel6AbsthreshPortn": pmopm8CfgChannel6AbsthreshPortn,
       "pmopm8CfgChannel7AbsthreshPortn": pmopm8CfgChannel7AbsthreshPortn,
       "pmopm8CfgChannel8AbsthreshPortn": pmopm8CfgChannel8AbsthreshPortn,
       "pmopm8CfgChannel9AbsthreshPortn": pmopm8CfgChannel9AbsthreshPortn,
       "pmopm8CfgChannel10AbsthreshPortn": pmopm8CfgChannel10AbsthreshPortn,
       "pmopm8CfgChannel11AbsthreshPortn": pmopm8CfgChannel11AbsthreshPortn,
       "pmopm8CfgChannel12AbsthreshPortn": pmopm8CfgChannel12AbsthreshPortn,
       "pmopm8CfgChannel13AbsthreshPortn": pmopm8CfgChannel13AbsthreshPortn,
       "pmopm8CfgChannel14AbsthreshPortn": pmopm8CfgChannel14AbsthreshPortn,
       "pmopm8CfgChannel15AbsthreshPortn": pmopm8CfgChannel15AbsthreshPortn,
       "pmopm8CfgChannel16AbsthreshPortn": pmopm8CfgChannel16AbsthreshPortn,
       "pmopm8CfgChannel17AbsthreshPortn": pmopm8CfgChannel17AbsthreshPortn,
       "pmopm8CfgChannel18AbsthreshPortn": pmopm8CfgChannel18AbsthreshPortn,
       "pmopm8CfgChannel19AbsthreshPortn": pmopm8CfgChannel19AbsthreshPortn,
       "pmopm8CfgChannel20AbsthreshPortn": pmopm8CfgChannel20AbsthreshPortn,
       "pmopm8CfgChannel21AbsthreshPortn": pmopm8CfgChannel21AbsthreshPortn,
       "pmopm8CfgChannel22AbsthreshPortn": pmopm8CfgChannel22AbsthreshPortn,
       "pmopm8CfgChannel23AbsthreshPortn": pmopm8CfgChannel23AbsthreshPortn,
       "pmopm8CfgChannel24AbsthreshPortn": pmopm8CfgChannel24AbsthreshPortn,
       "pmopm8CfgChannel25AbsthreshPortn": pmopm8CfgChannel25AbsthreshPortn,
       "pmopm8CfgChannel26AbsthreshPortn": pmopm8CfgChannel26AbsthreshPortn,
       "pmopm8CfgChannel27AbsthreshPortn": pmopm8CfgChannel27AbsthreshPortn,
       "pmopm8CfgChannel28AbsthreshPortn": pmopm8CfgChannel28AbsthreshPortn,
       "pmopm8CfgChannel29AbsthreshPortn": pmopm8CfgChannel29AbsthreshPortn,
       "pmopm8CfgChannel30AbsthreshPortn": pmopm8CfgChannel30AbsthreshPortn,
       "pmopm8CfgChannel31AbsthreshPortn": pmopm8CfgChannel31AbsthreshPortn,
       "pmopm8CfgChannel32AbsthreshPortn": pmopm8CfgChannel32AbsthreshPortn,
       "pmopm8CfgChannel33AbsthreshPortn": pmopm8CfgChannel33AbsthreshPortn,
       "pmopm8CfgChannel34AbsthreshPortn": pmopm8CfgChannel34AbsthreshPortn,
       "pmopm8CfgChannel35AbsthreshPortn": pmopm8CfgChannel35AbsthreshPortn,
       "pmopm8CfgChannel36AbsthreshPortn": pmopm8CfgChannel36AbsthreshPortn,
       "pmopm8CfgChannel37AbsthreshPortn": pmopm8CfgChannel37AbsthreshPortn,
       "pmopm8CfgChannel38AbsthreshPortn": pmopm8CfgChannel38AbsthreshPortn,
       "pmopm8CfgChannel39AbsthreshPortn": pmopm8CfgChannel39AbsthreshPortn,
       "pmopm8CfgChannel40AbsthreshPortn": pmopm8CfgChannel40AbsthreshPortn,
       "pmopm8CfgChannel41AbsthreshPortn": pmopm8CfgChannel41AbsthreshPortn,
       "pmopm8CfgChannel42AbsthreshPortn": pmopm8CfgChannel42AbsthreshPortn,
       "pmopm8CfgChannel43AbsthreshPortn": pmopm8CfgChannel43AbsthreshPortn,
       "pmopm8CfgChannel44AbsthreshPortn": pmopm8CfgChannel44AbsthreshPortn,
       "pmopm8CfgChannel45AbsthreshPortn": pmopm8CfgChannel45AbsthreshPortn,
       "pmopm8CfgChannel46AbsthreshPortn": pmopm8CfgChannel46AbsthreshPortn,
       "pmopm8CfgChannel47AbsthreshPortn": pmopm8CfgChannel47AbsthreshPortn,
       "pmopm8CfgChannel48AbsthreshPortn": pmopm8CfgChannel48AbsthreshPortn,
       "pmopm8CfgChannel49AbsthreshPortn": pmopm8CfgChannel49AbsthreshPortn,
       "pmopm8CfgChannel50AbsthreshPortn": pmopm8CfgChannel50AbsthreshPortn,
       "pmopm8CfgChannel51AbsthreshPortn": pmopm8CfgChannel51AbsthreshPortn,
       "pmopm8CfgChannel52AbsthreshPortn": pmopm8CfgChannel52AbsthreshPortn,
       "pmopm8CfgChannel53AbsthreshPortn": pmopm8CfgChannel53AbsthreshPortn,
       "pmopm8CfgChannel54AbsthreshPortn": pmopm8CfgChannel54AbsthreshPortn,
       "pmopm8CfgChannel55AbsthreshPortn": pmopm8CfgChannel55AbsthreshPortn,
       "pmopm8CfgChannel56AbsthreshPortn": pmopm8CfgChannel56AbsthreshPortn,
       "pmopm8CfgChannel57AbsthreshPortn": pmopm8CfgChannel57AbsthreshPortn,
       "pmopm8CfgChannel58AbsthreshPortn": pmopm8CfgChannel58AbsthreshPortn,
       "pmopm8CfgChannel59AbsthreshPortn": pmopm8CfgChannel59AbsthreshPortn,
       "pmopm8CfgChannel60AbsthreshPortn": pmopm8CfgChannel60AbsthreshPortn,
       "pmopm8CfgChannel61AbsthreshPortn": pmopm8CfgChannel61AbsthreshPortn,
       "pmopm8CfgChannel62AbsthreshPortn": pmopm8CfgChannel62AbsthreshPortn,
       "pmopm8CfgChannel63AbsthreshPortn": pmopm8CfgChannel63AbsthreshPortn,
       "pmopm8CfgChannel64AbsthreshPortn": pmopm8CfgChannel64AbsthreshPortn,
       "pmopm8CfgChannel65AbsthreshPortn": pmopm8CfgChannel65AbsthreshPortn,
       "pmopm8CfgChannel66AbsthreshPortn": pmopm8CfgChannel66AbsthreshPortn,
       "pmopm8CfgChannel67AbsthreshPortn": pmopm8CfgChannel67AbsthreshPortn,
       "pmopm8CfgChannel68AbsthreshPortn": pmopm8CfgChannel68AbsthreshPortn,
       "pmopm8CfgChannel69AbsthreshPortn": pmopm8CfgChannel69AbsthreshPortn,
       "pmopm8CfgChannel70AbsthreshPortn": pmopm8CfgChannel70AbsthreshPortn,
       "pmopm8CfgChannel71AbsthreshPortn": pmopm8CfgChannel71AbsthreshPortn,
       "pmopm8CfgChannel72AbsthreshPortn": pmopm8CfgChannel72AbsthreshPortn,
       "pmopm8CfgChannel73AbsthreshPortn": pmopm8CfgChannel73AbsthreshPortn,
       "pmopm8CfgChannel74AbsthreshPortn": pmopm8CfgChannel74AbsthreshPortn,
       "pmopm8CfgChannel75AbsthreshPortn": pmopm8CfgChannel75AbsthreshPortn,
       "pmopm8CfgChannel76AbsthreshPortn": pmopm8CfgChannel76AbsthreshPortn,
       "pmopm8CfgChannel77AbsthreshPortn": pmopm8CfgChannel77AbsthreshPortn,
       "pmopm8CfgChannel78AbsthreshPortn": pmopm8CfgChannel78AbsthreshPortn,
       "pmopm8CfgChannel79AbsthreshPortn": pmopm8CfgChannel79AbsthreshPortn,
       "pmopm8CfgChannel80AbsthreshPortn": pmopm8CfgChannel80AbsthreshPortn,
       "pmopm8CfgChannel81AbsthreshPortn": pmopm8CfgChannel81AbsthreshPortn,
       "pmopm8CfgChannel82AbsthreshPortn": pmopm8CfgChannel82AbsthreshPortn,
       "pmopm8CfgChannel83AbsthreshPortn": pmopm8CfgChannel83AbsthreshPortn,
       "pmopm8CfgChannel84AbsthreshPortn": pmopm8CfgChannel84AbsthreshPortn,
       "pmopm8CfgChannel85AbsthreshPortn": pmopm8CfgChannel85AbsthreshPortn,
       "pmopm8CfgChannel86AbsthreshPortn": pmopm8CfgChannel86AbsthreshPortn,
       "pmopm8CfgChannel87AbsthreshPortn": pmopm8CfgChannel87AbsthreshPortn,
       "pmopm8CfgChannel88AbsthreshPortn": pmopm8CfgChannel88AbsthreshPortn,
       "pmopm8CfgChannel89AbsthreshPortn": pmopm8CfgChannel89AbsthreshPortn,
       "pmopm8CfgChannel90AbsthreshPortn": pmopm8CfgChannel90AbsthreshPortn,
       "pmopm8CfgChannel91AbsthreshPortn": pmopm8CfgChannel91AbsthreshPortn,
       "pmopm8CfgChannel92AbsthreshPortn": pmopm8CfgChannel92AbsthreshPortn,
       "pmopm8CfgChannel93AbsthreshPortn": pmopm8CfgChannel93AbsthreshPortn,
       "pmopm8CfgChannel94AbsthreshPortn": pmopm8CfgChannel94AbsthreshPortn,
       "pmopm8CfgChannel95AbsthreshPortn": pmopm8CfgChannel95AbsthreshPortn,
       "pmopm8CfgChannel96AbsthreshPortn": pmopm8CfgChannel96AbsthreshPortn,
       "pmopm8CfgClientStartupPwrHighTable": pmopm8CfgClientStartupPwrHighTable,
       "pmopm8CfgClientStartupPwrHighEntry": pmopm8CfgClientStartupPwrHighEntry,
       "pmopm8CfgClientStartupPwrHighIndex": pmopm8CfgClientStartupPwrHighIndex,
       "pmopm8CfgChannel1PwrhighPortn": pmopm8CfgChannel1PwrhighPortn,
       "pmopm8CfgChannel2PwrhighPortn": pmopm8CfgChannel2PwrhighPortn,
       "pmopm8CfgChannel3PwrhighPortn": pmopm8CfgChannel3PwrhighPortn,
       "pmopm8CfgChannel4PwrhighPortn": pmopm8CfgChannel4PwrhighPortn,
       "pmopm8CfgChannel5PwrhighPortn": pmopm8CfgChannel5PwrhighPortn,
       "pmopm8CfgChannel6PwrhighPortn": pmopm8CfgChannel6PwrhighPortn,
       "pmopm8CfgChannel7PwrhighPortn": pmopm8CfgChannel7PwrhighPortn,
       "pmopm8CfgChannel8PwrhighPortn": pmopm8CfgChannel8PwrhighPortn,
       "pmopm8CfgChannel9PwrhighPortn": pmopm8CfgChannel9PwrhighPortn,
       "pmopm8CfgChannel10PwrhighPortn": pmopm8CfgChannel10PwrhighPortn,
       "pmopm8CfgChannel11PwrhighPortn": pmopm8CfgChannel11PwrhighPortn,
       "pmopm8CfgChannel12PwrhighPortn": pmopm8CfgChannel12PwrhighPortn,
       "pmopm8CfgChannel13PwrhighPortn": pmopm8CfgChannel13PwrhighPortn,
       "pmopm8CfgChannel14PwrhighPortn": pmopm8CfgChannel14PwrhighPortn,
       "pmopm8CfgChannel15PwrhighPortn": pmopm8CfgChannel15PwrhighPortn,
       "pmopm8CfgChannel16PwrhighPortn": pmopm8CfgChannel16PwrhighPortn,
       "pmopm8CfgChannel17PwrhighPortn": pmopm8CfgChannel17PwrhighPortn,
       "pmopm8CfgChannel18PwrhighPortn": pmopm8CfgChannel18PwrhighPortn,
       "pmopm8CfgChannel19PwrhighPortn": pmopm8CfgChannel19PwrhighPortn,
       "pmopm8CfgChannel20PwrhighPortn": pmopm8CfgChannel20PwrhighPortn,
       "pmopm8CfgChannel21PwrhighPortn": pmopm8CfgChannel21PwrhighPortn,
       "pmopm8CfgChannel22PwrhighPortn": pmopm8CfgChannel22PwrhighPortn,
       "pmopm8CfgChannel23PwrhighPortn": pmopm8CfgChannel23PwrhighPortn,
       "pmopm8CfgChannel24PwrhighPortn": pmopm8CfgChannel24PwrhighPortn,
       "pmopm8CfgChannel25PwrhighPortn": pmopm8CfgChannel25PwrhighPortn,
       "pmopm8CfgChannel26PwrhighPortn": pmopm8CfgChannel26PwrhighPortn,
       "pmopm8CfgChannel27PwrhighPortn": pmopm8CfgChannel27PwrhighPortn,
       "pmopm8CfgChannel28PwrhighPortn": pmopm8CfgChannel28PwrhighPortn,
       "pmopm8CfgChannel29PwrhighPortn": pmopm8CfgChannel29PwrhighPortn,
       "pmopm8CfgChannel30PwrhighPortn": pmopm8CfgChannel30PwrhighPortn,
       "pmopm8CfgChannel31PwrhighPortn": pmopm8CfgChannel31PwrhighPortn,
       "pmopm8CfgChannel32PwrhighPortn": pmopm8CfgChannel32PwrhighPortn,
       "pmopm8CfgChannel33PwrhighPortn": pmopm8CfgChannel33PwrhighPortn,
       "pmopm8CfgChannel34PwrhighPortn": pmopm8CfgChannel34PwrhighPortn,
       "pmopm8CfgChannel35PwrhighPortn": pmopm8CfgChannel35PwrhighPortn,
       "pmopm8CfgChannel36PwrhighPortn": pmopm8CfgChannel36PwrhighPortn,
       "pmopm8CfgChannel37PwrhighPortn": pmopm8CfgChannel37PwrhighPortn,
       "pmopm8CfgChannel38PwrhighPortn": pmopm8CfgChannel38PwrhighPortn,
       "pmopm8CfgChannel39PwrhighPortn": pmopm8CfgChannel39PwrhighPortn,
       "pmopm8CfgChannel40PwrhighPortn": pmopm8CfgChannel40PwrhighPortn,
       "pmopm8CfgChannel41PwrhighPortn": pmopm8CfgChannel41PwrhighPortn,
       "pmopm8CfgChannel42PwrhighPortn": pmopm8CfgChannel42PwrhighPortn,
       "pmopm8CfgChannel43PwrhighPortn": pmopm8CfgChannel43PwrhighPortn,
       "pmopm8CfgChannel44PwrhighPortn": pmopm8CfgChannel44PwrhighPortn,
       "pmopm8CfgChannel45PwrhighPortn": pmopm8CfgChannel45PwrhighPortn,
       "pmopm8CfgChannel46PwrhighPortn": pmopm8CfgChannel46PwrhighPortn,
       "pmopm8CfgChannel47PwrhighPortn": pmopm8CfgChannel47PwrhighPortn,
       "pmopm8CfgChannel48PwrhighPortn": pmopm8CfgChannel48PwrhighPortn,
       "pmopm8CfgChannel49PwrhighPortn": pmopm8CfgChannel49PwrhighPortn,
       "pmopm8CfgChannel50PwrhighPortn": pmopm8CfgChannel50PwrhighPortn,
       "pmopm8CfgChannel51PwrhighPortn": pmopm8CfgChannel51PwrhighPortn,
       "pmopm8CfgChannel52PwrhighPortn": pmopm8CfgChannel52PwrhighPortn,
       "pmopm8CfgChannel53PwrhighPortn": pmopm8CfgChannel53PwrhighPortn,
       "pmopm8CfgChannel54PwrhighPortn": pmopm8CfgChannel54PwrhighPortn,
       "pmopm8CfgChannel55PwrhighPortn": pmopm8CfgChannel55PwrhighPortn,
       "pmopm8CfgChannel56PwrhighPortn": pmopm8CfgChannel56PwrhighPortn,
       "pmopm8CfgChannel57PwrhighPortn": pmopm8CfgChannel57PwrhighPortn,
       "pmopm8CfgChannel58PwrhighPortn": pmopm8CfgChannel58PwrhighPortn,
       "pmopm8CfgChannel59PwrhighPortn": pmopm8CfgChannel59PwrhighPortn,
       "pmopm8CfgChannel60PwrhighPortn": pmopm8CfgChannel60PwrhighPortn,
       "pmopm8CfgChannel61PwrhighPortn": pmopm8CfgChannel61PwrhighPortn,
       "pmopm8CfgChannel62PwrhighPortn": pmopm8CfgChannel62PwrhighPortn,
       "pmopm8CfgChannel63PwrhighPortn": pmopm8CfgChannel63PwrhighPortn,
       "pmopm8CfgChannel64PwrhighPortn": pmopm8CfgChannel64PwrhighPortn,
       "pmopm8CfgChannel65PwrhighPortn": pmopm8CfgChannel65PwrhighPortn,
       "pmopm8CfgChannel66PwrhighPortn": pmopm8CfgChannel66PwrhighPortn,
       "pmopm8CfgChannel67PwrhighPortn": pmopm8CfgChannel67PwrhighPortn,
       "pmopm8CfgChannel68PwrhighPortn": pmopm8CfgChannel68PwrhighPortn,
       "pmopm8CfgChannel69PwrhighPortn": pmopm8CfgChannel69PwrhighPortn,
       "pmopm8CfgChannel70PwrhighPortn": pmopm8CfgChannel70PwrhighPortn,
       "pmopm8CfgChannel71PwrhighPortn": pmopm8CfgChannel71PwrhighPortn,
       "pmopm8CfgChannel72PwrhighPortn": pmopm8CfgChannel72PwrhighPortn,
       "pmopm8CfgChannel73PwrhighPortn": pmopm8CfgChannel73PwrhighPortn,
       "pmopm8CfgChannel74PwrhighPortn": pmopm8CfgChannel74PwrhighPortn,
       "pmopm8CfgChannel75PwrhighPortn": pmopm8CfgChannel75PwrhighPortn,
       "pmopm8CfgChannel76PwrhighPortn": pmopm8CfgChannel76PwrhighPortn,
       "pmopm8CfgChannel77PwrhighPortn": pmopm8CfgChannel77PwrhighPortn,
       "pmopm8CfgChannel78PwrhighPortn": pmopm8CfgChannel78PwrhighPortn,
       "pmopm8CfgChannel79PwrhighPortn": pmopm8CfgChannel79PwrhighPortn,
       "pmopm8CfgChannel80PwrhighPortn": pmopm8CfgChannel80PwrhighPortn,
       "pmopm8CfgChannel81PwrhighPortn": pmopm8CfgChannel81PwrhighPortn,
       "pmopm8CfgChannel82PwrhighPortn": pmopm8CfgChannel82PwrhighPortn,
       "pmopm8CfgChannel83PwrhighPortn": pmopm8CfgChannel83PwrhighPortn,
       "pmopm8CfgChannel84PwrhighPortn": pmopm8CfgChannel84PwrhighPortn,
       "pmopm8CfgChannel85PwrhighPortn": pmopm8CfgChannel85PwrhighPortn,
       "pmopm8CfgChannel86PwrhighPortn": pmopm8CfgChannel86PwrhighPortn,
       "pmopm8CfgChannel87PwrhighPortn": pmopm8CfgChannel87PwrhighPortn,
       "pmopm8CfgChannel88PwrhighPortn": pmopm8CfgChannel88PwrhighPortn,
       "pmopm8CfgChannel89PwrhighPortn": pmopm8CfgChannel89PwrhighPortn,
       "pmopm8CfgChannel90PwrhighPortn": pmopm8CfgChannel90PwrhighPortn,
       "pmopm8CfgChannel91PwrhighPortn": pmopm8CfgChannel91PwrhighPortn,
       "pmopm8CfgChannel92PwrhighPortn": pmopm8CfgChannel92PwrhighPortn,
       "pmopm8CfgChannel93PwrhighPortn": pmopm8CfgChannel93PwrhighPortn,
       "pmopm8CfgChannel94PwrhighPortn": pmopm8CfgChannel94PwrhighPortn,
       "pmopm8CfgChannel95PwrhighPortn": pmopm8CfgChannel95PwrhighPortn,
       "pmopm8CfgChannel96PwrhighPortn": pmopm8CfgChannel96PwrhighPortn,
       "pmopm8CfgClientStartupPwrLowTable": pmopm8CfgClientStartupPwrLowTable,
       "pmopm8CfgClientStartupPwrLowEntry": pmopm8CfgClientStartupPwrLowEntry,
       "pmopm8CfgClientStartupPwrLowIndex": pmopm8CfgClientStartupPwrLowIndex,
       "pmopm8CfgChannel1PwrlowPortn": pmopm8CfgChannel1PwrlowPortn,
       "pmopm8CfgChannel2PwrlowPortn": pmopm8CfgChannel2PwrlowPortn,
       "pmopm8CfgChannel3PwrlowPortn": pmopm8CfgChannel3PwrlowPortn,
       "pmopm8CfgChannel4PwrlowPortn": pmopm8CfgChannel4PwrlowPortn,
       "pmopm8CfgChannel5PwrlowPortn": pmopm8CfgChannel5PwrlowPortn,
       "pmopm8CfgChannel6PwrlowPortn": pmopm8CfgChannel6PwrlowPortn,
       "pmopm8CfgChannel7PwrlowPortn": pmopm8CfgChannel7PwrlowPortn,
       "pmopm8CfgChannel8PwrlowPortn": pmopm8CfgChannel8PwrlowPortn,
       "pmopm8CfgChannel9PwrlowPortn": pmopm8CfgChannel9PwrlowPortn,
       "pmopm8CfgChannel10PwrlowPortn": pmopm8CfgChannel10PwrlowPortn,
       "pmopm8CfgChannel11PwrlowPortn": pmopm8CfgChannel11PwrlowPortn,
       "pmopm8CfgChannel12PwrlowPortn": pmopm8CfgChannel12PwrlowPortn,
       "pmopm8CfgChannel13PwrlowPortn": pmopm8CfgChannel13PwrlowPortn,
       "pmopm8CfgChannel14PwrlowPortn": pmopm8CfgChannel14PwrlowPortn,
       "pmopm8CfgChannel15PwrlowPortn": pmopm8CfgChannel15PwrlowPortn,
       "pmopm8CfgChannel16PwrlowPortn": pmopm8CfgChannel16PwrlowPortn,
       "pmopm8CfgChannel17PwrlowPortn": pmopm8CfgChannel17PwrlowPortn,
       "pmopm8CfgChannel18PwrlowPortn": pmopm8CfgChannel18PwrlowPortn,
       "pmopm8CfgChannel19PwrlowPortn": pmopm8CfgChannel19PwrlowPortn,
       "pmopm8CfgChannel20PwrlowPortn": pmopm8CfgChannel20PwrlowPortn,
       "pmopm8CfgChannel21PwrlowPortn": pmopm8CfgChannel21PwrlowPortn,
       "pmopm8CfgChannel22PwrlowPortn": pmopm8CfgChannel22PwrlowPortn,
       "pmopm8CfgChannel23PwrlowPortn": pmopm8CfgChannel23PwrlowPortn,
       "pmopm8CfgChannel24PwrlowPortn": pmopm8CfgChannel24PwrlowPortn,
       "pmopm8CfgChannel25PwrlowPortn": pmopm8CfgChannel25PwrlowPortn,
       "pmopm8CfgChannel26PwrlowPortn": pmopm8CfgChannel26PwrlowPortn,
       "pmopm8CfgChannel27PwrlowPortn": pmopm8CfgChannel27PwrlowPortn,
       "pmopm8CfgChannel28PwrlowPortn": pmopm8CfgChannel28PwrlowPortn,
       "pmopm8CfgChannel29PwrlowPortn": pmopm8CfgChannel29PwrlowPortn,
       "pmopm8CfgChannel30PwrlowPortn": pmopm8CfgChannel30PwrlowPortn,
       "pmopm8CfgChannel31PwrlowPortn": pmopm8CfgChannel31PwrlowPortn,
       "pmopm8CfgChannel32PwrlowPortn": pmopm8CfgChannel32PwrlowPortn,
       "pmopm8CfgChannel33PwrlowPortn": pmopm8CfgChannel33PwrlowPortn,
       "pmopm8CfgChannel34PwrlowPortn": pmopm8CfgChannel34PwrlowPortn,
       "pmopm8CfgChannel35PwrlowPortn": pmopm8CfgChannel35PwrlowPortn,
       "pmopm8CfgChannel36PwrlowPortn": pmopm8CfgChannel36PwrlowPortn,
       "pmopm8CfgChannel37PwrlowPortn": pmopm8CfgChannel37PwrlowPortn,
       "pmopm8CfgChannel38PwrlowPortn": pmopm8CfgChannel38PwrlowPortn,
       "pmopm8CfgChannel39PwrlowPortn": pmopm8CfgChannel39PwrlowPortn,
       "pmopm8CfgChannel40PwrlowPortn": pmopm8CfgChannel40PwrlowPortn,
       "pmopm8CfgChannel41PwrlowPortn": pmopm8CfgChannel41PwrlowPortn,
       "pmopm8CfgChannel42PwrlowPortn": pmopm8CfgChannel42PwrlowPortn,
       "pmopm8CfgChannel43PwrlowPortn": pmopm8CfgChannel43PwrlowPortn,
       "pmopm8CfgChannel44PwrlowPortn": pmopm8CfgChannel44PwrlowPortn,
       "pmopm8CfgChannel45PwrlowPortn": pmopm8CfgChannel45PwrlowPortn,
       "pmopm8CfgChannel46PwrlowPortn": pmopm8CfgChannel46PwrlowPortn,
       "pmopm8CfgChannel47PwrlowPortn": pmopm8CfgChannel47PwrlowPortn,
       "pmopm8CfgChannel48PwrlowPortn": pmopm8CfgChannel48PwrlowPortn,
       "pmopm8CfgChannel49PwrlowPortn": pmopm8CfgChannel49PwrlowPortn,
       "pmopm8CfgChannel50PwrlowPortn": pmopm8CfgChannel50PwrlowPortn,
       "pmopm8CfgChannel51PwrlowPortn": pmopm8CfgChannel51PwrlowPortn,
       "pmopm8CfgChannel52PwrlowPortn": pmopm8CfgChannel52PwrlowPortn,
       "pmopm8CfgChannel53PwrlowPortn": pmopm8CfgChannel53PwrlowPortn,
       "pmopm8CfgChannel54PwrlowPortn": pmopm8CfgChannel54PwrlowPortn,
       "pmopm8CfgChannel55PwrlowPortn": pmopm8CfgChannel55PwrlowPortn,
       "pmopm8CfgChannel56PwrlowPortn": pmopm8CfgChannel56PwrlowPortn,
       "pmopm8CfgChannel57PwrlowPortn": pmopm8CfgChannel57PwrlowPortn,
       "pmopm8CfgChannel58PwrlowPortn": pmopm8CfgChannel58PwrlowPortn,
       "pmopm8CfgChannel59PwrlowPortn": pmopm8CfgChannel59PwrlowPortn,
       "pmopm8CfgChannel60PwrlowPortn": pmopm8CfgChannel60PwrlowPortn,
       "pmopm8CfgChannel61PwrlowPortn": pmopm8CfgChannel61PwrlowPortn,
       "pmopm8CfgChannel62PwrlowPortn": pmopm8CfgChannel62PwrlowPortn,
       "pmopm8CfgChannel63PwrlowPortn": pmopm8CfgChannel63PwrlowPortn,
       "pmopm8CfgChannel64PwrlowPortn": pmopm8CfgChannel64PwrlowPortn,
       "pmopm8CfgChannel65PwrlowPortn": pmopm8CfgChannel65PwrlowPortn,
       "pmopm8CfgChannel66PwrlowPortn": pmopm8CfgChannel66PwrlowPortn,
       "pmopm8CfgChannel67PwrlowPortn": pmopm8CfgChannel67PwrlowPortn,
       "pmopm8CfgChannel68PwrlowPortn": pmopm8CfgChannel68PwrlowPortn,
       "pmopm8CfgChannel69PwrlowPortn": pmopm8CfgChannel69PwrlowPortn,
       "pmopm8CfgChannel70PwrlowPortn": pmopm8CfgChannel70PwrlowPortn,
       "pmopm8CfgChannel71PwrlowPortn": pmopm8CfgChannel71PwrlowPortn,
       "pmopm8CfgChannel72PwrlowPortn": pmopm8CfgChannel72PwrlowPortn,
       "pmopm8CfgChannel73PwrlowPortn": pmopm8CfgChannel73PwrlowPortn,
       "pmopm8CfgChannel74PwrlowPortn": pmopm8CfgChannel74PwrlowPortn,
       "pmopm8CfgChannel75PwrlowPortn": pmopm8CfgChannel75PwrlowPortn,
       "pmopm8CfgChannel76PwrlowPortn": pmopm8CfgChannel76PwrlowPortn,
       "pmopm8CfgChannel77PwrlowPortn": pmopm8CfgChannel77PwrlowPortn,
       "pmopm8CfgChannel78PwrlowPortn": pmopm8CfgChannel78PwrlowPortn,
       "pmopm8CfgChannel79PwrlowPortn": pmopm8CfgChannel79PwrlowPortn,
       "pmopm8CfgChannel80PwrlowPortn": pmopm8CfgChannel80PwrlowPortn,
       "pmopm8CfgChannel81PwrlowPortn": pmopm8CfgChannel81PwrlowPortn,
       "pmopm8CfgChannel82PwrlowPortn": pmopm8CfgChannel82PwrlowPortn,
       "pmopm8CfgChannel83PwrlowPortn": pmopm8CfgChannel83PwrlowPortn,
       "pmopm8CfgChannel84PwrlowPortn": pmopm8CfgChannel84PwrlowPortn,
       "pmopm8CfgChannel85PwrlowPortn": pmopm8CfgChannel85PwrlowPortn,
       "pmopm8CfgChannel86PwrlowPortn": pmopm8CfgChannel86PwrlowPortn,
       "pmopm8CfgChannel87PwrlowPortn": pmopm8CfgChannel87PwrlowPortn,
       "pmopm8CfgChannel88PwrlowPortn": pmopm8CfgChannel88PwrlowPortn,
       "pmopm8CfgChannel89PwrlowPortn": pmopm8CfgChannel89PwrlowPortn,
       "pmopm8CfgChannel90PwrlowPortn": pmopm8CfgChannel90PwrlowPortn,
       "pmopm8CfgChannel91PwrlowPortn": pmopm8CfgChannel91PwrlowPortn,
       "pmopm8CfgChannel92PwrlowPortn": pmopm8CfgChannel92PwrlowPortn,
       "pmopm8CfgChannel93PwrlowPortn": pmopm8CfgChannel93PwrlowPortn,
       "pmopm8CfgChannel94PwrlowPortn": pmopm8CfgChannel94PwrlowPortn,
       "pmopm8CfgChannel95PwrlowPortn": pmopm8CfgChannel95PwrlowPortn,
       "pmopm8CfgChannel96PwrlowPortn": pmopm8CfgChannel96PwrlowPortn,
       "pmopm8CfgLabelclientTable": pmopm8CfgLabelclientTable,
       "pmopm8CfgLabelclientEntry": pmopm8CfgLabelclientEntry,
       "pmopm8CfgLabelclientIndex": pmopm8CfgLabelclientIndex,
       "pmopm8CfgLabelclientPortn": pmopm8CfgLabelclientPortn,
       "pmopm8CfgLabellineTable": pmopm8CfgLabellineTable,
       "pmopm8CfgLabellineEntry": pmopm8CfgLabellineEntry,
       "pmopm8CfgLabellineIndex": pmopm8CfgLabellineIndex,
       "pmopm8CfgLabellinePortn": pmopm8CfgLabellinePortn,
       "pmopm8CfgWriteConfiguration": pmopm8CfgWriteConfiguration,
       "pmopm8traps": pmopm8traps,
       "pmopm8trapPortNumber": pmopm8trapPortNumber,
       "pmopm8trapLineNumber": pmopm8trapLineNumber,
       "pmopm8trapBoardNumber": pmopm8trapBoardNumber,
       "pmopm8PowerTrapUrgentGoesOn": pmopm8PowerTrapUrgentGoesOn,
       "pmopm8PowerTrapUrgentGoesOff": pmopm8PowerTrapUrgentGoesOff}
)
