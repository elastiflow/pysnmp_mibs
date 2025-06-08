# SNMP MIB module (EKINOPS-Pmvoa-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmvoa-MIB.mib
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

modulePmvoa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84)
)
if mibBuilder.loadTexts:
    modulePmvoa.setRevisions(
        ("2016-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmvoaMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("attenuationctrl", 0),
          ("powerctrl", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Pmvoaalarms_ObjectIdentity = ObjectIdentity
pmvoaalarms = _Pmvoaalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2)
)
_PmvoaAlmOther_ObjectIdentity = ObjectIdentity
pmvoaAlmOther = _PmvoaAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1)
)
_PmvoaAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmvoaAlmOtherNurg = _PmvoaAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 1)
)
_PmvoaAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmvoaAlmsynthAlm2 = _PmvoaAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 1, 2)
)
_PmvoaAlmConfTableSave_Type = EkiOnOff
_PmvoaAlmConfTableSave_Object = MibScalar
pmvoaAlmConfTableSave = _PmvoaAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 1, 2, 1),
    _PmvoaAlmConfTableSave_Type()
)
pmvoaAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmConfTableSave.setStatus("current")
_PmvoaAlmInvUpload_Type = EkiOnOff
_PmvoaAlmInvUpload_Object = MibScalar
pmvoaAlmInvUpload = _PmvoaAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 1, 2, 2),
    _PmvoaAlmInvUpload_Type()
)
pmvoaAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmInvUpload.setStatus("current")
_PmvoaAlmConfTableLoad_Type = EkiOnOff
_PmvoaAlmConfTableLoad_Object = MibScalar
pmvoaAlmConfTableLoad = _PmvoaAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 1, 2, 3),
    _PmvoaAlmConfTableLoad_Type()
)
pmvoaAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmConfTableLoad.setStatus("current")
_PmvoaAlmCorrelatOff_Type = EkiOnOff
_PmvoaAlmCorrelatOff_Object = MibScalar
pmvoaAlmCorrelatOff = _PmvoaAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 1, 2, 4),
    _PmvoaAlmCorrelatOff_Type()
)
pmvoaAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmCorrelatOff.setStatus("current")
_PmvoaAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmvoaAlmOtherUrg = _PmvoaAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 2)
)
_PmvoaAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmvoaAlmOtherCrit = _PmvoaAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 3)
)
_PmvoaAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmvoaAlmsynthAlm0 = _PmvoaAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 3, 0)
)
_PmvoaAlmModGlobFail_Type = EkiOnOff
_PmvoaAlmModGlobFail_Object = MibScalar
pmvoaAlmModGlobFail = _PmvoaAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 3, 0, 9),
    _PmvoaAlmModGlobFail_Type()
)
pmvoaAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmModGlobFail.setStatus("current")
_PmvoaAlmDefFuseA_Type = EkiOnOff
_PmvoaAlmDefFuseA_Object = MibScalar
pmvoaAlmDefFuseA = _PmvoaAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 3, 0, 15),
    _PmvoaAlmDefFuseA_Type()
)
pmvoaAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmDefFuseA.setStatus("current")
_PmvoaAlmDefFuseB_Type = EkiOnOff
_PmvoaAlmDefFuseB_Object = MibScalar
pmvoaAlmDefFuseB = _PmvoaAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 1, 3, 0, 16),
    _PmvoaAlmDefFuseB_Type()
)
pmvoaAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmDefFuseB.setStatus("current")
_PmvoaAlmClient_ObjectIdentity = ObjectIdentity
pmvoaAlmClient = _PmvoaAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 2)
)
_PmvoaAlmClientNurg_ObjectIdentity = ObjectIdentity
pmvoaAlmClientNurg = _PmvoaAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 2, 1)
)
_PmvoaAlmClientUrg_ObjectIdentity = ObjectIdentity
pmvoaAlmClientUrg = _PmvoaAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 2, 2)
)
_PmvoaAlmClientCrit_ObjectIdentity = ObjectIdentity
pmvoaAlmClientCrit = _PmvoaAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 2, 3)
)
_PmvoaAlmLine_ObjectIdentity = ObjectIdentity
pmvoaAlmLine = _PmvoaAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3)
)
_PmvoaAlmLineNurg_ObjectIdentity = ObjectIdentity
pmvoaAlmLineNurg = _PmvoaAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 1)
)
_PmvoaAlmLineUrg_ObjectIdentity = ObjectIdentity
pmvoaAlmLineUrg = _PmvoaAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 2)
)
_PmvoaAlmLineCrit_ObjectIdentity = ObjectIdentity
pmvoaAlmLineCrit = _PmvoaAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3)
)
_PmvoaAlmsynthAlmLineTable_Object = MibTable
pmvoaAlmsynthAlmLineTable = _PmvoaAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pmvoaAlmsynthAlmLineTable.setStatus("current")
_PmvoaAlmsynthAlmLineEntry_Object = MibTableRow
pmvoaAlmsynthAlmLineEntry = _PmvoaAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 24, 1)
)
pmvoaAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pmvoaAlmsynthAlmLineEntry.setStatus("current")


class _PmvoaAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pmvoaAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_PmvoaAlmsynthAlmLineIndex_Object = MibTableColumn
pmvoaAlmsynthAlmLineIndex = _PmvoaAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 24, 1, 1),
    _PmvoaAlmsynthAlmLineIndex_Type()
)
pmvoaAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmsynthAlmLineIndex.setStatus("current")
_PmvoaAlmLineSfpVoaAbsentPortn_Type = EkiOnOff
_PmvoaAlmLineSfpVoaAbsentPortn_Object = MibTableColumn
pmvoaAlmLineSfpVoaAbsentPortn = _PmvoaAlmLineSfpVoaAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 24, 1, 2),
    _PmvoaAlmLineSfpVoaAbsentPortn_Type()
)
pmvoaAlmLineSfpVoaAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmLineSfpVoaAbsentPortn.setStatus("current")
_PmvoaAlmLineHwFailPortn_Type = EkiOnOff
_PmvoaAlmLineHwFailPortn_Object = MibTableColumn
pmvoaAlmLineHwFailPortn = _PmvoaAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 24, 1, 5),
    _PmvoaAlmLineHwFailPortn_Type()
)
pmvoaAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmLineHwFailPortn.setStatus("current")
_PmvoaAlmLineOosPortn_Type = EkiOnOff
_PmvoaAlmLineOosPortn_Object = MibTableColumn
pmvoaAlmLineOosPortn = _PmvoaAlmLineOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 24, 1, 7),
    _PmvoaAlmLineOosPortn_Type()
)
pmvoaAlmLineOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmLineOosPortn.setStatus("current")
_PmvoaAlmLineFailPortn_Type = EkiOnOff
_PmvoaAlmLineFailPortn_Object = MibTableColumn
pmvoaAlmLineFailPortn = _PmvoaAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 24, 1, 13),
    _PmvoaAlmLineFailPortn_Type()
)
pmvoaAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmLineFailPortn.setStatus("current")
_PmvoaAlmlineAlmTable_Object = MibTable
pmvoaAlmlineAlmTable = _PmvoaAlmlineAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40)
)
if mibBuilder.loadTexts:
    pmvoaAlmlineAlmTable.setStatus("current")
