# SNMP MIB module (EKINOPS-Pmopm2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmopm2-MIB.mib
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

modulePmopm2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64)
)
if mibBuilder.loadTexts:
    modulePmopm2.setRevisions(
        ("2004-12-20 00:00",
         "2016-05-23 00:00",
         "2016-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmopm2Grid(TextualConvention, Integer32):
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



class Pmopm2MultiRate(TextualConvention, Integer32):
    status = "current"


class Pmopm2OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pmopm2AdjustValue(TextualConvention, Integer32):
    status = "current"


class Pmopm2OtxMode(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pmopm2alarms_ObjectIdentity = ObjectIdentity
pmopm2alarms = _Pmopm2alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2)
)
_Pmopm2AlmOther_ObjectIdentity = ObjectIdentity
pmopm2AlmOther = _Pmopm2AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1)
)
_Pmopm2AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmopm2AlmOtherNurg = _Pmopm2AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 1)
)
_Pmopm2AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmopm2AlmsynthAlm2 = _Pmopm2AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 1, 2)
)
_Pmopm2AlmConfTableSave_Type = EkiOnOff
_Pmopm2AlmConfTableSave_Object = MibScalar
pmopm2AlmConfTableSave = _Pmopm2AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 1, 2, 1),
    _Pmopm2AlmConfTableSave_Type()
)
pmopm2AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmConfTableSave.setStatus("current")
_Pmopm2AlmInvUpload_Type = EkiOnOff
_Pmopm2AlmInvUpload_Object = MibScalar
pmopm2AlmInvUpload = _Pmopm2AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 1, 2, 2),
    _Pmopm2AlmInvUpload_Type()
)
pmopm2AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmInvUpload.setStatus("current")
_Pmopm2AlmConfTableLoad_Type = EkiOnOff
_Pmopm2AlmConfTableLoad_Object = MibScalar
pmopm2AlmConfTableLoad = _Pmopm2AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 1, 2, 3),
    _Pmopm2AlmConfTableLoad_Type()
)
pmopm2AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmConfTableLoad.setStatus("current")
_Pmopm2AlmCorrelatOff_Type = EkiOnOff
_Pmopm2AlmCorrelatOff_Object = MibScalar
pmopm2AlmCorrelatOff = _Pmopm2AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 1, 2, 4),
    _Pmopm2AlmCorrelatOff_Type()
)
pmopm2AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmCorrelatOff.setStatus("current")
_Pmopm2AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmopm2AlmOtherUrg = _Pmopm2AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 2)
)
_Pmopm2AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmopm2AlmOtherCrit = _Pmopm2AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 3)
)
_Pmopm2AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmopm2AlmsynthAlm0 = _Pmopm2AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 3, 0)
)
_Pmopm2AlmModGlobFail_Type = EkiOnOff
_Pmopm2AlmModGlobFail_Object = MibScalar
pmopm2AlmModGlobFail = _Pmopm2AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 3, 0, 9),
    _Pmopm2AlmModGlobFail_Type()
)
pmopm2AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmModGlobFail.setStatus("current")
_Pmopm2AlmDefFuseA_Type = EkiOnOff
_Pmopm2AlmDefFuseA_Object = MibScalar
pmopm2AlmDefFuseA = _Pmopm2AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 3, 0, 15),
    _Pmopm2AlmDefFuseA_Type()
)
pmopm2AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmDefFuseA.setStatus("current")
_Pmopm2AlmDefFuseB_Type = EkiOnOff
_Pmopm2AlmDefFuseB_Object = MibScalar
pmopm2AlmDefFuseB = _Pmopm2AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 1, 3, 0, 16),
    _Pmopm2AlmDefFuseB_Type()
)
pmopm2AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmDefFuseB.setStatus("current")
_Pmopm2AlmClient_ObjectIdentity = ObjectIdentity
pmopm2AlmClient = _Pmopm2AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2)
)
_Pmopm2AlmClientNurg_ObjectIdentity = ObjectIdentity
pmopm2AlmClientNurg = _Pmopm2AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 1)
)
_Pmopm2AlmClientUrg_ObjectIdentity = ObjectIdentity
pmopm2AlmClientUrg = _Pmopm2AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 2)
)
_Pmopm2AlmClientCrit_ObjectIdentity = ObjectIdentity
pmopm2AlmClientCrit = _Pmopm2AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3)
)
_Pmopm2AlmsynthAlmPortTable_Object = MibTable
pmopm2AlmsynthAlmPortTable = _Pmopm2AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmopm2AlmsynthAlmPortTable.setStatus("current")
_Pmopm2AlmsynthAlmPortEntry_Object = MibTableRow
pmopm2AlmsynthAlmPortEntry = _Pmopm2AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 8, 1)
)
pmopm2AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2AlmsynthAlmPortEntry.setStatus("current")


class _Pmopm2AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pmopm2AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pmopm2AlmsynthAlmPortIndex_Object = MibTableColumn
pmopm2AlmsynthAlmPortIndex = _Pmopm2AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 8, 1, 1),
    _Pmopm2AlmsynthAlmPortIndex_Type()
)
pmopm2AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmsynthAlmPortIndex.setStatus("current")
_Pmopm2AlmSpectrumAbsentPortn_Type = EkiOnOff
_Pmopm2AlmSpectrumAbsentPortn_Object = MibTableColumn
pmopm2AlmSpectrumAbsentPortn = _Pmopm2AlmSpectrumAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 8, 1, 2),
    _Pmopm2AlmSpectrumAbsentPortn_Type()
)
pmopm2AlmSpectrumAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmSpectrumAbsentPortn.setStatus("current")
_Pmopm2Almchannel1PortTable_Object = MibTable
pmopm2Almchannel1PortTable = _Pmopm2Almchannel1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel1PortTable.setStatus("current")
_Pmopm2Almchannel1PortEntry_Object = MibTableRow
pmopm2Almchannel1PortEntry = _Pmopm2Almchannel1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1)
)
pmopm2Almchannel1PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel1PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel1PortEntry.setStatus("current")


class _Pmopm2Almchannel1PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel1PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel1PortIndex_Object = MibTableColumn
pmopm2Almchannel1PortIndex = _Pmopm2Almchannel1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1, 1),
    _Pmopm2Almchannel1PortIndex_Type()
)
pmopm2Almchannel1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel1PortIndex.setStatus("current")
_Pmopm2AlmChannel1AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel1AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel1AbsentPortn = _Pmopm2AlmChannel1AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1, 2),
    _Pmopm2AlmChannel1AbsentPortn_Type()
)
pmopm2AlmChannel1AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel1AbsentPortn.setStatus("current")
_Pmopm2AlmChannel1MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel1MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel1MismatchPortn = _Pmopm2AlmChannel1MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1, 3),
    _Pmopm2AlmChannel1MismatchPortn_Type()
)
pmopm2AlmChannel1MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel1MismatchPortn.setStatus("current")
_Pmopm2AlmChannel1BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel1BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel1BalancedPortn = _Pmopm2AlmChannel1BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1, 4),
    _Pmopm2AlmChannel1BalancedPortn_Type()
)
pmopm2AlmChannel1BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel1BalancedPortn.setStatus("current")
_Pmopm2AlmChannel1PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel1PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel1PowerLowPortn = _Pmopm2AlmChannel1PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1, 5),
    _Pmopm2AlmChannel1PowerLowPortn_Type()
)
pmopm2AlmChannel1PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel1PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel1PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel1PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel1PowerHighPortn = _Pmopm2AlmChannel1PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1, 6),
    _Pmopm2AlmChannel1PowerHighPortn_Type()
)
pmopm2AlmChannel1PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel1PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel1OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel1OosPortn_Object = MibTableColumn
pmopm2AlmChannel1OosPortn = _Pmopm2AlmChannel1OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 16, 1, 7),
    _Pmopm2AlmChannel1OosPortn_Type()
)
pmopm2AlmChannel1OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel1OosPortn.setStatus("current")
_Pmopm2Almchannel2PortTable_Object = MibTable
pmopm2Almchannel2PortTable = _Pmopm2Almchannel2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel2PortTable.setStatus("current")
_Pmopm2Almchannel2PortEntry_Object = MibTableRow
pmopm2Almchannel2PortEntry = _Pmopm2Almchannel2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1)
)
pmopm2Almchannel2PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel2PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel2PortEntry.setStatus("current")


class _Pmopm2Almchannel2PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel2PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel2PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel2PortIndex_Object = MibTableColumn
pmopm2Almchannel2PortIndex = _Pmopm2Almchannel2PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1, 1),
    _Pmopm2Almchannel2PortIndex_Type()
)
pmopm2Almchannel2PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel2PortIndex.setStatus("current")
_Pmopm2AlmChannel2AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel2AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel2AbsentPortn = _Pmopm2AlmChannel2AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1, 2),
    _Pmopm2AlmChannel2AbsentPortn_Type()
)
pmopm2AlmChannel2AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel2AbsentPortn.setStatus("current")
_Pmopm2AlmChannel2MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel2MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel2MismatchPortn = _Pmopm2AlmChannel2MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1, 3),
    _Pmopm2AlmChannel2MismatchPortn_Type()
)
pmopm2AlmChannel2MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel2MismatchPortn.setStatus("current")
_Pmopm2AlmChannel2BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel2BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel2BalancedPortn = _Pmopm2AlmChannel2BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1, 4),
    _Pmopm2AlmChannel2BalancedPortn_Type()
)
pmopm2AlmChannel2BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel2BalancedPortn.setStatus("current")
_Pmopm2AlmChannel2PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel2PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel2PowerLowPortn = _Pmopm2AlmChannel2PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1, 5),
    _Pmopm2AlmChannel2PowerLowPortn_Type()
)
pmopm2AlmChannel2PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel2PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel2PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel2PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel2PowerHighPortn = _Pmopm2AlmChannel2PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1, 6),
    _Pmopm2AlmChannel2PowerHighPortn_Type()
)
pmopm2AlmChannel2PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel2PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel2OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel2OosPortn_Object = MibTableColumn
pmopm2AlmChannel2OosPortn = _Pmopm2AlmChannel2OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 18, 1, 7),
    _Pmopm2AlmChannel2OosPortn_Type()
)
pmopm2AlmChannel2OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel2OosPortn.setStatus("current")
_Pmopm2Almchannel3PortTable_Object = MibTable
pmopm2Almchannel3PortTable = _Pmopm2Almchannel3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel3PortTable.setStatus("current")
_Pmopm2Almchannel3PortEntry_Object = MibTableRow
pmopm2Almchannel3PortEntry = _Pmopm2Almchannel3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1)
)
pmopm2Almchannel3PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel3PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel3PortEntry.setStatus("current")


class _Pmopm2Almchannel3PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel3PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel3PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel3PortIndex_Object = MibTableColumn
pmopm2Almchannel3PortIndex = _Pmopm2Almchannel3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1, 1),
    _Pmopm2Almchannel3PortIndex_Type()
)
pmopm2Almchannel3PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel3PortIndex.setStatus("current")
_Pmopm2AlmChannel3AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel3AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel3AbsentPortn = _Pmopm2AlmChannel3AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1, 2),
    _Pmopm2AlmChannel3AbsentPortn_Type()
)
pmopm2AlmChannel3AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel3AbsentPortn.setStatus("current")
_Pmopm2AlmChannel3MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel3MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel3MismatchPortn = _Pmopm2AlmChannel3MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1, 3),
    _Pmopm2AlmChannel3MismatchPortn_Type()
)
pmopm2AlmChannel3MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel3MismatchPortn.setStatus("current")
_Pmopm2AlmChannel3BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel3BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel3BalancedPortn = _Pmopm2AlmChannel3BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1, 4),
    _Pmopm2AlmChannel3BalancedPortn_Type()
)
pmopm2AlmChannel3BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel3BalancedPortn.setStatus("current")
_Pmopm2AlmChannel3PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel3PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel3PowerLowPortn = _Pmopm2AlmChannel3PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1, 5),
    _Pmopm2AlmChannel3PowerLowPortn_Type()
)
pmopm2AlmChannel3PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel3PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel3PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel3PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel3PowerHighPortn = _Pmopm2AlmChannel3PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1, 6),
    _Pmopm2AlmChannel3PowerHighPortn_Type()
)
pmopm2AlmChannel3PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel3PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel3OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel3OosPortn_Object = MibTableColumn
pmopm2AlmChannel3OosPortn = _Pmopm2AlmChannel3OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 20, 1, 7),
    _Pmopm2AlmChannel3OosPortn_Type()
)
pmopm2AlmChannel3OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel3OosPortn.setStatus("current")
_Pmopm2Almchannel4PortTable_Object = MibTable
pmopm2Almchannel4PortTable = _Pmopm2Almchannel4PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel4PortTable.setStatus("current")
_Pmopm2Almchannel4PortEntry_Object = MibTableRow
pmopm2Almchannel4PortEntry = _Pmopm2Almchannel4PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1)
)
pmopm2Almchannel4PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel4PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel4PortEntry.setStatus("current")


class _Pmopm2Almchannel4PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel4PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel4PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel4PortIndex_Object = MibTableColumn
pmopm2Almchannel4PortIndex = _Pmopm2Almchannel4PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1, 1),
    _Pmopm2Almchannel4PortIndex_Type()
)
pmopm2Almchannel4PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel4PortIndex.setStatus("current")
_Pmopm2AlmChannel4AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel4AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel4AbsentPortn = _Pmopm2AlmChannel4AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1, 2),
    _Pmopm2AlmChannel4AbsentPortn_Type()
)
pmopm2AlmChannel4AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel4AbsentPortn.setStatus("current")
_Pmopm2AlmChannel4MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel4MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel4MismatchPortn = _Pmopm2AlmChannel4MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1, 3),
    _Pmopm2AlmChannel4MismatchPortn_Type()
)
pmopm2AlmChannel4MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel4MismatchPortn.setStatus("current")
_Pmopm2AlmChannel4BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel4BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel4BalancedPortn = _Pmopm2AlmChannel4BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1, 4),
    _Pmopm2AlmChannel4BalancedPortn_Type()
)
pmopm2AlmChannel4BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel4BalancedPortn.setStatus("current")
_Pmopm2AlmChannel4PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel4PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel4PowerLowPortn = _Pmopm2AlmChannel4PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1, 5),
    _Pmopm2AlmChannel4PowerLowPortn_Type()
)
pmopm2AlmChannel4PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel4PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel4PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel4PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel4PowerHighPortn = _Pmopm2AlmChannel4PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1, 6),
    _Pmopm2AlmChannel4PowerHighPortn_Type()
)
pmopm2AlmChannel4PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel4PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel4OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel4OosPortn_Object = MibTableColumn
pmopm2AlmChannel4OosPortn = _Pmopm2AlmChannel4OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 22, 1, 7),
    _Pmopm2AlmChannel4OosPortn_Type()
)
pmopm2AlmChannel4OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel4OosPortn.setStatus("current")
_Pmopm2Almchannel5PortTable_Object = MibTable
pmopm2Almchannel5PortTable = _Pmopm2Almchannel5PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel5PortTable.setStatus("current")
_Pmopm2Almchannel5PortEntry_Object = MibTableRow
pmopm2Almchannel5PortEntry = _Pmopm2Almchannel5PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1)
)
pmopm2Almchannel5PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel5PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel5PortEntry.setStatus("current")


class _Pmopm2Almchannel5PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel5PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel5PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel5PortIndex_Object = MibTableColumn
pmopm2Almchannel5PortIndex = _Pmopm2Almchannel5PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1, 1),
    _Pmopm2Almchannel5PortIndex_Type()
)
pmopm2Almchannel5PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel5PortIndex.setStatus("current")
_Pmopm2AlmChannel5AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel5AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel5AbsentPortn = _Pmopm2AlmChannel5AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1, 2),
    _Pmopm2AlmChannel5AbsentPortn_Type()
)
pmopm2AlmChannel5AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel5AbsentPortn.setStatus("current")
_Pmopm2AlmChannel5MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel5MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel5MismatchPortn = _Pmopm2AlmChannel5MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1, 3),
    _Pmopm2AlmChannel5MismatchPortn_Type()
)
pmopm2AlmChannel5MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel5MismatchPortn.setStatus("current")
_Pmopm2AlmChannel5BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel5BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel5BalancedPortn = _Pmopm2AlmChannel5BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1, 4),
    _Pmopm2AlmChannel5BalancedPortn_Type()
)
pmopm2AlmChannel5BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel5BalancedPortn.setStatus("current")
_Pmopm2AlmChannel5PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel5PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel5PowerLowPortn = _Pmopm2AlmChannel5PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1, 5),
    _Pmopm2AlmChannel5PowerLowPortn_Type()
)
pmopm2AlmChannel5PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel5PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel5PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel5PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel5PowerHighPortn = _Pmopm2AlmChannel5PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1, 6),
    _Pmopm2AlmChannel5PowerHighPortn_Type()
)
pmopm2AlmChannel5PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel5PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel5OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel5OosPortn_Object = MibTableColumn
pmopm2AlmChannel5OosPortn = _Pmopm2AlmChannel5OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 24, 1, 7),
    _Pmopm2AlmChannel5OosPortn_Type()
)
pmopm2AlmChannel5OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel5OosPortn.setStatus("current")
_Pmopm2Almchannel6PortTable_Object = MibTable
pmopm2Almchannel6PortTable = _Pmopm2Almchannel6PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel6PortTable.setStatus("current")
_Pmopm2Almchannel6PortEntry_Object = MibTableRow
pmopm2Almchannel6PortEntry = _Pmopm2Almchannel6PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1)
)
pmopm2Almchannel6PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel6PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel6PortEntry.setStatus("current")


class _Pmopm2Almchannel6PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel6PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel6PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel6PortIndex_Object = MibTableColumn
pmopm2Almchannel6PortIndex = _Pmopm2Almchannel6PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1, 1),
    _Pmopm2Almchannel6PortIndex_Type()
)
pmopm2Almchannel6PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel6PortIndex.setStatus("current")
_Pmopm2AlmChannel6AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel6AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel6AbsentPortn = _Pmopm2AlmChannel6AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1, 2),
    _Pmopm2AlmChannel6AbsentPortn_Type()
)
pmopm2AlmChannel6AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel6AbsentPortn.setStatus("current")
_Pmopm2AlmChannel6MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel6MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel6MismatchPortn = _Pmopm2AlmChannel6MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1, 3),
    _Pmopm2AlmChannel6MismatchPortn_Type()
)
pmopm2AlmChannel6MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel6MismatchPortn.setStatus("current")
_Pmopm2AlmChannel6BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel6BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel6BalancedPortn = _Pmopm2AlmChannel6BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1, 4),
    _Pmopm2AlmChannel6BalancedPortn_Type()
)
pmopm2AlmChannel6BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel6BalancedPortn.setStatus("current")
_Pmopm2AlmChannel6PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel6PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel6PowerLowPortn = _Pmopm2AlmChannel6PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1, 5),
    _Pmopm2AlmChannel6PowerLowPortn_Type()
)
pmopm2AlmChannel6PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel6PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel6PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel6PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel6PowerHighPortn = _Pmopm2AlmChannel6PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1, 6),
    _Pmopm2AlmChannel6PowerHighPortn_Type()
)
pmopm2AlmChannel6PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel6PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel6OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel6OosPortn_Object = MibTableColumn
pmopm2AlmChannel6OosPortn = _Pmopm2AlmChannel6OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 26, 1, 7),
    _Pmopm2AlmChannel6OosPortn_Type()
)
pmopm2AlmChannel6OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel6OosPortn.setStatus("current")
_Pmopm2Almchannel7PortTable_Object = MibTable
pmopm2Almchannel7PortTable = _Pmopm2Almchannel7PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel7PortTable.setStatus("current")
_Pmopm2Almchannel7PortEntry_Object = MibTableRow
pmopm2Almchannel7PortEntry = _Pmopm2Almchannel7PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1)
)
pmopm2Almchannel7PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel7PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel7PortEntry.setStatus("current")


class _Pmopm2Almchannel7PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel7PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel7PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel7PortIndex_Object = MibTableColumn
pmopm2Almchannel7PortIndex = _Pmopm2Almchannel7PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1, 1),
    _Pmopm2Almchannel7PortIndex_Type()
)
pmopm2Almchannel7PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel7PortIndex.setStatus("current")
_Pmopm2AlmChannel7AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel7AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel7AbsentPortn = _Pmopm2AlmChannel7AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1, 2),
    _Pmopm2AlmChannel7AbsentPortn_Type()
)
pmopm2AlmChannel7AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel7AbsentPortn.setStatus("current")
_Pmopm2AlmChannel7MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel7MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel7MismatchPortn = _Pmopm2AlmChannel7MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1, 3),
    _Pmopm2AlmChannel7MismatchPortn_Type()
)
pmopm2AlmChannel7MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel7MismatchPortn.setStatus("current")
_Pmopm2AlmChannel7BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel7BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel7BalancedPortn = _Pmopm2AlmChannel7BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1, 4),
    _Pmopm2AlmChannel7BalancedPortn_Type()
)
pmopm2AlmChannel7BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel7BalancedPortn.setStatus("current")
_Pmopm2AlmChannel7PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel7PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel7PowerLowPortn = _Pmopm2AlmChannel7PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1, 5),
    _Pmopm2AlmChannel7PowerLowPortn_Type()
)
pmopm2AlmChannel7PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel7PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel7PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel7PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel7PowerHighPortn = _Pmopm2AlmChannel7PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1, 6),
    _Pmopm2AlmChannel7PowerHighPortn_Type()
)
pmopm2AlmChannel7PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel7PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel7OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel7OosPortn_Object = MibTableColumn
pmopm2AlmChannel7OosPortn = _Pmopm2AlmChannel7OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 28, 1, 7),
    _Pmopm2AlmChannel7OosPortn_Type()
)
pmopm2AlmChannel7OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel7OosPortn.setStatus("current")
_Pmopm2Almchannel8PortTable_Object = MibTable
pmopm2Almchannel8PortTable = _Pmopm2Almchannel8PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel8PortTable.setStatus("current")
_Pmopm2Almchannel8PortEntry_Object = MibTableRow
pmopm2Almchannel8PortEntry = _Pmopm2Almchannel8PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1)
)
pmopm2Almchannel8PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel8PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel8PortEntry.setStatus("current")


class _Pmopm2Almchannel8PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel8PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel8PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel8PortIndex_Object = MibTableColumn
pmopm2Almchannel8PortIndex = _Pmopm2Almchannel8PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1, 1),
    _Pmopm2Almchannel8PortIndex_Type()
)
pmopm2Almchannel8PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel8PortIndex.setStatus("current")
_Pmopm2AlmChannel8AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel8AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel8AbsentPortn = _Pmopm2AlmChannel8AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1, 2),
    _Pmopm2AlmChannel8AbsentPortn_Type()
)
pmopm2AlmChannel8AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel8AbsentPortn.setStatus("current")
_Pmopm2AlmChannel8MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel8MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel8MismatchPortn = _Pmopm2AlmChannel8MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1, 3),
    _Pmopm2AlmChannel8MismatchPortn_Type()
)
pmopm2AlmChannel8MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel8MismatchPortn.setStatus("current")
_Pmopm2AlmChannel8BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel8BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel8BalancedPortn = _Pmopm2AlmChannel8BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1, 4),
    _Pmopm2AlmChannel8BalancedPortn_Type()
)
pmopm2AlmChannel8BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel8BalancedPortn.setStatus("current")
_Pmopm2AlmChannel8PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel8PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel8PowerLowPortn = _Pmopm2AlmChannel8PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1, 5),
    _Pmopm2AlmChannel8PowerLowPortn_Type()
)
pmopm2AlmChannel8PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel8PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel8PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel8PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel8PowerHighPortn = _Pmopm2AlmChannel8PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1, 6),
    _Pmopm2AlmChannel8PowerHighPortn_Type()
)
pmopm2AlmChannel8PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel8PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel8OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel8OosPortn_Object = MibTableColumn
pmopm2AlmChannel8OosPortn = _Pmopm2AlmChannel8OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 30, 1, 7),
    _Pmopm2AlmChannel8OosPortn_Type()
)
pmopm2AlmChannel8OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel8OosPortn.setStatus("current")
_Pmopm2Almchannel9PortTable_Object = MibTable
pmopm2Almchannel9PortTable = _Pmopm2Almchannel9PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel9PortTable.setStatus("current")
_Pmopm2Almchannel9PortEntry_Object = MibTableRow
pmopm2Almchannel9PortEntry = _Pmopm2Almchannel9PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1)
)
pmopm2Almchannel9PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel9PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel9PortEntry.setStatus("current")


class _Pmopm2Almchannel9PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel9PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel9PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel9PortIndex_Object = MibTableColumn
pmopm2Almchannel9PortIndex = _Pmopm2Almchannel9PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1, 1),
    _Pmopm2Almchannel9PortIndex_Type()
)
pmopm2Almchannel9PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel9PortIndex.setStatus("current")
_Pmopm2AlmChannel9AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel9AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel9AbsentPortn = _Pmopm2AlmChannel9AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1, 2),
    _Pmopm2AlmChannel9AbsentPortn_Type()
)
pmopm2AlmChannel9AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel9AbsentPortn.setStatus("current")
_Pmopm2AlmChannel9MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel9MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel9MismatchPortn = _Pmopm2AlmChannel9MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1, 3),
    _Pmopm2AlmChannel9MismatchPortn_Type()
)
pmopm2AlmChannel9MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel9MismatchPortn.setStatus("current")
_Pmopm2AlmChannel9BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel9BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel9BalancedPortn = _Pmopm2AlmChannel9BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1, 4),
    _Pmopm2AlmChannel9BalancedPortn_Type()
)
pmopm2AlmChannel9BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel9BalancedPortn.setStatus("current")
_Pmopm2AlmChannel9PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel9PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel9PowerLowPortn = _Pmopm2AlmChannel9PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1, 5),
    _Pmopm2AlmChannel9PowerLowPortn_Type()
)
pmopm2AlmChannel9PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel9PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel9PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel9PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel9PowerHighPortn = _Pmopm2AlmChannel9PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1, 6),
    _Pmopm2AlmChannel9PowerHighPortn_Type()
)
pmopm2AlmChannel9PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel9PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel9OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel9OosPortn_Object = MibTableColumn
pmopm2AlmChannel9OosPortn = _Pmopm2AlmChannel9OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 32, 1, 7),
    _Pmopm2AlmChannel9OosPortn_Type()
)
pmopm2AlmChannel9OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel9OosPortn.setStatus("current")
_Pmopm2Almchannel10PortTable_Object = MibTable
pmopm2Almchannel10PortTable = _Pmopm2Almchannel10PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel10PortTable.setStatus("current")
_Pmopm2Almchannel10PortEntry_Object = MibTableRow
pmopm2Almchannel10PortEntry = _Pmopm2Almchannel10PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1)
)
pmopm2Almchannel10PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel10PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel10PortEntry.setStatus("current")


class _Pmopm2Almchannel10PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel10PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel10PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel10PortIndex_Object = MibTableColumn
pmopm2Almchannel10PortIndex = _Pmopm2Almchannel10PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1, 1),
    _Pmopm2Almchannel10PortIndex_Type()
)
pmopm2Almchannel10PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel10PortIndex.setStatus("current")
_Pmopm2AlmChannel10AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel10AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel10AbsentPortn = _Pmopm2AlmChannel10AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1, 2),
    _Pmopm2AlmChannel10AbsentPortn_Type()
)
pmopm2AlmChannel10AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel10AbsentPortn.setStatus("current")
_Pmopm2AlmChannel10MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel10MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel10MismatchPortn = _Pmopm2AlmChannel10MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1, 3),
    _Pmopm2AlmChannel10MismatchPortn_Type()
)
pmopm2AlmChannel10MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel10MismatchPortn.setStatus("current")
_Pmopm2AlmChannel10BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel10BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel10BalancedPortn = _Pmopm2AlmChannel10BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1, 4),
    _Pmopm2AlmChannel10BalancedPortn_Type()
)
pmopm2AlmChannel10BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel10BalancedPortn.setStatus("current")
_Pmopm2AlmChannel10PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel10PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel10PowerLowPortn = _Pmopm2AlmChannel10PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1, 5),
    _Pmopm2AlmChannel10PowerLowPortn_Type()
)
pmopm2AlmChannel10PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel10PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel10PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel10PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel10PowerHighPortn = _Pmopm2AlmChannel10PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1, 6),
    _Pmopm2AlmChannel10PowerHighPortn_Type()
)
pmopm2AlmChannel10PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel10PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel10OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel10OosPortn_Object = MibTableColumn
pmopm2AlmChannel10OosPortn = _Pmopm2AlmChannel10OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 34, 1, 7),
    _Pmopm2AlmChannel10OosPortn_Type()
)
pmopm2AlmChannel10OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel10OosPortn.setStatus("current")
_Pmopm2Almchannel11PortTable_Object = MibTable
pmopm2Almchannel11PortTable = _Pmopm2Almchannel11PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel11PortTable.setStatus("current")
_Pmopm2Almchannel11PortEntry_Object = MibTableRow
pmopm2Almchannel11PortEntry = _Pmopm2Almchannel11PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1)
)
pmopm2Almchannel11PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel11PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel11PortEntry.setStatus("current")


class _Pmopm2Almchannel11PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel11PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel11PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel11PortIndex_Object = MibTableColumn
pmopm2Almchannel11PortIndex = _Pmopm2Almchannel11PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1, 1),
    _Pmopm2Almchannel11PortIndex_Type()
)
pmopm2Almchannel11PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel11PortIndex.setStatus("current")
_Pmopm2AlmChannel11AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel11AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel11AbsentPortn = _Pmopm2AlmChannel11AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1, 2),
    _Pmopm2AlmChannel11AbsentPortn_Type()
)
pmopm2AlmChannel11AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel11AbsentPortn.setStatus("current")
_Pmopm2AlmChannel11MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel11MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel11MismatchPortn = _Pmopm2AlmChannel11MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1, 3),
    _Pmopm2AlmChannel11MismatchPortn_Type()
)
pmopm2AlmChannel11MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel11MismatchPortn.setStatus("current")
_Pmopm2AlmChannel11BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel11BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel11BalancedPortn = _Pmopm2AlmChannel11BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1, 4),
    _Pmopm2AlmChannel11BalancedPortn_Type()
)
pmopm2AlmChannel11BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel11BalancedPortn.setStatus("current")
_Pmopm2AlmChannel11PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel11PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel11PowerLowPortn = _Pmopm2AlmChannel11PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1, 5),
    _Pmopm2AlmChannel11PowerLowPortn_Type()
)
pmopm2AlmChannel11PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel11PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel11PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel11PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel11PowerHighPortn = _Pmopm2AlmChannel11PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1, 6),
    _Pmopm2AlmChannel11PowerHighPortn_Type()
)
pmopm2AlmChannel11PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel11PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel11OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel11OosPortn_Object = MibTableColumn
pmopm2AlmChannel11OosPortn = _Pmopm2AlmChannel11OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 36, 1, 7),
    _Pmopm2AlmChannel11OosPortn_Type()
)
pmopm2AlmChannel11OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel11OosPortn.setStatus("current")
_Pmopm2Almchannel12PortTable_Object = MibTable
pmopm2Almchannel12PortTable = _Pmopm2Almchannel12PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel12PortTable.setStatus("current")
_Pmopm2Almchannel12PortEntry_Object = MibTableRow
pmopm2Almchannel12PortEntry = _Pmopm2Almchannel12PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1)
)
pmopm2Almchannel12PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel12PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel12PortEntry.setStatus("current")


class _Pmopm2Almchannel12PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel12PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel12PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel12PortIndex_Object = MibTableColumn
pmopm2Almchannel12PortIndex = _Pmopm2Almchannel12PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1, 1),
    _Pmopm2Almchannel12PortIndex_Type()
)
pmopm2Almchannel12PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel12PortIndex.setStatus("current")
_Pmopm2AlmChannel12AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel12AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel12AbsentPortn = _Pmopm2AlmChannel12AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1, 2),
    _Pmopm2AlmChannel12AbsentPortn_Type()
)
pmopm2AlmChannel12AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel12AbsentPortn.setStatus("current")
_Pmopm2AlmChannel12MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel12MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel12MismatchPortn = _Pmopm2AlmChannel12MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1, 3),
    _Pmopm2AlmChannel12MismatchPortn_Type()
)
pmopm2AlmChannel12MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel12MismatchPortn.setStatus("current")
_Pmopm2AlmChannel12BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel12BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel12BalancedPortn = _Pmopm2AlmChannel12BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1, 4),
    _Pmopm2AlmChannel12BalancedPortn_Type()
)
pmopm2AlmChannel12BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel12BalancedPortn.setStatus("current")
_Pmopm2AlmChannel12PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel12PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel12PowerLowPortn = _Pmopm2AlmChannel12PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1, 5),
    _Pmopm2AlmChannel12PowerLowPortn_Type()
)
pmopm2AlmChannel12PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel12PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel12PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel12PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel12PowerHighPortn = _Pmopm2AlmChannel12PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1, 6),
    _Pmopm2AlmChannel12PowerHighPortn_Type()
)
pmopm2AlmChannel12PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel12PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel12OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel12OosPortn_Object = MibTableColumn
pmopm2AlmChannel12OosPortn = _Pmopm2AlmChannel12OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 38, 1, 7),
    _Pmopm2AlmChannel12OosPortn_Type()
)
pmopm2AlmChannel12OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel12OosPortn.setStatus("current")
_Pmopm2Almchannel13PortTable_Object = MibTable
pmopm2Almchannel13PortTable = _Pmopm2Almchannel13PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel13PortTable.setStatus("current")
_Pmopm2Almchannel13PortEntry_Object = MibTableRow
pmopm2Almchannel13PortEntry = _Pmopm2Almchannel13PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1)
)
pmopm2Almchannel13PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel13PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel13PortEntry.setStatus("current")


class _Pmopm2Almchannel13PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel13PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel13PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel13PortIndex_Object = MibTableColumn
pmopm2Almchannel13PortIndex = _Pmopm2Almchannel13PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1, 1),
    _Pmopm2Almchannel13PortIndex_Type()
)
pmopm2Almchannel13PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel13PortIndex.setStatus("current")
_Pmopm2AlmChannel13AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel13AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel13AbsentPortn = _Pmopm2AlmChannel13AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1, 2),
    _Pmopm2AlmChannel13AbsentPortn_Type()
)
pmopm2AlmChannel13AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel13AbsentPortn.setStatus("current")
_Pmopm2AlmChannel13MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel13MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel13MismatchPortn = _Pmopm2AlmChannel13MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1, 3),
    _Pmopm2AlmChannel13MismatchPortn_Type()
)
pmopm2AlmChannel13MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel13MismatchPortn.setStatus("current")
_Pmopm2AlmChannel13BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel13BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel13BalancedPortn = _Pmopm2AlmChannel13BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1, 4),
    _Pmopm2AlmChannel13BalancedPortn_Type()
)
pmopm2AlmChannel13BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel13BalancedPortn.setStatus("current")
_Pmopm2AlmChannel13PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel13PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel13PowerLowPortn = _Pmopm2AlmChannel13PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1, 5),
    _Pmopm2AlmChannel13PowerLowPortn_Type()
)
pmopm2AlmChannel13PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel13PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel13PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel13PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel13PowerHighPortn = _Pmopm2AlmChannel13PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1, 6),
    _Pmopm2AlmChannel13PowerHighPortn_Type()
)
pmopm2AlmChannel13PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel13PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel13OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel13OosPortn_Object = MibTableColumn
pmopm2AlmChannel13OosPortn = _Pmopm2AlmChannel13OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 40, 1, 7),
    _Pmopm2AlmChannel13OosPortn_Type()
)
pmopm2AlmChannel13OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel13OosPortn.setStatus("current")
_Pmopm2Almchannel14PortTable_Object = MibTable
pmopm2Almchannel14PortTable = _Pmopm2Almchannel14PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel14PortTable.setStatus("current")
_Pmopm2Almchannel14PortEntry_Object = MibTableRow
pmopm2Almchannel14PortEntry = _Pmopm2Almchannel14PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1)
)
pmopm2Almchannel14PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel14PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel14PortEntry.setStatus("current")


class _Pmopm2Almchannel14PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel14PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel14PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel14PortIndex_Object = MibTableColumn
pmopm2Almchannel14PortIndex = _Pmopm2Almchannel14PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1, 1),
    _Pmopm2Almchannel14PortIndex_Type()
)
pmopm2Almchannel14PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel14PortIndex.setStatus("current")
_Pmopm2AlmChannel14AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel14AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel14AbsentPortn = _Pmopm2AlmChannel14AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1, 2),
    _Pmopm2AlmChannel14AbsentPortn_Type()
)
pmopm2AlmChannel14AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel14AbsentPortn.setStatus("current")
_Pmopm2AlmChannel14MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel14MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel14MismatchPortn = _Pmopm2AlmChannel14MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1, 3),
    _Pmopm2AlmChannel14MismatchPortn_Type()
)
pmopm2AlmChannel14MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel14MismatchPortn.setStatus("current")
_Pmopm2AlmChannel14BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel14BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel14BalancedPortn = _Pmopm2AlmChannel14BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1, 4),
    _Pmopm2AlmChannel14BalancedPortn_Type()
)
pmopm2AlmChannel14BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel14BalancedPortn.setStatus("current")
_Pmopm2AlmChannel14PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel14PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel14PowerLowPortn = _Pmopm2AlmChannel14PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1, 5),
    _Pmopm2AlmChannel14PowerLowPortn_Type()
)
pmopm2AlmChannel14PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel14PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel14PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel14PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel14PowerHighPortn = _Pmopm2AlmChannel14PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1, 6),
    _Pmopm2AlmChannel14PowerHighPortn_Type()
)
pmopm2AlmChannel14PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel14PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel14OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel14OosPortn_Object = MibTableColumn
pmopm2AlmChannel14OosPortn = _Pmopm2AlmChannel14OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 42, 1, 7),
    _Pmopm2AlmChannel14OosPortn_Type()
)
pmopm2AlmChannel14OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel14OosPortn.setStatus("current")
_Pmopm2Almchannel15PortTable_Object = MibTable
pmopm2Almchannel15PortTable = _Pmopm2Almchannel15PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel15PortTable.setStatus("current")
_Pmopm2Almchannel15PortEntry_Object = MibTableRow
pmopm2Almchannel15PortEntry = _Pmopm2Almchannel15PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1)
)
pmopm2Almchannel15PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel15PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel15PortEntry.setStatus("current")


class _Pmopm2Almchannel15PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel15PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel15PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel15PortIndex_Object = MibTableColumn
pmopm2Almchannel15PortIndex = _Pmopm2Almchannel15PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1, 1),
    _Pmopm2Almchannel15PortIndex_Type()
)
pmopm2Almchannel15PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel15PortIndex.setStatus("current")
_Pmopm2AlmChannel15AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel15AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel15AbsentPortn = _Pmopm2AlmChannel15AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1, 2),
    _Pmopm2AlmChannel15AbsentPortn_Type()
)
pmopm2AlmChannel15AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel15AbsentPortn.setStatus("current")
_Pmopm2AlmChannel15MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel15MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel15MismatchPortn = _Pmopm2AlmChannel15MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1, 3),
    _Pmopm2AlmChannel15MismatchPortn_Type()
)
pmopm2AlmChannel15MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel15MismatchPortn.setStatus("current")
_Pmopm2AlmChannel15BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel15BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel15BalancedPortn = _Pmopm2AlmChannel15BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1, 4),
    _Pmopm2AlmChannel15BalancedPortn_Type()
)
pmopm2AlmChannel15BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel15BalancedPortn.setStatus("current")
_Pmopm2AlmChannel15PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel15PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel15PowerLowPortn = _Pmopm2AlmChannel15PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1, 5),
    _Pmopm2AlmChannel15PowerLowPortn_Type()
)
pmopm2AlmChannel15PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel15PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel15PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel15PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel15PowerHighPortn = _Pmopm2AlmChannel15PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1, 6),
    _Pmopm2AlmChannel15PowerHighPortn_Type()
)
pmopm2AlmChannel15PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel15PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel15OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel15OosPortn_Object = MibTableColumn
pmopm2AlmChannel15OosPortn = _Pmopm2AlmChannel15OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 44, 1, 7),
    _Pmopm2AlmChannel15OosPortn_Type()
)
pmopm2AlmChannel15OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel15OosPortn.setStatus("current")
_Pmopm2Almchannel16PortTable_Object = MibTable
pmopm2Almchannel16PortTable = _Pmopm2Almchannel16PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel16PortTable.setStatus("current")
_Pmopm2Almchannel16PortEntry_Object = MibTableRow
pmopm2Almchannel16PortEntry = _Pmopm2Almchannel16PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1)
)
pmopm2Almchannel16PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel16PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel16PortEntry.setStatus("current")


class _Pmopm2Almchannel16PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel16PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel16PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel16PortIndex_Object = MibTableColumn
pmopm2Almchannel16PortIndex = _Pmopm2Almchannel16PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1, 1),
    _Pmopm2Almchannel16PortIndex_Type()
)
pmopm2Almchannel16PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel16PortIndex.setStatus("current")
_Pmopm2AlmChannel16AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel16AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel16AbsentPortn = _Pmopm2AlmChannel16AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1, 2),
    _Pmopm2AlmChannel16AbsentPortn_Type()
)
pmopm2AlmChannel16AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel16AbsentPortn.setStatus("current")
_Pmopm2AlmChannel16MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel16MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel16MismatchPortn = _Pmopm2AlmChannel16MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1, 3),
    _Pmopm2AlmChannel16MismatchPortn_Type()
)
pmopm2AlmChannel16MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel16MismatchPortn.setStatus("current")
_Pmopm2AlmChannel16BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel16BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel16BalancedPortn = _Pmopm2AlmChannel16BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1, 4),
    _Pmopm2AlmChannel16BalancedPortn_Type()
)
pmopm2AlmChannel16BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel16BalancedPortn.setStatus("current")
_Pmopm2AlmChannel16PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel16PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel16PowerLowPortn = _Pmopm2AlmChannel16PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1, 5),
    _Pmopm2AlmChannel16PowerLowPortn_Type()
)
pmopm2AlmChannel16PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel16PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel16PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel16PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel16PowerHighPortn = _Pmopm2AlmChannel16PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1, 6),
    _Pmopm2AlmChannel16PowerHighPortn_Type()
)
pmopm2AlmChannel16PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel16PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel16OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel16OosPortn_Object = MibTableColumn
pmopm2AlmChannel16OosPortn = _Pmopm2AlmChannel16OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 46, 1, 7),
    _Pmopm2AlmChannel16OosPortn_Type()
)
pmopm2AlmChannel16OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel16OosPortn.setStatus("current")
_Pmopm2Almchannel17PortTable_Object = MibTable
pmopm2Almchannel17PortTable = _Pmopm2Almchannel17PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel17PortTable.setStatus("current")
_Pmopm2Almchannel17PortEntry_Object = MibTableRow
pmopm2Almchannel17PortEntry = _Pmopm2Almchannel17PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1)
)
pmopm2Almchannel17PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel17PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel17PortEntry.setStatus("current")


class _Pmopm2Almchannel17PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel17PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel17PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel17PortIndex_Object = MibTableColumn
pmopm2Almchannel17PortIndex = _Pmopm2Almchannel17PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1, 1),
    _Pmopm2Almchannel17PortIndex_Type()
)
pmopm2Almchannel17PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel17PortIndex.setStatus("current")
_Pmopm2AlmChannel17AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel17AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel17AbsentPortn = _Pmopm2AlmChannel17AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1, 2),
    _Pmopm2AlmChannel17AbsentPortn_Type()
)
pmopm2AlmChannel17AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel17AbsentPortn.setStatus("current")
_Pmopm2AlmChannel17MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel17MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel17MismatchPortn = _Pmopm2AlmChannel17MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1, 3),
    _Pmopm2AlmChannel17MismatchPortn_Type()
)
pmopm2AlmChannel17MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel17MismatchPortn.setStatus("current")
_Pmopm2AlmChannel17BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel17BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel17BalancedPortn = _Pmopm2AlmChannel17BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1, 4),
    _Pmopm2AlmChannel17BalancedPortn_Type()
)
pmopm2AlmChannel17BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel17BalancedPortn.setStatus("current")
_Pmopm2AlmChannel17PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel17PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel17PowerLowPortn = _Pmopm2AlmChannel17PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1, 5),
    _Pmopm2AlmChannel17PowerLowPortn_Type()
)
pmopm2AlmChannel17PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel17PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel17PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel17PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel17PowerHighPortn = _Pmopm2AlmChannel17PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1, 6),
    _Pmopm2AlmChannel17PowerHighPortn_Type()
)
pmopm2AlmChannel17PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel17PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel17OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel17OosPortn_Object = MibTableColumn
pmopm2AlmChannel17OosPortn = _Pmopm2AlmChannel17OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 48, 1, 7),
    _Pmopm2AlmChannel17OosPortn_Type()
)
pmopm2AlmChannel17OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel17OosPortn.setStatus("current")
_Pmopm2Almchannel18PortTable_Object = MibTable
pmopm2Almchannel18PortTable = _Pmopm2Almchannel18PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel18PortTable.setStatus("current")
_Pmopm2Almchannel18PortEntry_Object = MibTableRow
pmopm2Almchannel18PortEntry = _Pmopm2Almchannel18PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1)
)
pmopm2Almchannel18PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel18PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel18PortEntry.setStatus("current")


class _Pmopm2Almchannel18PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel18PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel18PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel18PortIndex_Object = MibTableColumn
pmopm2Almchannel18PortIndex = _Pmopm2Almchannel18PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1, 1),
    _Pmopm2Almchannel18PortIndex_Type()
)
pmopm2Almchannel18PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel18PortIndex.setStatus("current")
_Pmopm2AlmChannel18AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel18AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel18AbsentPortn = _Pmopm2AlmChannel18AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1, 2),
    _Pmopm2AlmChannel18AbsentPortn_Type()
)
pmopm2AlmChannel18AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel18AbsentPortn.setStatus("current")
_Pmopm2AlmChannel18MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel18MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel18MismatchPortn = _Pmopm2AlmChannel18MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1, 3),
    _Pmopm2AlmChannel18MismatchPortn_Type()
)
pmopm2AlmChannel18MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel18MismatchPortn.setStatus("current")
_Pmopm2AlmChannel18BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel18BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel18BalancedPortn = _Pmopm2AlmChannel18BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1, 4),
    _Pmopm2AlmChannel18BalancedPortn_Type()
)
pmopm2AlmChannel18BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel18BalancedPortn.setStatus("current")
_Pmopm2AlmChannel18PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel18PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel18PowerLowPortn = _Pmopm2AlmChannel18PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1, 5),
    _Pmopm2AlmChannel18PowerLowPortn_Type()
)
pmopm2AlmChannel18PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel18PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel18PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel18PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel18PowerHighPortn = _Pmopm2AlmChannel18PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1, 6),
    _Pmopm2AlmChannel18PowerHighPortn_Type()
)
pmopm2AlmChannel18PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel18PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel18OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel18OosPortn_Object = MibTableColumn
pmopm2AlmChannel18OosPortn = _Pmopm2AlmChannel18OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 50, 1, 7),
    _Pmopm2AlmChannel18OosPortn_Type()
)
pmopm2AlmChannel18OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel18OosPortn.setStatus("current")
_Pmopm2Almchannel19PortTable_Object = MibTable
pmopm2Almchannel19PortTable = _Pmopm2Almchannel19PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel19PortTable.setStatus("current")
_Pmopm2Almchannel19PortEntry_Object = MibTableRow
pmopm2Almchannel19PortEntry = _Pmopm2Almchannel19PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1)
)
pmopm2Almchannel19PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel19PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel19PortEntry.setStatus("current")


class _Pmopm2Almchannel19PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel19PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel19PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel19PortIndex_Object = MibTableColumn
pmopm2Almchannel19PortIndex = _Pmopm2Almchannel19PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1, 1),
    _Pmopm2Almchannel19PortIndex_Type()
)
pmopm2Almchannel19PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel19PortIndex.setStatus("current")
_Pmopm2AlmChannel19AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel19AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel19AbsentPortn = _Pmopm2AlmChannel19AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1, 2),
    _Pmopm2AlmChannel19AbsentPortn_Type()
)
pmopm2AlmChannel19AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel19AbsentPortn.setStatus("current")
_Pmopm2AlmChannel19MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel19MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel19MismatchPortn = _Pmopm2AlmChannel19MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1, 3),
    _Pmopm2AlmChannel19MismatchPortn_Type()
)
pmopm2AlmChannel19MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel19MismatchPortn.setStatus("current")
_Pmopm2AlmChannel19BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel19BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel19BalancedPortn = _Pmopm2AlmChannel19BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1, 4),
    _Pmopm2AlmChannel19BalancedPortn_Type()
)
pmopm2AlmChannel19BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel19BalancedPortn.setStatus("current")
_Pmopm2AlmChannel19PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel19PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel19PowerLowPortn = _Pmopm2AlmChannel19PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1, 5),
    _Pmopm2AlmChannel19PowerLowPortn_Type()
)
pmopm2AlmChannel19PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel19PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel19PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel19PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel19PowerHighPortn = _Pmopm2AlmChannel19PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1, 6),
    _Pmopm2AlmChannel19PowerHighPortn_Type()
)
pmopm2AlmChannel19PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel19PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel19OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel19OosPortn_Object = MibTableColumn
pmopm2AlmChannel19OosPortn = _Pmopm2AlmChannel19OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 52, 1, 7),
    _Pmopm2AlmChannel19OosPortn_Type()
)
pmopm2AlmChannel19OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel19OosPortn.setStatus("current")
_Pmopm2Almchannel20PortTable_Object = MibTable
pmopm2Almchannel20PortTable = _Pmopm2Almchannel20PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel20PortTable.setStatus("current")
_Pmopm2Almchannel20PortEntry_Object = MibTableRow
pmopm2Almchannel20PortEntry = _Pmopm2Almchannel20PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1)
)
pmopm2Almchannel20PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel20PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel20PortEntry.setStatus("current")


class _Pmopm2Almchannel20PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel20PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel20PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel20PortIndex_Object = MibTableColumn
pmopm2Almchannel20PortIndex = _Pmopm2Almchannel20PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1, 1),
    _Pmopm2Almchannel20PortIndex_Type()
)
pmopm2Almchannel20PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel20PortIndex.setStatus("current")
_Pmopm2AlmChannel20AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel20AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel20AbsentPortn = _Pmopm2AlmChannel20AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1, 2),
    _Pmopm2AlmChannel20AbsentPortn_Type()
)
pmopm2AlmChannel20AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel20AbsentPortn.setStatus("current")
_Pmopm2AlmChannel20MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel20MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel20MismatchPortn = _Pmopm2AlmChannel20MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1, 3),
    _Pmopm2AlmChannel20MismatchPortn_Type()
)
pmopm2AlmChannel20MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel20MismatchPortn.setStatus("current")
_Pmopm2AlmChannel20BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel20BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel20BalancedPortn = _Pmopm2AlmChannel20BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1, 4),
    _Pmopm2AlmChannel20BalancedPortn_Type()
)
pmopm2AlmChannel20BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel20BalancedPortn.setStatus("current")
_Pmopm2AlmChannel20PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel20PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel20PowerLowPortn = _Pmopm2AlmChannel20PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1, 5),
    _Pmopm2AlmChannel20PowerLowPortn_Type()
)
pmopm2AlmChannel20PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel20PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel20PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel20PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel20PowerHighPortn = _Pmopm2AlmChannel20PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1, 6),
    _Pmopm2AlmChannel20PowerHighPortn_Type()
)
pmopm2AlmChannel20PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel20PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel20OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel20OosPortn_Object = MibTableColumn
pmopm2AlmChannel20OosPortn = _Pmopm2AlmChannel20OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 54, 1, 7),
    _Pmopm2AlmChannel20OosPortn_Type()
)
pmopm2AlmChannel20OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel20OosPortn.setStatus("current")
_Pmopm2Almchannel21PortTable_Object = MibTable
pmopm2Almchannel21PortTable = _Pmopm2Almchannel21PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel21PortTable.setStatus("current")
_Pmopm2Almchannel21PortEntry_Object = MibTableRow
pmopm2Almchannel21PortEntry = _Pmopm2Almchannel21PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1)
)
pmopm2Almchannel21PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel21PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel21PortEntry.setStatus("current")


class _Pmopm2Almchannel21PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel21PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel21PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel21PortIndex_Object = MibTableColumn
pmopm2Almchannel21PortIndex = _Pmopm2Almchannel21PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1, 1),
    _Pmopm2Almchannel21PortIndex_Type()
)
pmopm2Almchannel21PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel21PortIndex.setStatus("current")
_Pmopm2AlmChannel21AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel21AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel21AbsentPortn = _Pmopm2AlmChannel21AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1, 2),
    _Pmopm2AlmChannel21AbsentPortn_Type()
)
pmopm2AlmChannel21AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel21AbsentPortn.setStatus("current")
_Pmopm2AlmChannel21MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel21MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel21MismatchPortn = _Pmopm2AlmChannel21MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1, 3),
    _Pmopm2AlmChannel21MismatchPortn_Type()
)
pmopm2AlmChannel21MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel21MismatchPortn.setStatus("current")
_Pmopm2AlmChannel21BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel21BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel21BalancedPortn = _Pmopm2AlmChannel21BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1, 4),
    _Pmopm2AlmChannel21BalancedPortn_Type()
)
pmopm2AlmChannel21BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel21BalancedPortn.setStatus("current")
_Pmopm2AlmChannel21PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel21PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel21PowerLowPortn = _Pmopm2AlmChannel21PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1, 5),
    _Pmopm2AlmChannel21PowerLowPortn_Type()
)
pmopm2AlmChannel21PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel21PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel21PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel21PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel21PowerHighPortn = _Pmopm2AlmChannel21PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1, 6),
    _Pmopm2AlmChannel21PowerHighPortn_Type()
)
pmopm2AlmChannel21PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel21PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel21OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel21OosPortn_Object = MibTableColumn
pmopm2AlmChannel21OosPortn = _Pmopm2AlmChannel21OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 56, 1, 7),
    _Pmopm2AlmChannel21OosPortn_Type()
)
pmopm2AlmChannel21OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel21OosPortn.setStatus("current")
_Pmopm2Almchannel22PortTable_Object = MibTable
pmopm2Almchannel22PortTable = _Pmopm2Almchannel22PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel22PortTable.setStatus("current")
_Pmopm2Almchannel22PortEntry_Object = MibTableRow
pmopm2Almchannel22PortEntry = _Pmopm2Almchannel22PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1)
)
pmopm2Almchannel22PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel22PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel22PortEntry.setStatus("current")


class _Pmopm2Almchannel22PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel22PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel22PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel22PortIndex_Object = MibTableColumn
pmopm2Almchannel22PortIndex = _Pmopm2Almchannel22PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1, 1),
    _Pmopm2Almchannel22PortIndex_Type()
)
pmopm2Almchannel22PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel22PortIndex.setStatus("current")
_Pmopm2AlmChannel22AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel22AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel22AbsentPortn = _Pmopm2AlmChannel22AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1, 2),
    _Pmopm2AlmChannel22AbsentPortn_Type()
)
pmopm2AlmChannel22AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel22AbsentPortn.setStatus("current")
_Pmopm2AlmChannel22MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel22MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel22MismatchPortn = _Pmopm2AlmChannel22MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1, 3),
    _Pmopm2AlmChannel22MismatchPortn_Type()
)
pmopm2AlmChannel22MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel22MismatchPortn.setStatus("current")
_Pmopm2AlmChannel22BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel22BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel22BalancedPortn = _Pmopm2AlmChannel22BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1, 4),
    _Pmopm2AlmChannel22BalancedPortn_Type()
)
pmopm2AlmChannel22BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel22BalancedPortn.setStatus("current")
_Pmopm2AlmChannel22PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel22PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel22PowerLowPortn = _Pmopm2AlmChannel22PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1, 5),
    _Pmopm2AlmChannel22PowerLowPortn_Type()
)
pmopm2AlmChannel22PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel22PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel22PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel22PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel22PowerHighPortn = _Pmopm2AlmChannel22PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1, 6),
    _Pmopm2AlmChannel22PowerHighPortn_Type()
)
pmopm2AlmChannel22PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel22PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel22OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel22OosPortn_Object = MibTableColumn
pmopm2AlmChannel22OosPortn = _Pmopm2AlmChannel22OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 58, 1, 7),
    _Pmopm2AlmChannel22OosPortn_Type()
)
pmopm2AlmChannel22OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel22OosPortn.setStatus("current")
_Pmopm2Almchannel23PortTable_Object = MibTable
pmopm2Almchannel23PortTable = _Pmopm2Almchannel23PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel23PortTable.setStatus("current")
_Pmopm2Almchannel23PortEntry_Object = MibTableRow
pmopm2Almchannel23PortEntry = _Pmopm2Almchannel23PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1)
)
pmopm2Almchannel23PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel23PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel23PortEntry.setStatus("current")


class _Pmopm2Almchannel23PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel23PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel23PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel23PortIndex_Object = MibTableColumn
pmopm2Almchannel23PortIndex = _Pmopm2Almchannel23PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1, 1),
    _Pmopm2Almchannel23PortIndex_Type()
)
pmopm2Almchannel23PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel23PortIndex.setStatus("current")
_Pmopm2AlmChannel23AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel23AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel23AbsentPortn = _Pmopm2AlmChannel23AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1, 2),
    _Pmopm2AlmChannel23AbsentPortn_Type()
)
pmopm2AlmChannel23AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel23AbsentPortn.setStatus("current")
_Pmopm2AlmChannel23MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel23MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel23MismatchPortn = _Pmopm2AlmChannel23MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1, 3),
    _Pmopm2AlmChannel23MismatchPortn_Type()
)
pmopm2AlmChannel23MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel23MismatchPortn.setStatus("current")
_Pmopm2AlmChannel23BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel23BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel23BalancedPortn = _Pmopm2AlmChannel23BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1, 4),
    _Pmopm2AlmChannel23BalancedPortn_Type()
)
pmopm2AlmChannel23BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel23BalancedPortn.setStatus("current")
_Pmopm2AlmChannel23PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel23PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel23PowerLowPortn = _Pmopm2AlmChannel23PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1, 5),
    _Pmopm2AlmChannel23PowerLowPortn_Type()
)
pmopm2AlmChannel23PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel23PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel23PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel23PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel23PowerHighPortn = _Pmopm2AlmChannel23PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1, 6),
    _Pmopm2AlmChannel23PowerHighPortn_Type()
)
pmopm2AlmChannel23PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel23PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel23OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel23OosPortn_Object = MibTableColumn
pmopm2AlmChannel23OosPortn = _Pmopm2AlmChannel23OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 60, 1, 7),
    _Pmopm2AlmChannel23OosPortn_Type()
)
pmopm2AlmChannel23OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel23OosPortn.setStatus("current")
_Pmopm2Almchannel24PortTable_Object = MibTable
pmopm2Almchannel24PortTable = _Pmopm2Almchannel24PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel24PortTable.setStatus("current")
_Pmopm2Almchannel24PortEntry_Object = MibTableRow
pmopm2Almchannel24PortEntry = _Pmopm2Almchannel24PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1)
)
pmopm2Almchannel24PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel24PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel24PortEntry.setStatus("current")


class _Pmopm2Almchannel24PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel24PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel24PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel24PortIndex_Object = MibTableColumn
pmopm2Almchannel24PortIndex = _Pmopm2Almchannel24PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1, 1),
    _Pmopm2Almchannel24PortIndex_Type()
)
pmopm2Almchannel24PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel24PortIndex.setStatus("current")
_Pmopm2AlmChannel24AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel24AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel24AbsentPortn = _Pmopm2AlmChannel24AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1, 2),
    _Pmopm2AlmChannel24AbsentPortn_Type()
)
pmopm2AlmChannel24AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel24AbsentPortn.setStatus("current")
_Pmopm2AlmChannel24MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel24MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel24MismatchPortn = _Pmopm2AlmChannel24MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1, 3),
    _Pmopm2AlmChannel24MismatchPortn_Type()
)
pmopm2AlmChannel24MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel24MismatchPortn.setStatus("current")
_Pmopm2AlmChannel24BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel24BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel24BalancedPortn = _Pmopm2AlmChannel24BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1, 4),
    _Pmopm2AlmChannel24BalancedPortn_Type()
)
pmopm2AlmChannel24BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel24BalancedPortn.setStatus("current")
_Pmopm2AlmChannel24PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel24PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel24PowerLowPortn = _Pmopm2AlmChannel24PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1, 5),
    _Pmopm2AlmChannel24PowerLowPortn_Type()
)
pmopm2AlmChannel24PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel24PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel24PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel24PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel24PowerHighPortn = _Pmopm2AlmChannel24PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1, 6),
    _Pmopm2AlmChannel24PowerHighPortn_Type()
)
pmopm2AlmChannel24PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel24PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel24OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel24OosPortn_Object = MibTableColumn
pmopm2AlmChannel24OosPortn = _Pmopm2AlmChannel24OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 62, 1, 7),
    _Pmopm2AlmChannel24OosPortn_Type()
)
pmopm2AlmChannel24OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel24OosPortn.setStatus("current")
_Pmopm2Almchannel25PortTable_Object = MibTable
pmopm2Almchannel25PortTable = _Pmopm2Almchannel25PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel25PortTable.setStatus("current")
_Pmopm2Almchannel25PortEntry_Object = MibTableRow
pmopm2Almchannel25PortEntry = _Pmopm2Almchannel25PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1)
)
pmopm2Almchannel25PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel25PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel25PortEntry.setStatus("current")


class _Pmopm2Almchannel25PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel25PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel25PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel25PortIndex_Object = MibTableColumn
pmopm2Almchannel25PortIndex = _Pmopm2Almchannel25PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1, 1),
    _Pmopm2Almchannel25PortIndex_Type()
)
pmopm2Almchannel25PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel25PortIndex.setStatus("current")
_Pmopm2AlmChannel25AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel25AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel25AbsentPortn = _Pmopm2AlmChannel25AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1, 2),
    _Pmopm2AlmChannel25AbsentPortn_Type()
)
pmopm2AlmChannel25AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel25AbsentPortn.setStatus("current")
_Pmopm2AlmChannel25MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel25MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel25MismatchPortn = _Pmopm2AlmChannel25MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1, 3),
    _Pmopm2AlmChannel25MismatchPortn_Type()
)
pmopm2AlmChannel25MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel25MismatchPortn.setStatus("current")
_Pmopm2AlmChannel25BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel25BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel25BalancedPortn = _Pmopm2AlmChannel25BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1, 4),
    _Pmopm2AlmChannel25BalancedPortn_Type()
)
pmopm2AlmChannel25BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel25BalancedPortn.setStatus("current")
_Pmopm2AlmChannel25PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel25PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel25PowerLowPortn = _Pmopm2AlmChannel25PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1, 5),
    _Pmopm2AlmChannel25PowerLowPortn_Type()
)
pmopm2AlmChannel25PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel25PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel25PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel25PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel25PowerHighPortn = _Pmopm2AlmChannel25PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1, 6),
    _Pmopm2AlmChannel25PowerHighPortn_Type()
)
pmopm2AlmChannel25PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel25PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel25OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel25OosPortn_Object = MibTableColumn
pmopm2AlmChannel25OosPortn = _Pmopm2AlmChannel25OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 64, 1, 7),
    _Pmopm2AlmChannel25OosPortn_Type()
)
pmopm2AlmChannel25OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel25OosPortn.setStatus("current")
_Pmopm2Almchannel26PortTable_Object = MibTable
pmopm2Almchannel26PortTable = _Pmopm2Almchannel26PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel26PortTable.setStatus("current")
_Pmopm2Almchannel26PortEntry_Object = MibTableRow
pmopm2Almchannel26PortEntry = _Pmopm2Almchannel26PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1)
)
pmopm2Almchannel26PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel26PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel26PortEntry.setStatus("current")


class _Pmopm2Almchannel26PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel26PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel26PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel26PortIndex_Object = MibTableColumn
pmopm2Almchannel26PortIndex = _Pmopm2Almchannel26PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1, 1),
    _Pmopm2Almchannel26PortIndex_Type()
)
pmopm2Almchannel26PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel26PortIndex.setStatus("current")
_Pmopm2AlmChannel26AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel26AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel26AbsentPortn = _Pmopm2AlmChannel26AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1, 2),
    _Pmopm2AlmChannel26AbsentPortn_Type()
)
pmopm2AlmChannel26AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel26AbsentPortn.setStatus("current")
_Pmopm2AlmChannel26MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel26MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel26MismatchPortn = _Pmopm2AlmChannel26MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1, 3),
    _Pmopm2AlmChannel26MismatchPortn_Type()
)
pmopm2AlmChannel26MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel26MismatchPortn.setStatus("current")
_Pmopm2AlmChannel26BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel26BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel26BalancedPortn = _Pmopm2AlmChannel26BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1, 4),
    _Pmopm2AlmChannel26BalancedPortn_Type()
)
pmopm2AlmChannel26BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel26BalancedPortn.setStatus("current")
_Pmopm2AlmChannel26PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel26PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel26PowerLowPortn = _Pmopm2AlmChannel26PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1, 5),
    _Pmopm2AlmChannel26PowerLowPortn_Type()
)
pmopm2AlmChannel26PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel26PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel26PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel26PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel26PowerHighPortn = _Pmopm2AlmChannel26PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1, 6),
    _Pmopm2AlmChannel26PowerHighPortn_Type()
)
pmopm2AlmChannel26PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel26PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel26OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel26OosPortn_Object = MibTableColumn
pmopm2AlmChannel26OosPortn = _Pmopm2AlmChannel26OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 66, 1, 7),
    _Pmopm2AlmChannel26OosPortn_Type()
)
pmopm2AlmChannel26OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel26OosPortn.setStatus("current")
_Pmopm2Almchannel27PortTable_Object = MibTable
pmopm2Almchannel27PortTable = _Pmopm2Almchannel27PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel27PortTable.setStatus("current")
_Pmopm2Almchannel27PortEntry_Object = MibTableRow
pmopm2Almchannel27PortEntry = _Pmopm2Almchannel27PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1)
)
pmopm2Almchannel27PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel27PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel27PortEntry.setStatus("current")


class _Pmopm2Almchannel27PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel27PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel27PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel27PortIndex_Object = MibTableColumn
pmopm2Almchannel27PortIndex = _Pmopm2Almchannel27PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1, 1),
    _Pmopm2Almchannel27PortIndex_Type()
)
pmopm2Almchannel27PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel27PortIndex.setStatus("current")
_Pmopm2AlmChannel27AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel27AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel27AbsentPortn = _Pmopm2AlmChannel27AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1, 2),
    _Pmopm2AlmChannel27AbsentPortn_Type()
)
pmopm2AlmChannel27AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel27AbsentPortn.setStatus("current")
_Pmopm2AlmChannel27MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel27MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel27MismatchPortn = _Pmopm2AlmChannel27MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1, 3),
    _Pmopm2AlmChannel27MismatchPortn_Type()
)
pmopm2AlmChannel27MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel27MismatchPortn.setStatus("current")
_Pmopm2AlmChannel27BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel27BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel27BalancedPortn = _Pmopm2AlmChannel27BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1, 4),
    _Pmopm2AlmChannel27BalancedPortn_Type()
)
pmopm2AlmChannel27BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel27BalancedPortn.setStatus("current")
_Pmopm2AlmChannel27PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel27PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel27PowerLowPortn = _Pmopm2AlmChannel27PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1, 5),
    _Pmopm2AlmChannel27PowerLowPortn_Type()
)
pmopm2AlmChannel27PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel27PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel27PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel27PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel27PowerHighPortn = _Pmopm2AlmChannel27PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1, 6),
    _Pmopm2AlmChannel27PowerHighPortn_Type()
)
pmopm2AlmChannel27PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel27PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel27OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel27OosPortn_Object = MibTableColumn
pmopm2AlmChannel27OosPortn = _Pmopm2AlmChannel27OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 68, 1, 7),
    _Pmopm2AlmChannel27OosPortn_Type()
)
pmopm2AlmChannel27OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel27OosPortn.setStatus("current")
_Pmopm2Almchannel28PortTable_Object = MibTable
pmopm2Almchannel28PortTable = _Pmopm2Almchannel28PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel28PortTable.setStatus("current")
_Pmopm2Almchannel28PortEntry_Object = MibTableRow
pmopm2Almchannel28PortEntry = _Pmopm2Almchannel28PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1)
)
pmopm2Almchannel28PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel28PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel28PortEntry.setStatus("current")


class _Pmopm2Almchannel28PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel28PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel28PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel28PortIndex_Object = MibTableColumn
pmopm2Almchannel28PortIndex = _Pmopm2Almchannel28PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1, 1),
    _Pmopm2Almchannel28PortIndex_Type()
)
pmopm2Almchannel28PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel28PortIndex.setStatus("current")
_Pmopm2AlmChannel28AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel28AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel28AbsentPortn = _Pmopm2AlmChannel28AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1, 2),
    _Pmopm2AlmChannel28AbsentPortn_Type()
)
pmopm2AlmChannel28AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel28AbsentPortn.setStatus("current")
_Pmopm2AlmChannel28MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel28MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel28MismatchPortn = _Pmopm2AlmChannel28MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1, 3),
    _Pmopm2AlmChannel28MismatchPortn_Type()
)
pmopm2AlmChannel28MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel28MismatchPortn.setStatus("current")
_Pmopm2AlmChannel28BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel28BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel28BalancedPortn = _Pmopm2AlmChannel28BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1, 4),
    _Pmopm2AlmChannel28BalancedPortn_Type()
)
pmopm2AlmChannel28BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel28BalancedPortn.setStatus("current")
_Pmopm2AlmChannel28PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel28PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel28PowerLowPortn = _Pmopm2AlmChannel28PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1, 5),
    _Pmopm2AlmChannel28PowerLowPortn_Type()
)
pmopm2AlmChannel28PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel28PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel28PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel28PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel28PowerHighPortn = _Pmopm2AlmChannel28PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1, 6),
    _Pmopm2AlmChannel28PowerHighPortn_Type()
)
pmopm2AlmChannel28PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel28PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel28OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel28OosPortn_Object = MibTableColumn
pmopm2AlmChannel28OosPortn = _Pmopm2AlmChannel28OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 70, 1, 7),
    _Pmopm2AlmChannel28OosPortn_Type()
)
pmopm2AlmChannel28OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel28OosPortn.setStatus("current")
_Pmopm2Almchannel29PortTable_Object = MibTable
pmopm2Almchannel29PortTable = _Pmopm2Almchannel29PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel29PortTable.setStatus("current")
_Pmopm2Almchannel29PortEntry_Object = MibTableRow
pmopm2Almchannel29PortEntry = _Pmopm2Almchannel29PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1)
)
pmopm2Almchannel29PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel29PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel29PortEntry.setStatus("current")


class _Pmopm2Almchannel29PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel29PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel29PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel29PortIndex_Object = MibTableColumn
pmopm2Almchannel29PortIndex = _Pmopm2Almchannel29PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1, 1),
    _Pmopm2Almchannel29PortIndex_Type()
)
pmopm2Almchannel29PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel29PortIndex.setStatus("current")
_Pmopm2AlmChannel29AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel29AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel29AbsentPortn = _Pmopm2AlmChannel29AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1, 2),
    _Pmopm2AlmChannel29AbsentPortn_Type()
)
pmopm2AlmChannel29AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel29AbsentPortn.setStatus("current")
_Pmopm2AlmChannel29MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel29MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel29MismatchPortn = _Pmopm2AlmChannel29MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1, 3),
    _Pmopm2AlmChannel29MismatchPortn_Type()
)
pmopm2AlmChannel29MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel29MismatchPortn.setStatus("current")
_Pmopm2AlmChannel29BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel29BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel29BalancedPortn = _Pmopm2AlmChannel29BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1, 4),
    _Pmopm2AlmChannel29BalancedPortn_Type()
)
pmopm2AlmChannel29BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel29BalancedPortn.setStatus("current")
_Pmopm2AlmChannel29PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel29PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel29PowerLowPortn = _Pmopm2AlmChannel29PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1, 5),
    _Pmopm2AlmChannel29PowerLowPortn_Type()
)
pmopm2AlmChannel29PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel29PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel29PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel29PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel29PowerHighPortn = _Pmopm2AlmChannel29PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1, 6),
    _Pmopm2AlmChannel29PowerHighPortn_Type()
)
pmopm2AlmChannel29PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel29PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel29OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel29OosPortn_Object = MibTableColumn
pmopm2AlmChannel29OosPortn = _Pmopm2AlmChannel29OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 72, 1, 7),
    _Pmopm2AlmChannel29OosPortn_Type()
)
pmopm2AlmChannel29OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel29OosPortn.setStatus("current")
_Pmopm2Almchannel30PortTable_Object = MibTable
pmopm2Almchannel30PortTable = _Pmopm2Almchannel30PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel30PortTable.setStatus("current")
_Pmopm2Almchannel30PortEntry_Object = MibTableRow
pmopm2Almchannel30PortEntry = _Pmopm2Almchannel30PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1)
)
pmopm2Almchannel30PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel30PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel30PortEntry.setStatus("current")


class _Pmopm2Almchannel30PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel30PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel30PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel30PortIndex_Object = MibTableColumn
pmopm2Almchannel30PortIndex = _Pmopm2Almchannel30PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1, 1),
    _Pmopm2Almchannel30PortIndex_Type()
)
pmopm2Almchannel30PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel30PortIndex.setStatus("current")
_Pmopm2AlmChannel30AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel30AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel30AbsentPortn = _Pmopm2AlmChannel30AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1, 2),
    _Pmopm2AlmChannel30AbsentPortn_Type()
)
pmopm2AlmChannel30AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel30AbsentPortn.setStatus("current")
_Pmopm2AlmChannel30MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel30MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel30MismatchPortn = _Pmopm2AlmChannel30MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1, 3),
    _Pmopm2AlmChannel30MismatchPortn_Type()
)
pmopm2AlmChannel30MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel30MismatchPortn.setStatus("current")
_Pmopm2AlmChannel30BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel30BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel30BalancedPortn = _Pmopm2AlmChannel30BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1, 4),
    _Pmopm2AlmChannel30BalancedPortn_Type()
)
pmopm2AlmChannel30BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel30BalancedPortn.setStatus("current")
_Pmopm2AlmChannel30PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel30PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel30PowerLowPortn = _Pmopm2AlmChannel30PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1, 5),
    _Pmopm2AlmChannel30PowerLowPortn_Type()
)
pmopm2AlmChannel30PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel30PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel30PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel30PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel30PowerHighPortn = _Pmopm2AlmChannel30PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1, 6),
    _Pmopm2AlmChannel30PowerHighPortn_Type()
)
pmopm2AlmChannel30PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel30PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel30OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel30OosPortn_Object = MibTableColumn
pmopm2AlmChannel30OosPortn = _Pmopm2AlmChannel30OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 74, 1, 7),
    _Pmopm2AlmChannel30OosPortn_Type()
)
pmopm2AlmChannel30OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel30OosPortn.setStatus("current")
_Pmopm2Almchannel31PortTable_Object = MibTable
pmopm2Almchannel31PortTable = _Pmopm2Almchannel31PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel31PortTable.setStatus("current")
_Pmopm2Almchannel31PortEntry_Object = MibTableRow
pmopm2Almchannel31PortEntry = _Pmopm2Almchannel31PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1)
)
pmopm2Almchannel31PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel31PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel31PortEntry.setStatus("current")


class _Pmopm2Almchannel31PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel31PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel31PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel31PortIndex_Object = MibTableColumn
pmopm2Almchannel31PortIndex = _Pmopm2Almchannel31PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1, 1),
    _Pmopm2Almchannel31PortIndex_Type()
)
pmopm2Almchannel31PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel31PortIndex.setStatus("current")
_Pmopm2AlmChannel31AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel31AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel31AbsentPortn = _Pmopm2AlmChannel31AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1, 2),
    _Pmopm2AlmChannel31AbsentPortn_Type()
)
pmopm2AlmChannel31AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel31AbsentPortn.setStatus("current")
_Pmopm2AlmChannel31MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel31MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel31MismatchPortn = _Pmopm2AlmChannel31MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1, 3),
    _Pmopm2AlmChannel31MismatchPortn_Type()
)
pmopm2AlmChannel31MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel31MismatchPortn.setStatus("current")
_Pmopm2AlmChannel31BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel31BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel31BalancedPortn = _Pmopm2AlmChannel31BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1, 4),
    _Pmopm2AlmChannel31BalancedPortn_Type()
)
pmopm2AlmChannel31BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel31BalancedPortn.setStatus("current")
_Pmopm2AlmChannel31PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel31PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel31PowerLowPortn = _Pmopm2AlmChannel31PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1, 5),
    _Pmopm2AlmChannel31PowerLowPortn_Type()
)
pmopm2AlmChannel31PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel31PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel31PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel31PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel31PowerHighPortn = _Pmopm2AlmChannel31PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1, 6),
    _Pmopm2AlmChannel31PowerHighPortn_Type()
)
pmopm2AlmChannel31PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel31PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel31OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel31OosPortn_Object = MibTableColumn
pmopm2AlmChannel31OosPortn = _Pmopm2AlmChannel31OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 76, 1, 7),
    _Pmopm2AlmChannel31OosPortn_Type()
)
pmopm2AlmChannel31OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel31OosPortn.setStatus("current")
_Pmopm2Almchannel32PortTable_Object = MibTable
pmopm2Almchannel32PortTable = _Pmopm2Almchannel32PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel32PortTable.setStatus("current")
_Pmopm2Almchannel32PortEntry_Object = MibTableRow
pmopm2Almchannel32PortEntry = _Pmopm2Almchannel32PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1)
)
pmopm2Almchannel32PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel32PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel32PortEntry.setStatus("current")


class _Pmopm2Almchannel32PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel32PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel32PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel32PortIndex_Object = MibTableColumn
pmopm2Almchannel32PortIndex = _Pmopm2Almchannel32PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1, 1),
    _Pmopm2Almchannel32PortIndex_Type()
)
pmopm2Almchannel32PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel32PortIndex.setStatus("current")
_Pmopm2AlmChannel32AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel32AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel32AbsentPortn = _Pmopm2AlmChannel32AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1, 2),
    _Pmopm2AlmChannel32AbsentPortn_Type()
)
pmopm2AlmChannel32AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel32AbsentPortn.setStatus("current")
_Pmopm2AlmChannel32MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel32MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel32MismatchPortn = _Pmopm2AlmChannel32MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1, 3),
    _Pmopm2AlmChannel32MismatchPortn_Type()
)
pmopm2AlmChannel32MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel32MismatchPortn.setStatus("current")
_Pmopm2AlmChannel32BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel32BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel32BalancedPortn = _Pmopm2AlmChannel32BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1, 4),
    _Pmopm2AlmChannel32BalancedPortn_Type()
)
pmopm2AlmChannel32BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel32BalancedPortn.setStatus("current")
_Pmopm2AlmChannel32PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel32PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel32PowerLowPortn = _Pmopm2AlmChannel32PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1, 5),
    _Pmopm2AlmChannel32PowerLowPortn_Type()
)
pmopm2AlmChannel32PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel32PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel32PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel32PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel32PowerHighPortn = _Pmopm2AlmChannel32PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1, 6),
    _Pmopm2AlmChannel32PowerHighPortn_Type()
)
pmopm2AlmChannel32PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel32PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel32OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel32OosPortn_Object = MibTableColumn
pmopm2AlmChannel32OosPortn = _Pmopm2AlmChannel32OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 78, 1, 7),
    _Pmopm2AlmChannel32OosPortn_Type()
)
pmopm2AlmChannel32OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel32OosPortn.setStatus("current")
_Pmopm2Almchannel33PortTable_Object = MibTable
pmopm2Almchannel33PortTable = _Pmopm2Almchannel33PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel33PortTable.setStatus("current")
_Pmopm2Almchannel33PortEntry_Object = MibTableRow
pmopm2Almchannel33PortEntry = _Pmopm2Almchannel33PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1)
)
pmopm2Almchannel33PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel33PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel33PortEntry.setStatus("current")


class _Pmopm2Almchannel33PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel33PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel33PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel33PortIndex_Object = MibTableColumn
pmopm2Almchannel33PortIndex = _Pmopm2Almchannel33PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1, 1),
    _Pmopm2Almchannel33PortIndex_Type()
)
pmopm2Almchannel33PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel33PortIndex.setStatus("current")
_Pmopm2AlmChannel33AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel33AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel33AbsentPortn = _Pmopm2AlmChannel33AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1, 2),
    _Pmopm2AlmChannel33AbsentPortn_Type()
)
pmopm2AlmChannel33AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel33AbsentPortn.setStatus("current")
_Pmopm2AlmChannel33MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel33MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel33MismatchPortn = _Pmopm2AlmChannel33MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1, 3),
    _Pmopm2AlmChannel33MismatchPortn_Type()
)
pmopm2AlmChannel33MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel33MismatchPortn.setStatus("current")
_Pmopm2AlmChannel33BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel33BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel33BalancedPortn = _Pmopm2AlmChannel33BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1, 4),
    _Pmopm2AlmChannel33BalancedPortn_Type()
)
pmopm2AlmChannel33BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel33BalancedPortn.setStatus("current")
_Pmopm2AlmChannel33PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel33PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel33PowerLowPortn = _Pmopm2AlmChannel33PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1, 5),
    _Pmopm2AlmChannel33PowerLowPortn_Type()
)
pmopm2AlmChannel33PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel33PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel33PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel33PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel33PowerHighPortn = _Pmopm2AlmChannel33PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1, 6),
    _Pmopm2AlmChannel33PowerHighPortn_Type()
)
pmopm2AlmChannel33PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel33PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel33OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel33OosPortn_Object = MibTableColumn
pmopm2AlmChannel33OosPortn = _Pmopm2AlmChannel33OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 80, 1, 7),
    _Pmopm2AlmChannel33OosPortn_Type()
)
pmopm2AlmChannel33OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel33OosPortn.setStatus("current")
_Pmopm2Almchannel34PortTable_Object = MibTable
pmopm2Almchannel34PortTable = _Pmopm2Almchannel34PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel34PortTable.setStatus("current")
_Pmopm2Almchannel34PortEntry_Object = MibTableRow
pmopm2Almchannel34PortEntry = _Pmopm2Almchannel34PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1)
)
pmopm2Almchannel34PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel34PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel34PortEntry.setStatus("current")


class _Pmopm2Almchannel34PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel34PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel34PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel34PortIndex_Object = MibTableColumn
pmopm2Almchannel34PortIndex = _Pmopm2Almchannel34PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1, 1),
    _Pmopm2Almchannel34PortIndex_Type()
)
pmopm2Almchannel34PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel34PortIndex.setStatus("current")
_Pmopm2AlmChannel34AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel34AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel34AbsentPortn = _Pmopm2AlmChannel34AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1, 2),
    _Pmopm2AlmChannel34AbsentPortn_Type()
)
pmopm2AlmChannel34AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel34AbsentPortn.setStatus("current")
_Pmopm2AlmChannel34MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel34MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel34MismatchPortn = _Pmopm2AlmChannel34MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1, 3),
    _Pmopm2AlmChannel34MismatchPortn_Type()
)
pmopm2AlmChannel34MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel34MismatchPortn.setStatus("current")
_Pmopm2AlmChannel34BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel34BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel34BalancedPortn = _Pmopm2AlmChannel34BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1, 4),
    _Pmopm2AlmChannel34BalancedPortn_Type()
)
pmopm2AlmChannel34BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel34BalancedPortn.setStatus("current")
_Pmopm2AlmChannel34PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel34PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel34PowerLowPortn = _Pmopm2AlmChannel34PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1, 5),
    _Pmopm2AlmChannel34PowerLowPortn_Type()
)
pmopm2AlmChannel34PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel34PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel34PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel34PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel34PowerHighPortn = _Pmopm2AlmChannel34PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1, 6),
    _Pmopm2AlmChannel34PowerHighPortn_Type()
)
pmopm2AlmChannel34PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel34PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel34OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel34OosPortn_Object = MibTableColumn
pmopm2AlmChannel34OosPortn = _Pmopm2AlmChannel34OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 82, 1, 7),
    _Pmopm2AlmChannel34OosPortn_Type()
)
pmopm2AlmChannel34OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel34OosPortn.setStatus("current")
_Pmopm2Almchannel35PortTable_Object = MibTable
pmopm2Almchannel35PortTable = _Pmopm2Almchannel35PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel35PortTable.setStatus("current")
_Pmopm2Almchannel35PortEntry_Object = MibTableRow
pmopm2Almchannel35PortEntry = _Pmopm2Almchannel35PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1)
)
pmopm2Almchannel35PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel35PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel35PortEntry.setStatus("current")


class _Pmopm2Almchannel35PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel35PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel35PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel35PortIndex_Object = MibTableColumn
pmopm2Almchannel35PortIndex = _Pmopm2Almchannel35PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1, 1),
    _Pmopm2Almchannel35PortIndex_Type()
)
pmopm2Almchannel35PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel35PortIndex.setStatus("current")
_Pmopm2AlmChannel35AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel35AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel35AbsentPortn = _Pmopm2AlmChannel35AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1, 2),
    _Pmopm2AlmChannel35AbsentPortn_Type()
)
pmopm2AlmChannel35AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel35AbsentPortn.setStatus("current")
_Pmopm2AlmChannel35MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel35MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel35MismatchPortn = _Pmopm2AlmChannel35MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1, 3),
    _Pmopm2AlmChannel35MismatchPortn_Type()
)
pmopm2AlmChannel35MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel35MismatchPortn.setStatus("current")
_Pmopm2AlmChannel35BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel35BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel35BalancedPortn = _Pmopm2AlmChannel35BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1, 4),
    _Pmopm2AlmChannel35BalancedPortn_Type()
)
pmopm2AlmChannel35BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel35BalancedPortn.setStatus("current")
_Pmopm2AlmChannel35PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel35PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel35PowerLowPortn = _Pmopm2AlmChannel35PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1, 5),
    _Pmopm2AlmChannel35PowerLowPortn_Type()
)
pmopm2AlmChannel35PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel35PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel35PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel35PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel35PowerHighPortn = _Pmopm2AlmChannel35PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1, 6),
    _Pmopm2AlmChannel35PowerHighPortn_Type()
)
pmopm2AlmChannel35PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel35PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel35OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel35OosPortn_Object = MibTableColumn
pmopm2AlmChannel35OosPortn = _Pmopm2AlmChannel35OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 84, 1, 7),
    _Pmopm2AlmChannel35OosPortn_Type()
)
pmopm2AlmChannel35OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel35OosPortn.setStatus("current")
_Pmopm2Almchannel36PortTable_Object = MibTable
pmopm2Almchannel36PortTable = _Pmopm2Almchannel36PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel36PortTable.setStatus("current")
_Pmopm2Almchannel36PortEntry_Object = MibTableRow
pmopm2Almchannel36PortEntry = _Pmopm2Almchannel36PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1)
)
pmopm2Almchannel36PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel36PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel36PortEntry.setStatus("current")


class _Pmopm2Almchannel36PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel36PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel36PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel36PortIndex_Object = MibTableColumn
pmopm2Almchannel36PortIndex = _Pmopm2Almchannel36PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1, 1),
    _Pmopm2Almchannel36PortIndex_Type()
)
pmopm2Almchannel36PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel36PortIndex.setStatus("current")
_Pmopm2AlmChannel36AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel36AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel36AbsentPortn = _Pmopm2AlmChannel36AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1, 2),
    _Pmopm2AlmChannel36AbsentPortn_Type()
)
pmopm2AlmChannel36AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel36AbsentPortn.setStatus("current")
_Pmopm2AlmChannel36MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel36MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel36MismatchPortn = _Pmopm2AlmChannel36MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1, 3),
    _Pmopm2AlmChannel36MismatchPortn_Type()
)
pmopm2AlmChannel36MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel36MismatchPortn.setStatus("current")
_Pmopm2AlmChannel36BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel36BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel36BalancedPortn = _Pmopm2AlmChannel36BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1, 4),
    _Pmopm2AlmChannel36BalancedPortn_Type()
)
pmopm2AlmChannel36BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel36BalancedPortn.setStatus("current")
_Pmopm2AlmChannel36PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel36PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel36PowerLowPortn = _Pmopm2AlmChannel36PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1, 5),
    _Pmopm2AlmChannel36PowerLowPortn_Type()
)
pmopm2AlmChannel36PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel36PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel36PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel36PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel36PowerHighPortn = _Pmopm2AlmChannel36PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1, 6),
    _Pmopm2AlmChannel36PowerHighPortn_Type()
)
pmopm2AlmChannel36PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel36PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel36OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel36OosPortn_Object = MibTableColumn
pmopm2AlmChannel36OosPortn = _Pmopm2AlmChannel36OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 86, 1, 7),
    _Pmopm2AlmChannel36OosPortn_Type()
)
pmopm2AlmChannel36OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel36OosPortn.setStatus("current")
_Pmopm2Almchannel37PortTable_Object = MibTable
pmopm2Almchannel37PortTable = _Pmopm2Almchannel37PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel37PortTable.setStatus("current")
_Pmopm2Almchannel37PortEntry_Object = MibTableRow
pmopm2Almchannel37PortEntry = _Pmopm2Almchannel37PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1)
)
pmopm2Almchannel37PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel37PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel37PortEntry.setStatus("current")


class _Pmopm2Almchannel37PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel37PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel37PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel37PortIndex_Object = MibTableColumn
pmopm2Almchannel37PortIndex = _Pmopm2Almchannel37PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1, 1),
    _Pmopm2Almchannel37PortIndex_Type()
)
pmopm2Almchannel37PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel37PortIndex.setStatus("current")
_Pmopm2AlmChannel37AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel37AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel37AbsentPortn = _Pmopm2AlmChannel37AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1, 2),
    _Pmopm2AlmChannel37AbsentPortn_Type()
)
pmopm2AlmChannel37AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel37AbsentPortn.setStatus("current")
_Pmopm2AlmChannel37MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel37MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel37MismatchPortn = _Pmopm2AlmChannel37MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1, 3),
    _Pmopm2AlmChannel37MismatchPortn_Type()
)
pmopm2AlmChannel37MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel37MismatchPortn.setStatus("current")
_Pmopm2AlmChannel37BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel37BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel37BalancedPortn = _Pmopm2AlmChannel37BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1, 4),
    _Pmopm2AlmChannel37BalancedPortn_Type()
)
pmopm2AlmChannel37BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel37BalancedPortn.setStatus("current")
_Pmopm2AlmChannel37PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel37PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel37PowerLowPortn = _Pmopm2AlmChannel37PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1, 5),
    _Pmopm2AlmChannel37PowerLowPortn_Type()
)
pmopm2AlmChannel37PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel37PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel37PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel37PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel37PowerHighPortn = _Pmopm2AlmChannel37PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1, 6),
    _Pmopm2AlmChannel37PowerHighPortn_Type()
)
pmopm2AlmChannel37PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel37PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel37OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel37OosPortn_Object = MibTableColumn
pmopm2AlmChannel37OosPortn = _Pmopm2AlmChannel37OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 88, 1, 7),
    _Pmopm2AlmChannel37OosPortn_Type()
)
pmopm2AlmChannel37OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel37OosPortn.setStatus("current")
_Pmopm2Almchannel38PortTable_Object = MibTable
pmopm2Almchannel38PortTable = _Pmopm2Almchannel38PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel38PortTable.setStatus("current")
_Pmopm2Almchannel38PortEntry_Object = MibTableRow
pmopm2Almchannel38PortEntry = _Pmopm2Almchannel38PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1)
)
pmopm2Almchannel38PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel38PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel38PortEntry.setStatus("current")


class _Pmopm2Almchannel38PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel38PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel38PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel38PortIndex_Object = MibTableColumn
pmopm2Almchannel38PortIndex = _Pmopm2Almchannel38PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1, 1),
    _Pmopm2Almchannel38PortIndex_Type()
)
pmopm2Almchannel38PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel38PortIndex.setStatus("current")
_Pmopm2AlmChannel38AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel38AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel38AbsentPortn = _Pmopm2AlmChannel38AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1, 2),
    _Pmopm2AlmChannel38AbsentPortn_Type()
)
pmopm2AlmChannel38AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel38AbsentPortn.setStatus("current")
_Pmopm2AlmChannel38MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel38MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel38MismatchPortn = _Pmopm2AlmChannel38MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1, 3),
    _Pmopm2AlmChannel38MismatchPortn_Type()
)
pmopm2AlmChannel38MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel38MismatchPortn.setStatus("current")
_Pmopm2AlmChannel38BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel38BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel38BalancedPortn = _Pmopm2AlmChannel38BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1, 4),
    _Pmopm2AlmChannel38BalancedPortn_Type()
)
pmopm2AlmChannel38BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel38BalancedPortn.setStatus("current")
_Pmopm2AlmChannel38PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel38PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel38PowerLowPortn = _Pmopm2AlmChannel38PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1, 5),
    _Pmopm2AlmChannel38PowerLowPortn_Type()
)
pmopm2AlmChannel38PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel38PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel38PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel38PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel38PowerHighPortn = _Pmopm2AlmChannel38PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1, 6),
    _Pmopm2AlmChannel38PowerHighPortn_Type()
)
pmopm2AlmChannel38PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel38PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel38OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel38OosPortn_Object = MibTableColumn
pmopm2AlmChannel38OosPortn = _Pmopm2AlmChannel38OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 90, 1, 7),
    _Pmopm2AlmChannel38OosPortn_Type()
)
pmopm2AlmChannel38OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel38OosPortn.setStatus("current")
_Pmopm2Almchannel39PortTable_Object = MibTable
pmopm2Almchannel39PortTable = _Pmopm2Almchannel39PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel39PortTable.setStatus("current")
_Pmopm2Almchannel39PortEntry_Object = MibTableRow
pmopm2Almchannel39PortEntry = _Pmopm2Almchannel39PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1)
)
pmopm2Almchannel39PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel39PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel39PortEntry.setStatus("current")


class _Pmopm2Almchannel39PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel39PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel39PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel39PortIndex_Object = MibTableColumn
pmopm2Almchannel39PortIndex = _Pmopm2Almchannel39PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1, 1),
    _Pmopm2Almchannel39PortIndex_Type()
)
pmopm2Almchannel39PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel39PortIndex.setStatus("current")
_Pmopm2AlmChannel39AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel39AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel39AbsentPortn = _Pmopm2AlmChannel39AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1, 2),
    _Pmopm2AlmChannel39AbsentPortn_Type()
)
pmopm2AlmChannel39AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel39AbsentPortn.setStatus("current")
_Pmopm2AlmChannel39MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel39MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel39MismatchPortn = _Pmopm2AlmChannel39MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1, 3),
    _Pmopm2AlmChannel39MismatchPortn_Type()
)
pmopm2AlmChannel39MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel39MismatchPortn.setStatus("current")
_Pmopm2AlmChannel39BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel39BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel39BalancedPortn = _Pmopm2AlmChannel39BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1, 4),
    _Pmopm2AlmChannel39BalancedPortn_Type()
)
pmopm2AlmChannel39BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel39BalancedPortn.setStatus("current")
_Pmopm2AlmChannel39PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel39PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel39PowerLowPortn = _Pmopm2AlmChannel39PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1, 5),
    _Pmopm2AlmChannel39PowerLowPortn_Type()
)
pmopm2AlmChannel39PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel39PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel39PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel39PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel39PowerHighPortn = _Pmopm2AlmChannel39PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1, 6),
    _Pmopm2AlmChannel39PowerHighPortn_Type()
)
pmopm2AlmChannel39PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel39PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel39OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel39OosPortn_Object = MibTableColumn
pmopm2AlmChannel39OosPortn = _Pmopm2AlmChannel39OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 92, 1, 7),
    _Pmopm2AlmChannel39OosPortn_Type()
)
pmopm2AlmChannel39OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel39OosPortn.setStatus("current")
_Pmopm2Almchannel40PortTable_Object = MibTable
pmopm2Almchannel40PortTable = _Pmopm2Almchannel40PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel40PortTable.setStatus("current")
_Pmopm2Almchannel40PortEntry_Object = MibTableRow
pmopm2Almchannel40PortEntry = _Pmopm2Almchannel40PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1)
)
pmopm2Almchannel40PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel40PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel40PortEntry.setStatus("current")


class _Pmopm2Almchannel40PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel40PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel40PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel40PortIndex_Object = MibTableColumn
pmopm2Almchannel40PortIndex = _Pmopm2Almchannel40PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1, 1),
    _Pmopm2Almchannel40PortIndex_Type()
)
pmopm2Almchannel40PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel40PortIndex.setStatus("current")
_Pmopm2AlmChannel40AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel40AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel40AbsentPortn = _Pmopm2AlmChannel40AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1, 2),
    _Pmopm2AlmChannel40AbsentPortn_Type()
)
pmopm2AlmChannel40AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel40AbsentPortn.setStatus("current")
_Pmopm2AlmChannel40MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel40MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel40MismatchPortn = _Pmopm2AlmChannel40MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1, 3),
    _Pmopm2AlmChannel40MismatchPortn_Type()
)
pmopm2AlmChannel40MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel40MismatchPortn.setStatus("current")
_Pmopm2AlmChannel40BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel40BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel40BalancedPortn = _Pmopm2AlmChannel40BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1, 4),
    _Pmopm2AlmChannel40BalancedPortn_Type()
)
pmopm2AlmChannel40BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel40BalancedPortn.setStatus("current")
_Pmopm2AlmChannel40PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel40PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel40PowerLowPortn = _Pmopm2AlmChannel40PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1, 5),
    _Pmopm2AlmChannel40PowerLowPortn_Type()
)
pmopm2AlmChannel40PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel40PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel40PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel40PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel40PowerHighPortn = _Pmopm2AlmChannel40PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1, 6),
    _Pmopm2AlmChannel40PowerHighPortn_Type()
)
pmopm2AlmChannel40PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel40PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel40OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel40OosPortn_Object = MibTableColumn
pmopm2AlmChannel40OosPortn = _Pmopm2AlmChannel40OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 94, 1, 7),
    _Pmopm2AlmChannel40OosPortn_Type()
)
pmopm2AlmChannel40OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel40OosPortn.setStatus("current")
_Pmopm2Almchannel41PortTable_Object = MibTable
pmopm2Almchannel41PortTable = _Pmopm2Almchannel41PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel41PortTable.setStatus("current")
_Pmopm2Almchannel41PortEntry_Object = MibTableRow
pmopm2Almchannel41PortEntry = _Pmopm2Almchannel41PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1)
)
pmopm2Almchannel41PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel41PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel41PortEntry.setStatus("current")


class _Pmopm2Almchannel41PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel41PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel41PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel41PortIndex_Object = MibTableColumn
pmopm2Almchannel41PortIndex = _Pmopm2Almchannel41PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1, 1),
    _Pmopm2Almchannel41PortIndex_Type()
)
pmopm2Almchannel41PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel41PortIndex.setStatus("current")
_Pmopm2AlmChannel41AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel41AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel41AbsentPortn = _Pmopm2AlmChannel41AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1, 2),
    _Pmopm2AlmChannel41AbsentPortn_Type()
)
pmopm2AlmChannel41AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel41AbsentPortn.setStatus("current")
_Pmopm2AlmChannel41MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel41MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel41MismatchPortn = _Pmopm2AlmChannel41MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1, 3),
    _Pmopm2AlmChannel41MismatchPortn_Type()
)
pmopm2AlmChannel41MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel41MismatchPortn.setStatus("current")
_Pmopm2AlmChannel41BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel41BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel41BalancedPortn = _Pmopm2AlmChannel41BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1, 4),
    _Pmopm2AlmChannel41BalancedPortn_Type()
)
pmopm2AlmChannel41BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel41BalancedPortn.setStatus("current")
_Pmopm2AlmChannel41PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel41PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel41PowerLowPortn = _Pmopm2AlmChannel41PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1, 5),
    _Pmopm2AlmChannel41PowerLowPortn_Type()
)
pmopm2AlmChannel41PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel41PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel41PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel41PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel41PowerHighPortn = _Pmopm2AlmChannel41PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1, 6),
    _Pmopm2AlmChannel41PowerHighPortn_Type()
)
pmopm2AlmChannel41PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel41PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel41OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel41OosPortn_Object = MibTableColumn
pmopm2AlmChannel41OosPortn = _Pmopm2AlmChannel41OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 96, 1, 7),
    _Pmopm2AlmChannel41OosPortn_Type()
)
pmopm2AlmChannel41OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel41OosPortn.setStatus("current")
_Pmopm2Almchannel42PortTable_Object = MibTable
pmopm2Almchannel42PortTable = _Pmopm2Almchannel42PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel42PortTable.setStatus("current")
_Pmopm2Almchannel42PortEntry_Object = MibTableRow
pmopm2Almchannel42PortEntry = _Pmopm2Almchannel42PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1)
)
pmopm2Almchannel42PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel42PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel42PortEntry.setStatus("current")


class _Pmopm2Almchannel42PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel42PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel42PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel42PortIndex_Object = MibTableColumn
pmopm2Almchannel42PortIndex = _Pmopm2Almchannel42PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1, 1),
    _Pmopm2Almchannel42PortIndex_Type()
)
pmopm2Almchannel42PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel42PortIndex.setStatus("current")
_Pmopm2AlmChannel42AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel42AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel42AbsentPortn = _Pmopm2AlmChannel42AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1, 2),
    _Pmopm2AlmChannel42AbsentPortn_Type()
)
pmopm2AlmChannel42AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel42AbsentPortn.setStatus("current")
_Pmopm2AlmChannel42MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel42MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel42MismatchPortn = _Pmopm2AlmChannel42MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1, 3),
    _Pmopm2AlmChannel42MismatchPortn_Type()
)
pmopm2AlmChannel42MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel42MismatchPortn.setStatus("current")
_Pmopm2AlmChannel42BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel42BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel42BalancedPortn = _Pmopm2AlmChannel42BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1, 4),
    _Pmopm2AlmChannel42BalancedPortn_Type()
)
pmopm2AlmChannel42BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel42BalancedPortn.setStatus("current")
_Pmopm2AlmChannel42PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel42PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel42PowerLowPortn = _Pmopm2AlmChannel42PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1, 5),
    _Pmopm2AlmChannel42PowerLowPortn_Type()
)
pmopm2AlmChannel42PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel42PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel42PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel42PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel42PowerHighPortn = _Pmopm2AlmChannel42PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1, 6),
    _Pmopm2AlmChannel42PowerHighPortn_Type()
)
pmopm2AlmChannel42PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel42PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel42OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel42OosPortn_Object = MibTableColumn
pmopm2AlmChannel42OosPortn = _Pmopm2AlmChannel42OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 98, 1, 7),
    _Pmopm2AlmChannel42OosPortn_Type()
)
pmopm2AlmChannel42OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel42OosPortn.setStatus("current")
_Pmopm2Almchannel43PortTable_Object = MibTable
pmopm2Almchannel43PortTable = _Pmopm2Almchannel43PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel43PortTable.setStatus("current")
_Pmopm2Almchannel43PortEntry_Object = MibTableRow
pmopm2Almchannel43PortEntry = _Pmopm2Almchannel43PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1)
)
pmopm2Almchannel43PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel43PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel43PortEntry.setStatus("current")


class _Pmopm2Almchannel43PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel43PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel43PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel43PortIndex_Object = MibTableColumn
pmopm2Almchannel43PortIndex = _Pmopm2Almchannel43PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1, 1),
    _Pmopm2Almchannel43PortIndex_Type()
)
pmopm2Almchannel43PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel43PortIndex.setStatus("current")
_Pmopm2AlmChannel43AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel43AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel43AbsentPortn = _Pmopm2AlmChannel43AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1, 2),
    _Pmopm2AlmChannel43AbsentPortn_Type()
)
pmopm2AlmChannel43AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel43AbsentPortn.setStatus("current")
_Pmopm2AlmChannel43MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel43MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel43MismatchPortn = _Pmopm2AlmChannel43MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1, 3),
    _Pmopm2AlmChannel43MismatchPortn_Type()
)
pmopm2AlmChannel43MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel43MismatchPortn.setStatus("current")
_Pmopm2AlmChannel43BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel43BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel43BalancedPortn = _Pmopm2AlmChannel43BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1, 4),
    _Pmopm2AlmChannel43BalancedPortn_Type()
)
pmopm2AlmChannel43BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel43BalancedPortn.setStatus("current")
_Pmopm2AlmChannel43PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel43PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel43PowerLowPortn = _Pmopm2AlmChannel43PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1, 5),
    _Pmopm2AlmChannel43PowerLowPortn_Type()
)
pmopm2AlmChannel43PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel43PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel43PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel43PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel43PowerHighPortn = _Pmopm2AlmChannel43PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1, 6),
    _Pmopm2AlmChannel43PowerHighPortn_Type()
)
pmopm2AlmChannel43PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel43PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel43OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel43OosPortn_Object = MibTableColumn
pmopm2AlmChannel43OosPortn = _Pmopm2AlmChannel43OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 100, 1, 7),
    _Pmopm2AlmChannel43OosPortn_Type()
)
pmopm2AlmChannel43OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel43OosPortn.setStatus("current")
_Pmopm2Almchannel44PortTable_Object = MibTable
pmopm2Almchannel44PortTable = _Pmopm2Almchannel44PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel44PortTable.setStatus("current")
_Pmopm2Almchannel44PortEntry_Object = MibTableRow
pmopm2Almchannel44PortEntry = _Pmopm2Almchannel44PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1)
)
pmopm2Almchannel44PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel44PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel44PortEntry.setStatus("current")


class _Pmopm2Almchannel44PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel44PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel44PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel44PortIndex_Object = MibTableColumn
pmopm2Almchannel44PortIndex = _Pmopm2Almchannel44PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1, 1),
    _Pmopm2Almchannel44PortIndex_Type()
)
pmopm2Almchannel44PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel44PortIndex.setStatus("current")
_Pmopm2AlmChannel44AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel44AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel44AbsentPortn = _Pmopm2AlmChannel44AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1, 2),
    _Pmopm2AlmChannel44AbsentPortn_Type()
)
pmopm2AlmChannel44AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel44AbsentPortn.setStatus("current")
_Pmopm2AlmChannel44MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel44MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel44MismatchPortn = _Pmopm2AlmChannel44MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1, 3),
    _Pmopm2AlmChannel44MismatchPortn_Type()
)
pmopm2AlmChannel44MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel44MismatchPortn.setStatus("current")
_Pmopm2AlmChannel44BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel44BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel44BalancedPortn = _Pmopm2AlmChannel44BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1, 4),
    _Pmopm2AlmChannel44BalancedPortn_Type()
)
pmopm2AlmChannel44BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel44BalancedPortn.setStatus("current")
_Pmopm2AlmChannel44PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel44PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel44PowerLowPortn = _Pmopm2AlmChannel44PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1, 5),
    _Pmopm2AlmChannel44PowerLowPortn_Type()
)
pmopm2AlmChannel44PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel44PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel44PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel44PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel44PowerHighPortn = _Pmopm2AlmChannel44PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1, 6),
    _Pmopm2AlmChannel44PowerHighPortn_Type()
)
pmopm2AlmChannel44PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel44PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel44OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel44OosPortn_Object = MibTableColumn
pmopm2AlmChannel44OosPortn = _Pmopm2AlmChannel44OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 102, 1, 7),
    _Pmopm2AlmChannel44OosPortn_Type()
)
pmopm2AlmChannel44OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel44OosPortn.setStatus("current")
_Pmopm2Almchannel45PortTable_Object = MibTable
pmopm2Almchannel45PortTable = _Pmopm2Almchannel45PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel45PortTable.setStatus("current")
_Pmopm2Almchannel45PortEntry_Object = MibTableRow
pmopm2Almchannel45PortEntry = _Pmopm2Almchannel45PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1)
)
pmopm2Almchannel45PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel45PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel45PortEntry.setStatus("current")


class _Pmopm2Almchannel45PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel45PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel45PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel45PortIndex_Object = MibTableColumn
pmopm2Almchannel45PortIndex = _Pmopm2Almchannel45PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1, 1),
    _Pmopm2Almchannel45PortIndex_Type()
)
pmopm2Almchannel45PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel45PortIndex.setStatus("current")
_Pmopm2AlmChannel45AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel45AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel45AbsentPortn = _Pmopm2AlmChannel45AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1, 2),
    _Pmopm2AlmChannel45AbsentPortn_Type()
)
pmopm2AlmChannel45AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel45AbsentPortn.setStatus("current")
_Pmopm2AlmChannel45MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel45MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel45MismatchPortn = _Pmopm2AlmChannel45MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1, 3),
    _Pmopm2AlmChannel45MismatchPortn_Type()
)
pmopm2AlmChannel45MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel45MismatchPortn.setStatus("current")
_Pmopm2AlmChannel45BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel45BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel45BalancedPortn = _Pmopm2AlmChannel45BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1, 4),
    _Pmopm2AlmChannel45BalancedPortn_Type()
)
pmopm2AlmChannel45BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel45BalancedPortn.setStatus("current")
_Pmopm2AlmChannel45PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel45PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel45PowerLowPortn = _Pmopm2AlmChannel45PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1, 5),
    _Pmopm2AlmChannel45PowerLowPortn_Type()
)
pmopm2AlmChannel45PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel45PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel45PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel45PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel45PowerHighPortn = _Pmopm2AlmChannel45PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1, 6),
    _Pmopm2AlmChannel45PowerHighPortn_Type()
)
pmopm2AlmChannel45PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel45PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel45OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel45OosPortn_Object = MibTableColumn
pmopm2AlmChannel45OosPortn = _Pmopm2AlmChannel45OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 104, 1, 7),
    _Pmopm2AlmChannel45OosPortn_Type()
)
pmopm2AlmChannel45OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel45OosPortn.setStatus("current")
_Pmopm2Almchannel46PortTable_Object = MibTable
pmopm2Almchannel46PortTable = _Pmopm2Almchannel46PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel46PortTable.setStatus("current")
_Pmopm2Almchannel46PortEntry_Object = MibTableRow
pmopm2Almchannel46PortEntry = _Pmopm2Almchannel46PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1)
)
pmopm2Almchannel46PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel46PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel46PortEntry.setStatus("current")


class _Pmopm2Almchannel46PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel46PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel46PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel46PortIndex_Object = MibTableColumn
pmopm2Almchannel46PortIndex = _Pmopm2Almchannel46PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1, 1),
    _Pmopm2Almchannel46PortIndex_Type()
)
pmopm2Almchannel46PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel46PortIndex.setStatus("current")
_Pmopm2AlmChannel46AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel46AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel46AbsentPortn = _Pmopm2AlmChannel46AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1, 2),
    _Pmopm2AlmChannel46AbsentPortn_Type()
)
pmopm2AlmChannel46AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel46AbsentPortn.setStatus("current")
_Pmopm2AlmChannel46MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel46MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel46MismatchPortn = _Pmopm2AlmChannel46MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1, 3),
    _Pmopm2AlmChannel46MismatchPortn_Type()
)
pmopm2AlmChannel46MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel46MismatchPortn.setStatus("current")
_Pmopm2AlmChannel46BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel46BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel46BalancedPortn = _Pmopm2AlmChannel46BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1, 4),
    _Pmopm2AlmChannel46BalancedPortn_Type()
)
pmopm2AlmChannel46BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel46BalancedPortn.setStatus("current")
_Pmopm2AlmChannel46PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel46PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel46PowerLowPortn = _Pmopm2AlmChannel46PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1, 5),
    _Pmopm2AlmChannel46PowerLowPortn_Type()
)
pmopm2AlmChannel46PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel46PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel46PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel46PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel46PowerHighPortn = _Pmopm2AlmChannel46PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1, 6),
    _Pmopm2AlmChannel46PowerHighPortn_Type()
)
pmopm2AlmChannel46PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel46PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel46OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel46OosPortn_Object = MibTableColumn
pmopm2AlmChannel46OosPortn = _Pmopm2AlmChannel46OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 106, 1, 7),
    _Pmopm2AlmChannel46OosPortn_Type()
)
pmopm2AlmChannel46OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel46OosPortn.setStatus("current")
_Pmopm2Almchannel47PortTable_Object = MibTable
pmopm2Almchannel47PortTable = _Pmopm2Almchannel47PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel47PortTable.setStatus("current")
_Pmopm2Almchannel47PortEntry_Object = MibTableRow
pmopm2Almchannel47PortEntry = _Pmopm2Almchannel47PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1)
)
pmopm2Almchannel47PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel47PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel47PortEntry.setStatus("current")


class _Pmopm2Almchannel47PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel47PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel47PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel47PortIndex_Object = MibTableColumn
pmopm2Almchannel47PortIndex = _Pmopm2Almchannel47PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1, 1),
    _Pmopm2Almchannel47PortIndex_Type()
)
pmopm2Almchannel47PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel47PortIndex.setStatus("current")
_Pmopm2AlmChannel47AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel47AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel47AbsentPortn = _Pmopm2AlmChannel47AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1, 2),
    _Pmopm2AlmChannel47AbsentPortn_Type()
)
pmopm2AlmChannel47AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel47AbsentPortn.setStatus("current")
_Pmopm2AlmChannel47MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel47MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel47MismatchPortn = _Pmopm2AlmChannel47MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1, 3),
    _Pmopm2AlmChannel47MismatchPortn_Type()
)
pmopm2AlmChannel47MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel47MismatchPortn.setStatus("current")
_Pmopm2AlmChannel47BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel47BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel47BalancedPortn = _Pmopm2AlmChannel47BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1, 4),
    _Pmopm2AlmChannel47BalancedPortn_Type()
)
pmopm2AlmChannel47BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel47BalancedPortn.setStatus("current")
_Pmopm2AlmChannel47PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel47PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel47PowerLowPortn = _Pmopm2AlmChannel47PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1, 5),
    _Pmopm2AlmChannel47PowerLowPortn_Type()
)
pmopm2AlmChannel47PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel47PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel47PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel47PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel47PowerHighPortn = _Pmopm2AlmChannel47PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1, 6),
    _Pmopm2AlmChannel47PowerHighPortn_Type()
)
pmopm2AlmChannel47PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel47PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel47OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel47OosPortn_Object = MibTableColumn
pmopm2AlmChannel47OosPortn = _Pmopm2AlmChannel47OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 108, 1, 7),
    _Pmopm2AlmChannel47OosPortn_Type()
)
pmopm2AlmChannel47OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel47OosPortn.setStatus("current")
_Pmopm2Almchannel48PortTable_Object = MibTable
pmopm2Almchannel48PortTable = _Pmopm2Almchannel48PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel48PortTable.setStatus("current")
_Pmopm2Almchannel48PortEntry_Object = MibTableRow
pmopm2Almchannel48PortEntry = _Pmopm2Almchannel48PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1)
)
pmopm2Almchannel48PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel48PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel48PortEntry.setStatus("current")


class _Pmopm2Almchannel48PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel48PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel48PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel48PortIndex_Object = MibTableColumn
pmopm2Almchannel48PortIndex = _Pmopm2Almchannel48PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1, 1),
    _Pmopm2Almchannel48PortIndex_Type()
)
pmopm2Almchannel48PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel48PortIndex.setStatus("current")
_Pmopm2AlmChannel48AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel48AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel48AbsentPortn = _Pmopm2AlmChannel48AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1, 2),
    _Pmopm2AlmChannel48AbsentPortn_Type()
)
pmopm2AlmChannel48AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel48AbsentPortn.setStatus("current")
_Pmopm2AlmChannel48MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel48MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel48MismatchPortn = _Pmopm2AlmChannel48MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1, 3),
    _Pmopm2AlmChannel48MismatchPortn_Type()
)
pmopm2AlmChannel48MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel48MismatchPortn.setStatus("current")
_Pmopm2AlmChannel48BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel48BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel48BalancedPortn = _Pmopm2AlmChannel48BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1, 4),
    _Pmopm2AlmChannel48BalancedPortn_Type()
)
pmopm2AlmChannel48BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel48BalancedPortn.setStatus("current")
_Pmopm2AlmChannel48PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel48PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel48PowerLowPortn = _Pmopm2AlmChannel48PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1, 5),
    _Pmopm2AlmChannel48PowerLowPortn_Type()
)
pmopm2AlmChannel48PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel48PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel48PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel48PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel48PowerHighPortn = _Pmopm2AlmChannel48PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1, 6),
    _Pmopm2AlmChannel48PowerHighPortn_Type()
)
pmopm2AlmChannel48PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel48PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel48OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel48OosPortn_Object = MibTableColumn
pmopm2AlmChannel48OosPortn = _Pmopm2AlmChannel48OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 110, 1, 7),
    _Pmopm2AlmChannel48OosPortn_Type()
)
pmopm2AlmChannel48OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel48OosPortn.setStatus("current")
_Pmopm2Almchannel49PortTable_Object = MibTable
pmopm2Almchannel49PortTable = _Pmopm2Almchannel49PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel49PortTable.setStatus("current")
_Pmopm2Almchannel49PortEntry_Object = MibTableRow
pmopm2Almchannel49PortEntry = _Pmopm2Almchannel49PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1)
)
pmopm2Almchannel49PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel49PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel49PortEntry.setStatus("current")


class _Pmopm2Almchannel49PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel49PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel49PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel49PortIndex_Object = MibTableColumn
pmopm2Almchannel49PortIndex = _Pmopm2Almchannel49PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1, 1),
    _Pmopm2Almchannel49PortIndex_Type()
)
pmopm2Almchannel49PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel49PortIndex.setStatus("current")
_Pmopm2AlmChannel49AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel49AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel49AbsentPortn = _Pmopm2AlmChannel49AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1, 2),
    _Pmopm2AlmChannel49AbsentPortn_Type()
)
pmopm2AlmChannel49AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel49AbsentPortn.setStatus("current")
_Pmopm2AlmChannel49MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel49MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel49MismatchPortn = _Pmopm2AlmChannel49MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1, 3),
    _Pmopm2AlmChannel49MismatchPortn_Type()
)
pmopm2AlmChannel49MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel49MismatchPortn.setStatus("current")
_Pmopm2AlmChannel49BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel49BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel49BalancedPortn = _Pmopm2AlmChannel49BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1, 4),
    _Pmopm2AlmChannel49BalancedPortn_Type()
)
pmopm2AlmChannel49BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel49BalancedPortn.setStatus("current")
_Pmopm2AlmChannel49PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel49PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel49PowerLowPortn = _Pmopm2AlmChannel49PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1, 5),
    _Pmopm2AlmChannel49PowerLowPortn_Type()
)
pmopm2AlmChannel49PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel49PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel49PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel49PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel49PowerHighPortn = _Pmopm2AlmChannel49PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1, 6),
    _Pmopm2AlmChannel49PowerHighPortn_Type()
)
pmopm2AlmChannel49PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel49PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel49OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel49OosPortn_Object = MibTableColumn
pmopm2AlmChannel49OosPortn = _Pmopm2AlmChannel49OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 112, 1, 7),
    _Pmopm2AlmChannel49OosPortn_Type()
)
pmopm2AlmChannel49OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel49OosPortn.setStatus("current")
_Pmopm2Almchannel50PortTable_Object = MibTable
pmopm2Almchannel50PortTable = _Pmopm2Almchannel50PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel50PortTable.setStatus("current")
_Pmopm2Almchannel50PortEntry_Object = MibTableRow
pmopm2Almchannel50PortEntry = _Pmopm2Almchannel50PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1)
)
pmopm2Almchannel50PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel50PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel50PortEntry.setStatus("current")


class _Pmopm2Almchannel50PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel50PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel50PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel50PortIndex_Object = MibTableColumn
pmopm2Almchannel50PortIndex = _Pmopm2Almchannel50PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1, 1),
    _Pmopm2Almchannel50PortIndex_Type()
)
pmopm2Almchannel50PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel50PortIndex.setStatus("current")
_Pmopm2AlmChannel50AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel50AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel50AbsentPortn = _Pmopm2AlmChannel50AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1, 2),
    _Pmopm2AlmChannel50AbsentPortn_Type()
)
pmopm2AlmChannel50AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel50AbsentPortn.setStatus("current")
_Pmopm2AlmChannel50MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel50MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel50MismatchPortn = _Pmopm2AlmChannel50MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1, 3),
    _Pmopm2AlmChannel50MismatchPortn_Type()
)
pmopm2AlmChannel50MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel50MismatchPortn.setStatus("current")
_Pmopm2AlmChannel50BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel50BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel50BalancedPortn = _Pmopm2AlmChannel50BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1, 4),
    _Pmopm2AlmChannel50BalancedPortn_Type()
)
pmopm2AlmChannel50BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel50BalancedPortn.setStatus("current")
_Pmopm2AlmChannel50PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel50PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel50PowerLowPortn = _Pmopm2AlmChannel50PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1, 5),
    _Pmopm2AlmChannel50PowerLowPortn_Type()
)
pmopm2AlmChannel50PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel50PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel50PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel50PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel50PowerHighPortn = _Pmopm2AlmChannel50PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1, 6),
    _Pmopm2AlmChannel50PowerHighPortn_Type()
)
pmopm2AlmChannel50PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel50PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel50OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel50OosPortn_Object = MibTableColumn
pmopm2AlmChannel50OosPortn = _Pmopm2AlmChannel50OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 114, 1, 7),
    _Pmopm2AlmChannel50OosPortn_Type()
)
pmopm2AlmChannel50OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel50OosPortn.setStatus("current")
_Pmopm2Almchannel51PortTable_Object = MibTable
pmopm2Almchannel51PortTable = _Pmopm2Almchannel51PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel51PortTable.setStatus("current")
_Pmopm2Almchannel51PortEntry_Object = MibTableRow
pmopm2Almchannel51PortEntry = _Pmopm2Almchannel51PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1)
)
pmopm2Almchannel51PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel51PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel51PortEntry.setStatus("current")


class _Pmopm2Almchannel51PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel51PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel51PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel51PortIndex_Object = MibTableColumn
pmopm2Almchannel51PortIndex = _Pmopm2Almchannel51PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1, 1),
    _Pmopm2Almchannel51PortIndex_Type()
)
pmopm2Almchannel51PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel51PortIndex.setStatus("current")
_Pmopm2AlmChannel51AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel51AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel51AbsentPortn = _Pmopm2AlmChannel51AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1, 2),
    _Pmopm2AlmChannel51AbsentPortn_Type()
)
pmopm2AlmChannel51AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel51AbsentPortn.setStatus("current")
_Pmopm2AlmChannel51MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel51MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel51MismatchPortn = _Pmopm2AlmChannel51MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1, 3),
    _Pmopm2AlmChannel51MismatchPortn_Type()
)
pmopm2AlmChannel51MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel51MismatchPortn.setStatus("current")
_Pmopm2AlmChannel51BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel51BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel51BalancedPortn = _Pmopm2AlmChannel51BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1, 4),
    _Pmopm2AlmChannel51BalancedPortn_Type()
)
pmopm2AlmChannel51BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel51BalancedPortn.setStatus("current")
_Pmopm2AlmChannel51PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel51PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel51PowerLowPortn = _Pmopm2AlmChannel51PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1, 5),
    _Pmopm2AlmChannel51PowerLowPortn_Type()
)
pmopm2AlmChannel51PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel51PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel51PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel51PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel51PowerHighPortn = _Pmopm2AlmChannel51PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1, 6),
    _Pmopm2AlmChannel51PowerHighPortn_Type()
)
pmopm2AlmChannel51PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel51PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel51OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel51OosPortn_Object = MibTableColumn
pmopm2AlmChannel51OosPortn = _Pmopm2AlmChannel51OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 116, 1, 7),
    _Pmopm2AlmChannel51OosPortn_Type()
)
pmopm2AlmChannel51OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel51OosPortn.setStatus("current")
_Pmopm2Almchannel52PortTable_Object = MibTable
pmopm2Almchannel52PortTable = _Pmopm2Almchannel52PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel52PortTable.setStatus("current")
_Pmopm2Almchannel52PortEntry_Object = MibTableRow
pmopm2Almchannel52PortEntry = _Pmopm2Almchannel52PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1)
)
pmopm2Almchannel52PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel52PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel52PortEntry.setStatus("current")


class _Pmopm2Almchannel52PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel52PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel52PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel52PortIndex_Object = MibTableColumn
pmopm2Almchannel52PortIndex = _Pmopm2Almchannel52PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1, 1),
    _Pmopm2Almchannel52PortIndex_Type()
)
pmopm2Almchannel52PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel52PortIndex.setStatus("current")
_Pmopm2AlmChannel52AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel52AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel52AbsentPortn = _Pmopm2AlmChannel52AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1, 2),
    _Pmopm2AlmChannel52AbsentPortn_Type()
)
pmopm2AlmChannel52AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel52AbsentPortn.setStatus("current")
_Pmopm2AlmChannel52MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel52MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel52MismatchPortn = _Pmopm2AlmChannel52MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1, 3),
    _Pmopm2AlmChannel52MismatchPortn_Type()
)
pmopm2AlmChannel52MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel52MismatchPortn.setStatus("current")
_Pmopm2AlmChannel52BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel52BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel52BalancedPortn = _Pmopm2AlmChannel52BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1, 4),
    _Pmopm2AlmChannel52BalancedPortn_Type()
)
pmopm2AlmChannel52BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel52BalancedPortn.setStatus("current")
_Pmopm2AlmChannel52PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel52PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel52PowerLowPortn = _Pmopm2AlmChannel52PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1, 5),
    _Pmopm2AlmChannel52PowerLowPortn_Type()
)
pmopm2AlmChannel52PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel52PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel52PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel52PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel52PowerHighPortn = _Pmopm2AlmChannel52PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1, 6),
    _Pmopm2AlmChannel52PowerHighPortn_Type()
)
pmopm2AlmChannel52PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel52PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel52OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel52OosPortn_Object = MibTableColumn
pmopm2AlmChannel52OosPortn = _Pmopm2AlmChannel52OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 118, 1, 7),
    _Pmopm2AlmChannel52OosPortn_Type()
)
pmopm2AlmChannel52OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel52OosPortn.setStatus("current")
_Pmopm2Almchannel53PortTable_Object = MibTable
pmopm2Almchannel53PortTable = _Pmopm2Almchannel53PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel53PortTable.setStatus("current")
_Pmopm2Almchannel53PortEntry_Object = MibTableRow
pmopm2Almchannel53PortEntry = _Pmopm2Almchannel53PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1)
)
pmopm2Almchannel53PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel53PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel53PortEntry.setStatus("current")


class _Pmopm2Almchannel53PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel53PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel53PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel53PortIndex_Object = MibTableColumn
pmopm2Almchannel53PortIndex = _Pmopm2Almchannel53PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1, 1),
    _Pmopm2Almchannel53PortIndex_Type()
)
pmopm2Almchannel53PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel53PortIndex.setStatus("current")
_Pmopm2AlmChannel53AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel53AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel53AbsentPortn = _Pmopm2AlmChannel53AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1, 2),
    _Pmopm2AlmChannel53AbsentPortn_Type()
)
pmopm2AlmChannel53AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel53AbsentPortn.setStatus("current")
_Pmopm2AlmChannel53MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel53MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel53MismatchPortn = _Pmopm2AlmChannel53MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1, 3),
    _Pmopm2AlmChannel53MismatchPortn_Type()
)
pmopm2AlmChannel53MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel53MismatchPortn.setStatus("current")
_Pmopm2AlmChannel53BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel53BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel53BalancedPortn = _Pmopm2AlmChannel53BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1, 4),
    _Pmopm2AlmChannel53BalancedPortn_Type()
)
pmopm2AlmChannel53BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel53BalancedPortn.setStatus("current")
_Pmopm2AlmChannel53PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel53PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel53PowerLowPortn = _Pmopm2AlmChannel53PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1, 5),
    _Pmopm2AlmChannel53PowerLowPortn_Type()
)
pmopm2AlmChannel53PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel53PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel53PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel53PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel53PowerHighPortn = _Pmopm2AlmChannel53PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1, 6),
    _Pmopm2AlmChannel53PowerHighPortn_Type()
)
pmopm2AlmChannel53PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel53PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel53OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel53OosPortn_Object = MibTableColumn
pmopm2AlmChannel53OosPortn = _Pmopm2AlmChannel53OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 120, 1, 7),
    _Pmopm2AlmChannel53OosPortn_Type()
)
pmopm2AlmChannel53OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel53OosPortn.setStatus("current")
_Pmopm2Almchannel54PortTable_Object = MibTable
pmopm2Almchannel54PortTable = _Pmopm2Almchannel54PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel54PortTable.setStatus("current")
_Pmopm2Almchannel54PortEntry_Object = MibTableRow
pmopm2Almchannel54PortEntry = _Pmopm2Almchannel54PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1)
)
pmopm2Almchannel54PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel54PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel54PortEntry.setStatus("current")


class _Pmopm2Almchannel54PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel54PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel54PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel54PortIndex_Object = MibTableColumn
pmopm2Almchannel54PortIndex = _Pmopm2Almchannel54PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1, 1),
    _Pmopm2Almchannel54PortIndex_Type()
)
pmopm2Almchannel54PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel54PortIndex.setStatus("current")
_Pmopm2AlmChannel54AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel54AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel54AbsentPortn = _Pmopm2AlmChannel54AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1, 2),
    _Pmopm2AlmChannel54AbsentPortn_Type()
)
pmopm2AlmChannel54AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel54AbsentPortn.setStatus("current")
_Pmopm2AlmChannel54MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel54MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel54MismatchPortn = _Pmopm2AlmChannel54MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1, 3),
    _Pmopm2AlmChannel54MismatchPortn_Type()
)
pmopm2AlmChannel54MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel54MismatchPortn.setStatus("current")
_Pmopm2AlmChannel54BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel54BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel54BalancedPortn = _Pmopm2AlmChannel54BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1, 4),
    _Pmopm2AlmChannel54BalancedPortn_Type()
)
pmopm2AlmChannel54BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel54BalancedPortn.setStatus("current")
_Pmopm2AlmChannel54PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel54PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel54PowerLowPortn = _Pmopm2AlmChannel54PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1, 5),
    _Pmopm2AlmChannel54PowerLowPortn_Type()
)
pmopm2AlmChannel54PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel54PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel54PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel54PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel54PowerHighPortn = _Pmopm2AlmChannel54PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1, 6),
    _Pmopm2AlmChannel54PowerHighPortn_Type()
)
pmopm2AlmChannel54PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel54PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel54OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel54OosPortn_Object = MibTableColumn
pmopm2AlmChannel54OosPortn = _Pmopm2AlmChannel54OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 122, 1, 7),
    _Pmopm2AlmChannel54OosPortn_Type()
)
pmopm2AlmChannel54OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel54OosPortn.setStatus("current")
_Pmopm2Almchannel55PortTable_Object = MibTable
pmopm2Almchannel55PortTable = _Pmopm2Almchannel55PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel55PortTable.setStatus("current")
_Pmopm2Almchannel55PortEntry_Object = MibTableRow
pmopm2Almchannel55PortEntry = _Pmopm2Almchannel55PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1)
)
pmopm2Almchannel55PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel55PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel55PortEntry.setStatus("current")


class _Pmopm2Almchannel55PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel55PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel55PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel55PortIndex_Object = MibTableColumn
pmopm2Almchannel55PortIndex = _Pmopm2Almchannel55PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1, 1),
    _Pmopm2Almchannel55PortIndex_Type()
)
pmopm2Almchannel55PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel55PortIndex.setStatus("current")
_Pmopm2AlmChannel55AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel55AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel55AbsentPortn = _Pmopm2AlmChannel55AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1, 2),
    _Pmopm2AlmChannel55AbsentPortn_Type()
)
pmopm2AlmChannel55AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel55AbsentPortn.setStatus("current")
_Pmopm2AlmChannel55MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel55MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel55MismatchPortn = _Pmopm2AlmChannel55MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1, 3),
    _Pmopm2AlmChannel55MismatchPortn_Type()
)
pmopm2AlmChannel55MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel55MismatchPortn.setStatus("current")
_Pmopm2AlmChannel55BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel55BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel55BalancedPortn = _Pmopm2AlmChannel55BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1, 4),
    _Pmopm2AlmChannel55BalancedPortn_Type()
)
pmopm2AlmChannel55BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel55BalancedPortn.setStatus("current")
_Pmopm2AlmChannel55PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel55PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel55PowerLowPortn = _Pmopm2AlmChannel55PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1, 5),
    _Pmopm2AlmChannel55PowerLowPortn_Type()
)
pmopm2AlmChannel55PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel55PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel55PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel55PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel55PowerHighPortn = _Pmopm2AlmChannel55PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1, 6),
    _Pmopm2AlmChannel55PowerHighPortn_Type()
)
pmopm2AlmChannel55PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel55PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel55OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel55OosPortn_Object = MibTableColumn
pmopm2AlmChannel55OosPortn = _Pmopm2AlmChannel55OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 124, 1, 7),
    _Pmopm2AlmChannel55OosPortn_Type()
)
pmopm2AlmChannel55OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel55OosPortn.setStatus("current")
_Pmopm2Almchannel56PortTable_Object = MibTable
pmopm2Almchannel56PortTable = _Pmopm2Almchannel56PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel56PortTable.setStatus("current")
_Pmopm2Almchannel56PortEntry_Object = MibTableRow
pmopm2Almchannel56PortEntry = _Pmopm2Almchannel56PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1)
)
pmopm2Almchannel56PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel56PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel56PortEntry.setStatus("current")


class _Pmopm2Almchannel56PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel56PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel56PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel56PortIndex_Object = MibTableColumn
pmopm2Almchannel56PortIndex = _Pmopm2Almchannel56PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1, 1),
    _Pmopm2Almchannel56PortIndex_Type()
)
pmopm2Almchannel56PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel56PortIndex.setStatus("current")
_Pmopm2AlmChannel56AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel56AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel56AbsentPortn = _Pmopm2AlmChannel56AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1, 2),
    _Pmopm2AlmChannel56AbsentPortn_Type()
)
pmopm2AlmChannel56AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel56AbsentPortn.setStatus("current")
_Pmopm2AlmChannel56MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel56MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel56MismatchPortn = _Pmopm2AlmChannel56MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1, 3),
    _Pmopm2AlmChannel56MismatchPortn_Type()
)
pmopm2AlmChannel56MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel56MismatchPortn.setStatus("current")
_Pmopm2AlmChannel56BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel56BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel56BalancedPortn = _Pmopm2AlmChannel56BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1, 4),
    _Pmopm2AlmChannel56BalancedPortn_Type()
)
pmopm2AlmChannel56BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel56BalancedPortn.setStatus("current")
_Pmopm2AlmChannel56PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel56PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel56PowerLowPortn = _Pmopm2AlmChannel56PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1, 5),
    _Pmopm2AlmChannel56PowerLowPortn_Type()
)
pmopm2AlmChannel56PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel56PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel56PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel56PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel56PowerHighPortn = _Pmopm2AlmChannel56PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1, 6),
    _Pmopm2AlmChannel56PowerHighPortn_Type()
)
pmopm2AlmChannel56PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel56PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel56OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel56OosPortn_Object = MibTableColumn
pmopm2AlmChannel56OosPortn = _Pmopm2AlmChannel56OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 126, 1, 7),
    _Pmopm2AlmChannel56OosPortn_Type()
)
pmopm2AlmChannel56OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel56OosPortn.setStatus("current")
_Pmopm2Almchannel57PortTable_Object = MibTable
pmopm2Almchannel57PortTable = _Pmopm2Almchannel57PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel57PortTable.setStatus("current")
_Pmopm2Almchannel57PortEntry_Object = MibTableRow
pmopm2Almchannel57PortEntry = _Pmopm2Almchannel57PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1)
)
pmopm2Almchannel57PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel57PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel57PortEntry.setStatus("current")


class _Pmopm2Almchannel57PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel57PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel57PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel57PortIndex_Object = MibTableColumn
pmopm2Almchannel57PortIndex = _Pmopm2Almchannel57PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1, 1),
    _Pmopm2Almchannel57PortIndex_Type()
)
pmopm2Almchannel57PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel57PortIndex.setStatus("current")
_Pmopm2AlmChannel57AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel57AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel57AbsentPortn = _Pmopm2AlmChannel57AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1, 2),
    _Pmopm2AlmChannel57AbsentPortn_Type()
)
pmopm2AlmChannel57AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel57AbsentPortn.setStatus("current")
_Pmopm2AlmChannel57MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel57MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel57MismatchPortn = _Pmopm2AlmChannel57MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1, 3),
    _Pmopm2AlmChannel57MismatchPortn_Type()
)
pmopm2AlmChannel57MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel57MismatchPortn.setStatus("current")
_Pmopm2AlmChannel57BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel57BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel57BalancedPortn = _Pmopm2AlmChannel57BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1, 4),
    _Pmopm2AlmChannel57BalancedPortn_Type()
)
pmopm2AlmChannel57BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel57BalancedPortn.setStatus("current")
_Pmopm2AlmChannel57PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel57PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel57PowerLowPortn = _Pmopm2AlmChannel57PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1, 5),
    _Pmopm2AlmChannel57PowerLowPortn_Type()
)
pmopm2AlmChannel57PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel57PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel57PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel57PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel57PowerHighPortn = _Pmopm2AlmChannel57PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1, 6),
    _Pmopm2AlmChannel57PowerHighPortn_Type()
)
pmopm2AlmChannel57PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel57PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel57OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel57OosPortn_Object = MibTableColumn
pmopm2AlmChannel57OosPortn = _Pmopm2AlmChannel57OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 128, 1, 7),
    _Pmopm2AlmChannel57OosPortn_Type()
)
pmopm2AlmChannel57OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel57OosPortn.setStatus("current")
_Pmopm2Almchannel58PortTable_Object = MibTable
pmopm2Almchannel58PortTable = _Pmopm2Almchannel58PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel58PortTable.setStatus("current")
_Pmopm2Almchannel58PortEntry_Object = MibTableRow
pmopm2Almchannel58PortEntry = _Pmopm2Almchannel58PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1)
)
pmopm2Almchannel58PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel58PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel58PortEntry.setStatus("current")


class _Pmopm2Almchannel58PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel58PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel58PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel58PortIndex_Object = MibTableColumn
pmopm2Almchannel58PortIndex = _Pmopm2Almchannel58PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1, 1),
    _Pmopm2Almchannel58PortIndex_Type()
)
pmopm2Almchannel58PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel58PortIndex.setStatus("current")
_Pmopm2AlmChannel58AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel58AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel58AbsentPortn = _Pmopm2AlmChannel58AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1, 2),
    _Pmopm2AlmChannel58AbsentPortn_Type()
)
pmopm2AlmChannel58AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel58AbsentPortn.setStatus("current")
_Pmopm2AlmChannel58MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel58MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel58MismatchPortn = _Pmopm2AlmChannel58MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1, 3),
    _Pmopm2AlmChannel58MismatchPortn_Type()
)
pmopm2AlmChannel58MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel58MismatchPortn.setStatus("current")
_Pmopm2AlmChannel58BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel58BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel58BalancedPortn = _Pmopm2AlmChannel58BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1, 4),
    _Pmopm2AlmChannel58BalancedPortn_Type()
)
pmopm2AlmChannel58BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel58BalancedPortn.setStatus("current")
_Pmopm2AlmChannel58PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel58PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel58PowerLowPortn = _Pmopm2AlmChannel58PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1, 5),
    _Pmopm2AlmChannel58PowerLowPortn_Type()
)
pmopm2AlmChannel58PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel58PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel58PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel58PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel58PowerHighPortn = _Pmopm2AlmChannel58PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1, 6),
    _Pmopm2AlmChannel58PowerHighPortn_Type()
)
pmopm2AlmChannel58PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel58PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel58OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel58OosPortn_Object = MibTableColumn
pmopm2AlmChannel58OosPortn = _Pmopm2AlmChannel58OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 130, 1, 7),
    _Pmopm2AlmChannel58OosPortn_Type()
)
pmopm2AlmChannel58OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel58OosPortn.setStatus("current")
_Pmopm2Almchannel59PortTable_Object = MibTable
pmopm2Almchannel59PortTable = _Pmopm2Almchannel59PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel59PortTable.setStatus("current")
_Pmopm2Almchannel59PortEntry_Object = MibTableRow
pmopm2Almchannel59PortEntry = _Pmopm2Almchannel59PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1)
)
pmopm2Almchannel59PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel59PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel59PortEntry.setStatus("current")


class _Pmopm2Almchannel59PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel59PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel59PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel59PortIndex_Object = MibTableColumn
pmopm2Almchannel59PortIndex = _Pmopm2Almchannel59PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1, 1),
    _Pmopm2Almchannel59PortIndex_Type()
)
pmopm2Almchannel59PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel59PortIndex.setStatus("current")
_Pmopm2AlmChannel59AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel59AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel59AbsentPortn = _Pmopm2AlmChannel59AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1, 2),
    _Pmopm2AlmChannel59AbsentPortn_Type()
)
pmopm2AlmChannel59AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel59AbsentPortn.setStatus("current")
_Pmopm2AlmChannel59MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel59MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel59MismatchPortn = _Pmopm2AlmChannel59MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1, 3),
    _Pmopm2AlmChannel59MismatchPortn_Type()
)
pmopm2AlmChannel59MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel59MismatchPortn.setStatus("current")
_Pmopm2AlmChannel59BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel59BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel59BalancedPortn = _Pmopm2AlmChannel59BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1, 4),
    _Pmopm2AlmChannel59BalancedPortn_Type()
)
pmopm2AlmChannel59BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel59BalancedPortn.setStatus("current")
_Pmopm2AlmChannel59PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel59PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel59PowerLowPortn = _Pmopm2AlmChannel59PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1, 5),
    _Pmopm2AlmChannel59PowerLowPortn_Type()
)
pmopm2AlmChannel59PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel59PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel59PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel59PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel59PowerHighPortn = _Pmopm2AlmChannel59PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1, 6),
    _Pmopm2AlmChannel59PowerHighPortn_Type()
)
pmopm2AlmChannel59PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel59PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel59OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel59OosPortn_Object = MibTableColumn
pmopm2AlmChannel59OosPortn = _Pmopm2AlmChannel59OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 132, 1, 7),
    _Pmopm2AlmChannel59OosPortn_Type()
)
pmopm2AlmChannel59OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel59OosPortn.setStatus("current")
_Pmopm2Almchannel60PortTable_Object = MibTable
pmopm2Almchannel60PortTable = _Pmopm2Almchannel60PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel60PortTable.setStatus("current")
_Pmopm2Almchannel60PortEntry_Object = MibTableRow
pmopm2Almchannel60PortEntry = _Pmopm2Almchannel60PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1)
)
pmopm2Almchannel60PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel60PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel60PortEntry.setStatus("current")


class _Pmopm2Almchannel60PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel60PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel60PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel60PortIndex_Object = MibTableColumn
pmopm2Almchannel60PortIndex = _Pmopm2Almchannel60PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1, 1),
    _Pmopm2Almchannel60PortIndex_Type()
)
pmopm2Almchannel60PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel60PortIndex.setStatus("current")
_Pmopm2AlmChannel60AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel60AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel60AbsentPortn = _Pmopm2AlmChannel60AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1, 2),
    _Pmopm2AlmChannel60AbsentPortn_Type()
)
pmopm2AlmChannel60AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel60AbsentPortn.setStatus("current")
_Pmopm2AlmChannel60MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel60MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel60MismatchPortn = _Pmopm2AlmChannel60MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1, 3),
    _Pmopm2AlmChannel60MismatchPortn_Type()
)
pmopm2AlmChannel60MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel60MismatchPortn.setStatus("current")
_Pmopm2AlmChannel60BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel60BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel60BalancedPortn = _Pmopm2AlmChannel60BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1, 4),
    _Pmopm2AlmChannel60BalancedPortn_Type()
)
pmopm2AlmChannel60BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel60BalancedPortn.setStatus("current")
_Pmopm2AlmChannel60PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel60PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel60PowerLowPortn = _Pmopm2AlmChannel60PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1, 5),
    _Pmopm2AlmChannel60PowerLowPortn_Type()
)
pmopm2AlmChannel60PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel60PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel60PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel60PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel60PowerHighPortn = _Pmopm2AlmChannel60PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1, 6),
    _Pmopm2AlmChannel60PowerHighPortn_Type()
)
pmopm2AlmChannel60PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel60PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel60OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel60OosPortn_Object = MibTableColumn
pmopm2AlmChannel60OosPortn = _Pmopm2AlmChannel60OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 134, 1, 7),
    _Pmopm2AlmChannel60OosPortn_Type()
)
pmopm2AlmChannel60OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel60OosPortn.setStatus("current")
_Pmopm2Almchannel61PortTable_Object = MibTable
pmopm2Almchannel61PortTable = _Pmopm2Almchannel61PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel61PortTable.setStatus("current")
_Pmopm2Almchannel61PortEntry_Object = MibTableRow
pmopm2Almchannel61PortEntry = _Pmopm2Almchannel61PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1)
)
pmopm2Almchannel61PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel61PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel61PortEntry.setStatus("current")


class _Pmopm2Almchannel61PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel61PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel61PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel61PortIndex_Object = MibTableColumn
pmopm2Almchannel61PortIndex = _Pmopm2Almchannel61PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1, 1),
    _Pmopm2Almchannel61PortIndex_Type()
)
pmopm2Almchannel61PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel61PortIndex.setStatus("current")
_Pmopm2AlmChannel61AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel61AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel61AbsentPortn = _Pmopm2AlmChannel61AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1, 2),
    _Pmopm2AlmChannel61AbsentPortn_Type()
)
pmopm2AlmChannel61AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel61AbsentPortn.setStatus("current")
_Pmopm2AlmChannel61MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel61MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel61MismatchPortn = _Pmopm2AlmChannel61MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1, 3),
    _Pmopm2AlmChannel61MismatchPortn_Type()
)
pmopm2AlmChannel61MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel61MismatchPortn.setStatus("current")
_Pmopm2AlmChannel61BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel61BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel61BalancedPortn = _Pmopm2AlmChannel61BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1, 4),
    _Pmopm2AlmChannel61BalancedPortn_Type()
)
pmopm2AlmChannel61BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel61BalancedPortn.setStatus("current")
_Pmopm2AlmChannel61PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel61PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel61PowerLowPortn = _Pmopm2AlmChannel61PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1, 5),
    _Pmopm2AlmChannel61PowerLowPortn_Type()
)
pmopm2AlmChannel61PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel61PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel61PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel61PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel61PowerHighPortn = _Pmopm2AlmChannel61PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1, 6),
    _Pmopm2AlmChannel61PowerHighPortn_Type()
)
pmopm2AlmChannel61PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel61PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel61OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel61OosPortn_Object = MibTableColumn
pmopm2AlmChannel61OosPortn = _Pmopm2AlmChannel61OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 136, 1, 7),
    _Pmopm2AlmChannel61OosPortn_Type()
)
pmopm2AlmChannel61OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel61OosPortn.setStatus("current")
_Pmopm2Almchannel62PortTable_Object = MibTable
pmopm2Almchannel62PortTable = _Pmopm2Almchannel62PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel62PortTable.setStatus("current")
_Pmopm2Almchannel62PortEntry_Object = MibTableRow
pmopm2Almchannel62PortEntry = _Pmopm2Almchannel62PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1)
)
pmopm2Almchannel62PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel62PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel62PortEntry.setStatus("current")


class _Pmopm2Almchannel62PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel62PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel62PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel62PortIndex_Object = MibTableColumn
pmopm2Almchannel62PortIndex = _Pmopm2Almchannel62PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1, 1),
    _Pmopm2Almchannel62PortIndex_Type()
)
pmopm2Almchannel62PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel62PortIndex.setStatus("current")
_Pmopm2AlmChannel62AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel62AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel62AbsentPortn = _Pmopm2AlmChannel62AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1, 2),
    _Pmopm2AlmChannel62AbsentPortn_Type()
)
pmopm2AlmChannel62AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel62AbsentPortn.setStatus("current")
_Pmopm2AlmChannel62MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel62MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel62MismatchPortn = _Pmopm2AlmChannel62MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1, 3),
    _Pmopm2AlmChannel62MismatchPortn_Type()
)
pmopm2AlmChannel62MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel62MismatchPortn.setStatus("current")
_Pmopm2AlmChannel62BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel62BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel62BalancedPortn = _Pmopm2AlmChannel62BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1, 4),
    _Pmopm2AlmChannel62BalancedPortn_Type()
)
pmopm2AlmChannel62BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel62BalancedPortn.setStatus("current")
_Pmopm2AlmChannel62PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel62PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel62PowerLowPortn = _Pmopm2AlmChannel62PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1, 5),
    _Pmopm2AlmChannel62PowerLowPortn_Type()
)
pmopm2AlmChannel62PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel62PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel62PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel62PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel62PowerHighPortn = _Pmopm2AlmChannel62PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1, 6),
    _Pmopm2AlmChannel62PowerHighPortn_Type()
)
pmopm2AlmChannel62PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel62PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel62OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel62OosPortn_Object = MibTableColumn
pmopm2AlmChannel62OosPortn = _Pmopm2AlmChannel62OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 138, 1, 7),
    _Pmopm2AlmChannel62OosPortn_Type()
)
pmopm2AlmChannel62OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel62OosPortn.setStatus("current")
_Pmopm2Almchannel63PortTable_Object = MibTable
pmopm2Almchannel63PortTable = _Pmopm2Almchannel63PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel63PortTable.setStatus("current")
_Pmopm2Almchannel63PortEntry_Object = MibTableRow
pmopm2Almchannel63PortEntry = _Pmopm2Almchannel63PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1)
)
pmopm2Almchannel63PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel63PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel63PortEntry.setStatus("current")


class _Pmopm2Almchannel63PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel63PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel63PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel63PortIndex_Object = MibTableColumn
pmopm2Almchannel63PortIndex = _Pmopm2Almchannel63PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1, 1),
    _Pmopm2Almchannel63PortIndex_Type()
)
pmopm2Almchannel63PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel63PortIndex.setStatus("current")
_Pmopm2AlmChannel63AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel63AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel63AbsentPortn = _Pmopm2AlmChannel63AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1, 2),
    _Pmopm2AlmChannel63AbsentPortn_Type()
)
pmopm2AlmChannel63AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel63AbsentPortn.setStatus("current")
_Pmopm2AlmChannel63MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel63MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel63MismatchPortn = _Pmopm2AlmChannel63MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1, 3),
    _Pmopm2AlmChannel63MismatchPortn_Type()
)
pmopm2AlmChannel63MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel63MismatchPortn.setStatus("current")
_Pmopm2AlmChannel63BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel63BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel63BalancedPortn = _Pmopm2AlmChannel63BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1, 4),
    _Pmopm2AlmChannel63BalancedPortn_Type()
)
pmopm2AlmChannel63BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel63BalancedPortn.setStatus("current")
_Pmopm2AlmChannel63PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel63PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel63PowerLowPortn = _Pmopm2AlmChannel63PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1, 5),
    _Pmopm2AlmChannel63PowerLowPortn_Type()
)
pmopm2AlmChannel63PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel63PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel63PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel63PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel63PowerHighPortn = _Pmopm2AlmChannel63PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1, 6),
    _Pmopm2AlmChannel63PowerHighPortn_Type()
)
pmopm2AlmChannel63PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel63PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel63OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel63OosPortn_Object = MibTableColumn
pmopm2AlmChannel63OosPortn = _Pmopm2AlmChannel63OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 140, 1, 7),
    _Pmopm2AlmChannel63OosPortn_Type()
)
pmopm2AlmChannel63OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel63OosPortn.setStatus("current")
_Pmopm2Almchannel64PortTable_Object = MibTable
pmopm2Almchannel64PortTable = _Pmopm2Almchannel64PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel64PortTable.setStatus("current")
_Pmopm2Almchannel64PortEntry_Object = MibTableRow
pmopm2Almchannel64PortEntry = _Pmopm2Almchannel64PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1)
)
pmopm2Almchannel64PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel64PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel64PortEntry.setStatus("current")


class _Pmopm2Almchannel64PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel64PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel64PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel64PortIndex_Object = MibTableColumn
pmopm2Almchannel64PortIndex = _Pmopm2Almchannel64PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1, 1),
    _Pmopm2Almchannel64PortIndex_Type()
)
pmopm2Almchannel64PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel64PortIndex.setStatus("current")
_Pmopm2AlmChannel64AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel64AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel64AbsentPortn = _Pmopm2AlmChannel64AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1, 2),
    _Pmopm2AlmChannel64AbsentPortn_Type()
)
pmopm2AlmChannel64AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel64AbsentPortn.setStatus("current")
_Pmopm2AlmChannel64MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel64MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel64MismatchPortn = _Pmopm2AlmChannel64MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1, 3),
    _Pmopm2AlmChannel64MismatchPortn_Type()
)
pmopm2AlmChannel64MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel64MismatchPortn.setStatus("current")
_Pmopm2AlmChannel64BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel64BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel64BalancedPortn = _Pmopm2AlmChannel64BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1, 4),
    _Pmopm2AlmChannel64BalancedPortn_Type()
)
pmopm2AlmChannel64BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel64BalancedPortn.setStatus("current")
_Pmopm2AlmChannel64PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel64PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel64PowerLowPortn = _Pmopm2AlmChannel64PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1, 5),
    _Pmopm2AlmChannel64PowerLowPortn_Type()
)
pmopm2AlmChannel64PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel64PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel64PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel64PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel64PowerHighPortn = _Pmopm2AlmChannel64PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1, 6),
    _Pmopm2AlmChannel64PowerHighPortn_Type()
)
pmopm2AlmChannel64PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel64PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel64OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel64OosPortn_Object = MibTableColumn
pmopm2AlmChannel64OosPortn = _Pmopm2AlmChannel64OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 142, 1, 7),
    _Pmopm2AlmChannel64OosPortn_Type()
)
pmopm2AlmChannel64OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel64OosPortn.setStatus("current")
_Pmopm2Almchannel65PortTable_Object = MibTable
pmopm2Almchannel65PortTable = _Pmopm2Almchannel65PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel65PortTable.setStatus("current")
_Pmopm2Almchannel65PortEntry_Object = MibTableRow
pmopm2Almchannel65PortEntry = _Pmopm2Almchannel65PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1)
)
pmopm2Almchannel65PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel65PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel65PortEntry.setStatus("current")


class _Pmopm2Almchannel65PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel65PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel65PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel65PortIndex_Object = MibTableColumn
pmopm2Almchannel65PortIndex = _Pmopm2Almchannel65PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1, 1),
    _Pmopm2Almchannel65PortIndex_Type()
)
pmopm2Almchannel65PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel65PortIndex.setStatus("current")
_Pmopm2AlmChannel65AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel65AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel65AbsentPortn = _Pmopm2AlmChannel65AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1, 2),
    _Pmopm2AlmChannel65AbsentPortn_Type()
)
pmopm2AlmChannel65AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel65AbsentPortn.setStatus("current")
_Pmopm2AlmChannel65MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel65MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel65MismatchPortn = _Pmopm2AlmChannel65MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1, 3),
    _Pmopm2AlmChannel65MismatchPortn_Type()
)
pmopm2AlmChannel65MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel65MismatchPortn.setStatus("current")
_Pmopm2AlmChannel65BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel65BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel65BalancedPortn = _Pmopm2AlmChannel65BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1, 4),
    _Pmopm2AlmChannel65BalancedPortn_Type()
)
pmopm2AlmChannel65BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel65BalancedPortn.setStatus("current")
_Pmopm2AlmChannel65PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel65PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel65PowerLowPortn = _Pmopm2AlmChannel65PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1, 5),
    _Pmopm2AlmChannel65PowerLowPortn_Type()
)
pmopm2AlmChannel65PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel65PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel65PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel65PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel65PowerHighPortn = _Pmopm2AlmChannel65PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1, 6),
    _Pmopm2AlmChannel65PowerHighPortn_Type()
)
pmopm2AlmChannel65PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel65PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel65OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel65OosPortn_Object = MibTableColumn
pmopm2AlmChannel65OosPortn = _Pmopm2AlmChannel65OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 144, 1, 7),
    _Pmopm2AlmChannel65OosPortn_Type()
)
pmopm2AlmChannel65OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel65OosPortn.setStatus("current")
_Pmopm2Almchannel66PortTable_Object = MibTable
pmopm2Almchannel66PortTable = _Pmopm2Almchannel66PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel66PortTable.setStatus("current")
_Pmopm2Almchannel66PortEntry_Object = MibTableRow
pmopm2Almchannel66PortEntry = _Pmopm2Almchannel66PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1)
)
pmopm2Almchannel66PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel66PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel66PortEntry.setStatus("current")


class _Pmopm2Almchannel66PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel66PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel66PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel66PortIndex_Object = MibTableColumn
pmopm2Almchannel66PortIndex = _Pmopm2Almchannel66PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1, 1),
    _Pmopm2Almchannel66PortIndex_Type()
)
pmopm2Almchannel66PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel66PortIndex.setStatus("current")
_Pmopm2AlmChannel66AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel66AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel66AbsentPortn = _Pmopm2AlmChannel66AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1, 2),
    _Pmopm2AlmChannel66AbsentPortn_Type()
)
pmopm2AlmChannel66AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel66AbsentPortn.setStatus("current")
_Pmopm2AlmChannel66MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel66MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel66MismatchPortn = _Pmopm2AlmChannel66MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1, 3),
    _Pmopm2AlmChannel66MismatchPortn_Type()
)
pmopm2AlmChannel66MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel66MismatchPortn.setStatus("current")
_Pmopm2AlmChannel66BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel66BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel66BalancedPortn = _Pmopm2AlmChannel66BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1, 4),
    _Pmopm2AlmChannel66BalancedPortn_Type()
)
pmopm2AlmChannel66BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel66BalancedPortn.setStatus("current")
_Pmopm2AlmChannel66PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel66PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel66PowerLowPortn = _Pmopm2AlmChannel66PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1, 5),
    _Pmopm2AlmChannel66PowerLowPortn_Type()
)
pmopm2AlmChannel66PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel66PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel66PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel66PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel66PowerHighPortn = _Pmopm2AlmChannel66PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1, 6),
    _Pmopm2AlmChannel66PowerHighPortn_Type()
)
pmopm2AlmChannel66PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel66PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel66OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel66OosPortn_Object = MibTableColumn
pmopm2AlmChannel66OosPortn = _Pmopm2AlmChannel66OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 146, 1, 7),
    _Pmopm2AlmChannel66OosPortn_Type()
)
pmopm2AlmChannel66OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel66OosPortn.setStatus("current")
_Pmopm2Almchannel67PortTable_Object = MibTable
pmopm2Almchannel67PortTable = _Pmopm2Almchannel67PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel67PortTable.setStatus("current")
_Pmopm2Almchannel67PortEntry_Object = MibTableRow
pmopm2Almchannel67PortEntry = _Pmopm2Almchannel67PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1)
)
pmopm2Almchannel67PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel67PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel67PortEntry.setStatus("current")


class _Pmopm2Almchannel67PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel67PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel67PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel67PortIndex_Object = MibTableColumn
pmopm2Almchannel67PortIndex = _Pmopm2Almchannel67PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1, 1),
    _Pmopm2Almchannel67PortIndex_Type()
)
pmopm2Almchannel67PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel67PortIndex.setStatus("current")
_Pmopm2AlmChannel67AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel67AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel67AbsentPortn = _Pmopm2AlmChannel67AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1, 2),
    _Pmopm2AlmChannel67AbsentPortn_Type()
)
pmopm2AlmChannel67AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel67AbsentPortn.setStatus("current")
_Pmopm2AlmChannel67MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel67MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel67MismatchPortn = _Pmopm2AlmChannel67MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1, 3),
    _Pmopm2AlmChannel67MismatchPortn_Type()
)
pmopm2AlmChannel67MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel67MismatchPortn.setStatus("current")
_Pmopm2AlmChannel67BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel67BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel67BalancedPortn = _Pmopm2AlmChannel67BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1, 4),
    _Pmopm2AlmChannel67BalancedPortn_Type()
)
pmopm2AlmChannel67BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel67BalancedPortn.setStatus("current")
_Pmopm2AlmChannel67PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel67PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel67PowerLowPortn = _Pmopm2AlmChannel67PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1, 5),
    _Pmopm2AlmChannel67PowerLowPortn_Type()
)
pmopm2AlmChannel67PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel67PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel67PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel67PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel67PowerHighPortn = _Pmopm2AlmChannel67PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1, 6),
    _Pmopm2AlmChannel67PowerHighPortn_Type()
)
pmopm2AlmChannel67PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel67PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel67OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel67OosPortn_Object = MibTableColumn
pmopm2AlmChannel67OosPortn = _Pmopm2AlmChannel67OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 148, 1, 7),
    _Pmopm2AlmChannel67OosPortn_Type()
)
pmopm2AlmChannel67OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel67OosPortn.setStatus("current")
_Pmopm2Almchannel68PortTable_Object = MibTable
pmopm2Almchannel68PortTable = _Pmopm2Almchannel68PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel68PortTable.setStatus("current")
_Pmopm2Almchannel68PortEntry_Object = MibTableRow
pmopm2Almchannel68PortEntry = _Pmopm2Almchannel68PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1)
)
pmopm2Almchannel68PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel68PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel68PortEntry.setStatus("current")


class _Pmopm2Almchannel68PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel68PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel68PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel68PortIndex_Object = MibTableColumn
pmopm2Almchannel68PortIndex = _Pmopm2Almchannel68PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1, 1),
    _Pmopm2Almchannel68PortIndex_Type()
)
pmopm2Almchannel68PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel68PortIndex.setStatus("current")
_Pmopm2AlmChannel68AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel68AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel68AbsentPortn = _Pmopm2AlmChannel68AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1, 2),
    _Pmopm2AlmChannel68AbsentPortn_Type()
)
pmopm2AlmChannel68AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel68AbsentPortn.setStatus("current")
_Pmopm2AlmChannel68MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel68MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel68MismatchPortn = _Pmopm2AlmChannel68MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1, 3),
    _Pmopm2AlmChannel68MismatchPortn_Type()
)
pmopm2AlmChannel68MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel68MismatchPortn.setStatus("current")
_Pmopm2AlmChannel68BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel68BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel68BalancedPortn = _Pmopm2AlmChannel68BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1, 4),
    _Pmopm2AlmChannel68BalancedPortn_Type()
)
pmopm2AlmChannel68BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel68BalancedPortn.setStatus("current")
_Pmopm2AlmChannel68PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel68PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel68PowerLowPortn = _Pmopm2AlmChannel68PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1, 5),
    _Pmopm2AlmChannel68PowerLowPortn_Type()
)
pmopm2AlmChannel68PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel68PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel68PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel68PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel68PowerHighPortn = _Pmopm2AlmChannel68PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1, 6),
    _Pmopm2AlmChannel68PowerHighPortn_Type()
)
pmopm2AlmChannel68PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel68PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel68OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel68OosPortn_Object = MibTableColumn
pmopm2AlmChannel68OosPortn = _Pmopm2AlmChannel68OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 150, 1, 7),
    _Pmopm2AlmChannel68OosPortn_Type()
)
pmopm2AlmChannel68OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel68OosPortn.setStatus("current")
_Pmopm2Almchannel69PortTable_Object = MibTable
pmopm2Almchannel69PortTable = _Pmopm2Almchannel69PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel69PortTable.setStatus("current")
_Pmopm2Almchannel69PortEntry_Object = MibTableRow
pmopm2Almchannel69PortEntry = _Pmopm2Almchannel69PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1)
)
pmopm2Almchannel69PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel69PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel69PortEntry.setStatus("current")


class _Pmopm2Almchannel69PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel69PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel69PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel69PortIndex_Object = MibTableColumn
pmopm2Almchannel69PortIndex = _Pmopm2Almchannel69PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1, 1),
    _Pmopm2Almchannel69PortIndex_Type()
)
pmopm2Almchannel69PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel69PortIndex.setStatus("current")
_Pmopm2AlmChannel69AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel69AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel69AbsentPortn = _Pmopm2AlmChannel69AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1, 2),
    _Pmopm2AlmChannel69AbsentPortn_Type()
)
pmopm2AlmChannel69AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel69AbsentPortn.setStatus("current")
_Pmopm2AlmChannel69MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel69MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel69MismatchPortn = _Pmopm2AlmChannel69MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1, 3),
    _Pmopm2AlmChannel69MismatchPortn_Type()
)
pmopm2AlmChannel69MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel69MismatchPortn.setStatus("current")
_Pmopm2AlmChannel69BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel69BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel69BalancedPortn = _Pmopm2AlmChannel69BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1, 4),
    _Pmopm2AlmChannel69BalancedPortn_Type()
)
pmopm2AlmChannel69BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel69BalancedPortn.setStatus("current")
_Pmopm2AlmChannel69PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel69PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel69PowerLowPortn = _Pmopm2AlmChannel69PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1, 5),
    _Pmopm2AlmChannel69PowerLowPortn_Type()
)
pmopm2AlmChannel69PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel69PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel69PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel69PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel69PowerHighPortn = _Pmopm2AlmChannel69PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1, 6),
    _Pmopm2AlmChannel69PowerHighPortn_Type()
)
pmopm2AlmChannel69PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel69PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel69OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel69OosPortn_Object = MibTableColumn
pmopm2AlmChannel69OosPortn = _Pmopm2AlmChannel69OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 152, 1, 7),
    _Pmopm2AlmChannel69OosPortn_Type()
)
pmopm2AlmChannel69OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel69OosPortn.setStatus("current")
_Pmopm2Almchannel70PortTable_Object = MibTable
pmopm2Almchannel70PortTable = _Pmopm2Almchannel70PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel70PortTable.setStatus("current")
_Pmopm2Almchannel70PortEntry_Object = MibTableRow
pmopm2Almchannel70PortEntry = _Pmopm2Almchannel70PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1)
)
pmopm2Almchannel70PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel70PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel70PortEntry.setStatus("current")


class _Pmopm2Almchannel70PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel70PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel70PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel70PortIndex_Object = MibTableColumn
pmopm2Almchannel70PortIndex = _Pmopm2Almchannel70PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1, 1),
    _Pmopm2Almchannel70PortIndex_Type()
)
pmopm2Almchannel70PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel70PortIndex.setStatus("current")
_Pmopm2AlmChannel70AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel70AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel70AbsentPortn = _Pmopm2AlmChannel70AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1, 2),
    _Pmopm2AlmChannel70AbsentPortn_Type()
)
pmopm2AlmChannel70AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel70AbsentPortn.setStatus("current")
_Pmopm2AlmChannel70MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel70MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel70MismatchPortn = _Pmopm2AlmChannel70MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1, 3),
    _Pmopm2AlmChannel70MismatchPortn_Type()
)
pmopm2AlmChannel70MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel70MismatchPortn.setStatus("current")
_Pmopm2AlmChannel70BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel70BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel70BalancedPortn = _Pmopm2AlmChannel70BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1, 4),
    _Pmopm2AlmChannel70BalancedPortn_Type()
)
pmopm2AlmChannel70BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel70BalancedPortn.setStatus("current")
_Pmopm2AlmChannel70PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel70PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel70PowerLowPortn = _Pmopm2AlmChannel70PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1, 5),
    _Pmopm2AlmChannel70PowerLowPortn_Type()
)
pmopm2AlmChannel70PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel70PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel70PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel70PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel70PowerHighPortn = _Pmopm2AlmChannel70PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1, 6),
    _Pmopm2AlmChannel70PowerHighPortn_Type()
)
pmopm2AlmChannel70PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel70PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel70OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel70OosPortn_Object = MibTableColumn
pmopm2AlmChannel70OosPortn = _Pmopm2AlmChannel70OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 154, 1, 7),
    _Pmopm2AlmChannel70OosPortn_Type()
)
pmopm2AlmChannel70OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel70OosPortn.setStatus("current")
_Pmopm2Almchannel71PortTable_Object = MibTable
pmopm2Almchannel71PortTable = _Pmopm2Almchannel71PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel71PortTable.setStatus("current")
_Pmopm2Almchannel71PortEntry_Object = MibTableRow
pmopm2Almchannel71PortEntry = _Pmopm2Almchannel71PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1)
)
pmopm2Almchannel71PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel71PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel71PortEntry.setStatus("current")


class _Pmopm2Almchannel71PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel71PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel71PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel71PortIndex_Object = MibTableColumn
pmopm2Almchannel71PortIndex = _Pmopm2Almchannel71PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1, 1),
    _Pmopm2Almchannel71PortIndex_Type()
)
pmopm2Almchannel71PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel71PortIndex.setStatus("current")
_Pmopm2AlmChannel71AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel71AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel71AbsentPortn = _Pmopm2AlmChannel71AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1, 2),
    _Pmopm2AlmChannel71AbsentPortn_Type()
)
pmopm2AlmChannel71AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel71AbsentPortn.setStatus("current")
_Pmopm2AlmChannel71MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel71MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel71MismatchPortn = _Pmopm2AlmChannel71MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1, 3),
    _Pmopm2AlmChannel71MismatchPortn_Type()
)
pmopm2AlmChannel71MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel71MismatchPortn.setStatus("current")
_Pmopm2AlmChannel71BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel71BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel71BalancedPortn = _Pmopm2AlmChannel71BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1, 4),
    _Pmopm2AlmChannel71BalancedPortn_Type()
)
pmopm2AlmChannel71BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel71BalancedPortn.setStatus("current")
_Pmopm2AlmChannel71PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel71PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel71PowerLowPortn = _Pmopm2AlmChannel71PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1, 5),
    _Pmopm2AlmChannel71PowerLowPortn_Type()
)
pmopm2AlmChannel71PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel71PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel71PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel71PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel71PowerHighPortn = _Pmopm2AlmChannel71PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1, 6),
    _Pmopm2AlmChannel71PowerHighPortn_Type()
)
pmopm2AlmChannel71PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel71PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel71OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel71OosPortn_Object = MibTableColumn
pmopm2AlmChannel71OosPortn = _Pmopm2AlmChannel71OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 156, 1, 7),
    _Pmopm2AlmChannel71OosPortn_Type()
)
pmopm2AlmChannel71OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel71OosPortn.setStatus("current")
_Pmopm2Almchannel72PortTable_Object = MibTable
pmopm2Almchannel72PortTable = _Pmopm2Almchannel72PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel72PortTable.setStatus("current")
_Pmopm2Almchannel72PortEntry_Object = MibTableRow
pmopm2Almchannel72PortEntry = _Pmopm2Almchannel72PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1)
)
pmopm2Almchannel72PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel72PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel72PortEntry.setStatus("current")


class _Pmopm2Almchannel72PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel72PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel72PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel72PortIndex_Object = MibTableColumn
pmopm2Almchannel72PortIndex = _Pmopm2Almchannel72PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1, 1),
    _Pmopm2Almchannel72PortIndex_Type()
)
pmopm2Almchannel72PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel72PortIndex.setStatus("current")
_Pmopm2AlmChannel72AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel72AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel72AbsentPortn = _Pmopm2AlmChannel72AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1, 2),
    _Pmopm2AlmChannel72AbsentPortn_Type()
)
pmopm2AlmChannel72AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel72AbsentPortn.setStatus("current")
_Pmopm2AlmChannel72MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel72MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel72MismatchPortn = _Pmopm2AlmChannel72MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1, 3),
    _Pmopm2AlmChannel72MismatchPortn_Type()
)
pmopm2AlmChannel72MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel72MismatchPortn.setStatus("current")
_Pmopm2AlmChannel72BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel72BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel72BalancedPortn = _Pmopm2AlmChannel72BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1, 4),
    _Pmopm2AlmChannel72BalancedPortn_Type()
)
pmopm2AlmChannel72BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel72BalancedPortn.setStatus("current")
_Pmopm2AlmChannel72PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel72PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel72PowerLowPortn = _Pmopm2AlmChannel72PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1, 5),
    _Pmopm2AlmChannel72PowerLowPortn_Type()
)
pmopm2AlmChannel72PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel72PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel72PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel72PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel72PowerHighPortn = _Pmopm2AlmChannel72PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1, 6),
    _Pmopm2AlmChannel72PowerHighPortn_Type()
)
pmopm2AlmChannel72PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel72PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel72OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel72OosPortn_Object = MibTableColumn
pmopm2AlmChannel72OosPortn = _Pmopm2AlmChannel72OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 158, 1, 7),
    _Pmopm2AlmChannel72OosPortn_Type()
)
pmopm2AlmChannel72OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel72OosPortn.setStatus("current")
_Pmopm2Almchannel73PortTable_Object = MibTable
pmopm2Almchannel73PortTable = _Pmopm2Almchannel73PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel73PortTable.setStatus("current")
_Pmopm2Almchannel73PortEntry_Object = MibTableRow
pmopm2Almchannel73PortEntry = _Pmopm2Almchannel73PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1)
)
pmopm2Almchannel73PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel73PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel73PortEntry.setStatus("current")


class _Pmopm2Almchannel73PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel73PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel73PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel73PortIndex_Object = MibTableColumn
pmopm2Almchannel73PortIndex = _Pmopm2Almchannel73PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1, 1),
    _Pmopm2Almchannel73PortIndex_Type()
)
pmopm2Almchannel73PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel73PortIndex.setStatus("current")
_Pmopm2AlmChannel73AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel73AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel73AbsentPortn = _Pmopm2AlmChannel73AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1, 2),
    _Pmopm2AlmChannel73AbsentPortn_Type()
)
pmopm2AlmChannel73AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel73AbsentPortn.setStatus("current")
_Pmopm2AlmChannel73MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel73MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel73MismatchPortn = _Pmopm2AlmChannel73MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1, 3),
    _Pmopm2AlmChannel73MismatchPortn_Type()
)
pmopm2AlmChannel73MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel73MismatchPortn.setStatus("current")
_Pmopm2AlmChannel73BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel73BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel73BalancedPortn = _Pmopm2AlmChannel73BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1, 4),
    _Pmopm2AlmChannel73BalancedPortn_Type()
)
pmopm2AlmChannel73BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel73BalancedPortn.setStatus("current")
_Pmopm2AlmChannel73PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel73PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel73PowerLowPortn = _Pmopm2AlmChannel73PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1, 5),
    _Pmopm2AlmChannel73PowerLowPortn_Type()
)
pmopm2AlmChannel73PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel73PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel73PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel73PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel73PowerHighPortn = _Pmopm2AlmChannel73PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1, 6),
    _Pmopm2AlmChannel73PowerHighPortn_Type()
)
pmopm2AlmChannel73PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel73PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel73OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel73OosPortn_Object = MibTableColumn
pmopm2AlmChannel73OosPortn = _Pmopm2AlmChannel73OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 160, 1, 7),
    _Pmopm2AlmChannel73OosPortn_Type()
)
pmopm2AlmChannel73OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel73OosPortn.setStatus("current")
_Pmopm2Almchannel74PortTable_Object = MibTable
pmopm2Almchannel74PortTable = _Pmopm2Almchannel74PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel74PortTable.setStatus("current")
_Pmopm2Almchannel74PortEntry_Object = MibTableRow
pmopm2Almchannel74PortEntry = _Pmopm2Almchannel74PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1)
)
pmopm2Almchannel74PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel74PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel74PortEntry.setStatus("current")


class _Pmopm2Almchannel74PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel74PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel74PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel74PortIndex_Object = MibTableColumn
pmopm2Almchannel74PortIndex = _Pmopm2Almchannel74PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1, 1),
    _Pmopm2Almchannel74PortIndex_Type()
)
pmopm2Almchannel74PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel74PortIndex.setStatus("current")
_Pmopm2AlmChannel74AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel74AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel74AbsentPortn = _Pmopm2AlmChannel74AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1, 2),
    _Pmopm2AlmChannel74AbsentPortn_Type()
)
pmopm2AlmChannel74AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel74AbsentPortn.setStatus("current")
_Pmopm2AlmChannel74MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel74MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel74MismatchPortn = _Pmopm2AlmChannel74MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1, 3),
    _Pmopm2AlmChannel74MismatchPortn_Type()
)
pmopm2AlmChannel74MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel74MismatchPortn.setStatus("current")
_Pmopm2AlmChannel74BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel74BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel74BalancedPortn = _Pmopm2AlmChannel74BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1, 4),
    _Pmopm2AlmChannel74BalancedPortn_Type()
)
pmopm2AlmChannel74BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel74BalancedPortn.setStatus("current")
_Pmopm2AlmChannel74PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel74PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel74PowerLowPortn = _Pmopm2AlmChannel74PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1, 5),
    _Pmopm2AlmChannel74PowerLowPortn_Type()
)
pmopm2AlmChannel74PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel74PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel74PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel74PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel74PowerHighPortn = _Pmopm2AlmChannel74PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1, 6),
    _Pmopm2AlmChannel74PowerHighPortn_Type()
)
pmopm2AlmChannel74PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel74PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel74OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel74OosPortn_Object = MibTableColumn
pmopm2AlmChannel74OosPortn = _Pmopm2AlmChannel74OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 162, 1, 7),
    _Pmopm2AlmChannel74OosPortn_Type()
)
pmopm2AlmChannel74OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel74OosPortn.setStatus("current")
_Pmopm2Almchannel75PortTable_Object = MibTable
pmopm2Almchannel75PortTable = _Pmopm2Almchannel75PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel75PortTable.setStatus("current")
_Pmopm2Almchannel75PortEntry_Object = MibTableRow
pmopm2Almchannel75PortEntry = _Pmopm2Almchannel75PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1)
)
pmopm2Almchannel75PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel75PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel75PortEntry.setStatus("current")


class _Pmopm2Almchannel75PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel75PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel75PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel75PortIndex_Object = MibTableColumn
pmopm2Almchannel75PortIndex = _Pmopm2Almchannel75PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1, 1),
    _Pmopm2Almchannel75PortIndex_Type()
)
pmopm2Almchannel75PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel75PortIndex.setStatus("current")
_Pmopm2AlmChannel75AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel75AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel75AbsentPortn = _Pmopm2AlmChannel75AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1, 2),
    _Pmopm2AlmChannel75AbsentPortn_Type()
)
pmopm2AlmChannel75AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel75AbsentPortn.setStatus("current")
_Pmopm2AlmChannel75MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel75MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel75MismatchPortn = _Pmopm2AlmChannel75MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1, 3),
    _Pmopm2AlmChannel75MismatchPortn_Type()
)
pmopm2AlmChannel75MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel75MismatchPortn.setStatus("current")
_Pmopm2AlmChannel75BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel75BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel75BalancedPortn = _Pmopm2AlmChannel75BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1, 4),
    _Pmopm2AlmChannel75BalancedPortn_Type()
)
pmopm2AlmChannel75BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel75BalancedPortn.setStatus("current")
_Pmopm2AlmChannel75PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel75PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel75PowerLowPortn = _Pmopm2AlmChannel75PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1, 5),
    _Pmopm2AlmChannel75PowerLowPortn_Type()
)
pmopm2AlmChannel75PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel75PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel75PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel75PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel75PowerHighPortn = _Pmopm2AlmChannel75PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1, 6),
    _Pmopm2AlmChannel75PowerHighPortn_Type()
)
pmopm2AlmChannel75PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel75PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel75OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel75OosPortn_Object = MibTableColumn
pmopm2AlmChannel75OosPortn = _Pmopm2AlmChannel75OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 164, 1, 7),
    _Pmopm2AlmChannel75OosPortn_Type()
)
pmopm2AlmChannel75OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel75OosPortn.setStatus("current")
_Pmopm2Almchannel76PortTable_Object = MibTable
pmopm2Almchannel76PortTable = _Pmopm2Almchannel76PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel76PortTable.setStatus("current")
_Pmopm2Almchannel76PortEntry_Object = MibTableRow
pmopm2Almchannel76PortEntry = _Pmopm2Almchannel76PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1)
)
pmopm2Almchannel76PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel76PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel76PortEntry.setStatus("current")


class _Pmopm2Almchannel76PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel76PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel76PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel76PortIndex_Object = MibTableColumn
pmopm2Almchannel76PortIndex = _Pmopm2Almchannel76PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1, 1),
    _Pmopm2Almchannel76PortIndex_Type()
)
pmopm2Almchannel76PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel76PortIndex.setStatus("current")
_Pmopm2AlmChannel76AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel76AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel76AbsentPortn = _Pmopm2AlmChannel76AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1, 2),
    _Pmopm2AlmChannel76AbsentPortn_Type()
)
pmopm2AlmChannel76AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel76AbsentPortn.setStatus("current")
_Pmopm2AlmChannel76MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel76MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel76MismatchPortn = _Pmopm2AlmChannel76MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1, 3),
    _Pmopm2AlmChannel76MismatchPortn_Type()
)
pmopm2AlmChannel76MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel76MismatchPortn.setStatus("current")
_Pmopm2AlmChannel76BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel76BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel76BalancedPortn = _Pmopm2AlmChannel76BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1, 4),
    _Pmopm2AlmChannel76BalancedPortn_Type()
)
pmopm2AlmChannel76BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel76BalancedPortn.setStatus("current")
_Pmopm2AlmChannel76PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel76PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel76PowerLowPortn = _Pmopm2AlmChannel76PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1, 5),
    _Pmopm2AlmChannel76PowerLowPortn_Type()
)
pmopm2AlmChannel76PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel76PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel76PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel76PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel76PowerHighPortn = _Pmopm2AlmChannel76PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1, 6),
    _Pmopm2AlmChannel76PowerHighPortn_Type()
)
pmopm2AlmChannel76PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel76PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel76OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel76OosPortn_Object = MibTableColumn
pmopm2AlmChannel76OosPortn = _Pmopm2AlmChannel76OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 166, 1, 7),
    _Pmopm2AlmChannel76OosPortn_Type()
)
pmopm2AlmChannel76OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel76OosPortn.setStatus("current")
_Pmopm2Almchannel77PortTable_Object = MibTable
pmopm2Almchannel77PortTable = _Pmopm2Almchannel77PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel77PortTable.setStatus("current")
_Pmopm2Almchannel77PortEntry_Object = MibTableRow
pmopm2Almchannel77PortEntry = _Pmopm2Almchannel77PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1)
)
pmopm2Almchannel77PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel77PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel77PortEntry.setStatus("current")


class _Pmopm2Almchannel77PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel77PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel77PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel77PortIndex_Object = MibTableColumn
pmopm2Almchannel77PortIndex = _Pmopm2Almchannel77PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1, 1),
    _Pmopm2Almchannel77PortIndex_Type()
)
pmopm2Almchannel77PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel77PortIndex.setStatus("current")
_Pmopm2AlmChannel77AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel77AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel77AbsentPortn = _Pmopm2AlmChannel77AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1, 2),
    _Pmopm2AlmChannel77AbsentPortn_Type()
)
pmopm2AlmChannel77AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel77AbsentPortn.setStatus("current")
_Pmopm2AlmChannel77MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel77MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel77MismatchPortn = _Pmopm2AlmChannel77MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1, 3),
    _Pmopm2AlmChannel77MismatchPortn_Type()
)
pmopm2AlmChannel77MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel77MismatchPortn.setStatus("current")
_Pmopm2AlmChannel77BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel77BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel77BalancedPortn = _Pmopm2AlmChannel77BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1, 4),
    _Pmopm2AlmChannel77BalancedPortn_Type()
)
pmopm2AlmChannel77BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel77BalancedPortn.setStatus("current")
_Pmopm2AlmChannel77PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel77PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel77PowerLowPortn = _Pmopm2AlmChannel77PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1, 5),
    _Pmopm2AlmChannel77PowerLowPortn_Type()
)
pmopm2AlmChannel77PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel77PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel77PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel77PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel77PowerHighPortn = _Pmopm2AlmChannel77PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1, 6),
    _Pmopm2AlmChannel77PowerHighPortn_Type()
)
pmopm2AlmChannel77PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel77PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel77OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel77OosPortn_Object = MibTableColumn
pmopm2AlmChannel77OosPortn = _Pmopm2AlmChannel77OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 168, 1, 7),
    _Pmopm2AlmChannel77OosPortn_Type()
)
pmopm2AlmChannel77OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel77OosPortn.setStatus("current")
_Pmopm2Almchannel78PortTable_Object = MibTable
pmopm2Almchannel78PortTable = _Pmopm2Almchannel78PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel78PortTable.setStatus("current")
_Pmopm2Almchannel78PortEntry_Object = MibTableRow
pmopm2Almchannel78PortEntry = _Pmopm2Almchannel78PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1)
)
pmopm2Almchannel78PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel78PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel78PortEntry.setStatus("current")


class _Pmopm2Almchannel78PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel78PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel78PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel78PortIndex_Object = MibTableColumn
pmopm2Almchannel78PortIndex = _Pmopm2Almchannel78PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1, 1),
    _Pmopm2Almchannel78PortIndex_Type()
)
pmopm2Almchannel78PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel78PortIndex.setStatus("current")
_Pmopm2AlmChannel78AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel78AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel78AbsentPortn = _Pmopm2AlmChannel78AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1, 2),
    _Pmopm2AlmChannel78AbsentPortn_Type()
)
pmopm2AlmChannel78AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel78AbsentPortn.setStatus("current")
_Pmopm2AlmChannel78MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel78MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel78MismatchPortn = _Pmopm2AlmChannel78MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1, 3),
    _Pmopm2AlmChannel78MismatchPortn_Type()
)
pmopm2AlmChannel78MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel78MismatchPortn.setStatus("current")
_Pmopm2AlmChannel78BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel78BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel78BalancedPortn = _Pmopm2AlmChannel78BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1, 4),
    _Pmopm2AlmChannel78BalancedPortn_Type()
)
pmopm2AlmChannel78BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel78BalancedPortn.setStatus("current")
_Pmopm2AlmChannel78PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel78PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel78PowerLowPortn = _Pmopm2AlmChannel78PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1, 5),
    _Pmopm2AlmChannel78PowerLowPortn_Type()
)
pmopm2AlmChannel78PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel78PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel78PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel78PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel78PowerHighPortn = _Pmopm2AlmChannel78PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1, 6),
    _Pmopm2AlmChannel78PowerHighPortn_Type()
)
pmopm2AlmChannel78PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel78PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel78OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel78OosPortn_Object = MibTableColumn
pmopm2AlmChannel78OosPortn = _Pmopm2AlmChannel78OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 170, 1, 7),
    _Pmopm2AlmChannel78OosPortn_Type()
)
pmopm2AlmChannel78OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel78OosPortn.setStatus("current")
_Pmopm2Almchannel79PortTable_Object = MibTable
pmopm2Almchannel79PortTable = _Pmopm2Almchannel79PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel79PortTable.setStatus("current")
_Pmopm2Almchannel79PortEntry_Object = MibTableRow
pmopm2Almchannel79PortEntry = _Pmopm2Almchannel79PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1)
)
pmopm2Almchannel79PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel79PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel79PortEntry.setStatus("current")


class _Pmopm2Almchannel79PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel79PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel79PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel79PortIndex_Object = MibTableColumn
pmopm2Almchannel79PortIndex = _Pmopm2Almchannel79PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1, 1),
    _Pmopm2Almchannel79PortIndex_Type()
)
pmopm2Almchannel79PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel79PortIndex.setStatus("current")
_Pmopm2AlmChannel79AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel79AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel79AbsentPortn = _Pmopm2AlmChannel79AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1, 2),
    _Pmopm2AlmChannel79AbsentPortn_Type()
)
pmopm2AlmChannel79AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel79AbsentPortn.setStatus("current")
_Pmopm2AlmChannel79MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel79MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel79MismatchPortn = _Pmopm2AlmChannel79MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1, 3),
    _Pmopm2AlmChannel79MismatchPortn_Type()
)
pmopm2AlmChannel79MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel79MismatchPortn.setStatus("current")
_Pmopm2AlmChannel79BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel79BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel79BalancedPortn = _Pmopm2AlmChannel79BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1, 4),
    _Pmopm2AlmChannel79BalancedPortn_Type()
)
pmopm2AlmChannel79BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel79BalancedPortn.setStatus("current")
_Pmopm2AlmChannel79PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel79PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel79PowerLowPortn = _Pmopm2AlmChannel79PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1, 5),
    _Pmopm2AlmChannel79PowerLowPortn_Type()
)
pmopm2AlmChannel79PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel79PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel79PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel79PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel79PowerHighPortn = _Pmopm2AlmChannel79PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1, 6),
    _Pmopm2AlmChannel79PowerHighPortn_Type()
)
pmopm2AlmChannel79PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel79PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel79OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel79OosPortn_Object = MibTableColumn
pmopm2AlmChannel79OosPortn = _Pmopm2AlmChannel79OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 172, 1, 7),
    _Pmopm2AlmChannel79OosPortn_Type()
)
pmopm2AlmChannel79OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel79OosPortn.setStatus("current")
_Pmopm2Almchannel80PortTable_Object = MibTable
pmopm2Almchannel80PortTable = _Pmopm2Almchannel80PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel80PortTable.setStatus("current")
_Pmopm2Almchannel80PortEntry_Object = MibTableRow
pmopm2Almchannel80PortEntry = _Pmopm2Almchannel80PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1)
)
pmopm2Almchannel80PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel80PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel80PortEntry.setStatus("current")


class _Pmopm2Almchannel80PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel80PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel80PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel80PortIndex_Object = MibTableColumn
pmopm2Almchannel80PortIndex = _Pmopm2Almchannel80PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1, 1),
    _Pmopm2Almchannel80PortIndex_Type()
)
pmopm2Almchannel80PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel80PortIndex.setStatus("current")
_Pmopm2AlmChannel80AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel80AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel80AbsentPortn = _Pmopm2AlmChannel80AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1, 2),
    _Pmopm2AlmChannel80AbsentPortn_Type()
)
pmopm2AlmChannel80AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel80AbsentPortn.setStatus("current")
_Pmopm2AlmChannel80MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel80MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel80MismatchPortn = _Pmopm2AlmChannel80MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1, 3),
    _Pmopm2AlmChannel80MismatchPortn_Type()
)
pmopm2AlmChannel80MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel80MismatchPortn.setStatus("current")
_Pmopm2AlmChannel80BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel80BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel80BalancedPortn = _Pmopm2AlmChannel80BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1, 4),
    _Pmopm2AlmChannel80BalancedPortn_Type()
)
pmopm2AlmChannel80BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel80BalancedPortn.setStatus("current")
_Pmopm2AlmChannel80PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel80PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel80PowerLowPortn = _Pmopm2AlmChannel80PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1, 5),
    _Pmopm2AlmChannel80PowerLowPortn_Type()
)
pmopm2AlmChannel80PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel80PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel80PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel80PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel80PowerHighPortn = _Pmopm2AlmChannel80PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1, 6),
    _Pmopm2AlmChannel80PowerHighPortn_Type()
)
pmopm2AlmChannel80PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel80PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel80OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel80OosPortn_Object = MibTableColumn
pmopm2AlmChannel80OosPortn = _Pmopm2AlmChannel80OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 174, 1, 7),
    _Pmopm2AlmChannel80OosPortn_Type()
)
pmopm2AlmChannel80OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel80OosPortn.setStatus("current")
_Pmopm2Almchannel81PortTable_Object = MibTable
pmopm2Almchannel81PortTable = _Pmopm2Almchannel81PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel81PortTable.setStatus("current")
_Pmopm2Almchannel81PortEntry_Object = MibTableRow
pmopm2Almchannel81PortEntry = _Pmopm2Almchannel81PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1)
)
pmopm2Almchannel81PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel81PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel81PortEntry.setStatus("current")


class _Pmopm2Almchannel81PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel81PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel81PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel81PortIndex_Object = MibTableColumn
pmopm2Almchannel81PortIndex = _Pmopm2Almchannel81PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1, 1),
    _Pmopm2Almchannel81PortIndex_Type()
)
pmopm2Almchannel81PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel81PortIndex.setStatus("current")
_Pmopm2AlmChannel81AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel81AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel81AbsentPortn = _Pmopm2AlmChannel81AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1, 2),
    _Pmopm2AlmChannel81AbsentPortn_Type()
)
pmopm2AlmChannel81AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel81AbsentPortn.setStatus("current")
_Pmopm2AlmChannel81MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel81MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel81MismatchPortn = _Pmopm2AlmChannel81MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1, 3),
    _Pmopm2AlmChannel81MismatchPortn_Type()
)
pmopm2AlmChannel81MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel81MismatchPortn.setStatus("current")
_Pmopm2AlmChannel81BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel81BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel81BalancedPortn = _Pmopm2AlmChannel81BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1, 4),
    _Pmopm2AlmChannel81BalancedPortn_Type()
)
pmopm2AlmChannel81BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel81BalancedPortn.setStatus("current")
_Pmopm2AlmChannel81PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel81PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel81PowerLowPortn = _Pmopm2AlmChannel81PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1, 5),
    _Pmopm2AlmChannel81PowerLowPortn_Type()
)
pmopm2AlmChannel81PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel81PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel81PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel81PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel81PowerHighPortn = _Pmopm2AlmChannel81PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1, 6),
    _Pmopm2AlmChannel81PowerHighPortn_Type()
)
pmopm2AlmChannel81PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel81PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel81OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel81OosPortn_Object = MibTableColumn
pmopm2AlmChannel81OosPortn = _Pmopm2AlmChannel81OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 176, 1, 7),
    _Pmopm2AlmChannel81OosPortn_Type()
)
pmopm2AlmChannel81OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel81OosPortn.setStatus("current")
_Pmopm2Almchannel82PortTable_Object = MibTable
pmopm2Almchannel82PortTable = _Pmopm2Almchannel82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel82PortTable.setStatus("current")
_Pmopm2Almchannel82PortEntry_Object = MibTableRow
pmopm2Almchannel82PortEntry = _Pmopm2Almchannel82PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1)
)
pmopm2Almchannel82PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel82PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel82PortEntry.setStatus("current")


class _Pmopm2Almchannel82PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel82PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel82PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel82PortIndex_Object = MibTableColumn
pmopm2Almchannel82PortIndex = _Pmopm2Almchannel82PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1, 1),
    _Pmopm2Almchannel82PortIndex_Type()
)
pmopm2Almchannel82PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel82PortIndex.setStatus("current")
_Pmopm2AlmChannel82AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel82AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel82AbsentPortn = _Pmopm2AlmChannel82AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1, 2),
    _Pmopm2AlmChannel82AbsentPortn_Type()
)
pmopm2AlmChannel82AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel82AbsentPortn.setStatus("current")
_Pmopm2AlmChannel82MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel82MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel82MismatchPortn = _Pmopm2AlmChannel82MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1, 3),
    _Pmopm2AlmChannel82MismatchPortn_Type()
)
pmopm2AlmChannel82MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel82MismatchPortn.setStatus("current")
_Pmopm2AlmChannel82BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel82BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel82BalancedPortn = _Pmopm2AlmChannel82BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1, 4),
    _Pmopm2AlmChannel82BalancedPortn_Type()
)
pmopm2AlmChannel82BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel82BalancedPortn.setStatus("current")
_Pmopm2AlmChannel82PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel82PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel82PowerLowPortn = _Pmopm2AlmChannel82PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1, 5),
    _Pmopm2AlmChannel82PowerLowPortn_Type()
)
pmopm2AlmChannel82PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel82PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel82PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel82PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel82PowerHighPortn = _Pmopm2AlmChannel82PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1, 6),
    _Pmopm2AlmChannel82PowerHighPortn_Type()
)
pmopm2AlmChannel82PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel82PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel82OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel82OosPortn_Object = MibTableColumn
pmopm2AlmChannel82OosPortn = _Pmopm2AlmChannel82OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 178, 1, 7),
    _Pmopm2AlmChannel82OosPortn_Type()
)
pmopm2AlmChannel82OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel82OosPortn.setStatus("current")
_Pmopm2Almchannel83PortTable_Object = MibTable
pmopm2Almchannel83PortTable = _Pmopm2Almchannel83PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel83PortTable.setStatus("current")
_Pmopm2Almchannel83PortEntry_Object = MibTableRow
pmopm2Almchannel83PortEntry = _Pmopm2Almchannel83PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1)
)
pmopm2Almchannel83PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel83PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel83PortEntry.setStatus("current")


class _Pmopm2Almchannel83PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel83PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel83PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel83PortIndex_Object = MibTableColumn
pmopm2Almchannel83PortIndex = _Pmopm2Almchannel83PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1, 1),
    _Pmopm2Almchannel83PortIndex_Type()
)
pmopm2Almchannel83PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel83PortIndex.setStatus("current")
_Pmopm2AlmChannel83AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel83AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel83AbsentPortn = _Pmopm2AlmChannel83AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1, 2),
    _Pmopm2AlmChannel83AbsentPortn_Type()
)
pmopm2AlmChannel83AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel83AbsentPortn.setStatus("current")
_Pmopm2AlmChannel83MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel83MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel83MismatchPortn = _Pmopm2AlmChannel83MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1, 3),
    _Pmopm2AlmChannel83MismatchPortn_Type()
)
pmopm2AlmChannel83MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel83MismatchPortn.setStatus("current")
_Pmopm2AlmChannel83BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel83BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel83BalancedPortn = _Pmopm2AlmChannel83BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1, 4),
    _Pmopm2AlmChannel83BalancedPortn_Type()
)
pmopm2AlmChannel83BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel83BalancedPortn.setStatus("current")
_Pmopm2AlmChannel83PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel83PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel83PowerLowPortn = _Pmopm2AlmChannel83PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1, 5),
    _Pmopm2AlmChannel83PowerLowPortn_Type()
)
pmopm2AlmChannel83PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel83PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel83PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel83PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel83PowerHighPortn = _Pmopm2AlmChannel83PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1, 6),
    _Pmopm2AlmChannel83PowerHighPortn_Type()
)
pmopm2AlmChannel83PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel83PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel83OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel83OosPortn_Object = MibTableColumn
pmopm2AlmChannel83OosPortn = _Pmopm2AlmChannel83OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 180, 1, 7),
    _Pmopm2AlmChannel83OosPortn_Type()
)
pmopm2AlmChannel83OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel83OosPortn.setStatus("current")
_Pmopm2Almchannel84PortTable_Object = MibTable
pmopm2Almchannel84PortTable = _Pmopm2Almchannel84PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel84PortTable.setStatus("current")
_Pmopm2Almchannel84PortEntry_Object = MibTableRow
pmopm2Almchannel84PortEntry = _Pmopm2Almchannel84PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1)
)
pmopm2Almchannel84PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel84PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel84PortEntry.setStatus("current")


class _Pmopm2Almchannel84PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel84PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel84PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel84PortIndex_Object = MibTableColumn
pmopm2Almchannel84PortIndex = _Pmopm2Almchannel84PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1, 1),
    _Pmopm2Almchannel84PortIndex_Type()
)
pmopm2Almchannel84PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel84PortIndex.setStatus("current")
_Pmopm2AlmChannel84AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel84AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel84AbsentPortn = _Pmopm2AlmChannel84AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1, 2),
    _Pmopm2AlmChannel84AbsentPortn_Type()
)
pmopm2AlmChannel84AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel84AbsentPortn.setStatus("current")
_Pmopm2AlmChannel84MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel84MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel84MismatchPortn = _Pmopm2AlmChannel84MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1, 3),
    _Pmopm2AlmChannel84MismatchPortn_Type()
)
pmopm2AlmChannel84MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel84MismatchPortn.setStatus("current")
_Pmopm2AlmChannel84BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel84BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel84BalancedPortn = _Pmopm2AlmChannel84BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1, 4),
    _Pmopm2AlmChannel84BalancedPortn_Type()
)
pmopm2AlmChannel84BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel84BalancedPortn.setStatus("current")
_Pmopm2AlmChannel84PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel84PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel84PowerLowPortn = _Pmopm2AlmChannel84PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1, 5),
    _Pmopm2AlmChannel84PowerLowPortn_Type()
)
pmopm2AlmChannel84PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel84PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel84PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel84PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel84PowerHighPortn = _Pmopm2AlmChannel84PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1, 6),
    _Pmopm2AlmChannel84PowerHighPortn_Type()
)
pmopm2AlmChannel84PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel84PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel84OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel84OosPortn_Object = MibTableColumn
pmopm2AlmChannel84OosPortn = _Pmopm2AlmChannel84OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 182, 1, 7),
    _Pmopm2AlmChannel84OosPortn_Type()
)
pmopm2AlmChannel84OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel84OosPortn.setStatus("current")
_Pmopm2Almchannel85PortTable_Object = MibTable
pmopm2Almchannel85PortTable = _Pmopm2Almchannel85PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel85PortTable.setStatus("current")
_Pmopm2Almchannel85PortEntry_Object = MibTableRow
pmopm2Almchannel85PortEntry = _Pmopm2Almchannel85PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1)
)
pmopm2Almchannel85PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel85PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel85PortEntry.setStatus("current")


class _Pmopm2Almchannel85PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel85PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel85PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel85PortIndex_Object = MibTableColumn
pmopm2Almchannel85PortIndex = _Pmopm2Almchannel85PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1, 1),
    _Pmopm2Almchannel85PortIndex_Type()
)
pmopm2Almchannel85PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel85PortIndex.setStatus("current")
_Pmopm2AlmChannel85AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel85AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel85AbsentPortn = _Pmopm2AlmChannel85AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1, 2),
    _Pmopm2AlmChannel85AbsentPortn_Type()
)
pmopm2AlmChannel85AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel85AbsentPortn.setStatus("current")
_Pmopm2AlmChannel85MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel85MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel85MismatchPortn = _Pmopm2AlmChannel85MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1, 3),
    _Pmopm2AlmChannel85MismatchPortn_Type()
)
pmopm2AlmChannel85MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel85MismatchPortn.setStatus("current")
_Pmopm2AlmChannel85BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel85BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel85BalancedPortn = _Pmopm2AlmChannel85BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1, 4),
    _Pmopm2AlmChannel85BalancedPortn_Type()
)
pmopm2AlmChannel85BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel85BalancedPortn.setStatus("current")
_Pmopm2AlmChannel85PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel85PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel85PowerLowPortn = _Pmopm2AlmChannel85PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1, 5),
    _Pmopm2AlmChannel85PowerLowPortn_Type()
)
pmopm2AlmChannel85PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel85PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel85PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel85PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel85PowerHighPortn = _Pmopm2AlmChannel85PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1, 6),
    _Pmopm2AlmChannel85PowerHighPortn_Type()
)
pmopm2AlmChannel85PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel85PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel85OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel85OosPortn_Object = MibTableColumn
pmopm2AlmChannel85OosPortn = _Pmopm2AlmChannel85OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 184, 1, 7),
    _Pmopm2AlmChannel85OosPortn_Type()
)
pmopm2AlmChannel85OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel85OosPortn.setStatus("current")
_Pmopm2Almchannel86PortTable_Object = MibTable
pmopm2Almchannel86PortTable = _Pmopm2Almchannel86PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel86PortTable.setStatus("current")
_Pmopm2Almchannel86PortEntry_Object = MibTableRow
pmopm2Almchannel86PortEntry = _Pmopm2Almchannel86PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1)
)
pmopm2Almchannel86PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel86PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel86PortEntry.setStatus("current")


class _Pmopm2Almchannel86PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel86PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel86PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel86PortIndex_Object = MibTableColumn
pmopm2Almchannel86PortIndex = _Pmopm2Almchannel86PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1, 1),
    _Pmopm2Almchannel86PortIndex_Type()
)
pmopm2Almchannel86PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel86PortIndex.setStatus("current")
_Pmopm2AlmChannel86AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel86AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel86AbsentPortn = _Pmopm2AlmChannel86AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1, 2),
    _Pmopm2AlmChannel86AbsentPortn_Type()
)
pmopm2AlmChannel86AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel86AbsentPortn.setStatus("current")
_Pmopm2AlmChannel86MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel86MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel86MismatchPortn = _Pmopm2AlmChannel86MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1, 3),
    _Pmopm2AlmChannel86MismatchPortn_Type()
)
pmopm2AlmChannel86MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel86MismatchPortn.setStatus("current")
_Pmopm2AlmChannel86BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel86BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel86BalancedPortn = _Pmopm2AlmChannel86BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1, 4),
    _Pmopm2AlmChannel86BalancedPortn_Type()
)
pmopm2AlmChannel86BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel86BalancedPortn.setStatus("current")
_Pmopm2AlmChannel86PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel86PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel86PowerLowPortn = _Pmopm2AlmChannel86PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1, 5),
    _Pmopm2AlmChannel86PowerLowPortn_Type()
)
pmopm2AlmChannel86PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel86PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel86PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel86PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel86PowerHighPortn = _Pmopm2AlmChannel86PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1, 6),
    _Pmopm2AlmChannel86PowerHighPortn_Type()
)
pmopm2AlmChannel86PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel86PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel86OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel86OosPortn_Object = MibTableColumn
pmopm2AlmChannel86OosPortn = _Pmopm2AlmChannel86OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 186, 1, 7),
    _Pmopm2AlmChannel86OosPortn_Type()
)
pmopm2AlmChannel86OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel86OosPortn.setStatus("current")
_Pmopm2Almchannel87PortTable_Object = MibTable
pmopm2Almchannel87PortTable = _Pmopm2Almchannel87PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel87PortTable.setStatus("current")
_Pmopm2Almchannel87PortEntry_Object = MibTableRow
pmopm2Almchannel87PortEntry = _Pmopm2Almchannel87PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1)
)
pmopm2Almchannel87PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel87PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel87PortEntry.setStatus("current")


class _Pmopm2Almchannel87PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel87PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel87PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel87PortIndex_Object = MibTableColumn
pmopm2Almchannel87PortIndex = _Pmopm2Almchannel87PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1, 1),
    _Pmopm2Almchannel87PortIndex_Type()
)
pmopm2Almchannel87PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel87PortIndex.setStatus("current")
_Pmopm2AlmChannel87AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel87AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel87AbsentPortn = _Pmopm2AlmChannel87AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1, 2),
    _Pmopm2AlmChannel87AbsentPortn_Type()
)
pmopm2AlmChannel87AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel87AbsentPortn.setStatus("current")
_Pmopm2AlmChannel87MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel87MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel87MismatchPortn = _Pmopm2AlmChannel87MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1, 3),
    _Pmopm2AlmChannel87MismatchPortn_Type()
)
pmopm2AlmChannel87MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel87MismatchPortn.setStatus("current")
_Pmopm2AlmChannel87BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel87BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel87BalancedPortn = _Pmopm2AlmChannel87BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1, 4),
    _Pmopm2AlmChannel87BalancedPortn_Type()
)
pmopm2AlmChannel87BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel87BalancedPortn.setStatus("current")
_Pmopm2AlmChannel87PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel87PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel87PowerLowPortn = _Pmopm2AlmChannel87PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1, 5),
    _Pmopm2AlmChannel87PowerLowPortn_Type()
)
pmopm2AlmChannel87PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel87PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel87PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel87PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel87PowerHighPortn = _Pmopm2AlmChannel87PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1, 6),
    _Pmopm2AlmChannel87PowerHighPortn_Type()
)
pmopm2AlmChannel87PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel87PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel87OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel87OosPortn_Object = MibTableColumn
pmopm2AlmChannel87OosPortn = _Pmopm2AlmChannel87OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 188, 1, 7),
    _Pmopm2AlmChannel87OosPortn_Type()
)
pmopm2AlmChannel87OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel87OosPortn.setStatus("current")
_Pmopm2Almchannel88PortTable_Object = MibTable
pmopm2Almchannel88PortTable = _Pmopm2Almchannel88PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel88PortTable.setStatus("current")
_Pmopm2Almchannel88PortEntry_Object = MibTableRow
pmopm2Almchannel88PortEntry = _Pmopm2Almchannel88PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1)
)
pmopm2Almchannel88PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel88PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel88PortEntry.setStatus("current")


class _Pmopm2Almchannel88PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel88PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel88PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel88PortIndex_Object = MibTableColumn
pmopm2Almchannel88PortIndex = _Pmopm2Almchannel88PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1, 1),
    _Pmopm2Almchannel88PortIndex_Type()
)
pmopm2Almchannel88PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel88PortIndex.setStatus("current")
_Pmopm2AlmChannel88AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel88AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel88AbsentPortn = _Pmopm2AlmChannel88AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1, 2),
    _Pmopm2AlmChannel88AbsentPortn_Type()
)
pmopm2AlmChannel88AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel88AbsentPortn.setStatus("current")
_Pmopm2AlmChannel88MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel88MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel88MismatchPortn = _Pmopm2AlmChannel88MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1, 3),
    _Pmopm2AlmChannel88MismatchPortn_Type()
)
pmopm2AlmChannel88MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel88MismatchPortn.setStatus("current")
_Pmopm2AlmChannel88BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel88BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel88BalancedPortn = _Pmopm2AlmChannel88BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1, 4),
    _Pmopm2AlmChannel88BalancedPortn_Type()
)
pmopm2AlmChannel88BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel88BalancedPortn.setStatus("current")
_Pmopm2AlmChannel88PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel88PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel88PowerLowPortn = _Pmopm2AlmChannel88PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1, 5),
    _Pmopm2AlmChannel88PowerLowPortn_Type()
)
pmopm2AlmChannel88PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel88PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel88PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel88PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel88PowerHighPortn = _Pmopm2AlmChannel88PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1, 6),
    _Pmopm2AlmChannel88PowerHighPortn_Type()
)
pmopm2AlmChannel88PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel88PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel88OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel88OosPortn_Object = MibTableColumn
pmopm2AlmChannel88OosPortn = _Pmopm2AlmChannel88OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 190, 1, 7),
    _Pmopm2AlmChannel88OosPortn_Type()
)
pmopm2AlmChannel88OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel88OosPortn.setStatus("current")
_Pmopm2Almchannel89PortTable_Object = MibTable
pmopm2Almchannel89PortTable = _Pmopm2Almchannel89PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel89PortTable.setStatus("current")
_Pmopm2Almchannel89PortEntry_Object = MibTableRow
pmopm2Almchannel89PortEntry = _Pmopm2Almchannel89PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1)
)
pmopm2Almchannel89PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel89PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel89PortEntry.setStatus("current")


class _Pmopm2Almchannel89PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel89PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel89PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel89PortIndex_Object = MibTableColumn
pmopm2Almchannel89PortIndex = _Pmopm2Almchannel89PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1, 1),
    _Pmopm2Almchannel89PortIndex_Type()
)
pmopm2Almchannel89PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel89PortIndex.setStatus("current")
_Pmopm2AlmChannel89AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel89AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel89AbsentPortn = _Pmopm2AlmChannel89AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1, 2),
    _Pmopm2AlmChannel89AbsentPortn_Type()
)
pmopm2AlmChannel89AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel89AbsentPortn.setStatus("current")
_Pmopm2AlmChannel89MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel89MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel89MismatchPortn = _Pmopm2AlmChannel89MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1, 3),
    _Pmopm2AlmChannel89MismatchPortn_Type()
)
pmopm2AlmChannel89MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel89MismatchPortn.setStatus("current")
_Pmopm2AlmChannel89BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel89BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel89BalancedPortn = _Pmopm2AlmChannel89BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1, 4),
    _Pmopm2AlmChannel89BalancedPortn_Type()
)
pmopm2AlmChannel89BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel89BalancedPortn.setStatus("current")
_Pmopm2AlmChannel89PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel89PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel89PowerLowPortn = _Pmopm2AlmChannel89PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1, 5),
    _Pmopm2AlmChannel89PowerLowPortn_Type()
)
pmopm2AlmChannel89PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel89PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel89PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel89PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel89PowerHighPortn = _Pmopm2AlmChannel89PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1, 6),
    _Pmopm2AlmChannel89PowerHighPortn_Type()
)
pmopm2AlmChannel89PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel89PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel89OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel89OosPortn_Object = MibTableColumn
pmopm2AlmChannel89OosPortn = _Pmopm2AlmChannel89OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 192, 1, 7),
    _Pmopm2AlmChannel89OosPortn_Type()
)
pmopm2AlmChannel89OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel89OosPortn.setStatus("current")
_Pmopm2Almchannel90PortTable_Object = MibTable
pmopm2Almchannel90PortTable = _Pmopm2Almchannel90PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel90PortTable.setStatus("current")
_Pmopm2Almchannel90PortEntry_Object = MibTableRow
pmopm2Almchannel90PortEntry = _Pmopm2Almchannel90PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1)
)
pmopm2Almchannel90PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel90PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel90PortEntry.setStatus("current")


class _Pmopm2Almchannel90PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel90PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel90PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel90PortIndex_Object = MibTableColumn
pmopm2Almchannel90PortIndex = _Pmopm2Almchannel90PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1, 1),
    _Pmopm2Almchannel90PortIndex_Type()
)
pmopm2Almchannel90PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel90PortIndex.setStatus("current")
_Pmopm2AlmChannel90AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel90AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel90AbsentPortn = _Pmopm2AlmChannel90AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1, 2),
    _Pmopm2AlmChannel90AbsentPortn_Type()
)
pmopm2AlmChannel90AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel90AbsentPortn.setStatus("current")
_Pmopm2AlmChannel90MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel90MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel90MismatchPortn = _Pmopm2AlmChannel90MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1, 3),
    _Pmopm2AlmChannel90MismatchPortn_Type()
)
pmopm2AlmChannel90MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel90MismatchPortn.setStatus("current")
_Pmopm2AlmChannel90BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel90BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel90BalancedPortn = _Pmopm2AlmChannel90BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1, 4),
    _Pmopm2AlmChannel90BalancedPortn_Type()
)
pmopm2AlmChannel90BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel90BalancedPortn.setStatus("current")
_Pmopm2AlmChannel90PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel90PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel90PowerLowPortn = _Pmopm2AlmChannel90PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1, 5),
    _Pmopm2AlmChannel90PowerLowPortn_Type()
)
pmopm2AlmChannel90PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel90PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel90PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel90PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel90PowerHighPortn = _Pmopm2AlmChannel90PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1, 6),
    _Pmopm2AlmChannel90PowerHighPortn_Type()
)
pmopm2AlmChannel90PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel90PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel90OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel90OosPortn_Object = MibTableColumn
pmopm2AlmChannel90OosPortn = _Pmopm2AlmChannel90OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 194, 1, 7),
    _Pmopm2AlmChannel90OosPortn_Type()
)
pmopm2AlmChannel90OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel90OosPortn.setStatus("current")
_Pmopm2Almchannel91PortTable_Object = MibTable
pmopm2Almchannel91PortTable = _Pmopm2Almchannel91PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel91PortTable.setStatus("current")
_Pmopm2Almchannel91PortEntry_Object = MibTableRow
pmopm2Almchannel91PortEntry = _Pmopm2Almchannel91PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1)
)
pmopm2Almchannel91PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel91PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel91PortEntry.setStatus("current")


class _Pmopm2Almchannel91PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel91PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel91PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel91PortIndex_Object = MibTableColumn
pmopm2Almchannel91PortIndex = _Pmopm2Almchannel91PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1, 1),
    _Pmopm2Almchannel91PortIndex_Type()
)
pmopm2Almchannel91PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel91PortIndex.setStatus("current")
_Pmopm2AlmChannel91AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel91AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel91AbsentPortn = _Pmopm2AlmChannel91AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1, 2),
    _Pmopm2AlmChannel91AbsentPortn_Type()
)
pmopm2AlmChannel91AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel91AbsentPortn.setStatus("current")
_Pmopm2AlmChannel91MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel91MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel91MismatchPortn = _Pmopm2AlmChannel91MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1, 3),
    _Pmopm2AlmChannel91MismatchPortn_Type()
)
pmopm2AlmChannel91MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel91MismatchPortn.setStatus("current")
_Pmopm2AlmChannel91BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel91BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel91BalancedPortn = _Pmopm2AlmChannel91BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1, 4),
    _Pmopm2AlmChannel91BalancedPortn_Type()
)
pmopm2AlmChannel91BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel91BalancedPortn.setStatus("current")
_Pmopm2AlmChannel91PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel91PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel91PowerLowPortn = _Pmopm2AlmChannel91PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1, 5),
    _Pmopm2AlmChannel91PowerLowPortn_Type()
)
pmopm2AlmChannel91PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel91PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel91PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel91PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel91PowerHighPortn = _Pmopm2AlmChannel91PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1, 6),
    _Pmopm2AlmChannel91PowerHighPortn_Type()
)
pmopm2AlmChannel91PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel91PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel91OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel91OosPortn_Object = MibTableColumn
pmopm2AlmChannel91OosPortn = _Pmopm2AlmChannel91OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 196, 1, 7),
    _Pmopm2AlmChannel91OosPortn_Type()
)
pmopm2AlmChannel91OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel91OosPortn.setStatus("current")
_Pmopm2Almchannel92PortTable_Object = MibTable
pmopm2Almchannel92PortTable = _Pmopm2Almchannel92PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel92PortTable.setStatus("current")
_Pmopm2Almchannel92PortEntry_Object = MibTableRow
pmopm2Almchannel92PortEntry = _Pmopm2Almchannel92PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1)
)
pmopm2Almchannel92PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel92PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel92PortEntry.setStatus("current")


class _Pmopm2Almchannel92PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel92PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel92PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel92PortIndex_Object = MibTableColumn
pmopm2Almchannel92PortIndex = _Pmopm2Almchannel92PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1, 1),
    _Pmopm2Almchannel92PortIndex_Type()
)
pmopm2Almchannel92PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel92PortIndex.setStatus("current")
_Pmopm2AlmChannel92AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel92AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel92AbsentPortn = _Pmopm2AlmChannel92AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1, 2),
    _Pmopm2AlmChannel92AbsentPortn_Type()
)
pmopm2AlmChannel92AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel92AbsentPortn.setStatus("current")
_Pmopm2AlmChannel92MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel92MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel92MismatchPortn = _Pmopm2AlmChannel92MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1, 3),
    _Pmopm2AlmChannel92MismatchPortn_Type()
)
pmopm2AlmChannel92MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel92MismatchPortn.setStatus("current")
_Pmopm2AlmChannel92BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel92BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel92BalancedPortn = _Pmopm2AlmChannel92BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1, 4),
    _Pmopm2AlmChannel92BalancedPortn_Type()
)
pmopm2AlmChannel92BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel92BalancedPortn.setStatus("current")
_Pmopm2AlmChannel92PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel92PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel92PowerLowPortn = _Pmopm2AlmChannel92PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1, 5),
    _Pmopm2AlmChannel92PowerLowPortn_Type()
)
pmopm2AlmChannel92PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel92PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel92PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel92PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel92PowerHighPortn = _Pmopm2AlmChannel92PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1, 6),
    _Pmopm2AlmChannel92PowerHighPortn_Type()
)
pmopm2AlmChannel92PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel92PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel92OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel92OosPortn_Object = MibTableColumn
pmopm2AlmChannel92OosPortn = _Pmopm2AlmChannel92OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 198, 1, 7),
    _Pmopm2AlmChannel92OosPortn_Type()
)
pmopm2AlmChannel92OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel92OosPortn.setStatus("current")
_Pmopm2Almchannel93PortTable_Object = MibTable
pmopm2Almchannel93PortTable = _Pmopm2Almchannel93PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel93PortTable.setStatus("current")
_Pmopm2Almchannel93PortEntry_Object = MibTableRow
pmopm2Almchannel93PortEntry = _Pmopm2Almchannel93PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1)
)
pmopm2Almchannel93PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel93PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel93PortEntry.setStatus("current")


class _Pmopm2Almchannel93PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel93PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel93PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel93PortIndex_Object = MibTableColumn
pmopm2Almchannel93PortIndex = _Pmopm2Almchannel93PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1, 1),
    _Pmopm2Almchannel93PortIndex_Type()
)
pmopm2Almchannel93PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel93PortIndex.setStatus("current")
_Pmopm2AlmChannel93AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel93AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel93AbsentPortn = _Pmopm2AlmChannel93AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1, 2),
    _Pmopm2AlmChannel93AbsentPortn_Type()
)
pmopm2AlmChannel93AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel93AbsentPortn.setStatus("current")
_Pmopm2AlmChannel93MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel93MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel93MismatchPortn = _Pmopm2AlmChannel93MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1, 3),
    _Pmopm2AlmChannel93MismatchPortn_Type()
)
pmopm2AlmChannel93MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel93MismatchPortn.setStatus("current")
_Pmopm2AlmChannel93BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel93BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel93BalancedPortn = _Pmopm2AlmChannel93BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1, 4),
    _Pmopm2AlmChannel93BalancedPortn_Type()
)
pmopm2AlmChannel93BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel93BalancedPortn.setStatus("current")
_Pmopm2AlmChannel93PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel93PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel93PowerLowPortn = _Pmopm2AlmChannel93PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1, 5),
    _Pmopm2AlmChannel93PowerLowPortn_Type()
)
pmopm2AlmChannel93PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel93PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel93PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel93PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel93PowerHighPortn = _Pmopm2AlmChannel93PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1, 6),
    _Pmopm2AlmChannel93PowerHighPortn_Type()
)
pmopm2AlmChannel93PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel93PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel93OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel93OosPortn_Object = MibTableColumn
pmopm2AlmChannel93OosPortn = _Pmopm2AlmChannel93OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 200, 1, 7),
    _Pmopm2AlmChannel93OosPortn_Type()
)
pmopm2AlmChannel93OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel93OosPortn.setStatus("current")
_Pmopm2Almchannel94PortTable_Object = MibTable
pmopm2Almchannel94PortTable = _Pmopm2Almchannel94PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel94PortTable.setStatus("current")
_Pmopm2Almchannel94PortEntry_Object = MibTableRow
pmopm2Almchannel94PortEntry = _Pmopm2Almchannel94PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1)
)
pmopm2Almchannel94PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel94PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel94PortEntry.setStatus("current")


class _Pmopm2Almchannel94PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel94PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel94PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel94PortIndex_Object = MibTableColumn
pmopm2Almchannel94PortIndex = _Pmopm2Almchannel94PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1, 1),
    _Pmopm2Almchannel94PortIndex_Type()
)
pmopm2Almchannel94PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel94PortIndex.setStatus("current")
_Pmopm2AlmChannel94AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel94AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel94AbsentPortn = _Pmopm2AlmChannel94AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1, 2),
    _Pmopm2AlmChannel94AbsentPortn_Type()
)
pmopm2AlmChannel94AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel94AbsentPortn.setStatus("current")
_Pmopm2AlmChannel94MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel94MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel94MismatchPortn = _Pmopm2AlmChannel94MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1, 3),
    _Pmopm2AlmChannel94MismatchPortn_Type()
)
pmopm2AlmChannel94MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel94MismatchPortn.setStatus("current")
_Pmopm2AlmChannel94BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel94BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel94BalancedPortn = _Pmopm2AlmChannel94BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1, 4),
    _Pmopm2AlmChannel94BalancedPortn_Type()
)
pmopm2AlmChannel94BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel94BalancedPortn.setStatus("current")
_Pmopm2AlmChannel94PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel94PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel94PowerLowPortn = _Pmopm2AlmChannel94PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1, 5),
    _Pmopm2AlmChannel94PowerLowPortn_Type()
)
pmopm2AlmChannel94PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel94PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel94PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel94PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel94PowerHighPortn = _Pmopm2AlmChannel94PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1, 6),
    _Pmopm2AlmChannel94PowerHighPortn_Type()
)
pmopm2AlmChannel94PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel94PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel94OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel94OosPortn_Object = MibTableColumn
pmopm2AlmChannel94OosPortn = _Pmopm2AlmChannel94OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 202, 1, 7),
    _Pmopm2AlmChannel94OosPortn_Type()
)
pmopm2AlmChannel94OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel94OosPortn.setStatus("current")
_Pmopm2Almchannel95PortTable_Object = MibTable
pmopm2Almchannel95PortTable = _Pmopm2Almchannel95PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel95PortTable.setStatus("current")
_Pmopm2Almchannel95PortEntry_Object = MibTableRow
pmopm2Almchannel95PortEntry = _Pmopm2Almchannel95PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1)
)
pmopm2Almchannel95PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel95PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel95PortEntry.setStatus("current")


class _Pmopm2Almchannel95PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel95PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel95PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel95PortIndex_Object = MibTableColumn
pmopm2Almchannel95PortIndex = _Pmopm2Almchannel95PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1, 1),
    _Pmopm2Almchannel95PortIndex_Type()
)
pmopm2Almchannel95PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel95PortIndex.setStatus("current")
_Pmopm2AlmChannel95AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel95AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel95AbsentPortn = _Pmopm2AlmChannel95AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1, 2),
    _Pmopm2AlmChannel95AbsentPortn_Type()
)
pmopm2AlmChannel95AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel95AbsentPortn.setStatus("current")
_Pmopm2AlmChannel95MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel95MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel95MismatchPortn = _Pmopm2AlmChannel95MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1, 3),
    _Pmopm2AlmChannel95MismatchPortn_Type()
)
pmopm2AlmChannel95MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel95MismatchPortn.setStatus("current")
_Pmopm2AlmChannel95BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel95BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel95BalancedPortn = _Pmopm2AlmChannel95BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1, 4),
    _Pmopm2AlmChannel95BalancedPortn_Type()
)
pmopm2AlmChannel95BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel95BalancedPortn.setStatus("current")
_Pmopm2AlmChannel95PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel95PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel95PowerLowPortn = _Pmopm2AlmChannel95PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1, 5),
    _Pmopm2AlmChannel95PowerLowPortn_Type()
)
pmopm2AlmChannel95PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel95PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel95PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel95PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel95PowerHighPortn = _Pmopm2AlmChannel95PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1, 6),
    _Pmopm2AlmChannel95PowerHighPortn_Type()
)
pmopm2AlmChannel95PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel95PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel95OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel95OosPortn_Object = MibTableColumn
pmopm2AlmChannel95OosPortn = _Pmopm2AlmChannel95OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 204, 1, 7),
    _Pmopm2AlmChannel95OosPortn_Type()
)
pmopm2AlmChannel95OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel95OosPortn.setStatus("current")
_Pmopm2Almchannel96PortTable_Object = MibTable
pmopm2Almchannel96PortTable = _Pmopm2Almchannel96PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206)
)
if mibBuilder.loadTexts:
    pmopm2Almchannel96PortTable.setStatus("current")
_Pmopm2Almchannel96PortEntry_Object = MibTableRow
pmopm2Almchannel96PortEntry = _Pmopm2Almchannel96PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1)
)
pmopm2Almchannel96PortEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Almchannel96PortIndex"),
)
if mibBuilder.loadTexts:
    pmopm2Almchannel96PortEntry.setStatus("current")


class _Pmopm2Almchannel96PortIndex_Type(Integer32):
    """Custom type pmopm2Almchannel96PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Almchannel96PortIndex_Type.__name__ = "Integer32"
_Pmopm2Almchannel96PortIndex_Object = MibTableColumn
pmopm2Almchannel96PortIndex = _Pmopm2Almchannel96PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1, 1),
    _Pmopm2Almchannel96PortIndex_Type()
)
pmopm2Almchannel96PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Almchannel96PortIndex.setStatus("current")
_Pmopm2AlmChannel96AbsentPortn_Type = EkiOnOff
_Pmopm2AlmChannel96AbsentPortn_Object = MibTableColumn
pmopm2AlmChannel96AbsentPortn = _Pmopm2AlmChannel96AbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1, 2),
    _Pmopm2AlmChannel96AbsentPortn_Type()
)
pmopm2AlmChannel96AbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel96AbsentPortn.setStatus("current")
_Pmopm2AlmChannel96MismatchPortn_Type = EkiOnOff
_Pmopm2AlmChannel96MismatchPortn_Object = MibTableColumn
pmopm2AlmChannel96MismatchPortn = _Pmopm2AlmChannel96MismatchPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1, 3),
    _Pmopm2AlmChannel96MismatchPortn_Type()
)
pmopm2AlmChannel96MismatchPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel96MismatchPortn.setStatus("current")
_Pmopm2AlmChannel96BalancedPortn_Type = EkiOnOff
_Pmopm2AlmChannel96BalancedPortn_Object = MibTableColumn
pmopm2AlmChannel96BalancedPortn = _Pmopm2AlmChannel96BalancedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1, 4),
    _Pmopm2AlmChannel96BalancedPortn_Type()
)
pmopm2AlmChannel96BalancedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel96BalancedPortn.setStatus("current")
_Pmopm2AlmChannel96PowerLowPortn_Type = EkiOnOff
_Pmopm2AlmChannel96PowerLowPortn_Object = MibTableColumn
pmopm2AlmChannel96PowerLowPortn = _Pmopm2AlmChannel96PowerLowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1, 5),
    _Pmopm2AlmChannel96PowerLowPortn_Type()
)
pmopm2AlmChannel96PowerLowPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel96PowerLowPortn.setStatus("current")
_Pmopm2AlmChannel96PowerHighPortn_Type = EkiOnOff
_Pmopm2AlmChannel96PowerHighPortn_Object = MibTableColumn
pmopm2AlmChannel96PowerHighPortn = _Pmopm2AlmChannel96PowerHighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1, 6),
    _Pmopm2AlmChannel96PowerHighPortn_Type()
)
pmopm2AlmChannel96PowerHighPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel96PowerHighPortn.setStatus("current")
_Pmopm2AlmChannel96OosPortn_Type = EkiOnOff
_Pmopm2AlmChannel96OosPortn_Object = MibTableColumn
pmopm2AlmChannel96OosPortn = _Pmopm2AlmChannel96OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 2, 3, 206, 1, 7),
    _Pmopm2AlmChannel96OosPortn_Type()
)
pmopm2AlmChannel96OosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2AlmChannel96OosPortn.setStatus("current")
_Pmopm2AlmLine_ObjectIdentity = ObjectIdentity
pmopm2AlmLine = _Pmopm2AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 3)
)
_Pmopm2AlmLineNurg_ObjectIdentity = ObjectIdentity
pmopm2AlmLineNurg = _Pmopm2AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 3, 1)
)
_Pmopm2AlmLineUrg_ObjectIdentity = ObjectIdentity
pmopm2AlmLineUrg = _Pmopm2AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 3, 2)
)
_Pmopm2AlmLineCrit_ObjectIdentity = ObjectIdentity
pmopm2AlmLineCrit = _Pmopm2AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 2, 3, 3)
)
_Pmopm2measures_ObjectIdentity = ObjectIdentity
pmopm2measures = _Pmopm2measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3)
)
_Pmopm2MesrOther_ObjectIdentity = ObjectIdentity
pmopm2MesrOther = _Pmopm2MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 1)
)


class _Pmopm2MesropmTemp_Type(Unsigned32):
    """Custom type pmopm2MesropmTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2MesropmTemp_Type.__name__ = "Unsigned32"
_Pmopm2MesropmTemp_Object = MibScalar
pmopm2MesropmTemp = _Pmopm2MesropmTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 1, 248),
    _Pmopm2MesropmTemp_Type()
)
pmopm2MesropmTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2MesropmTemp.setStatus("current")
_Pmopm2MesrClient_ObjectIdentity = ObjectIdentity
pmopm2MesrClient = _Pmopm2MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2)
)
_Pmopm2Mesrchannel1Table_Object = MibTable
pmopm2Mesrchannel1Table = _Pmopm2Mesrchannel1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel1Table.setStatus("current")
_Pmopm2Mesrchannel1Entry_Object = MibTableRow
pmopm2Mesrchannel1Entry = _Pmopm2Mesrchannel1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 16, 1)
)
pmopm2Mesrchannel1Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel1Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel1Entry.setStatus("current")


class _Pmopm2Mesrchannel1Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel1Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel1Index_Object = MibTableColumn
pmopm2Mesrchannel1Index = _Pmopm2Mesrchannel1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 16, 1, 1),
    _Pmopm2Mesrchannel1Index_Type()
)
pmopm2Mesrchannel1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel1Index.setStatus("current")


class _Pmopm2Mesrchannel1Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel1Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel1Portn_Object = MibTableColumn
pmopm2Mesrchannel1Portn = _Pmopm2Mesrchannel1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 16, 1, 2),
    _Pmopm2Mesrchannel1Portn_Type()
)
pmopm2Mesrchannel1Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel1Portn.setStatus("current")
_Pmopm2Mesrchannel2Table_Object = MibTable
pmopm2Mesrchannel2Table = _Pmopm2Mesrchannel2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 18)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel2Table.setStatus("current")
_Pmopm2Mesrchannel2Entry_Object = MibTableRow
pmopm2Mesrchannel2Entry = _Pmopm2Mesrchannel2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 18, 1)
)
pmopm2Mesrchannel2Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel2Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel2Entry.setStatus("current")


class _Pmopm2Mesrchannel2Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel2Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel2Index_Object = MibTableColumn
pmopm2Mesrchannel2Index = _Pmopm2Mesrchannel2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 18, 1, 1),
    _Pmopm2Mesrchannel2Index_Type()
)
pmopm2Mesrchannel2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel2Index.setStatus("current")


class _Pmopm2Mesrchannel2Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel2Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel2Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel2Portn_Object = MibTableColumn
pmopm2Mesrchannel2Portn = _Pmopm2Mesrchannel2Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 18, 1, 2),
    _Pmopm2Mesrchannel2Portn_Type()
)
pmopm2Mesrchannel2Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel2Portn.setStatus("current")
_Pmopm2Mesrchannel3Table_Object = MibTable
pmopm2Mesrchannel3Table = _Pmopm2Mesrchannel3Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 20)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel3Table.setStatus("current")
_Pmopm2Mesrchannel3Entry_Object = MibTableRow
pmopm2Mesrchannel3Entry = _Pmopm2Mesrchannel3Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 20, 1)
)
pmopm2Mesrchannel3Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel3Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel3Entry.setStatus("current")


class _Pmopm2Mesrchannel3Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel3Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel3Index_Object = MibTableColumn
pmopm2Mesrchannel3Index = _Pmopm2Mesrchannel3Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 20, 1, 1),
    _Pmopm2Mesrchannel3Index_Type()
)
pmopm2Mesrchannel3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel3Index.setStatus("current")


class _Pmopm2Mesrchannel3Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel3Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel3Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel3Portn_Object = MibTableColumn
pmopm2Mesrchannel3Portn = _Pmopm2Mesrchannel3Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 20, 1, 2),
    _Pmopm2Mesrchannel3Portn_Type()
)
pmopm2Mesrchannel3Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel3Portn.setStatus("current")
_Pmopm2Mesrchannel4Table_Object = MibTable
pmopm2Mesrchannel4Table = _Pmopm2Mesrchannel4Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 22)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel4Table.setStatus("current")
_Pmopm2Mesrchannel4Entry_Object = MibTableRow
pmopm2Mesrchannel4Entry = _Pmopm2Mesrchannel4Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 22, 1)
)
pmopm2Mesrchannel4Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel4Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel4Entry.setStatus("current")


class _Pmopm2Mesrchannel4Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel4Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel4Index_Object = MibTableColumn
pmopm2Mesrchannel4Index = _Pmopm2Mesrchannel4Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 22, 1, 1),
    _Pmopm2Mesrchannel4Index_Type()
)
pmopm2Mesrchannel4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel4Index.setStatus("current")


class _Pmopm2Mesrchannel4Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel4Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel4Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel4Portn_Object = MibTableColumn
pmopm2Mesrchannel4Portn = _Pmopm2Mesrchannel4Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 22, 1, 2),
    _Pmopm2Mesrchannel4Portn_Type()
)
pmopm2Mesrchannel4Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel4Portn.setStatus("current")
_Pmopm2Mesrchannel5Table_Object = MibTable
pmopm2Mesrchannel5Table = _Pmopm2Mesrchannel5Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel5Table.setStatus("current")
_Pmopm2Mesrchannel5Entry_Object = MibTableRow
pmopm2Mesrchannel5Entry = _Pmopm2Mesrchannel5Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 24, 1)
)
pmopm2Mesrchannel5Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel5Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel5Entry.setStatus("current")


class _Pmopm2Mesrchannel5Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel5Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel5Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel5Index_Object = MibTableColumn
pmopm2Mesrchannel5Index = _Pmopm2Mesrchannel5Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 24, 1, 1),
    _Pmopm2Mesrchannel5Index_Type()
)
pmopm2Mesrchannel5Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel5Index.setStatus("current")


class _Pmopm2Mesrchannel5Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel5Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel5Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel5Portn_Object = MibTableColumn
pmopm2Mesrchannel5Portn = _Pmopm2Mesrchannel5Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 24, 1, 2),
    _Pmopm2Mesrchannel5Portn_Type()
)
pmopm2Mesrchannel5Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel5Portn.setStatus("current")
_Pmopm2Mesrchannel6Table_Object = MibTable
pmopm2Mesrchannel6Table = _Pmopm2Mesrchannel6Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 26)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel6Table.setStatus("current")
_Pmopm2Mesrchannel6Entry_Object = MibTableRow
pmopm2Mesrchannel6Entry = _Pmopm2Mesrchannel6Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 26, 1)
)
pmopm2Mesrchannel6Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel6Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel6Entry.setStatus("current")


class _Pmopm2Mesrchannel6Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel6Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel6Index_Object = MibTableColumn
pmopm2Mesrchannel6Index = _Pmopm2Mesrchannel6Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 26, 1, 1),
    _Pmopm2Mesrchannel6Index_Type()
)
pmopm2Mesrchannel6Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel6Index.setStatus("current")


class _Pmopm2Mesrchannel6Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel6Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel6Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel6Portn_Object = MibTableColumn
pmopm2Mesrchannel6Portn = _Pmopm2Mesrchannel6Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 26, 1, 2),
    _Pmopm2Mesrchannel6Portn_Type()
)
pmopm2Mesrchannel6Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel6Portn.setStatus("current")
_Pmopm2Mesrchannel7Table_Object = MibTable
pmopm2Mesrchannel7Table = _Pmopm2Mesrchannel7Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 28)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel7Table.setStatus("current")
_Pmopm2Mesrchannel7Entry_Object = MibTableRow
pmopm2Mesrchannel7Entry = _Pmopm2Mesrchannel7Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 28, 1)
)
pmopm2Mesrchannel7Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel7Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel7Entry.setStatus("current")


class _Pmopm2Mesrchannel7Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel7Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel7Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel7Index_Object = MibTableColumn
pmopm2Mesrchannel7Index = _Pmopm2Mesrchannel7Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 28, 1, 1),
    _Pmopm2Mesrchannel7Index_Type()
)
pmopm2Mesrchannel7Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel7Index.setStatus("current")


class _Pmopm2Mesrchannel7Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel7Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel7Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel7Portn_Object = MibTableColumn
pmopm2Mesrchannel7Portn = _Pmopm2Mesrchannel7Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 28, 1, 2),
    _Pmopm2Mesrchannel7Portn_Type()
)
pmopm2Mesrchannel7Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel7Portn.setStatus("current")
_Pmopm2Mesrchannel8Table_Object = MibTable
pmopm2Mesrchannel8Table = _Pmopm2Mesrchannel8Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 30)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel8Table.setStatus("current")
_Pmopm2Mesrchannel8Entry_Object = MibTableRow
pmopm2Mesrchannel8Entry = _Pmopm2Mesrchannel8Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 30, 1)
)
pmopm2Mesrchannel8Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel8Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel8Entry.setStatus("current")


class _Pmopm2Mesrchannel8Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel8Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel8Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel8Index_Object = MibTableColumn
pmopm2Mesrchannel8Index = _Pmopm2Mesrchannel8Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 30, 1, 1),
    _Pmopm2Mesrchannel8Index_Type()
)
pmopm2Mesrchannel8Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel8Index.setStatus("current")


class _Pmopm2Mesrchannel8Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel8Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel8Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel8Portn_Object = MibTableColumn
pmopm2Mesrchannel8Portn = _Pmopm2Mesrchannel8Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 30, 1, 2),
    _Pmopm2Mesrchannel8Portn_Type()
)
pmopm2Mesrchannel8Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel8Portn.setStatus("current")
_Pmopm2Mesrchannel9Table_Object = MibTable
pmopm2Mesrchannel9Table = _Pmopm2Mesrchannel9Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel9Table.setStatus("current")
_Pmopm2Mesrchannel9Entry_Object = MibTableRow
pmopm2Mesrchannel9Entry = _Pmopm2Mesrchannel9Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 32, 1)
)
pmopm2Mesrchannel9Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel9Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel9Entry.setStatus("current")


class _Pmopm2Mesrchannel9Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel9Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel9Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel9Index_Object = MibTableColumn
pmopm2Mesrchannel9Index = _Pmopm2Mesrchannel9Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 32, 1, 1),
    _Pmopm2Mesrchannel9Index_Type()
)
pmopm2Mesrchannel9Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel9Index.setStatus("current")


class _Pmopm2Mesrchannel9Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel9Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel9Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel9Portn_Object = MibTableColumn
pmopm2Mesrchannel9Portn = _Pmopm2Mesrchannel9Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 32, 1, 2),
    _Pmopm2Mesrchannel9Portn_Type()
)
pmopm2Mesrchannel9Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel9Portn.setStatus("current")
_Pmopm2Mesrchannel10Table_Object = MibTable
pmopm2Mesrchannel10Table = _Pmopm2Mesrchannel10Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 34)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel10Table.setStatus("current")
_Pmopm2Mesrchannel10Entry_Object = MibTableRow
pmopm2Mesrchannel10Entry = _Pmopm2Mesrchannel10Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 34, 1)
)
pmopm2Mesrchannel10Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel10Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel10Entry.setStatus("current")


class _Pmopm2Mesrchannel10Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel10Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel10Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel10Index_Object = MibTableColumn
pmopm2Mesrchannel10Index = _Pmopm2Mesrchannel10Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 34, 1, 1),
    _Pmopm2Mesrchannel10Index_Type()
)
pmopm2Mesrchannel10Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel10Index.setStatus("current")


class _Pmopm2Mesrchannel10Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel10Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel10Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel10Portn_Object = MibTableColumn
pmopm2Mesrchannel10Portn = _Pmopm2Mesrchannel10Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 34, 1, 2),
    _Pmopm2Mesrchannel10Portn_Type()
)
pmopm2Mesrchannel10Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel10Portn.setStatus("current")
_Pmopm2Mesrchannel11Table_Object = MibTable
pmopm2Mesrchannel11Table = _Pmopm2Mesrchannel11Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 36)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel11Table.setStatus("current")
_Pmopm2Mesrchannel11Entry_Object = MibTableRow
pmopm2Mesrchannel11Entry = _Pmopm2Mesrchannel11Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 36, 1)
)
pmopm2Mesrchannel11Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel11Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel11Entry.setStatus("current")


class _Pmopm2Mesrchannel11Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel11Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel11Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel11Index_Object = MibTableColumn
pmopm2Mesrchannel11Index = _Pmopm2Mesrchannel11Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 36, 1, 1),
    _Pmopm2Mesrchannel11Index_Type()
)
pmopm2Mesrchannel11Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel11Index.setStatus("current")


class _Pmopm2Mesrchannel11Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel11Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel11Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel11Portn_Object = MibTableColumn
pmopm2Mesrchannel11Portn = _Pmopm2Mesrchannel11Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 36, 1, 2),
    _Pmopm2Mesrchannel11Portn_Type()
)
pmopm2Mesrchannel11Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel11Portn.setStatus("current")
_Pmopm2Mesrchannel12Table_Object = MibTable
pmopm2Mesrchannel12Table = _Pmopm2Mesrchannel12Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 38)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel12Table.setStatus("current")
_Pmopm2Mesrchannel12Entry_Object = MibTableRow
pmopm2Mesrchannel12Entry = _Pmopm2Mesrchannel12Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 38, 1)
)
pmopm2Mesrchannel12Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel12Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel12Entry.setStatus("current")


class _Pmopm2Mesrchannel12Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel12Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel12Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel12Index_Object = MibTableColumn
pmopm2Mesrchannel12Index = _Pmopm2Mesrchannel12Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 38, 1, 1),
    _Pmopm2Mesrchannel12Index_Type()
)
pmopm2Mesrchannel12Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel12Index.setStatus("current")


class _Pmopm2Mesrchannel12Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel12Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel12Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel12Portn_Object = MibTableColumn
pmopm2Mesrchannel12Portn = _Pmopm2Mesrchannel12Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 38, 1, 2),
    _Pmopm2Mesrchannel12Portn_Type()
)
pmopm2Mesrchannel12Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel12Portn.setStatus("current")
_Pmopm2Mesrchannel13Table_Object = MibTable
pmopm2Mesrchannel13Table = _Pmopm2Mesrchannel13Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel13Table.setStatus("current")
_Pmopm2Mesrchannel13Entry_Object = MibTableRow
pmopm2Mesrchannel13Entry = _Pmopm2Mesrchannel13Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 40, 1)
)
pmopm2Mesrchannel13Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel13Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel13Entry.setStatus("current")


class _Pmopm2Mesrchannel13Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel13Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel13Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel13Index_Object = MibTableColumn
pmopm2Mesrchannel13Index = _Pmopm2Mesrchannel13Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 40, 1, 1),
    _Pmopm2Mesrchannel13Index_Type()
)
pmopm2Mesrchannel13Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel13Index.setStatus("current")


class _Pmopm2Mesrchannel13Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel13Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel13Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel13Portn_Object = MibTableColumn
pmopm2Mesrchannel13Portn = _Pmopm2Mesrchannel13Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 40, 1, 2),
    _Pmopm2Mesrchannel13Portn_Type()
)
pmopm2Mesrchannel13Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel13Portn.setStatus("current")
_Pmopm2Mesrchannel14Table_Object = MibTable
pmopm2Mesrchannel14Table = _Pmopm2Mesrchannel14Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 42)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel14Table.setStatus("current")
_Pmopm2Mesrchannel14Entry_Object = MibTableRow
pmopm2Mesrchannel14Entry = _Pmopm2Mesrchannel14Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 42, 1)
)
pmopm2Mesrchannel14Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel14Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel14Entry.setStatus("current")


class _Pmopm2Mesrchannel14Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel14Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel14Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel14Index_Object = MibTableColumn
pmopm2Mesrchannel14Index = _Pmopm2Mesrchannel14Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 42, 1, 1),
    _Pmopm2Mesrchannel14Index_Type()
)
pmopm2Mesrchannel14Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel14Index.setStatus("current")


class _Pmopm2Mesrchannel14Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel14Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel14Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel14Portn_Object = MibTableColumn
pmopm2Mesrchannel14Portn = _Pmopm2Mesrchannel14Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 42, 1, 2),
    _Pmopm2Mesrchannel14Portn_Type()
)
pmopm2Mesrchannel14Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel14Portn.setStatus("current")
_Pmopm2Mesrchannel15Table_Object = MibTable
pmopm2Mesrchannel15Table = _Pmopm2Mesrchannel15Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 44)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel15Table.setStatus("current")
_Pmopm2Mesrchannel15Entry_Object = MibTableRow
pmopm2Mesrchannel15Entry = _Pmopm2Mesrchannel15Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 44, 1)
)
pmopm2Mesrchannel15Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel15Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel15Entry.setStatus("current")


class _Pmopm2Mesrchannel15Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel15Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel15Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel15Index_Object = MibTableColumn
pmopm2Mesrchannel15Index = _Pmopm2Mesrchannel15Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 44, 1, 1),
    _Pmopm2Mesrchannel15Index_Type()
)
pmopm2Mesrchannel15Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel15Index.setStatus("current")


class _Pmopm2Mesrchannel15Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel15Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel15Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel15Portn_Object = MibTableColumn
pmopm2Mesrchannel15Portn = _Pmopm2Mesrchannel15Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 44, 1, 2),
    _Pmopm2Mesrchannel15Portn_Type()
)
pmopm2Mesrchannel15Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel15Portn.setStatus("current")
_Pmopm2Mesrchannel16Table_Object = MibTable
pmopm2Mesrchannel16Table = _Pmopm2Mesrchannel16Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 46)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel16Table.setStatus("current")
_Pmopm2Mesrchannel16Entry_Object = MibTableRow
pmopm2Mesrchannel16Entry = _Pmopm2Mesrchannel16Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 46, 1)
)
pmopm2Mesrchannel16Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel16Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel16Entry.setStatus("current")


class _Pmopm2Mesrchannel16Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel16Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel16Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel16Index_Object = MibTableColumn
pmopm2Mesrchannel16Index = _Pmopm2Mesrchannel16Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 46, 1, 1),
    _Pmopm2Mesrchannel16Index_Type()
)
pmopm2Mesrchannel16Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel16Index.setStatus("current")


class _Pmopm2Mesrchannel16Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel16Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel16Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel16Portn_Object = MibTableColumn
pmopm2Mesrchannel16Portn = _Pmopm2Mesrchannel16Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 46, 1, 2),
    _Pmopm2Mesrchannel16Portn_Type()
)
pmopm2Mesrchannel16Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel16Portn.setStatus("current")
_Pmopm2Mesrchannel17Table_Object = MibTable
pmopm2Mesrchannel17Table = _Pmopm2Mesrchannel17Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel17Table.setStatus("current")
_Pmopm2Mesrchannel17Entry_Object = MibTableRow
pmopm2Mesrchannel17Entry = _Pmopm2Mesrchannel17Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 48, 1)
)
pmopm2Mesrchannel17Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel17Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel17Entry.setStatus("current")


class _Pmopm2Mesrchannel17Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel17Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel17Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel17Index_Object = MibTableColumn
pmopm2Mesrchannel17Index = _Pmopm2Mesrchannel17Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 48, 1, 1),
    _Pmopm2Mesrchannel17Index_Type()
)
pmopm2Mesrchannel17Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel17Index.setStatus("current")


class _Pmopm2Mesrchannel17Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel17Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel17Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel17Portn_Object = MibTableColumn
pmopm2Mesrchannel17Portn = _Pmopm2Mesrchannel17Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 48, 1, 2),
    _Pmopm2Mesrchannel17Portn_Type()
)
pmopm2Mesrchannel17Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel17Portn.setStatus("current")
_Pmopm2Mesrchannel18Table_Object = MibTable
pmopm2Mesrchannel18Table = _Pmopm2Mesrchannel18Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 50)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel18Table.setStatus("current")
_Pmopm2Mesrchannel18Entry_Object = MibTableRow
pmopm2Mesrchannel18Entry = _Pmopm2Mesrchannel18Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 50, 1)
)
pmopm2Mesrchannel18Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel18Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel18Entry.setStatus("current")


class _Pmopm2Mesrchannel18Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel18Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel18Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel18Index_Object = MibTableColumn
pmopm2Mesrchannel18Index = _Pmopm2Mesrchannel18Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 50, 1, 1),
    _Pmopm2Mesrchannel18Index_Type()
)
pmopm2Mesrchannel18Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel18Index.setStatus("current")


class _Pmopm2Mesrchannel18Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel18Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel18Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel18Portn_Object = MibTableColumn
pmopm2Mesrchannel18Portn = _Pmopm2Mesrchannel18Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 50, 1, 2),
    _Pmopm2Mesrchannel18Portn_Type()
)
pmopm2Mesrchannel18Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel18Portn.setStatus("current")
_Pmopm2Mesrchannel19Table_Object = MibTable
pmopm2Mesrchannel19Table = _Pmopm2Mesrchannel19Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 52)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel19Table.setStatus("current")
_Pmopm2Mesrchannel19Entry_Object = MibTableRow
pmopm2Mesrchannel19Entry = _Pmopm2Mesrchannel19Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 52, 1)
)
pmopm2Mesrchannel19Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel19Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel19Entry.setStatus("current")


class _Pmopm2Mesrchannel19Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel19Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel19Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel19Index_Object = MibTableColumn
pmopm2Mesrchannel19Index = _Pmopm2Mesrchannel19Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 52, 1, 1),
    _Pmopm2Mesrchannel19Index_Type()
)
pmopm2Mesrchannel19Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel19Index.setStatus("current")


class _Pmopm2Mesrchannel19Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel19Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel19Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel19Portn_Object = MibTableColumn
pmopm2Mesrchannel19Portn = _Pmopm2Mesrchannel19Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 52, 1, 2),
    _Pmopm2Mesrchannel19Portn_Type()
)
pmopm2Mesrchannel19Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel19Portn.setStatus("current")
_Pmopm2Mesrchannel20Table_Object = MibTable
pmopm2Mesrchannel20Table = _Pmopm2Mesrchannel20Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 54)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel20Table.setStatus("current")
_Pmopm2Mesrchannel20Entry_Object = MibTableRow
pmopm2Mesrchannel20Entry = _Pmopm2Mesrchannel20Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 54, 1)
)
pmopm2Mesrchannel20Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel20Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel20Entry.setStatus("current")


class _Pmopm2Mesrchannel20Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel20Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel20Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel20Index_Object = MibTableColumn
pmopm2Mesrchannel20Index = _Pmopm2Mesrchannel20Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 54, 1, 1),
    _Pmopm2Mesrchannel20Index_Type()
)
pmopm2Mesrchannel20Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel20Index.setStatus("current")


class _Pmopm2Mesrchannel20Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel20Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel20Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel20Portn_Object = MibTableColumn
pmopm2Mesrchannel20Portn = _Pmopm2Mesrchannel20Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 54, 1, 2),
    _Pmopm2Mesrchannel20Portn_Type()
)
pmopm2Mesrchannel20Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel20Portn.setStatus("current")
_Pmopm2Mesrchannel21Table_Object = MibTable
pmopm2Mesrchannel21Table = _Pmopm2Mesrchannel21Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 56)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel21Table.setStatus("current")
_Pmopm2Mesrchannel21Entry_Object = MibTableRow
pmopm2Mesrchannel21Entry = _Pmopm2Mesrchannel21Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 56, 1)
)
pmopm2Mesrchannel21Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel21Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel21Entry.setStatus("current")


class _Pmopm2Mesrchannel21Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel21Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel21Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel21Index_Object = MibTableColumn
pmopm2Mesrchannel21Index = _Pmopm2Mesrchannel21Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 56, 1, 1),
    _Pmopm2Mesrchannel21Index_Type()
)
pmopm2Mesrchannel21Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel21Index.setStatus("current")


class _Pmopm2Mesrchannel21Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel21Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel21Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel21Portn_Object = MibTableColumn
pmopm2Mesrchannel21Portn = _Pmopm2Mesrchannel21Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 56, 1, 2),
    _Pmopm2Mesrchannel21Portn_Type()
)
pmopm2Mesrchannel21Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel21Portn.setStatus("current")
_Pmopm2Mesrchannel22Table_Object = MibTable
pmopm2Mesrchannel22Table = _Pmopm2Mesrchannel22Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 58)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel22Table.setStatus("current")
_Pmopm2Mesrchannel22Entry_Object = MibTableRow
pmopm2Mesrchannel22Entry = _Pmopm2Mesrchannel22Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 58, 1)
)
pmopm2Mesrchannel22Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel22Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel22Entry.setStatus("current")


class _Pmopm2Mesrchannel22Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel22Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel22Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel22Index_Object = MibTableColumn
pmopm2Mesrchannel22Index = _Pmopm2Mesrchannel22Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 58, 1, 1),
    _Pmopm2Mesrchannel22Index_Type()
)
pmopm2Mesrchannel22Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel22Index.setStatus("current")


class _Pmopm2Mesrchannel22Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel22Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel22Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel22Portn_Object = MibTableColumn
pmopm2Mesrchannel22Portn = _Pmopm2Mesrchannel22Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 58, 1, 2),
    _Pmopm2Mesrchannel22Portn_Type()
)
pmopm2Mesrchannel22Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel22Portn.setStatus("current")
_Pmopm2Mesrchannel23Table_Object = MibTable
pmopm2Mesrchannel23Table = _Pmopm2Mesrchannel23Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 60)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel23Table.setStatus("current")
_Pmopm2Mesrchannel23Entry_Object = MibTableRow
pmopm2Mesrchannel23Entry = _Pmopm2Mesrchannel23Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 60, 1)
)
pmopm2Mesrchannel23Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel23Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel23Entry.setStatus("current")


class _Pmopm2Mesrchannel23Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel23Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel23Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel23Index_Object = MibTableColumn
pmopm2Mesrchannel23Index = _Pmopm2Mesrchannel23Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 60, 1, 1),
    _Pmopm2Mesrchannel23Index_Type()
)
pmopm2Mesrchannel23Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel23Index.setStatus("current")


class _Pmopm2Mesrchannel23Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel23Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel23Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel23Portn_Object = MibTableColumn
pmopm2Mesrchannel23Portn = _Pmopm2Mesrchannel23Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 60, 1, 2),
    _Pmopm2Mesrchannel23Portn_Type()
)
pmopm2Mesrchannel23Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel23Portn.setStatus("current")
_Pmopm2Mesrchannel24Table_Object = MibTable
pmopm2Mesrchannel24Table = _Pmopm2Mesrchannel24Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 62)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel24Table.setStatus("current")
_Pmopm2Mesrchannel24Entry_Object = MibTableRow
pmopm2Mesrchannel24Entry = _Pmopm2Mesrchannel24Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 62, 1)
)
pmopm2Mesrchannel24Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel24Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel24Entry.setStatus("current")


class _Pmopm2Mesrchannel24Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel24Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel24Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel24Index_Object = MibTableColumn
pmopm2Mesrchannel24Index = _Pmopm2Mesrchannel24Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 62, 1, 1),
    _Pmopm2Mesrchannel24Index_Type()
)
pmopm2Mesrchannel24Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel24Index.setStatus("current")


class _Pmopm2Mesrchannel24Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel24Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel24Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel24Portn_Object = MibTableColumn
pmopm2Mesrchannel24Portn = _Pmopm2Mesrchannel24Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 62, 1, 2),
    _Pmopm2Mesrchannel24Portn_Type()
)
pmopm2Mesrchannel24Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel24Portn.setStatus("current")
_Pmopm2Mesrchannel25Table_Object = MibTable
pmopm2Mesrchannel25Table = _Pmopm2Mesrchannel25Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel25Table.setStatus("current")
_Pmopm2Mesrchannel25Entry_Object = MibTableRow
pmopm2Mesrchannel25Entry = _Pmopm2Mesrchannel25Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 64, 1)
)
pmopm2Mesrchannel25Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel25Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel25Entry.setStatus("current")


class _Pmopm2Mesrchannel25Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel25Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel25Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel25Index_Object = MibTableColumn
pmopm2Mesrchannel25Index = _Pmopm2Mesrchannel25Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 64, 1, 1),
    _Pmopm2Mesrchannel25Index_Type()
)
pmopm2Mesrchannel25Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel25Index.setStatus("current")


class _Pmopm2Mesrchannel25Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel25Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel25Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel25Portn_Object = MibTableColumn
pmopm2Mesrchannel25Portn = _Pmopm2Mesrchannel25Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 64, 1, 2),
    _Pmopm2Mesrchannel25Portn_Type()
)
pmopm2Mesrchannel25Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel25Portn.setStatus("current")
_Pmopm2Mesrchannel26Table_Object = MibTable
pmopm2Mesrchannel26Table = _Pmopm2Mesrchannel26Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 66)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel26Table.setStatus("current")
_Pmopm2Mesrchannel26Entry_Object = MibTableRow
pmopm2Mesrchannel26Entry = _Pmopm2Mesrchannel26Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 66, 1)
)
pmopm2Mesrchannel26Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel26Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel26Entry.setStatus("current")


class _Pmopm2Mesrchannel26Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel26Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel26Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel26Index_Object = MibTableColumn
pmopm2Mesrchannel26Index = _Pmopm2Mesrchannel26Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 66, 1, 1),
    _Pmopm2Mesrchannel26Index_Type()
)
pmopm2Mesrchannel26Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel26Index.setStatus("current")


class _Pmopm2Mesrchannel26Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel26Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel26Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel26Portn_Object = MibTableColumn
pmopm2Mesrchannel26Portn = _Pmopm2Mesrchannel26Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 66, 1, 2),
    _Pmopm2Mesrchannel26Portn_Type()
)
pmopm2Mesrchannel26Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel26Portn.setStatus("current")
_Pmopm2Mesrchannel27Table_Object = MibTable
pmopm2Mesrchannel27Table = _Pmopm2Mesrchannel27Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 68)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel27Table.setStatus("current")
_Pmopm2Mesrchannel27Entry_Object = MibTableRow
pmopm2Mesrchannel27Entry = _Pmopm2Mesrchannel27Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 68, 1)
)
pmopm2Mesrchannel27Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel27Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel27Entry.setStatus("current")


class _Pmopm2Mesrchannel27Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel27Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel27Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel27Index_Object = MibTableColumn
pmopm2Mesrchannel27Index = _Pmopm2Mesrchannel27Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 68, 1, 1),
    _Pmopm2Mesrchannel27Index_Type()
)
pmopm2Mesrchannel27Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel27Index.setStatus("current")


class _Pmopm2Mesrchannel27Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel27Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel27Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel27Portn_Object = MibTableColumn
pmopm2Mesrchannel27Portn = _Pmopm2Mesrchannel27Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 68, 1, 2),
    _Pmopm2Mesrchannel27Portn_Type()
)
pmopm2Mesrchannel27Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel27Portn.setStatus("current")
_Pmopm2Mesrchannel28Table_Object = MibTable
pmopm2Mesrchannel28Table = _Pmopm2Mesrchannel28Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 70)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel28Table.setStatus("current")
_Pmopm2Mesrchannel28Entry_Object = MibTableRow
pmopm2Mesrchannel28Entry = _Pmopm2Mesrchannel28Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 70, 1)
)
pmopm2Mesrchannel28Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel28Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel28Entry.setStatus("current")


class _Pmopm2Mesrchannel28Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel28Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel28Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel28Index_Object = MibTableColumn
pmopm2Mesrchannel28Index = _Pmopm2Mesrchannel28Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 70, 1, 1),
    _Pmopm2Mesrchannel28Index_Type()
)
pmopm2Mesrchannel28Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel28Index.setStatus("current")


class _Pmopm2Mesrchannel28Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel28Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel28Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel28Portn_Object = MibTableColumn
pmopm2Mesrchannel28Portn = _Pmopm2Mesrchannel28Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 70, 1, 2),
    _Pmopm2Mesrchannel28Portn_Type()
)
pmopm2Mesrchannel28Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel28Portn.setStatus("current")
_Pmopm2Mesrchannel29Table_Object = MibTable
pmopm2Mesrchannel29Table = _Pmopm2Mesrchannel29Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 72)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel29Table.setStatus("current")
_Pmopm2Mesrchannel29Entry_Object = MibTableRow
pmopm2Mesrchannel29Entry = _Pmopm2Mesrchannel29Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 72, 1)
)
pmopm2Mesrchannel29Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel29Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel29Entry.setStatus("current")


class _Pmopm2Mesrchannel29Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel29Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel29Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel29Index_Object = MibTableColumn
pmopm2Mesrchannel29Index = _Pmopm2Mesrchannel29Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 72, 1, 1),
    _Pmopm2Mesrchannel29Index_Type()
)
pmopm2Mesrchannel29Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel29Index.setStatus("current")


class _Pmopm2Mesrchannel29Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel29Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel29Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel29Portn_Object = MibTableColumn
pmopm2Mesrchannel29Portn = _Pmopm2Mesrchannel29Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 72, 1, 2),
    _Pmopm2Mesrchannel29Portn_Type()
)
pmopm2Mesrchannel29Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel29Portn.setStatus("current")
_Pmopm2Mesrchannel30Table_Object = MibTable
pmopm2Mesrchannel30Table = _Pmopm2Mesrchannel30Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 74)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel30Table.setStatus("current")
_Pmopm2Mesrchannel30Entry_Object = MibTableRow
pmopm2Mesrchannel30Entry = _Pmopm2Mesrchannel30Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 74, 1)
)
pmopm2Mesrchannel30Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel30Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel30Entry.setStatus("current")


class _Pmopm2Mesrchannel30Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel30Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel30Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel30Index_Object = MibTableColumn
pmopm2Mesrchannel30Index = _Pmopm2Mesrchannel30Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 74, 1, 1),
    _Pmopm2Mesrchannel30Index_Type()
)
pmopm2Mesrchannel30Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel30Index.setStatus("current")


class _Pmopm2Mesrchannel30Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel30Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel30Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel30Portn_Object = MibTableColumn
pmopm2Mesrchannel30Portn = _Pmopm2Mesrchannel30Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 74, 1, 2),
    _Pmopm2Mesrchannel30Portn_Type()
)
pmopm2Mesrchannel30Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel30Portn.setStatus("current")
_Pmopm2Mesrchannel31Table_Object = MibTable
pmopm2Mesrchannel31Table = _Pmopm2Mesrchannel31Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 76)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel31Table.setStatus("current")
_Pmopm2Mesrchannel31Entry_Object = MibTableRow
pmopm2Mesrchannel31Entry = _Pmopm2Mesrchannel31Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 76, 1)
)
pmopm2Mesrchannel31Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel31Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel31Entry.setStatus("current")


class _Pmopm2Mesrchannel31Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel31Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel31Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel31Index_Object = MibTableColumn
pmopm2Mesrchannel31Index = _Pmopm2Mesrchannel31Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 76, 1, 1),
    _Pmopm2Mesrchannel31Index_Type()
)
pmopm2Mesrchannel31Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel31Index.setStatus("current")


class _Pmopm2Mesrchannel31Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel31Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel31Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel31Portn_Object = MibTableColumn
pmopm2Mesrchannel31Portn = _Pmopm2Mesrchannel31Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 76, 1, 2),
    _Pmopm2Mesrchannel31Portn_Type()
)
pmopm2Mesrchannel31Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel31Portn.setStatus("current")
_Pmopm2Mesrchannel32Table_Object = MibTable
pmopm2Mesrchannel32Table = _Pmopm2Mesrchannel32Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 78)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel32Table.setStatus("current")
_Pmopm2Mesrchannel32Entry_Object = MibTableRow
pmopm2Mesrchannel32Entry = _Pmopm2Mesrchannel32Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 78, 1)
)
pmopm2Mesrchannel32Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel32Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel32Entry.setStatus("current")


class _Pmopm2Mesrchannel32Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel32Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel32Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel32Index_Object = MibTableColumn
pmopm2Mesrchannel32Index = _Pmopm2Mesrchannel32Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 78, 1, 1),
    _Pmopm2Mesrchannel32Index_Type()
)
pmopm2Mesrchannel32Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel32Index.setStatus("current")


class _Pmopm2Mesrchannel32Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel32Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel32Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel32Portn_Object = MibTableColumn
pmopm2Mesrchannel32Portn = _Pmopm2Mesrchannel32Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 78, 1, 2),
    _Pmopm2Mesrchannel32Portn_Type()
)
pmopm2Mesrchannel32Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel32Portn.setStatus("current")
_Pmopm2Mesrchannel33Table_Object = MibTable
pmopm2Mesrchannel33Table = _Pmopm2Mesrchannel33Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 80)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel33Table.setStatus("current")
_Pmopm2Mesrchannel33Entry_Object = MibTableRow
pmopm2Mesrchannel33Entry = _Pmopm2Mesrchannel33Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 80, 1)
)
pmopm2Mesrchannel33Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel33Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel33Entry.setStatus("current")


class _Pmopm2Mesrchannel33Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel33Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel33Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel33Index_Object = MibTableColumn
pmopm2Mesrchannel33Index = _Pmopm2Mesrchannel33Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 80, 1, 1),
    _Pmopm2Mesrchannel33Index_Type()
)
pmopm2Mesrchannel33Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel33Index.setStatus("current")


class _Pmopm2Mesrchannel33Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel33Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel33Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel33Portn_Object = MibTableColumn
pmopm2Mesrchannel33Portn = _Pmopm2Mesrchannel33Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 80, 1, 2),
    _Pmopm2Mesrchannel33Portn_Type()
)
pmopm2Mesrchannel33Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel33Portn.setStatus("current")
_Pmopm2Mesrchannel34Table_Object = MibTable
pmopm2Mesrchannel34Table = _Pmopm2Mesrchannel34Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 82)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel34Table.setStatus("current")
_Pmopm2Mesrchannel34Entry_Object = MibTableRow
pmopm2Mesrchannel34Entry = _Pmopm2Mesrchannel34Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 82, 1)
)
pmopm2Mesrchannel34Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel34Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel34Entry.setStatus("current")


class _Pmopm2Mesrchannel34Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel34Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel34Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel34Index_Object = MibTableColumn
pmopm2Mesrchannel34Index = _Pmopm2Mesrchannel34Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 82, 1, 1),
    _Pmopm2Mesrchannel34Index_Type()
)
pmopm2Mesrchannel34Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel34Index.setStatus("current")


class _Pmopm2Mesrchannel34Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel34Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel34Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel34Portn_Object = MibTableColumn
pmopm2Mesrchannel34Portn = _Pmopm2Mesrchannel34Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 82, 1, 2),
    _Pmopm2Mesrchannel34Portn_Type()
)
pmopm2Mesrchannel34Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel34Portn.setStatus("current")
_Pmopm2Mesrchannel35Table_Object = MibTable
pmopm2Mesrchannel35Table = _Pmopm2Mesrchannel35Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 84)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel35Table.setStatus("current")
_Pmopm2Mesrchannel35Entry_Object = MibTableRow
pmopm2Mesrchannel35Entry = _Pmopm2Mesrchannel35Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 84, 1)
)
pmopm2Mesrchannel35Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel35Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel35Entry.setStatus("current")


class _Pmopm2Mesrchannel35Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel35Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel35Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel35Index_Object = MibTableColumn
pmopm2Mesrchannel35Index = _Pmopm2Mesrchannel35Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 84, 1, 1),
    _Pmopm2Mesrchannel35Index_Type()
)
pmopm2Mesrchannel35Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel35Index.setStatus("current")


class _Pmopm2Mesrchannel35Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel35Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel35Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel35Portn_Object = MibTableColumn
pmopm2Mesrchannel35Portn = _Pmopm2Mesrchannel35Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 84, 1, 2),
    _Pmopm2Mesrchannel35Portn_Type()
)
pmopm2Mesrchannel35Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel35Portn.setStatus("current")
_Pmopm2Mesrchannel36Table_Object = MibTable
pmopm2Mesrchannel36Table = _Pmopm2Mesrchannel36Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 86)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel36Table.setStatus("current")
_Pmopm2Mesrchannel36Entry_Object = MibTableRow
pmopm2Mesrchannel36Entry = _Pmopm2Mesrchannel36Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 86, 1)
)
pmopm2Mesrchannel36Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel36Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel36Entry.setStatus("current")


class _Pmopm2Mesrchannel36Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel36Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel36Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel36Index_Object = MibTableColumn
pmopm2Mesrchannel36Index = _Pmopm2Mesrchannel36Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 86, 1, 1),
    _Pmopm2Mesrchannel36Index_Type()
)
pmopm2Mesrchannel36Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel36Index.setStatus("current")


class _Pmopm2Mesrchannel36Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel36Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel36Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel36Portn_Object = MibTableColumn
pmopm2Mesrchannel36Portn = _Pmopm2Mesrchannel36Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 86, 1, 2),
    _Pmopm2Mesrchannel36Portn_Type()
)
pmopm2Mesrchannel36Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel36Portn.setStatus("current")
_Pmopm2Mesrchannel37Table_Object = MibTable
pmopm2Mesrchannel37Table = _Pmopm2Mesrchannel37Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 88)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel37Table.setStatus("current")
_Pmopm2Mesrchannel37Entry_Object = MibTableRow
pmopm2Mesrchannel37Entry = _Pmopm2Mesrchannel37Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 88, 1)
)
pmopm2Mesrchannel37Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel37Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel37Entry.setStatus("current")


class _Pmopm2Mesrchannel37Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel37Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel37Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel37Index_Object = MibTableColumn
pmopm2Mesrchannel37Index = _Pmopm2Mesrchannel37Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 88, 1, 1),
    _Pmopm2Mesrchannel37Index_Type()
)
pmopm2Mesrchannel37Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel37Index.setStatus("current")


class _Pmopm2Mesrchannel37Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel37Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel37Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel37Portn_Object = MibTableColumn
pmopm2Mesrchannel37Portn = _Pmopm2Mesrchannel37Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 88, 1, 2),
    _Pmopm2Mesrchannel37Portn_Type()
)
pmopm2Mesrchannel37Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel37Portn.setStatus("current")
_Pmopm2Mesrchannel38Table_Object = MibTable
pmopm2Mesrchannel38Table = _Pmopm2Mesrchannel38Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 90)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel38Table.setStatus("current")
_Pmopm2Mesrchannel38Entry_Object = MibTableRow
pmopm2Mesrchannel38Entry = _Pmopm2Mesrchannel38Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 90, 1)
)
pmopm2Mesrchannel38Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel38Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel38Entry.setStatus("current")


class _Pmopm2Mesrchannel38Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel38Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel38Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel38Index_Object = MibTableColumn
pmopm2Mesrchannel38Index = _Pmopm2Mesrchannel38Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 90, 1, 1),
    _Pmopm2Mesrchannel38Index_Type()
)
pmopm2Mesrchannel38Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel38Index.setStatus("current")


class _Pmopm2Mesrchannel38Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel38Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel38Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel38Portn_Object = MibTableColumn
pmopm2Mesrchannel38Portn = _Pmopm2Mesrchannel38Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 90, 1, 2),
    _Pmopm2Mesrchannel38Portn_Type()
)
pmopm2Mesrchannel38Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel38Portn.setStatus("current")
_Pmopm2Mesrchannel39Table_Object = MibTable
pmopm2Mesrchannel39Table = _Pmopm2Mesrchannel39Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 92)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel39Table.setStatus("current")
_Pmopm2Mesrchannel39Entry_Object = MibTableRow
pmopm2Mesrchannel39Entry = _Pmopm2Mesrchannel39Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 92, 1)
)
pmopm2Mesrchannel39Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel39Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel39Entry.setStatus("current")


class _Pmopm2Mesrchannel39Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel39Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel39Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel39Index_Object = MibTableColumn
pmopm2Mesrchannel39Index = _Pmopm2Mesrchannel39Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 92, 1, 1),
    _Pmopm2Mesrchannel39Index_Type()
)
pmopm2Mesrchannel39Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel39Index.setStatus("current")


class _Pmopm2Mesrchannel39Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel39Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel39Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel39Portn_Object = MibTableColumn
pmopm2Mesrchannel39Portn = _Pmopm2Mesrchannel39Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 92, 1, 2),
    _Pmopm2Mesrchannel39Portn_Type()
)
pmopm2Mesrchannel39Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel39Portn.setStatus("current")
_Pmopm2Mesrchannel40Table_Object = MibTable
pmopm2Mesrchannel40Table = _Pmopm2Mesrchannel40Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 94)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel40Table.setStatus("current")
_Pmopm2Mesrchannel40Entry_Object = MibTableRow
pmopm2Mesrchannel40Entry = _Pmopm2Mesrchannel40Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 94, 1)
)
pmopm2Mesrchannel40Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel40Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel40Entry.setStatus("current")


class _Pmopm2Mesrchannel40Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel40Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel40Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel40Index_Object = MibTableColumn
pmopm2Mesrchannel40Index = _Pmopm2Mesrchannel40Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 94, 1, 1),
    _Pmopm2Mesrchannel40Index_Type()
)
pmopm2Mesrchannel40Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel40Index.setStatus("current")


class _Pmopm2Mesrchannel40Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel40Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel40Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel40Portn_Object = MibTableColumn
pmopm2Mesrchannel40Portn = _Pmopm2Mesrchannel40Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 94, 1, 2),
    _Pmopm2Mesrchannel40Portn_Type()
)
pmopm2Mesrchannel40Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel40Portn.setStatus("current")
_Pmopm2Mesrchannel41Table_Object = MibTable
pmopm2Mesrchannel41Table = _Pmopm2Mesrchannel41Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 96)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel41Table.setStatus("current")
_Pmopm2Mesrchannel41Entry_Object = MibTableRow
pmopm2Mesrchannel41Entry = _Pmopm2Mesrchannel41Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 96, 1)
)
pmopm2Mesrchannel41Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel41Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel41Entry.setStatus("current")


class _Pmopm2Mesrchannel41Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel41Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel41Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel41Index_Object = MibTableColumn
pmopm2Mesrchannel41Index = _Pmopm2Mesrchannel41Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 96, 1, 1),
    _Pmopm2Mesrchannel41Index_Type()
)
pmopm2Mesrchannel41Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel41Index.setStatus("current")


class _Pmopm2Mesrchannel41Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel41Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel41Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel41Portn_Object = MibTableColumn
pmopm2Mesrchannel41Portn = _Pmopm2Mesrchannel41Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 96, 1, 2),
    _Pmopm2Mesrchannel41Portn_Type()
)
pmopm2Mesrchannel41Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel41Portn.setStatus("current")
_Pmopm2Mesrchannel42Table_Object = MibTable
pmopm2Mesrchannel42Table = _Pmopm2Mesrchannel42Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 98)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel42Table.setStatus("current")
_Pmopm2Mesrchannel42Entry_Object = MibTableRow
pmopm2Mesrchannel42Entry = _Pmopm2Mesrchannel42Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 98, 1)
)
pmopm2Mesrchannel42Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel42Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel42Entry.setStatus("current")


class _Pmopm2Mesrchannel42Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel42Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel42Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel42Index_Object = MibTableColumn
pmopm2Mesrchannel42Index = _Pmopm2Mesrchannel42Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 98, 1, 1),
    _Pmopm2Mesrchannel42Index_Type()
)
pmopm2Mesrchannel42Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel42Index.setStatus("current")


class _Pmopm2Mesrchannel42Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel42Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel42Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel42Portn_Object = MibTableColumn
pmopm2Mesrchannel42Portn = _Pmopm2Mesrchannel42Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 98, 1, 2),
    _Pmopm2Mesrchannel42Portn_Type()
)
pmopm2Mesrchannel42Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel42Portn.setStatus("current")
_Pmopm2Mesrchannel43Table_Object = MibTable
pmopm2Mesrchannel43Table = _Pmopm2Mesrchannel43Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 100)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel43Table.setStatus("current")
_Pmopm2Mesrchannel43Entry_Object = MibTableRow
pmopm2Mesrchannel43Entry = _Pmopm2Mesrchannel43Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 100, 1)
)
pmopm2Mesrchannel43Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel43Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel43Entry.setStatus("current")


class _Pmopm2Mesrchannel43Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel43Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel43Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel43Index_Object = MibTableColumn
pmopm2Mesrchannel43Index = _Pmopm2Mesrchannel43Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 100, 1, 1),
    _Pmopm2Mesrchannel43Index_Type()
)
pmopm2Mesrchannel43Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel43Index.setStatus("current")


class _Pmopm2Mesrchannel43Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel43Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel43Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel43Portn_Object = MibTableColumn
pmopm2Mesrchannel43Portn = _Pmopm2Mesrchannel43Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 100, 1, 2),
    _Pmopm2Mesrchannel43Portn_Type()
)
pmopm2Mesrchannel43Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel43Portn.setStatus("current")
_Pmopm2Mesrchannel44Table_Object = MibTable
pmopm2Mesrchannel44Table = _Pmopm2Mesrchannel44Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 102)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel44Table.setStatus("current")
_Pmopm2Mesrchannel44Entry_Object = MibTableRow
pmopm2Mesrchannel44Entry = _Pmopm2Mesrchannel44Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 102, 1)
)
pmopm2Mesrchannel44Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel44Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel44Entry.setStatus("current")


class _Pmopm2Mesrchannel44Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel44Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel44Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel44Index_Object = MibTableColumn
pmopm2Mesrchannel44Index = _Pmopm2Mesrchannel44Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 102, 1, 1),
    _Pmopm2Mesrchannel44Index_Type()
)
pmopm2Mesrchannel44Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel44Index.setStatus("current")


class _Pmopm2Mesrchannel44Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel44Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel44Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel44Portn_Object = MibTableColumn
pmopm2Mesrchannel44Portn = _Pmopm2Mesrchannel44Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 102, 1, 2),
    _Pmopm2Mesrchannel44Portn_Type()
)
pmopm2Mesrchannel44Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel44Portn.setStatus("current")
_Pmopm2Mesrchannel45Table_Object = MibTable
pmopm2Mesrchannel45Table = _Pmopm2Mesrchannel45Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 104)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel45Table.setStatus("current")
_Pmopm2Mesrchannel45Entry_Object = MibTableRow
pmopm2Mesrchannel45Entry = _Pmopm2Mesrchannel45Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 104, 1)
)
pmopm2Mesrchannel45Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel45Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel45Entry.setStatus("current")


class _Pmopm2Mesrchannel45Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel45Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel45Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel45Index_Object = MibTableColumn
pmopm2Mesrchannel45Index = _Pmopm2Mesrchannel45Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 104, 1, 1),
    _Pmopm2Mesrchannel45Index_Type()
)
pmopm2Mesrchannel45Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel45Index.setStatus("current")


class _Pmopm2Mesrchannel45Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel45Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel45Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel45Portn_Object = MibTableColumn
pmopm2Mesrchannel45Portn = _Pmopm2Mesrchannel45Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 104, 1, 2),
    _Pmopm2Mesrchannel45Portn_Type()
)
pmopm2Mesrchannel45Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel45Portn.setStatus("current")
_Pmopm2Mesrchannel46Table_Object = MibTable
pmopm2Mesrchannel46Table = _Pmopm2Mesrchannel46Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 106)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel46Table.setStatus("current")
_Pmopm2Mesrchannel46Entry_Object = MibTableRow
pmopm2Mesrchannel46Entry = _Pmopm2Mesrchannel46Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 106, 1)
)
pmopm2Mesrchannel46Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel46Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel46Entry.setStatus("current")


class _Pmopm2Mesrchannel46Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel46Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel46Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel46Index_Object = MibTableColumn
pmopm2Mesrchannel46Index = _Pmopm2Mesrchannel46Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 106, 1, 1),
    _Pmopm2Mesrchannel46Index_Type()
)
pmopm2Mesrchannel46Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel46Index.setStatus("current")


class _Pmopm2Mesrchannel46Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel46Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel46Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel46Portn_Object = MibTableColumn
pmopm2Mesrchannel46Portn = _Pmopm2Mesrchannel46Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 106, 1, 2),
    _Pmopm2Mesrchannel46Portn_Type()
)
pmopm2Mesrchannel46Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel46Portn.setStatus("current")
_Pmopm2Mesrchannel47Table_Object = MibTable
pmopm2Mesrchannel47Table = _Pmopm2Mesrchannel47Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 108)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel47Table.setStatus("current")
_Pmopm2Mesrchannel47Entry_Object = MibTableRow
pmopm2Mesrchannel47Entry = _Pmopm2Mesrchannel47Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 108, 1)
)
pmopm2Mesrchannel47Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel47Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel47Entry.setStatus("current")


class _Pmopm2Mesrchannel47Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel47Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel47Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel47Index_Object = MibTableColumn
pmopm2Mesrchannel47Index = _Pmopm2Mesrchannel47Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 108, 1, 1),
    _Pmopm2Mesrchannel47Index_Type()
)
pmopm2Mesrchannel47Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel47Index.setStatus("current")


class _Pmopm2Mesrchannel47Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel47Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel47Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel47Portn_Object = MibTableColumn
pmopm2Mesrchannel47Portn = _Pmopm2Mesrchannel47Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 108, 1, 2),
    _Pmopm2Mesrchannel47Portn_Type()
)
pmopm2Mesrchannel47Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel47Portn.setStatus("current")
_Pmopm2Mesrchannel48Table_Object = MibTable
pmopm2Mesrchannel48Table = _Pmopm2Mesrchannel48Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 110)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel48Table.setStatus("current")
_Pmopm2Mesrchannel48Entry_Object = MibTableRow
pmopm2Mesrchannel48Entry = _Pmopm2Mesrchannel48Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 110, 1)
)
pmopm2Mesrchannel48Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel48Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel48Entry.setStatus("current")


class _Pmopm2Mesrchannel48Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel48Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel48Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel48Index_Object = MibTableColumn
pmopm2Mesrchannel48Index = _Pmopm2Mesrchannel48Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 110, 1, 1),
    _Pmopm2Mesrchannel48Index_Type()
)
pmopm2Mesrchannel48Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel48Index.setStatus("current")


class _Pmopm2Mesrchannel48Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel48Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel48Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel48Portn_Object = MibTableColumn
pmopm2Mesrchannel48Portn = _Pmopm2Mesrchannel48Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 110, 1, 2),
    _Pmopm2Mesrchannel48Portn_Type()
)
pmopm2Mesrchannel48Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel48Portn.setStatus("current")
_Pmopm2Mesrchannel49Table_Object = MibTable
pmopm2Mesrchannel49Table = _Pmopm2Mesrchannel49Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 112)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel49Table.setStatus("current")
_Pmopm2Mesrchannel49Entry_Object = MibTableRow
pmopm2Mesrchannel49Entry = _Pmopm2Mesrchannel49Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 112, 1)
)
pmopm2Mesrchannel49Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel49Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel49Entry.setStatus("current")


class _Pmopm2Mesrchannel49Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel49Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel49Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel49Index_Object = MibTableColumn
pmopm2Mesrchannel49Index = _Pmopm2Mesrchannel49Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 112, 1, 1),
    _Pmopm2Mesrchannel49Index_Type()
)
pmopm2Mesrchannel49Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel49Index.setStatus("current")


class _Pmopm2Mesrchannel49Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel49Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel49Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel49Portn_Object = MibTableColumn
pmopm2Mesrchannel49Portn = _Pmopm2Mesrchannel49Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 112, 1, 2),
    _Pmopm2Mesrchannel49Portn_Type()
)
pmopm2Mesrchannel49Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel49Portn.setStatus("current")
_Pmopm2Mesrchannel50Table_Object = MibTable
pmopm2Mesrchannel50Table = _Pmopm2Mesrchannel50Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 114)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel50Table.setStatus("current")
_Pmopm2Mesrchannel50Entry_Object = MibTableRow
pmopm2Mesrchannel50Entry = _Pmopm2Mesrchannel50Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 114, 1)
)
pmopm2Mesrchannel50Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel50Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel50Entry.setStatus("current")


class _Pmopm2Mesrchannel50Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel50Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel50Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel50Index_Object = MibTableColumn
pmopm2Mesrchannel50Index = _Pmopm2Mesrchannel50Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 114, 1, 1),
    _Pmopm2Mesrchannel50Index_Type()
)
pmopm2Mesrchannel50Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel50Index.setStatus("current")


class _Pmopm2Mesrchannel50Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel50Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel50Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel50Portn_Object = MibTableColumn
pmopm2Mesrchannel50Portn = _Pmopm2Mesrchannel50Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 114, 1, 2),
    _Pmopm2Mesrchannel50Portn_Type()
)
pmopm2Mesrchannel50Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel50Portn.setStatus("current")
_Pmopm2Mesrchannel51Table_Object = MibTable
pmopm2Mesrchannel51Table = _Pmopm2Mesrchannel51Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 116)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel51Table.setStatus("current")
_Pmopm2Mesrchannel51Entry_Object = MibTableRow
pmopm2Mesrchannel51Entry = _Pmopm2Mesrchannel51Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 116, 1)
)
pmopm2Mesrchannel51Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel51Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel51Entry.setStatus("current")


class _Pmopm2Mesrchannel51Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel51Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel51Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel51Index_Object = MibTableColumn
pmopm2Mesrchannel51Index = _Pmopm2Mesrchannel51Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 116, 1, 1),
    _Pmopm2Mesrchannel51Index_Type()
)
pmopm2Mesrchannel51Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel51Index.setStatus("current")


class _Pmopm2Mesrchannel51Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel51Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel51Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel51Portn_Object = MibTableColumn
pmopm2Mesrchannel51Portn = _Pmopm2Mesrchannel51Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 116, 1, 2),
    _Pmopm2Mesrchannel51Portn_Type()
)
pmopm2Mesrchannel51Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel51Portn.setStatus("current")
_Pmopm2Mesrchannel52Table_Object = MibTable
pmopm2Mesrchannel52Table = _Pmopm2Mesrchannel52Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 118)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel52Table.setStatus("current")
_Pmopm2Mesrchannel52Entry_Object = MibTableRow
pmopm2Mesrchannel52Entry = _Pmopm2Mesrchannel52Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 118, 1)
)
pmopm2Mesrchannel52Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel52Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel52Entry.setStatus("current")


class _Pmopm2Mesrchannel52Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel52Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel52Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel52Index_Object = MibTableColumn
pmopm2Mesrchannel52Index = _Pmopm2Mesrchannel52Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 118, 1, 1),
    _Pmopm2Mesrchannel52Index_Type()
)
pmopm2Mesrchannel52Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel52Index.setStatus("current")


class _Pmopm2Mesrchannel52Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel52Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel52Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel52Portn_Object = MibTableColumn
pmopm2Mesrchannel52Portn = _Pmopm2Mesrchannel52Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 118, 1, 2),
    _Pmopm2Mesrchannel52Portn_Type()
)
pmopm2Mesrchannel52Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel52Portn.setStatus("current")
_Pmopm2Mesrchannel53Table_Object = MibTable
pmopm2Mesrchannel53Table = _Pmopm2Mesrchannel53Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 120)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel53Table.setStatus("current")
_Pmopm2Mesrchannel53Entry_Object = MibTableRow
pmopm2Mesrchannel53Entry = _Pmopm2Mesrchannel53Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 120, 1)
)
pmopm2Mesrchannel53Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel53Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel53Entry.setStatus("current")


class _Pmopm2Mesrchannel53Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel53Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel53Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel53Index_Object = MibTableColumn
pmopm2Mesrchannel53Index = _Pmopm2Mesrchannel53Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 120, 1, 1),
    _Pmopm2Mesrchannel53Index_Type()
)
pmopm2Mesrchannel53Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel53Index.setStatus("current")


class _Pmopm2Mesrchannel53Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel53Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel53Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel53Portn_Object = MibTableColumn
pmopm2Mesrchannel53Portn = _Pmopm2Mesrchannel53Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 120, 1, 2),
    _Pmopm2Mesrchannel53Portn_Type()
)
pmopm2Mesrchannel53Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel53Portn.setStatus("current")
_Pmopm2Mesrchannel54Table_Object = MibTable
pmopm2Mesrchannel54Table = _Pmopm2Mesrchannel54Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 122)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel54Table.setStatus("current")
_Pmopm2Mesrchannel54Entry_Object = MibTableRow
pmopm2Mesrchannel54Entry = _Pmopm2Mesrchannel54Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 122, 1)
)
pmopm2Mesrchannel54Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel54Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel54Entry.setStatus("current")


class _Pmopm2Mesrchannel54Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel54Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel54Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel54Index_Object = MibTableColumn
pmopm2Mesrchannel54Index = _Pmopm2Mesrchannel54Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 122, 1, 1),
    _Pmopm2Mesrchannel54Index_Type()
)
pmopm2Mesrchannel54Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel54Index.setStatus("current")


class _Pmopm2Mesrchannel54Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel54Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel54Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel54Portn_Object = MibTableColumn
pmopm2Mesrchannel54Portn = _Pmopm2Mesrchannel54Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 122, 1, 2),
    _Pmopm2Mesrchannel54Portn_Type()
)
pmopm2Mesrchannel54Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel54Portn.setStatus("current")
_Pmopm2Mesrchannel55Table_Object = MibTable
pmopm2Mesrchannel55Table = _Pmopm2Mesrchannel55Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 124)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel55Table.setStatus("current")
_Pmopm2Mesrchannel55Entry_Object = MibTableRow
pmopm2Mesrchannel55Entry = _Pmopm2Mesrchannel55Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 124, 1)
)
pmopm2Mesrchannel55Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel55Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel55Entry.setStatus("current")


class _Pmopm2Mesrchannel55Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel55Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel55Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel55Index_Object = MibTableColumn
pmopm2Mesrchannel55Index = _Pmopm2Mesrchannel55Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 124, 1, 1),
    _Pmopm2Mesrchannel55Index_Type()
)
pmopm2Mesrchannel55Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel55Index.setStatus("current")


class _Pmopm2Mesrchannel55Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel55Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel55Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel55Portn_Object = MibTableColumn
pmopm2Mesrchannel55Portn = _Pmopm2Mesrchannel55Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 124, 1, 2),
    _Pmopm2Mesrchannel55Portn_Type()
)
pmopm2Mesrchannel55Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel55Portn.setStatus("current")
_Pmopm2Mesrchannel56Table_Object = MibTable
pmopm2Mesrchannel56Table = _Pmopm2Mesrchannel56Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 126)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel56Table.setStatus("current")
_Pmopm2Mesrchannel56Entry_Object = MibTableRow
pmopm2Mesrchannel56Entry = _Pmopm2Mesrchannel56Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 126, 1)
)
pmopm2Mesrchannel56Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel56Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel56Entry.setStatus("current")


class _Pmopm2Mesrchannel56Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel56Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel56Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel56Index_Object = MibTableColumn
pmopm2Mesrchannel56Index = _Pmopm2Mesrchannel56Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 126, 1, 1),
    _Pmopm2Mesrchannel56Index_Type()
)
pmopm2Mesrchannel56Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel56Index.setStatus("current")


class _Pmopm2Mesrchannel56Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel56Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel56Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel56Portn_Object = MibTableColumn
pmopm2Mesrchannel56Portn = _Pmopm2Mesrchannel56Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 126, 1, 2),
    _Pmopm2Mesrchannel56Portn_Type()
)
pmopm2Mesrchannel56Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel56Portn.setStatus("current")
_Pmopm2Mesrchannel57Table_Object = MibTable
pmopm2Mesrchannel57Table = _Pmopm2Mesrchannel57Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 128)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel57Table.setStatus("current")
_Pmopm2Mesrchannel57Entry_Object = MibTableRow
pmopm2Mesrchannel57Entry = _Pmopm2Mesrchannel57Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 128, 1)
)
pmopm2Mesrchannel57Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel57Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel57Entry.setStatus("current")


class _Pmopm2Mesrchannel57Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel57Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel57Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel57Index_Object = MibTableColumn
pmopm2Mesrchannel57Index = _Pmopm2Mesrchannel57Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 128, 1, 1),
    _Pmopm2Mesrchannel57Index_Type()
)
pmopm2Mesrchannel57Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel57Index.setStatus("current")


class _Pmopm2Mesrchannel57Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel57Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel57Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel57Portn_Object = MibTableColumn
pmopm2Mesrchannel57Portn = _Pmopm2Mesrchannel57Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 128, 1, 2),
    _Pmopm2Mesrchannel57Portn_Type()
)
pmopm2Mesrchannel57Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel57Portn.setStatus("current")
_Pmopm2Mesrchannel58Table_Object = MibTable
pmopm2Mesrchannel58Table = _Pmopm2Mesrchannel58Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 130)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel58Table.setStatus("current")
_Pmopm2Mesrchannel58Entry_Object = MibTableRow
pmopm2Mesrchannel58Entry = _Pmopm2Mesrchannel58Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 130, 1)
)
pmopm2Mesrchannel58Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel58Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel58Entry.setStatus("current")


class _Pmopm2Mesrchannel58Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel58Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel58Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel58Index_Object = MibTableColumn
pmopm2Mesrchannel58Index = _Pmopm2Mesrchannel58Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 130, 1, 1),
    _Pmopm2Mesrchannel58Index_Type()
)
pmopm2Mesrchannel58Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel58Index.setStatus("current")


class _Pmopm2Mesrchannel58Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel58Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel58Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel58Portn_Object = MibTableColumn
pmopm2Mesrchannel58Portn = _Pmopm2Mesrchannel58Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 130, 1, 2),
    _Pmopm2Mesrchannel58Portn_Type()
)
pmopm2Mesrchannel58Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel58Portn.setStatus("current")
_Pmopm2Mesrchannel59Table_Object = MibTable
pmopm2Mesrchannel59Table = _Pmopm2Mesrchannel59Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 132)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel59Table.setStatus("current")
_Pmopm2Mesrchannel59Entry_Object = MibTableRow
pmopm2Mesrchannel59Entry = _Pmopm2Mesrchannel59Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 132, 1)
)
pmopm2Mesrchannel59Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel59Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel59Entry.setStatus("current")


class _Pmopm2Mesrchannel59Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel59Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel59Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel59Index_Object = MibTableColumn
pmopm2Mesrchannel59Index = _Pmopm2Mesrchannel59Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 132, 1, 1),
    _Pmopm2Mesrchannel59Index_Type()
)
pmopm2Mesrchannel59Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel59Index.setStatus("current")


class _Pmopm2Mesrchannel59Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel59Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel59Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel59Portn_Object = MibTableColumn
pmopm2Mesrchannel59Portn = _Pmopm2Mesrchannel59Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 132, 1, 2),
    _Pmopm2Mesrchannel59Portn_Type()
)
pmopm2Mesrchannel59Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel59Portn.setStatus("current")
_Pmopm2Mesrchannel60Table_Object = MibTable
pmopm2Mesrchannel60Table = _Pmopm2Mesrchannel60Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 134)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel60Table.setStatus("current")
_Pmopm2Mesrchannel60Entry_Object = MibTableRow
pmopm2Mesrchannel60Entry = _Pmopm2Mesrchannel60Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 134, 1)
)
pmopm2Mesrchannel60Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel60Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel60Entry.setStatus("current")


class _Pmopm2Mesrchannel60Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel60Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel60Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel60Index_Object = MibTableColumn
pmopm2Mesrchannel60Index = _Pmopm2Mesrchannel60Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 134, 1, 1),
    _Pmopm2Mesrchannel60Index_Type()
)
pmopm2Mesrchannel60Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel60Index.setStatus("current")


class _Pmopm2Mesrchannel60Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel60Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel60Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel60Portn_Object = MibTableColumn
pmopm2Mesrchannel60Portn = _Pmopm2Mesrchannel60Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 134, 1, 2),
    _Pmopm2Mesrchannel60Portn_Type()
)
pmopm2Mesrchannel60Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel60Portn.setStatus("current")
_Pmopm2Mesrchannel61Table_Object = MibTable
pmopm2Mesrchannel61Table = _Pmopm2Mesrchannel61Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 136)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel61Table.setStatus("current")
_Pmopm2Mesrchannel61Entry_Object = MibTableRow
pmopm2Mesrchannel61Entry = _Pmopm2Mesrchannel61Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 136, 1)
)
pmopm2Mesrchannel61Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel61Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel61Entry.setStatus("current")


class _Pmopm2Mesrchannel61Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel61Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel61Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel61Index_Object = MibTableColumn
pmopm2Mesrchannel61Index = _Pmopm2Mesrchannel61Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 136, 1, 1),
    _Pmopm2Mesrchannel61Index_Type()
)
pmopm2Mesrchannel61Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel61Index.setStatus("current")


class _Pmopm2Mesrchannel61Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel61Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel61Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel61Portn_Object = MibTableColumn
pmopm2Mesrchannel61Portn = _Pmopm2Mesrchannel61Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 136, 1, 2),
    _Pmopm2Mesrchannel61Portn_Type()
)
pmopm2Mesrchannel61Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel61Portn.setStatus("current")
_Pmopm2Mesrchannel62Table_Object = MibTable
pmopm2Mesrchannel62Table = _Pmopm2Mesrchannel62Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 138)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel62Table.setStatus("current")
_Pmopm2Mesrchannel62Entry_Object = MibTableRow
pmopm2Mesrchannel62Entry = _Pmopm2Mesrchannel62Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 138, 1)
)
pmopm2Mesrchannel62Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel62Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel62Entry.setStatus("current")


class _Pmopm2Mesrchannel62Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel62Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel62Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel62Index_Object = MibTableColumn
pmopm2Mesrchannel62Index = _Pmopm2Mesrchannel62Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 138, 1, 1),
    _Pmopm2Mesrchannel62Index_Type()
)
pmopm2Mesrchannel62Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel62Index.setStatus("current")


class _Pmopm2Mesrchannel62Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel62Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel62Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel62Portn_Object = MibTableColumn
pmopm2Mesrchannel62Portn = _Pmopm2Mesrchannel62Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 138, 1, 2),
    _Pmopm2Mesrchannel62Portn_Type()
)
pmopm2Mesrchannel62Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel62Portn.setStatus("current")
_Pmopm2Mesrchannel63Table_Object = MibTable
pmopm2Mesrchannel63Table = _Pmopm2Mesrchannel63Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 140)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel63Table.setStatus("current")
_Pmopm2Mesrchannel63Entry_Object = MibTableRow
pmopm2Mesrchannel63Entry = _Pmopm2Mesrchannel63Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 140, 1)
)
pmopm2Mesrchannel63Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel63Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel63Entry.setStatus("current")


class _Pmopm2Mesrchannel63Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel63Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel63Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel63Index_Object = MibTableColumn
pmopm2Mesrchannel63Index = _Pmopm2Mesrchannel63Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 140, 1, 1),
    _Pmopm2Mesrchannel63Index_Type()
)
pmopm2Mesrchannel63Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel63Index.setStatus("current")


class _Pmopm2Mesrchannel63Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel63Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel63Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel63Portn_Object = MibTableColumn
pmopm2Mesrchannel63Portn = _Pmopm2Mesrchannel63Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 140, 1, 2),
    _Pmopm2Mesrchannel63Portn_Type()
)
pmopm2Mesrchannel63Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel63Portn.setStatus("current")
_Pmopm2Mesrchannel64Table_Object = MibTable
pmopm2Mesrchannel64Table = _Pmopm2Mesrchannel64Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 142)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel64Table.setStatus("current")
_Pmopm2Mesrchannel64Entry_Object = MibTableRow
pmopm2Mesrchannel64Entry = _Pmopm2Mesrchannel64Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 142, 1)
)
pmopm2Mesrchannel64Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel64Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel64Entry.setStatus("current")


class _Pmopm2Mesrchannel64Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel64Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel64Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel64Index_Object = MibTableColumn
pmopm2Mesrchannel64Index = _Pmopm2Mesrchannel64Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 142, 1, 1),
    _Pmopm2Mesrchannel64Index_Type()
)
pmopm2Mesrchannel64Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel64Index.setStatus("current")


class _Pmopm2Mesrchannel64Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel64Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel64Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel64Portn_Object = MibTableColumn
pmopm2Mesrchannel64Portn = _Pmopm2Mesrchannel64Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 142, 1, 2),
    _Pmopm2Mesrchannel64Portn_Type()
)
pmopm2Mesrchannel64Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel64Portn.setStatus("current")
_Pmopm2Mesrchannel65Table_Object = MibTable
pmopm2Mesrchannel65Table = _Pmopm2Mesrchannel65Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 144)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel65Table.setStatus("current")
_Pmopm2Mesrchannel65Entry_Object = MibTableRow
pmopm2Mesrchannel65Entry = _Pmopm2Mesrchannel65Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 144, 1)
)
pmopm2Mesrchannel65Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel65Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel65Entry.setStatus("current")


class _Pmopm2Mesrchannel65Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel65Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel65Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel65Index_Object = MibTableColumn
pmopm2Mesrchannel65Index = _Pmopm2Mesrchannel65Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 144, 1, 1),
    _Pmopm2Mesrchannel65Index_Type()
)
pmopm2Mesrchannel65Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel65Index.setStatus("current")


class _Pmopm2Mesrchannel65Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel65Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel65Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel65Portn_Object = MibTableColumn
pmopm2Mesrchannel65Portn = _Pmopm2Mesrchannel65Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 144, 1, 2),
    _Pmopm2Mesrchannel65Portn_Type()
)
pmopm2Mesrchannel65Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel65Portn.setStatus("current")
_Pmopm2Mesrchannel66Table_Object = MibTable
pmopm2Mesrchannel66Table = _Pmopm2Mesrchannel66Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 146)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel66Table.setStatus("current")
_Pmopm2Mesrchannel66Entry_Object = MibTableRow
pmopm2Mesrchannel66Entry = _Pmopm2Mesrchannel66Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 146, 1)
)
pmopm2Mesrchannel66Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel66Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel66Entry.setStatus("current")


class _Pmopm2Mesrchannel66Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel66Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel66Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel66Index_Object = MibTableColumn
pmopm2Mesrchannel66Index = _Pmopm2Mesrchannel66Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 146, 1, 1),
    _Pmopm2Mesrchannel66Index_Type()
)
pmopm2Mesrchannel66Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel66Index.setStatus("current")


class _Pmopm2Mesrchannel66Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel66Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel66Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel66Portn_Object = MibTableColumn
pmopm2Mesrchannel66Portn = _Pmopm2Mesrchannel66Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 146, 1, 2),
    _Pmopm2Mesrchannel66Portn_Type()
)
pmopm2Mesrchannel66Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel66Portn.setStatus("current")
_Pmopm2Mesrchannel67Table_Object = MibTable
pmopm2Mesrchannel67Table = _Pmopm2Mesrchannel67Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 148)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel67Table.setStatus("current")
_Pmopm2Mesrchannel67Entry_Object = MibTableRow
pmopm2Mesrchannel67Entry = _Pmopm2Mesrchannel67Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 148, 1)
)
pmopm2Mesrchannel67Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel67Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel67Entry.setStatus("current")


class _Pmopm2Mesrchannel67Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel67Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel67Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel67Index_Object = MibTableColumn
pmopm2Mesrchannel67Index = _Pmopm2Mesrchannel67Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 148, 1, 1),
    _Pmopm2Mesrchannel67Index_Type()
)
pmopm2Mesrchannel67Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel67Index.setStatus("current")


class _Pmopm2Mesrchannel67Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel67Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel67Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel67Portn_Object = MibTableColumn
pmopm2Mesrchannel67Portn = _Pmopm2Mesrchannel67Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 148, 1, 2),
    _Pmopm2Mesrchannel67Portn_Type()
)
pmopm2Mesrchannel67Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel67Portn.setStatus("current")
_Pmopm2Mesrchannel68Table_Object = MibTable
pmopm2Mesrchannel68Table = _Pmopm2Mesrchannel68Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 150)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel68Table.setStatus("current")
_Pmopm2Mesrchannel68Entry_Object = MibTableRow
pmopm2Mesrchannel68Entry = _Pmopm2Mesrchannel68Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 150, 1)
)
pmopm2Mesrchannel68Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel68Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel68Entry.setStatus("current")


class _Pmopm2Mesrchannel68Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel68Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel68Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel68Index_Object = MibTableColumn
pmopm2Mesrchannel68Index = _Pmopm2Mesrchannel68Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 150, 1, 1),
    _Pmopm2Mesrchannel68Index_Type()
)
pmopm2Mesrchannel68Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel68Index.setStatus("current")


class _Pmopm2Mesrchannel68Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel68Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel68Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel68Portn_Object = MibTableColumn
pmopm2Mesrchannel68Portn = _Pmopm2Mesrchannel68Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 150, 1, 2),
    _Pmopm2Mesrchannel68Portn_Type()
)
pmopm2Mesrchannel68Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel68Portn.setStatus("current")
_Pmopm2Mesrchannel69Table_Object = MibTable
pmopm2Mesrchannel69Table = _Pmopm2Mesrchannel69Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel69Table.setStatus("current")
_Pmopm2Mesrchannel69Entry_Object = MibTableRow
pmopm2Mesrchannel69Entry = _Pmopm2Mesrchannel69Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 152, 1)
)
pmopm2Mesrchannel69Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel69Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel69Entry.setStatus("current")


class _Pmopm2Mesrchannel69Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel69Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel69Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel69Index_Object = MibTableColumn
pmopm2Mesrchannel69Index = _Pmopm2Mesrchannel69Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 152, 1, 1),
    _Pmopm2Mesrchannel69Index_Type()
)
pmopm2Mesrchannel69Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel69Index.setStatus("current")


class _Pmopm2Mesrchannel69Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel69Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel69Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel69Portn_Object = MibTableColumn
pmopm2Mesrchannel69Portn = _Pmopm2Mesrchannel69Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 152, 1, 2),
    _Pmopm2Mesrchannel69Portn_Type()
)
pmopm2Mesrchannel69Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel69Portn.setStatus("current")
_Pmopm2Mesrchannel70Table_Object = MibTable
pmopm2Mesrchannel70Table = _Pmopm2Mesrchannel70Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 154)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel70Table.setStatus("current")
_Pmopm2Mesrchannel70Entry_Object = MibTableRow
pmopm2Mesrchannel70Entry = _Pmopm2Mesrchannel70Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 154, 1)
)
pmopm2Mesrchannel70Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel70Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel70Entry.setStatus("current")


class _Pmopm2Mesrchannel70Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel70Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel70Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel70Index_Object = MibTableColumn
pmopm2Mesrchannel70Index = _Pmopm2Mesrchannel70Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 154, 1, 1),
    _Pmopm2Mesrchannel70Index_Type()
)
pmopm2Mesrchannel70Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel70Index.setStatus("current")


class _Pmopm2Mesrchannel70Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel70Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel70Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel70Portn_Object = MibTableColumn
pmopm2Mesrchannel70Portn = _Pmopm2Mesrchannel70Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 154, 1, 2),
    _Pmopm2Mesrchannel70Portn_Type()
)
pmopm2Mesrchannel70Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel70Portn.setStatus("current")
_Pmopm2Mesrchannel71Table_Object = MibTable
pmopm2Mesrchannel71Table = _Pmopm2Mesrchannel71Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 156)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel71Table.setStatus("current")
_Pmopm2Mesrchannel71Entry_Object = MibTableRow
pmopm2Mesrchannel71Entry = _Pmopm2Mesrchannel71Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 156, 1)
)
pmopm2Mesrchannel71Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel71Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel71Entry.setStatus("current")


class _Pmopm2Mesrchannel71Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel71Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel71Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel71Index_Object = MibTableColumn
pmopm2Mesrchannel71Index = _Pmopm2Mesrchannel71Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 156, 1, 1),
    _Pmopm2Mesrchannel71Index_Type()
)
pmopm2Mesrchannel71Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel71Index.setStatus("current")


class _Pmopm2Mesrchannel71Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel71Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel71Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel71Portn_Object = MibTableColumn
pmopm2Mesrchannel71Portn = _Pmopm2Mesrchannel71Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 156, 1, 2),
    _Pmopm2Mesrchannel71Portn_Type()
)
pmopm2Mesrchannel71Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel71Portn.setStatus("current")
_Pmopm2Mesrchannel72Table_Object = MibTable
pmopm2Mesrchannel72Table = _Pmopm2Mesrchannel72Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 158)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel72Table.setStatus("current")
_Pmopm2Mesrchannel72Entry_Object = MibTableRow
pmopm2Mesrchannel72Entry = _Pmopm2Mesrchannel72Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 158, 1)
)
pmopm2Mesrchannel72Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel72Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel72Entry.setStatus("current")


class _Pmopm2Mesrchannel72Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel72Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel72Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel72Index_Object = MibTableColumn
pmopm2Mesrchannel72Index = _Pmopm2Mesrchannel72Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 158, 1, 1),
    _Pmopm2Mesrchannel72Index_Type()
)
pmopm2Mesrchannel72Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel72Index.setStatus("current")


class _Pmopm2Mesrchannel72Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel72Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel72Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel72Portn_Object = MibTableColumn
pmopm2Mesrchannel72Portn = _Pmopm2Mesrchannel72Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 158, 1, 2),
    _Pmopm2Mesrchannel72Portn_Type()
)
pmopm2Mesrchannel72Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel72Portn.setStatus("current")
_Pmopm2Mesrchannel73Table_Object = MibTable
pmopm2Mesrchannel73Table = _Pmopm2Mesrchannel73Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 160)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel73Table.setStatus("current")
_Pmopm2Mesrchannel73Entry_Object = MibTableRow
pmopm2Mesrchannel73Entry = _Pmopm2Mesrchannel73Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 160, 1)
)
pmopm2Mesrchannel73Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel73Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel73Entry.setStatus("current")


class _Pmopm2Mesrchannel73Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel73Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel73Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel73Index_Object = MibTableColumn
pmopm2Mesrchannel73Index = _Pmopm2Mesrchannel73Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 160, 1, 1),
    _Pmopm2Mesrchannel73Index_Type()
)
pmopm2Mesrchannel73Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel73Index.setStatus("current")


class _Pmopm2Mesrchannel73Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel73Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel73Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel73Portn_Object = MibTableColumn
pmopm2Mesrchannel73Portn = _Pmopm2Mesrchannel73Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 160, 1, 2),
    _Pmopm2Mesrchannel73Portn_Type()
)
pmopm2Mesrchannel73Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel73Portn.setStatus("current")
_Pmopm2Mesrchannel74Table_Object = MibTable
pmopm2Mesrchannel74Table = _Pmopm2Mesrchannel74Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 162)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel74Table.setStatus("current")
_Pmopm2Mesrchannel74Entry_Object = MibTableRow
pmopm2Mesrchannel74Entry = _Pmopm2Mesrchannel74Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 162, 1)
)
pmopm2Mesrchannel74Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel74Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel74Entry.setStatus("current")


class _Pmopm2Mesrchannel74Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel74Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel74Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel74Index_Object = MibTableColumn
pmopm2Mesrchannel74Index = _Pmopm2Mesrchannel74Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 162, 1, 1),
    _Pmopm2Mesrchannel74Index_Type()
)
pmopm2Mesrchannel74Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel74Index.setStatus("current")


class _Pmopm2Mesrchannel74Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel74Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel74Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel74Portn_Object = MibTableColumn
pmopm2Mesrchannel74Portn = _Pmopm2Mesrchannel74Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 162, 1, 2),
    _Pmopm2Mesrchannel74Portn_Type()
)
pmopm2Mesrchannel74Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel74Portn.setStatus("current")
_Pmopm2Mesrchannel75Table_Object = MibTable
pmopm2Mesrchannel75Table = _Pmopm2Mesrchannel75Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 164)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel75Table.setStatus("current")
_Pmopm2Mesrchannel75Entry_Object = MibTableRow
pmopm2Mesrchannel75Entry = _Pmopm2Mesrchannel75Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 164, 1)
)
pmopm2Mesrchannel75Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel75Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel75Entry.setStatus("current")


class _Pmopm2Mesrchannel75Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel75Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel75Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel75Index_Object = MibTableColumn
pmopm2Mesrchannel75Index = _Pmopm2Mesrchannel75Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 164, 1, 1),
    _Pmopm2Mesrchannel75Index_Type()
)
pmopm2Mesrchannel75Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel75Index.setStatus("current")


class _Pmopm2Mesrchannel75Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel75Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel75Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel75Portn_Object = MibTableColumn
pmopm2Mesrchannel75Portn = _Pmopm2Mesrchannel75Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 164, 1, 2),
    _Pmopm2Mesrchannel75Portn_Type()
)
pmopm2Mesrchannel75Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel75Portn.setStatus("current")
_Pmopm2Mesrchannel76Table_Object = MibTable
pmopm2Mesrchannel76Table = _Pmopm2Mesrchannel76Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 166)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel76Table.setStatus("current")
_Pmopm2Mesrchannel76Entry_Object = MibTableRow
pmopm2Mesrchannel76Entry = _Pmopm2Mesrchannel76Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 166, 1)
)
pmopm2Mesrchannel76Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel76Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel76Entry.setStatus("current")


class _Pmopm2Mesrchannel76Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel76Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel76Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel76Index_Object = MibTableColumn
pmopm2Mesrchannel76Index = _Pmopm2Mesrchannel76Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 166, 1, 1),
    _Pmopm2Mesrchannel76Index_Type()
)
pmopm2Mesrchannel76Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel76Index.setStatus("current")


class _Pmopm2Mesrchannel76Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel76Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel76Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel76Portn_Object = MibTableColumn
pmopm2Mesrchannel76Portn = _Pmopm2Mesrchannel76Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 166, 1, 2),
    _Pmopm2Mesrchannel76Portn_Type()
)
pmopm2Mesrchannel76Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel76Portn.setStatus("current")
_Pmopm2Mesrchannel77Table_Object = MibTable
pmopm2Mesrchannel77Table = _Pmopm2Mesrchannel77Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 168)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel77Table.setStatus("current")
_Pmopm2Mesrchannel77Entry_Object = MibTableRow
pmopm2Mesrchannel77Entry = _Pmopm2Mesrchannel77Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 168, 1)
)
pmopm2Mesrchannel77Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel77Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel77Entry.setStatus("current")


class _Pmopm2Mesrchannel77Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel77Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel77Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel77Index_Object = MibTableColumn
pmopm2Mesrchannel77Index = _Pmopm2Mesrchannel77Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 168, 1, 1),
    _Pmopm2Mesrchannel77Index_Type()
)
pmopm2Mesrchannel77Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel77Index.setStatus("current")


class _Pmopm2Mesrchannel77Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel77Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel77Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel77Portn_Object = MibTableColumn
pmopm2Mesrchannel77Portn = _Pmopm2Mesrchannel77Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 168, 1, 2),
    _Pmopm2Mesrchannel77Portn_Type()
)
pmopm2Mesrchannel77Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel77Portn.setStatus("current")
_Pmopm2Mesrchannel78Table_Object = MibTable
pmopm2Mesrchannel78Table = _Pmopm2Mesrchannel78Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 170)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel78Table.setStatus("current")
_Pmopm2Mesrchannel78Entry_Object = MibTableRow
pmopm2Mesrchannel78Entry = _Pmopm2Mesrchannel78Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 170, 1)
)
pmopm2Mesrchannel78Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel78Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel78Entry.setStatus("current")


class _Pmopm2Mesrchannel78Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel78Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel78Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel78Index_Object = MibTableColumn
pmopm2Mesrchannel78Index = _Pmopm2Mesrchannel78Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 170, 1, 1),
    _Pmopm2Mesrchannel78Index_Type()
)
pmopm2Mesrchannel78Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel78Index.setStatus("current")


class _Pmopm2Mesrchannel78Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel78Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel78Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel78Portn_Object = MibTableColumn
pmopm2Mesrchannel78Portn = _Pmopm2Mesrchannel78Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 170, 1, 2),
    _Pmopm2Mesrchannel78Portn_Type()
)
pmopm2Mesrchannel78Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel78Portn.setStatus("current")
_Pmopm2Mesrchannel79Table_Object = MibTable
pmopm2Mesrchannel79Table = _Pmopm2Mesrchannel79Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 172)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel79Table.setStatus("current")
_Pmopm2Mesrchannel79Entry_Object = MibTableRow
pmopm2Mesrchannel79Entry = _Pmopm2Mesrchannel79Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 172, 1)
)
pmopm2Mesrchannel79Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel79Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel79Entry.setStatus("current")


class _Pmopm2Mesrchannel79Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel79Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel79Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel79Index_Object = MibTableColumn
pmopm2Mesrchannel79Index = _Pmopm2Mesrchannel79Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 172, 1, 1),
    _Pmopm2Mesrchannel79Index_Type()
)
pmopm2Mesrchannel79Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel79Index.setStatus("current")


class _Pmopm2Mesrchannel79Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel79Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel79Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel79Portn_Object = MibTableColumn
pmopm2Mesrchannel79Portn = _Pmopm2Mesrchannel79Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 172, 1, 2),
    _Pmopm2Mesrchannel79Portn_Type()
)
pmopm2Mesrchannel79Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel79Portn.setStatus("current")
_Pmopm2Mesrchannel80Table_Object = MibTable
pmopm2Mesrchannel80Table = _Pmopm2Mesrchannel80Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 174)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel80Table.setStatus("current")
_Pmopm2Mesrchannel80Entry_Object = MibTableRow
pmopm2Mesrchannel80Entry = _Pmopm2Mesrchannel80Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 174, 1)
)
pmopm2Mesrchannel80Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel80Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel80Entry.setStatus("current")


class _Pmopm2Mesrchannel80Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel80Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel80Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel80Index_Object = MibTableColumn
pmopm2Mesrchannel80Index = _Pmopm2Mesrchannel80Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 174, 1, 1),
    _Pmopm2Mesrchannel80Index_Type()
)
pmopm2Mesrchannel80Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel80Index.setStatus("current")


class _Pmopm2Mesrchannel80Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel80Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel80Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel80Portn_Object = MibTableColumn
pmopm2Mesrchannel80Portn = _Pmopm2Mesrchannel80Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 174, 1, 2),
    _Pmopm2Mesrchannel80Portn_Type()
)
pmopm2Mesrchannel80Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel80Portn.setStatus("current")
_Pmopm2Mesrchannel81Table_Object = MibTable
pmopm2Mesrchannel81Table = _Pmopm2Mesrchannel81Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 176)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel81Table.setStatus("current")
_Pmopm2Mesrchannel81Entry_Object = MibTableRow
pmopm2Mesrchannel81Entry = _Pmopm2Mesrchannel81Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 176, 1)
)
pmopm2Mesrchannel81Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel81Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel81Entry.setStatus("current")


class _Pmopm2Mesrchannel81Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel81Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel81Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel81Index_Object = MibTableColumn
pmopm2Mesrchannel81Index = _Pmopm2Mesrchannel81Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 176, 1, 1),
    _Pmopm2Mesrchannel81Index_Type()
)
pmopm2Mesrchannel81Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel81Index.setStatus("current")


class _Pmopm2Mesrchannel81Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel81Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel81Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel81Portn_Object = MibTableColumn
pmopm2Mesrchannel81Portn = _Pmopm2Mesrchannel81Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 176, 1, 2),
    _Pmopm2Mesrchannel81Portn_Type()
)
pmopm2Mesrchannel81Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel81Portn.setStatus("current")
_Pmopm2Mesrchannel82Table_Object = MibTable
pmopm2Mesrchannel82Table = _Pmopm2Mesrchannel82Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 178)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel82Table.setStatus("current")
_Pmopm2Mesrchannel82Entry_Object = MibTableRow
pmopm2Mesrchannel82Entry = _Pmopm2Mesrchannel82Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 178, 1)
)
pmopm2Mesrchannel82Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel82Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel82Entry.setStatus("current")


class _Pmopm2Mesrchannel82Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel82Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel82Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel82Index_Object = MibTableColumn
pmopm2Mesrchannel82Index = _Pmopm2Mesrchannel82Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 178, 1, 1),
    _Pmopm2Mesrchannel82Index_Type()
)
pmopm2Mesrchannel82Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel82Index.setStatus("current")


class _Pmopm2Mesrchannel82Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel82Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel82Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel82Portn_Object = MibTableColumn
pmopm2Mesrchannel82Portn = _Pmopm2Mesrchannel82Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 178, 1, 2),
    _Pmopm2Mesrchannel82Portn_Type()
)
pmopm2Mesrchannel82Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel82Portn.setStatus("current")
_Pmopm2Mesrchannel83Table_Object = MibTable
pmopm2Mesrchannel83Table = _Pmopm2Mesrchannel83Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 180)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel83Table.setStatus("current")
_Pmopm2Mesrchannel83Entry_Object = MibTableRow
pmopm2Mesrchannel83Entry = _Pmopm2Mesrchannel83Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 180, 1)
)
pmopm2Mesrchannel83Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel83Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel83Entry.setStatus("current")


class _Pmopm2Mesrchannel83Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel83Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel83Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel83Index_Object = MibTableColumn
pmopm2Mesrchannel83Index = _Pmopm2Mesrchannel83Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 180, 1, 1),
    _Pmopm2Mesrchannel83Index_Type()
)
pmopm2Mesrchannel83Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel83Index.setStatus("current")


class _Pmopm2Mesrchannel83Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel83Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel83Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel83Portn_Object = MibTableColumn
pmopm2Mesrchannel83Portn = _Pmopm2Mesrchannel83Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 180, 1, 2),
    _Pmopm2Mesrchannel83Portn_Type()
)
pmopm2Mesrchannel83Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel83Portn.setStatus("current")
_Pmopm2Mesrchannel84Table_Object = MibTable
pmopm2Mesrchannel84Table = _Pmopm2Mesrchannel84Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 182)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel84Table.setStatus("current")
_Pmopm2Mesrchannel84Entry_Object = MibTableRow
pmopm2Mesrchannel84Entry = _Pmopm2Mesrchannel84Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 182, 1)
)
pmopm2Mesrchannel84Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel84Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel84Entry.setStatus("current")


class _Pmopm2Mesrchannel84Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel84Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel84Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel84Index_Object = MibTableColumn
pmopm2Mesrchannel84Index = _Pmopm2Mesrchannel84Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 182, 1, 1),
    _Pmopm2Mesrchannel84Index_Type()
)
pmopm2Mesrchannel84Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel84Index.setStatus("current")


class _Pmopm2Mesrchannel84Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel84Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel84Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel84Portn_Object = MibTableColumn
pmopm2Mesrchannel84Portn = _Pmopm2Mesrchannel84Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 182, 1, 2),
    _Pmopm2Mesrchannel84Portn_Type()
)
pmopm2Mesrchannel84Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel84Portn.setStatus("current")
_Pmopm2Mesrchannel85Table_Object = MibTable
pmopm2Mesrchannel85Table = _Pmopm2Mesrchannel85Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 184)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel85Table.setStatus("current")
_Pmopm2Mesrchannel85Entry_Object = MibTableRow
pmopm2Mesrchannel85Entry = _Pmopm2Mesrchannel85Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 184, 1)
)
pmopm2Mesrchannel85Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel85Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel85Entry.setStatus("current")


class _Pmopm2Mesrchannel85Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel85Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel85Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel85Index_Object = MibTableColumn
pmopm2Mesrchannel85Index = _Pmopm2Mesrchannel85Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 184, 1, 1),
    _Pmopm2Mesrchannel85Index_Type()
)
pmopm2Mesrchannel85Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel85Index.setStatus("current")


class _Pmopm2Mesrchannel85Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel85Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel85Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel85Portn_Object = MibTableColumn
pmopm2Mesrchannel85Portn = _Pmopm2Mesrchannel85Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 184, 1, 2),
    _Pmopm2Mesrchannel85Portn_Type()
)
pmopm2Mesrchannel85Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel85Portn.setStatus("current")
_Pmopm2Mesrchannel86Table_Object = MibTable
pmopm2Mesrchannel86Table = _Pmopm2Mesrchannel86Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 186)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel86Table.setStatus("current")
_Pmopm2Mesrchannel86Entry_Object = MibTableRow
pmopm2Mesrchannel86Entry = _Pmopm2Mesrchannel86Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 186, 1)
)
pmopm2Mesrchannel86Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel86Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel86Entry.setStatus("current")


class _Pmopm2Mesrchannel86Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel86Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel86Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel86Index_Object = MibTableColumn
pmopm2Mesrchannel86Index = _Pmopm2Mesrchannel86Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 186, 1, 1),
    _Pmopm2Mesrchannel86Index_Type()
)
pmopm2Mesrchannel86Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel86Index.setStatus("current")


class _Pmopm2Mesrchannel86Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel86Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel86Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel86Portn_Object = MibTableColumn
pmopm2Mesrchannel86Portn = _Pmopm2Mesrchannel86Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 186, 1, 2),
    _Pmopm2Mesrchannel86Portn_Type()
)
pmopm2Mesrchannel86Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel86Portn.setStatus("current")
_Pmopm2Mesrchannel87Table_Object = MibTable
pmopm2Mesrchannel87Table = _Pmopm2Mesrchannel87Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 188)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel87Table.setStatus("current")
_Pmopm2Mesrchannel87Entry_Object = MibTableRow
pmopm2Mesrchannel87Entry = _Pmopm2Mesrchannel87Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 188, 1)
)
pmopm2Mesrchannel87Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel87Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel87Entry.setStatus("current")


class _Pmopm2Mesrchannel87Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel87Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel87Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel87Index_Object = MibTableColumn
pmopm2Mesrchannel87Index = _Pmopm2Mesrchannel87Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 188, 1, 1),
    _Pmopm2Mesrchannel87Index_Type()
)
pmopm2Mesrchannel87Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel87Index.setStatus("current")


class _Pmopm2Mesrchannel87Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel87Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel87Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel87Portn_Object = MibTableColumn
pmopm2Mesrchannel87Portn = _Pmopm2Mesrchannel87Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 188, 1, 2),
    _Pmopm2Mesrchannel87Portn_Type()
)
pmopm2Mesrchannel87Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel87Portn.setStatus("current")
_Pmopm2Mesrchannel88Table_Object = MibTable
pmopm2Mesrchannel88Table = _Pmopm2Mesrchannel88Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 190)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel88Table.setStatus("current")
_Pmopm2Mesrchannel88Entry_Object = MibTableRow
pmopm2Mesrchannel88Entry = _Pmopm2Mesrchannel88Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 190, 1)
)
pmopm2Mesrchannel88Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel88Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel88Entry.setStatus("current")


class _Pmopm2Mesrchannel88Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel88Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel88Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel88Index_Object = MibTableColumn
pmopm2Mesrchannel88Index = _Pmopm2Mesrchannel88Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 190, 1, 1),
    _Pmopm2Mesrchannel88Index_Type()
)
pmopm2Mesrchannel88Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel88Index.setStatus("current")


class _Pmopm2Mesrchannel88Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel88Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel88Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel88Portn_Object = MibTableColumn
pmopm2Mesrchannel88Portn = _Pmopm2Mesrchannel88Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 190, 1, 2),
    _Pmopm2Mesrchannel88Portn_Type()
)
pmopm2Mesrchannel88Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel88Portn.setStatus("current")
_Pmopm2Mesrchannel89Table_Object = MibTable
pmopm2Mesrchannel89Table = _Pmopm2Mesrchannel89Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 192)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel89Table.setStatus("current")
_Pmopm2Mesrchannel89Entry_Object = MibTableRow
pmopm2Mesrchannel89Entry = _Pmopm2Mesrchannel89Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 192, 1)
)
pmopm2Mesrchannel89Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel89Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel89Entry.setStatus("current")


class _Pmopm2Mesrchannel89Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel89Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel89Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel89Index_Object = MibTableColumn
pmopm2Mesrchannel89Index = _Pmopm2Mesrchannel89Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 192, 1, 1),
    _Pmopm2Mesrchannel89Index_Type()
)
pmopm2Mesrchannel89Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel89Index.setStatus("current")


class _Pmopm2Mesrchannel89Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel89Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel89Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel89Portn_Object = MibTableColumn
pmopm2Mesrchannel89Portn = _Pmopm2Mesrchannel89Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 192, 1, 2),
    _Pmopm2Mesrchannel89Portn_Type()
)
pmopm2Mesrchannel89Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel89Portn.setStatus("current")
_Pmopm2Mesrchannel90Table_Object = MibTable
pmopm2Mesrchannel90Table = _Pmopm2Mesrchannel90Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 194)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel90Table.setStatus("current")
_Pmopm2Mesrchannel90Entry_Object = MibTableRow
pmopm2Mesrchannel90Entry = _Pmopm2Mesrchannel90Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 194, 1)
)
pmopm2Mesrchannel90Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel90Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel90Entry.setStatus("current")


class _Pmopm2Mesrchannel90Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel90Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel90Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel90Index_Object = MibTableColumn
pmopm2Mesrchannel90Index = _Pmopm2Mesrchannel90Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 194, 1, 1),
    _Pmopm2Mesrchannel90Index_Type()
)
pmopm2Mesrchannel90Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel90Index.setStatus("current")


class _Pmopm2Mesrchannel90Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel90Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel90Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel90Portn_Object = MibTableColumn
pmopm2Mesrchannel90Portn = _Pmopm2Mesrchannel90Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 194, 1, 2),
    _Pmopm2Mesrchannel90Portn_Type()
)
pmopm2Mesrchannel90Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel90Portn.setStatus("current")
_Pmopm2Mesrchannel91Table_Object = MibTable
pmopm2Mesrchannel91Table = _Pmopm2Mesrchannel91Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 196)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel91Table.setStatus("current")
_Pmopm2Mesrchannel91Entry_Object = MibTableRow
pmopm2Mesrchannel91Entry = _Pmopm2Mesrchannel91Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 196, 1)
)
pmopm2Mesrchannel91Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel91Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel91Entry.setStatus("current")


class _Pmopm2Mesrchannel91Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel91Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel91Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel91Index_Object = MibTableColumn
pmopm2Mesrchannel91Index = _Pmopm2Mesrchannel91Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 196, 1, 1),
    _Pmopm2Mesrchannel91Index_Type()
)
pmopm2Mesrchannel91Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel91Index.setStatus("current")


class _Pmopm2Mesrchannel91Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel91Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel91Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel91Portn_Object = MibTableColumn
pmopm2Mesrchannel91Portn = _Pmopm2Mesrchannel91Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 196, 1, 2),
    _Pmopm2Mesrchannel91Portn_Type()
)
pmopm2Mesrchannel91Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel91Portn.setStatus("current")
_Pmopm2Mesrchannel92Table_Object = MibTable
pmopm2Mesrchannel92Table = _Pmopm2Mesrchannel92Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 198)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel92Table.setStatus("current")
_Pmopm2Mesrchannel92Entry_Object = MibTableRow
pmopm2Mesrchannel92Entry = _Pmopm2Mesrchannel92Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 198, 1)
)
pmopm2Mesrchannel92Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel92Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel92Entry.setStatus("current")


class _Pmopm2Mesrchannel92Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel92Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel92Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel92Index_Object = MibTableColumn
pmopm2Mesrchannel92Index = _Pmopm2Mesrchannel92Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 198, 1, 1),
    _Pmopm2Mesrchannel92Index_Type()
)
pmopm2Mesrchannel92Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel92Index.setStatus("current")


class _Pmopm2Mesrchannel92Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel92Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel92Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel92Portn_Object = MibTableColumn
pmopm2Mesrchannel92Portn = _Pmopm2Mesrchannel92Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 198, 1, 2),
    _Pmopm2Mesrchannel92Portn_Type()
)
pmopm2Mesrchannel92Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel92Portn.setStatus("current")
_Pmopm2Mesrchannel93Table_Object = MibTable
pmopm2Mesrchannel93Table = _Pmopm2Mesrchannel93Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 200)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel93Table.setStatus("current")
_Pmopm2Mesrchannel93Entry_Object = MibTableRow
pmopm2Mesrchannel93Entry = _Pmopm2Mesrchannel93Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 200, 1)
)
pmopm2Mesrchannel93Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel93Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel93Entry.setStatus("current")


class _Pmopm2Mesrchannel93Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel93Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel93Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel93Index_Object = MibTableColumn
pmopm2Mesrchannel93Index = _Pmopm2Mesrchannel93Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 200, 1, 1),
    _Pmopm2Mesrchannel93Index_Type()
)
pmopm2Mesrchannel93Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel93Index.setStatus("current")


class _Pmopm2Mesrchannel93Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel93Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel93Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel93Portn_Object = MibTableColumn
pmopm2Mesrchannel93Portn = _Pmopm2Mesrchannel93Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 200, 1, 2),
    _Pmopm2Mesrchannel93Portn_Type()
)
pmopm2Mesrchannel93Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel93Portn.setStatus("current")
_Pmopm2Mesrchannel94Table_Object = MibTable
pmopm2Mesrchannel94Table = _Pmopm2Mesrchannel94Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 202)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel94Table.setStatus("current")
_Pmopm2Mesrchannel94Entry_Object = MibTableRow
pmopm2Mesrchannel94Entry = _Pmopm2Mesrchannel94Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 202, 1)
)
pmopm2Mesrchannel94Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel94Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel94Entry.setStatus("current")


class _Pmopm2Mesrchannel94Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel94Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel94Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel94Index_Object = MibTableColumn
pmopm2Mesrchannel94Index = _Pmopm2Mesrchannel94Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 202, 1, 1),
    _Pmopm2Mesrchannel94Index_Type()
)
pmopm2Mesrchannel94Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel94Index.setStatus("current")


class _Pmopm2Mesrchannel94Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel94Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel94Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel94Portn_Object = MibTableColumn
pmopm2Mesrchannel94Portn = _Pmopm2Mesrchannel94Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 202, 1, 2),
    _Pmopm2Mesrchannel94Portn_Type()
)
pmopm2Mesrchannel94Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel94Portn.setStatus("current")
_Pmopm2Mesrchannel95Table_Object = MibTable
pmopm2Mesrchannel95Table = _Pmopm2Mesrchannel95Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 204)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel95Table.setStatus("current")
_Pmopm2Mesrchannel95Entry_Object = MibTableRow
pmopm2Mesrchannel95Entry = _Pmopm2Mesrchannel95Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 204, 1)
)
pmopm2Mesrchannel95Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel95Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel95Entry.setStatus("current")


class _Pmopm2Mesrchannel95Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel95Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel95Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel95Index_Object = MibTableColumn
pmopm2Mesrchannel95Index = _Pmopm2Mesrchannel95Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 204, 1, 1),
    _Pmopm2Mesrchannel95Index_Type()
)
pmopm2Mesrchannel95Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel95Index.setStatus("current")


class _Pmopm2Mesrchannel95Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel95Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel95Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel95Portn_Object = MibTableColumn
pmopm2Mesrchannel95Portn = _Pmopm2Mesrchannel95Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 204, 1, 2),
    _Pmopm2Mesrchannel95Portn_Type()
)
pmopm2Mesrchannel95Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel95Portn.setStatus("current")
_Pmopm2Mesrchannel96Table_Object = MibTable
pmopm2Mesrchannel96Table = _Pmopm2Mesrchannel96Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 206)
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel96Table.setStatus("current")
_Pmopm2Mesrchannel96Entry_Object = MibTableRow
pmopm2Mesrchannel96Entry = _Pmopm2Mesrchannel96Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 206, 1)
)
pmopm2Mesrchannel96Entry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2Mesrchannel96Index"),
)
if mibBuilder.loadTexts:
    pmopm2Mesrchannel96Entry.setStatus("current")


class _Pmopm2Mesrchannel96Index_Type(Integer32):
    """Custom type pmopm2Mesrchannel96Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2Mesrchannel96Index_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel96Index_Object = MibTableColumn
pmopm2Mesrchannel96Index = _Pmopm2Mesrchannel96Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 206, 1, 1),
    _Pmopm2Mesrchannel96Index_Type()
)
pmopm2Mesrchannel96Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel96Index.setStatus("current")


class _Pmopm2Mesrchannel96Portn_Type(Integer32):
    """Custom type pmopm2Mesrchannel96Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2Mesrchannel96Portn_Type.__name__ = "Integer32"
_Pmopm2Mesrchannel96Portn_Object = MibTableColumn
pmopm2Mesrchannel96Portn = _Pmopm2Mesrchannel96Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 206, 1, 2),
    _Pmopm2Mesrchannel96Portn_Type()
)
pmopm2Mesrchannel96Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Mesrchannel96Portn.setStatus("current")
_Pmopm2MesrportInputPwrTable_Object = MibTable
pmopm2MesrportInputPwrTable = _Pmopm2MesrportInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pmopm2MesrportInputPwrTable.setStatus("current")
_Pmopm2MesrportInputPwrEntry_Object = MibTableRow
pmopm2MesrportInputPwrEntry = _Pmopm2MesrportInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 208, 1)
)
pmopm2MesrportInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2MesrportInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pmopm2MesrportInputPwrEntry.setStatus("current")


class _Pmopm2MesrportInputPwrIndex_Type(Integer32):
    """Custom type pmopm2MesrportInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2MesrportInputPwrIndex_Type.__name__ = "Integer32"
_Pmopm2MesrportInputPwrIndex_Object = MibTableColumn
pmopm2MesrportInputPwrIndex = _Pmopm2MesrportInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 208, 1, 1),
    _Pmopm2MesrportInputPwrIndex_Type()
)
pmopm2MesrportInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2MesrportInputPwrIndex.setStatus("current")


class _Pmopm2MesrportInputPwrPortn_Type(Integer32):
    """Custom type pmopm2MesrportInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2MesrportInputPwrPortn_Type.__name__ = "Integer32"
_Pmopm2MesrportInputPwrPortn_Object = MibTableColumn
pmopm2MesrportInputPwrPortn = _Pmopm2MesrportInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 208, 1, 2),
    _Pmopm2MesrportInputPwrPortn_Type()
)
pmopm2MesrportInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2MesrportInputPwrPortn.setStatus("current")
_Pmopm2MesrchannelMaxPwrTable_Object = MibTable
pmopm2MesrchannelMaxPwrTable = _Pmopm2MesrchannelMaxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 210)
)
if mibBuilder.loadTexts:
    pmopm2MesrchannelMaxPwrTable.setStatus("current")
_Pmopm2MesrchannelMaxPwrEntry_Object = MibTableRow
pmopm2MesrchannelMaxPwrEntry = _Pmopm2MesrchannelMaxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 210, 1)
)
pmopm2MesrchannelMaxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2MesrchannelMaxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmopm2MesrchannelMaxPwrEntry.setStatus("current")


class _Pmopm2MesrchannelMaxPwrIndex_Type(Integer32):
    """Custom type pmopm2MesrchannelMaxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2MesrchannelMaxPwrIndex_Type.__name__ = "Integer32"
_Pmopm2MesrchannelMaxPwrIndex_Object = MibTableColumn
pmopm2MesrchannelMaxPwrIndex = _Pmopm2MesrchannelMaxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 210, 1, 1),
    _Pmopm2MesrchannelMaxPwrIndex_Type()
)
pmopm2MesrchannelMaxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2MesrchannelMaxPwrIndex.setStatus("current")


class _Pmopm2MesrchannelMaxPwrPortn_Type(Integer32):
    """Custom type pmopm2MesrchannelMaxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2MesrchannelMaxPwrPortn_Type.__name__ = "Integer32"
_Pmopm2MesrchannelMaxPwrPortn_Object = MibTableColumn
pmopm2MesrchannelMaxPwrPortn = _Pmopm2MesrchannelMaxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 210, 1, 2),
    _Pmopm2MesrchannelMaxPwrPortn_Type()
)
pmopm2MesrchannelMaxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2MesrchannelMaxPwrPortn.setStatus("current")
_Pmopm2MesrchannelMinPwrTable_Object = MibTable
pmopm2MesrchannelMinPwrTable = _Pmopm2MesrchannelMinPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pmopm2MesrchannelMinPwrTable.setStatus("current")
_Pmopm2MesrchannelMinPwrEntry_Object = MibTableRow
pmopm2MesrchannelMinPwrEntry = _Pmopm2MesrchannelMinPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 212, 1)
)
pmopm2MesrchannelMinPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2MesrchannelMinPwrIndex"),
)
if mibBuilder.loadTexts:
    pmopm2MesrchannelMinPwrEntry.setStatus("current")


class _Pmopm2MesrchannelMinPwrIndex_Type(Integer32):
    """Custom type pmopm2MesrchannelMinPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2MesrchannelMinPwrIndex_Type.__name__ = "Integer32"
_Pmopm2MesrchannelMinPwrIndex_Object = MibTableColumn
pmopm2MesrchannelMinPwrIndex = _Pmopm2MesrchannelMinPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 212, 1, 1),
    _Pmopm2MesrchannelMinPwrIndex_Type()
)
pmopm2MesrchannelMinPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2MesrchannelMinPwrIndex.setStatus("current")


class _Pmopm2MesrchannelMinPwrPortn_Type(Integer32):
    """Custom type pmopm2MesrchannelMinPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2MesrchannelMinPwrPortn_Type.__name__ = "Integer32"
_Pmopm2MesrchannelMinPwrPortn_Object = MibTableColumn
pmopm2MesrchannelMinPwrPortn = _Pmopm2MesrchannelMinPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 2, 212, 1, 2),
    _Pmopm2MesrchannelMinPwrPortn_Type()
)
pmopm2MesrchannelMinPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2MesrchannelMinPwrPortn.setStatus("current")
_Pmopm2MesrLine_ObjectIdentity = ObjectIdentity
pmopm2MesrLine = _Pmopm2MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 3, 3)
)
_Pmopm2controlsWrite_ObjectIdentity = ObjectIdentity
pmopm2controlsWrite = _Pmopm2controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6)
)
_Pmopm2CtrlOther_ObjectIdentity = ObjectIdentity
pmopm2CtrlOther = _Pmopm2CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1)
)
_Pmopm2CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmopm2CtrlconfMgnt1 = _Pmopm2CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 1)
)
_Pmopm2CtrlConf1Load1_Type = EkiOnOff
_Pmopm2CtrlConf1Load1_Object = MibScalar
pmopm2CtrlConf1Load1 = _Pmopm2CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 1, 1),
    _Pmopm2CtrlConf1Load1_Type()
)
pmopm2CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlConf1Load1.setStatus("current")
_Pmopm2CtrlConf2Load1_Type = EkiOnOff
_Pmopm2CtrlConf2Load1_Object = MibScalar
pmopm2CtrlConf2Load1 = _Pmopm2CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 1, 2),
    _Pmopm2CtrlConf2Load1_Type()
)
pmopm2CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlConf2Load1.setStatus("current")
_Pmopm2CtrlConf2Flash1_Type = EkiOnOff
_Pmopm2CtrlConf2Flash1_Object = MibScalar
pmopm2CtrlConf2Flash1 = _Pmopm2CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 1, 10),
    _Pmopm2CtrlConf2Flash1_Type()
)
pmopm2CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlConf2Flash1.setStatus("current")
_Pmopm2CtrlConf2Clear1_Type = EkiOnOff
_Pmopm2CtrlConf2Clear1_Object = MibScalar
pmopm2CtrlConf2Clear1 = _Pmopm2CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 1, 14),
    _Pmopm2CtrlConf2Clear1_Type()
)
pmopm2CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlConf2Clear1.setStatus("current")
_Pmopm2Ctrlsynth4_ObjectIdentity = ObjectIdentity
pmopm2Ctrlsynth4 = _Pmopm2Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 4)
)
_Pmopm2CtrlCorrelatOn_Type = EkiOnOff
_Pmopm2CtrlCorrelatOn_Object = MibScalar
pmopm2CtrlCorrelatOn = _Pmopm2CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 4, 1),
    _Pmopm2CtrlCorrelatOn_Type()
)
pmopm2CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlCorrelatOn.setStatus("current")
_Pmopm2CtrlCorrelatOff_Type = EkiOnOff
_Pmopm2CtrlCorrelatOff_Object = MibScalar
pmopm2CtrlCorrelatOff = _Pmopm2CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 4, 2),
    _Pmopm2CtrlCorrelatOff_Type()
)
pmopm2CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlCorrelatOff.setStatus("current")
_Pmopm2CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmopm2CtrlswMgnt = _Pmopm2CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 5)
)
_Pmopm2CtrlColdReset_Type = EkiOnOff
_Pmopm2CtrlColdReset_Object = MibScalar
pmopm2CtrlColdReset = _Pmopm2CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 5, 2),
    _Pmopm2CtrlColdReset_Type()
)
pmopm2CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlColdReset.setStatus("current")
_Pmopm2CtrlWarmReset_Type = EkiOnOff
_Pmopm2CtrlWarmReset_Object = MibScalar
pmopm2CtrlWarmReset = _Pmopm2CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 5, 3),
    _Pmopm2CtrlWarmReset_Type()
)
pmopm2CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlWarmReset.setStatus("current")
_Pmopm2CtrlLoadSwBank1_Type = EkiOnOff
_Pmopm2CtrlLoadSwBank1_Object = MibScalar
pmopm2CtrlLoadSwBank1 = _Pmopm2CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 5, 5),
    _Pmopm2CtrlLoadSwBank1_Type()
)
pmopm2CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlLoadSwBank1.setStatus("current")
_Pmopm2CtrlLoadSwBank2_Type = EkiOnOff
_Pmopm2CtrlLoadSwBank2_Object = MibScalar
pmopm2CtrlLoadSwBank2 = _Pmopm2CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 5, 6),
    _Pmopm2CtrlLoadSwBank2_Type()
)
pmopm2CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlLoadSwBank2.setStatus("current")
_Pmopm2CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmopm2CtrlgwMgnt = _Pmopm2CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 6)
)
_Pmopm2CtrlCurrentGwReset_Type = EkiOnOff
_Pmopm2CtrlCurrentGwReset_Object = MibScalar
pmopm2CtrlCurrentGwReset = _Pmopm2CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 6, 1),
    _Pmopm2CtrlCurrentGwReset_Type()
)
pmopm2CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlCurrentGwReset.setStatus("current")
_Pmopm2CtrlLoadGwBank1_Type = EkiOnOff
_Pmopm2CtrlLoadGwBank1_Object = MibScalar
pmopm2CtrlLoadGwBank1 = _Pmopm2CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 6, 5),
    _Pmopm2CtrlLoadGwBank1_Type()
)
pmopm2CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlLoadGwBank1.setStatus("current")
_Pmopm2CtrlLoadGwBank2_Type = EkiOnOff
_Pmopm2CtrlLoadGwBank2_Object = MibScalar
pmopm2CtrlLoadGwBank2 = _Pmopm2CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 6, 6),
    _Pmopm2CtrlLoadGwBank2_Type()
)
pmopm2CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlLoadGwBank2.setStatus("current")
_Pmopm2CtrlLoadGwBank3_Type = EkiOnOff
_Pmopm2CtrlLoadGwBank3_Object = MibScalar
pmopm2CtrlLoadGwBank3 = _Pmopm2CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 6, 7),
    _Pmopm2CtrlLoadGwBank3_Type()
)
pmopm2CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlLoadGwBank3.setStatus("current")
_Pmopm2CtrlLoadGwBank4_Type = EkiOnOff
_Pmopm2CtrlLoadGwBank4_Object = MibScalar
pmopm2CtrlLoadGwBank4 = _Pmopm2CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 6, 8),
    _Pmopm2CtrlLoadGwBank4_Type()
)
pmopm2CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlLoadGwBank4.setStatus("current")
_Pmopm2CtrlledTest_ObjectIdentity = ObjectIdentity
pmopm2CtrlledTest = _Pmopm2CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 192)
)
_Pmopm2CtrlGreenLed_Type = EkiOnOff
_Pmopm2CtrlGreenLed_Object = MibScalar
pmopm2CtrlGreenLed = _Pmopm2CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 192, 1),
    _Pmopm2CtrlGreenLed_Type()
)
pmopm2CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlGreenLed.setStatus("current")
_Pmopm2CtrlRedLed_Type = EkiOnOff
_Pmopm2CtrlRedLed_Object = MibScalar
pmopm2CtrlRedLed = _Pmopm2CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 192, 2),
    _Pmopm2CtrlRedLed_Type()
)
pmopm2CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlRedLed.setStatus("current")
_Pmopm2CtrlLedOff_Type = EkiOnOff
_Pmopm2CtrlLedOff_Object = MibScalar
pmopm2CtrlLedOff = _Pmopm2CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 1, 192, 3),
    _Pmopm2CtrlLedOff_Type()
)
pmopm2CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlLedOff.setStatus("current")
_Pmopm2CtrlClient_ObjectIdentity = ObjectIdentity
pmopm2CtrlClient = _Pmopm2CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2)
)
_Pmopm2CtrlcalibrationTable_Object = MibTable
pmopm2CtrlcalibrationTable = _Pmopm2CtrlcalibrationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pmopm2CtrlcalibrationTable.setStatus("current")
_Pmopm2CtrlcalibrationEntry_Object = MibTableRow
pmopm2CtrlcalibrationEntry = _Pmopm2CtrlcalibrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 16, 1)
)
pmopm2CtrlcalibrationEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CtrlcalibrationIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CtrlcalibrationEntry.setStatus("current")


class _Pmopm2CtrlcalibrationIndex_Type(Integer32):
    """Custom type pmopm2CtrlcalibrationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CtrlcalibrationIndex_Type.__name__ = "Integer32"
_Pmopm2CtrlcalibrationIndex_Object = MibTableColumn
pmopm2CtrlcalibrationIndex = _Pmopm2CtrlcalibrationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 16, 1, 1),
    _Pmopm2CtrlcalibrationIndex_Type()
)
pmopm2CtrlcalibrationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CtrlcalibrationIndex.setStatus("current")
_Pmopm2CtrlcalibrationPortn_Type = EkiState
_Pmopm2CtrlcalibrationPortn_Object = MibTableColumn
pmopm2CtrlcalibrationPortn = _Pmopm2CtrlcalibrationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 16, 1, 2),
    _Pmopm2CtrlcalibrationPortn_Type()
)
pmopm2CtrlcalibrationPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlcalibrationPortn.setStatus("current")
_Pmopm2CtrlspectrumAutodiscoveryTable_Object = MibTable
pmopm2CtrlspectrumAutodiscoveryTable = _Pmopm2CtrlspectrumAutodiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pmopm2CtrlspectrumAutodiscoveryTable.setStatus("current")
_Pmopm2CtrlspectrumAutodiscoveryEntry_Object = MibTableRow
pmopm2CtrlspectrumAutodiscoveryEntry = _Pmopm2CtrlspectrumAutodiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 17, 1)
)
pmopm2CtrlspectrumAutodiscoveryEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CtrlspectrumAutodiscoveryIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CtrlspectrumAutodiscoveryEntry.setStatus("current")


class _Pmopm2CtrlspectrumAutodiscoveryIndex_Type(Integer32):
    """Custom type pmopm2CtrlspectrumAutodiscoveryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CtrlspectrumAutodiscoveryIndex_Type.__name__ = "Integer32"
_Pmopm2CtrlspectrumAutodiscoveryIndex_Object = MibTableColumn
pmopm2CtrlspectrumAutodiscoveryIndex = _Pmopm2CtrlspectrumAutodiscoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 17, 1, 1),
    _Pmopm2CtrlspectrumAutodiscoveryIndex_Type()
)
pmopm2CtrlspectrumAutodiscoveryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CtrlspectrumAutodiscoveryIndex.setStatus("current")
_Pmopm2CtrlspectrumAutodiscoveryPortn_Type = EkiState
_Pmopm2CtrlspectrumAutodiscoveryPortn_Object = MibTableColumn
pmopm2CtrlspectrumAutodiscoveryPortn = _Pmopm2CtrlspectrumAutodiscoveryPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 17, 1, 2),
    _Pmopm2CtrlspectrumAutodiscoveryPortn_Type()
)
pmopm2CtrlspectrumAutodiscoveryPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlspectrumAutodiscoveryPortn.setStatus("current")
_Pmopm2CtrlthresholdsAutoconfigTable_Object = MibTable
pmopm2CtrlthresholdsAutoconfigTable = _Pmopm2CtrlthresholdsAutoconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pmopm2CtrlthresholdsAutoconfigTable.setStatus("current")
_Pmopm2CtrlthresholdsAutoconfigEntry_Object = MibTableRow
pmopm2CtrlthresholdsAutoconfigEntry = _Pmopm2CtrlthresholdsAutoconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 18, 1)
)
pmopm2CtrlthresholdsAutoconfigEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CtrlthresholdsAutoconfigIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CtrlthresholdsAutoconfigEntry.setStatus("current")


class _Pmopm2CtrlthresholdsAutoconfigIndex_Type(Integer32):
    """Custom type pmopm2CtrlthresholdsAutoconfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CtrlthresholdsAutoconfigIndex_Type.__name__ = "Integer32"
_Pmopm2CtrlthresholdsAutoconfigIndex_Object = MibTableColumn
pmopm2CtrlthresholdsAutoconfigIndex = _Pmopm2CtrlthresholdsAutoconfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 18, 1, 1),
    _Pmopm2CtrlthresholdsAutoconfigIndex_Type()
)
pmopm2CtrlthresholdsAutoconfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CtrlthresholdsAutoconfigIndex.setStatus("current")
_Pmopm2CtrlthresholdsAutoconfigPortn_Type = EkiState
_Pmopm2CtrlthresholdsAutoconfigPortn_Object = MibTableColumn
pmopm2CtrlthresholdsAutoconfigPortn = _Pmopm2CtrlthresholdsAutoconfigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 18, 1, 2),
    _Pmopm2CtrlthresholdsAutoconfigPortn_Type()
)
pmopm2CtrlthresholdsAutoconfigPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlthresholdsAutoconfigPortn.setStatus("current")
_Pmopm2CtrlpowerLossDeltaTable_Object = MibTable
pmopm2CtrlpowerLossDeltaTable = _Pmopm2CtrlpowerLossDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 32)
)
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLossDeltaTable.setStatus("current")
_Pmopm2CtrlpowerLossDeltaEntry_Object = MibTableRow
pmopm2CtrlpowerLossDeltaEntry = _Pmopm2CtrlpowerLossDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 32, 1)
)
pmopm2CtrlpowerLossDeltaEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CtrlpowerLossDeltaIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLossDeltaEntry.setStatus("current")


class _Pmopm2CtrlpowerLossDeltaIndex_Type(Integer32):
    """Custom type pmopm2CtrlpowerLossDeltaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CtrlpowerLossDeltaIndex_Type.__name__ = "Integer32"
_Pmopm2CtrlpowerLossDeltaIndex_Object = MibTableColumn
pmopm2CtrlpowerLossDeltaIndex = _Pmopm2CtrlpowerLossDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 32, 1, 1),
    _Pmopm2CtrlpowerLossDeltaIndex_Type()
)
pmopm2CtrlpowerLossDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLossDeltaIndex.setStatus("current")


class _Pmopm2CtrlpowerLossDeltaPortn_Type(Integer32):
    """Custom type pmopm2CtrlpowerLossDeltaPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2CtrlpowerLossDeltaPortn_Type.__name__ = "Integer32"
_Pmopm2CtrlpowerLossDeltaPortn_Object = MibTableColumn
pmopm2CtrlpowerLossDeltaPortn = _Pmopm2CtrlpowerLossDeltaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 32, 1, 2),
    _Pmopm2CtrlpowerLossDeltaPortn_Type()
)
pmopm2CtrlpowerLossDeltaPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLossDeltaPortn.setStatus("current")
_Pmopm2CtrlpowerHighDeltaTable_Object = MibTable
pmopm2CtrlpowerHighDeltaTable = _Pmopm2CtrlpowerHighDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 40)
)
if mibBuilder.loadTexts:
    pmopm2CtrlpowerHighDeltaTable.setStatus("current")
_Pmopm2CtrlpowerHighDeltaEntry_Object = MibTableRow
pmopm2CtrlpowerHighDeltaEntry = _Pmopm2CtrlpowerHighDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 40, 1)
)
pmopm2CtrlpowerHighDeltaEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CtrlpowerHighDeltaIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CtrlpowerHighDeltaEntry.setStatus("current")


class _Pmopm2CtrlpowerHighDeltaIndex_Type(Integer32):
    """Custom type pmopm2CtrlpowerHighDeltaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CtrlpowerHighDeltaIndex_Type.__name__ = "Integer32"
_Pmopm2CtrlpowerHighDeltaIndex_Object = MibTableColumn
pmopm2CtrlpowerHighDeltaIndex = _Pmopm2CtrlpowerHighDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 40, 1, 1),
    _Pmopm2CtrlpowerHighDeltaIndex_Type()
)
pmopm2CtrlpowerHighDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CtrlpowerHighDeltaIndex.setStatus("current")


class _Pmopm2CtrlpowerHighDeltaPortn_Type(Integer32):
    """Custom type pmopm2CtrlpowerHighDeltaPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2CtrlpowerHighDeltaPortn_Type.__name__ = "Integer32"
_Pmopm2CtrlpowerHighDeltaPortn_Object = MibTableColumn
pmopm2CtrlpowerHighDeltaPortn = _Pmopm2CtrlpowerHighDeltaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 40, 1, 2),
    _Pmopm2CtrlpowerHighDeltaPortn_Type()
)
pmopm2CtrlpowerHighDeltaPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlpowerHighDeltaPortn.setStatus("current")
_Pmopm2CtrlpowerLowDeltaTable_Object = MibTable
pmopm2CtrlpowerLowDeltaTable = _Pmopm2CtrlpowerLowDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 48)
)
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLowDeltaTable.setStatus("current")
_Pmopm2CtrlpowerLowDeltaEntry_Object = MibTableRow
pmopm2CtrlpowerLowDeltaEntry = _Pmopm2CtrlpowerLowDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 48, 1)
)
pmopm2CtrlpowerLowDeltaEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CtrlpowerLowDeltaIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLowDeltaEntry.setStatus("current")


class _Pmopm2CtrlpowerLowDeltaIndex_Type(Integer32):
    """Custom type pmopm2CtrlpowerLowDeltaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CtrlpowerLowDeltaIndex_Type.__name__ = "Integer32"
_Pmopm2CtrlpowerLowDeltaIndex_Object = MibTableColumn
pmopm2CtrlpowerLowDeltaIndex = _Pmopm2CtrlpowerLowDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 48, 1, 1),
    _Pmopm2CtrlpowerLowDeltaIndex_Type()
)
pmopm2CtrlpowerLowDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLowDeltaIndex.setStatus("current")


class _Pmopm2CtrlpowerLowDeltaPortn_Type(Integer32):
    """Custom type pmopm2CtrlpowerLowDeltaPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2CtrlpowerLowDeltaPortn_Type.__name__ = "Integer32"
_Pmopm2CtrlpowerLowDeltaPortn_Object = MibTableColumn
pmopm2CtrlpowerLowDeltaPortn = _Pmopm2CtrlpowerLowDeltaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 48, 1, 2),
    _Pmopm2CtrlpowerLowDeltaPortn_Type()
)
pmopm2CtrlpowerLowDeltaPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlpowerLowDeltaPortn.setStatus("current")
_Pmopm2CtrlinputPowerRefTable_Object = MibTable
pmopm2CtrlinputPowerRefTable = _Pmopm2CtrlinputPowerRefTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 64)
)
if mibBuilder.loadTexts:
    pmopm2CtrlinputPowerRefTable.setStatus("current")
_Pmopm2CtrlinputPowerRefEntry_Object = MibTableRow
pmopm2CtrlinputPowerRefEntry = _Pmopm2CtrlinputPowerRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 64, 1)
)
pmopm2CtrlinputPowerRefEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CtrlinputPowerRefIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CtrlinputPowerRefEntry.setStatus("current")


class _Pmopm2CtrlinputPowerRefIndex_Type(Integer32):
    """Custom type pmopm2CtrlinputPowerRefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CtrlinputPowerRefIndex_Type.__name__ = "Integer32"
_Pmopm2CtrlinputPowerRefIndex_Object = MibTableColumn
pmopm2CtrlinputPowerRefIndex = _Pmopm2CtrlinputPowerRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 64, 1, 1),
    _Pmopm2CtrlinputPowerRefIndex_Type()
)
pmopm2CtrlinputPowerRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CtrlinputPowerRefIndex.setStatus("current")


class _Pmopm2CtrlinputPowerRefPortn_Type(Integer32):
    """Custom type pmopm2CtrlinputPowerRefPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmopm2CtrlinputPowerRefPortn_Type.__name__ = "Integer32"
_Pmopm2CtrlinputPowerRefPortn_Object = MibTableColumn
pmopm2CtrlinputPowerRefPortn = _Pmopm2CtrlinputPowerRefPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 2, 64, 1, 2),
    _Pmopm2CtrlinputPowerRefPortn_Type()
)
pmopm2CtrlinputPowerRefPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CtrlinputPowerRefPortn.setStatus("current")
_Pmopm2CtrlLine_ObjectIdentity = ObjectIdentity
pmopm2CtrlLine = _Pmopm2CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 6, 3)
)
_Pmopm2ri_ObjectIdentity = ObjectIdentity
pmopm2ri = _Pmopm2ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7)
)
_Pmopm2riTable_ObjectIdentity = ObjectIdentity
pmopm2riTable = _Pmopm2riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1)
)
_Pmopm2RinvSfpTable_Object = MibTable
pmopm2RinvSfpTable = _Pmopm2RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmopm2RinvSfpTable.setStatus("current")
_Pmopm2RinvSfpEntry_Object = MibTableRow
pmopm2RinvSfpEntry = _Pmopm2RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 1, 1)
)
pmopm2RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pmopm2RinvSfpEntry.setStatus("current")


class _Pmopm2RinvSfpIndex_Type(Integer32):
    """Custom type pmopm2RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmopm2RinvSfpIndex_Type.__name__ = "Integer32"
_Pmopm2RinvSfpIndex_Object = MibTableColumn
pmopm2RinvSfpIndex = _Pmopm2RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 1, 1, 1),
    _Pmopm2RinvSfpIndex_Type()
)
pmopm2RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2RinvSfpIndex.setStatus("current")
_Pmopm2Rinvsfp_Type = DisplayString
_Pmopm2Rinvsfp_Object = MibTableColumn
pmopm2Rinvsfp = _Pmopm2Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 1, 1, 2),
    _Pmopm2Rinvsfp_Type()
)
pmopm2Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Rinvsfp.setStatus("current")
_Pmopm2RinvLineTable_Object = MibTable
pmopm2RinvLineTable = _Pmopm2RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmopm2RinvLineTable.setStatus("current")
_Pmopm2RinvLineEntry_Object = MibTableRow
pmopm2RinvLineEntry = _Pmopm2RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 2, 1)
)
pmopm2RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmopm2RinvLineEntry.setStatus("current")


class _Pmopm2RinvLineIndex_Type(Integer32):
    """Custom type pmopm2RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmopm2RinvLineIndex_Type.__name__ = "Integer32"
_Pmopm2RinvLineIndex_Object = MibTableColumn
pmopm2RinvLineIndex = _Pmopm2RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 2, 1, 1),
    _Pmopm2RinvLineIndex_Type()
)
pmopm2RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2RinvLineIndex.setStatus("current")
_Pmopm2RinvxfpLine_Type = DisplayString
_Pmopm2RinvxfpLine_Object = MibTableColumn
pmopm2RinvxfpLine = _Pmopm2RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 1, 2, 1, 2),
    _Pmopm2RinvxfpLine_Type()
)
pmopm2RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2RinvxfpLine.setStatus("current")
_Pmopm2RinvReloadInventory_Type = EkiOnOff
_Pmopm2RinvReloadInventory_Object = MibScalar
pmopm2RinvReloadInventory = _Pmopm2RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 2),
    _Pmopm2RinvReloadInventory_Type()
)
pmopm2RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2RinvReloadInventory.setStatus("current")
_Pmopm2RinvHwPlatform_Type = DisplayString
_Pmopm2RinvHwPlatform_Object = MibScalar
pmopm2RinvHwPlatform = _Pmopm2RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 3),
    _Pmopm2RinvHwPlatform_Type()
)
pmopm2RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2RinvHwPlatform.setStatus("current")
_Pmopm2RinvModulePlatform_Type = DisplayString
_Pmopm2RinvModulePlatform_Object = MibScalar
pmopm2RinvModulePlatform = _Pmopm2RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 4),
    _Pmopm2RinvModulePlatform_Type()
)
pmopm2RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2RinvModulePlatform.setStatus("current")
_Pmopm2RinvSwPlatform_Type = DisplayString
_Pmopm2RinvSwPlatform_Object = MibScalar
pmopm2RinvSwPlatform = _Pmopm2RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 5),
    _Pmopm2RinvSwPlatform_Type()
)
pmopm2RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2RinvSwPlatform.setStatus("current")
_Pmopm2RinvGwPlatform_Type = DisplayString
_Pmopm2RinvGwPlatform_Object = MibScalar
pmopm2RinvGwPlatform = _Pmopm2RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 7, 6),
    _Pmopm2RinvGwPlatform_Type()
)
pmopm2RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2RinvGwPlatform.setStatus("current")
_Pmopm2download_ObjectIdentity = ObjectIdentity
pmopm2download = _Pmopm2download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8)
)
_Pmopm2DwlOther_ObjectIdentity = ObjectIdentity
pmopm2DwlOther = _Pmopm2DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1)
)
_Pmopm2DwlrestartProcess_ObjectIdentity = ObjectIdentity
pmopm2DwlrestartProcess = _Pmopm2DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 0)
)
_Pmopm2DwlWarmRestartProcessed_Type = EkiOnOff
_Pmopm2DwlWarmRestartProcessed_Object = MibScalar
pmopm2DwlWarmRestartProcessed = _Pmopm2DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 0, 1),
    _Pmopm2DwlWarmRestartProcessed_Type()
)
pmopm2DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlWarmRestartProcessed.setStatus("current")
_Pmopm2DwlColdRestartProcessed_Type = EkiOnOff
_Pmopm2DwlColdRestartProcessed_Object = MibScalar
pmopm2DwlColdRestartProcessed = _Pmopm2DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 0, 2),
    _Pmopm2DwlColdRestartProcessed_Type()
)
pmopm2DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlColdRestartProcessed.setStatus("current")
_Pmopm2DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmopm2DwlswBanksUsed = _Pmopm2DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 1)
)
_Pmopm2DwlSwBank1Used_Type = EkiOnOff
_Pmopm2DwlSwBank1Used_Object = MibScalar
pmopm2DwlSwBank1Used = _Pmopm2DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 1, 1),
    _Pmopm2DwlSwBank1Used_Type()
)
pmopm2DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlSwBank1Used.setStatus("current")
_Pmopm2DwlSwBank2Used_Type = EkiOnOff
_Pmopm2DwlSwBank2Used_Object = MibScalar
pmopm2DwlSwBank2Used = _Pmopm2DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 1, 2),
    _Pmopm2DwlSwBank2Used_Type()
)
pmopm2DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlSwBank2Used.setStatus("current")
_Pmopm2DwlSwBank1Notempty_Type = EkiOnOff
_Pmopm2DwlSwBank1Notempty_Object = MibScalar
pmopm2DwlSwBank1Notempty = _Pmopm2DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 1, 5),
    _Pmopm2DwlSwBank1Notempty_Type()
)
pmopm2DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlSwBank1Notempty.setStatus("current")
_Pmopm2DwlSwBank2Notempty_Type = EkiOnOff
_Pmopm2DwlSwBank2Notempty_Object = MibScalar
pmopm2DwlSwBank2Notempty = _Pmopm2DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 1, 6),
    _Pmopm2DwlSwBank2Notempty_Type()
)
pmopm2DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlSwBank2Notempty.setStatus("current")
_Pmopm2DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmopm2DwlgwBanksUsed = _Pmopm2DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2)
)
_Pmopm2DwlGwBank1Used_Type = EkiOnOff
_Pmopm2DwlGwBank1Used_Object = MibScalar
pmopm2DwlGwBank1Used = _Pmopm2DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 1),
    _Pmopm2DwlGwBank1Used_Type()
)
pmopm2DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank1Used.setStatus("current")
_Pmopm2DwlGwBank2Used_Type = EkiOnOff
_Pmopm2DwlGwBank2Used_Object = MibScalar
pmopm2DwlGwBank2Used = _Pmopm2DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 2),
    _Pmopm2DwlGwBank2Used_Type()
)
pmopm2DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank2Used.setStatus("current")
_Pmopm2DwlGwBank3Used_Type = EkiOnOff
_Pmopm2DwlGwBank3Used_Object = MibScalar
pmopm2DwlGwBank3Used = _Pmopm2DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 3),
    _Pmopm2DwlGwBank3Used_Type()
)
pmopm2DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank3Used.setStatus("current")
_Pmopm2DwlGwBank4Used_Type = EkiOnOff
_Pmopm2DwlGwBank4Used_Object = MibScalar
pmopm2DwlGwBank4Used = _Pmopm2DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 4),
    _Pmopm2DwlGwBank4Used_Type()
)
pmopm2DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank4Used.setStatus("current")
_Pmopm2DwlGwBank1Notempty_Type = EkiOnOff
_Pmopm2DwlGwBank1Notempty_Object = MibScalar
pmopm2DwlGwBank1Notempty = _Pmopm2DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 5),
    _Pmopm2DwlGwBank1Notempty_Type()
)
pmopm2DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank1Notempty.setStatus("current")
_Pmopm2DwlGwBank2Notempty_Type = EkiOnOff
_Pmopm2DwlGwBank2Notempty_Object = MibScalar
pmopm2DwlGwBank2Notempty = _Pmopm2DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 6),
    _Pmopm2DwlGwBank2Notempty_Type()
)
pmopm2DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank2Notempty.setStatus("current")
_Pmopm2DwlGwBank3Notempty_Type = EkiOnOff
_Pmopm2DwlGwBank3Notempty_Object = MibScalar
pmopm2DwlGwBank3Notempty = _Pmopm2DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 7),
    _Pmopm2DwlGwBank3Notempty_Type()
)
pmopm2DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank3Notempty.setStatus("current")
_Pmopm2DwlGwBank4Notempty_Type = EkiOnOff
_Pmopm2DwlGwBank4Notempty_Object = MibScalar
pmopm2DwlGwBank4Notempty = _Pmopm2DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 1, 2, 8),
    _Pmopm2DwlGwBank4Notempty_Type()
)
pmopm2DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2DwlGwBank4Notempty.setStatus("current")
_Pmopm2DwlClient_ObjectIdentity = ObjectIdentity
pmopm2DwlClient = _Pmopm2DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 2)
)
_Pmopm2DwlLine_ObjectIdentity = ObjectIdentity
pmopm2DwlLine = _Pmopm2DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 8, 3)
)
_Pmopm2Config_ObjectIdentity = ObjectIdentity
pmopm2Config = _Pmopm2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9)
)
_Pmopm2CfgLsd_ObjectIdentity = ObjectIdentity
pmopm2CfgLsd = _Pmopm2CfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 1)
)
_Pmopm2tableclientcaiscsf_ObjectIdentity = ObjectIdentity
pmopm2tableclientcaiscsf = _Pmopm2tableclientcaiscsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 1, 1)
)
_Pmopm2CfgStartup_ObjectIdentity = ObjectIdentity
pmopm2CfgStartup = _Pmopm2CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2)
)
_Pmopm2tableother_ObjectIdentity = ObjectIdentity
pmopm2tableother = _Pmopm2tableother_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 1)
)


class _Pmopm2CfgcomponentType_Type(Unsigned32):
    """Custom type pmopm2CfgcomponentType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgcomponentType_Type.__name__ = "Unsigned32"
_Pmopm2CfgcomponentType_Object = MibScalar
pmopm2CfgcomponentType = _Pmopm2CfgcomponentType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 1, 2),
    _Pmopm2CfgcomponentType_Type()
)
pmopm2CfgcomponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgcomponentType.setStatus("current")


class _Pmopm2Cfgmiscellaneous_Type(Unsigned32):
    """Custom type pmopm2Cfgmiscellaneous based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2Cfgmiscellaneous_Type.__name__ = "Unsigned32"
_Pmopm2Cfgmiscellaneous_Object = MibScalar
pmopm2Cfgmiscellaneous = _Pmopm2Cfgmiscellaneous_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 1, 3),
    _Pmopm2Cfgmiscellaneous_Type()
)
pmopm2Cfgmiscellaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Cfgmiscellaneous.setStatus("current")


class _Pmopm2CfgfirstChannel_Type(Unsigned32):
    """Custom type pmopm2CfgfirstChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgfirstChannel_Type.__name__ = "Unsigned32"
_Pmopm2CfgfirstChannel_Object = MibScalar
pmopm2CfgfirstChannel = _Pmopm2CfgfirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 1, 4),
    _Pmopm2CfgfirstChannel_Type()
)
pmopm2CfgfirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgfirstChannel.setStatus("current")


class _Pmopm2CfglastChannel_Type(Unsigned32):
    """Custom type pmopm2CfglastChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfglastChannel_Type.__name__ = "Unsigned32"
_Pmopm2CfglastChannel_Object = MibScalar
pmopm2CfglastChannel = _Pmopm2CfglastChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 1, 5),
    _Pmopm2CfglastChannel_Type()
)
pmopm2CfglastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfglastChannel.setStatus("current")


class _Pmopm2Cfggrid_Type(Unsigned32):
    """Custom type pmopm2Cfggrid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2Cfggrid_Type.__name__ = "Unsigned32"
_Pmopm2Cfggrid_Object = MibScalar
pmopm2Cfggrid = _Pmopm2Cfggrid_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 1, 6),
    _Pmopm2Cfggrid_Type()
)
pmopm2Cfggrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2Cfggrid.setStatus("current")
_Pmopm2CfgClientStartupOosTable_Object = MibTable
pmopm2CfgClientStartupOosTable = _Pmopm2CfgClientStartupOosTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupOosTable.setStatus("current")
_Pmopm2CfgClientStartupOosEntry_Object = MibTableRow
pmopm2CfgClientStartupOosEntry = _Pmopm2CfgClientStartupOosEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1)
)
pmopm2CfgClientStartupOosEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CfgClientStartupOosIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupOosEntry.setStatus("current")


class _Pmopm2CfgClientStartupOosIndex_Type(Integer32):
    """Custom type pmopm2CfgClientStartupOosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CfgClientStartupOosIndex_Type.__name__ = "Integer32"
_Pmopm2CfgClientStartupOosIndex_Object = MibTableColumn
pmopm2CfgClientStartupOosIndex = _Pmopm2CfgClientStartupOosIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 1),
    _Pmopm2CfgClientStartupOosIndex_Type()
)
pmopm2CfgClientStartupOosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupOosIndex.setStatus("current")


class _Pmopm2CfgSpectrumOosPortn_Type(Unsigned32):
    """Custom type pmopm2CfgSpectrumOosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgSpectrumOosPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgSpectrumOosPortn_Object = MibTableColumn
pmopm2CfgSpectrumOosPortn = _Pmopm2CfgSpectrumOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 3),
    _Pmopm2CfgSpectrumOosPortn_Type()
)
pmopm2CfgSpectrumOosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgSpectrumOosPortn.setStatus("current")


class _Pmopm2CfgSpectrumOffsetPortn_Type(Unsigned32):
    """Custom type pmopm2CfgSpectrumOffsetPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgSpectrumOffsetPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgSpectrumOffsetPortn_Object = MibTableColumn
pmopm2CfgSpectrumOffsetPortn = _Pmopm2CfgSpectrumOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 4),
    _Pmopm2CfgSpectrumOffsetPortn_Type()
)
pmopm2CfgSpectrumOffsetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgSpectrumOffsetPortn.setStatus("current")


class _Pmopm2CfgCh1Ch16OosPortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh1Ch16OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh1Ch16OosPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh1Ch16OosPortn_Object = MibTableColumn
pmopm2CfgCh1Ch16OosPortn = _Pmopm2CfgCh1Ch16OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 5),
    _Pmopm2CfgCh1Ch16OosPortn_Type()
)
pmopm2CfgCh1Ch16OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh1Ch16OosPortn.setStatus("current")


class _Pmopm2CfgCh17Ch32OosPortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh17Ch32OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh17Ch32OosPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh17Ch32OosPortn_Object = MibTableColumn
pmopm2CfgCh17Ch32OosPortn = _Pmopm2CfgCh17Ch32OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 6),
    _Pmopm2CfgCh17Ch32OosPortn_Type()
)
pmopm2CfgCh17Ch32OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh17Ch32OosPortn.setStatus("current")


class _Pmopm2CfgCh33Ch48OosPortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh33Ch48OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh33Ch48OosPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh33Ch48OosPortn_Object = MibTableColumn
pmopm2CfgCh33Ch48OosPortn = _Pmopm2CfgCh33Ch48OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 7),
    _Pmopm2CfgCh33Ch48OosPortn_Type()
)
pmopm2CfgCh33Ch48OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh33Ch48OosPortn.setStatus("current")


class _Pmopm2CfgCh49Ch64OosPortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh49Ch64OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh49Ch64OosPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh49Ch64OosPortn_Object = MibTableColumn
pmopm2CfgCh49Ch64OosPortn = _Pmopm2CfgCh49Ch64OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 8),
    _Pmopm2CfgCh49Ch64OosPortn_Type()
)
pmopm2CfgCh49Ch64OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh49Ch64OosPortn.setStatus("current")


class _Pmopm2CfgCh65Ch80OosPortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh65Ch80OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh65Ch80OosPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh65Ch80OosPortn_Object = MibTableColumn
pmopm2CfgCh65Ch80OosPortn = _Pmopm2CfgCh65Ch80OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 9),
    _Pmopm2CfgCh65Ch80OosPortn_Type()
)
pmopm2CfgCh65Ch80OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh65Ch80OosPortn.setStatus("current")


class _Pmopm2CfgCh81Ch96OosPortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh81Ch96OosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh81Ch96OosPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh81Ch96OosPortn_Object = MibTableColumn
pmopm2CfgCh81Ch96OosPortn = _Pmopm2CfgCh81Ch96OosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 2, 1, 10),
    _Pmopm2CfgCh81Ch96OosPortn_Type()
)
pmopm2CfgCh81Ch96OosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh81Ch96OosPortn.setStatus("current")
_Pmopm2CfgClientStartupBalanceTable_Object = MibTable
pmopm2CfgClientStartupBalanceTable = _Pmopm2CfgClientStartupBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupBalanceTable.setStatus("current")
_Pmopm2CfgClientStartupBalanceEntry_Object = MibTableRow
pmopm2CfgClientStartupBalanceEntry = _Pmopm2CfgClientStartupBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1)
)
pmopm2CfgClientStartupBalanceEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CfgClientStartupBalanceIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupBalanceEntry.setStatus("current")


class _Pmopm2CfgClientStartupBalanceIndex_Type(Integer32):
    """Custom type pmopm2CfgClientStartupBalanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CfgClientStartupBalanceIndex_Type.__name__ = "Integer32"
_Pmopm2CfgClientStartupBalanceIndex_Object = MibTableColumn
pmopm2CfgClientStartupBalanceIndex = _Pmopm2CfgClientStartupBalanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1, 1),
    _Pmopm2CfgClientStartupBalanceIndex_Type()
)
pmopm2CfgClientStartupBalanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupBalanceIndex.setStatus("current")


class _Pmopm2CfgCh1Ch16BalancePortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh1Ch16BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh1Ch16BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh1Ch16BalancePortn_Object = MibTableColumn
pmopm2CfgCh1Ch16BalancePortn = _Pmopm2CfgCh1Ch16BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1, 3),
    _Pmopm2CfgCh1Ch16BalancePortn_Type()
)
pmopm2CfgCh1Ch16BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh1Ch16BalancePortn.setStatus("current")


class _Pmopm2CfgCh17Ch32BalancePortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh17Ch32BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh17Ch32BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh17Ch32BalancePortn_Object = MibTableColumn
pmopm2CfgCh17Ch32BalancePortn = _Pmopm2CfgCh17Ch32BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1, 4),
    _Pmopm2CfgCh17Ch32BalancePortn_Type()
)
pmopm2CfgCh17Ch32BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh17Ch32BalancePortn.setStatus("current")


class _Pmopm2CfgCh33Ch48BalancePortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh33Ch48BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh33Ch48BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh33Ch48BalancePortn_Object = MibTableColumn
pmopm2CfgCh33Ch48BalancePortn = _Pmopm2CfgCh33Ch48BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1, 5),
    _Pmopm2CfgCh33Ch48BalancePortn_Type()
)
pmopm2CfgCh33Ch48BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh33Ch48BalancePortn.setStatus("current")


class _Pmopm2CfgCh49Ch64BalancePortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh49Ch64BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh49Ch64BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh49Ch64BalancePortn_Object = MibTableColumn
pmopm2CfgCh49Ch64BalancePortn = _Pmopm2CfgCh49Ch64BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1, 6),
    _Pmopm2CfgCh49Ch64BalancePortn_Type()
)
pmopm2CfgCh49Ch64BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh49Ch64BalancePortn.setStatus("current")


class _Pmopm2CfgCh65Ch80BalancePortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh65Ch80BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh65Ch80BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh65Ch80BalancePortn_Object = MibTableColumn
pmopm2CfgCh65Ch80BalancePortn = _Pmopm2CfgCh65Ch80BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1, 7),
    _Pmopm2CfgCh65Ch80BalancePortn_Type()
)
pmopm2CfgCh65Ch80BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh65Ch80BalancePortn.setStatus("current")


class _Pmopm2CfgCh81Ch96BalancePortn_Type(Unsigned32):
    """Custom type pmopm2CfgCh81Ch96BalancePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgCh81Ch96BalancePortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgCh81Ch96BalancePortn_Object = MibTableColumn
pmopm2CfgCh81Ch96BalancePortn = _Pmopm2CfgCh81Ch96BalancePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 3, 1, 8),
    _Pmopm2CfgCh81Ch96BalancePortn_Type()
)
pmopm2CfgCh81Ch96BalancePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgCh81Ch96BalancePortn.setStatus("current")
_Pmopm2CfgClientStartupAbsthreshTable_Object = MibTable
pmopm2CfgClientStartupAbsthreshTable = _Pmopm2CfgClientStartupAbsthreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4)
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupAbsthreshTable.setStatus("current")
_Pmopm2CfgClientStartupAbsthreshEntry_Object = MibTableRow
pmopm2CfgClientStartupAbsthreshEntry = _Pmopm2CfgClientStartupAbsthreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1)
)
pmopm2CfgClientStartupAbsthreshEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CfgClientStartupAbsthreshIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupAbsthreshEntry.setStatus("current")


class _Pmopm2CfgClientStartupAbsthreshIndex_Type(Integer32):
    """Custom type pmopm2CfgClientStartupAbsthreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CfgClientStartupAbsthreshIndex_Type.__name__ = "Integer32"
_Pmopm2CfgClientStartupAbsthreshIndex_Object = MibTableColumn
pmopm2CfgClientStartupAbsthreshIndex = _Pmopm2CfgClientStartupAbsthreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 1),
    _Pmopm2CfgClientStartupAbsthreshIndex_Type()
)
pmopm2CfgClientStartupAbsthreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupAbsthreshIndex.setStatus("current")


class _Pmopm2CfgChannel1AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel1AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel1AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel1AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel1AbsthreshPortn = _Pmopm2CfgChannel1AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 3),
    _Pmopm2CfgChannel1AbsthreshPortn_Type()
)
pmopm2CfgChannel1AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel1AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel2AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel2AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel2AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel2AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel2AbsthreshPortn = _Pmopm2CfgChannel2AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 4),
    _Pmopm2CfgChannel2AbsthreshPortn_Type()
)
pmopm2CfgChannel2AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel2AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel3AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel3AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel3AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel3AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel3AbsthreshPortn = _Pmopm2CfgChannel3AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 5),
    _Pmopm2CfgChannel3AbsthreshPortn_Type()
)
pmopm2CfgChannel3AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel3AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel4AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel4AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel4AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel4AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel4AbsthreshPortn = _Pmopm2CfgChannel4AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 6),
    _Pmopm2CfgChannel4AbsthreshPortn_Type()
)
pmopm2CfgChannel4AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel4AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel5AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel5AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel5AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel5AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel5AbsthreshPortn = _Pmopm2CfgChannel5AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 7),
    _Pmopm2CfgChannel5AbsthreshPortn_Type()
)
pmopm2CfgChannel5AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel5AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel6AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel6AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel6AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel6AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel6AbsthreshPortn = _Pmopm2CfgChannel6AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 8),
    _Pmopm2CfgChannel6AbsthreshPortn_Type()
)
pmopm2CfgChannel6AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel6AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel7AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel7AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel7AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel7AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel7AbsthreshPortn = _Pmopm2CfgChannel7AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 9),
    _Pmopm2CfgChannel7AbsthreshPortn_Type()
)
pmopm2CfgChannel7AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel7AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel8AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel8AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel8AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel8AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel8AbsthreshPortn = _Pmopm2CfgChannel8AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 10),
    _Pmopm2CfgChannel8AbsthreshPortn_Type()
)
pmopm2CfgChannel8AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel8AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel9AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel9AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel9AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel9AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel9AbsthreshPortn = _Pmopm2CfgChannel9AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 11),
    _Pmopm2CfgChannel9AbsthreshPortn_Type()
)
pmopm2CfgChannel9AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel9AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel10AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel10AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel10AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel10AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel10AbsthreshPortn = _Pmopm2CfgChannel10AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 12),
    _Pmopm2CfgChannel10AbsthreshPortn_Type()
)
pmopm2CfgChannel10AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel10AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel11AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel11AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel11AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel11AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel11AbsthreshPortn = _Pmopm2CfgChannel11AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 13),
    _Pmopm2CfgChannel11AbsthreshPortn_Type()
)
pmopm2CfgChannel11AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel11AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel12AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel12AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel12AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel12AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel12AbsthreshPortn = _Pmopm2CfgChannel12AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 14),
    _Pmopm2CfgChannel12AbsthreshPortn_Type()
)
pmopm2CfgChannel12AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel12AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel13AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel13AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel13AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel13AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel13AbsthreshPortn = _Pmopm2CfgChannel13AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 15),
    _Pmopm2CfgChannel13AbsthreshPortn_Type()
)
pmopm2CfgChannel13AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel13AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel14AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel14AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel14AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel14AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel14AbsthreshPortn = _Pmopm2CfgChannel14AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 16),
    _Pmopm2CfgChannel14AbsthreshPortn_Type()
)
pmopm2CfgChannel14AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel14AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel15AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel15AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel15AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel15AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel15AbsthreshPortn = _Pmopm2CfgChannel15AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 17),
    _Pmopm2CfgChannel15AbsthreshPortn_Type()
)
pmopm2CfgChannel15AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel15AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel16AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel16AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel16AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel16AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel16AbsthreshPortn = _Pmopm2CfgChannel16AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 18),
    _Pmopm2CfgChannel16AbsthreshPortn_Type()
)
pmopm2CfgChannel16AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel16AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel17AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel17AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel17AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel17AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel17AbsthreshPortn = _Pmopm2CfgChannel17AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 19),
    _Pmopm2CfgChannel17AbsthreshPortn_Type()
)
pmopm2CfgChannel17AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel17AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel18AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel18AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel18AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel18AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel18AbsthreshPortn = _Pmopm2CfgChannel18AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 20),
    _Pmopm2CfgChannel18AbsthreshPortn_Type()
)
pmopm2CfgChannel18AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel18AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel19AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel19AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel19AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel19AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel19AbsthreshPortn = _Pmopm2CfgChannel19AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 21),
    _Pmopm2CfgChannel19AbsthreshPortn_Type()
)
pmopm2CfgChannel19AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel19AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel20AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel20AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel20AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel20AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel20AbsthreshPortn = _Pmopm2CfgChannel20AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 22),
    _Pmopm2CfgChannel20AbsthreshPortn_Type()
)
pmopm2CfgChannel20AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel20AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel21AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel21AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel21AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel21AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel21AbsthreshPortn = _Pmopm2CfgChannel21AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 23),
    _Pmopm2CfgChannel21AbsthreshPortn_Type()
)
pmopm2CfgChannel21AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel21AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel22AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel22AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel22AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel22AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel22AbsthreshPortn = _Pmopm2CfgChannel22AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 24),
    _Pmopm2CfgChannel22AbsthreshPortn_Type()
)
pmopm2CfgChannel22AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel22AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel23AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel23AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel23AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel23AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel23AbsthreshPortn = _Pmopm2CfgChannel23AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 25),
    _Pmopm2CfgChannel23AbsthreshPortn_Type()
)
pmopm2CfgChannel23AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel23AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel24AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel24AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel24AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel24AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel24AbsthreshPortn = _Pmopm2CfgChannel24AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 26),
    _Pmopm2CfgChannel24AbsthreshPortn_Type()
)
pmopm2CfgChannel24AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel24AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel25AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel25AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel25AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel25AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel25AbsthreshPortn = _Pmopm2CfgChannel25AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 27),
    _Pmopm2CfgChannel25AbsthreshPortn_Type()
)
pmopm2CfgChannel25AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel25AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel26AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel26AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel26AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel26AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel26AbsthreshPortn = _Pmopm2CfgChannel26AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 28),
    _Pmopm2CfgChannel26AbsthreshPortn_Type()
)
pmopm2CfgChannel26AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel26AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel27AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel27AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel27AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel27AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel27AbsthreshPortn = _Pmopm2CfgChannel27AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 29),
    _Pmopm2CfgChannel27AbsthreshPortn_Type()
)
pmopm2CfgChannel27AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel27AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel28AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel28AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel28AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel28AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel28AbsthreshPortn = _Pmopm2CfgChannel28AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 30),
    _Pmopm2CfgChannel28AbsthreshPortn_Type()
)
pmopm2CfgChannel28AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel28AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel29AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel29AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel29AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel29AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel29AbsthreshPortn = _Pmopm2CfgChannel29AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 31),
    _Pmopm2CfgChannel29AbsthreshPortn_Type()
)
pmopm2CfgChannel29AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel29AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel30AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel30AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel30AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel30AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel30AbsthreshPortn = _Pmopm2CfgChannel30AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 32),
    _Pmopm2CfgChannel30AbsthreshPortn_Type()
)
pmopm2CfgChannel30AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel30AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel31AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel31AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel31AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel31AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel31AbsthreshPortn = _Pmopm2CfgChannel31AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 33),
    _Pmopm2CfgChannel31AbsthreshPortn_Type()
)
pmopm2CfgChannel31AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel31AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel32AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel32AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel32AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel32AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel32AbsthreshPortn = _Pmopm2CfgChannel32AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 34),
    _Pmopm2CfgChannel32AbsthreshPortn_Type()
)
pmopm2CfgChannel32AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel32AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel33AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel33AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel33AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel33AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel33AbsthreshPortn = _Pmopm2CfgChannel33AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 35),
    _Pmopm2CfgChannel33AbsthreshPortn_Type()
)
pmopm2CfgChannel33AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel33AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel34AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel34AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel34AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel34AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel34AbsthreshPortn = _Pmopm2CfgChannel34AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 36),
    _Pmopm2CfgChannel34AbsthreshPortn_Type()
)
pmopm2CfgChannel34AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel34AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel35AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel35AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel35AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel35AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel35AbsthreshPortn = _Pmopm2CfgChannel35AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 37),
    _Pmopm2CfgChannel35AbsthreshPortn_Type()
)
pmopm2CfgChannel35AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel35AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel36AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel36AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel36AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel36AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel36AbsthreshPortn = _Pmopm2CfgChannel36AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 38),
    _Pmopm2CfgChannel36AbsthreshPortn_Type()
)
pmopm2CfgChannel36AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel36AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel37AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel37AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel37AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel37AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel37AbsthreshPortn = _Pmopm2CfgChannel37AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 39),
    _Pmopm2CfgChannel37AbsthreshPortn_Type()
)
pmopm2CfgChannel37AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel37AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel38AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel38AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel38AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel38AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel38AbsthreshPortn = _Pmopm2CfgChannel38AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 40),
    _Pmopm2CfgChannel38AbsthreshPortn_Type()
)
pmopm2CfgChannel38AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel38AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel39AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel39AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel39AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel39AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel39AbsthreshPortn = _Pmopm2CfgChannel39AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 41),
    _Pmopm2CfgChannel39AbsthreshPortn_Type()
)
pmopm2CfgChannel39AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel39AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel40AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel40AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel40AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel40AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel40AbsthreshPortn = _Pmopm2CfgChannel40AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 42),
    _Pmopm2CfgChannel40AbsthreshPortn_Type()
)
pmopm2CfgChannel40AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel40AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel41AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel41AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel41AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel41AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel41AbsthreshPortn = _Pmopm2CfgChannel41AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 43),
    _Pmopm2CfgChannel41AbsthreshPortn_Type()
)
pmopm2CfgChannel41AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel41AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel42AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel42AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel42AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel42AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel42AbsthreshPortn = _Pmopm2CfgChannel42AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 44),
    _Pmopm2CfgChannel42AbsthreshPortn_Type()
)
pmopm2CfgChannel42AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel42AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel43AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel43AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel43AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel43AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel43AbsthreshPortn = _Pmopm2CfgChannel43AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 45),
    _Pmopm2CfgChannel43AbsthreshPortn_Type()
)
pmopm2CfgChannel43AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel43AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel44AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel44AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel44AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel44AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel44AbsthreshPortn = _Pmopm2CfgChannel44AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 46),
    _Pmopm2CfgChannel44AbsthreshPortn_Type()
)
pmopm2CfgChannel44AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel44AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel45AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel45AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel45AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel45AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel45AbsthreshPortn = _Pmopm2CfgChannel45AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 47),
    _Pmopm2CfgChannel45AbsthreshPortn_Type()
)
pmopm2CfgChannel45AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel45AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel46AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel46AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel46AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel46AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel46AbsthreshPortn = _Pmopm2CfgChannel46AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 48),
    _Pmopm2CfgChannel46AbsthreshPortn_Type()
)
pmopm2CfgChannel46AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel46AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel47AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel47AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel47AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel47AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel47AbsthreshPortn = _Pmopm2CfgChannel47AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 49),
    _Pmopm2CfgChannel47AbsthreshPortn_Type()
)
pmopm2CfgChannel47AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel47AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel48AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel48AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel48AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel48AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel48AbsthreshPortn = _Pmopm2CfgChannel48AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 50),
    _Pmopm2CfgChannel48AbsthreshPortn_Type()
)
pmopm2CfgChannel48AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel48AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel49AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel49AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel49AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel49AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel49AbsthreshPortn = _Pmopm2CfgChannel49AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 51),
    _Pmopm2CfgChannel49AbsthreshPortn_Type()
)
pmopm2CfgChannel49AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel49AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel50AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel50AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel50AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel50AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel50AbsthreshPortn = _Pmopm2CfgChannel50AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 52),
    _Pmopm2CfgChannel50AbsthreshPortn_Type()
)
pmopm2CfgChannel50AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel50AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel51AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel51AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel51AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel51AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel51AbsthreshPortn = _Pmopm2CfgChannel51AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 53),
    _Pmopm2CfgChannel51AbsthreshPortn_Type()
)
pmopm2CfgChannel51AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel51AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel52AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel52AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel52AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel52AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel52AbsthreshPortn = _Pmopm2CfgChannel52AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 54),
    _Pmopm2CfgChannel52AbsthreshPortn_Type()
)
pmopm2CfgChannel52AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel52AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel53AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel53AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel53AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel53AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel53AbsthreshPortn = _Pmopm2CfgChannel53AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 55),
    _Pmopm2CfgChannel53AbsthreshPortn_Type()
)
pmopm2CfgChannel53AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel53AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel54AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel54AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel54AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel54AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel54AbsthreshPortn = _Pmopm2CfgChannel54AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 56),
    _Pmopm2CfgChannel54AbsthreshPortn_Type()
)
pmopm2CfgChannel54AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel54AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel55AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel55AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel55AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel55AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel55AbsthreshPortn = _Pmopm2CfgChannel55AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 57),
    _Pmopm2CfgChannel55AbsthreshPortn_Type()
)
pmopm2CfgChannel55AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel55AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel56AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel56AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel56AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel56AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel56AbsthreshPortn = _Pmopm2CfgChannel56AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 58),
    _Pmopm2CfgChannel56AbsthreshPortn_Type()
)
pmopm2CfgChannel56AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel56AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel57AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel57AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel57AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel57AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel57AbsthreshPortn = _Pmopm2CfgChannel57AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 59),
    _Pmopm2CfgChannel57AbsthreshPortn_Type()
)
pmopm2CfgChannel57AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel57AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel58AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel58AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel58AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel58AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel58AbsthreshPortn = _Pmopm2CfgChannel58AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 60),
    _Pmopm2CfgChannel58AbsthreshPortn_Type()
)
pmopm2CfgChannel58AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel58AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel59AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel59AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel59AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel59AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel59AbsthreshPortn = _Pmopm2CfgChannel59AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 61),
    _Pmopm2CfgChannel59AbsthreshPortn_Type()
)
pmopm2CfgChannel59AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel59AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel60AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel60AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel60AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel60AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel60AbsthreshPortn = _Pmopm2CfgChannel60AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 62),
    _Pmopm2CfgChannel60AbsthreshPortn_Type()
)
pmopm2CfgChannel60AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel60AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel61AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel61AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel61AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel61AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel61AbsthreshPortn = _Pmopm2CfgChannel61AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 63),
    _Pmopm2CfgChannel61AbsthreshPortn_Type()
)
pmopm2CfgChannel61AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel61AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel62AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel62AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel62AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel62AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel62AbsthreshPortn = _Pmopm2CfgChannel62AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 64),
    _Pmopm2CfgChannel62AbsthreshPortn_Type()
)
pmopm2CfgChannel62AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel62AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel63AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel63AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel63AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel63AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel63AbsthreshPortn = _Pmopm2CfgChannel63AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 65),
    _Pmopm2CfgChannel63AbsthreshPortn_Type()
)
pmopm2CfgChannel63AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel63AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel64AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel64AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel64AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel64AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel64AbsthreshPortn = _Pmopm2CfgChannel64AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 66),
    _Pmopm2CfgChannel64AbsthreshPortn_Type()
)
pmopm2CfgChannel64AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel64AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel65AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel65AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel65AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel65AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel65AbsthreshPortn = _Pmopm2CfgChannel65AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 67),
    _Pmopm2CfgChannel65AbsthreshPortn_Type()
)
pmopm2CfgChannel65AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel65AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel66AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel66AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel66AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel66AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel66AbsthreshPortn = _Pmopm2CfgChannel66AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 68),
    _Pmopm2CfgChannel66AbsthreshPortn_Type()
)
pmopm2CfgChannel66AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel66AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel67AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel67AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel67AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel67AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel67AbsthreshPortn = _Pmopm2CfgChannel67AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 69),
    _Pmopm2CfgChannel67AbsthreshPortn_Type()
)
pmopm2CfgChannel67AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel67AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel68AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel68AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel68AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel68AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel68AbsthreshPortn = _Pmopm2CfgChannel68AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 70),
    _Pmopm2CfgChannel68AbsthreshPortn_Type()
)
pmopm2CfgChannel68AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel68AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel69AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel69AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel69AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel69AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel69AbsthreshPortn = _Pmopm2CfgChannel69AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 71),
    _Pmopm2CfgChannel69AbsthreshPortn_Type()
)
pmopm2CfgChannel69AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel69AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel70AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel70AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel70AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel70AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel70AbsthreshPortn = _Pmopm2CfgChannel70AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 72),
    _Pmopm2CfgChannel70AbsthreshPortn_Type()
)
pmopm2CfgChannel70AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel70AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel71AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel71AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel71AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel71AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel71AbsthreshPortn = _Pmopm2CfgChannel71AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 73),
    _Pmopm2CfgChannel71AbsthreshPortn_Type()
)
pmopm2CfgChannel71AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel71AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel72AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel72AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel72AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel72AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel72AbsthreshPortn = _Pmopm2CfgChannel72AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 74),
    _Pmopm2CfgChannel72AbsthreshPortn_Type()
)
pmopm2CfgChannel72AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel72AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel73AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel73AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel73AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel73AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel73AbsthreshPortn = _Pmopm2CfgChannel73AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 75),
    _Pmopm2CfgChannel73AbsthreshPortn_Type()
)
pmopm2CfgChannel73AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel73AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel74AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel74AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel74AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel74AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel74AbsthreshPortn = _Pmopm2CfgChannel74AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 76),
    _Pmopm2CfgChannel74AbsthreshPortn_Type()
)
pmopm2CfgChannel74AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel74AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel75AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel75AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel75AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel75AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel75AbsthreshPortn = _Pmopm2CfgChannel75AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 77),
    _Pmopm2CfgChannel75AbsthreshPortn_Type()
)
pmopm2CfgChannel75AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel75AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel76AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel76AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel76AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel76AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel76AbsthreshPortn = _Pmopm2CfgChannel76AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 78),
    _Pmopm2CfgChannel76AbsthreshPortn_Type()
)
pmopm2CfgChannel76AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel76AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel77AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel77AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel77AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel77AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel77AbsthreshPortn = _Pmopm2CfgChannel77AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 79),
    _Pmopm2CfgChannel77AbsthreshPortn_Type()
)
pmopm2CfgChannel77AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel77AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel78AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel78AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel78AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel78AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel78AbsthreshPortn = _Pmopm2CfgChannel78AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 80),
    _Pmopm2CfgChannel78AbsthreshPortn_Type()
)
pmopm2CfgChannel78AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel78AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel79AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel79AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel79AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel79AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel79AbsthreshPortn = _Pmopm2CfgChannel79AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 81),
    _Pmopm2CfgChannel79AbsthreshPortn_Type()
)
pmopm2CfgChannel79AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel79AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel80AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel80AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel80AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel80AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel80AbsthreshPortn = _Pmopm2CfgChannel80AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 82),
    _Pmopm2CfgChannel80AbsthreshPortn_Type()
)
pmopm2CfgChannel80AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel80AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel81AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel81AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel81AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel81AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel81AbsthreshPortn = _Pmopm2CfgChannel81AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 83),
    _Pmopm2CfgChannel81AbsthreshPortn_Type()
)
pmopm2CfgChannel81AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel81AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel82AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel82AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel82AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel82AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel82AbsthreshPortn = _Pmopm2CfgChannel82AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 84),
    _Pmopm2CfgChannel82AbsthreshPortn_Type()
)
pmopm2CfgChannel82AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel82AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel83AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel83AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel83AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel83AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel83AbsthreshPortn = _Pmopm2CfgChannel83AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 85),
    _Pmopm2CfgChannel83AbsthreshPortn_Type()
)
pmopm2CfgChannel83AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel83AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel84AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel84AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel84AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel84AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel84AbsthreshPortn = _Pmopm2CfgChannel84AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 86),
    _Pmopm2CfgChannel84AbsthreshPortn_Type()
)
pmopm2CfgChannel84AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel84AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel85AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel85AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel85AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel85AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel85AbsthreshPortn = _Pmopm2CfgChannel85AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 87),
    _Pmopm2CfgChannel85AbsthreshPortn_Type()
)
pmopm2CfgChannel85AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel85AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel86AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel86AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel86AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel86AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel86AbsthreshPortn = _Pmopm2CfgChannel86AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 88),
    _Pmopm2CfgChannel86AbsthreshPortn_Type()
)
pmopm2CfgChannel86AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel86AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel87AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel87AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel87AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel87AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel87AbsthreshPortn = _Pmopm2CfgChannel87AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 89),
    _Pmopm2CfgChannel87AbsthreshPortn_Type()
)
pmopm2CfgChannel87AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel87AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel88AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel88AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel88AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel88AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel88AbsthreshPortn = _Pmopm2CfgChannel88AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 90),
    _Pmopm2CfgChannel88AbsthreshPortn_Type()
)
pmopm2CfgChannel88AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel88AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel89AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel89AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel89AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel89AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel89AbsthreshPortn = _Pmopm2CfgChannel89AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 91),
    _Pmopm2CfgChannel89AbsthreshPortn_Type()
)
pmopm2CfgChannel89AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel89AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel90AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel90AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel90AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel90AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel90AbsthreshPortn = _Pmopm2CfgChannel90AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 92),
    _Pmopm2CfgChannel90AbsthreshPortn_Type()
)
pmopm2CfgChannel90AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel90AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel91AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel91AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel91AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel91AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel91AbsthreshPortn = _Pmopm2CfgChannel91AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 93),
    _Pmopm2CfgChannel91AbsthreshPortn_Type()
)
pmopm2CfgChannel91AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel91AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel92AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel92AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel92AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel92AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel92AbsthreshPortn = _Pmopm2CfgChannel92AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 94),
    _Pmopm2CfgChannel92AbsthreshPortn_Type()
)
pmopm2CfgChannel92AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel92AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel93AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel93AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel93AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel93AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel93AbsthreshPortn = _Pmopm2CfgChannel93AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 95),
    _Pmopm2CfgChannel93AbsthreshPortn_Type()
)
pmopm2CfgChannel93AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel93AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel94AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel94AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel94AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel94AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel94AbsthreshPortn = _Pmopm2CfgChannel94AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 96),
    _Pmopm2CfgChannel94AbsthreshPortn_Type()
)
pmopm2CfgChannel94AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel94AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel95AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel95AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel95AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel95AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel95AbsthreshPortn = _Pmopm2CfgChannel95AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 97),
    _Pmopm2CfgChannel95AbsthreshPortn_Type()
)
pmopm2CfgChannel95AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel95AbsthreshPortn.setStatus("current")


class _Pmopm2CfgChannel96AbsthreshPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel96AbsthreshPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel96AbsthreshPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel96AbsthreshPortn_Object = MibTableColumn
pmopm2CfgChannel96AbsthreshPortn = _Pmopm2CfgChannel96AbsthreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 4, 1, 98),
    _Pmopm2CfgChannel96AbsthreshPortn_Type()
)
pmopm2CfgChannel96AbsthreshPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel96AbsthreshPortn.setStatus("current")
_Pmopm2CfgClientStartupPwrHighTable_Object = MibTable
pmopm2CfgClientStartupPwrHighTable = _Pmopm2CfgClientStartupPwrHighTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5)
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupPwrHighTable.setStatus("current")
_Pmopm2CfgClientStartupPwrHighEntry_Object = MibTableRow
pmopm2CfgClientStartupPwrHighEntry = _Pmopm2CfgClientStartupPwrHighEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1)
)
pmopm2CfgClientStartupPwrHighEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CfgClientStartupPwrHighIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupPwrHighEntry.setStatus("current")


class _Pmopm2CfgClientStartupPwrHighIndex_Type(Integer32):
    """Custom type pmopm2CfgClientStartupPwrHighIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CfgClientStartupPwrHighIndex_Type.__name__ = "Integer32"
_Pmopm2CfgClientStartupPwrHighIndex_Object = MibTableColumn
pmopm2CfgClientStartupPwrHighIndex = _Pmopm2CfgClientStartupPwrHighIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 1),
    _Pmopm2CfgClientStartupPwrHighIndex_Type()
)
pmopm2CfgClientStartupPwrHighIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupPwrHighIndex.setStatus("current")


class _Pmopm2CfgChannel1PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel1PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel1PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel1PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel1PwrhighPortn = _Pmopm2CfgChannel1PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 3),
    _Pmopm2CfgChannel1PwrhighPortn_Type()
)
pmopm2CfgChannel1PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel1PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel2PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel2PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel2PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel2PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel2PwrhighPortn = _Pmopm2CfgChannel2PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 4),
    _Pmopm2CfgChannel2PwrhighPortn_Type()
)
pmopm2CfgChannel2PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel2PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel3PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel3PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel3PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel3PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel3PwrhighPortn = _Pmopm2CfgChannel3PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 5),
    _Pmopm2CfgChannel3PwrhighPortn_Type()
)
pmopm2CfgChannel3PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel3PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel4PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel4PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel4PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel4PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel4PwrhighPortn = _Pmopm2CfgChannel4PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 6),
    _Pmopm2CfgChannel4PwrhighPortn_Type()
)
pmopm2CfgChannel4PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel4PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel5PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel5PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel5PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel5PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel5PwrhighPortn = _Pmopm2CfgChannel5PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 7),
    _Pmopm2CfgChannel5PwrhighPortn_Type()
)
pmopm2CfgChannel5PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel5PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel6PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel6PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel6PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel6PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel6PwrhighPortn = _Pmopm2CfgChannel6PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 8),
    _Pmopm2CfgChannel6PwrhighPortn_Type()
)
pmopm2CfgChannel6PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel6PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel7PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel7PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel7PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel7PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel7PwrhighPortn = _Pmopm2CfgChannel7PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 9),
    _Pmopm2CfgChannel7PwrhighPortn_Type()
)
pmopm2CfgChannel7PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel7PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel8PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel8PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel8PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel8PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel8PwrhighPortn = _Pmopm2CfgChannel8PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 10),
    _Pmopm2CfgChannel8PwrhighPortn_Type()
)
pmopm2CfgChannel8PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel8PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel9PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel9PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel9PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel9PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel9PwrhighPortn = _Pmopm2CfgChannel9PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 11),
    _Pmopm2CfgChannel9PwrhighPortn_Type()
)
pmopm2CfgChannel9PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel9PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel10PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel10PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel10PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel10PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel10PwrhighPortn = _Pmopm2CfgChannel10PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 12),
    _Pmopm2CfgChannel10PwrhighPortn_Type()
)
pmopm2CfgChannel10PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel10PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel11PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel11PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel11PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel11PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel11PwrhighPortn = _Pmopm2CfgChannel11PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 13),
    _Pmopm2CfgChannel11PwrhighPortn_Type()
)
pmopm2CfgChannel11PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel11PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel12PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel12PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel12PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel12PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel12PwrhighPortn = _Pmopm2CfgChannel12PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 14),
    _Pmopm2CfgChannel12PwrhighPortn_Type()
)
pmopm2CfgChannel12PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel12PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel13PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel13PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel13PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel13PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel13PwrhighPortn = _Pmopm2CfgChannel13PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 15),
    _Pmopm2CfgChannel13PwrhighPortn_Type()
)
pmopm2CfgChannel13PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel13PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel14PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel14PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel14PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel14PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel14PwrhighPortn = _Pmopm2CfgChannel14PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 16),
    _Pmopm2CfgChannel14PwrhighPortn_Type()
)
pmopm2CfgChannel14PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel14PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel15PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel15PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel15PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel15PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel15PwrhighPortn = _Pmopm2CfgChannel15PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 17),
    _Pmopm2CfgChannel15PwrhighPortn_Type()
)
pmopm2CfgChannel15PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel15PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel16PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel16PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel16PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel16PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel16PwrhighPortn = _Pmopm2CfgChannel16PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 18),
    _Pmopm2CfgChannel16PwrhighPortn_Type()
)
pmopm2CfgChannel16PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel16PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel17PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel17PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel17PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel17PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel17PwrhighPortn = _Pmopm2CfgChannel17PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 19),
    _Pmopm2CfgChannel17PwrhighPortn_Type()
)
pmopm2CfgChannel17PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel17PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel18PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel18PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel18PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel18PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel18PwrhighPortn = _Pmopm2CfgChannel18PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 20),
    _Pmopm2CfgChannel18PwrhighPortn_Type()
)
pmopm2CfgChannel18PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel18PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel19PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel19PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel19PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel19PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel19PwrhighPortn = _Pmopm2CfgChannel19PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 21),
    _Pmopm2CfgChannel19PwrhighPortn_Type()
)
pmopm2CfgChannel19PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel19PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel20PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel20PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel20PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel20PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel20PwrhighPortn = _Pmopm2CfgChannel20PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 22),
    _Pmopm2CfgChannel20PwrhighPortn_Type()
)
pmopm2CfgChannel20PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel20PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel21PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel21PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel21PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel21PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel21PwrhighPortn = _Pmopm2CfgChannel21PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 23),
    _Pmopm2CfgChannel21PwrhighPortn_Type()
)
pmopm2CfgChannel21PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel21PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel22PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel22PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel22PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel22PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel22PwrhighPortn = _Pmopm2CfgChannel22PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 24),
    _Pmopm2CfgChannel22PwrhighPortn_Type()
)
pmopm2CfgChannel22PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel22PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel23PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel23PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel23PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel23PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel23PwrhighPortn = _Pmopm2CfgChannel23PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 25),
    _Pmopm2CfgChannel23PwrhighPortn_Type()
)
pmopm2CfgChannel23PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel23PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel24PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel24PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel24PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel24PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel24PwrhighPortn = _Pmopm2CfgChannel24PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 26),
    _Pmopm2CfgChannel24PwrhighPortn_Type()
)
pmopm2CfgChannel24PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel24PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel25PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel25PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel25PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel25PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel25PwrhighPortn = _Pmopm2CfgChannel25PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 27),
    _Pmopm2CfgChannel25PwrhighPortn_Type()
)
pmopm2CfgChannel25PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel25PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel26PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel26PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel26PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel26PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel26PwrhighPortn = _Pmopm2CfgChannel26PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 28),
    _Pmopm2CfgChannel26PwrhighPortn_Type()
)
pmopm2CfgChannel26PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel26PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel27PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel27PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel27PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel27PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel27PwrhighPortn = _Pmopm2CfgChannel27PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 29),
    _Pmopm2CfgChannel27PwrhighPortn_Type()
)
pmopm2CfgChannel27PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel27PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel28PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel28PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel28PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel28PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel28PwrhighPortn = _Pmopm2CfgChannel28PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 30),
    _Pmopm2CfgChannel28PwrhighPortn_Type()
)
pmopm2CfgChannel28PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel28PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel29PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel29PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel29PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel29PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel29PwrhighPortn = _Pmopm2CfgChannel29PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 31),
    _Pmopm2CfgChannel29PwrhighPortn_Type()
)
pmopm2CfgChannel29PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel29PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel30PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel30PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel30PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel30PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel30PwrhighPortn = _Pmopm2CfgChannel30PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 32),
    _Pmopm2CfgChannel30PwrhighPortn_Type()
)
pmopm2CfgChannel30PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel30PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel31PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel31PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel31PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel31PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel31PwrhighPortn = _Pmopm2CfgChannel31PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 33),
    _Pmopm2CfgChannel31PwrhighPortn_Type()
)
pmopm2CfgChannel31PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel31PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel32PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel32PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel32PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel32PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel32PwrhighPortn = _Pmopm2CfgChannel32PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 34),
    _Pmopm2CfgChannel32PwrhighPortn_Type()
)
pmopm2CfgChannel32PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel32PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel33PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel33PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel33PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel33PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel33PwrhighPortn = _Pmopm2CfgChannel33PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 35),
    _Pmopm2CfgChannel33PwrhighPortn_Type()
)
pmopm2CfgChannel33PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel33PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel34PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel34PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel34PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel34PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel34PwrhighPortn = _Pmopm2CfgChannel34PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 36),
    _Pmopm2CfgChannel34PwrhighPortn_Type()
)
pmopm2CfgChannel34PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel34PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel35PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel35PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel35PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel35PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel35PwrhighPortn = _Pmopm2CfgChannel35PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 37),
    _Pmopm2CfgChannel35PwrhighPortn_Type()
)
pmopm2CfgChannel35PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel35PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel36PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel36PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel36PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel36PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel36PwrhighPortn = _Pmopm2CfgChannel36PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 38),
    _Pmopm2CfgChannel36PwrhighPortn_Type()
)
pmopm2CfgChannel36PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel36PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel37PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel37PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel37PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel37PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel37PwrhighPortn = _Pmopm2CfgChannel37PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 39),
    _Pmopm2CfgChannel37PwrhighPortn_Type()
)
pmopm2CfgChannel37PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel37PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel38PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel38PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel38PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel38PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel38PwrhighPortn = _Pmopm2CfgChannel38PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 40),
    _Pmopm2CfgChannel38PwrhighPortn_Type()
)
pmopm2CfgChannel38PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel38PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel39PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel39PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel39PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel39PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel39PwrhighPortn = _Pmopm2CfgChannel39PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 41),
    _Pmopm2CfgChannel39PwrhighPortn_Type()
)
pmopm2CfgChannel39PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel39PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel40PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel40PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel40PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel40PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel40PwrhighPortn = _Pmopm2CfgChannel40PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 42),
    _Pmopm2CfgChannel40PwrhighPortn_Type()
)
pmopm2CfgChannel40PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel40PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel41PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel41PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel41PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel41PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel41PwrhighPortn = _Pmopm2CfgChannel41PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 43),
    _Pmopm2CfgChannel41PwrhighPortn_Type()
)
pmopm2CfgChannel41PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel41PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel42PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel42PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel42PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel42PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel42PwrhighPortn = _Pmopm2CfgChannel42PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 44),
    _Pmopm2CfgChannel42PwrhighPortn_Type()
)
pmopm2CfgChannel42PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel42PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel43PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel43PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel43PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel43PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel43PwrhighPortn = _Pmopm2CfgChannel43PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 45),
    _Pmopm2CfgChannel43PwrhighPortn_Type()
)
pmopm2CfgChannel43PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel43PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel44PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel44PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel44PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel44PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel44PwrhighPortn = _Pmopm2CfgChannel44PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 46),
    _Pmopm2CfgChannel44PwrhighPortn_Type()
)
pmopm2CfgChannel44PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel44PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel45PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel45PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel45PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel45PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel45PwrhighPortn = _Pmopm2CfgChannel45PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 47),
    _Pmopm2CfgChannel45PwrhighPortn_Type()
)
pmopm2CfgChannel45PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel45PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel46PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel46PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel46PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel46PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel46PwrhighPortn = _Pmopm2CfgChannel46PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 48),
    _Pmopm2CfgChannel46PwrhighPortn_Type()
)
pmopm2CfgChannel46PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel46PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel47PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel47PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel47PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel47PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel47PwrhighPortn = _Pmopm2CfgChannel47PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 49),
    _Pmopm2CfgChannel47PwrhighPortn_Type()
)
pmopm2CfgChannel47PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel47PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel48PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel48PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel48PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel48PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel48PwrhighPortn = _Pmopm2CfgChannel48PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 50),
    _Pmopm2CfgChannel48PwrhighPortn_Type()
)
pmopm2CfgChannel48PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel48PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel49PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel49PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel49PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel49PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel49PwrhighPortn = _Pmopm2CfgChannel49PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 51),
    _Pmopm2CfgChannel49PwrhighPortn_Type()
)
pmopm2CfgChannel49PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel49PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel50PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel50PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel50PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel50PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel50PwrhighPortn = _Pmopm2CfgChannel50PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 52),
    _Pmopm2CfgChannel50PwrhighPortn_Type()
)
pmopm2CfgChannel50PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel50PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel51PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel51PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel51PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel51PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel51PwrhighPortn = _Pmopm2CfgChannel51PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 53),
    _Pmopm2CfgChannel51PwrhighPortn_Type()
)
pmopm2CfgChannel51PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel51PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel52PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel52PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel52PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel52PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel52PwrhighPortn = _Pmopm2CfgChannel52PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 54),
    _Pmopm2CfgChannel52PwrhighPortn_Type()
)
pmopm2CfgChannel52PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel52PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel53PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel53PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel53PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel53PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel53PwrhighPortn = _Pmopm2CfgChannel53PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 55),
    _Pmopm2CfgChannel53PwrhighPortn_Type()
)
pmopm2CfgChannel53PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel53PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel54PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel54PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel54PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel54PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel54PwrhighPortn = _Pmopm2CfgChannel54PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 56),
    _Pmopm2CfgChannel54PwrhighPortn_Type()
)
pmopm2CfgChannel54PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel54PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel55PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel55PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel55PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel55PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel55PwrhighPortn = _Pmopm2CfgChannel55PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 57),
    _Pmopm2CfgChannel55PwrhighPortn_Type()
)
pmopm2CfgChannel55PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel55PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel56PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel56PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel56PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel56PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel56PwrhighPortn = _Pmopm2CfgChannel56PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 58),
    _Pmopm2CfgChannel56PwrhighPortn_Type()
)
pmopm2CfgChannel56PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel56PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel57PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel57PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel57PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel57PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel57PwrhighPortn = _Pmopm2CfgChannel57PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 59),
    _Pmopm2CfgChannel57PwrhighPortn_Type()
)
pmopm2CfgChannel57PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel57PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel58PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel58PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel58PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel58PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel58PwrhighPortn = _Pmopm2CfgChannel58PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 60),
    _Pmopm2CfgChannel58PwrhighPortn_Type()
)
pmopm2CfgChannel58PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel58PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel59PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel59PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel59PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel59PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel59PwrhighPortn = _Pmopm2CfgChannel59PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 61),
    _Pmopm2CfgChannel59PwrhighPortn_Type()
)
pmopm2CfgChannel59PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel59PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel60PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel60PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel60PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel60PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel60PwrhighPortn = _Pmopm2CfgChannel60PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 62),
    _Pmopm2CfgChannel60PwrhighPortn_Type()
)
pmopm2CfgChannel60PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel60PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel61PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel61PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel61PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel61PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel61PwrhighPortn = _Pmopm2CfgChannel61PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 63),
    _Pmopm2CfgChannel61PwrhighPortn_Type()
)
pmopm2CfgChannel61PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel61PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel62PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel62PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel62PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel62PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel62PwrhighPortn = _Pmopm2CfgChannel62PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 64),
    _Pmopm2CfgChannel62PwrhighPortn_Type()
)
pmopm2CfgChannel62PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel62PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel63PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel63PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel63PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel63PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel63PwrhighPortn = _Pmopm2CfgChannel63PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 65),
    _Pmopm2CfgChannel63PwrhighPortn_Type()
)
pmopm2CfgChannel63PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel63PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel64PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel64PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel64PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel64PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel64PwrhighPortn = _Pmopm2CfgChannel64PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 66),
    _Pmopm2CfgChannel64PwrhighPortn_Type()
)
pmopm2CfgChannel64PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel64PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel65PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel65PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel65PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel65PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel65PwrhighPortn = _Pmopm2CfgChannel65PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 67),
    _Pmopm2CfgChannel65PwrhighPortn_Type()
)
pmopm2CfgChannel65PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel65PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel66PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel66PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel66PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel66PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel66PwrhighPortn = _Pmopm2CfgChannel66PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 68),
    _Pmopm2CfgChannel66PwrhighPortn_Type()
)
pmopm2CfgChannel66PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel66PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel67PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel67PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel67PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel67PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel67PwrhighPortn = _Pmopm2CfgChannel67PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 69),
    _Pmopm2CfgChannel67PwrhighPortn_Type()
)
pmopm2CfgChannel67PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel67PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel68PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel68PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel68PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel68PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel68PwrhighPortn = _Pmopm2CfgChannel68PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 70),
    _Pmopm2CfgChannel68PwrhighPortn_Type()
)
pmopm2CfgChannel68PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel68PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel69PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel69PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel69PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel69PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel69PwrhighPortn = _Pmopm2CfgChannel69PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 71),
    _Pmopm2CfgChannel69PwrhighPortn_Type()
)
pmopm2CfgChannel69PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel69PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel70PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel70PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel70PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel70PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel70PwrhighPortn = _Pmopm2CfgChannel70PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 72),
    _Pmopm2CfgChannel70PwrhighPortn_Type()
)
pmopm2CfgChannel70PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel70PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel71PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel71PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel71PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel71PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel71PwrhighPortn = _Pmopm2CfgChannel71PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 73),
    _Pmopm2CfgChannel71PwrhighPortn_Type()
)
pmopm2CfgChannel71PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel71PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel72PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel72PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel72PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel72PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel72PwrhighPortn = _Pmopm2CfgChannel72PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 74),
    _Pmopm2CfgChannel72PwrhighPortn_Type()
)
pmopm2CfgChannel72PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel72PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel73PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel73PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel73PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel73PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel73PwrhighPortn = _Pmopm2CfgChannel73PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 75),
    _Pmopm2CfgChannel73PwrhighPortn_Type()
)
pmopm2CfgChannel73PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel73PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel74PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel74PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel74PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel74PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel74PwrhighPortn = _Pmopm2CfgChannel74PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 76),
    _Pmopm2CfgChannel74PwrhighPortn_Type()
)
pmopm2CfgChannel74PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel74PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel75PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel75PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel75PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel75PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel75PwrhighPortn = _Pmopm2CfgChannel75PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 77),
    _Pmopm2CfgChannel75PwrhighPortn_Type()
)
pmopm2CfgChannel75PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel75PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel76PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel76PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel76PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel76PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel76PwrhighPortn = _Pmopm2CfgChannel76PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 78),
    _Pmopm2CfgChannel76PwrhighPortn_Type()
)
pmopm2CfgChannel76PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel76PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel77PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel77PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel77PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel77PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel77PwrhighPortn = _Pmopm2CfgChannel77PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 79),
    _Pmopm2CfgChannel77PwrhighPortn_Type()
)
pmopm2CfgChannel77PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel77PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel78PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel78PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel78PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel78PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel78PwrhighPortn = _Pmopm2CfgChannel78PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 80),
    _Pmopm2CfgChannel78PwrhighPortn_Type()
)
pmopm2CfgChannel78PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel78PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel79PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel79PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel79PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel79PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel79PwrhighPortn = _Pmopm2CfgChannel79PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 81),
    _Pmopm2CfgChannel79PwrhighPortn_Type()
)
pmopm2CfgChannel79PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel79PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel80PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel80PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel80PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel80PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel80PwrhighPortn = _Pmopm2CfgChannel80PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 82),
    _Pmopm2CfgChannel80PwrhighPortn_Type()
)
pmopm2CfgChannel80PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel80PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel81PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel81PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel81PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel81PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel81PwrhighPortn = _Pmopm2CfgChannel81PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 83),
    _Pmopm2CfgChannel81PwrhighPortn_Type()
)
pmopm2CfgChannel81PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel81PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel82PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel82PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel82PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel82PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel82PwrhighPortn = _Pmopm2CfgChannel82PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 84),
    _Pmopm2CfgChannel82PwrhighPortn_Type()
)
pmopm2CfgChannel82PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel82PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel83PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel83PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel83PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel83PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel83PwrhighPortn = _Pmopm2CfgChannel83PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 85),
    _Pmopm2CfgChannel83PwrhighPortn_Type()
)
pmopm2CfgChannel83PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel83PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel84PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel84PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel84PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel84PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel84PwrhighPortn = _Pmopm2CfgChannel84PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 86),
    _Pmopm2CfgChannel84PwrhighPortn_Type()
)
pmopm2CfgChannel84PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel84PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel85PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel85PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel85PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel85PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel85PwrhighPortn = _Pmopm2CfgChannel85PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 87),
    _Pmopm2CfgChannel85PwrhighPortn_Type()
)
pmopm2CfgChannel85PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel85PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel86PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel86PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel86PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel86PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel86PwrhighPortn = _Pmopm2CfgChannel86PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 88),
    _Pmopm2CfgChannel86PwrhighPortn_Type()
)
pmopm2CfgChannel86PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel86PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel87PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel87PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel87PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel87PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel87PwrhighPortn = _Pmopm2CfgChannel87PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 89),
    _Pmopm2CfgChannel87PwrhighPortn_Type()
)
pmopm2CfgChannel87PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel87PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel88PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel88PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel88PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel88PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel88PwrhighPortn = _Pmopm2CfgChannel88PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 90),
    _Pmopm2CfgChannel88PwrhighPortn_Type()
)
pmopm2CfgChannel88PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel88PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel89PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel89PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel89PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel89PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel89PwrhighPortn = _Pmopm2CfgChannel89PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 91),
    _Pmopm2CfgChannel89PwrhighPortn_Type()
)
pmopm2CfgChannel89PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel89PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel90PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel90PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel90PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel90PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel90PwrhighPortn = _Pmopm2CfgChannel90PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 92),
    _Pmopm2CfgChannel90PwrhighPortn_Type()
)
pmopm2CfgChannel90PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel90PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel91PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel91PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel91PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel91PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel91PwrhighPortn = _Pmopm2CfgChannel91PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 93),
    _Pmopm2CfgChannel91PwrhighPortn_Type()
)
pmopm2CfgChannel91PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel91PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel92PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel92PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel92PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel92PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel92PwrhighPortn = _Pmopm2CfgChannel92PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 94),
    _Pmopm2CfgChannel92PwrhighPortn_Type()
)
pmopm2CfgChannel92PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel92PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel93PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel93PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel93PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel93PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel93PwrhighPortn = _Pmopm2CfgChannel93PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 95),
    _Pmopm2CfgChannel93PwrhighPortn_Type()
)
pmopm2CfgChannel93PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel93PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel94PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel94PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel94PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel94PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel94PwrhighPortn = _Pmopm2CfgChannel94PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 96),
    _Pmopm2CfgChannel94PwrhighPortn_Type()
)
pmopm2CfgChannel94PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel94PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel95PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel95PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel95PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel95PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel95PwrhighPortn = _Pmopm2CfgChannel95PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 97),
    _Pmopm2CfgChannel95PwrhighPortn_Type()
)
pmopm2CfgChannel95PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel95PwrhighPortn.setStatus("current")


class _Pmopm2CfgChannel96PwrhighPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel96PwrhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel96PwrhighPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel96PwrhighPortn_Object = MibTableColumn
pmopm2CfgChannel96PwrhighPortn = _Pmopm2CfgChannel96PwrhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 5, 1, 98),
    _Pmopm2CfgChannel96PwrhighPortn_Type()
)
pmopm2CfgChannel96PwrhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel96PwrhighPortn.setStatus("current")
_Pmopm2CfgClientStartupPwrLowTable_Object = MibTable
pmopm2CfgClientStartupPwrLowTable = _Pmopm2CfgClientStartupPwrLowTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6)
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupPwrLowTable.setStatus("current")
_Pmopm2CfgClientStartupPwrLowEntry_Object = MibTableRow
pmopm2CfgClientStartupPwrLowEntry = _Pmopm2CfgClientStartupPwrLowEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1)
)
pmopm2CfgClientStartupPwrLowEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CfgClientStartupPwrLowIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupPwrLowEntry.setStatus("current")


class _Pmopm2CfgClientStartupPwrLowIndex_Type(Integer32):
    """Custom type pmopm2CfgClientStartupPwrLowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CfgClientStartupPwrLowIndex_Type.__name__ = "Integer32"
_Pmopm2CfgClientStartupPwrLowIndex_Object = MibTableColumn
pmopm2CfgClientStartupPwrLowIndex = _Pmopm2CfgClientStartupPwrLowIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 1),
    _Pmopm2CfgClientStartupPwrLowIndex_Type()
)
pmopm2CfgClientStartupPwrLowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgClientStartupPwrLowIndex.setStatus("current")


class _Pmopm2CfgChannel1PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel1PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel1PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel1PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel1PwrlowPortn = _Pmopm2CfgChannel1PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 3),
    _Pmopm2CfgChannel1PwrlowPortn_Type()
)
pmopm2CfgChannel1PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel1PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel2PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel2PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel2PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel2PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel2PwrlowPortn = _Pmopm2CfgChannel2PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 4),
    _Pmopm2CfgChannel2PwrlowPortn_Type()
)
pmopm2CfgChannel2PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel2PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel3PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel3PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel3PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel3PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel3PwrlowPortn = _Pmopm2CfgChannel3PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 5),
    _Pmopm2CfgChannel3PwrlowPortn_Type()
)
pmopm2CfgChannel3PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel3PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel4PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel4PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel4PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel4PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel4PwrlowPortn = _Pmopm2CfgChannel4PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 6),
    _Pmopm2CfgChannel4PwrlowPortn_Type()
)
pmopm2CfgChannel4PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel4PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel5PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel5PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel5PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel5PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel5PwrlowPortn = _Pmopm2CfgChannel5PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 7),
    _Pmopm2CfgChannel5PwrlowPortn_Type()
)
pmopm2CfgChannel5PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel5PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel6PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel6PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel6PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel6PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel6PwrlowPortn = _Pmopm2CfgChannel6PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 8),
    _Pmopm2CfgChannel6PwrlowPortn_Type()
)
pmopm2CfgChannel6PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel6PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel7PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel7PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel7PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel7PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel7PwrlowPortn = _Pmopm2CfgChannel7PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 9),
    _Pmopm2CfgChannel7PwrlowPortn_Type()
)
pmopm2CfgChannel7PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel7PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel8PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel8PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel8PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel8PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel8PwrlowPortn = _Pmopm2CfgChannel8PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 10),
    _Pmopm2CfgChannel8PwrlowPortn_Type()
)
pmopm2CfgChannel8PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel8PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel9PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel9PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel9PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel9PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel9PwrlowPortn = _Pmopm2CfgChannel9PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 11),
    _Pmopm2CfgChannel9PwrlowPortn_Type()
)
pmopm2CfgChannel9PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel9PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel10PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel10PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel10PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel10PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel10PwrlowPortn = _Pmopm2CfgChannel10PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 12),
    _Pmopm2CfgChannel10PwrlowPortn_Type()
)
pmopm2CfgChannel10PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel10PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel11PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel11PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel11PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel11PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel11PwrlowPortn = _Pmopm2CfgChannel11PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 13),
    _Pmopm2CfgChannel11PwrlowPortn_Type()
)
pmopm2CfgChannel11PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel11PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel12PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel12PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel12PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel12PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel12PwrlowPortn = _Pmopm2CfgChannel12PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 14),
    _Pmopm2CfgChannel12PwrlowPortn_Type()
)
pmopm2CfgChannel12PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel12PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel13PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel13PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel13PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel13PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel13PwrlowPortn = _Pmopm2CfgChannel13PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 15),
    _Pmopm2CfgChannel13PwrlowPortn_Type()
)
pmopm2CfgChannel13PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel13PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel14PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel14PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel14PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel14PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel14PwrlowPortn = _Pmopm2CfgChannel14PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 16),
    _Pmopm2CfgChannel14PwrlowPortn_Type()
)
pmopm2CfgChannel14PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel14PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel15PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel15PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel15PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel15PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel15PwrlowPortn = _Pmopm2CfgChannel15PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 17),
    _Pmopm2CfgChannel15PwrlowPortn_Type()
)
pmopm2CfgChannel15PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel15PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel16PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel16PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel16PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel16PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel16PwrlowPortn = _Pmopm2CfgChannel16PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 18),
    _Pmopm2CfgChannel16PwrlowPortn_Type()
)
pmopm2CfgChannel16PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel16PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel17PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel17PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel17PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel17PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel17PwrlowPortn = _Pmopm2CfgChannel17PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 19),
    _Pmopm2CfgChannel17PwrlowPortn_Type()
)
pmopm2CfgChannel17PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel17PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel18PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel18PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel18PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel18PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel18PwrlowPortn = _Pmopm2CfgChannel18PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 20),
    _Pmopm2CfgChannel18PwrlowPortn_Type()
)
pmopm2CfgChannel18PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel18PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel19PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel19PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel19PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel19PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel19PwrlowPortn = _Pmopm2CfgChannel19PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 21),
    _Pmopm2CfgChannel19PwrlowPortn_Type()
)
pmopm2CfgChannel19PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel19PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel20PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel20PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel20PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel20PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel20PwrlowPortn = _Pmopm2CfgChannel20PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 22),
    _Pmopm2CfgChannel20PwrlowPortn_Type()
)
pmopm2CfgChannel20PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel20PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel21PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel21PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel21PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel21PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel21PwrlowPortn = _Pmopm2CfgChannel21PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 23),
    _Pmopm2CfgChannel21PwrlowPortn_Type()
)
pmopm2CfgChannel21PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel21PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel22PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel22PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel22PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel22PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel22PwrlowPortn = _Pmopm2CfgChannel22PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 24),
    _Pmopm2CfgChannel22PwrlowPortn_Type()
)
pmopm2CfgChannel22PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel22PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel23PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel23PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel23PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel23PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel23PwrlowPortn = _Pmopm2CfgChannel23PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 25),
    _Pmopm2CfgChannel23PwrlowPortn_Type()
)
pmopm2CfgChannel23PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel23PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel24PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel24PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel24PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel24PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel24PwrlowPortn = _Pmopm2CfgChannel24PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 26),
    _Pmopm2CfgChannel24PwrlowPortn_Type()
)
pmopm2CfgChannel24PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel24PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel25PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel25PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel25PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel25PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel25PwrlowPortn = _Pmopm2CfgChannel25PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 27),
    _Pmopm2CfgChannel25PwrlowPortn_Type()
)
pmopm2CfgChannel25PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel25PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel26PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel26PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel26PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel26PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel26PwrlowPortn = _Pmopm2CfgChannel26PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 28),
    _Pmopm2CfgChannel26PwrlowPortn_Type()
)
pmopm2CfgChannel26PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel26PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel27PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel27PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel27PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel27PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel27PwrlowPortn = _Pmopm2CfgChannel27PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 29),
    _Pmopm2CfgChannel27PwrlowPortn_Type()
)
pmopm2CfgChannel27PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel27PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel28PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel28PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel28PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel28PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel28PwrlowPortn = _Pmopm2CfgChannel28PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 30),
    _Pmopm2CfgChannel28PwrlowPortn_Type()
)
pmopm2CfgChannel28PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel28PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel29PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel29PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel29PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel29PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel29PwrlowPortn = _Pmopm2CfgChannel29PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 31),
    _Pmopm2CfgChannel29PwrlowPortn_Type()
)
pmopm2CfgChannel29PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel29PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel30PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel30PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel30PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel30PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel30PwrlowPortn = _Pmopm2CfgChannel30PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 32),
    _Pmopm2CfgChannel30PwrlowPortn_Type()
)
pmopm2CfgChannel30PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel30PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel31PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel31PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel31PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel31PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel31PwrlowPortn = _Pmopm2CfgChannel31PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 33),
    _Pmopm2CfgChannel31PwrlowPortn_Type()
)
pmopm2CfgChannel31PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel31PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel32PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel32PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel32PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel32PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel32PwrlowPortn = _Pmopm2CfgChannel32PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 34),
    _Pmopm2CfgChannel32PwrlowPortn_Type()
)
pmopm2CfgChannel32PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel32PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel33PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel33PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel33PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel33PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel33PwrlowPortn = _Pmopm2CfgChannel33PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 35),
    _Pmopm2CfgChannel33PwrlowPortn_Type()
)
pmopm2CfgChannel33PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel33PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel34PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel34PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel34PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel34PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel34PwrlowPortn = _Pmopm2CfgChannel34PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 36),
    _Pmopm2CfgChannel34PwrlowPortn_Type()
)
pmopm2CfgChannel34PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel34PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel35PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel35PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel35PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel35PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel35PwrlowPortn = _Pmopm2CfgChannel35PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 37),
    _Pmopm2CfgChannel35PwrlowPortn_Type()
)
pmopm2CfgChannel35PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel35PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel36PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel36PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel36PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel36PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel36PwrlowPortn = _Pmopm2CfgChannel36PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 38),
    _Pmopm2CfgChannel36PwrlowPortn_Type()
)
pmopm2CfgChannel36PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel36PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel37PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel37PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel37PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel37PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel37PwrlowPortn = _Pmopm2CfgChannel37PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 39),
    _Pmopm2CfgChannel37PwrlowPortn_Type()
)
pmopm2CfgChannel37PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel37PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel38PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel38PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel38PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel38PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel38PwrlowPortn = _Pmopm2CfgChannel38PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 40),
    _Pmopm2CfgChannel38PwrlowPortn_Type()
)
pmopm2CfgChannel38PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel38PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel39PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel39PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel39PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel39PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel39PwrlowPortn = _Pmopm2CfgChannel39PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 41),
    _Pmopm2CfgChannel39PwrlowPortn_Type()
)
pmopm2CfgChannel39PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel39PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel40PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel40PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel40PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel40PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel40PwrlowPortn = _Pmopm2CfgChannel40PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 42),
    _Pmopm2CfgChannel40PwrlowPortn_Type()
)
pmopm2CfgChannel40PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel40PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel41PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel41PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel41PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel41PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel41PwrlowPortn = _Pmopm2CfgChannel41PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 43),
    _Pmopm2CfgChannel41PwrlowPortn_Type()
)
pmopm2CfgChannel41PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel41PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel42PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel42PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel42PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel42PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel42PwrlowPortn = _Pmopm2CfgChannel42PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 44),
    _Pmopm2CfgChannel42PwrlowPortn_Type()
)
pmopm2CfgChannel42PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel42PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel43PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel43PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel43PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel43PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel43PwrlowPortn = _Pmopm2CfgChannel43PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 45),
    _Pmopm2CfgChannel43PwrlowPortn_Type()
)
pmopm2CfgChannel43PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel43PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel44PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel44PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel44PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel44PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel44PwrlowPortn = _Pmopm2CfgChannel44PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 46),
    _Pmopm2CfgChannel44PwrlowPortn_Type()
)
pmopm2CfgChannel44PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel44PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel45PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel45PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel45PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel45PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel45PwrlowPortn = _Pmopm2CfgChannel45PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 47),
    _Pmopm2CfgChannel45PwrlowPortn_Type()
)
pmopm2CfgChannel45PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel45PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel46PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel46PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel46PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel46PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel46PwrlowPortn = _Pmopm2CfgChannel46PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 48),
    _Pmopm2CfgChannel46PwrlowPortn_Type()
)
pmopm2CfgChannel46PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel46PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel47PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel47PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel47PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel47PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel47PwrlowPortn = _Pmopm2CfgChannel47PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 49),
    _Pmopm2CfgChannel47PwrlowPortn_Type()
)
pmopm2CfgChannel47PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel47PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel48PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel48PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel48PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel48PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel48PwrlowPortn = _Pmopm2CfgChannel48PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 50),
    _Pmopm2CfgChannel48PwrlowPortn_Type()
)
pmopm2CfgChannel48PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel48PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel49PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel49PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel49PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel49PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel49PwrlowPortn = _Pmopm2CfgChannel49PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 51),
    _Pmopm2CfgChannel49PwrlowPortn_Type()
)
pmopm2CfgChannel49PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel49PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel50PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel50PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel50PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel50PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel50PwrlowPortn = _Pmopm2CfgChannel50PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 52),
    _Pmopm2CfgChannel50PwrlowPortn_Type()
)
pmopm2CfgChannel50PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel50PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel51PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel51PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel51PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel51PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel51PwrlowPortn = _Pmopm2CfgChannel51PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 53),
    _Pmopm2CfgChannel51PwrlowPortn_Type()
)
pmopm2CfgChannel51PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel51PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel52PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel52PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel52PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel52PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel52PwrlowPortn = _Pmopm2CfgChannel52PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 54),
    _Pmopm2CfgChannel52PwrlowPortn_Type()
)
pmopm2CfgChannel52PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel52PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel53PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel53PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel53PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel53PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel53PwrlowPortn = _Pmopm2CfgChannel53PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 55),
    _Pmopm2CfgChannel53PwrlowPortn_Type()
)
pmopm2CfgChannel53PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel53PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel54PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel54PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel54PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel54PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel54PwrlowPortn = _Pmopm2CfgChannel54PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 56),
    _Pmopm2CfgChannel54PwrlowPortn_Type()
)
pmopm2CfgChannel54PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel54PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel55PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel55PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel55PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel55PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel55PwrlowPortn = _Pmopm2CfgChannel55PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 57),
    _Pmopm2CfgChannel55PwrlowPortn_Type()
)
pmopm2CfgChannel55PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel55PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel56PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel56PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel56PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel56PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel56PwrlowPortn = _Pmopm2CfgChannel56PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 58),
    _Pmopm2CfgChannel56PwrlowPortn_Type()
)
pmopm2CfgChannel56PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel56PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel57PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel57PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel57PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel57PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel57PwrlowPortn = _Pmopm2CfgChannel57PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 59),
    _Pmopm2CfgChannel57PwrlowPortn_Type()
)
pmopm2CfgChannel57PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel57PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel58PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel58PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel58PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel58PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel58PwrlowPortn = _Pmopm2CfgChannel58PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 60),
    _Pmopm2CfgChannel58PwrlowPortn_Type()
)
pmopm2CfgChannel58PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel58PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel59PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel59PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel59PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel59PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel59PwrlowPortn = _Pmopm2CfgChannel59PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 61),
    _Pmopm2CfgChannel59PwrlowPortn_Type()
)
pmopm2CfgChannel59PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel59PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel60PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel60PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel60PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel60PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel60PwrlowPortn = _Pmopm2CfgChannel60PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 62),
    _Pmopm2CfgChannel60PwrlowPortn_Type()
)
pmopm2CfgChannel60PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel60PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel61PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel61PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel61PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel61PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel61PwrlowPortn = _Pmopm2CfgChannel61PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 63),
    _Pmopm2CfgChannel61PwrlowPortn_Type()
)
pmopm2CfgChannel61PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel61PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel62PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel62PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel62PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel62PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel62PwrlowPortn = _Pmopm2CfgChannel62PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 64),
    _Pmopm2CfgChannel62PwrlowPortn_Type()
)
pmopm2CfgChannel62PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel62PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel63PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel63PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel63PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel63PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel63PwrlowPortn = _Pmopm2CfgChannel63PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 65),
    _Pmopm2CfgChannel63PwrlowPortn_Type()
)
pmopm2CfgChannel63PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel63PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel64PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel64PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel64PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel64PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel64PwrlowPortn = _Pmopm2CfgChannel64PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 66),
    _Pmopm2CfgChannel64PwrlowPortn_Type()
)
pmopm2CfgChannel64PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel64PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel65PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel65PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel65PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel65PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel65PwrlowPortn = _Pmopm2CfgChannel65PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 67),
    _Pmopm2CfgChannel65PwrlowPortn_Type()
)
pmopm2CfgChannel65PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel65PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel66PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel66PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel66PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel66PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel66PwrlowPortn = _Pmopm2CfgChannel66PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 68),
    _Pmopm2CfgChannel66PwrlowPortn_Type()
)
pmopm2CfgChannel66PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel66PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel67PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel67PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel67PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel67PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel67PwrlowPortn = _Pmopm2CfgChannel67PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 69),
    _Pmopm2CfgChannel67PwrlowPortn_Type()
)
pmopm2CfgChannel67PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel67PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel68PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel68PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel68PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel68PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel68PwrlowPortn = _Pmopm2CfgChannel68PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 70),
    _Pmopm2CfgChannel68PwrlowPortn_Type()
)
pmopm2CfgChannel68PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel68PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel69PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel69PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel69PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel69PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel69PwrlowPortn = _Pmopm2CfgChannel69PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 71),
    _Pmopm2CfgChannel69PwrlowPortn_Type()
)
pmopm2CfgChannel69PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel69PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel70PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel70PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel70PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel70PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel70PwrlowPortn = _Pmopm2CfgChannel70PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 72),
    _Pmopm2CfgChannel70PwrlowPortn_Type()
)
pmopm2CfgChannel70PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel70PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel71PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel71PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel71PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel71PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel71PwrlowPortn = _Pmopm2CfgChannel71PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 73),
    _Pmopm2CfgChannel71PwrlowPortn_Type()
)
pmopm2CfgChannel71PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel71PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel72PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel72PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel72PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel72PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel72PwrlowPortn = _Pmopm2CfgChannel72PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 74),
    _Pmopm2CfgChannel72PwrlowPortn_Type()
)
pmopm2CfgChannel72PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel72PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel73PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel73PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel73PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel73PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel73PwrlowPortn = _Pmopm2CfgChannel73PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 75),
    _Pmopm2CfgChannel73PwrlowPortn_Type()
)
pmopm2CfgChannel73PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel73PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel74PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel74PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel74PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel74PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel74PwrlowPortn = _Pmopm2CfgChannel74PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 76),
    _Pmopm2CfgChannel74PwrlowPortn_Type()
)
pmopm2CfgChannel74PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel74PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel75PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel75PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel75PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel75PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel75PwrlowPortn = _Pmopm2CfgChannel75PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 77),
    _Pmopm2CfgChannel75PwrlowPortn_Type()
)
pmopm2CfgChannel75PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel75PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel76PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel76PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel76PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel76PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel76PwrlowPortn = _Pmopm2CfgChannel76PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 78),
    _Pmopm2CfgChannel76PwrlowPortn_Type()
)
pmopm2CfgChannel76PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel76PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel77PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel77PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel77PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel77PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel77PwrlowPortn = _Pmopm2CfgChannel77PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 79),
    _Pmopm2CfgChannel77PwrlowPortn_Type()
)
pmopm2CfgChannel77PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel77PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel78PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel78PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel78PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel78PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel78PwrlowPortn = _Pmopm2CfgChannel78PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 80),
    _Pmopm2CfgChannel78PwrlowPortn_Type()
)
pmopm2CfgChannel78PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel78PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel79PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel79PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel79PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel79PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel79PwrlowPortn = _Pmopm2CfgChannel79PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 81),
    _Pmopm2CfgChannel79PwrlowPortn_Type()
)
pmopm2CfgChannel79PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel79PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel80PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel80PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel80PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel80PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel80PwrlowPortn = _Pmopm2CfgChannel80PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 82),
    _Pmopm2CfgChannel80PwrlowPortn_Type()
)
pmopm2CfgChannel80PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel80PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel81PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel81PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel81PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel81PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel81PwrlowPortn = _Pmopm2CfgChannel81PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 83),
    _Pmopm2CfgChannel81PwrlowPortn_Type()
)
pmopm2CfgChannel81PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel81PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel82PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel82PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel82PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel82PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel82PwrlowPortn = _Pmopm2CfgChannel82PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 84),
    _Pmopm2CfgChannel82PwrlowPortn_Type()
)
pmopm2CfgChannel82PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel82PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel83PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel83PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel83PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel83PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel83PwrlowPortn = _Pmopm2CfgChannel83PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 85),
    _Pmopm2CfgChannel83PwrlowPortn_Type()
)
pmopm2CfgChannel83PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel83PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel84PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel84PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel84PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel84PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel84PwrlowPortn = _Pmopm2CfgChannel84PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 86),
    _Pmopm2CfgChannel84PwrlowPortn_Type()
)
pmopm2CfgChannel84PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel84PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel85PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel85PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel85PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel85PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel85PwrlowPortn = _Pmopm2CfgChannel85PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 87),
    _Pmopm2CfgChannel85PwrlowPortn_Type()
)
pmopm2CfgChannel85PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel85PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel86PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel86PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel86PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel86PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel86PwrlowPortn = _Pmopm2CfgChannel86PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 88),
    _Pmopm2CfgChannel86PwrlowPortn_Type()
)
pmopm2CfgChannel86PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel86PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel87PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel87PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel87PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel87PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel87PwrlowPortn = _Pmopm2CfgChannel87PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 89),
    _Pmopm2CfgChannel87PwrlowPortn_Type()
)
pmopm2CfgChannel87PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel87PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel88PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel88PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel88PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel88PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel88PwrlowPortn = _Pmopm2CfgChannel88PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 90),
    _Pmopm2CfgChannel88PwrlowPortn_Type()
)
pmopm2CfgChannel88PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel88PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel89PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel89PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel89PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel89PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel89PwrlowPortn = _Pmopm2CfgChannel89PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 91),
    _Pmopm2CfgChannel89PwrlowPortn_Type()
)
pmopm2CfgChannel89PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel89PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel90PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel90PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel90PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel90PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel90PwrlowPortn = _Pmopm2CfgChannel90PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 92),
    _Pmopm2CfgChannel90PwrlowPortn_Type()
)
pmopm2CfgChannel90PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel90PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel91PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel91PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel91PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel91PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel91PwrlowPortn = _Pmopm2CfgChannel91PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 93),
    _Pmopm2CfgChannel91PwrlowPortn_Type()
)
pmopm2CfgChannel91PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel91PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel92PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel92PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel92PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel92PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel92PwrlowPortn = _Pmopm2CfgChannel92PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 94),
    _Pmopm2CfgChannel92PwrlowPortn_Type()
)
pmopm2CfgChannel92PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel92PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel93PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel93PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel93PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel93PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel93PwrlowPortn = _Pmopm2CfgChannel93PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 95),
    _Pmopm2CfgChannel93PwrlowPortn_Type()
)
pmopm2CfgChannel93PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel93PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel94PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel94PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel94PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel94PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel94PwrlowPortn = _Pmopm2CfgChannel94PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 96),
    _Pmopm2CfgChannel94PwrlowPortn_Type()
)
pmopm2CfgChannel94PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel94PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel95PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel95PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel95PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel95PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel95PwrlowPortn = _Pmopm2CfgChannel95PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 97),
    _Pmopm2CfgChannel95PwrlowPortn_Type()
)
pmopm2CfgChannel95PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel95PwrlowPortn.setStatus("current")


class _Pmopm2CfgChannel96PwrlowPortn_Type(Unsigned32):
    """Custom type pmopm2CfgChannel96PwrlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmopm2CfgChannel96PwrlowPortn_Type.__name__ = "Unsigned32"
_Pmopm2CfgChannel96PwrlowPortn_Object = MibTableColumn
pmopm2CfgChannel96PwrlowPortn = _Pmopm2CfgChannel96PwrlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 6, 1, 98),
    _Pmopm2CfgChannel96PwrlowPortn_Type()
)
pmopm2CfgChannel96PwrlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgChannel96PwrlowPortn.setStatus("current")
_Pmopm2CfgLabelclientTable_Object = MibTable
pmopm2CfgLabelclientTable = _Pmopm2CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 7)
)
if mibBuilder.loadTexts:
    pmopm2CfgLabelclientTable.setStatus("current")
_Pmopm2CfgLabelclientEntry_Object = MibTableRow
pmopm2CfgLabelclientEntry = _Pmopm2CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 7, 1)
)
pmopm2CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CfgLabelclientEntry.setStatus("current")


class _Pmopm2CfgLabelclientIndex_Type(Integer32):
    """Custom type pmopm2CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmopm2CfgLabelclientIndex_Object = MibTableColumn
pmopm2CfgLabelclientIndex = _Pmopm2CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 7, 1, 1),
    _Pmopm2CfgLabelclientIndex_Type()
)
pmopm2CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgLabelclientIndex.setStatus("current")


class _Pmopm2CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmopm2CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmopm2CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmopm2CfgLabelclientPortn_Object = MibTableColumn
pmopm2CfgLabelclientPortn = _Pmopm2CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 7, 1, 3),
    _Pmopm2CfgLabelclientPortn_Type()
)
pmopm2CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgLabelclientPortn.setStatus("current")
_Pmopm2CfgLabellineTable_Object = MibTable
pmopm2CfgLabellineTable = _Pmopm2CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 8)
)
if mibBuilder.loadTexts:
    pmopm2CfgLabellineTable.setStatus("current")
_Pmopm2CfgLabellineEntry_Object = MibTableRow
pmopm2CfgLabellineEntry = _Pmopm2CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 8, 1)
)
pmopm2CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmopm2-MIB", "pmopm2CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmopm2CfgLabellineEntry.setStatus("current")


class _Pmopm2CfgLabellineIndex_Type(Integer32):
    """Custom type pmopm2CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmopm2CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmopm2CfgLabellineIndex_Object = MibTableColumn
pmopm2CfgLabellineIndex = _Pmopm2CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 8, 1, 1),
    _Pmopm2CfgLabellineIndex_Type()
)
pmopm2CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2CfgLabellineIndex.setStatus("current")


class _Pmopm2CfgLabellinePortn_Type(DisplayString):
    """Custom type pmopm2CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmopm2CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmopm2CfgLabellinePortn_Object = MibTableColumn
pmopm2CfgLabellinePortn = _Pmopm2CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 2, 8, 1, 3),
    _Pmopm2CfgLabellinePortn_Type()
)
pmopm2CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgLabellinePortn.setStatus("current")
_Pmopm2CfgWriteConfiguration_Type = EkiOnOff
_Pmopm2CfgWriteConfiguration_Object = MibScalar
pmopm2CfgWriteConfiguration = _Pmopm2CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 9, 257),
    _Pmopm2CfgWriteConfiguration_Type()
)
pmopm2CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopm2CfgWriteConfiguration.setStatus("current")
_Pmopm2traps_ObjectIdentity = ObjectIdentity
pmopm2traps = _Pmopm2traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 64, 10)
)


class _Pmopm2trapPortNumber_Type(Integer32):
    """Custom type pmopm2trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmopm2trapPortNumber_Type.__name__ = "Integer32"
_Pmopm2trapPortNumber_Object = MibScalar
pmopm2trapPortNumber = _Pmopm2trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 10, 2),
    _Pmopm2trapPortNumber_Type()
)
pmopm2trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2trapPortNumber.setStatus("current")


class _Pmopm2trapLineNumber_Type(Integer32):
    """Custom type pmopm2trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmopm2trapLineNumber_Type.__name__ = "Integer32"
_Pmopm2trapLineNumber_Object = MibScalar
pmopm2trapLineNumber = _Pmopm2trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 10, 3),
    _Pmopm2trapLineNumber_Type()
)
pmopm2trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2trapLineNumber.setStatus("current")


class _Pmopm2trapBoardNumber_Type(Integer32):
    """Custom type pmopm2trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmopm2trapBoardNumber_Type.__name__ = "Integer32"
_Pmopm2trapBoardNumber_Object = MibScalar
pmopm2trapBoardNumber = _Pmopm2trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 64, 10, 4),
    _Pmopm2trapBoardNumber_Type()
)
pmopm2trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopm2trapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmopm2PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 64, 10, 50)
)
pmopm2PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmopm2-MIB", "pmopm2AlmDefFuseB"),
        ("EKINOPS-Pmopm2-MIB", "pmopm2AlmDefFuseA"),
        ("EKINOPS-Pmopm2-MIB", "pmopm2trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopm2PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmopm2PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 64, 10, 51)
)
pmopm2PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmopm2-MIB", "pmopm2AlmDefFuseB"),
        ("EKINOPS-Pmopm2-MIB", "pmopm2AlmDefFuseA"),
        ("EKINOPS-Pmopm2-MIB", "pmopm2trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopm2PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmopm2-MIB",
    **{"Pmopm2Grid": Pmopm2Grid,
       "Pmopm2MultiRate": Pmopm2MultiRate,
       "Pmopm2OtxChannel": Pmopm2OtxChannel,
       "Pmopm2AdjustValue": Pmopm2AdjustValue,
       "Pmopm2OtxMode": Pmopm2OtxMode,
       "modulePmopm2": modulePmopm2,
       "pmopm2alarms": pmopm2alarms,
       "pmopm2AlmOther": pmopm2AlmOther,
       "pmopm2AlmOtherNurg": pmopm2AlmOtherNurg,
       "pmopm2AlmsynthAlm2": pmopm2AlmsynthAlm2,
       "pmopm2AlmConfTableSave": pmopm2AlmConfTableSave,
       "pmopm2AlmInvUpload": pmopm2AlmInvUpload,
       "pmopm2AlmConfTableLoad": pmopm2AlmConfTableLoad,
       "pmopm2AlmCorrelatOff": pmopm2AlmCorrelatOff,
       "pmopm2AlmOtherUrg": pmopm2AlmOtherUrg,
       "pmopm2AlmOtherCrit": pmopm2AlmOtherCrit,
       "pmopm2AlmsynthAlm0": pmopm2AlmsynthAlm0,
       "pmopm2AlmModGlobFail": pmopm2AlmModGlobFail,
       "pmopm2AlmDefFuseA": pmopm2AlmDefFuseA,
       "pmopm2AlmDefFuseB": pmopm2AlmDefFuseB,
       "pmopm2AlmClient": pmopm2AlmClient,
       "pmopm2AlmClientNurg": pmopm2AlmClientNurg,
       "pmopm2AlmClientUrg": pmopm2AlmClientUrg,
       "pmopm2AlmClientCrit": pmopm2AlmClientCrit,
       "pmopm2AlmsynthAlmPortTable": pmopm2AlmsynthAlmPortTable,
       "pmopm2AlmsynthAlmPortEntry": pmopm2AlmsynthAlmPortEntry,
       "pmopm2AlmsynthAlmPortIndex": pmopm2AlmsynthAlmPortIndex,
       "pmopm2AlmSpectrumAbsentPortn": pmopm2AlmSpectrumAbsentPortn,
       "pmopm2Almchannel1PortTable": pmopm2Almchannel1PortTable,
       "pmopm2Almchannel1PortEntry": pmopm2Almchannel1PortEntry,
       "pmopm2Almchannel1PortIndex": pmopm2Almchannel1PortIndex,
       "pmopm2AlmChannel1AbsentPortn": pmopm2AlmChannel1AbsentPortn,
       "pmopm2AlmChannel1MismatchPortn": pmopm2AlmChannel1MismatchPortn,
       "pmopm2AlmChannel1BalancedPortn": pmopm2AlmChannel1BalancedPortn,
       "pmopm2AlmChannel1PowerLowPortn": pmopm2AlmChannel1PowerLowPortn,
       "pmopm2AlmChannel1PowerHighPortn": pmopm2AlmChannel1PowerHighPortn,
       "pmopm2AlmChannel1OosPortn": pmopm2AlmChannel1OosPortn,
       "pmopm2Almchannel2PortTable": pmopm2Almchannel2PortTable,
       "pmopm2Almchannel2PortEntry": pmopm2Almchannel2PortEntry,
       "pmopm2Almchannel2PortIndex": pmopm2Almchannel2PortIndex,
       "pmopm2AlmChannel2AbsentPortn": pmopm2AlmChannel2AbsentPortn,
       "pmopm2AlmChannel2MismatchPortn": pmopm2AlmChannel2MismatchPortn,
       "pmopm2AlmChannel2BalancedPortn": pmopm2AlmChannel2BalancedPortn,
       "pmopm2AlmChannel2PowerLowPortn": pmopm2AlmChannel2PowerLowPortn,
       "pmopm2AlmChannel2PowerHighPortn": pmopm2AlmChannel2PowerHighPortn,
       "pmopm2AlmChannel2OosPortn": pmopm2AlmChannel2OosPortn,
       "pmopm2Almchannel3PortTable": pmopm2Almchannel3PortTable,
       "pmopm2Almchannel3PortEntry": pmopm2Almchannel3PortEntry,
       "pmopm2Almchannel3PortIndex": pmopm2Almchannel3PortIndex,
       "pmopm2AlmChannel3AbsentPortn": pmopm2AlmChannel3AbsentPortn,
       "pmopm2AlmChannel3MismatchPortn": pmopm2AlmChannel3MismatchPortn,
       "pmopm2AlmChannel3BalancedPortn": pmopm2AlmChannel3BalancedPortn,
       "pmopm2AlmChannel3PowerLowPortn": pmopm2AlmChannel3PowerLowPortn,
       "pmopm2AlmChannel3PowerHighPortn": pmopm2AlmChannel3PowerHighPortn,
       "pmopm2AlmChannel3OosPortn": pmopm2AlmChannel3OosPortn,
       "pmopm2Almchannel4PortTable": pmopm2Almchannel4PortTable,
       "pmopm2Almchannel4PortEntry": pmopm2Almchannel4PortEntry,
       "pmopm2Almchannel4PortIndex": pmopm2Almchannel4PortIndex,
       "pmopm2AlmChannel4AbsentPortn": pmopm2AlmChannel4AbsentPortn,
       "pmopm2AlmChannel4MismatchPortn": pmopm2AlmChannel4MismatchPortn,
       "pmopm2AlmChannel4BalancedPortn": pmopm2AlmChannel4BalancedPortn,
       "pmopm2AlmChannel4PowerLowPortn": pmopm2AlmChannel4PowerLowPortn,
       "pmopm2AlmChannel4PowerHighPortn": pmopm2AlmChannel4PowerHighPortn,
       "pmopm2AlmChannel4OosPortn": pmopm2AlmChannel4OosPortn,
       "pmopm2Almchannel5PortTable": pmopm2Almchannel5PortTable,
       "pmopm2Almchannel5PortEntry": pmopm2Almchannel5PortEntry,
       "pmopm2Almchannel5PortIndex": pmopm2Almchannel5PortIndex,
       "pmopm2AlmChannel5AbsentPortn": pmopm2AlmChannel5AbsentPortn,
       "pmopm2AlmChannel5MismatchPortn": pmopm2AlmChannel5MismatchPortn,
       "pmopm2AlmChannel5BalancedPortn": pmopm2AlmChannel5BalancedPortn,
       "pmopm2AlmChannel5PowerLowPortn": pmopm2AlmChannel5PowerLowPortn,
       "pmopm2AlmChannel5PowerHighPortn": pmopm2AlmChannel5PowerHighPortn,
       "pmopm2AlmChannel5OosPortn": pmopm2AlmChannel5OosPortn,
       "pmopm2Almchannel6PortTable": pmopm2Almchannel6PortTable,
       "pmopm2Almchannel6PortEntry": pmopm2Almchannel6PortEntry,
       "pmopm2Almchannel6PortIndex": pmopm2Almchannel6PortIndex,
       "pmopm2AlmChannel6AbsentPortn": pmopm2AlmChannel6AbsentPortn,
       "pmopm2AlmChannel6MismatchPortn": pmopm2AlmChannel6MismatchPortn,
       "pmopm2AlmChannel6BalancedPortn": pmopm2AlmChannel6BalancedPortn,
       "pmopm2AlmChannel6PowerLowPortn": pmopm2AlmChannel6PowerLowPortn,
       "pmopm2AlmChannel6PowerHighPortn": pmopm2AlmChannel6PowerHighPortn,
       "pmopm2AlmChannel6OosPortn": pmopm2AlmChannel6OosPortn,
       "pmopm2Almchannel7PortTable": pmopm2Almchannel7PortTable,
       "pmopm2Almchannel7PortEntry": pmopm2Almchannel7PortEntry,
       "pmopm2Almchannel7PortIndex": pmopm2Almchannel7PortIndex,
       "pmopm2AlmChannel7AbsentPortn": pmopm2AlmChannel7AbsentPortn,
       "pmopm2AlmChannel7MismatchPortn": pmopm2AlmChannel7MismatchPortn,
       "pmopm2AlmChannel7BalancedPortn": pmopm2AlmChannel7BalancedPortn,
       "pmopm2AlmChannel7PowerLowPortn": pmopm2AlmChannel7PowerLowPortn,
       "pmopm2AlmChannel7PowerHighPortn": pmopm2AlmChannel7PowerHighPortn,
       "pmopm2AlmChannel7OosPortn": pmopm2AlmChannel7OosPortn,
       "pmopm2Almchannel8PortTable": pmopm2Almchannel8PortTable,
       "pmopm2Almchannel8PortEntry": pmopm2Almchannel8PortEntry,
       "pmopm2Almchannel8PortIndex": pmopm2Almchannel8PortIndex,
       "pmopm2AlmChannel8AbsentPortn": pmopm2AlmChannel8AbsentPortn,
       "pmopm2AlmChannel8MismatchPortn": pmopm2AlmChannel8MismatchPortn,
       "pmopm2AlmChannel8BalancedPortn": pmopm2AlmChannel8BalancedPortn,
       "pmopm2AlmChannel8PowerLowPortn": pmopm2AlmChannel8PowerLowPortn,
       "pmopm2AlmChannel8PowerHighPortn": pmopm2AlmChannel8PowerHighPortn,
       "pmopm2AlmChannel8OosPortn": pmopm2AlmChannel8OosPortn,
       "pmopm2Almchannel9PortTable": pmopm2Almchannel9PortTable,
       "pmopm2Almchannel9PortEntry": pmopm2Almchannel9PortEntry,
       "pmopm2Almchannel9PortIndex": pmopm2Almchannel9PortIndex,
       "pmopm2AlmChannel9AbsentPortn": pmopm2AlmChannel9AbsentPortn,
       "pmopm2AlmChannel9MismatchPortn": pmopm2AlmChannel9MismatchPortn,
       "pmopm2AlmChannel9BalancedPortn": pmopm2AlmChannel9BalancedPortn,
       "pmopm2AlmChannel9PowerLowPortn": pmopm2AlmChannel9PowerLowPortn,
       "pmopm2AlmChannel9PowerHighPortn": pmopm2AlmChannel9PowerHighPortn,
       "pmopm2AlmChannel9OosPortn": pmopm2AlmChannel9OosPortn,
       "pmopm2Almchannel10PortTable": pmopm2Almchannel10PortTable,
       "pmopm2Almchannel10PortEntry": pmopm2Almchannel10PortEntry,
       "pmopm2Almchannel10PortIndex": pmopm2Almchannel10PortIndex,
       "pmopm2AlmChannel10AbsentPortn": pmopm2AlmChannel10AbsentPortn,
       "pmopm2AlmChannel10MismatchPortn": pmopm2AlmChannel10MismatchPortn,
       "pmopm2AlmChannel10BalancedPortn": pmopm2AlmChannel10BalancedPortn,
       "pmopm2AlmChannel10PowerLowPortn": pmopm2AlmChannel10PowerLowPortn,
       "pmopm2AlmChannel10PowerHighPortn": pmopm2AlmChannel10PowerHighPortn,
       "pmopm2AlmChannel10OosPortn": pmopm2AlmChannel10OosPortn,
       "pmopm2Almchannel11PortTable": pmopm2Almchannel11PortTable,
       "pmopm2Almchannel11PortEntry": pmopm2Almchannel11PortEntry,
       "pmopm2Almchannel11PortIndex": pmopm2Almchannel11PortIndex,
       "pmopm2AlmChannel11AbsentPortn": pmopm2AlmChannel11AbsentPortn,
       "pmopm2AlmChannel11MismatchPortn": pmopm2AlmChannel11MismatchPortn,
       "pmopm2AlmChannel11BalancedPortn": pmopm2AlmChannel11BalancedPortn,
       "pmopm2AlmChannel11PowerLowPortn": pmopm2AlmChannel11PowerLowPortn,
       "pmopm2AlmChannel11PowerHighPortn": pmopm2AlmChannel11PowerHighPortn,
       "pmopm2AlmChannel11OosPortn": pmopm2AlmChannel11OosPortn,
       "pmopm2Almchannel12PortTable": pmopm2Almchannel12PortTable,
       "pmopm2Almchannel12PortEntry": pmopm2Almchannel12PortEntry,
       "pmopm2Almchannel12PortIndex": pmopm2Almchannel12PortIndex,
       "pmopm2AlmChannel12AbsentPortn": pmopm2AlmChannel12AbsentPortn,
       "pmopm2AlmChannel12MismatchPortn": pmopm2AlmChannel12MismatchPortn,
       "pmopm2AlmChannel12BalancedPortn": pmopm2AlmChannel12BalancedPortn,
       "pmopm2AlmChannel12PowerLowPortn": pmopm2AlmChannel12PowerLowPortn,
       "pmopm2AlmChannel12PowerHighPortn": pmopm2AlmChannel12PowerHighPortn,
       "pmopm2AlmChannel12OosPortn": pmopm2AlmChannel12OosPortn,
       "pmopm2Almchannel13PortTable": pmopm2Almchannel13PortTable,
       "pmopm2Almchannel13PortEntry": pmopm2Almchannel13PortEntry,
       "pmopm2Almchannel13PortIndex": pmopm2Almchannel13PortIndex,
       "pmopm2AlmChannel13AbsentPortn": pmopm2AlmChannel13AbsentPortn,
       "pmopm2AlmChannel13MismatchPortn": pmopm2AlmChannel13MismatchPortn,
       "pmopm2AlmChannel13BalancedPortn": pmopm2AlmChannel13BalancedPortn,
       "pmopm2AlmChannel13PowerLowPortn": pmopm2AlmChannel13PowerLowPortn,
       "pmopm2AlmChannel13PowerHighPortn": pmopm2AlmChannel13PowerHighPortn,
       "pmopm2AlmChannel13OosPortn": pmopm2AlmChannel13OosPortn,
       "pmopm2Almchannel14PortTable": pmopm2Almchannel14PortTable,
       "pmopm2Almchannel14PortEntry": pmopm2Almchannel14PortEntry,
       "pmopm2Almchannel14PortIndex": pmopm2Almchannel14PortIndex,
       "pmopm2AlmChannel14AbsentPortn": pmopm2AlmChannel14AbsentPortn,
       "pmopm2AlmChannel14MismatchPortn": pmopm2AlmChannel14MismatchPortn,
       "pmopm2AlmChannel14BalancedPortn": pmopm2AlmChannel14BalancedPortn,
       "pmopm2AlmChannel14PowerLowPortn": pmopm2AlmChannel14PowerLowPortn,
       "pmopm2AlmChannel14PowerHighPortn": pmopm2AlmChannel14PowerHighPortn,
       "pmopm2AlmChannel14OosPortn": pmopm2AlmChannel14OosPortn,
       "pmopm2Almchannel15PortTable": pmopm2Almchannel15PortTable,
       "pmopm2Almchannel15PortEntry": pmopm2Almchannel15PortEntry,
       "pmopm2Almchannel15PortIndex": pmopm2Almchannel15PortIndex,
       "pmopm2AlmChannel15AbsentPortn": pmopm2AlmChannel15AbsentPortn,
       "pmopm2AlmChannel15MismatchPortn": pmopm2AlmChannel15MismatchPortn,
       "pmopm2AlmChannel15BalancedPortn": pmopm2AlmChannel15BalancedPortn,
       "pmopm2AlmChannel15PowerLowPortn": pmopm2AlmChannel15PowerLowPortn,
       "pmopm2AlmChannel15PowerHighPortn": pmopm2AlmChannel15PowerHighPortn,
       "pmopm2AlmChannel15OosPortn": pmopm2AlmChannel15OosPortn,
       "pmopm2Almchannel16PortTable": pmopm2Almchannel16PortTable,
       "pmopm2Almchannel16PortEntry": pmopm2Almchannel16PortEntry,
       "pmopm2Almchannel16PortIndex": pmopm2Almchannel16PortIndex,
       "pmopm2AlmChannel16AbsentPortn": pmopm2AlmChannel16AbsentPortn,
       "pmopm2AlmChannel16MismatchPortn": pmopm2AlmChannel16MismatchPortn,
       "pmopm2AlmChannel16BalancedPortn": pmopm2AlmChannel16BalancedPortn,
       "pmopm2AlmChannel16PowerLowPortn": pmopm2AlmChannel16PowerLowPortn,
       "pmopm2AlmChannel16PowerHighPortn": pmopm2AlmChannel16PowerHighPortn,
       "pmopm2AlmChannel16OosPortn": pmopm2AlmChannel16OosPortn,
       "pmopm2Almchannel17PortTable": pmopm2Almchannel17PortTable,
       "pmopm2Almchannel17PortEntry": pmopm2Almchannel17PortEntry,
       "pmopm2Almchannel17PortIndex": pmopm2Almchannel17PortIndex,
       "pmopm2AlmChannel17AbsentPortn": pmopm2AlmChannel17AbsentPortn,
       "pmopm2AlmChannel17MismatchPortn": pmopm2AlmChannel17MismatchPortn,
       "pmopm2AlmChannel17BalancedPortn": pmopm2AlmChannel17BalancedPortn,
       "pmopm2AlmChannel17PowerLowPortn": pmopm2AlmChannel17PowerLowPortn,
       "pmopm2AlmChannel17PowerHighPortn": pmopm2AlmChannel17PowerHighPortn,
       "pmopm2AlmChannel17OosPortn": pmopm2AlmChannel17OosPortn,
       "pmopm2Almchannel18PortTable": pmopm2Almchannel18PortTable,
       "pmopm2Almchannel18PortEntry": pmopm2Almchannel18PortEntry,
       "pmopm2Almchannel18PortIndex": pmopm2Almchannel18PortIndex,
       "pmopm2AlmChannel18AbsentPortn": pmopm2AlmChannel18AbsentPortn,
       "pmopm2AlmChannel18MismatchPortn": pmopm2AlmChannel18MismatchPortn,
       "pmopm2AlmChannel18BalancedPortn": pmopm2AlmChannel18BalancedPortn,
       "pmopm2AlmChannel18PowerLowPortn": pmopm2AlmChannel18PowerLowPortn,
       "pmopm2AlmChannel18PowerHighPortn": pmopm2AlmChannel18PowerHighPortn,
       "pmopm2AlmChannel18OosPortn": pmopm2AlmChannel18OosPortn,
       "pmopm2Almchannel19PortTable": pmopm2Almchannel19PortTable,
       "pmopm2Almchannel19PortEntry": pmopm2Almchannel19PortEntry,
       "pmopm2Almchannel19PortIndex": pmopm2Almchannel19PortIndex,
       "pmopm2AlmChannel19AbsentPortn": pmopm2AlmChannel19AbsentPortn,
       "pmopm2AlmChannel19MismatchPortn": pmopm2AlmChannel19MismatchPortn,
       "pmopm2AlmChannel19BalancedPortn": pmopm2AlmChannel19BalancedPortn,
       "pmopm2AlmChannel19PowerLowPortn": pmopm2AlmChannel19PowerLowPortn,
       "pmopm2AlmChannel19PowerHighPortn": pmopm2AlmChannel19PowerHighPortn,
       "pmopm2AlmChannel19OosPortn": pmopm2AlmChannel19OosPortn,
       "pmopm2Almchannel20PortTable": pmopm2Almchannel20PortTable,
       "pmopm2Almchannel20PortEntry": pmopm2Almchannel20PortEntry,
       "pmopm2Almchannel20PortIndex": pmopm2Almchannel20PortIndex,
       "pmopm2AlmChannel20AbsentPortn": pmopm2AlmChannel20AbsentPortn,
       "pmopm2AlmChannel20MismatchPortn": pmopm2AlmChannel20MismatchPortn,
       "pmopm2AlmChannel20BalancedPortn": pmopm2AlmChannel20BalancedPortn,
       "pmopm2AlmChannel20PowerLowPortn": pmopm2AlmChannel20PowerLowPortn,
       "pmopm2AlmChannel20PowerHighPortn": pmopm2AlmChannel20PowerHighPortn,
       "pmopm2AlmChannel20OosPortn": pmopm2AlmChannel20OosPortn,
       "pmopm2Almchannel21PortTable": pmopm2Almchannel21PortTable,
       "pmopm2Almchannel21PortEntry": pmopm2Almchannel21PortEntry,
       "pmopm2Almchannel21PortIndex": pmopm2Almchannel21PortIndex,
       "pmopm2AlmChannel21AbsentPortn": pmopm2AlmChannel21AbsentPortn,
       "pmopm2AlmChannel21MismatchPortn": pmopm2AlmChannel21MismatchPortn,
       "pmopm2AlmChannel21BalancedPortn": pmopm2AlmChannel21BalancedPortn,
       "pmopm2AlmChannel21PowerLowPortn": pmopm2AlmChannel21PowerLowPortn,
       "pmopm2AlmChannel21PowerHighPortn": pmopm2AlmChannel21PowerHighPortn,
       "pmopm2AlmChannel21OosPortn": pmopm2AlmChannel21OosPortn,
       "pmopm2Almchannel22PortTable": pmopm2Almchannel22PortTable,
       "pmopm2Almchannel22PortEntry": pmopm2Almchannel22PortEntry,
       "pmopm2Almchannel22PortIndex": pmopm2Almchannel22PortIndex,
       "pmopm2AlmChannel22AbsentPortn": pmopm2AlmChannel22AbsentPortn,
       "pmopm2AlmChannel22MismatchPortn": pmopm2AlmChannel22MismatchPortn,
       "pmopm2AlmChannel22BalancedPortn": pmopm2AlmChannel22BalancedPortn,
       "pmopm2AlmChannel22PowerLowPortn": pmopm2AlmChannel22PowerLowPortn,
       "pmopm2AlmChannel22PowerHighPortn": pmopm2AlmChannel22PowerHighPortn,
       "pmopm2AlmChannel22OosPortn": pmopm2AlmChannel22OosPortn,
       "pmopm2Almchannel23PortTable": pmopm2Almchannel23PortTable,
       "pmopm2Almchannel23PortEntry": pmopm2Almchannel23PortEntry,
       "pmopm2Almchannel23PortIndex": pmopm2Almchannel23PortIndex,
       "pmopm2AlmChannel23AbsentPortn": pmopm2AlmChannel23AbsentPortn,
       "pmopm2AlmChannel23MismatchPortn": pmopm2AlmChannel23MismatchPortn,
       "pmopm2AlmChannel23BalancedPortn": pmopm2AlmChannel23BalancedPortn,
       "pmopm2AlmChannel23PowerLowPortn": pmopm2AlmChannel23PowerLowPortn,
       "pmopm2AlmChannel23PowerHighPortn": pmopm2AlmChannel23PowerHighPortn,
       "pmopm2AlmChannel23OosPortn": pmopm2AlmChannel23OosPortn,
       "pmopm2Almchannel24PortTable": pmopm2Almchannel24PortTable,
       "pmopm2Almchannel24PortEntry": pmopm2Almchannel24PortEntry,
       "pmopm2Almchannel24PortIndex": pmopm2Almchannel24PortIndex,
       "pmopm2AlmChannel24AbsentPortn": pmopm2AlmChannel24AbsentPortn,
       "pmopm2AlmChannel24MismatchPortn": pmopm2AlmChannel24MismatchPortn,
       "pmopm2AlmChannel24BalancedPortn": pmopm2AlmChannel24BalancedPortn,
       "pmopm2AlmChannel24PowerLowPortn": pmopm2AlmChannel24PowerLowPortn,
       "pmopm2AlmChannel24PowerHighPortn": pmopm2AlmChannel24PowerHighPortn,
       "pmopm2AlmChannel24OosPortn": pmopm2AlmChannel24OosPortn,
       "pmopm2Almchannel25PortTable": pmopm2Almchannel25PortTable,
       "pmopm2Almchannel25PortEntry": pmopm2Almchannel25PortEntry,
       "pmopm2Almchannel25PortIndex": pmopm2Almchannel25PortIndex,
       "pmopm2AlmChannel25AbsentPortn": pmopm2AlmChannel25AbsentPortn,
       "pmopm2AlmChannel25MismatchPortn": pmopm2AlmChannel25MismatchPortn,
       "pmopm2AlmChannel25BalancedPortn": pmopm2AlmChannel25BalancedPortn,
       "pmopm2AlmChannel25PowerLowPortn": pmopm2AlmChannel25PowerLowPortn,
       "pmopm2AlmChannel25PowerHighPortn": pmopm2AlmChannel25PowerHighPortn,
       "pmopm2AlmChannel25OosPortn": pmopm2AlmChannel25OosPortn,
       "pmopm2Almchannel26PortTable": pmopm2Almchannel26PortTable,
       "pmopm2Almchannel26PortEntry": pmopm2Almchannel26PortEntry,
       "pmopm2Almchannel26PortIndex": pmopm2Almchannel26PortIndex,
       "pmopm2AlmChannel26AbsentPortn": pmopm2AlmChannel26AbsentPortn,
       "pmopm2AlmChannel26MismatchPortn": pmopm2AlmChannel26MismatchPortn,
       "pmopm2AlmChannel26BalancedPortn": pmopm2AlmChannel26BalancedPortn,
       "pmopm2AlmChannel26PowerLowPortn": pmopm2AlmChannel26PowerLowPortn,
       "pmopm2AlmChannel26PowerHighPortn": pmopm2AlmChannel26PowerHighPortn,
       "pmopm2AlmChannel26OosPortn": pmopm2AlmChannel26OosPortn,
       "pmopm2Almchannel27PortTable": pmopm2Almchannel27PortTable,
       "pmopm2Almchannel27PortEntry": pmopm2Almchannel27PortEntry,
       "pmopm2Almchannel27PortIndex": pmopm2Almchannel27PortIndex,
       "pmopm2AlmChannel27AbsentPortn": pmopm2AlmChannel27AbsentPortn,
       "pmopm2AlmChannel27MismatchPortn": pmopm2AlmChannel27MismatchPortn,
       "pmopm2AlmChannel27BalancedPortn": pmopm2AlmChannel27BalancedPortn,
       "pmopm2AlmChannel27PowerLowPortn": pmopm2AlmChannel27PowerLowPortn,
       "pmopm2AlmChannel27PowerHighPortn": pmopm2AlmChannel27PowerHighPortn,
       "pmopm2AlmChannel27OosPortn": pmopm2AlmChannel27OosPortn,
       "pmopm2Almchannel28PortTable": pmopm2Almchannel28PortTable,
       "pmopm2Almchannel28PortEntry": pmopm2Almchannel28PortEntry,
       "pmopm2Almchannel28PortIndex": pmopm2Almchannel28PortIndex,
       "pmopm2AlmChannel28AbsentPortn": pmopm2AlmChannel28AbsentPortn,
       "pmopm2AlmChannel28MismatchPortn": pmopm2AlmChannel28MismatchPortn,
       "pmopm2AlmChannel28BalancedPortn": pmopm2AlmChannel28BalancedPortn,
       "pmopm2AlmChannel28PowerLowPortn": pmopm2AlmChannel28PowerLowPortn,
       "pmopm2AlmChannel28PowerHighPortn": pmopm2AlmChannel28PowerHighPortn,
       "pmopm2AlmChannel28OosPortn": pmopm2AlmChannel28OosPortn,
       "pmopm2Almchannel29PortTable": pmopm2Almchannel29PortTable,
       "pmopm2Almchannel29PortEntry": pmopm2Almchannel29PortEntry,
       "pmopm2Almchannel29PortIndex": pmopm2Almchannel29PortIndex,
       "pmopm2AlmChannel29AbsentPortn": pmopm2AlmChannel29AbsentPortn,
       "pmopm2AlmChannel29MismatchPortn": pmopm2AlmChannel29MismatchPortn,
       "pmopm2AlmChannel29BalancedPortn": pmopm2AlmChannel29BalancedPortn,
       "pmopm2AlmChannel29PowerLowPortn": pmopm2AlmChannel29PowerLowPortn,
       "pmopm2AlmChannel29PowerHighPortn": pmopm2AlmChannel29PowerHighPortn,
       "pmopm2AlmChannel29OosPortn": pmopm2AlmChannel29OosPortn,
       "pmopm2Almchannel30PortTable": pmopm2Almchannel30PortTable,
       "pmopm2Almchannel30PortEntry": pmopm2Almchannel30PortEntry,
       "pmopm2Almchannel30PortIndex": pmopm2Almchannel30PortIndex,
       "pmopm2AlmChannel30AbsentPortn": pmopm2AlmChannel30AbsentPortn,
       "pmopm2AlmChannel30MismatchPortn": pmopm2AlmChannel30MismatchPortn,
       "pmopm2AlmChannel30BalancedPortn": pmopm2AlmChannel30BalancedPortn,
       "pmopm2AlmChannel30PowerLowPortn": pmopm2AlmChannel30PowerLowPortn,
       "pmopm2AlmChannel30PowerHighPortn": pmopm2AlmChannel30PowerHighPortn,
       "pmopm2AlmChannel30OosPortn": pmopm2AlmChannel30OosPortn,
       "pmopm2Almchannel31PortTable": pmopm2Almchannel31PortTable,
       "pmopm2Almchannel31PortEntry": pmopm2Almchannel31PortEntry,
       "pmopm2Almchannel31PortIndex": pmopm2Almchannel31PortIndex,
       "pmopm2AlmChannel31AbsentPortn": pmopm2AlmChannel31AbsentPortn,
       "pmopm2AlmChannel31MismatchPortn": pmopm2AlmChannel31MismatchPortn,
       "pmopm2AlmChannel31BalancedPortn": pmopm2AlmChannel31BalancedPortn,
       "pmopm2AlmChannel31PowerLowPortn": pmopm2AlmChannel31PowerLowPortn,
       "pmopm2AlmChannel31PowerHighPortn": pmopm2AlmChannel31PowerHighPortn,
       "pmopm2AlmChannel31OosPortn": pmopm2AlmChannel31OosPortn,
       "pmopm2Almchannel32PortTable": pmopm2Almchannel32PortTable,
       "pmopm2Almchannel32PortEntry": pmopm2Almchannel32PortEntry,
       "pmopm2Almchannel32PortIndex": pmopm2Almchannel32PortIndex,
       "pmopm2AlmChannel32AbsentPortn": pmopm2AlmChannel32AbsentPortn,
       "pmopm2AlmChannel32MismatchPortn": pmopm2AlmChannel32MismatchPortn,
       "pmopm2AlmChannel32BalancedPortn": pmopm2AlmChannel32BalancedPortn,
       "pmopm2AlmChannel32PowerLowPortn": pmopm2AlmChannel32PowerLowPortn,
       "pmopm2AlmChannel32PowerHighPortn": pmopm2AlmChannel32PowerHighPortn,
       "pmopm2AlmChannel32OosPortn": pmopm2AlmChannel32OosPortn,
       "pmopm2Almchannel33PortTable": pmopm2Almchannel33PortTable,
       "pmopm2Almchannel33PortEntry": pmopm2Almchannel33PortEntry,
       "pmopm2Almchannel33PortIndex": pmopm2Almchannel33PortIndex,
       "pmopm2AlmChannel33AbsentPortn": pmopm2AlmChannel33AbsentPortn,
       "pmopm2AlmChannel33MismatchPortn": pmopm2AlmChannel33MismatchPortn,
       "pmopm2AlmChannel33BalancedPortn": pmopm2AlmChannel33BalancedPortn,
       "pmopm2AlmChannel33PowerLowPortn": pmopm2AlmChannel33PowerLowPortn,
       "pmopm2AlmChannel33PowerHighPortn": pmopm2AlmChannel33PowerHighPortn,
       "pmopm2AlmChannel33OosPortn": pmopm2AlmChannel33OosPortn,
       "pmopm2Almchannel34PortTable": pmopm2Almchannel34PortTable,
       "pmopm2Almchannel34PortEntry": pmopm2Almchannel34PortEntry,
       "pmopm2Almchannel34PortIndex": pmopm2Almchannel34PortIndex,
       "pmopm2AlmChannel34AbsentPortn": pmopm2AlmChannel34AbsentPortn,
       "pmopm2AlmChannel34MismatchPortn": pmopm2AlmChannel34MismatchPortn,
       "pmopm2AlmChannel34BalancedPortn": pmopm2AlmChannel34BalancedPortn,
       "pmopm2AlmChannel34PowerLowPortn": pmopm2AlmChannel34PowerLowPortn,
       "pmopm2AlmChannel34PowerHighPortn": pmopm2AlmChannel34PowerHighPortn,
       "pmopm2AlmChannel34OosPortn": pmopm2AlmChannel34OosPortn,
       "pmopm2Almchannel35PortTable": pmopm2Almchannel35PortTable,
       "pmopm2Almchannel35PortEntry": pmopm2Almchannel35PortEntry,
       "pmopm2Almchannel35PortIndex": pmopm2Almchannel35PortIndex,
       "pmopm2AlmChannel35AbsentPortn": pmopm2AlmChannel35AbsentPortn,
       "pmopm2AlmChannel35MismatchPortn": pmopm2AlmChannel35MismatchPortn,
       "pmopm2AlmChannel35BalancedPortn": pmopm2AlmChannel35BalancedPortn,
       "pmopm2AlmChannel35PowerLowPortn": pmopm2AlmChannel35PowerLowPortn,
       "pmopm2AlmChannel35PowerHighPortn": pmopm2AlmChannel35PowerHighPortn,
       "pmopm2AlmChannel35OosPortn": pmopm2AlmChannel35OosPortn,
       "pmopm2Almchannel36PortTable": pmopm2Almchannel36PortTable,
       "pmopm2Almchannel36PortEntry": pmopm2Almchannel36PortEntry,
       "pmopm2Almchannel36PortIndex": pmopm2Almchannel36PortIndex,
       "pmopm2AlmChannel36AbsentPortn": pmopm2AlmChannel36AbsentPortn,
       "pmopm2AlmChannel36MismatchPortn": pmopm2AlmChannel36MismatchPortn,
       "pmopm2AlmChannel36BalancedPortn": pmopm2AlmChannel36BalancedPortn,
       "pmopm2AlmChannel36PowerLowPortn": pmopm2AlmChannel36PowerLowPortn,
       "pmopm2AlmChannel36PowerHighPortn": pmopm2AlmChannel36PowerHighPortn,
       "pmopm2AlmChannel36OosPortn": pmopm2AlmChannel36OosPortn,
       "pmopm2Almchannel37PortTable": pmopm2Almchannel37PortTable,
       "pmopm2Almchannel37PortEntry": pmopm2Almchannel37PortEntry,
       "pmopm2Almchannel37PortIndex": pmopm2Almchannel37PortIndex,
       "pmopm2AlmChannel37AbsentPortn": pmopm2AlmChannel37AbsentPortn,
       "pmopm2AlmChannel37MismatchPortn": pmopm2AlmChannel37MismatchPortn,
       "pmopm2AlmChannel37BalancedPortn": pmopm2AlmChannel37BalancedPortn,
       "pmopm2AlmChannel37PowerLowPortn": pmopm2AlmChannel37PowerLowPortn,
       "pmopm2AlmChannel37PowerHighPortn": pmopm2AlmChannel37PowerHighPortn,
       "pmopm2AlmChannel37OosPortn": pmopm2AlmChannel37OosPortn,
       "pmopm2Almchannel38PortTable": pmopm2Almchannel38PortTable,
       "pmopm2Almchannel38PortEntry": pmopm2Almchannel38PortEntry,
       "pmopm2Almchannel38PortIndex": pmopm2Almchannel38PortIndex,
       "pmopm2AlmChannel38AbsentPortn": pmopm2AlmChannel38AbsentPortn,
       "pmopm2AlmChannel38MismatchPortn": pmopm2AlmChannel38MismatchPortn,
       "pmopm2AlmChannel38BalancedPortn": pmopm2AlmChannel38BalancedPortn,
       "pmopm2AlmChannel38PowerLowPortn": pmopm2AlmChannel38PowerLowPortn,
       "pmopm2AlmChannel38PowerHighPortn": pmopm2AlmChannel38PowerHighPortn,
       "pmopm2AlmChannel38OosPortn": pmopm2AlmChannel38OosPortn,
       "pmopm2Almchannel39PortTable": pmopm2Almchannel39PortTable,
       "pmopm2Almchannel39PortEntry": pmopm2Almchannel39PortEntry,
       "pmopm2Almchannel39PortIndex": pmopm2Almchannel39PortIndex,
       "pmopm2AlmChannel39AbsentPortn": pmopm2AlmChannel39AbsentPortn,
       "pmopm2AlmChannel39MismatchPortn": pmopm2AlmChannel39MismatchPortn,
       "pmopm2AlmChannel39BalancedPortn": pmopm2AlmChannel39BalancedPortn,
       "pmopm2AlmChannel39PowerLowPortn": pmopm2AlmChannel39PowerLowPortn,
       "pmopm2AlmChannel39PowerHighPortn": pmopm2AlmChannel39PowerHighPortn,
       "pmopm2AlmChannel39OosPortn": pmopm2AlmChannel39OosPortn,
       "pmopm2Almchannel40PortTable": pmopm2Almchannel40PortTable,
       "pmopm2Almchannel40PortEntry": pmopm2Almchannel40PortEntry,
       "pmopm2Almchannel40PortIndex": pmopm2Almchannel40PortIndex,
       "pmopm2AlmChannel40AbsentPortn": pmopm2AlmChannel40AbsentPortn,
       "pmopm2AlmChannel40MismatchPortn": pmopm2AlmChannel40MismatchPortn,
       "pmopm2AlmChannel40BalancedPortn": pmopm2AlmChannel40BalancedPortn,
       "pmopm2AlmChannel40PowerLowPortn": pmopm2AlmChannel40PowerLowPortn,
       "pmopm2AlmChannel40PowerHighPortn": pmopm2AlmChannel40PowerHighPortn,
       "pmopm2AlmChannel40OosPortn": pmopm2AlmChannel40OosPortn,
       "pmopm2Almchannel41PortTable": pmopm2Almchannel41PortTable,
       "pmopm2Almchannel41PortEntry": pmopm2Almchannel41PortEntry,
       "pmopm2Almchannel41PortIndex": pmopm2Almchannel41PortIndex,
       "pmopm2AlmChannel41AbsentPortn": pmopm2AlmChannel41AbsentPortn,
       "pmopm2AlmChannel41MismatchPortn": pmopm2AlmChannel41MismatchPortn,
       "pmopm2AlmChannel41BalancedPortn": pmopm2AlmChannel41BalancedPortn,
       "pmopm2AlmChannel41PowerLowPortn": pmopm2AlmChannel41PowerLowPortn,
       "pmopm2AlmChannel41PowerHighPortn": pmopm2AlmChannel41PowerHighPortn,
       "pmopm2AlmChannel41OosPortn": pmopm2AlmChannel41OosPortn,
       "pmopm2Almchannel42PortTable": pmopm2Almchannel42PortTable,
       "pmopm2Almchannel42PortEntry": pmopm2Almchannel42PortEntry,
       "pmopm2Almchannel42PortIndex": pmopm2Almchannel42PortIndex,
       "pmopm2AlmChannel42AbsentPortn": pmopm2AlmChannel42AbsentPortn,
       "pmopm2AlmChannel42MismatchPortn": pmopm2AlmChannel42MismatchPortn,
       "pmopm2AlmChannel42BalancedPortn": pmopm2AlmChannel42BalancedPortn,
       "pmopm2AlmChannel42PowerLowPortn": pmopm2AlmChannel42PowerLowPortn,
       "pmopm2AlmChannel42PowerHighPortn": pmopm2AlmChannel42PowerHighPortn,
       "pmopm2AlmChannel42OosPortn": pmopm2AlmChannel42OosPortn,
       "pmopm2Almchannel43PortTable": pmopm2Almchannel43PortTable,
       "pmopm2Almchannel43PortEntry": pmopm2Almchannel43PortEntry,
       "pmopm2Almchannel43PortIndex": pmopm2Almchannel43PortIndex,
       "pmopm2AlmChannel43AbsentPortn": pmopm2AlmChannel43AbsentPortn,
       "pmopm2AlmChannel43MismatchPortn": pmopm2AlmChannel43MismatchPortn,
       "pmopm2AlmChannel43BalancedPortn": pmopm2AlmChannel43BalancedPortn,
       "pmopm2AlmChannel43PowerLowPortn": pmopm2AlmChannel43PowerLowPortn,
       "pmopm2AlmChannel43PowerHighPortn": pmopm2AlmChannel43PowerHighPortn,
       "pmopm2AlmChannel43OosPortn": pmopm2AlmChannel43OosPortn,
       "pmopm2Almchannel44PortTable": pmopm2Almchannel44PortTable,
       "pmopm2Almchannel44PortEntry": pmopm2Almchannel44PortEntry,
       "pmopm2Almchannel44PortIndex": pmopm2Almchannel44PortIndex,
       "pmopm2AlmChannel44AbsentPortn": pmopm2AlmChannel44AbsentPortn,
       "pmopm2AlmChannel44MismatchPortn": pmopm2AlmChannel44MismatchPortn,
       "pmopm2AlmChannel44BalancedPortn": pmopm2AlmChannel44BalancedPortn,
       "pmopm2AlmChannel44PowerLowPortn": pmopm2AlmChannel44PowerLowPortn,
       "pmopm2AlmChannel44PowerHighPortn": pmopm2AlmChannel44PowerHighPortn,
       "pmopm2AlmChannel44OosPortn": pmopm2AlmChannel44OosPortn,
       "pmopm2Almchannel45PortTable": pmopm2Almchannel45PortTable,
       "pmopm2Almchannel45PortEntry": pmopm2Almchannel45PortEntry,
       "pmopm2Almchannel45PortIndex": pmopm2Almchannel45PortIndex,
       "pmopm2AlmChannel45AbsentPortn": pmopm2AlmChannel45AbsentPortn,
       "pmopm2AlmChannel45MismatchPortn": pmopm2AlmChannel45MismatchPortn,
       "pmopm2AlmChannel45BalancedPortn": pmopm2AlmChannel45BalancedPortn,
       "pmopm2AlmChannel45PowerLowPortn": pmopm2AlmChannel45PowerLowPortn,
       "pmopm2AlmChannel45PowerHighPortn": pmopm2AlmChannel45PowerHighPortn,
       "pmopm2AlmChannel45OosPortn": pmopm2AlmChannel45OosPortn,
       "pmopm2Almchannel46PortTable": pmopm2Almchannel46PortTable,
       "pmopm2Almchannel46PortEntry": pmopm2Almchannel46PortEntry,
       "pmopm2Almchannel46PortIndex": pmopm2Almchannel46PortIndex,
       "pmopm2AlmChannel46AbsentPortn": pmopm2AlmChannel46AbsentPortn,
       "pmopm2AlmChannel46MismatchPortn": pmopm2AlmChannel46MismatchPortn,
       "pmopm2AlmChannel46BalancedPortn": pmopm2AlmChannel46BalancedPortn,
       "pmopm2AlmChannel46PowerLowPortn": pmopm2AlmChannel46PowerLowPortn,
       "pmopm2AlmChannel46PowerHighPortn": pmopm2AlmChannel46PowerHighPortn,
       "pmopm2AlmChannel46OosPortn": pmopm2AlmChannel46OosPortn,
       "pmopm2Almchannel47PortTable": pmopm2Almchannel47PortTable,
       "pmopm2Almchannel47PortEntry": pmopm2Almchannel47PortEntry,
       "pmopm2Almchannel47PortIndex": pmopm2Almchannel47PortIndex,
       "pmopm2AlmChannel47AbsentPortn": pmopm2AlmChannel47AbsentPortn,
       "pmopm2AlmChannel47MismatchPortn": pmopm2AlmChannel47MismatchPortn,
       "pmopm2AlmChannel47BalancedPortn": pmopm2AlmChannel47BalancedPortn,
       "pmopm2AlmChannel47PowerLowPortn": pmopm2AlmChannel47PowerLowPortn,
       "pmopm2AlmChannel47PowerHighPortn": pmopm2AlmChannel47PowerHighPortn,
       "pmopm2AlmChannel47OosPortn": pmopm2AlmChannel47OosPortn,
       "pmopm2Almchannel48PortTable": pmopm2Almchannel48PortTable,
       "pmopm2Almchannel48PortEntry": pmopm2Almchannel48PortEntry,
       "pmopm2Almchannel48PortIndex": pmopm2Almchannel48PortIndex,
       "pmopm2AlmChannel48AbsentPortn": pmopm2AlmChannel48AbsentPortn,
       "pmopm2AlmChannel48MismatchPortn": pmopm2AlmChannel48MismatchPortn,
       "pmopm2AlmChannel48BalancedPortn": pmopm2AlmChannel48BalancedPortn,
       "pmopm2AlmChannel48PowerLowPortn": pmopm2AlmChannel48PowerLowPortn,
       "pmopm2AlmChannel48PowerHighPortn": pmopm2AlmChannel48PowerHighPortn,
       "pmopm2AlmChannel48OosPortn": pmopm2AlmChannel48OosPortn,
       "pmopm2Almchannel49PortTable": pmopm2Almchannel49PortTable,
       "pmopm2Almchannel49PortEntry": pmopm2Almchannel49PortEntry,
       "pmopm2Almchannel49PortIndex": pmopm2Almchannel49PortIndex,
       "pmopm2AlmChannel49AbsentPortn": pmopm2AlmChannel49AbsentPortn,
       "pmopm2AlmChannel49MismatchPortn": pmopm2AlmChannel49MismatchPortn,
       "pmopm2AlmChannel49BalancedPortn": pmopm2AlmChannel49BalancedPortn,
       "pmopm2AlmChannel49PowerLowPortn": pmopm2AlmChannel49PowerLowPortn,
       "pmopm2AlmChannel49PowerHighPortn": pmopm2AlmChannel49PowerHighPortn,
       "pmopm2AlmChannel49OosPortn": pmopm2AlmChannel49OosPortn,
       "pmopm2Almchannel50PortTable": pmopm2Almchannel50PortTable,
       "pmopm2Almchannel50PortEntry": pmopm2Almchannel50PortEntry,
       "pmopm2Almchannel50PortIndex": pmopm2Almchannel50PortIndex,
       "pmopm2AlmChannel50AbsentPortn": pmopm2AlmChannel50AbsentPortn,
       "pmopm2AlmChannel50MismatchPortn": pmopm2AlmChannel50MismatchPortn,
       "pmopm2AlmChannel50BalancedPortn": pmopm2AlmChannel50BalancedPortn,
       "pmopm2AlmChannel50PowerLowPortn": pmopm2AlmChannel50PowerLowPortn,
       "pmopm2AlmChannel50PowerHighPortn": pmopm2AlmChannel50PowerHighPortn,
       "pmopm2AlmChannel50OosPortn": pmopm2AlmChannel50OosPortn,
       "pmopm2Almchannel51PortTable": pmopm2Almchannel51PortTable,
       "pmopm2Almchannel51PortEntry": pmopm2Almchannel51PortEntry,
       "pmopm2Almchannel51PortIndex": pmopm2Almchannel51PortIndex,
       "pmopm2AlmChannel51AbsentPortn": pmopm2AlmChannel51AbsentPortn,
       "pmopm2AlmChannel51MismatchPortn": pmopm2AlmChannel51MismatchPortn,
       "pmopm2AlmChannel51BalancedPortn": pmopm2AlmChannel51BalancedPortn,
       "pmopm2AlmChannel51PowerLowPortn": pmopm2AlmChannel51PowerLowPortn,
       "pmopm2AlmChannel51PowerHighPortn": pmopm2AlmChannel51PowerHighPortn,
       "pmopm2AlmChannel51OosPortn": pmopm2AlmChannel51OosPortn,
       "pmopm2Almchannel52PortTable": pmopm2Almchannel52PortTable,
       "pmopm2Almchannel52PortEntry": pmopm2Almchannel52PortEntry,
       "pmopm2Almchannel52PortIndex": pmopm2Almchannel52PortIndex,
       "pmopm2AlmChannel52AbsentPortn": pmopm2AlmChannel52AbsentPortn,
       "pmopm2AlmChannel52MismatchPortn": pmopm2AlmChannel52MismatchPortn,
       "pmopm2AlmChannel52BalancedPortn": pmopm2AlmChannel52BalancedPortn,
       "pmopm2AlmChannel52PowerLowPortn": pmopm2AlmChannel52PowerLowPortn,
       "pmopm2AlmChannel52PowerHighPortn": pmopm2AlmChannel52PowerHighPortn,
       "pmopm2AlmChannel52OosPortn": pmopm2AlmChannel52OosPortn,
       "pmopm2Almchannel53PortTable": pmopm2Almchannel53PortTable,
       "pmopm2Almchannel53PortEntry": pmopm2Almchannel53PortEntry,
       "pmopm2Almchannel53PortIndex": pmopm2Almchannel53PortIndex,
       "pmopm2AlmChannel53AbsentPortn": pmopm2AlmChannel53AbsentPortn,
       "pmopm2AlmChannel53MismatchPortn": pmopm2AlmChannel53MismatchPortn,
       "pmopm2AlmChannel53BalancedPortn": pmopm2AlmChannel53BalancedPortn,
       "pmopm2AlmChannel53PowerLowPortn": pmopm2AlmChannel53PowerLowPortn,
       "pmopm2AlmChannel53PowerHighPortn": pmopm2AlmChannel53PowerHighPortn,
       "pmopm2AlmChannel53OosPortn": pmopm2AlmChannel53OosPortn,
       "pmopm2Almchannel54PortTable": pmopm2Almchannel54PortTable,
       "pmopm2Almchannel54PortEntry": pmopm2Almchannel54PortEntry,
       "pmopm2Almchannel54PortIndex": pmopm2Almchannel54PortIndex,
       "pmopm2AlmChannel54AbsentPortn": pmopm2AlmChannel54AbsentPortn,
       "pmopm2AlmChannel54MismatchPortn": pmopm2AlmChannel54MismatchPortn,
       "pmopm2AlmChannel54BalancedPortn": pmopm2AlmChannel54BalancedPortn,
       "pmopm2AlmChannel54PowerLowPortn": pmopm2AlmChannel54PowerLowPortn,
       "pmopm2AlmChannel54PowerHighPortn": pmopm2AlmChannel54PowerHighPortn,
       "pmopm2AlmChannel54OosPortn": pmopm2AlmChannel54OosPortn,
       "pmopm2Almchannel55PortTable": pmopm2Almchannel55PortTable,
       "pmopm2Almchannel55PortEntry": pmopm2Almchannel55PortEntry,
       "pmopm2Almchannel55PortIndex": pmopm2Almchannel55PortIndex,
       "pmopm2AlmChannel55AbsentPortn": pmopm2AlmChannel55AbsentPortn,
       "pmopm2AlmChannel55MismatchPortn": pmopm2AlmChannel55MismatchPortn,
       "pmopm2AlmChannel55BalancedPortn": pmopm2AlmChannel55BalancedPortn,
       "pmopm2AlmChannel55PowerLowPortn": pmopm2AlmChannel55PowerLowPortn,
       "pmopm2AlmChannel55PowerHighPortn": pmopm2AlmChannel55PowerHighPortn,
       "pmopm2AlmChannel55OosPortn": pmopm2AlmChannel55OosPortn,
       "pmopm2Almchannel56PortTable": pmopm2Almchannel56PortTable,
       "pmopm2Almchannel56PortEntry": pmopm2Almchannel56PortEntry,
       "pmopm2Almchannel56PortIndex": pmopm2Almchannel56PortIndex,
       "pmopm2AlmChannel56AbsentPortn": pmopm2AlmChannel56AbsentPortn,
       "pmopm2AlmChannel56MismatchPortn": pmopm2AlmChannel56MismatchPortn,
       "pmopm2AlmChannel56BalancedPortn": pmopm2AlmChannel56BalancedPortn,
       "pmopm2AlmChannel56PowerLowPortn": pmopm2AlmChannel56PowerLowPortn,
       "pmopm2AlmChannel56PowerHighPortn": pmopm2AlmChannel56PowerHighPortn,
       "pmopm2AlmChannel56OosPortn": pmopm2AlmChannel56OosPortn,
       "pmopm2Almchannel57PortTable": pmopm2Almchannel57PortTable,
       "pmopm2Almchannel57PortEntry": pmopm2Almchannel57PortEntry,
       "pmopm2Almchannel57PortIndex": pmopm2Almchannel57PortIndex,
       "pmopm2AlmChannel57AbsentPortn": pmopm2AlmChannel57AbsentPortn,
       "pmopm2AlmChannel57MismatchPortn": pmopm2AlmChannel57MismatchPortn,
       "pmopm2AlmChannel57BalancedPortn": pmopm2AlmChannel57BalancedPortn,
       "pmopm2AlmChannel57PowerLowPortn": pmopm2AlmChannel57PowerLowPortn,
       "pmopm2AlmChannel57PowerHighPortn": pmopm2AlmChannel57PowerHighPortn,
       "pmopm2AlmChannel57OosPortn": pmopm2AlmChannel57OosPortn,
       "pmopm2Almchannel58PortTable": pmopm2Almchannel58PortTable,
       "pmopm2Almchannel58PortEntry": pmopm2Almchannel58PortEntry,
       "pmopm2Almchannel58PortIndex": pmopm2Almchannel58PortIndex,
       "pmopm2AlmChannel58AbsentPortn": pmopm2AlmChannel58AbsentPortn,
       "pmopm2AlmChannel58MismatchPortn": pmopm2AlmChannel58MismatchPortn,
       "pmopm2AlmChannel58BalancedPortn": pmopm2AlmChannel58BalancedPortn,
       "pmopm2AlmChannel58PowerLowPortn": pmopm2AlmChannel58PowerLowPortn,
       "pmopm2AlmChannel58PowerHighPortn": pmopm2AlmChannel58PowerHighPortn,
       "pmopm2AlmChannel58OosPortn": pmopm2AlmChannel58OosPortn,
       "pmopm2Almchannel59PortTable": pmopm2Almchannel59PortTable,
       "pmopm2Almchannel59PortEntry": pmopm2Almchannel59PortEntry,
       "pmopm2Almchannel59PortIndex": pmopm2Almchannel59PortIndex,
       "pmopm2AlmChannel59AbsentPortn": pmopm2AlmChannel59AbsentPortn,
       "pmopm2AlmChannel59MismatchPortn": pmopm2AlmChannel59MismatchPortn,
       "pmopm2AlmChannel59BalancedPortn": pmopm2AlmChannel59BalancedPortn,
       "pmopm2AlmChannel59PowerLowPortn": pmopm2AlmChannel59PowerLowPortn,
       "pmopm2AlmChannel59PowerHighPortn": pmopm2AlmChannel59PowerHighPortn,
       "pmopm2AlmChannel59OosPortn": pmopm2AlmChannel59OosPortn,
       "pmopm2Almchannel60PortTable": pmopm2Almchannel60PortTable,
       "pmopm2Almchannel60PortEntry": pmopm2Almchannel60PortEntry,
       "pmopm2Almchannel60PortIndex": pmopm2Almchannel60PortIndex,
       "pmopm2AlmChannel60AbsentPortn": pmopm2AlmChannel60AbsentPortn,
       "pmopm2AlmChannel60MismatchPortn": pmopm2AlmChannel60MismatchPortn,
       "pmopm2AlmChannel60BalancedPortn": pmopm2AlmChannel60BalancedPortn,
       "pmopm2AlmChannel60PowerLowPortn": pmopm2AlmChannel60PowerLowPortn,
       "pmopm2AlmChannel60PowerHighPortn": pmopm2AlmChannel60PowerHighPortn,
       "pmopm2AlmChannel60OosPortn": pmopm2AlmChannel60OosPortn,
       "pmopm2Almchannel61PortTable": pmopm2Almchannel61PortTable,
       "pmopm2Almchannel61PortEntry": pmopm2Almchannel61PortEntry,
       "pmopm2Almchannel61PortIndex": pmopm2Almchannel61PortIndex,
       "pmopm2AlmChannel61AbsentPortn": pmopm2AlmChannel61AbsentPortn,
       "pmopm2AlmChannel61MismatchPortn": pmopm2AlmChannel61MismatchPortn,
       "pmopm2AlmChannel61BalancedPortn": pmopm2AlmChannel61BalancedPortn,
       "pmopm2AlmChannel61PowerLowPortn": pmopm2AlmChannel61PowerLowPortn,
       "pmopm2AlmChannel61PowerHighPortn": pmopm2AlmChannel61PowerHighPortn,
       "pmopm2AlmChannel61OosPortn": pmopm2AlmChannel61OosPortn,
       "pmopm2Almchannel62PortTable": pmopm2Almchannel62PortTable,
       "pmopm2Almchannel62PortEntry": pmopm2Almchannel62PortEntry,
       "pmopm2Almchannel62PortIndex": pmopm2Almchannel62PortIndex,
       "pmopm2AlmChannel62AbsentPortn": pmopm2AlmChannel62AbsentPortn,
       "pmopm2AlmChannel62MismatchPortn": pmopm2AlmChannel62MismatchPortn,
       "pmopm2AlmChannel62BalancedPortn": pmopm2AlmChannel62BalancedPortn,
       "pmopm2AlmChannel62PowerLowPortn": pmopm2AlmChannel62PowerLowPortn,
       "pmopm2AlmChannel62PowerHighPortn": pmopm2AlmChannel62PowerHighPortn,
       "pmopm2AlmChannel62OosPortn": pmopm2AlmChannel62OosPortn,
       "pmopm2Almchannel63PortTable": pmopm2Almchannel63PortTable,
       "pmopm2Almchannel63PortEntry": pmopm2Almchannel63PortEntry,
       "pmopm2Almchannel63PortIndex": pmopm2Almchannel63PortIndex,
       "pmopm2AlmChannel63AbsentPortn": pmopm2AlmChannel63AbsentPortn,
       "pmopm2AlmChannel63MismatchPortn": pmopm2AlmChannel63MismatchPortn,
       "pmopm2AlmChannel63BalancedPortn": pmopm2AlmChannel63BalancedPortn,
       "pmopm2AlmChannel63PowerLowPortn": pmopm2AlmChannel63PowerLowPortn,
       "pmopm2AlmChannel63PowerHighPortn": pmopm2AlmChannel63PowerHighPortn,
       "pmopm2AlmChannel63OosPortn": pmopm2AlmChannel63OosPortn,
       "pmopm2Almchannel64PortTable": pmopm2Almchannel64PortTable,
       "pmopm2Almchannel64PortEntry": pmopm2Almchannel64PortEntry,
       "pmopm2Almchannel64PortIndex": pmopm2Almchannel64PortIndex,
       "pmopm2AlmChannel64AbsentPortn": pmopm2AlmChannel64AbsentPortn,
       "pmopm2AlmChannel64MismatchPortn": pmopm2AlmChannel64MismatchPortn,
       "pmopm2AlmChannel64BalancedPortn": pmopm2AlmChannel64BalancedPortn,
       "pmopm2AlmChannel64PowerLowPortn": pmopm2AlmChannel64PowerLowPortn,
       "pmopm2AlmChannel64PowerHighPortn": pmopm2AlmChannel64PowerHighPortn,
       "pmopm2AlmChannel64OosPortn": pmopm2AlmChannel64OosPortn,
       "pmopm2Almchannel65PortTable": pmopm2Almchannel65PortTable,
       "pmopm2Almchannel65PortEntry": pmopm2Almchannel65PortEntry,
       "pmopm2Almchannel65PortIndex": pmopm2Almchannel65PortIndex,
       "pmopm2AlmChannel65AbsentPortn": pmopm2AlmChannel65AbsentPortn,
       "pmopm2AlmChannel65MismatchPortn": pmopm2AlmChannel65MismatchPortn,
       "pmopm2AlmChannel65BalancedPortn": pmopm2AlmChannel65BalancedPortn,
       "pmopm2AlmChannel65PowerLowPortn": pmopm2AlmChannel65PowerLowPortn,
       "pmopm2AlmChannel65PowerHighPortn": pmopm2AlmChannel65PowerHighPortn,
       "pmopm2AlmChannel65OosPortn": pmopm2AlmChannel65OosPortn,
       "pmopm2Almchannel66PortTable": pmopm2Almchannel66PortTable,
       "pmopm2Almchannel66PortEntry": pmopm2Almchannel66PortEntry,
       "pmopm2Almchannel66PortIndex": pmopm2Almchannel66PortIndex,
       "pmopm2AlmChannel66AbsentPortn": pmopm2AlmChannel66AbsentPortn,
       "pmopm2AlmChannel66MismatchPortn": pmopm2AlmChannel66MismatchPortn,
       "pmopm2AlmChannel66BalancedPortn": pmopm2AlmChannel66BalancedPortn,
       "pmopm2AlmChannel66PowerLowPortn": pmopm2AlmChannel66PowerLowPortn,
       "pmopm2AlmChannel66PowerHighPortn": pmopm2AlmChannel66PowerHighPortn,
       "pmopm2AlmChannel66OosPortn": pmopm2AlmChannel66OosPortn,
       "pmopm2Almchannel67PortTable": pmopm2Almchannel67PortTable,
       "pmopm2Almchannel67PortEntry": pmopm2Almchannel67PortEntry,
       "pmopm2Almchannel67PortIndex": pmopm2Almchannel67PortIndex,
       "pmopm2AlmChannel67AbsentPortn": pmopm2AlmChannel67AbsentPortn,
       "pmopm2AlmChannel67MismatchPortn": pmopm2AlmChannel67MismatchPortn,
       "pmopm2AlmChannel67BalancedPortn": pmopm2AlmChannel67BalancedPortn,
       "pmopm2AlmChannel67PowerLowPortn": pmopm2AlmChannel67PowerLowPortn,
       "pmopm2AlmChannel67PowerHighPortn": pmopm2AlmChannel67PowerHighPortn,
       "pmopm2AlmChannel67OosPortn": pmopm2AlmChannel67OosPortn,
       "pmopm2Almchannel68PortTable": pmopm2Almchannel68PortTable,
       "pmopm2Almchannel68PortEntry": pmopm2Almchannel68PortEntry,
       "pmopm2Almchannel68PortIndex": pmopm2Almchannel68PortIndex,
       "pmopm2AlmChannel68AbsentPortn": pmopm2AlmChannel68AbsentPortn,
       "pmopm2AlmChannel68MismatchPortn": pmopm2AlmChannel68MismatchPortn,
       "pmopm2AlmChannel68BalancedPortn": pmopm2AlmChannel68BalancedPortn,
       "pmopm2AlmChannel68PowerLowPortn": pmopm2AlmChannel68PowerLowPortn,
       "pmopm2AlmChannel68PowerHighPortn": pmopm2AlmChannel68PowerHighPortn,
       "pmopm2AlmChannel68OosPortn": pmopm2AlmChannel68OosPortn,
       "pmopm2Almchannel69PortTable": pmopm2Almchannel69PortTable,
       "pmopm2Almchannel69PortEntry": pmopm2Almchannel69PortEntry,
       "pmopm2Almchannel69PortIndex": pmopm2Almchannel69PortIndex,
       "pmopm2AlmChannel69AbsentPortn": pmopm2AlmChannel69AbsentPortn,
       "pmopm2AlmChannel69MismatchPortn": pmopm2AlmChannel69MismatchPortn,
       "pmopm2AlmChannel69BalancedPortn": pmopm2AlmChannel69BalancedPortn,
       "pmopm2AlmChannel69PowerLowPortn": pmopm2AlmChannel69PowerLowPortn,
       "pmopm2AlmChannel69PowerHighPortn": pmopm2AlmChannel69PowerHighPortn,
       "pmopm2AlmChannel69OosPortn": pmopm2AlmChannel69OosPortn,
       "pmopm2Almchannel70PortTable": pmopm2Almchannel70PortTable,
       "pmopm2Almchannel70PortEntry": pmopm2Almchannel70PortEntry,
       "pmopm2Almchannel70PortIndex": pmopm2Almchannel70PortIndex,
       "pmopm2AlmChannel70AbsentPortn": pmopm2AlmChannel70AbsentPortn,
       "pmopm2AlmChannel70MismatchPortn": pmopm2AlmChannel70MismatchPortn,
       "pmopm2AlmChannel70BalancedPortn": pmopm2AlmChannel70BalancedPortn,
       "pmopm2AlmChannel70PowerLowPortn": pmopm2AlmChannel70PowerLowPortn,
       "pmopm2AlmChannel70PowerHighPortn": pmopm2AlmChannel70PowerHighPortn,
       "pmopm2AlmChannel70OosPortn": pmopm2AlmChannel70OosPortn,
       "pmopm2Almchannel71PortTable": pmopm2Almchannel71PortTable,
       "pmopm2Almchannel71PortEntry": pmopm2Almchannel71PortEntry,
       "pmopm2Almchannel71PortIndex": pmopm2Almchannel71PortIndex,
       "pmopm2AlmChannel71AbsentPortn": pmopm2AlmChannel71AbsentPortn,
       "pmopm2AlmChannel71MismatchPortn": pmopm2AlmChannel71MismatchPortn,
       "pmopm2AlmChannel71BalancedPortn": pmopm2AlmChannel71BalancedPortn,
       "pmopm2AlmChannel71PowerLowPortn": pmopm2AlmChannel71PowerLowPortn,
       "pmopm2AlmChannel71PowerHighPortn": pmopm2AlmChannel71PowerHighPortn,
       "pmopm2AlmChannel71OosPortn": pmopm2AlmChannel71OosPortn,
       "pmopm2Almchannel72PortTable": pmopm2Almchannel72PortTable,
       "pmopm2Almchannel72PortEntry": pmopm2Almchannel72PortEntry,
       "pmopm2Almchannel72PortIndex": pmopm2Almchannel72PortIndex,
       "pmopm2AlmChannel72AbsentPortn": pmopm2AlmChannel72AbsentPortn,
       "pmopm2AlmChannel72MismatchPortn": pmopm2AlmChannel72MismatchPortn,
       "pmopm2AlmChannel72BalancedPortn": pmopm2AlmChannel72BalancedPortn,
       "pmopm2AlmChannel72PowerLowPortn": pmopm2AlmChannel72PowerLowPortn,
       "pmopm2AlmChannel72PowerHighPortn": pmopm2AlmChannel72PowerHighPortn,
       "pmopm2AlmChannel72OosPortn": pmopm2AlmChannel72OosPortn,
       "pmopm2Almchannel73PortTable": pmopm2Almchannel73PortTable,
       "pmopm2Almchannel73PortEntry": pmopm2Almchannel73PortEntry,
       "pmopm2Almchannel73PortIndex": pmopm2Almchannel73PortIndex,
       "pmopm2AlmChannel73AbsentPortn": pmopm2AlmChannel73AbsentPortn,
       "pmopm2AlmChannel73MismatchPortn": pmopm2AlmChannel73MismatchPortn,
       "pmopm2AlmChannel73BalancedPortn": pmopm2AlmChannel73BalancedPortn,
       "pmopm2AlmChannel73PowerLowPortn": pmopm2AlmChannel73PowerLowPortn,
       "pmopm2AlmChannel73PowerHighPortn": pmopm2AlmChannel73PowerHighPortn,
       "pmopm2AlmChannel73OosPortn": pmopm2AlmChannel73OosPortn,
       "pmopm2Almchannel74PortTable": pmopm2Almchannel74PortTable,
       "pmopm2Almchannel74PortEntry": pmopm2Almchannel74PortEntry,
       "pmopm2Almchannel74PortIndex": pmopm2Almchannel74PortIndex,
       "pmopm2AlmChannel74AbsentPortn": pmopm2AlmChannel74AbsentPortn,
       "pmopm2AlmChannel74MismatchPortn": pmopm2AlmChannel74MismatchPortn,
       "pmopm2AlmChannel74BalancedPortn": pmopm2AlmChannel74BalancedPortn,
       "pmopm2AlmChannel74PowerLowPortn": pmopm2AlmChannel74PowerLowPortn,
       "pmopm2AlmChannel74PowerHighPortn": pmopm2AlmChannel74PowerHighPortn,
       "pmopm2AlmChannel74OosPortn": pmopm2AlmChannel74OosPortn,
       "pmopm2Almchannel75PortTable": pmopm2Almchannel75PortTable,
       "pmopm2Almchannel75PortEntry": pmopm2Almchannel75PortEntry,
       "pmopm2Almchannel75PortIndex": pmopm2Almchannel75PortIndex,
       "pmopm2AlmChannel75AbsentPortn": pmopm2AlmChannel75AbsentPortn,
       "pmopm2AlmChannel75MismatchPortn": pmopm2AlmChannel75MismatchPortn,
       "pmopm2AlmChannel75BalancedPortn": pmopm2AlmChannel75BalancedPortn,
       "pmopm2AlmChannel75PowerLowPortn": pmopm2AlmChannel75PowerLowPortn,
       "pmopm2AlmChannel75PowerHighPortn": pmopm2AlmChannel75PowerHighPortn,
       "pmopm2AlmChannel75OosPortn": pmopm2AlmChannel75OosPortn,
       "pmopm2Almchannel76PortTable": pmopm2Almchannel76PortTable,
       "pmopm2Almchannel76PortEntry": pmopm2Almchannel76PortEntry,
       "pmopm2Almchannel76PortIndex": pmopm2Almchannel76PortIndex,
       "pmopm2AlmChannel76AbsentPortn": pmopm2AlmChannel76AbsentPortn,
       "pmopm2AlmChannel76MismatchPortn": pmopm2AlmChannel76MismatchPortn,
       "pmopm2AlmChannel76BalancedPortn": pmopm2AlmChannel76BalancedPortn,
       "pmopm2AlmChannel76PowerLowPortn": pmopm2AlmChannel76PowerLowPortn,
       "pmopm2AlmChannel76PowerHighPortn": pmopm2AlmChannel76PowerHighPortn,
       "pmopm2AlmChannel76OosPortn": pmopm2AlmChannel76OosPortn,
       "pmopm2Almchannel77PortTable": pmopm2Almchannel77PortTable,
       "pmopm2Almchannel77PortEntry": pmopm2Almchannel77PortEntry,
       "pmopm2Almchannel77PortIndex": pmopm2Almchannel77PortIndex,
       "pmopm2AlmChannel77AbsentPortn": pmopm2AlmChannel77AbsentPortn,
       "pmopm2AlmChannel77MismatchPortn": pmopm2AlmChannel77MismatchPortn,
       "pmopm2AlmChannel77BalancedPortn": pmopm2AlmChannel77BalancedPortn,
       "pmopm2AlmChannel77PowerLowPortn": pmopm2AlmChannel77PowerLowPortn,
       "pmopm2AlmChannel77PowerHighPortn": pmopm2AlmChannel77PowerHighPortn,
       "pmopm2AlmChannel77OosPortn": pmopm2AlmChannel77OosPortn,
       "pmopm2Almchannel78PortTable": pmopm2Almchannel78PortTable,
       "pmopm2Almchannel78PortEntry": pmopm2Almchannel78PortEntry,
       "pmopm2Almchannel78PortIndex": pmopm2Almchannel78PortIndex,
       "pmopm2AlmChannel78AbsentPortn": pmopm2AlmChannel78AbsentPortn,
       "pmopm2AlmChannel78MismatchPortn": pmopm2AlmChannel78MismatchPortn,
       "pmopm2AlmChannel78BalancedPortn": pmopm2AlmChannel78BalancedPortn,
       "pmopm2AlmChannel78PowerLowPortn": pmopm2AlmChannel78PowerLowPortn,
       "pmopm2AlmChannel78PowerHighPortn": pmopm2AlmChannel78PowerHighPortn,
       "pmopm2AlmChannel78OosPortn": pmopm2AlmChannel78OosPortn,
       "pmopm2Almchannel79PortTable": pmopm2Almchannel79PortTable,
       "pmopm2Almchannel79PortEntry": pmopm2Almchannel79PortEntry,
       "pmopm2Almchannel79PortIndex": pmopm2Almchannel79PortIndex,
       "pmopm2AlmChannel79AbsentPortn": pmopm2AlmChannel79AbsentPortn,
       "pmopm2AlmChannel79MismatchPortn": pmopm2AlmChannel79MismatchPortn,
       "pmopm2AlmChannel79BalancedPortn": pmopm2AlmChannel79BalancedPortn,
       "pmopm2AlmChannel79PowerLowPortn": pmopm2AlmChannel79PowerLowPortn,
       "pmopm2AlmChannel79PowerHighPortn": pmopm2AlmChannel79PowerHighPortn,
       "pmopm2AlmChannel79OosPortn": pmopm2AlmChannel79OosPortn,
       "pmopm2Almchannel80PortTable": pmopm2Almchannel80PortTable,
       "pmopm2Almchannel80PortEntry": pmopm2Almchannel80PortEntry,
       "pmopm2Almchannel80PortIndex": pmopm2Almchannel80PortIndex,
       "pmopm2AlmChannel80AbsentPortn": pmopm2AlmChannel80AbsentPortn,
       "pmopm2AlmChannel80MismatchPortn": pmopm2AlmChannel80MismatchPortn,
       "pmopm2AlmChannel80BalancedPortn": pmopm2AlmChannel80BalancedPortn,
       "pmopm2AlmChannel80PowerLowPortn": pmopm2AlmChannel80PowerLowPortn,
       "pmopm2AlmChannel80PowerHighPortn": pmopm2AlmChannel80PowerHighPortn,
       "pmopm2AlmChannel80OosPortn": pmopm2AlmChannel80OosPortn,
       "pmopm2Almchannel81PortTable": pmopm2Almchannel81PortTable,
       "pmopm2Almchannel81PortEntry": pmopm2Almchannel81PortEntry,
       "pmopm2Almchannel81PortIndex": pmopm2Almchannel81PortIndex,
       "pmopm2AlmChannel81AbsentPortn": pmopm2AlmChannel81AbsentPortn,
       "pmopm2AlmChannel81MismatchPortn": pmopm2AlmChannel81MismatchPortn,
       "pmopm2AlmChannel81BalancedPortn": pmopm2AlmChannel81BalancedPortn,
       "pmopm2AlmChannel81PowerLowPortn": pmopm2AlmChannel81PowerLowPortn,
       "pmopm2AlmChannel81PowerHighPortn": pmopm2AlmChannel81PowerHighPortn,
       "pmopm2AlmChannel81OosPortn": pmopm2AlmChannel81OosPortn,
       "pmopm2Almchannel82PortTable": pmopm2Almchannel82PortTable,
       "pmopm2Almchannel82PortEntry": pmopm2Almchannel82PortEntry,
       "pmopm2Almchannel82PortIndex": pmopm2Almchannel82PortIndex,
       "pmopm2AlmChannel82AbsentPortn": pmopm2AlmChannel82AbsentPortn,
       "pmopm2AlmChannel82MismatchPortn": pmopm2AlmChannel82MismatchPortn,
       "pmopm2AlmChannel82BalancedPortn": pmopm2AlmChannel82BalancedPortn,
       "pmopm2AlmChannel82PowerLowPortn": pmopm2AlmChannel82PowerLowPortn,
       "pmopm2AlmChannel82PowerHighPortn": pmopm2AlmChannel82PowerHighPortn,
       "pmopm2AlmChannel82OosPortn": pmopm2AlmChannel82OosPortn,
       "pmopm2Almchannel83PortTable": pmopm2Almchannel83PortTable,
       "pmopm2Almchannel83PortEntry": pmopm2Almchannel83PortEntry,
       "pmopm2Almchannel83PortIndex": pmopm2Almchannel83PortIndex,
       "pmopm2AlmChannel83AbsentPortn": pmopm2AlmChannel83AbsentPortn,
       "pmopm2AlmChannel83MismatchPortn": pmopm2AlmChannel83MismatchPortn,
       "pmopm2AlmChannel83BalancedPortn": pmopm2AlmChannel83BalancedPortn,
       "pmopm2AlmChannel83PowerLowPortn": pmopm2AlmChannel83PowerLowPortn,
       "pmopm2AlmChannel83PowerHighPortn": pmopm2AlmChannel83PowerHighPortn,
       "pmopm2AlmChannel83OosPortn": pmopm2AlmChannel83OosPortn,
       "pmopm2Almchannel84PortTable": pmopm2Almchannel84PortTable,
       "pmopm2Almchannel84PortEntry": pmopm2Almchannel84PortEntry,
       "pmopm2Almchannel84PortIndex": pmopm2Almchannel84PortIndex,
       "pmopm2AlmChannel84AbsentPortn": pmopm2AlmChannel84AbsentPortn,
       "pmopm2AlmChannel84MismatchPortn": pmopm2AlmChannel84MismatchPortn,
       "pmopm2AlmChannel84BalancedPortn": pmopm2AlmChannel84BalancedPortn,
       "pmopm2AlmChannel84PowerLowPortn": pmopm2AlmChannel84PowerLowPortn,
       "pmopm2AlmChannel84PowerHighPortn": pmopm2AlmChannel84PowerHighPortn,
       "pmopm2AlmChannel84OosPortn": pmopm2AlmChannel84OosPortn,
       "pmopm2Almchannel85PortTable": pmopm2Almchannel85PortTable,
       "pmopm2Almchannel85PortEntry": pmopm2Almchannel85PortEntry,
       "pmopm2Almchannel85PortIndex": pmopm2Almchannel85PortIndex,
       "pmopm2AlmChannel85AbsentPortn": pmopm2AlmChannel85AbsentPortn,
       "pmopm2AlmChannel85MismatchPortn": pmopm2AlmChannel85MismatchPortn,
       "pmopm2AlmChannel85BalancedPortn": pmopm2AlmChannel85BalancedPortn,
       "pmopm2AlmChannel85PowerLowPortn": pmopm2AlmChannel85PowerLowPortn,
       "pmopm2AlmChannel85PowerHighPortn": pmopm2AlmChannel85PowerHighPortn,
       "pmopm2AlmChannel85OosPortn": pmopm2AlmChannel85OosPortn,
       "pmopm2Almchannel86PortTable": pmopm2Almchannel86PortTable,
       "pmopm2Almchannel86PortEntry": pmopm2Almchannel86PortEntry,
       "pmopm2Almchannel86PortIndex": pmopm2Almchannel86PortIndex,
       "pmopm2AlmChannel86AbsentPortn": pmopm2AlmChannel86AbsentPortn,
       "pmopm2AlmChannel86MismatchPortn": pmopm2AlmChannel86MismatchPortn,
       "pmopm2AlmChannel86BalancedPortn": pmopm2AlmChannel86BalancedPortn,
       "pmopm2AlmChannel86PowerLowPortn": pmopm2AlmChannel86PowerLowPortn,
       "pmopm2AlmChannel86PowerHighPortn": pmopm2AlmChannel86PowerHighPortn,
       "pmopm2AlmChannel86OosPortn": pmopm2AlmChannel86OosPortn,
       "pmopm2Almchannel87PortTable": pmopm2Almchannel87PortTable,
       "pmopm2Almchannel87PortEntry": pmopm2Almchannel87PortEntry,
       "pmopm2Almchannel87PortIndex": pmopm2Almchannel87PortIndex,
       "pmopm2AlmChannel87AbsentPortn": pmopm2AlmChannel87AbsentPortn,
       "pmopm2AlmChannel87MismatchPortn": pmopm2AlmChannel87MismatchPortn,
       "pmopm2AlmChannel87BalancedPortn": pmopm2AlmChannel87BalancedPortn,
       "pmopm2AlmChannel87PowerLowPortn": pmopm2AlmChannel87PowerLowPortn,
       "pmopm2AlmChannel87PowerHighPortn": pmopm2AlmChannel87PowerHighPortn,
       "pmopm2AlmChannel87OosPortn": pmopm2AlmChannel87OosPortn,
       "pmopm2Almchannel88PortTable": pmopm2Almchannel88PortTable,
       "pmopm2Almchannel88PortEntry": pmopm2Almchannel88PortEntry,
       "pmopm2Almchannel88PortIndex": pmopm2Almchannel88PortIndex,
       "pmopm2AlmChannel88AbsentPortn": pmopm2AlmChannel88AbsentPortn,
       "pmopm2AlmChannel88MismatchPortn": pmopm2AlmChannel88MismatchPortn,
       "pmopm2AlmChannel88BalancedPortn": pmopm2AlmChannel88BalancedPortn,
       "pmopm2AlmChannel88PowerLowPortn": pmopm2AlmChannel88PowerLowPortn,
       "pmopm2AlmChannel88PowerHighPortn": pmopm2AlmChannel88PowerHighPortn,
       "pmopm2AlmChannel88OosPortn": pmopm2AlmChannel88OosPortn,
       "pmopm2Almchannel89PortTable": pmopm2Almchannel89PortTable,
       "pmopm2Almchannel89PortEntry": pmopm2Almchannel89PortEntry,
       "pmopm2Almchannel89PortIndex": pmopm2Almchannel89PortIndex,
       "pmopm2AlmChannel89AbsentPortn": pmopm2AlmChannel89AbsentPortn,
       "pmopm2AlmChannel89MismatchPortn": pmopm2AlmChannel89MismatchPortn,
       "pmopm2AlmChannel89BalancedPortn": pmopm2AlmChannel89BalancedPortn,
       "pmopm2AlmChannel89PowerLowPortn": pmopm2AlmChannel89PowerLowPortn,
       "pmopm2AlmChannel89PowerHighPortn": pmopm2AlmChannel89PowerHighPortn,
       "pmopm2AlmChannel89OosPortn": pmopm2AlmChannel89OosPortn,
       "pmopm2Almchannel90PortTable": pmopm2Almchannel90PortTable,
       "pmopm2Almchannel90PortEntry": pmopm2Almchannel90PortEntry,
       "pmopm2Almchannel90PortIndex": pmopm2Almchannel90PortIndex,
       "pmopm2AlmChannel90AbsentPortn": pmopm2AlmChannel90AbsentPortn,
       "pmopm2AlmChannel90MismatchPortn": pmopm2AlmChannel90MismatchPortn,
       "pmopm2AlmChannel90BalancedPortn": pmopm2AlmChannel90BalancedPortn,
       "pmopm2AlmChannel90PowerLowPortn": pmopm2AlmChannel90PowerLowPortn,
       "pmopm2AlmChannel90PowerHighPortn": pmopm2AlmChannel90PowerHighPortn,
       "pmopm2AlmChannel90OosPortn": pmopm2AlmChannel90OosPortn,
       "pmopm2Almchannel91PortTable": pmopm2Almchannel91PortTable,
       "pmopm2Almchannel91PortEntry": pmopm2Almchannel91PortEntry,
       "pmopm2Almchannel91PortIndex": pmopm2Almchannel91PortIndex,
       "pmopm2AlmChannel91AbsentPortn": pmopm2AlmChannel91AbsentPortn,
       "pmopm2AlmChannel91MismatchPortn": pmopm2AlmChannel91MismatchPortn,
       "pmopm2AlmChannel91BalancedPortn": pmopm2AlmChannel91BalancedPortn,
       "pmopm2AlmChannel91PowerLowPortn": pmopm2AlmChannel91PowerLowPortn,
       "pmopm2AlmChannel91PowerHighPortn": pmopm2AlmChannel91PowerHighPortn,
       "pmopm2AlmChannel91OosPortn": pmopm2AlmChannel91OosPortn,
       "pmopm2Almchannel92PortTable": pmopm2Almchannel92PortTable,
       "pmopm2Almchannel92PortEntry": pmopm2Almchannel92PortEntry,
       "pmopm2Almchannel92PortIndex": pmopm2Almchannel92PortIndex,
       "pmopm2AlmChannel92AbsentPortn": pmopm2AlmChannel92AbsentPortn,
       "pmopm2AlmChannel92MismatchPortn": pmopm2AlmChannel92MismatchPortn,
       "pmopm2AlmChannel92BalancedPortn": pmopm2AlmChannel92BalancedPortn,
       "pmopm2AlmChannel92PowerLowPortn": pmopm2AlmChannel92PowerLowPortn,
       "pmopm2AlmChannel92PowerHighPortn": pmopm2AlmChannel92PowerHighPortn,
       "pmopm2AlmChannel92OosPortn": pmopm2AlmChannel92OosPortn,
       "pmopm2Almchannel93PortTable": pmopm2Almchannel93PortTable,
       "pmopm2Almchannel93PortEntry": pmopm2Almchannel93PortEntry,
       "pmopm2Almchannel93PortIndex": pmopm2Almchannel93PortIndex,
       "pmopm2AlmChannel93AbsentPortn": pmopm2AlmChannel93AbsentPortn,
       "pmopm2AlmChannel93MismatchPortn": pmopm2AlmChannel93MismatchPortn,
       "pmopm2AlmChannel93BalancedPortn": pmopm2AlmChannel93BalancedPortn,
       "pmopm2AlmChannel93PowerLowPortn": pmopm2AlmChannel93PowerLowPortn,
       "pmopm2AlmChannel93PowerHighPortn": pmopm2AlmChannel93PowerHighPortn,
       "pmopm2AlmChannel93OosPortn": pmopm2AlmChannel93OosPortn,
       "pmopm2Almchannel94PortTable": pmopm2Almchannel94PortTable,
       "pmopm2Almchannel94PortEntry": pmopm2Almchannel94PortEntry,
       "pmopm2Almchannel94PortIndex": pmopm2Almchannel94PortIndex,
       "pmopm2AlmChannel94AbsentPortn": pmopm2AlmChannel94AbsentPortn,
       "pmopm2AlmChannel94MismatchPortn": pmopm2AlmChannel94MismatchPortn,
       "pmopm2AlmChannel94BalancedPortn": pmopm2AlmChannel94BalancedPortn,
       "pmopm2AlmChannel94PowerLowPortn": pmopm2AlmChannel94PowerLowPortn,
       "pmopm2AlmChannel94PowerHighPortn": pmopm2AlmChannel94PowerHighPortn,
       "pmopm2AlmChannel94OosPortn": pmopm2AlmChannel94OosPortn,
       "pmopm2Almchannel95PortTable": pmopm2Almchannel95PortTable,
       "pmopm2Almchannel95PortEntry": pmopm2Almchannel95PortEntry,
       "pmopm2Almchannel95PortIndex": pmopm2Almchannel95PortIndex,
       "pmopm2AlmChannel95AbsentPortn": pmopm2AlmChannel95AbsentPortn,
       "pmopm2AlmChannel95MismatchPortn": pmopm2AlmChannel95MismatchPortn,
       "pmopm2AlmChannel95BalancedPortn": pmopm2AlmChannel95BalancedPortn,
       "pmopm2AlmChannel95PowerLowPortn": pmopm2AlmChannel95PowerLowPortn,
       "pmopm2AlmChannel95PowerHighPortn": pmopm2AlmChannel95PowerHighPortn,
       "pmopm2AlmChannel95OosPortn": pmopm2AlmChannel95OosPortn,
       "pmopm2Almchannel96PortTable": pmopm2Almchannel96PortTable,
       "pmopm2Almchannel96PortEntry": pmopm2Almchannel96PortEntry,
       "pmopm2Almchannel96PortIndex": pmopm2Almchannel96PortIndex,
       "pmopm2AlmChannel96AbsentPortn": pmopm2AlmChannel96AbsentPortn,
       "pmopm2AlmChannel96MismatchPortn": pmopm2AlmChannel96MismatchPortn,
       "pmopm2AlmChannel96BalancedPortn": pmopm2AlmChannel96BalancedPortn,
       "pmopm2AlmChannel96PowerLowPortn": pmopm2AlmChannel96PowerLowPortn,
       "pmopm2AlmChannel96PowerHighPortn": pmopm2AlmChannel96PowerHighPortn,
       "pmopm2AlmChannel96OosPortn": pmopm2AlmChannel96OosPortn,
       "pmopm2AlmLine": pmopm2AlmLine,
       "pmopm2AlmLineNurg": pmopm2AlmLineNurg,
       "pmopm2AlmLineUrg": pmopm2AlmLineUrg,
       "pmopm2AlmLineCrit": pmopm2AlmLineCrit,
       "pmopm2measures": pmopm2measures,
       "pmopm2MesrOther": pmopm2MesrOther,
       "pmopm2MesropmTemp": pmopm2MesropmTemp,
       "pmopm2MesrClient": pmopm2MesrClient,
       "pmopm2Mesrchannel1Table": pmopm2Mesrchannel1Table,
       "pmopm2Mesrchannel1Entry": pmopm2Mesrchannel1Entry,
       "pmopm2Mesrchannel1Index": pmopm2Mesrchannel1Index,
       "pmopm2Mesrchannel1Portn": pmopm2Mesrchannel1Portn,
       "pmopm2Mesrchannel2Table": pmopm2Mesrchannel2Table,
       "pmopm2Mesrchannel2Entry": pmopm2Mesrchannel2Entry,
       "pmopm2Mesrchannel2Index": pmopm2Mesrchannel2Index,
       "pmopm2Mesrchannel2Portn": pmopm2Mesrchannel2Portn,
       "pmopm2Mesrchannel3Table": pmopm2Mesrchannel3Table,
       "pmopm2Mesrchannel3Entry": pmopm2Mesrchannel3Entry,
       "pmopm2Mesrchannel3Index": pmopm2Mesrchannel3Index,
       "pmopm2Mesrchannel3Portn": pmopm2Mesrchannel3Portn,
       "pmopm2Mesrchannel4Table": pmopm2Mesrchannel4Table,
       "pmopm2Mesrchannel4Entry": pmopm2Mesrchannel4Entry,
       "pmopm2Mesrchannel4Index": pmopm2Mesrchannel4Index,
       "pmopm2Mesrchannel4Portn": pmopm2Mesrchannel4Portn,
       "pmopm2Mesrchannel5Table": pmopm2Mesrchannel5Table,
       "pmopm2Mesrchannel5Entry": pmopm2Mesrchannel5Entry,
       "pmopm2Mesrchannel5Index": pmopm2Mesrchannel5Index,
       "pmopm2Mesrchannel5Portn": pmopm2Mesrchannel5Portn,
       "pmopm2Mesrchannel6Table": pmopm2Mesrchannel6Table,
       "pmopm2Mesrchannel6Entry": pmopm2Mesrchannel6Entry,
       "pmopm2Mesrchannel6Index": pmopm2Mesrchannel6Index,
       "pmopm2Mesrchannel6Portn": pmopm2Mesrchannel6Portn,
       "pmopm2Mesrchannel7Table": pmopm2Mesrchannel7Table,
       "pmopm2Mesrchannel7Entry": pmopm2Mesrchannel7Entry,
       "pmopm2Mesrchannel7Index": pmopm2Mesrchannel7Index,
       "pmopm2Mesrchannel7Portn": pmopm2Mesrchannel7Portn,
       "pmopm2Mesrchannel8Table": pmopm2Mesrchannel8Table,
       "pmopm2Mesrchannel8Entry": pmopm2Mesrchannel8Entry,
       "pmopm2Mesrchannel8Index": pmopm2Mesrchannel8Index,
       "pmopm2Mesrchannel8Portn": pmopm2Mesrchannel8Portn,
       "pmopm2Mesrchannel9Table": pmopm2Mesrchannel9Table,
       "pmopm2Mesrchannel9Entry": pmopm2Mesrchannel9Entry,
       "pmopm2Mesrchannel9Index": pmopm2Mesrchannel9Index,
       "pmopm2Mesrchannel9Portn": pmopm2Mesrchannel9Portn,
       "pmopm2Mesrchannel10Table": pmopm2Mesrchannel10Table,
       "pmopm2Mesrchannel10Entry": pmopm2Mesrchannel10Entry,
       "pmopm2Mesrchannel10Index": pmopm2Mesrchannel10Index,
       "pmopm2Mesrchannel10Portn": pmopm2Mesrchannel10Portn,
       "pmopm2Mesrchannel11Table": pmopm2Mesrchannel11Table,
       "pmopm2Mesrchannel11Entry": pmopm2Mesrchannel11Entry,
       "pmopm2Mesrchannel11Index": pmopm2Mesrchannel11Index,
       "pmopm2Mesrchannel11Portn": pmopm2Mesrchannel11Portn,
       "pmopm2Mesrchannel12Table": pmopm2Mesrchannel12Table,
       "pmopm2Mesrchannel12Entry": pmopm2Mesrchannel12Entry,
       "pmopm2Mesrchannel12Index": pmopm2Mesrchannel12Index,
       "pmopm2Mesrchannel12Portn": pmopm2Mesrchannel12Portn,
       "pmopm2Mesrchannel13Table": pmopm2Mesrchannel13Table,
       "pmopm2Mesrchannel13Entry": pmopm2Mesrchannel13Entry,
       "pmopm2Mesrchannel13Index": pmopm2Mesrchannel13Index,
       "pmopm2Mesrchannel13Portn": pmopm2Mesrchannel13Portn,
       "pmopm2Mesrchannel14Table": pmopm2Mesrchannel14Table,
       "pmopm2Mesrchannel14Entry": pmopm2Mesrchannel14Entry,
       "pmopm2Mesrchannel14Index": pmopm2Mesrchannel14Index,
       "pmopm2Mesrchannel14Portn": pmopm2Mesrchannel14Portn,
       "pmopm2Mesrchannel15Table": pmopm2Mesrchannel15Table,
       "pmopm2Mesrchannel15Entry": pmopm2Mesrchannel15Entry,
       "pmopm2Mesrchannel15Index": pmopm2Mesrchannel15Index,
       "pmopm2Mesrchannel15Portn": pmopm2Mesrchannel15Portn,
       "pmopm2Mesrchannel16Table": pmopm2Mesrchannel16Table,
       "pmopm2Mesrchannel16Entry": pmopm2Mesrchannel16Entry,
       "pmopm2Mesrchannel16Index": pmopm2Mesrchannel16Index,
       "pmopm2Mesrchannel16Portn": pmopm2Mesrchannel16Portn,
       "pmopm2Mesrchannel17Table": pmopm2Mesrchannel17Table,
       "pmopm2Mesrchannel17Entry": pmopm2Mesrchannel17Entry,
       "pmopm2Mesrchannel17Index": pmopm2Mesrchannel17Index,
       "pmopm2Mesrchannel17Portn": pmopm2Mesrchannel17Portn,
       "pmopm2Mesrchannel18Table": pmopm2Mesrchannel18Table,
       "pmopm2Mesrchannel18Entry": pmopm2Mesrchannel18Entry,
       "pmopm2Mesrchannel18Index": pmopm2Mesrchannel18Index,
       "pmopm2Mesrchannel18Portn": pmopm2Mesrchannel18Portn,
       "pmopm2Mesrchannel19Table": pmopm2Mesrchannel19Table,
       "pmopm2Mesrchannel19Entry": pmopm2Mesrchannel19Entry,
       "pmopm2Mesrchannel19Index": pmopm2Mesrchannel19Index,
       "pmopm2Mesrchannel19Portn": pmopm2Mesrchannel19Portn,
       "pmopm2Mesrchannel20Table": pmopm2Mesrchannel20Table,
       "pmopm2Mesrchannel20Entry": pmopm2Mesrchannel20Entry,
       "pmopm2Mesrchannel20Index": pmopm2Mesrchannel20Index,
       "pmopm2Mesrchannel20Portn": pmopm2Mesrchannel20Portn,
       "pmopm2Mesrchannel21Table": pmopm2Mesrchannel21Table,
       "pmopm2Mesrchannel21Entry": pmopm2Mesrchannel21Entry,
       "pmopm2Mesrchannel21Index": pmopm2Mesrchannel21Index,
       "pmopm2Mesrchannel21Portn": pmopm2Mesrchannel21Portn,
       "pmopm2Mesrchannel22Table": pmopm2Mesrchannel22Table,
       "pmopm2Mesrchannel22Entry": pmopm2Mesrchannel22Entry,
       "pmopm2Mesrchannel22Index": pmopm2Mesrchannel22Index,
       "pmopm2Mesrchannel22Portn": pmopm2Mesrchannel22Portn,
       "pmopm2Mesrchannel23Table": pmopm2Mesrchannel23Table,
       "pmopm2Mesrchannel23Entry": pmopm2Mesrchannel23Entry,
       "pmopm2Mesrchannel23Index": pmopm2Mesrchannel23Index,
       "pmopm2Mesrchannel23Portn": pmopm2Mesrchannel23Portn,
       "pmopm2Mesrchannel24Table": pmopm2Mesrchannel24Table,
       "pmopm2Mesrchannel24Entry": pmopm2Mesrchannel24Entry,
       "pmopm2Mesrchannel24Index": pmopm2Mesrchannel24Index,
       "pmopm2Mesrchannel24Portn": pmopm2Mesrchannel24Portn,
       "pmopm2Mesrchannel25Table": pmopm2Mesrchannel25Table,
       "pmopm2Mesrchannel25Entry": pmopm2Mesrchannel25Entry,
       "pmopm2Mesrchannel25Index": pmopm2Mesrchannel25Index,
       "pmopm2Mesrchannel25Portn": pmopm2Mesrchannel25Portn,
       "pmopm2Mesrchannel26Table": pmopm2Mesrchannel26Table,
       "pmopm2Mesrchannel26Entry": pmopm2Mesrchannel26Entry,
       "pmopm2Mesrchannel26Index": pmopm2Mesrchannel26Index,
       "pmopm2Mesrchannel26Portn": pmopm2Mesrchannel26Portn,
       "pmopm2Mesrchannel27Table": pmopm2Mesrchannel27Table,
       "pmopm2Mesrchannel27Entry": pmopm2Mesrchannel27Entry,
       "pmopm2Mesrchannel27Index": pmopm2Mesrchannel27Index,
       "pmopm2Mesrchannel27Portn": pmopm2Mesrchannel27Portn,
       "pmopm2Mesrchannel28Table": pmopm2Mesrchannel28Table,
       "pmopm2Mesrchannel28Entry": pmopm2Mesrchannel28Entry,
       "pmopm2Mesrchannel28Index": pmopm2Mesrchannel28Index,
       "pmopm2Mesrchannel28Portn": pmopm2Mesrchannel28Portn,
       "pmopm2Mesrchannel29Table": pmopm2Mesrchannel29Table,
       "pmopm2Mesrchannel29Entry": pmopm2Mesrchannel29Entry,
       "pmopm2Mesrchannel29Index": pmopm2Mesrchannel29Index,
       "pmopm2Mesrchannel29Portn": pmopm2Mesrchannel29Portn,
       "pmopm2Mesrchannel30Table": pmopm2Mesrchannel30Table,
       "pmopm2Mesrchannel30Entry": pmopm2Mesrchannel30Entry,
       "pmopm2Mesrchannel30Index": pmopm2Mesrchannel30Index,
       "pmopm2Mesrchannel30Portn": pmopm2Mesrchannel30Portn,
       "pmopm2Mesrchannel31Table": pmopm2Mesrchannel31Table,
       "pmopm2Mesrchannel31Entry": pmopm2Mesrchannel31Entry,
       "pmopm2Mesrchannel31Index": pmopm2Mesrchannel31Index,
       "pmopm2Mesrchannel31Portn": pmopm2Mesrchannel31Portn,
       "pmopm2Mesrchannel32Table": pmopm2Mesrchannel32Table,
       "pmopm2Mesrchannel32Entry": pmopm2Mesrchannel32Entry,
       "pmopm2Mesrchannel32Index": pmopm2Mesrchannel32Index,
       "pmopm2Mesrchannel32Portn": pmopm2Mesrchannel32Portn,
       "pmopm2Mesrchannel33Table": pmopm2Mesrchannel33Table,
       "pmopm2Mesrchannel33Entry": pmopm2Mesrchannel33Entry,
       "pmopm2Mesrchannel33Index": pmopm2Mesrchannel33Index,
       "pmopm2Mesrchannel33Portn": pmopm2Mesrchannel33Portn,
       "pmopm2Mesrchannel34Table": pmopm2Mesrchannel34Table,
       "pmopm2Mesrchannel34Entry": pmopm2Mesrchannel34Entry,
       "pmopm2Mesrchannel34Index": pmopm2Mesrchannel34Index,
       "pmopm2Mesrchannel34Portn": pmopm2Mesrchannel34Portn,
       "pmopm2Mesrchannel35Table": pmopm2Mesrchannel35Table,
       "pmopm2Mesrchannel35Entry": pmopm2Mesrchannel35Entry,
       "pmopm2Mesrchannel35Index": pmopm2Mesrchannel35Index,
       "pmopm2Mesrchannel35Portn": pmopm2Mesrchannel35Portn,
       "pmopm2Mesrchannel36Table": pmopm2Mesrchannel36Table,
       "pmopm2Mesrchannel36Entry": pmopm2Mesrchannel36Entry,
       "pmopm2Mesrchannel36Index": pmopm2Mesrchannel36Index,
       "pmopm2Mesrchannel36Portn": pmopm2Mesrchannel36Portn,
       "pmopm2Mesrchannel37Table": pmopm2Mesrchannel37Table,
       "pmopm2Mesrchannel37Entry": pmopm2Mesrchannel37Entry,
       "pmopm2Mesrchannel37Index": pmopm2Mesrchannel37Index,
       "pmopm2Mesrchannel37Portn": pmopm2Mesrchannel37Portn,
       "pmopm2Mesrchannel38Table": pmopm2Mesrchannel38Table,
       "pmopm2Mesrchannel38Entry": pmopm2Mesrchannel38Entry,
       "pmopm2Mesrchannel38Index": pmopm2Mesrchannel38Index,
       "pmopm2Mesrchannel38Portn": pmopm2Mesrchannel38Portn,
       "pmopm2Mesrchannel39Table": pmopm2Mesrchannel39Table,
       "pmopm2Mesrchannel39Entry": pmopm2Mesrchannel39Entry,
       "pmopm2Mesrchannel39Index": pmopm2Mesrchannel39Index,
       "pmopm2Mesrchannel39Portn": pmopm2Mesrchannel39Portn,
       "pmopm2Mesrchannel40Table": pmopm2Mesrchannel40Table,
       "pmopm2Mesrchannel40Entry": pmopm2Mesrchannel40Entry,
       "pmopm2Mesrchannel40Index": pmopm2Mesrchannel40Index,
       "pmopm2Mesrchannel40Portn": pmopm2Mesrchannel40Portn,
       "pmopm2Mesrchannel41Table": pmopm2Mesrchannel41Table,
       "pmopm2Mesrchannel41Entry": pmopm2Mesrchannel41Entry,
       "pmopm2Mesrchannel41Index": pmopm2Mesrchannel41Index,
       "pmopm2Mesrchannel41Portn": pmopm2Mesrchannel41Portn,
       "pmopm2Mesrchannel42Table": pmopm2Mesrchannel42Table,
       "pmopm2Mesrchannel42Entry": pmopm2Mesrchannel42Entry,
       "pmopm2Mesrchannel42Index": pmopm2Mesrchannel42Index,
       "pmopm2Mesrchannel42Portn": pmopm2Mesrchannel42Portn,
       "pmopm2Mesrchannel43Table": pmopm2Mesrchannel43Table,
       "pmopm2Mesrchannel43Entry": pmopm2Mesrchannel43Entry,
       "pmopm2Mesrchannel43Index": pmopm2Mesrchannel43Index,
       "pmopm2Mesrchannel43Portn": pmopm2Mesrchannel43Portn,
       "pmopm2Mesrchannel44Table": pmopm2Mesrchannel44Table,
       "pmopm2Mesrchannel44Entry": pmopm2Mesrchannel44Entry,
       "pmopm2Mesrchannel44Index": pmopm2Mesrchannel44Index,
       "pmopm2Mesrchannel44Portn": pmopm2Mesrchannel44Portn,
       "pmopm2Mesrchannel45Table": pmopm2Mesrchannel45Table,
       "pmopm2Mesrchannel45Entry": pmopm2Mesrchannel45Entry,
       "pmopm2Mesrchannel45Index": pmopm2Mesrchannel45Index,
       "pmopm2Mesrchannel45Portn": pmopm2Mesrchannel45Portn,
       "pmopm2Mesrchannel46Table": pmopm2Mesrchannel46Table,
       "pmopm2Mesrchannel46Entry": pmopm2Mesrchannel46Entry,
       "pmopm2Mesrchannel46Index": pmopm2Mesrchannel46Index,
       "pmopm2Mesrchannel46Portn": pmopm2Mesrchannel46Portn,
       "pmopm2Mesrchannel47Table": pmopm2Mesrchannel47Table,
       "pmopm2Mesrchannel47Entry": pmopm2Mesrchannel47Entry,
       "pmopm2Mesrchannel47Index": pmopm2Mesrchannel47Index,
       "pmopm2Mesrchannel47Portn": pmopm2Mesrchannel47Portn,
       "pmopm2Mesrchannel48Table": pmopm2Mesrchannel48Table,
       "pmopm2Mesrchannel48Entry": pmopm2Mesrchannel48Entry,
       "pmopm2Mesrchannel48Index": pmopm2Mesrchannel48Index,
       "pmopm2Mesrchannel48Portn": pmopm2Mesrchannel48Portn,
       "pmopm2Mesrchannel49Table": pmopm2Mesrchannel49Table,
       "pmopm2Mesrchannel49Entry": pmopm2Mesrchannel49Entry,
       "pmopm2Mesrchannel49Index": pmopm2Mesrchannel49Index,
       "pmopm2Mesrchannel49Portn": pmopm2Mesrchannel49Portn,
       "pmopm2Mesrchannel50Table": pmopm2Mesrchannel50Table,
       "pmopm2Mesrchannel50Entry": pmopm2Mesrchannel50Entry,
       "pmopm2Mesrchannel50Index": pmopm2Mesrchannel50Index,
       "pmopm2Mesrchannel50Portn": pmopm2Mesrchannel50Portn,
       "pmopm2Mesrchannel51Table": pmopm2Mesrchannel51Table,
       "pmopm2Mesrchannel51Entry": pmopm2Mesrchannel51Entry,
       "pmopm2Mesrchannel51Index": pmopm2Mesrchannel51Index,
       "pmopm2Mesrchannel51Portn": pmopm2Mesrchannel51Portn,
       "pmopm2Mesrchannel52Table": pmopm2Mesrchannel52Table,
       "pmopm2Mesrchannel52Entry": pmopm2Mesrchannel52Entry,
       "pmopm2Mesrchannel52Index": pmopm2Mesrchannel52Index,
       "pmopm2Mesrchannel52Portn": pmopm2Mesrchannel52Portn,
       "pmopm2Mesrchannel53Table": pmopm2Mesrchannel53Table,
       "pmopm2Mesrchannel53Entry": pmopm2Mesrchannel53Entry,
       "pmopm2Mesrchannel53Index": pmopm2Mesrchannel53Index,
       "pmopm2Mesrchannel53Portn": pmopm2Mesrchannel53Portn,
       "pmopm2Mesrchannel54Table": pmopm2Mesrchannel54Table,
       "pmopm2Mesrchannel54Entry": pmopm2Mesrchannel54Entry,
       "pmopm2Mesrchannel54Index": pmopm2Mesrchannel54Index,
       "pmopm2Mesrchannel54Portn": pmopm2Mesrchannel54Portn,
       "pmopm2Mesrchannel55Table": pmopm2Mesrchannel55Table,
       "pmopm2Mesrchannel55Entry": pmopm2Mesrchannel55Entry,
       "pmopm2Mesrchannel55Index": pmopm2Mesrchannel55Index,
       "pmopm2Mesrchannel55Portn": pmopm2Mesrchannel55Portn,
       "pmopm2Mesrchannel56Table": pmopm2Mesrchannel56Table,
       "pmopm2Mesrchannel56Entry": pmopm2Mesrchannel56Entry,
       "pmopm2Mesrchannel56Index": pmopm2Mesrchannel56Index,
       "pmopm2Mesrchannel56Portn": pmopm2Mesrchannel56Portn,
       "pmopm2Mesrchannel57Table": pmopm2Mesrchannel57Table,
       "pmopm2Mesrchannel57Entry": pmopm2Mesrchannel57Entry,
       "pmopm2Mesrchannel57Index": pmopm2Mesrchannel57Index,
       "pmopm2Mesrchannel57Portn": pmopm2Mesrchannel57Portn,
       "pmopm2Mesrchannel58Table": pmopm2Mesrchannel58Table,
       "pmopm2Mesrchannel58Entry": pmopm2Mesrchannel58Entry,
       "pmopm2Mesrchannel58Index": pmopm2Mesrchannel58Index,
       "pmopm2Mesrchannel58Portn": pmopm2Mesrchannel58Portn,
       "pmopm2Mesrchannel59Table": pmopm2Mesrchannel59Table,
       "pmopm2Mesrchannel59Entry": pmopm2Mesrchannel59Entry,
       "pmopm2Mesrchannel59Index": pmopm2Mesrchannel59Index,
       "pmopm2Mesrchannel59Portn": pmopm2Mesrchannel59Portn,
       "pmopm2Mesrchannel60Table": pmopm2Mesrchannel60Table,
       "pmopm2Mesrchannel60Entry": pmopm2Mesrchannel60Entry,
       "pmopm2Mesrchannel60Index": pmopm2Mesrchannel60Index,
       "pmopm2Mesrchannel60Portn": pmopm2Mesrchannel60Portn,
       "pmopm2Mesrchannel61Table": pmopm2Mesrchannel61Table,
       "pmopm2Mesrchannel61Entry": pmopm2Mesrchannel61Entry,
       "pmopm2Mesrchannel61Index": pmopm2Mesrchannel61Index,
       "pmopm2Mesrchannel61Portn": pmopm2Mesrchannel61Portn,
       "pmopm2Mesrchannel62Table": pmopm2Mesrchannel62Table,
       "pmopm2Mesrchannel62Entry": pmopm2Mesrchannel62Entry,
       "pmopm2Mesrchannel62Index": pmopm2Mesrchannel62Index,
       "pmopm2Mesrchannel62Portn": pmopm2Mesrchannel62Portn,
       "pmopm2Mesrchannel63Table": pmopm2Mesrchannel63Table,
       "pmopm2Mesrchannel63Entry": pmopm2Mesrchannel63Entry,
       "pmopm2Mesrchannel63Index": pmopm2Mesrchannel63Index,
       "pmopm2Mesrchannel63Portn": pmopm2Mesrchannel63Portn,
       "pmopm2Mesrchannel64Table": pmopm2Mesrchannel64Table,
       "pmopm2Mesrchannel64Entry": pmopm2Mesrchannel64Entry,
       "pmopm2Mesrchannel64Index": pmopm2Mesrchannel64Index,
       "pmopm2Mesrchannel64Portn": pmopm2Mesrchannel64Portn,
       "pmopm2Mesrchannel65Table": pmopm2Mesrchannel65Table,
       "pmopm2Mesrchannel65Entry": pmopm2Mesrchannel65Entry,
       "pmopm2Mesrchannel65Index": pmopm2Mesrchannel65Index,
       "pmopm2Mesrchannel65Portn": pmopm2Mesrchannel65Portn,
       "pmopm2Mesrchannel66Table": pmopm2Mesrchannel66Table,
       "pmopm2Mesrchannel66Entry": pmopm2Mesrchannel66Entry,
       "pmopm2Mesrchannel66Index": pmopm2Mesrchannel66Index,
       "pmopm2Mesrchannel66Portn": pmopm2Mesrchannel66Portn,
       "pmopm2Mesrchannel67Table": pmopm2Mesrchannel67Table,
       "pmopm2Mesrchannel67Entry": pmopm2Mesrchannel67Entry,
       "pmopm2Mesrchannel67Index": pmopm2Mesrchannel67Index,
       "pmopm2Mesrchannel67Portn": pmopm2Mesrchannel67Portn,
       "pmopm2Mesrchannel68Table": pmopm2Mesrchannel68Table,
       "pmopm2Mesrchannel68Entry": pmopm2Mesrchannel68Entry,
       "pmopm2Mesrchannel68Index": pmopm2Mesrchannel68Index,
       "pmopm2Mesrchannel68Portn": pmopm2Mesrchannel68Portn,
       "pmopm2Mesrchannel69Table": pmopm2Mesrchannel69Table,
       "pmopm2Mesrchannel69Entry": pmopm2Mesrchannel69Entry,
       "pmopm2Mesrchannel69Index": pmopm2Mesrchannel69Index,
       "pmopm2Mesrchannel69Portn": pmopm2Mesrchannel69Portn,
       "pmopm2Mesrchannel70Table": pmopm2Mesrchannel70Table,
       "pmopm2Mesrchannel70Entry": pmopm2Mesrchannel70Entry,
       "pmopm2Mesrchannel70Index": pmopm2Mesrchannel70Index,
       "pmopm2Mesrchannel70Portn": pmopm2Mesrchannel70Portn,
       "pmopm2Mesrchannel71Table": pmopm2Mesrchannel71Table,
       "pmopm2Mesrchannel71Entry": pmopm2Mesrchannel71Entry,
       "pmopm2Mesrchannel71Index": pmopm2Mesrchannel71Index,
       "pmopm2Mesrchannel71Portn": pmopm2Mesrchannel71Portn,
       "pmopm2Mesrchannel72Table": pmopm2Mesrchannel72Table,
       "pmopm2Mesrchannel72Entry": pmopm2Mesrchannel72Entry,
       "pmopm2Mesrchannel72Index": pmopm2Mesrchannel72Index,
       "pmopm2Mesrchannel72Portn": pmopm2Mesrchannel72Portn,
       "pmopm2Mesrchannel73Table": pmopm2Mesrchannel73Table,
       "pmopm2Mesrchannel73Entry": pmopm2Mesrchannel73Entry,
       "pmopm2Mesrchannel73Index": pmopm2Mesrchannel73Index,
       "pmopm2Mesrchannel73Portn": pmopm2Mesrchannel73Portn,
       "pmopm2Mesrchannel74Table": pmopm2Mesrchannel74Table,
       "pmopm2Mesrchannel74Entry": pmopm2Mesrchannel74Entry,
       "pmopm2Mesrchannel74Index": pmopm2Mesrchannel74Index,
       "pmopm2Mesrchannel74Portn": pmopm2Mesrchannel74Portn,
       "pmopm2Mesrchannel75Table": pmopm2Mesrchannel75Table,
       "pmopm2Mesrchannel75Entry": pmopm2Mesrchannel75Entry,
       "pmopm2Mesrchannel75Index": pmopm2Mesrchannel75Index,
       "pmopm2Mesrchannel75Portn": pmopm2Mesrchannel75Portn,
       "pmopm2Mesrchannel76Table": pmopm2Mesrchannel76Table,
       "pmopm2Mesrchannel76Entry": pmopm2Mesrchannel76Entry,
       "pmopm2Mesrchannel76Index": pmopm2Mesrchannel76Index,
       "pmopm2Mesrchannel76Portn": pmopm2Mesrchannel76Portn,
       "pmopm2Mesrchannel77Table": pmopm2Mesrchannel77Table,
       "pmopm2Mesrchannel77Entry": pmopm2Mesrchannel77Entry,
       "pmopm2Mesrchannel77Index": pmopm2Mesrchannel77Index,
       "pmopm2Mesrchannel77Portn": pmopm2Mesrchannel77Portn,
       "pmopm2Mesrchannel78Table": pmopm2Mesrchannel78Table,
       "pmopm2Mesrchannel78Entry": pmopm2Mesrchannel78Entry,
       "pmopm2Mesrchannel78Index": pmopm2Mesrchannel78Index,
       "pmopm2Mesrchannel78Portn": pmopm2Mesrchannel78Portn,
       "pmopm2Mesrchannel79Table": pmopm2Mesrchannel79Table,
       "pmopm2Mesrchannel79Entry": pmopm2Mesrchannel79Entry,
       "pmopm2Mesrchannel79Index": pmopm2Mesrchannel79Index,
       "pmopm2Mesrchannel79Portn": pmopm2Mesrchannel79Portn,
       "pmopm2Mesrchannel80Table": pmopm2Mesrchannel80Table,
       "pmopm2Mesrchannel80Entry": pmopm2Mesrchannel80Entry,
       "pmopm2Mesrchannel80Index": pmopm2Mesrchannel80Index,
       "pmopm2Mesrchannel80Portn": pmopm2Mesrchannel80Portn,
       "pmopm2Mesrchannel81Table": pmopm2Mesrchannel81Table,
       "pmopm2Mesrchannel81Entry": pmopm2Mesrchannel81Entry,
       "pmopm2Mesrchannel81Index": pmopm2Mesrchannel81Index,
       "pmopm2Mesrchannel81Portn": pmopm2Mesrchannel81Portn,
       "pmopm2Mesrchannel82Table": pmopm2Mesrchannel82Table,
       "pmopm2Mesrchannel82Entry": pmopm2Mesrchannel82Entry,
       "pmopm2Mesrchannel82Index": pmopm2Mesrchannel82Index,
       "pmopm2Mesrchannel82Portn": pmopm2Mesrchannel82Portn,
       "pmopm2Mesrchannel83Table": pmopm2Mesrchannel83Table,
       "pmopm2Mesrchannel83Entry": pmopm2Mesrchannel83Entry,
       "pmopm2Mesrchannel83Index": pmopm2Mesrchannel83Index,
       "pmopm2Mesrchannel83Portn": pmopm2Mesrchannel83Portn,
       "pmopm2Mesrchannel84Table": pmopm2Mesrchannel84Table,
       "pmopm2Mesrchannel84Entry": pmopm2Mesrchannel84Entry,
       "pmopm2Mesrchannel84Index": pmopm2Mesrchannel84Index,
       "pmopm2Mesrchannel84Portn": pmopm2Mesrchannel84Portn,
       "pmopm2Mesrchannel85Table": pmopm2Mesrchannel85Table,
       "pmopm2Mesrchannel85Entry": pmopm2Mesrchannel85Entry,
       "pmopm2Mesrchannel85Index": pmopm2Mesrchannel85Index,
       "pmopm2Mesrchannel85Portn": pmopm2Mesrchannel85Portn,
       "pmopm2Mesrchannel86Table": pmopm2Mesrchannel86Table,
       "pmopm2Mesrchannel86Entry": pmopm2Mesrchannel86Entry,
       "pmopm2Mesrchannel86Index": pmopm2Mesrchannel86Index,
       "pmopm2Mesrchannel86Portn": pmopm2Mesrchannel86Portn,
       "pmopm2Mesrchannel87Table": pmopm2Mesrchannel87Table,
       "pmopm2Mesrchannel87Entry": pmopm2Mesrchannel87Entry,
       "pmopm2Mesrchannel87Index": pmopm2Mesrchannel87Index,
       "pmopm2Mesrchannel87Portn": pmopm2Mesrchannel87Portn,
       "pmopm2Mesrchannel88Table": pmopm2Mesrchannel88Table,
       "pmopm2Mesrchannel88Entry": pmopm2Mesrchannel88Entry,
       "pmopm2Mesrchannel88Index": pmopm2Mesrchannel88Index,
       "pmopm2Mesrchannel88Portn": pmopm2Mesrchannel88Portn,
       "pmopm2Mesrchannel89Table": pmopm2Mesrchannel89Table,
       "pmopm2Mesrchannel89Entry": pmopm2Mesrchannel89Entry,
       "pmopm2Mesrchannel89Index": pmopm2Mesrchannel89Index,
       "pmopm2Mesrchannel89Portn": pmopm2Mesrchannel89Portn,
       "pmopm2Mesrchannel90Table": pmopm2Mesrchannel90Table,
       "pmopm2Mesrchannel90Entry": pmopm2Mesrchannel90Entry,
       "pmopm2Mesrchannel90Index": pmopm2Mesrchannel90Index,
       "pmopm2Mesrchannel90Portn": pmopm2Mesrchannel90Portn,
       "pmopm2Mesrchannel91Table": pmopm2Mesrchannel91Table,
       "pmopm2Mesrchannel91Entry": pmopm2Mesrchannel91Entry,
       "pmopm2Mesrchannel91Index": pmopm2Mesrchannel91Index,
       "pmopm2Mesrchannel91Portn": pmopm2Mesrchannel91Portn,
       "pmopm2Mesrchannel92Table": pmopm2Mesrchannel92Table,
       "pmopm2Mesrchannel92Entry": pmopm2Mesrchannel92Entry,
       "pmopm2Mesrchannel92Index": pmopm2Mesrchannel92Index,
       "pmopm2Mesrchannel92Portn": pmopm2Mesrchannel92Portn,
       "pmopm2Mesrchannel93Table": pmopm2Mesrchannel93Table,
       "pmopm2Mesrchannel93Entry": pmopm2Mesrchannel93Entry,
       "pmopm2Mesrchannel93Index": pmopm2Mesrchannel93Index,
       "pmopm2Mesrchannel93Portn": pmopm2Mesrchannel93Portn,
       "pmopm2Mesrchannel94Table": pmopm2Mesrchannel94Table,
       "pmopm2Mesrchannel94Entry": pmopm2Mesrchannel94Entry,
       "pmopm2Mesrchannel94Index": pmopm2Mesrchannel94Index,
       "pmopm2Mesrchannel94Portn": pmopm2Mesrchannel94Portn,
       "pmopm2Mesrchannel95Table": pmopm2Mesrchannel95Table,
       "pmopm2Mesrchannel95Entry": pmopm2Mesrchannel95Entry,
       "pmopm2Mesrchannel95Index": pmopm2Mesrchannel95Index,
       "pmopm2Mesrchannel95Portn": pmopm2Mesrchannel95Portn,
       "pmopm2Mesrchannel96Table": pmopm2Mesrchannel96Table,
       "pmopm2Mesrchannel96Entry": pmopm2Mesrchannel96Entry,
       "pmopm2Mesrchannel96Index": pmopm2Mesrchannel96Index,
       "pmopm2Mesrchannel96Portn": pmopm2Mesrchannel96Portn,
       "pmopm2MesrportInputPwrTable": pmopm2MesrportInputPwrTable,
       "pmopm2MesrportInputPwrEntry": pmopm2MesrportInputPwrEntry,
       "pmopm2MesrportInputPwrIndex": pmopm2MesrportInputPwrIndex,
       "pmopm2MesrportInputPwrPortn": pmopm2MesrportInputPwrPortn,
       "pmopm2MesrchannelMaxPwrTable": pmopm2MesrchannelMaxPwrTable,
       "pmopm2MesrchannelMaxPwrEntry": pmopm2MesrchannelMaxPwrEntry,
       "pmopm2MesrchannelMaxPwrIndex": pmopm2MesrchannelMaxPwrIndex,
       "pmopm2MesrchannelMaxPwrPortn": pmopm2MesrchannelMaxPwrPortn,
       "pmopm2MesrchannelMinPwrTable": pmopm2MesrchannelMinPwrTable,
       "pmopm2MesrchannelMinPwrEntry": pmopm2MesrchannelMinPwrEntry,
       "pmopm2MesrchannelMinPwrIndex": pmopm2MesrchannelMinPwrIndex,
       "pmopm2MesrchannelMinPwrPortn": pmopm2MesrchannelMinPwrPortn,
       "pmopm2MesrLine": pmopm2MesrLine,
       "pmopm2controlsWrite": pmopm2controlsWrite,
       "pmopm2CtrlOther": pmopm2CtrlOther,
       "pmopm2CtrlconfMgnt1": pmopm2CtrlconfMgnt1,
       "pmopm2CtrlConf1Load1": pmopm2CtrlConf1Load1,
       "pmopm2CtrlConf2Load1": pmopm2CtrlConf2Load1,
       "pmopm2CtrlConf2Flash1": pmopm2CtrlConf2Flash1,
       "pmopm2CtrlConf2Clear1": pmopm2CtrlConf2Clear1,
       "pmopm2Ctrlsynth4": pmopm2Ctrlsynth4,
       "pmopm2CtrlCorrelatOn": pmopm2CtrlCorrelatOn,
       "pmopm2CtrlCorrelatOff": pmopm2CtrlCorrelatOff,
       "pmopm2CtrlswMgnt": pmopm2CtrlswMgnt,
       "pmopm2CtrlColdReset": pmopm2CtrlColdReset,
       "pmopm2CtrlWarmReset": pmopm2CtrlWarmReset,
       "pmopm2CtrlLoadSwBank1": pmopm2CtrlLoadSwBank1,
       "pmopm2CtrlLoadSwBank2": pmopm2CtrlLoadSwBank2,
       "pmopm2CtrlgwMgnt": pmopm2CtrlgwMgnt,
       "pmopm2CtrlCurrentGwReset": pmopm2CtrlCurrentGwReset,
       "pmopm2CtrlLoadGwBank1": pmopm2CtrlLoadGwBank1,
       "pmopm2CtrlLoadGwBank2": pmopm2CtrlLoadGwBank2,
       "pmopm2CtrlLoadGwBank3": pmopm2CtrlLoadGwBank3,
       "pmopm2CtrlLoadGwBank4": pmopm2CtrlLoadGwBank4,
       "pmopm2CtrlledTest": pmopm2CtrlledTest,
       "pmopm2CtrlGreenLed": pmopm2CtrlGreenLed,
       "pmopm2CtrlRedLed": pmopm2CtrlRedLed,
       "pmopm2CtrlLedOff": pmopm2CtrlLedOff,
       "pmopm2CtrlClient": pmopm2CtrlClient,
       "pmopm2CtrlcalibrationTable": pmopm2CtrlcalibrationTable,
       "pmopm2CtrlcalibrationEntry": pmopm2CtrlcalibrationEntry,
       "pmopm2CtrlcalibrationIndex": pmopm2CtrlcalibrationIndex,
       "pmopm2CtrlcalibrationPortn": pmopm2CtrlcalibrationPortn,
       "pmopm2CtrlspectrumAutodiscoveryTable": pmopm2CtrlspectrumAutodiscoveryTable,
       "pmopm2CtrlspectrumAutodiscoveryEntry": pmopm2CtrlspectrumAutodiscoveryEntry,
       "pmopm2CtrlspectrumAutodiscoveryIndex": pmopm2CtrlspectrumAutodiscoveryIndex,
       "pmopm2CtrlspectrumAutodiscoveryPortn": pmopm2CtrlspectrumAutodiscoveryPortn,
       "pmopm2CtrlthresholdsAutoconfigTable": pmopm2CtrlthresholdsAutoconfigTable,
       "pmopm2CtrlthresholdsAutoconfigEntry": pmopm2CtrlthresholdsAutoconfigEntry,
       "pmopm2CtrlthresholdsAutoconfigIndex": pmopm2CtrlthresholdsAutoconfigIndex,
       "pmopm2CtrlthresholdsAutoconfigPortn": pmopm2CtrlthresholdsAutoconfigPortn,
       "pmopm2CtrlpowerLossDeltaTable": pmopm2CtrlpowerLossDeltaTable,
       "pmopm2CtrlpowerLossDeltaEntry": pmopm2CtrlpowerLossDeltaEntry,
       "pmopm2CtrlpowerLossDeltaIndex": pmopm2CtrlpowerLossDeltaIndex,
       "pmopm2CtrlpowerLossDeltaPortn": pmopm2CtrlpowerLossDeltaPortn,
       "pmopm2CtrlpowerHighDeltaTable": pmopm2CtrlpowerHighDeltaTable,
       "pmopm2CtrlpowerHighDeltaEntry": pmopm2CtrlpowerHighDeltaEntry,
       "pmopm2CtrlpowerHighDeltaIndex": pmopm2CtrlpowerHighDeltaIndex,
       "pmopm2CtrlpowerHighDeltaPortn": pmopm2CtrlpowerHighDeltaPortn,
       "pmopm2CtrlpowerLowDeltaTable": pmopm2CtrlpowerLowDeltaTable,
       "pmopm2CtrlpowerLowDeltaEntry": pmopm2CtrlpowerLowDeltaEntry,
       "pmopm2CtrlpowerLowDeltaIndex": pmopm2CtrlpowerLowDeltaIndex,
       "pmopm2CtrlpowerLowDeltaPortn": pmopm2CtrlpowerLowDeltaPortn,
       "pmopm2CtrlinputPowerRefTable": pmopm2CtrlinputPowerRefTable,
       "pmopm2CtrlinputPowerRefEntry": pmopm2CtrlinputPowerRefEntry,
       "pmopm2CtrlinputPowerRefIndex": pmopm2CtrlinputPowerRefIndex,
       "pmopm2CtrlinputPowerRefPortn": pmopm2CtrlinputPowerRefPortn,
       "pmopm2CtrlLine": pmopm2CtrlLine,
       "pmopm2ri": pmopm2ri,
       "pmopm2riTable": pmopm2riTable,
       "pmopm2RinvSfpTable": pmopm2RinvSfpTable,
       "pmopm2RinvSfpEntry": pmopm2RinvSfpEntry,
       "pmopm2RinvSfpIndex": pmopm2RinvSfpIndex,
       "pmopm2Rinvsfp": pmopm2Rinvsfp,
       "pmopm2RinvLineTable": pmopm2RinvLineTable,
       "pmopm2RinvLineEntry": pmopm2RinvLineEntry,
       "pmopm2RinvLineIndex": pmopm2RinvLineIndex,
       "pmopm2RinvxfpLine": pmopm2RinvxfpLine,
       "pmopm2RinvReloadInventory": pmopm2RinvReloadInventory,
       "pmopm2RinvHwPlatform": pmopm2RinvHwPlatform,
       "pmopm2RinvModulePlatform": pmopm2RinvModulePlatform,
       "pmopm2RinvSwPlatform": pmopm2RinvSwPlatform,
       "pmopm2RinvGwPlatform": pmopm2RinvGwPlatform,
       "pmopm2download": pmopm2download,
       "pmopm2DwlOther": pmopm2DwlOther,
       "pmopm2DwlrestartProcess": pmopm2DwlrestartProcess,
       "pmopm2DwlWarmRestartProcessed": pmopm2DwlWarmRestartProcessed,
       "pmopm2DwlColdRestartProcessed": pmopm2DwlColdRestartProcessed,
       "pmopm2DwlswBanksUsed": pmopm2DwlswBanksUsed,
       "pmopm2DwlSwBank1Used": pmopm2DwlSwBank1Used,
       "pmopm2DwlSwBank2Used": pmopm2DwlSwBank2Used,
       "pmopm2DwlSwBank1Notempty": pmopm2DwlSwBank1Notempty,
       "pmopm2DwlSwBank2Notempty": pmopm2DwlSwBank2Notempty,
       "pmopm2DwlgwBanksUsed": pmopm2DwlgwBanksUsed,
       "pmopm2DwlGwBank1Used": pmopm2DwlGwBank1Used,
       "pmopm2DwlGwBank2Used": pmopm2DwlGwBank2Used,
       "pmopm2DwlGwBank3Used": pmopm2DwlGwBank3Used,
       "pmopm2DwlGwBank4Used": pmopm2DwlGwBank4Used,
       "pmopm2DwlGwBank1Notempty": pmopm2DwlGwBank1Notempty,
       "pmopm2DwlGwBank2Notempty": pmopm2DwlGwBank2Notempty,
       "pmopm2DwlGwBank3Notempty": pmopm2DwlGwBank3Notempty,
       "pmopm2DwlGwBank4Notempty": pmopm2DwlGwBank4Notempty,
       "pmopm2DwlClient": pmopm2DwlClient,
       "pmopm2DwlLine": pmopm2DwlLine,
       "pmopm2Config": pmopm2Config,
       "pmopm2CfgLsd": pmopm2CfgLsd,
       "pmopm2tableclientcaiscsf": pmopm2tableclientcaiscsf,
       "pmopm2CfgStartup": pmopm2CfgStartup,
       "pmopm2tableother": pmopm2tableother,
       "pmopm2CfgcomponentType": pmopm2CfgcomponentType,
       "pmopm2Cfgmiscellaneous": pmopm2Cfgmiscellaneous,
       "pmopm2CfgfirstChannel": pmopm2CfgfirstChannel,
       "pmopm2CfglastChannel": pmopm2CfglastChannel,
       "pmopm2Cfggrid": pmopm2Cfggrid,
       "pmopm2CfgClientStartupOosTable": pmopm2CfgClientStartupOosTable,
       "pmopm2CfgClientStartupOosEntry": pmopm2CfgClientStartupOosEntry,
       "pmopm2CfgClientStartupOosIndex": pmopm2CfgClientStartupOosIndex,
       "pmopm2CfgSpectrumOosPortn": pmopm2CfgSpectrumOosPortn,
       "pmopm2CfgSpectrumOffsetPortn": pmopm2CfgSpectrumOffsetPortn,
       "pmopm2CfgCh1Ch16OosPortn": pmopm2CfgCh1Ch16OosPortn,
       "pmopm2CfgCh17Ch32OosPortn": pmopm2CfgCh17Ch32OosPortn,
       "pmopm2CfgCh33Ch48OosPortn": pmopm2CfgCh33Ch48OosPortn,
       "pmopm2CfgCh49Ch64OosPortn": pmopm2CfgCh49Ch64OosPortn,
       "pmopm2CfgCh65Ch80OosPortn": pmopm2CfgCh65Ch80OosPortn,
       "pmopm2CfgCh81Ch96OosPortn": pmopm2CfgCh81Ch96OosPortn,
       "pmopm2CfgClientStartupBalanceTable": pmopm2CfgClientStartupBalanceTable,
       "pmopm2CfgClientStartupBalanceEntry": pmopm2CfgClientStartupBalanceEntry,
       "pmopm2CfgClientStartupBalanceIndex": pmopm2CfgClientStartupBalanceIndex,
       "pmopm2CfgCh1Ch16BalancePortn": pmopm2CfgCh1Ch16BalancePortn,
       "pmopm2CfgCh17Ch32BalancePortn": pmopm2CfgCh17Ch32BalancePortn,
       "pmopm2CfgCh33Ch48BalancePortn": pmopm2CfgCh33Ch48BalancePortn,
       "pmopm2CfgCh49Ch64BalancePortn": pmopm2CfgCh49Ch64BalancePortn,
       "pmopm2CfgCh65Ch80BalancePortn": pmopm2CfgCh65Ch80BalancePortn,
       "pmopm2CfgCh81Ch96BalancePortn": pmopm2CfgCh81Ch96BalancePortn,
       "pmopm2CfgClientStartupAbsthreshTable": pmopm2CfgClientStartupAbsthreshTable,
       "pmopm2CfgClientStartupAbsthreshEntry": pmopm2CfgClientStartupAbsthreshEntry,
       "pmopm2CfgClientStartupAbsthreshIndex": pmopm2CfgClientStartupAbsthreshIndex,
       "pmopm2CfgChannel1AbsthreshPortn": pmopm2CfgChannel1AbsthreshPortn,
       "pmopm2CfgChannel2AbsthreshPortn": pmopm2CfgChannel2AbsthreshPortn,
       "pmopm2CfgChannel3AbsthreshPortn": pmopm2CfgChannel3AbsthreshPortn,
       "pmopm2CfgChannel4AbsthreshPortn": pmopm2CfgChannel4AbsthreshPortn,
       "pmopm2CfgChannel5AbsthreshPortn": pmopm2CfgChannel5AbsthreshPortn,
       "pmopm2CfgChannel6AbsthreshPortn": pmopm2CfgChannel6AbsthreshPortn,
       "pmopm2CfgChannel7AbsthreshPortn": pmopm2CfgChannel7AbsthreshPortn,
       "pmopm2CfgChannel8AbsthreshPortn": pmopm2CfgChannel8AbsthreshPortn,
       "pmopm2CfgChannel9AbsthreshPortn": pmopm2CfgChannel9AbsthreshPortn,
       "pmopm2CfgChannel10AbsthreshPortn": pmopm2CfgChannel10AbsthreshPortn,
       "pmopm2CfgChannel11AbsthreshPortn": pmopm2CfgChannel11AbsthreshPortn,
       "pmopm2CfgChannel12AbsthreshPortn": pmopm2CfgChannel12AbsthreshPortn,
       "pmopm2CfgChannel13AbsthreshPortn": pmopm2CfgChannel13AbsthreshPortn,
       "pmopm2CfgChannel14AbsthreshPortn": pmopm2CfgChannel14AbsthreshPortn,
       "pmopm2CfgChannel15AbsthreshPortn": pmopm2CfgChannel15AbsthreshPortn,
       "pmopm2CfgChannel16AbsthreshPortn": pmopm2CfgChannel16AbsthreshPortn,
       "pmopm2CfgChannel17AbsthreshPortn": pmopm2CfgChannel17AbsthreshPortn,
       "pmopm2CfgChannel18AbsthreshPortn": pmopm2CfgChannel18AbsthreshPortn,
       "pmopm2CfgChannel19AbsthreshPortn": pmopm2CfgChannel19AbsthreshPortn,
       "pmopm2CfgChannel20AbsthreshPortn": pmopm2CfgChannel20AbsthreshPortn,
       "pmopm2CfgChannel21AbsthreshPortn": pmopm2CfgChannel21AbsthreshPortn,
       "pmopm2CfgChannel22AbsthreshPortn": pmopm2CfgChannel22AbsthreshPortn,
       "pmopm2CfgChannel23AbsthreshPortn": pmopm2CfgChannel23AbsthreshPortn,
       "pmopm2CfgChannel24AbsthreshPortn": pmopm2CfgChannel24AbsthreshPortn,
       "pmopm2CfgChannel25AbsthreshPortn": pmopm2CfgChannel25AbsthreshPortn,
       "pmopm2CfgChannel26AbsthreshPortn": pmopm2CfgChannel26AbsthreshPortn,
       "pmopm2CfgChannel27AbsthreshPortn": pmopm2CfgChannel27AbsthreshPortn,
       "pmopm2CfgChannel28AbsthreshPortn": pmopm2CfgChannel28AbsthreshPortn,
       "pmopm2CfgChannel29AbsthreshPortn": pmopm2CfgChannel29AbsthreshPortn,
       "pmopm2CfgChannel30AbsthreshPortn": pmopm2CfgChannel30AbsthreshPortn,
       "pmopm2CfgChannel31AbsthreshPortn": pmopm2CfgChannel31AbsthreshPortn,
       "pmopm2CfgChannel32AbsthreshPortn": pmopm2CfgChannel32AbsthreshPortn,
       "pmopm2CfgChannel33AbsthreshPortn": pmopm2CfgChannel33AbsthreshPortn,
       "pmopm2CfgChannel34AbsthreshPortn": pmopm2CfgChannel34AbsthreshPortn,
       "pmopm2CfgChannel35AbsthreshPortn": pmopm2CfgChannel35AbsthreshPortn,
       "pmopm2CfgChannel36AbsthreshPortn": pmopm2CfgChannel36AbsthreshPortn,
       "pmopm2CfgChannel37AbsthreshPortn": pmopm2CfgChannel37AbsthreshPortn,
       "pmopm2CfgChannel38AbsthreshPortn": pmopm2CfgChannel38AbsthreshPortn,
       "pmopm2CfgChannel39AbsthreshPortn": pmopm2CfgChannel39AbsthreshPortn,
       "pmopm2CfgChannel40AbsthreshPortn": pmopm2CfgChannel40AbsthreshPortn,
       "pmopm2CfgChannel41AbsthreshPortn": pmopm2CfgChannel41AbsthreshPortn,
       "pmopm2CfgChannel42AbsthreshPortn": pmopm2CfgChannel42AbsthreshPortn,
       "pmopm2CfgChannel43AbsthreshPortn": pmopm2CfgChannel43AbsthreshPortn,
       "pmopm2CfgChannel44AbsthreshPortn": pmopm2CfgChannel44AbsthreshPortn,
       "pmopm2CfgChannel45AbsthreshPortn": pmopm2CfgChannel45AbsthreshPortn,
       "pmopm2CfgChannel46AbsthreshPortn": pmopm2CfgChannel46AbsthreshPortn,
       "pmopm2CfgChannel47AbsthreshPortn": pmopm2CfgChannel47AbsthreshPortn,
       "pmopm2CfgChannel48AbsthreshPortn": pmopm2CfgChannel48AbsthreshPortn,
       "pmopm2CfgChannel49AbsthreshPortn": pmopm2CfgChannel49AbsthreshPortn,
       "pmopm2CfgChannel50AbsthreshPortn": pmopm2CfgChannel50AbsthreshPortn,
       "pmopm2CfgChannel51AbsthreshPortn": pmopm2CfgChannel51AbsthreshPortn,
       "pmopm2CfgChannel52AbsthreshPortn": pmopm2CfgChannel52AbsthreshPortn,
       "pmopm2CfgChannel53AbsthreshPortn": pmopm2CfgChannel53AbsthreshPortn,
       "pmopm2CfgChannel54AbsthreshPortn": pmopm2CfgChannel54AbsthreshPortn,
       "pmopm2CfgChannel55AbsthreshPortn": pmopm2CfgChannel55AbsthreshPortn,
       "pmopm2CfgChannel56AbsthreshPortn": pmopm2CfgChannel56AbsthreshPortn,
       "pmopm2CfgChannel57AbsthreshPortn": pmopm2CfgChannel57AbsthreshPortn,
       "pmopm2CfgChannel58AbsthreshPortn": pmopm2CfgChannel58AbsthreshPortn,
       "pmopm2CfgChannel59AbsthreshPortn": pmopm2CfgChannel59AbsthreshPortn,
       "pmopm2CfgChannel60AbsthreshPortn": pmopm2CfgChannel60AbsthreshPortn,
       "pmopm2CfgChannel61AbsthreshPortn": pmopm2CfgChannel61AbsthreshPortn,
       "pmopm2CfgChannel62AbsthreshPortn": pmopm2CfgChannel62AbsthreshPortn,
       "pmopm2CfgChannel63AbsthreshPortn": pmopm2CfgChannel63AbsthreshPortn,
       "pmopm2CfgChannel64AbsthreshPortn": pmopm2CfgChannel64AbsthreshPortn,
       "pmopm2CfgChannel65AbsthreshPortn": pmopm2CfgChannel65AbsthreshPortn,
       "pmopm2CfgChannel66AbsthreshPortn": pmopm2CfgChannel66AbsthreshPortn,
       "pmopm2CfgChannel67AbsthreshPortn": pmopm2CfgChannel67AbsthreshPortn,
       "pmopm2CfgChannel68AbsthreshPortn": pmopm2CfgChannel68AbsthreshPortn,
       "pmopm2CfgChannel69AbsthreshPortn": pmopm2CfgChannel69AbsthreshPortn,
       "pmopm2CfgChannel70AbsthreshPortn": pmopm2CfgChannel70AbsthreshPortn,
       "pmopm2CfgChannel71AbsthreshPortn": pmopm2CfgChannel71AbsthreshPortn,
       "pmopm2CfgChannel72AbsthreshPortn": pmopm2CfgChannel72AbsthreshPortn,
       "pmopm2CfgChannel73AbsthreshPortn": pmopm2CfgChannel73AbsthreshPortn,
       "pmopm2CfgChannel74AbsthreshPortn": pmopm2CfgChannel74AbsthreshPortn,
       "pmopm2CfgChannel75AbsthreshPortn": pmopm2CfgChannel75AbsthreshPortn,
       "pmopm2CfgChannel76AbsthreshPortn": pmopm2CfgChannel76AbsthreshPortn,
       "pmopm2CfgChannel77AbsthreshPortn": pmopm2CfgChannel77AbsthreshPortn,
       "pmopm2CfgChannel78AbsthreshPortn": pmopm2CfgChannel78AbsthreshPortn,
       "pmopm2CfgChannel79AbsthreshPortn": pmopm2CfgChannel79AbsthreshPortn,
       "pmopm2CfgChannel80AbsthreshPortn": pmopm2CfgChannel80AbsthreshPortn,
       "pmopm2CfgChannel81AbsthreshPortn": pmopm2CfgChannel81AbsthreshPortn,
       "pmopm2CfgChannel82AbsthreshPortn": pmopm2CfgChannel82AbsthreshPortn,
       "pmopm2CfgChannel83AbsthreshPortn": pmopm2CfgChannel83AbsthreshPortn,
       "pmopm2CfgChannel84AbsthreshPortn": pmopm2CfgChannel84AbsthreshPortn,
       "pmopm2CfgChannel85AbsthreshPortn": pmopm2CfgChannel85AbsthreshPortn,
       "pmopm2CfgChannel86AbsthreshPortn": pmopm2CfgChannel86AbsthreshPortn,
       "pmopm2CfgChannel87AbsthreshPortn": pmopm2CfgChannel87AbsthreshPortn,
       "pmopm2CfgChannel88AbsthreshPortn": pmopm2CfgChannel88AbsthreshPortn,
       "pmopm2CfgChannel89AbsthreshPortn": pmopm2CfgChannel89AbsthreshPortn,
       "pmopm2CfgChannel90AbsthreshPortn": pmopm2CfgChannel90AbsthreshPortn,
       "pmopm2CfgChannel91AbsthreshPortn": pmopm2CfgChannel91AbsthreshPortn,
       "pmopm2CfgChannel92AbsthreshPortn": pmopm2CfgChannel92AbsthreshPortn,
       "pmopm2CfgChannel93AbsthreshPortn": pmopm2CfgChannel93AbsthreshPortn,
       "pmopm2CfgChannel94AbsthreshPortn": pmopm2CfgChannel94AbsthreshPortn,
       "pmopm2CfgChannel95AbsthreshPortn": pmopm2CfgChannel95AbsthreshPortn,
       "pmopm2CfgChannel96AbsthreshPortn": pmopm2CfgChannel96AbsthreshPortn,
       "pmopm2CfgClientStartupPwrHighTable": pmopm2CfgClientStartupPwrHighTable,
       "pmopm2CfgClientStartupPwrHighEntry": pmopm2CfgClientStartupPwrHighEntry,
       "pmopm2CfgClientStartupPwrHighIndex": pmopm2CfgClientStartupPwrHighIndex,
       "pmopm2CfgChannel1PwrhighPortn": pmopm2CfgChannel1PwrhighPortn,
       "pmopm2CfgChannel2PwrhighPortn": pmopm2CfgChannel2PwrhighPortn,
       "pmopm2CfgChannel3PwrhighPortn": pmopm2CfgChannel3PwrhighPortn,
       "pmopm2CfgChannel4PwrhighPortn": pmopm2CfgChannel4PwrhighPortn,
       "pmopm2CfgChannel5PwrhighPortn": pmopm2CfgChannel5PwrhighPortn,
       "pmopm2CfgChannel6PwrhighPortn": pmopm2CfgChannel6PwrhighPortn,
       "pmopm2CfgChannel7PwrhighPortn": pmopm2CfgChannel7PwrhighPortn,
       "pmopm2CfgChannel8PwrhighPortn": pmopm2CfgChannel8PwrhighPortn,
       "pmopm2CfgChannel9PwrhighPortn": pmopm2CfgChannel9PwrhighPortn,
       "pmopm2CfgChannel10PwrhighPortn": pmopm2CfgChannel10PwrhighPortn,
       "pmopm2CfgChannel11PwrhighPortn": pmopm2CfgChannel11PwrhighPortn,
       "pmopm2CfgChannel12PwrhighPortn": pmopm2CfgChannel12PwrhighPortn,
       "pmopm2CfgChannel13PwrhighPortn": pmopm2CfgChannel13PwrhighPortn,
       "pmopm2CfgChannel14PwrhighPortn": pmopm2CfgChannel14PwrhighPortn,
       "pmopm2CfgChannel15PwrhighPortn": pmopm2CfgChannel15PwrhighPortn,
       "pmopm2CfgChannel16PwrhighPortn": pmopm2CfgChannel16PwrhighPortn,
       "pmopm2CfgChannel17PwrhighPortn": pmopm2CfgChannel17PwrhighPortn,
       "pmopm2CfgChannel18PwrhighPortn": pmopm2CfgChannel18PwrhighPortn,
       "pmopm2CfgChannel19PwrhighPortn": pmopm2CfgChannel19PwrhighPortn,
       "pmopm2CfgChannel20PwrhighPortn": pmopm2CfgChannel20PwrhighPortn,
       "pmopm2CfgChannel21PwrhighPortn": pmopm2CfgChannel21PwrhighPortn,
       "pmopm2CfgChannel22PwrhighPortn": pmopm2CfgChannel22PwrhighPortn,
       "pmopm2CfgChannel23PwrhighPortn": pmopm2CfgChannel23PwrhighPortn,
       "pmopm2CfgChannel24PwrhighPortn": pmopm2CfgChannel24PwrhighPortn,
       "pmopm2CfgChannel25PwrhighPortn": pmopm2CfgChannel25PwrhighPortn,
       "pmopm2CfgChannel26PwrhighPortn": pmopm2CfgChannel26PwrhighPortn,
       "pmopm2CfgChannel27PwrhighPortn": pmopm2CfgChannel27PwrhighPortn,
       "pmopm2CfgChannel28PwrhighPortn": pmopm2CfgChannel28PwrhighPortn,
       "pmopm2CfgChannel29PwrhighPortn": pmopm2CfgChannel29PwrhighPortn,
       "pmopm2CfgChannel30PwrhighPortn": pmopm2CfgChannel30PwrhighPortn,
       "pmopm2CfgChannel31PwrhighPortn": pmopm2CfgChannel31PwrhighPortn,
       "pmopm2CfgChannel32PwrhighPortn": pmopm2CfgChannel32PwrhighPortn,
       "pmopm2CfgChannel33PwrhighPortn": pmopm2CfgChannel33PwrhighPortn,
       "pmopm2CfgChannel34PwrhighPortn": pmopm2CfgChannel34PwrhighPortn,
       "pmopm2CfgChannel35PwrhighPortn": pmopm2CfgChannel35PwrhighPortn,
       "pmopm2CfgChannel36PwrhighPortn": pmopm2CfgChannel36PwrhighPortn,
       "pmopm2CfgChannel37PwrhighPortn": pmopm2CfgChannel37PwrhighPortn,
       "pmopm2CfgChannel38PwrhighPortn": pmopm2CfgChannel38PwrhighPortn,
       "pmopm2CfgChannel39PwrhighPortn": pmopm2CfgChannel39PwrhighPortn,
       "pmopm2CfgChannel40PwrhighPortn": pmopm2CfgChannel40PwrhighPortn,
       "pmopm2CfgChannel41PwrhighPortn": pmopm2CfgChannel41PwrhighPortn,
       "pmopm2CfgChannel42PwrhighPortn": pmopm2CfgChannel42PwrhighPortn,
       "pmopm2CfgChannel43PwrhighPortn": pmopm2CfgChannel43PwrhighPortn,
       "pmopm2CfgChannel44PwrhighPortn": pmopm2CfgChannel44PwrhighPortn,
       "pmopm2CfgChannel45PwrhighPortn": pmopm2CfgChannel45PwrhighPortn,
       "pmopm2CfgChannel46PwrhighPortn": pmopm2CfgChannel46PwrhighPortn,
       "pmopm2CfgChannel47PwrhighPortn": pmopm2CfgChannel47PwrhighPortn,
       "pmopm2CfgChannel48PwrhighPortn": pmopm2CfgChannel48PwrhighPortn,
       "pmopm2CfgChannel49PwrhighPortn": pmopm2CfgChannel49PwrhighPortn,
       "pmopm2CfgChannel50PwrhighPortn": pmopm2CfgChannel50PwrhighPortn,
       "pmopm2CfgChannel51PwrhighPortn": pmopm2CfgChannel51PwrhighPortn,
       "pmopm2CfgChannel52PwrhighPortn": pmopm2CfgChannel52PwrhighPortn,
       "pmopm2CfgChannel53PwrhighPortn": pmopm2CfgChannel53PwrhighPortn,
       "pmopm2CfgChannel54PwrhighPortn": pmopm2CfgChannel54PwrhighPortn,
       "pmopm2CfgChannel55PwrhighPortn": pmopm2CfgChannel55PwrhighPortn,
       "pmopm2CfgChannel56PwrhighPortn": pmopm2CfgChannel56PwrhighPortn,
       "pmopm2CfgChannel57PwrhighPortn": pmopm2CfgChannel57PwrhighPortn,
       "pmopm2CfgChannel58PwrhighPortn": pmopm2CfgChannel58PwrhighPortn,
       "pmopm2CfgChannel59PwrhighPortn": pmopm2CfgChannel59PwrhighPortn,
       "pmopm2CfgChannel60PwrhighPortn": pmopm2CfgChannel60PwrhighPortn,
       "pmopm2CfgChannel61PwrhighPortn": pmopm2CfgChannel61PwrhighPortn,
       "pmopm2CfgChannel62PwrhighPortn": pmopm2CfgChannel62PwrhighPortn,
       "pmopm2CfgChannel63PwrhighPortn": pmopm2CfgChannel63PwrhighPortn,
       "pmopm2CfgChannel64PwrhighPortn": pmopm2CfgChannel64PwrhighPortn,
       "pmopm2CfgChannel65PwrhighPortn": pmopm2CfgChannel65PwrhighPortn,
       "pmopm2CfgChannel66PwrhighPortn": pmopm2CfgChannel66PwrhighPortn,
       "pmopm2CfgChannel67PwrhighPortn": pmopm2CfgChannel67PwrhighPortn,
       "pmopm2CfgChannel68PwrhighPortn": pmopm2CfgChannel68PwrhighPortn,
       "pmopm2CfgChannel69PwrhighPortn": pmopm2CfgChannel69PwrhighPortn,
       "pmopm2CfgChannel70PwrhighPortn": pmopm2CfgChannel70PwrhighPortn,
       "pmopm2CfgChannel71PwrhighPortn": pmopm2CfgChannel71PwrhighPortn,
       "pmopm2CfgChannel72PwrhighPortn": pmopm2CfgChannel72PwrhighPortn,
       "pmopm2CfgChannel73PwrhighPortn": pmopm2CfgChannel73PwrhighPortn,
       "pmopm2CfgChannel74PwrhighPortn": pmopm2CfgChannel74PwrhighPortn,
       "pmopm2CfgChannel75PwrhighPortn": pmopm2CfgChannel75PwrhighPortn,
       "pmopm2CfgChannel76PwrhighPortn": pmopm2CfgChannel76PwrhighPortn,
       "pmopm2CfgChannel77PwrhighPortn": pmopm2CfgChannel77PwrhighPortn,
       "pmopm2CfgChannel78PwrhighPortn": pmopm2CfgChannel78PwrhighPortn,
       "pmopm2CfgChannel79PwrhighPortn": pmopm2CfgChannel79PwrhighPortn,
       "pmopm2CfgChannel80PwrhighPortn": pmopm2CfgChannel80PwrhighPortn,
       "pmopm2CfgChannel81PwrhighPortn": pmopm2CfgChannel81PwrhighPortn,
       "pmopm2CfgChannel82PwrhighPortn": pmopm2CfgChannel82PwrhighPortn,
       "pmopm2CfgChannel83PwrhighPortn": pmopm2CfgChannel83PwrhighPortn,
       "pmopm2CfgChannel84PwrhighPortn": pmopm2CfgChannel84PwrhighPortn,
       "pmopm2CfgChannel85PwrhighPortn": pmopm2CfgChannel85PwrhighPortn,
       "pmopm2CfgChannel86PwrhighPortn": pmopm2CfgChannel86PwrhighPortn,
       "pmopm2CfgChannel87PwrhighPortn": pmopm2CfgChannel87PwrhighPortn,
       "pmopm2CfgChannel88PwrhighPortn": pmopm2CfgChannel88PwrhighPortn,
       "pmopm2CfgChannel89PwrhighPortn": pmopm2CfgChannel89PwrhighPortn,
       "pmopm2CfgChannel90PwrhighPortn": pmopm2CfgChannel90PwrhighPortn,
       "pmopm2CfgChannel91PwrhighPortn": pmopm2CfgChannel91PwrhighPortn,
       "pmopm2CfgChannel92PwrhighPortn": pmopm2CfgChannel92PwrhighPortn,
       "pmopm2CfgChannel93PwrhighPortn": pmopm2CfgChannel93PwrhighPortn,
       "pmopm2CfgChannel94PwrhighPortn": pmopm2CfgChannel94PwrhighPortn,
       "pmopm2CfgChannel95PwrhighPortn": pmopm2CfgChannel95PwrhighPortn,
       "pmopm2CfgChannel96PwrhighPortn": pmopm2CfgChannel96PwrhighPortn,
       "pmopm2CfgClientStartupPwrLowTable": pmopm2CfgClientStartupPwrLowTable,
       "pmopm2CfgClientStartupPwrLowEntry": pmopm2CfgClientStartupPwrLowEntry,
       "pmopm2CfgClientStartupPwrLowIndex": pmopm2CfgClientStartupPwrLowIndex,
       "pmopm2CfgChannel1PwrlowPortn": pmopm2CfgChannel1PwrlowPortn,
       "pmopm2CfgChannel2PwrlowPortn": pmopm2CfgChannel2PwrlowPortn,
       "pmopm2CfgChannel3PwrlowPortn": pmopm2CfgChannel3PwrlowPortn,
       "pmopm2CfgChannel4PwrlowPortn": pmopm2CfgChannel4PwrlowPortn,
       "pmopm2CfgChannel5PwrlowPortn": pmopm2CfgChannel5PwrlowPortn,
       "pmopm2CfgChannel6PwrlowPortn": pmopm2CfgChannel6PwrlowPortn,
       "pmopm2CfgChannel7PwrlowPortn": pmopm2CfgChannel7PwrlowPortn,
       "pmopm2CfgChannel8PwrlowPortn": pmopm2CfgChannel8PwrlowPortn,
       "pmopm2CfgChannel9PwrlowPortn": pmopm2CfgChannel9PwrlowPortn,
       "pmopm2CfgChannel10PwrlowPortn": pmopm2CfgChannel10PwrlowPortn,
       "pmopm2CfgChannel11PwrlowPortn": pmopm2CfgChannel11PwrlowPortn,
       "pmopm2CfgChannel12PwrlowPortn": pmopm2CfgChannel12PwrlowPortn,
       "pmopm2CfgChannel13PwrlowPortn": pmopm2CfgChannel13PwrlowPortn,
       "pmopm2CfgChannel14PwrlowPortn": pmopm2CfgChannel14PwrlowPortn,
       "pmopm2CfgChannel15PwrlowPortn": pmopm2CfgChannel15PwrlowPortn,
       "pmopm2CfgChannel16PwrlowPortn": pmopm2CfgChannel16PwrlowPortn,
       "pmopm2CfgChannel17PwrlowPortn": pmopm2CfgChannel17PwrlowPortn,
       "pmopm2CfgChannel18PwrlowPortn": pmopm2CfgChannel18PwrlowPortn,
       "pmopm2CfgChannel19PwrlowPortn": pmopm2CfgChannel19PwrlowPortn,
       "pmopm2CfgChannel20PwrlowPortn": pmopm2CfgChannel20PwrlowPortn,
       "pmopm2CfgChannel21PwrlowPortn": pmopm2CfgChannel21PwrlowPortn,
       "pmopm2CfgChannel22PwrlowPortn": pmopm2CfgChannel22PwrlowPortn,
       "pmopm2CfgChannel23PwrlowPortn": pmopm2CfgChannel23PwrlowPortn,
       "pmopm2CfgChannel24PwrlowPortn": pmopm2CfgChannel24PwrlowPortn,
       "pmopm2CfgChannel25PwrlowPortn": pmopm2CfgChannel25PwrlowPortn,
       "pmopm2CfgChannel26PwrlowPortn": pmopm2CfgChannel26PwrlowPortn,
       "pmopm2CfgChannel27PwrlowPortn": pmopm2CfgChannel27PwrlowPortn,
       "pmopm2CfgChannel28PwrlowPortn": pmopm2CfgChannel28PwrlowPortn,
       "pmopm2CfgChannel29PwrlowPortn": pmopm2CfgChannel29PwrlowPortn,
       "pmopm2CfgChannel30PwrlowPortn": pmopm2CfgChannel30PwrlowPortn,
       "pmopm2CfgChannel31PwrlowPortn": pmopm2CfgChannel31PwrlowPortn,
       "pmopm2CfgChannel32PwrlowPortn": pmopm2CfgChannel32PwrlowPortn,
       "pmopm2CfgChannel33PwrlowPortn": pmopm2CfgChannel33PwrlowPortn,
       "pmopm2CfgChannel34PwrlowPortn": pmopm2CfgChannel34PwrlowPortn,
       "pmopm2CfgChannel35PwrlowPortn": pmopm2CfgChannel35PwrlowPortn,
       "pmopm2CfgChannel36PwrlowPortn": pmopm2CfgChannel36PwrlowPortn,
       "pmopm2CfgChannel37PwrlowPortn": pmopm2CfgChannel37PwrlowPortn,
       "pmopm2CfgChannel38PwrlowPortn": pmopm2CfgChannel38PwrlowPortn,
       "pmopm2CfgChannel39PwrlowPortn": pmopm2CfgChannel39PwrlowPortn,
       "pmopm2CfgChannel40PwrlowPortn": pmopm2CfgChannel40PwrlowPortn,
       "pmopm2CfgChannel41PwrlowPortn": pmopm2CfgChannel41PwrlowPortn,
       "pmopm2CfgChannel42PwrlowPortn": pmopm2CfgChannel42PwrlowPortn,
       "pmopm2CfgChannel43PwrlowPortn": pmopm2CfgChannel43PwrlowPortn,
       "pmopm2CfgChannel44PwrlowPortn": pmopm2CfgChannel44PwrlowPortn,
       "pmopm2CfgChannel45PwrlowPortn": pmopm2CfgChannel45PwrlowPortn,
       "pmopm2CfgChannel46PwrlowPortn": pmopm2CfgChannel46PwrlowPortn,
       "pmopm2CfgChannel47PwrlowPortn": pmopm2CfgChannel47PwrlowPortn,
       "pmopm2CfgChannel48PwrlowPortn": pmopm2CfgChannel48PwrlowPortn,
       "pmopm2CfgChannel49PwrlowPortn": pmopm2CfgChannel49PwrlowPortn,
       "pmopm2CfgChannel50PwrlowPortn": pmopm2CfgChannel50PwrlowPortn,
       "pmopm2CfgChannel51PwrlowPortn": pmopm2CfgChannel51PwrlowPortn,
       "pmopm2CfgChannel52PwrlowPortn": pmopm2CfgChannel52PwrlowPortn,
       "pmopm2CfgChannel53PwrlowPortn": pmopm2CfgChannel53PwrlowPortn,
       "pmopm2CfgChannel54PwrlowPortn": pmopm2CfgChannel54PwrlowPortn,
       "pmopm2CfgChannel55PwrlowPortn": pmopm2CfgChannel55PwrlowPortn,
       "pmopm2CfgChannel56PwrlowPortn": pmopm2CfgChannel56PwrlowPortn,
       "pmopm2CfgChannel57PwrlowPortn": pmopm2CfgChannel57PwrlowPortn,
       "pmopm2CfgChannel58PwrlowPortn": pmopm2CfgChannel58PwrlowPortn,
       "pmopm2CfgChannel59PwrlowPortn": pmopm2CfgChannel59PwrlowPortn,
       "pmopm2CfgChannel60PwrlowPortn": pmopm2CfgChannel60PwrlowPortn,
       "pmopm2CfgChannel61PwrlowPortn": pmopm2CfgChannel61PwrlowPortn,
       "pmopm2CfgChannel62PwrlowPortn": pmopm2CfgChannel62PwrlowPortn,
       "pmopm2CfgChannel63PwrlowPortn": pmopm2CfgChannel63PwrlowPortn,
       "pmopm2CfgChannel64PwrlowPortn": pmopm2CfgChannel64PwrlowPortn,
       "pmopm2CfgChannel65PwrlowPortn": pmopm2CfgChannel65PwrlowPortn,
       "pmopm2CfgChannel66PwrlowPortn": pmopm2CfgChannel66PwrlowPortn,
       "pmopm2CfgChannel67PwrlowPortn": pmopm2CfgChannel67PwrlowPortn,
       "pmopm2CfgChannel68PwrlowPortn": pmopm2CfgChannel68PwrlowPortn,
       "pmopm2CfgChannel69PwrlowPortn": pmopm2CfgChannel69PwrlowPortn,
       "pmopm2CfgChannel70PwrlowPortn": pmopm2CfgChannel70PwrlowPortn,
       "pmopm2CfgChannel71PwrlowPortn": pmopm2CfgChannel71PwrlowPortn,
       "pmopm2CfgChannel72PwrlowPortn": pmopm2CfgChannel72PwrlowPortn,
       "pmopm2CfgChannel73PwrlowPortn": pmopm2CfgChannel73PwrlowPortn,
       "pmopm2CfgChannel74PwrlowPortn": pmopm2CfgChannel74PwrlowPortn,
       "pmopm2CfgChannel75PwrlowPortn": pmopm2CfgChannel75PwrlowPortn,
       "pmopm2CfgChannel76PwrlowPortn": pmopm2CfgChannel76PwrlowPortn,
       "pmopm2CfgChannel77PwrlowPortn": pmopm2CfgChannel77PwrlowPortn,
       "pmopm2CfgChannel78PwrlowPortn": pmopm2CfgChannel78PwrlowPortn,
       "pmopm2CfgChannel79PwrlowPortn": pmopm2CfgChannel79PwrlowPortn,
       "pmopm2CfgChannel80PwrlowPortn": pmopm2CfgChannel80PwrlowPortn,
       "pmopm2CfgChannel81PwrlowPortn": pmopm2CfgChannel81PwrlowPortn,
       "pmopm2CfgChannel82PwrlowPortn": pmopm2CfgChannel82PwrlowPortn,
       "pmopm2CfgChannel83PwrlowPortn": pmopm2CfgChannel83PwrlowPortn,
       "pmopm2CfgChannel84PwrlowPortn": pmopm2CfgChannel84PwrlowPortn,
       "pmopm2CfgChannel85PwrlowPortn": pmopm2CfgChannel85PwrlowPortn,
       "pmopm2CfgChannel86PwrlowPortn": pmopm2CfgChannel86PwrlowPortn,
       "pmopm2CfgChannel87PwrlowPortn": pmopm2CfgChannel87PwrlowPortn,
       "pmopm2CfgChannel88PwrlowPortn": pmopm2CfgChannel88PwrlowPortn,
       "pmopm2CfgChannel89PwrlowPortn": pmopm2CfgChannel89PwrlowPortn,
       "pmopm2CfgChannel90PwrlowPortn": pmopm2CfgChannel90PwrlowPortn,
       "pmopm2CfgChannel91PwrlowPortn": pmopm2CfgChannel91PwrlowPortn,
       "pmopm2CfgChannel92PwrlowPortn": pmopm2CfgChannel92PwrlowPortn,
       "pmopm2CfgChannel93PwrlowPortn": pmopm2CfgChannel93PwrlowPortn,
       "pmopm2CfgChannel94PwrlowPortn": pmopm2CfgChannel94PwrlowPortn,
       "pmopm2CfgChannel95PwrlowPortn": pmopm2CfgChannel95PwrlowPortn,
       "pmopm2CfgChannel96PwrlowPortn": pmopm2CfgChannel96PwrlowPortn,
       "pmopm2CfgLabelclientTable": pmopm2CfgLabelclientTable,
       "pmopm2CfgLabelclientEntry": pmopm2CfgLabelclientEntry,
       "pmopm2CfgLabelclientIndex": pmopm2CfgLabelclientIndex,
       "pmopm2CfgLabelclientPortn": pmopm2CfgLabelclientPortn,
       "pmopm2CfgLabellineTable": pmopm2CfgLabellineTable,
       "pmopm2CfgLabellineEntry": pmopm2CfgLabellineEntry,
       "pmopm2CfgLabellineIndex": pmopm2CfgLabellineIndex,
       "pmopm2CfgLabellinePortn": pmopm2CfgLabellinePortn,
       "pmopm2CfgWriteConfiguration": pmopm2CfgWriteConfiguration,
       "pmopm2traps": pmopm2traps,
       "pmopm2trapPortNumber": pmopm2trapPortNumber,
       "pmopm2trapLineNumber": pmopm2trapLineNumber,
       "pmopm2trapBoardNumber": pmopm2trapBoardNumber,
       "pmopm2PowerTrapUrgentGoesOn": pmopm2PowerTrapUrgentGoesOn,
       "pmopm2PowerTrapUrgentGoesOff": pmopm2PowerTrapUrgentGoesOff}
)