_PmvoaAlmlineAlmEntry_Object = MibTableRow
pmvoaAlmlineAlmEntry = _PmvoaAlmlineAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40, 1)
)
pmvoaAlmlineAlmEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaAlmlineAlmIndex"),
)
if mibBuilder.loadTexts:
    pmvoaAlmlineAlmEntry.setStatus("current")


class _PmvoaAlmlineAlmIndex_Type(Integer32):
    """Custom type pmvoaAlmlineAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaAlmlineAlmIndex_Type.__name__ = "Integer32"
_PmvoaAlmlineAlmIndex_Object = MibTableColumn
pmvoaAlmlineAlmIndex = _PmvoaAlmlineAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40, 1, 1),
    _PmvoaAlmlineAlmIndex_Type()
)
pmvoaAlmlineAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmlineAlmIndex.setStatus("current")
_PmvoaAlmOutputErrorPortn_Type = EkiOnOff
_PmvoaAlmOutputErrorPortn_Object = MibTableColumn
pmvoaAlmOutputErrorPortn = _PmvoaAlmOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40, 1, 2),
    _PmvoaAlmOutputErrorPortn_Type()
)
pmvoaAlmOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmOutputErrorPortn.setStatus("current")
_PmvoaAlmLossOutputPowerPortn_Type = EkiOnOff
_PmvoaAlmLossOutputPowerPortn_Object = MibTableColumn
pmvoaAlmLossOutputPowerPortn = _PmvoaAlmLossOutputPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40, 1, 3),
    _PmvoaAlmLossOutputPowerPortn_Type()
)
pmvoaAlmLossOutputPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmLossOutputPowerPortn.setStatus("current")
_PmvoaAlmTempHighAlarmPortn_Type = EkiOnOff
_PmvoaAlmTempHighAlarmPortn_Object = MibTableColumn
pmvoaAlmTempHighAlarmPortn = _PmvoaAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40, 1, 4),
    _PmvoaAlmTempHighAlarmPortn_Type()
)
pmvoaAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmTempHighAlarmPortn.setStatus("current")
_PmvoaAlmTempLowAlarmPortn_Type = EkiOnOff
_PmvoaAlmTempLowAlarmPortn_Object = MibTableColumn
pmvoaAlmTempLowAlarmPortn = _PmvoaAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40, 1, 5),
    _PmvoaAlmTempLowAlarmPortn_Type()
)
pmvoaAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmTempLowAlarmPortn.setStatus("current")
_PmvoaAlmLossInputPowerPortn_Type = EkiOnOff
_PmvoaAlmLossInputPowerPortn_Object = MibTableColumn
pmvoaAlmLossInputPowerPortn = _PmvoaAlmLossInputPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 2, 3, 3, 40, 1, 6),
    _PmvoaAlmLossInputPowerPortn_Type()
)
pmvoaAlmLossInputPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaAlmLossInputPowerPortn.setStatus("current")
_Pmvoameasures_ObjectIdentity = ObjectIdentity
pmvoameasures = _Pmvoameasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3)
)
_PmvoaMesrOther_ObjectIdentity = ObjectIdentity
pmvoaMesrOther = _PmvoaMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 1)
)
_PmvoaMesrClient_ObjectIdentity = ObjectIdentity
pmvoaMesrClient = _PmvoaMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 2)
)
_PmvoaMesrLine_ObjectIdentity = ObjectIdentity
pmvoaMesrLine = _PmvoaMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3)
)
_PmvoaMesrlineSfpTempTable_Object = MibTable
pmvoaMesrlineSfpTempTable = _PmvoaMesrlineSfpTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 16)
)
if mibBuilder.loadTexts:
    pmvoaMesrlineSfpTempTable.setStatus("current")
_PmvoaMesrlineSfpTempEntry_Object = MibTableRow
pmvoaMesrlineSfpTempEntry = _PmvoaMesrlineSfpTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 16, 1)
)
pmvoaMesrlineSfpTempEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaMesrlineSfpTempIndex"),
)
if mibBuilder.loadTexts:
    pmvoaMesrlineSfpTempEntry.setStatus("current")


class _PmvoaMesrlineSfpTempIndex_Type(Integer32):
    """Custom type pmvoaMesrlineSfpTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaMesrlineSfpTempIndex_Type.__name__ = "Integer32"
_PmvoaMesrlineSfpTempIndex_Object = MibTableColumn
pmvoaMesrlineSfpTempIndex = _PmvoaMesrlineSfpTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 16, 1, 1),
    _PmvoaMesrlineSfpTempIndex_Type()
)
pmvoaMesrlineSfpTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaMesrlineSfpTempIndex.setStatus("current")


class _PmvoaMesrlineSfpTempPortn_Type(Integer32):
    """Custom type pmvoaMesrlineSfpTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmvoaMesrlineSfpTempPortn_Type.__name__ = "Integer32"
_PmvoaMesrlineSfpTempPortn_Object = MibTableColumn
pmvoaMesrlineSfpTempPortn = _PmvoaMesrlineSfpTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 16, 1, 2),
    _PmvoaMesrlineSfpTempPortn_Type()
)
pmvoaMesrlineSfpTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaMesrlineSfpTempPortn.setStatus("current")
_PmvoaMesrlinePoutTable_Object = MibTable
pmvoaMesrlinePoutTable = _PmvoaMesrlinePoutTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 48)
)
if mibBuilder.loadTexts:
    pmvoaMesrlinePoutTable.setStatus("current")
_PmvoaMesrlinePoutEntry_Object = MibTableRow
pmvoaMesrlinePoutEntry = _PmvoaMesrlinePoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 48, 1)
)
pmvoaMesrlinePoutEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaMesrlinePoutIndex"),
)
if mibBuilder.loadTexts:
    pmvoaMesrlinePoutEntry.setStatus("current")


class _PmvoaMesrlinePoutIndex_Type(Integer32):
    """Custom type pmvoaMesrlinePoutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaMesrlinePoutIndex_Type.__name__ = "Integer32"
_PmvoaMesrlinePoutIndex_Object = MibTableColumn
pmvoaMesrlinePoutIndex = _PmvoaMesrlinePoutIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 48, 1, 1),
    _PmvoaMesrlinePoutIndex_Type()
)
pmvoaMesrlinePoutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaMesrlinePoutIndex.setStatus("current")


class _PmvoaMesrlinePoutPortn_Type(Integer32):
    """Custom type pmvoaMesrlinePoutPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmvoaMesrlinePoutPortn_Type.__name__ = "Integer32"
_PmvoaMesrlinePoutPortn_Object = MibTableColumn
pmvoaMesrlinePoutPortn = _PmvoaMesrlinePoutPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 48, 1, 2),
    _PmvoaMesrlinePoutPortn_Type()
)
pmvoaMesrlinePoutPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaMesrlinePoutPortn.setStatus("current")
_PmvoaMesrlineEstPinTable_Object = MibTable
pmvoaMesrlineEstPinTable = _PmvoaMesrlineEstPinTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 64)
)
if mibBuilder.loadTexts:
    pmvoaMesrlineEstPinTable.setStatus("current")
_PmvoaMesrlineEstPinEntry_Object = MibTableRow
pmvoaMesrlineEstPinEntry = _PmvoaMesrlineEstPinEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 64, 1)
)
pmvoaMesrlineEstPinEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaMesrlineEstPinIndex"),
)
if mibBuilder.loadTexts:
    pmvoaMesrlineEstPinEntry.setStatus("current")


class _PmvoaMesrlineEstPinIndex_Type(Integer32):
    """Custom type pmvoaMesrlineEstPinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaMesrlineEstPinIndex_Type.__name__ = "Integer32"
_PmvoaMesrlineEstPinIndex_Object = MibTableColumn
pmvoaMesrlineEstPinIndex = _PmvoaMesrlineEstPinIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 64, 1, 1),
    _PmvoaMesrlineEstPinIndex_Type()
)
pmvoaMesrlineEstPinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaMesrlineEstPinIndex.setStatus("current")


class _PmvoaMesrlineEstPinPortn_Type(Integer32):
    """Custom type pmvoaMesrlineEstPinPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmvoaMesrlineEstPinPortn_Type.__name__ = "Integer32"
_PmvoaMesrlineEstPinPortn_Object = MibTableColumn
pmvoaMesrlineEstPinPortn = _PmvoaMesrlineEstPinPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 3, 3, 64, 1, 2),
    _PmvoaMesrlineEstPinPortn_Type()
)
pmvoaMesrlineEstPinPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaMesrlineEstPinPortn.setStatus("current")
_PmvoacontrolsWrite_ObjectIdentity = ObjectIdentity
pmvoacontrolsWrite = _PmvoacontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6)
)
_PmvoaCtrlOther_ObjectIdentity = ObjectIdentity
pmvoaCtrlOther = _PmvoaCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1)
)
_PmvoaCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmvoaCtrlconfMgnt1 = _PmvoaCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 1)
)
_PmvoaCtrlConf1Load1_Type = EkiOnOff
_PmvoaCtrlConf1Load1_Object = MibScalar
pmvoaCtrlConf1Load1 = _PmvoaCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 1, 1),
    _PmvoaCtrlConf1Load1_Type()
)
pmvoaCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlConf1Load1.setStatus("current")
_PmvoaCtrlConf2Load1_Type = EkiOnOff
_PmvoaCtrlConf2Load1_Object = MibScalar
pmvoaCtrlConf2Load1 = _PmvoaCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 1, 2),
    _PmvoaCtrlConf2Load1_Type()
)
pmvoaCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlConf2Load1.setStatus("current")
_PmvoaCtrlConf2Flash1_Type = EkiOnOff
_PmvoaCtrlConf2Flash1_Object = MibScalar
pmvoaCtrlConf2Flash1 = _PmvoaCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 1, 10),
    _PmvoaCtrlConf2Flash1_Type()
)
pmvoaCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlConf2Flash1.setStatus("current")
_PmvoaCtrlConf2Clear1_Type = EkiOnOff
_PmvoaCtrlConf2Clear1_Object = MibScalar
pmvoaCtrlConf2Clear1 = _PmvoaCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 1, 14),
    _PmvoaCtrlConf2Clear1_Type()
)
pmvoaCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlConf2Clear1.setStatus("current")
_PmvoaCtrlsynth4_ObjectIdentity = ObjectIdentity
pmvoaCtrlsynth4 = _PmvoaCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 4)
)
_PmvoaCtrlCorrelatOn_Type = EkiOnOff
_PmvoaCtrlCorrelatOn_Object = MibScalar
pmvoaCtrlCorrelatOn = _PmvoaCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 4, 1),
    _PmvoaCtrlCorrelatOn_Type()
)
pmvoaCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlCorrelatOn.setStatus("current")
_PmvoaCtrlCorrelatOff_Type = EkiOnOff
_PmvoaCtrlCorrelatOff_Object = MibScalar
pmvoaCtrlCorrelatOff = _PmvoaCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 4, 2),
    _PmvoaCtrlCorrelatOff_Type()
)
pmvoaCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlCorrelatOff.setStatus("current")
_PmvoaCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmvoaCtrlswMgnt = _PmvoaCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 5)
)
_PmvoaCtrlColdReset_Type = EkiOnOff
_PmvoaCtrlColdReset_Object = MibScalar
pmvoaCtrlColdReset = _PmvoaCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 5, 2),
    _PmvoaCtrlColdReset_Type()
)
pmvoaCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlColdReset.setStatus("current")
_PmvoaCtrlWarmReset_Type = EkiOnOff
_PmvoaCtrlWarmReset_Object = MibScalar
pmvoaCtrlWarmReset = _PmvoaCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 5, 3),
    _PmvoaCtrlWarmReset_Type()
)
pmvoaCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlWarmReset.setStatus("current")
_PmvoaCtrlLoadSwBank1_Type = EkiOnOff
_PmvoaCtrlLoadSwBank1_Object = MibScalar
pmvoaCtrlLoadSwBank1 = _PmvoaCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 5, 5),
    _PmvoaCtrlLoadSwBank1_Type()
)
pmvoaCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlLoadSwBank1.setStatus("current")
_PmvoaCtrlLoadSwBank2_Type = EkiOnOff
_PmvoaCtrlLoadSwBank2_Object = MibScalar
pmvoaCtrlLoadSwBank2 = _PmvoaCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 5, 6),
    _PmvoaCtrlLoadSwBank2_Type()
)
pmvoaCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlLoadSwBank2.setStatus("current")
_PmvoaCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmvoaCtrlgwMgnt = _PmvoaCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 6)
)
_PmvoaCtrlCurrentGwReset_Type = EkiOnOff
_PmvoaCtrlCurrentGwReset_Object = MibScalar
pmvoaCtrlCurrentGwReset = _PmvoaCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 6, 1),
    _PmvoaCtrlCurrentGwReset_Type()
)
pmvoaCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlCurrentGwReset.setStatus("current")
_PmvoaCtrlLoadGwBank1_Type = EkiOnOff
_PmvoaCtrlLoadGwBank1_Object = MibScalar
pmvoaCtrlLoadGwBank1 = _PmvoaCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 6, 5),
    _PmvoaCtrlLoadGwBank1_Type()
)
pmvoaCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlLoadGwBank1.setStatus("current")
_PmvoaCtrlLoadGwBank2_Type = EkiOnOff
_PmvoaCtrlLoadGwBank2_Object = MibScalar
pmvoaCtrlLoadGwBank2 = _PmvoaCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 6, 6),
    _PmvoaCtrlLoadGwBank2_Type()
)
pmvoaCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlLoadGwBank2.setStatus("current")
_PmvoaCtrlLoadGwBank3_Type = EkiOnOff
_PmvoaCtrlLoadGwBank3_Object = MibScalar
pmvoaCtrlLoadGwBank3 = _PmvoaCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 6, 7),
    _PmvoaCtrlLoadGwBank3_Type()
)
pmvoaCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlLoadGwBank3.setStatus("current")
_PmvoaCtrlLoadGwBank4_Type = EkiOnOff
_PmvoaCtrlLoadGwBank4_Object = MibScalar
pmvoaCtrlLoadGwBank4 = _PmvoaCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 6, 8),
    _PmvoaCtrlLoadGwBank4_Type()
)
pmvoaCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlLoadGwBank4.setStatus("current")
_PmvoaCtrlledTest_ObjectIdentity = ObjectIdentity
pmvoaCtrlledTest = _PmvoaCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 72)
)
_PmvoaCtrlGreenLed_Type = EkiOnOff
_PmvoaCtrlGreenLed_Object = MibScalar
pmvoaCtrlGreenLed = _PmvoaCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 72, 1),
    _PmvoaCtrlGreenLed_Type()
)
pmvoaCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlGreenLed.setStatus("current")
_PmvoaCtrlRedLed_Type = EkiOnOff
_PmvoaCtrlRedLed_Object = MibScalar
pmvoaCtrlRedLed = _PmvoaCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 72, 2),
    _PmvoaCtrlRedLed_Type()
)
pmvoaCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlRedLed.setStatus("current")
_PmvoaCtrlLedOff_Type = EkiOnOff
_PmvoaCtrlLedOff_Object = MibScalar
pmvoaCtrlLedOff = _PmvoaCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 1, 72, 3),
    _PmvoaCtrlLedOff_Type()
)
pmvoaCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCtrlLedOff.setStatus("current")
_PmvoaCtrlClient_ObjectIdentity = ObjectIdentity
pmvoaCtrlClient = _PmvoaCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 2)
)
_PmvoaCtrlLine_ObjectIdentity = ObjectIdentity
pmvoaCtrlLine = _PmvoaCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 6, 3)
)
_Pmvoari_ObjectIdentity = ObjectIdentity
pmvoari = _Pmvoari_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7)
)
_PmvoariTable_ObjectIdentity = ObjectIdentity
pmvoariTable = _PmvoariTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 1)
)
_PmvoaRinvLineTable_Object = MibTable
pmvoaRinvLineTable = _PmvoaRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmvoaRinvLineTable.setStatus("current")
_PmvoaRinvLineEntry_Object = MibTableRow
pmvoaRinvLineEntry = _PmvoaRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 1, 2, 1)
)
pmvoaRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmvoaRinvLineEntry.setStatus("current")


class _PmvoaRinvLineIndex_Type(Integer32):
    """Custom type pmvoaRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmvoaRinvLineIndex_Type.__name__ = "Integer32"
_PmvoaRinvLineIndex_Object = MibTableColumn
pmvoaRinvLineIndex = _PmvoaRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 1, 2, 1, 1),
    _PmvoaRinvLineIndex_Type()
)
pmvoaRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaRinvLineIndex.setStatus("current")
_PmvoaRinvxfpLine_Type = DisplayString
_PmvoaRinvxfpLine_Object = MibTableColumn
pmvoaRinvxfpLine = _PmvoaRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 1, 2, 1, 2),
    _PmvoaRinvxfpLine_Type()
)
pmvoaRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaRinvxfpLine.setStatus("current")
_PmvoaRinvReloadInventory_Type = EkiOnOff
_PmvoaRinvReloadInventory_Object = MibScalar
pmvoaRinvReloadInventory = _PmvoaRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 2),
    _PmvoaRinvReloadInventory_Type()
)
pmvoaRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaRinvReloadInventory.setStatus("current")
_PmvoaRinvHwPlatform_Type = DisplayString
_PmvoaRinvHwPlatform_Object = MibScalar
pmvoaRinvHwPlatform = _PmvoaRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 3),
    _PmvoaRinvHwPlatform_Type()
)
pmvoaRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaRinvHwPlatform.setStatus("current")
_PmvoaRinvModulePlatform_Type = DisplayString
_PmvoaRinvModulePlatform_Object = MibScalar
pmvoaRinvModulePlatform = _PmvoaRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 4),
    _PmvoaRinvModulePlatform_Type()
)
pmvoaRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaRinvModulePlatform.setStatus("current")
_PmvoaRinvSwPlatform_Type = DisplayString
_PmvoaRinvSwPlatform_Object = MibScalar
pmvoaRinvSwPlatform = _PmvoaRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 5),
    _PmvoaRinvSwPlatform_Type()
)
pmvoaRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaRinvSwPlatform.setStatus("current")
_PmvoaRinvGwPlatform_Type = DisplayString
_PmvoaRinvGwPlatform_Object = MibScalar
pmvoaRinvGwPlatform = _PmvoaRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 7, 6),
    _PmvoaRinvGwPlatform_Type()
)
pmvoaRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaRinvGwPlatform.setStatus("current")
_Pmvoadownload_ObjectIdentity = ObjectIdentity
pmvoadownload = _Pmvoadownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8)
)
_PmvoaDwlOther_ObjectIdentity = ObjectIdentity
pmvoaDwlOther = _PmvoaDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1)
)
_PmvoaDwlrestartProcess_ObjectIdentity = ObjectIdentity
pmvoaDwlrestartProcess = _PmvoaDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 0)
)
_PmvoaDwlWarmRestartProcessed_Type = EkiOnOff
_PmvoaDwlWarmRestartProcessed_Object = MibScalar
pmvoaDwlWarmRestartProcessed = _PmvoaDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 0, 1),
    _PmvoaDwlWarmRestartProcessed_Type()
)
pmvoaDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlWarmRestartProcessed.setStatus("current")
_PmvoaDwlColdRestartProcessed_Type = EkiOnOff
_PmvoaDwlColdRestartProcessed_Object = MibScalar
pmvoaDwlColdRestartProcessed = _PmvoaDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 0, 2),
    _PmvoaDwlColdRestartProcessed_Type()
)
pmvoaDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlColdRestartProcessed.setStatus("current")
_PmvoaDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmvoaDwlswBanksUsed = _PmvoaDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 1)
)
_PmvoaDwlSwBank1Used_Type = EkiOnOff
_PmvoaDwlSwBank1Used_Object = MibScalar
pmvoaDwlSwBank1Used = _PmvoaDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 1, 1),
    _PmvoaDwlSwBank1Used_Type()
)
pmvoaDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlSwBank1Used.setStatus("current")
_PmvoaDwlSwBank2Used_Type = EkiOnOff
_PmvoaDwlSwBank2Used_Object = MibScalar
pmvoaDwlSwBank2Used = _PmvoaDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 1, 2),
    _PmvoaDwlSwBank2Used_Type()
)
pmvoaDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlSwBank2Used.setStatus("current")
_PmvoaDwlSwBank1Notempty_Type = EkiOnOff
_PmvoaDwlSwBank1Notempty_Object = MibScalar
pmvoaDwlSwBank1Notempty = _PmvoaDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 1, 5),
    _PmvoaDwlSwBank1Notempty_Type()
)
pmvoaDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlSwBank1Notempty.setStatus("current")
_PmvoaDwlSwBank2Notempty_Type = EkiOnOff
_PmvoaDwlSwBank2Notempty_Object = MibScalar
pmvoaDwlSwBank2Notempty = _PmvoaDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 1, 6),
    _PmvoaDwlSwBank2Notempty_Type()
)
pmvoaDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlSwBank2Notempty.setStatus("current")
_PmvoaDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmvoaDwlgwBanksUsed = _PmvoaDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2)
)
_PmvoaDwlGwBank1Used_Type = EkiOnOff
_PmvoaDwlGwBank1Used_Object = MibScalar
pmvoaDwlGwBank1Used = _PmvoaDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 1),
    _PmvoaDwlGwBank1Used_Type()
)
pmvoaDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank1Used.setStatus("current")
_PmvoaDwlGwBank2Used_Type = EkiOnOff
_PmvoaDwlGwBank2Used_Object = MibScalar
pmvoaDwlGwBank2Used = _PmvoaDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 2),
    _PmvoaDwlGwBank2Used_Type()
)
pmvoaDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank2Used.setStatus("current")
_PmvoaDwlGwBank3Used_Type = EkiOnOff
_PmvoaDwlGwBank3Used_Object = MibScalar
pmvoaDwlGwBank3Used = _PmvoaDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 3),
    _PmvoaDwlGwBank3Used_Type()
)
pmvoaDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank3Used.setStatus("current")
_PmvoaDwlGwBank4Used_Type = EkiOnOff
_PmvoaDwlGwBank4Used_Object = MibScalar
pmvoaDwlGwBank4Used = _PmvoaDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 4),
    _PmvoaDwlGwBank4Used_Type()
)
pmvoaDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank4Used.setStatus("current")
_PmvoaDwlGwBank1Notempty_Type = EkiOnOff
_PmvoaDwlGwBank1Notempty_Object = MibScalar
pmvoaDwlGwBank1Notempty = _PmvoaDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 5),
    _PmvoaDwlGwBank1Notempty_Type()
)
pmvoaDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank1Notempty.setStatus("current")
_PmvoaDwlGwBank2Notempty_Type = EkiOnOff
_PmvoaDwlGwBank2Notempty_Object = MibScalar
pmvoaDwlGwBank2Notempty = _PmvoaDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 6),
    _PmvoaDwlGwBank2Notempty_Type()
)
pmvoaDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank2Notempty.setStatus("current")
_PmvoaDwlGwBank3Notempty_Type = EkiOnOff
_PmvoaDwlGwBank3Notempty_Object = MibScalar
pmvoaDwlGwBank3Notempty = _PmvoaDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 7),
    _PmvoaDwlGwBank3Notempty_Type()
)
pmvoaDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank3Notempty.setStatus("current")
_PmvoaDwlGwBank4Notempty_Type = EkiOnOff
_PmvoaDwlGwBank4Notempty_Object = MibScalar
pmvoaDwlGwBank4Notempty = _PmvoaDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 1, 2, 8),
    _PmvoaDwlGwBank4Notempty_Type()
)
pmvoaDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaDwlGwBank4Notempty.setStatus("current")
_PmvoaDwlClient_ObjectIdentity = ObjectIdentity
pmvoaDwlClient = _PmvoaDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 2)
)
_PmvoaDwlLine_ObjectIdentity = ObjectIdentity
pmvoaDwlLine = _PmvoaDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 8, 3)
)
_PmvoaConfig_ObjectIdentity = ObjectIdentity
pmvoaConfig = _PmvoaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9)
)
_PmvoaCfgStartup_ObjectIdentity = ObjectIdentity
pmvoaCfgStartup = _PmvoaCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1)
)
_PmvoaCfgLinexr1StartupTable_Object = MibTable
pmvoaCfgLinexr1StartupTable = _PmvoaCfgLinexr1StartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pmvoaCfgLinexr1StartupTable.setStatus("current")
_PmvoaCfgLinexr1StartupEntry_Object = MibTableRow
pmvoaCfgLinexr1StartupEntry = _PmvoaCfgLinexr1StartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1, 1)
)
pmvoaCfgLinexr1StartupEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaCfgLinexr1StartupIndex"),
)
if mibBuilder.loadTexts:
    pmvoaCfgLinexr1StartupEntry.setStatus("current")


class _PmvoaCfgLinexr1StartupIndex_Type(Integer32):
    """Custom type pmvoaCfgLinexr1StartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaCfgLinexr1StartupIndex_Type.__name__ = "Integer32"
_PmvoaCfgLinexr1StartupIndex_Object = MibTableColumn
pmvoaCfgLinexr1StartupIndex = _PmvoaCfgLinexr1StartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1, 1, 1),
    _PmvoaCfgLinexr1StartupIndex_Type()
)
pmvoaCfgLinexr1StartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaCfgLinexr1StartupIndex.setStatus("current")


class _PmvoaCfgSfpModePortn_Type(Unsigned32):
    """Custom type pmvoaCfgSfpModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmvoaCfgSfpModePortn_Type.__name__ = "Unsigned32"
_PmvoaCfgSfpModePortn_Object = MibTableColumn
pmvoaCfgSfpModePortn = _PmvoaCfgSfpModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1, 1, 3),
    _PmvoaCfgSfpModePortn_Type()
)
pmvoaCfgSfpModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgSfpModePortn.setStatus("current")


class _PmvoaCfgAttenuationCtrlPortn_Type(Unsigned32):
    """Custom type pmvoaCfgAttenuationCtrlPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmvoaCfgAttenuationCtrlPortn_Type.__name__ = "Unsigned32"
_PmvoaCfgAttenuationCtrlPortn_Object = MibTableColumn
pmvoaCfgAttenuationCtrlPortn = _PmvoaCfgAttenuationCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1, 1, 4),
    _PmvoaCfgAttenuationCtrlPortn_Type()
)
pmvoaCfgAttenuationCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgAttenuationCtrlPortn.setStatus("current")


class _PmvoaCfgPowerCtrlPortn_Type(Unsigned32):
    """Custom type pmvoaCfgPowerCtrlPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmvoaCfgPowerCtrlPortn_Type.__name__ = "Unsigned32"
_PmvoaCfgPowerCtrlPortn_Object = MibTableColumn
pmvoaCfgPowerCtrlPortn = _PmvoaCfgPowerCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1, 1, 5),
    _PmvoaCfgPowerCtrlPortn_Type()
)
pmvoaCfgPowerCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgPowerCtrlPortn.setStatus("current")


class _PmvoaCfgLosInputThresholdPortn_Type(Unsigned32):
    """Custom type pmvoaCfgLosInputThresholdPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmvoaCfgLosInputThresholdPortn_Type.__name__ = "Unsigned32"
_PmvoaCfgLosInputThresholdPortn_Object = MibTableColumn
pmvoaCfgLosInputThresholdPortn = _PmvoaCfgLosInputThresholdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1, 1, 6),
    _PmvoaCfgLosInputThresholdPortn_Type()
)
pmvoaCfgLosInputThresholdPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgLosInputThresholdPortn.setStatus("current")


class _PmvoaCfgInsertionLossValuePortn_Type(Unsigned32):
    """Custom type pmvoaCfgInsertionLossValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmvoaCfgInsertionLossValuePortn_Type.__name__ = "Unsigned32"
_PmvoaCfgInsertionLossValuePortn_Object = MibTableColumn
pmvoaCfgInsertionLossValuePortn = _PmvoaCfgInsertionLossValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 1, 1, 1, 7),
    _PmvoaCfgInsertionLossValuePortn_Type()
)
pmvoaCfgInsertionLossValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgInsertionLossValuePortn.setStatus("current")
_PmvoaCfgLabels_ObjectIdentity = ObjectIdentity
pmvoaCfgLabels = _PmvoaCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2)
)
_PmvoaCfgLabelclientTable_Object = MibTable
pmvoaCfgLabelclientTable = _PmvoaCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pmvoaCfgLabelclientTable.setStatus("current")
_PmvoaCfgLabelclientEntry_Object = MibTableRow
pmvoaCfgLabelclientEntry = _PmvoaCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 1, 1)
)
pmvoaCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmvoaCfgLabelclientEntry.setStatus("current")


class _PmvoaCfgLabelclientIndex_Type(Integer32):
    """Custom type pmvoaCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmvoaCfgLabelclientIndex_Object = MibTableColumn
pmvoaCfgLabelclientIndex = _PmvoaCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 1, 1, 1),
    _PmvoaCfgLabelclientIndex_Type()
)
pmvoaCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaCfgLabelclientIndex.setStatus("current")


class _PmvoaCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmvoaCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmvoaCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmvoaCfgLabelclientPortn_Object = MibTableColumn
pmvoaCfgLabelclientPortn = _PmvoaCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 1, 1, 3),
    _PmvoaCfgLabelclientPortn_Type()
)
pmvoaCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgLabelclientPortn.setStatus("current")
_PmvoaCfgLabellineTable_Object = MibTable
pmvoaCfgLabellineTable = _PmvoaCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pmvoaCfgLabellineTable.setStatus("current")
_PmvoaCfgLabellineEntry_Object = MibTableRow
pmvoaCfgLabellineEntry = _PmvoaCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 2, 1)
)
pmvoaCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmvoa-MIB", "pmvoaCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmvoaCfgLabellineEntry.setStatus("current")


class _PmvoaCfgLabellineIndex_Type(Integer32):
    """Custom type pmvoaCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmvoaCfgLabellineIndex_Type.__name__ = "Integer32"
_PmvoaCfgLabellineIndex_Object = MibTableColumn
pmvoaCfgLabellineIndex = _PmvoaCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 2, 1, 1),
    _PmvoaCfgLabellineIndex_Type()
)
pmvoaCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoaCfgLabellineIndex.setStatus("current")


class _PmvoaCfgLabellinePortn_Type(DisplayString):
    """Custom type pmvoaCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmvoaCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmvoaCfgLabellinePortn_Object = MibTableColumn
pmvoaCfgLabellinePortn = _PmvoaCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 2, 2, 1, 3),
    _PmvoaCfgLabellinePortn_Type()
)
pmvoaCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgLabellinePortn.setStatus("current")
_PmvoaCfgWriteConfiguration_Type = EkiOnOff
_PmvoaCfgWriteConfiguration_Object = MibScalar
pmvoaCfgWriteConfiguration = _PmvoaCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 9, 257),
    _PmvoaCfgWriteConfiguration_Type()
)
pmvoaCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvoaCfgWriteConfiguration.setStatus("current")
_Pmvoatraps_ObjectIdentity = ObjectIdentity
pmvoatraps = _Pmvoatraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10)
)


class _PmvoatrapPortNumber_Type(Integer32):
    """Custom type pmvoatrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmvoatrapPortNumber_Type.__name__ = "Integer32"
_PmvoatrapPortNumber_Object = MibScalar
pmvoatrapPortNumber = _PmvoatrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10, 2),
    _PmvoatrapPortNumber_Type()
)
pmvoatrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoatrapPortNumber.setStatus("current")


class _PmvoatrapLineNumber_Type(Integer32):
    """Custom type pmvoatrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmvoatrapLineNumber_Type.__name__ = "Integer32"
_PmvoatrapLineNumber_Object = MibScalar
pmvoatrapLineNumber = _PmvoatrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10, 3),
    _PmvoatrapLineNumber_Type()
)
pmvoatrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoatrapLineNumber.setStatus("current")


class _PmvoatrapBoardNumber_Type(Integer32):
    """Custom type pmvoatrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmvoatrapBoardNumber_Type.__name__ = "Integer32"
_PmvoatrapBoardNumber_Object = MibScalar
pmvoatrapBoardNumber = _PmvoatrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10, 4),
    _PmvoatrapBoardNumber_Type()
)
pmvoatrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmvoatrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmvoaLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10, 34)
)
pmvoaLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmvoa-MIB", "pmvoaAlmLineFailPortn"),
        ("EKINOPS-Pmvoa-MIB", "pmvoaAlmLineHwFailPortn"),
        ("EKINOPS-Pmvoa-MIB", "pmvoatrapLineNumber"),
        ("EKINOPS-Pmvoa-MIB", "pmvoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmvoaLineTrapCritGoesOn.setStatus(
        "current"
    )

pmvoaLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10, 35)
)
pmvoaLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmvoa-MIB", "pmvoaAlmLineFailPortn"),
        ("EKINOPS-Pmvoa-MIB", "pmvoaAlmLineHwFailPortn"),
        ("EKINOPS-Pmvoa-MIB", "pmvoatrapLineNumber"),
        ("EKINOPS-Pmvoa-MIB", "pmvoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmvoaLineTrapCritGoesOff.setStatus(
        "current"
    )

pmvoaPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10, 50)
)
pmvoaPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmvoa-MIB", "pmvoaAlmDefFuseB"),
        ("EKINOPS-Pmvoa-MIB", "pmvoaAlmDefFuseA"),
        ("EKINOPS-Pmvoa-MIB", "pmvoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmvoaPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmvoaPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 84, 10, 51)
)
pmvoaPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmvoa-MIB", "pmvoaAlmDefFuseB"),
        ("EKINOPS-Pmvoa-MIB", "pmvoaAlmDefFuseA"),
        ("EKINOPS-Pmvoa-MIB", "pmvoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmvoaPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmvoa-MIB",
    **{"PmvoaMode": PmvoaMode,
       "modulePmvoa": modulePmvoa,
       "pmvoaalarms": pmvoaalarms,
       "pmvoaAlmOther": pmvoaAlmOther,
       "pmvoaAlmOtherNurg": pmvoaAlmOtherNurg,
       "pmvoaAlmsynthAlm2": pmvoaAlmsynthAlm2,
       "pmvoaAlmConfTableSave": pmvoaAlmConfTableSave,
       "pmvoaAlmInvUpload": pmvoaAlmInvUpload,
       "pmvoaAlmConfTableLoad": pmvoaAlmConfTableLoad,
       "pmvoaAlmCorrelatOff": pmvoaAlmCorrelatOff,
       "pmvoaAlmOtherUrg": pmvoaAlmOtherUrg,
       "pmvoaAlmOtherCrit": pmvoaAlmOtherCrit,
       "pmvoaAlmsynthAlm0": pmvoaAlmsynthAlm0,
       "pmvoaAlmModGlobFail": pmvoaAlmModGlobFail,
       "pmvoaAlmDefFuseA": pmvoaAlmDefFuseA,
       "pmvoaAlmDefFuseB": pmvoaAlmDefFuseB,
       "pmvoaAlmClient": pmvoaAlmClient,
       "pmvoaAlmClientNurg": pmvoaAlmClientNurg,
       "pmvoaAlmClientUrg": pmvoaAlmClientUrg,
       "pmvoaAlmClientCrit": pmvoaAlmClientCrit,
       "pmvoaAlmLine": pmvoaAlmLine,
       "pmvoaAlmLineNurg": pmvoaAlmLineNurg,
       "pmvoaAlmLineUrg": pmvoaAlmLineUrg,
       "pmvoaAlmLineCrit": pmvoaAlmLineCrit,
       "pmvoaAlmsynthAlmLineTable": pmvoaAlmsynthAlmLineTable,
       "pmvoaAlmsynthAlmLineEntry": pmvoaAlmsynthAlmLineEntry,
       "pmvoaAlmsynthAlmLineIndex": pmvoaAlmsynthAlmLineIndex,
       "pmvoaAlmLineSfpVoaAbsentPortn": pmvoaAlmLineSfpVoaAbsentPortn,
       "pmvoaAlmLineHwFailPortn": pmvoaAlmLineHwFailPortn,
       "pmvoaAlmLineOosPortn": pmvoaAlmLineOosPortn,
       "pmvoaAlmLineFailPortn": pmvoaAlmLineFailPortn,
       "pmvoaAlmlineAlmTable": pmvoaAlmlineAlmTable,
       "pmvoaAlmlineAlmEntry": pmvoaAlmlineAlmEntry,
       "pmvoaAlmlineAlmIndex": pmvoaAlmlineAlmIndex,
       "pmvoaAlmOutputErrorPortn": pmvoaAlmOutputErrorPortn,
       "pmvoaAlmLossOutputPowerPortn": pmvoaAlmLossOutputPowerPortn,
       "pmvoaAlmTempHighAlarmPortn": pmvoaAlmTempHighAlarmPortn,
       "pmvoaAlmTempLowAlarmPortn": pmvoaAlmTempLowAlarmPortn,
       "pmvoaAlmLossInputPowerPortn": pmvoaAlmLossInputPowerPortn,
       "pmvoameasures": pmvoameasures,
       "pmvoaMesrOther": pmvoaMesrOther,
       "pmvoaMesrClient": pmvoaMesrClient,
       "pmvoaMesrLine": pmvoaMesrLine,
       "pmvoaMesrlineSfpTempTable": pmvoaMesrlineSfpTempTable,
       "pmvoaMesrlineSfpTempEntry": pmvoaMesrlineSfpTempEntry,
       "pmvoaMesrlineSfpTempIndex": pmvoaMesrlineSfpTempIndex,
       "pmvoaMesrlineSfpTempPortn": pmvoaMesrlineSfpTempPortn,
       "pmvoaMesrlinePoutTable": pmvoaMesrlinePoutTable,
       "pmvoaMesrlinePoutEntry": pmvoaMesrlinePoutEntry,
       "pmvoaMesrlinePoutIndex": pmvoaMesrlinePoutIndex,
       "pmvoaMesrlinePoutPortn": pmvoaMesrlinePoutPortn,
       "pmvoaMesrlineEstPinTable": pmvoaMesrlineEstPinTable,
       "pmvoaMesrlineEstPinEntry": pmvoaMesrlineEstPinEntry,
       "pmvoaMesrlineEstPinIndex": pmvoaMesrlineEstPinIndex,
       "pmvoaMesrlineEstPinPortn": pmvoaMesrlineEstPinPortn,
       "pmvoacontrolsWrite": pmvoacontrolsWrite,
       "pmvoaCtrlOther": pmvoaCtrlOther,
       "pmvoaCtrlconfMgnt1": pmvoaCtrlconfMgnt1,
       "pmvoaCtrlConf1Load1": pmvoaCtrlConf1Load1,
       "pmvoaCtrlConf2Load1": pmvoaCtrlConf2Load1,
       "pmvoaCtrlConf2Flash1": pmvoaCtrlConf2Flash1,
       "pmvoaCtrlConf2Clear1": pmvoaCtrlConf2Clear1,
       "pmvoaCtrlsynth4": pmvoaCtrlsynth4,
       "pmvoaCtrlCorrelatOn": pmvoaCtrlCorrelatOn,
       "pmvoaCtrlCorrelatOff": pmvoaCtrlCorrelatOff,
       "pmvoaCtrlswMgnt": pmvoaCtrlswMgnt,
       "pmvoaCtrlColdReset": pmvoaCtrlColdReset,
       "pmvoaCtrlWarmReset": pmvoaCtrlWarmReset,
       "pmvoaCtrlLoadSwBank1": pmvoaCtrlLoadSwBank1,
       "pmvoaCtrlLoadSwBank2": pmvoaCtrlLoadSwBank2,
       "pmvoaCtrlgwMgnt": pmvoaCtrlgwMgnt,
       "pmvoaCtrlCurrentGwReset": pmvoaCtrlCurrentGwReset,
       "pmvoaCtrlLoadGwBank1": pmvoaCtrlLoadGwBank1,
       "pmvoaCtrlLoadGwBank2": pmvoaCtrlLoadGwBank2,
       "pmvoaCtrlLoadGwBank3": pmvoaCtrlLoadGwBank3,
       "pmvoaCtrlLoadGwBank4": pmvoaCtrlLoadGwBank4,
       "pmvoaCtrlledTest": pmvoaCtrlledTest,
       "pmvoaCtrlGreenLed": pmvoaCtrlGreenLed,
       "pmvoaCtrlRedLed": pmvoaCtrlRedLed,
       "pmvoaCtrlLedOff": pmvoaCtrlLedOff,
       "pmvoaCtrlClient": pmvoaCtrlClient,
       "pmvoaCtrlLine": pmvoaCtrlLine,
       "pmvoari": pmvoari,
       "pmvoariTable": pmvoariTable,
       "pmvoaRinvLineTable": pmvoaRinvLineTable,
       "pmvoaRinvLineEntry": pmvoaRinvLineEntry,
       "pmvoaRinvLineIndex": pmvoaRinvLineIndex,
       "pmvoaRinvxfpLine": pmvoaRinvxfpLine,
       "pmvoaRinvReloadInventory": pmvoaRinvReloadInventory,
       "pmvoaRinvHwPlatform": pmvoaRinvHwPlatform,
       "pmvoaRinvModulePlatform": pmvoaRinvModulePlatform,
       "pmvoaRinvSwPlatform": pmvoaRinvSwPlatform,
       "pmvoaRinvGwPlatform": pmvoaRinvGwPlatform,
       "pmvoadownload": pmvoadownload,
       "pmvoaDwlOther": pmvoaDwlOther,
       "pmvoaDwlrestartProcess": pmvoaDwlrestartProcess,
       "pmvoaDwlWarmRestartProcessed": pmvoaDwlWarmRestartProcessed,
       "pmvoaDwlColdRestartProcessed": pmvoaDwlColdRestartProcessed,
       "pmvoaDwlswBanksUsed": pmvoaDwlswBanksUsed,
       "pmvoaDwlSwBank1Used": pmvoaDwlSwBank1Used,
       "pmvoaDwlSwBank2Used": pmvoaDwlSwBank2Used,
       "pmvoaDwlSwBank1Notempty": pmvoaDwlSwBank1Notempty,
       "pmvoaDwlSwBank2Notempty": pmvoaDwlSwBank2Notempty,
       "pmvoaDwlgwBanksUsed": pmvoaDwlgwBanksUsed,
       "pmvoaDwlGwBank1Used": pmvoaDwlGwBank1Used,
       "pmvoaDwlGwBank2Used": pmvoaDwlGwBank2Used,
       "pmvoaDwlGwBank3Used": pmvoaDwlGwBank3Used,
       "pmvoaDwlGwBank4Used": pmvoaDwlGwBank4Used,
       "pmvoaDwlGwBank1Notempty": pmvoaDwlGwBank1Notempty,
       "pmvoaDwlGwBank2Notempty": pmvoaDwlGwBank2Notempty,
       "pmvoaDwlGwBank3Notempty": pmvoaDwlGwBank3Notempty,
       "pmvoaDwlGwBank4Notempty": pmvoaDwlGwBank4Notempty,
       "pmvoaDwlClient": pmvoaDwlClient,
       "pmvoaDwlLine": pmvoaDwlLine,
       "pmvoaConfig": pmvoaConfig,
       "pmvoaCfgStartup": pmvoaCfgStartup,
       "pmvoaCfgLinexr1StartupTable": pmvoaCfgLinexr1StartupTable,
       "pmvoaCfgLinexr1StartupEntry": pmvoaCfgLinexr1StartupEntry,
       "pmvoaCfgLinexr1StartupIndex": pmvoaCfgLinexr1StartupIndex,
       "pmvoaCfgSfpModePortn": pmvoaCfgSfpModePortn,
       "pmvoaCfgAttenuationCtrlPortn": pmvoaCfgAttenuationCtrlPortn,
       "pmvoaCfgPowerCtrlPortn": pmvoaCfgPowerCtrlPortn,
       "pmvoaCfgLosInputThresholdPortn": pmvoaCfgLosInputThresholdPortn,
       "pmvoaCfgInsertionLossValuePortn": pmvoaCfgInsertionLossValuePortn,
       "pmvoaCfgLabels": pmvoaCfgLabels,
       "pmvoaCfgLabelclientTable": pmvoaCfgLabelclientTable,
       "pmvoaCfgLabelclientEntry": pmvoaCfgLabelclientEntry,
       "pmvoaCfgLabelclientIndex": pmvoaCfgLabelclientIndex,
       "pmvoaCfgLabelclientPortn": pmvoaCfgLabelclientPortn,
       "pmvoaCfgLabellineTable": pmvoaCfgLabellineTable,
       "pmvoaCfgLabellineEntry": pmvoaCfgLabellineEntry,
       "pmvoaCfgLabellineIndex": pmvoaCfgLabellineIndex,
       "pmvoaCfgLabellinePortn": pmvoaCfgLabellinePortn,
       "pmvoaCfgWriteConfiguration": pmvoaCfgWriteConfiguration,
       "pmvoatraps": pmvoatraps,
       "pmvoatrapPortNumber": pmvoatrapPortNumber,
       "pmvoatrapLineNumber": pmvoatrapLineNumber,
       "pmvoatrapBoardNumber": pmvoatrapBoardNumber,
       "pmvoaLineTrapCritGoesOn": pmvoaLineTrapCritGoesOn,
       "pmvoaLineTrapCritGoesOff": pmvoaLineTrapCritGoesOff,
       "pmvoaPowerTrapUrgentGoesOn": pmvoaPowerTrapUrgentGoesOn,
       "pmvoaPowerTrapUrgentGoesOff": pmvoaPowerTrapUrgentGoesOff}
)
