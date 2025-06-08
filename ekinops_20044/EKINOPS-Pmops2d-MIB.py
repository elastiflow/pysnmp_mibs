# SNMP MIB module (EKINOPS-Pmops2d-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmops2d-MIB.mib
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

modulePmops2d = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71)
)
if mibBuilder.loadTexts:
    modulePmops2d.setRevisions(
        ("2015-06-25 00:00",
         "2015-06-25 00:00",
         "2016-03-04 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmops2dSwitchMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("switchManual1", 1),
          ("switchManual2", 2),
          ("switchAuto", 4),
          ("switchAutoRevertive", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Pmops2dalarms_ObjectIdentity = ObjectIdentity
pmops2dalarms = _Pmops2dalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2)
)
_Pmops2dAlmOther_ObjectIdentity = ObjectIdentity
pmops2dAlmOther = _Pmops2dAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1)
)
_Pmops2dAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmops2dAlmOtherNurg = _Pmops2dAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 1)
)
_Pmops2dAlmswitchOutOfService_ObjectIdentity = ObjectIdentity
pmops2dAlmswitchOutOfService = _Pmops2dAlmswitchOutOfService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 1, 64)
)
_Pmops2dAlmOpsaOutofservice_Type = EkiOnOff
_Pmops2dAlmOpsaOutofservice_Object = MibScalar
pmops2dAlmOpsaOutofservice = _Pmops2dAlmOpsaOutofservice_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 1, 64, 1),
    _Pmops2dAlmOpsaOutofservice_Type()
)
pmops2dAlmOpsaOutofservice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmOpsaOutofservice.setStatus("current")
_Pmops2dAlmOpsbOutofservice_Type = EkiOnOff
_Pmops2dAlmOpsbOutofservice_Object = MibScalar
pmops2dAlmOpsbOutofservice = _Pmops2dAlmOpsbOutofservice_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 1, 64, 2),
    _Pmops2dAlmOpsbOutofservice_Type()
)
pmops2dAlmOpsbOutofservice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmOpsbOutofservice.setStatus("current")
_Pmops2dAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmops2dAlmOtherUrg = _Pmops2dAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 2)
)
_Pmops2dAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmops2dAlmOtherCrit = _Pmops2dAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 3)
)
_Pmops2dAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmops2dAlmsynthAlm0 = _Pmops2dAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 3, 0)
)
_Pmops2dAlmModuleGlobFailure_Type = EkiOnOff
_Pmops2dAlmModuleGlobFailure_Object = MibScalar
pmops2dAlmModuleGlobFailure = _Pmops2dAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 3, 0, 9),
    _Pmops2dAlmModuleGlobFailure_Type()
)
pmops2dAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmModuleGlobFailure.setStatus("current")
_Pmops2dAlmDefFuseA_Type = EkiOnOff
_Pmops2dAlmDefFuseA_Object = MibScalar
pmops2dAlmDefFuseA = _Pmops2dAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 3, 0, 15),
    _Pmops2dAlmDefFuseA_Type()
)
pmops2dAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmDefFuseA.setStatus("current")
_Pmops2dAlmDefFuseB_Type = EkiOnOff
_Pmops2dAlmDefFuseB_Object = MibScalar
pmops2dAlmDefFuseB = _Pmops2dAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 1, 3, 0, 16),
    _Pmops2dAlmDefFuseB_Type()
)
pmops2dAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmDefFuseB.setStatus("current")
_Pmops2dAlmClient_ObjectIdentity = ObjectIdentity
pmops2dAlmClient = _Pmops2dAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2)
)
_Pmops2dAlmClientNurg_ObjectIdentity = ObjectIdentity
pmops2dAlmClientNurg = _Pmops2dAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 1)
)
_Pmops2dAlmClientUrg_ObjectIdentity = ObjectIdentity
pmops2dAlmClientUrg = _Pmops2dAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 2)
)
_Pmops2dAlmclientComAlarmTable_Object = MibTable
pmops2dAlmclientComAlarmTable = _Pmops2dAlmclientComAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 2, 24)
)
if mibBuilder.loadTexts:
    pmops2dAlmclientComAlarmTable.setStatus("current")
_Pmops2dAlmclientComAlarmEntry_Object = MibTableRow
pmops2dAlmclientComAlarmEntry = _Pmops2dAlmclientComAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 2, 24, 1)
)
pmops2dAlmclientComAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dAlmclientComAlarmIndex"),
)
if mibBuilder.loadTexts:
    pmops2dAlmclientComAlarmEntry.setStatus("current")


class _Pmops2dAlmclientComAlarmIndex_Type(Integer32):
    """Custom type pmops2dAlmclientComAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dAlmclientComAlarmIndex_Type.__name__ = "Integer32"
_Pmops2dAlmclientComAlarmIndex_Object = MibTableColumn
pmops2dAlmclientComAlarmIndex = _Pmops2dAlmclientComAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 2, 24, 1, 1),
    _Pmops2dAlmclientComAlarmIndex_Type()
)
pmops2dAlmclientComAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmclientComAlarmIndex.setStatus("current")
_Pmops2dAlmClientComSwitchFailPortn_Type = EkiOnOff
_Pmops2dAlmClientComSwitchFailPortn_Object = MibTableColumn
pmops2dAlmClientComSwitchFailPortn = _Pmops2dAlmClientComSwitchFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 2, 24, 1, 9),
    _Pmops2dAlmClientComSwitchFailPortn_Type()
)
pmops2dAlmClientComSwitchFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmClientComSwitchFailPortn.setStatus("current")
_Pmops2dAlmClientCrit_ObjectIdentity = ObjectIdentity
pmops2dAlmClientCrit = _Pmops2dAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 3)
)
_Pmops2dAlmsynthClientAlmTable_Object = MibTable
pmops2dAlmsynthClientAlmTable = _Pmops2dAlmsynthClientAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmops2dAlmsynthClientAlmTable.setStatus("current")
_Pmops2dAlmsynthClientAlmEntry_Object = MibTableRow
pmops2dAlmsynthClientAlmEntry = _Pmops2dAlmsynthClientAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 3, 8, 1)
)
pmops2dAlmsynthClientAlmEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dAlmsynthClientAlmIndex"),
)
if mibBuilder.loadTexts:
    pmops2dAlmsynthClientAlmEntry.setStatus("current")


class _Pmops2dAlmsynthClientAlmIndex_Type(Integer32):
    """Custom type pmops2dAlmsynthClientAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dAlmsynthClientAlmIndex_Type.__name__ = "Integer32"
_Pmops2dAlmsynthClientAlmIndex_Object = MibTableColumn
pmops2dAlmsynthClientAlmIndex = _Pmops2dAlmsynthClientAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 3, 8, 1, 1),
    _Pmops2dAlmsynthClientAlmIndex_Type()
)
pmops2dAlmsynthClientAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmsynthClientAlmIndex.setStatus("current")
_Pmops2dAlmClientHwFailAccPortn_Type = EkiOnOff
_Pmops2dAlmClientHwFailAccPortn_Object = MibTableColumn
pmops2dAlmClientHwFailAccPortn = _Pmops2dAlmClientHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 3, 8, 1, 5),
    _Pmops2dAlmClientHwFailAccPortn_Type()
)
pmops2dAlmClientHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmClientHwFailAccPortn.setStatus("current")
_Pmops2dAlmClientFailAccPortn_Type = EkiOnOff
_Pmops2dAlmClientFailAccPortn_Object = MibTableColumn
pmops2dAlmClientFailAccPortn = _Pmops2dAlmClientFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 2, 3, 8, 1, 13),
    _Pmops2dAlmClientFailAccPortn_Type()
)
pmops2dAlmClientFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmClientFailAccPortn.setStatus("current")
_Pmops2dAlmLine_ObjectIdentity = ObjectIdentity
pmops2dAlmLine = _Pmops2dAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3)
)
_Pmops2dAlmLineNurg_ObjectIdentity = ObjectIdentity
pmops2dAlmLineNurg = _Pmops2dAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1)
)
_Pmops2dAlmlineMeasWngTable_Object = MibTable
pmops2dAlmlineMeasWngTable = _Pmops2dAlmlineMeasWngTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1, 48)
)
if mibBuilder.loadTexts:
    pmops2dAlmlineMeasWngTable.setStatus("current")
_Pmops2dAlmlineMeasWngEntry_Object = MibTableRow
pmops2dAlmlineMeasWngEntry = _Pmops2dAlmlineMeasWngEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1, 48, 1)
)
pmops2dAlmlineMeasWngEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dAlmlineMeasWngIndex"),
)
if mibBuilder.loadTexts:
    pmops2dAlmlineMeasWngEntry.setStatus("current")


class _Pmops2dAlmlineMeasWngIndex_Type(Integer32):
    """Custom type pmops2dAlmlineMeasWngIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dAlmlineMeasWngIndex_Type.__name__ = "Integer32"
_Pmops2dAlmlineMeasWngIndex_Object = MibTableColumn
pmops2dAlmlineMeasWngIndex = _Pmops2dAlmlineMeasWngIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1, 48, 1, 1),
    _Pmops2dAlmlineMeasWngIndex_Type()
)
pmops2dAlmlineMeasWngIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmlineMeasWngIndex.setStatus("current")
_Pmops2dAlmLineTxPwrLowWngPortn_Type = EkiOnOff
_Pmops2dAlmLineTxPwrLowWngPortn_Object = MibTableColumn
pmops2dAlmLineTxPwrLowWngPortn = _Pmops2dAlmLineTxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1, 48, 1, 2),
    _Pmops2dAlmLineTxPwrLowWngPortn_Type()
)
pmops2dAlmLineTxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineTxPwrLowWngPortn.setStatus("current")
_Pmops2dAlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pmops2dAlmLineTxPwrHighWngPortn_Object = MibTableColumn
pmops2dAlmLineTxPwrHighWngPortn = _Pmops2dAlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1, 48, 1, 3),
    _Pmops2dAlmLineTxPwrHighWngPortn_Type()
)
pmops2dAlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineTxPwrHighWngPortn.setStatus("current")
_Pmops2dAlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pmops2dAlmLineRxPwrLowWngPortn_Object = MibTableColumn
pmops2dAlmLineRxPwrLowWngPortn = _Pmops2dAlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1, 48, 1, 4),
    _Pmops2dAlmLineRxPwrLowWngPortn_Type()
)
pmops2dAlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineRxPwrLowWngPortn.setStatus("current")
_Pmops2dAlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pmops2dAlmLineRxPwrHighWngPortn_Object = MibTableColumn
pmops2dAlmLineRxPwrHighWngPortn = _Pmops2dAlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 1, 48, 1, 5),
    _Pmops2dAlmLineRxPwrHighWngPortn_Type()
)
pmops2dAlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineRxPwrHighWngPortn.setStatus("current")
_Pmops2dAlmLineUrg_ObjectIdentity = ObjectIdentity
pmops2dAlmLineUrg = _Pmops2dAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2)
)
_Pmops2dAlmlineAlarmTable_Object = MibTable
pmops2dAlmlineAlarmTable = _Pmops2dAlmlineAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmops2dAlmlineAlarmTable.setStatus("current")
_Pmops2dAlmlineAlarmEntry_Object = MibTableRow
pmops2dAlmlineAlarmEntry = _Pmops2dAlmlineAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 32, 1)
)
pmops2dAlmlineAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dAlmlineAlarmIndex"),
)
if mibBuilder.loadTexts:
    pmops2dAlmlineAlarmEntry.setStatus("current")


class _Pmops2dAlmlineAlarmIndex_Type(Integer32):
    """Custom type pmops2dAlmlineAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dAlmlineAlarmIndex_Type.__name__ = "Integer32"
_Pmops2dAlmlineAlarmIndex_Object = MibTableColumn
pmops2dAlmlineAlarmIndex = _Pmops2dAlmlineAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 32, 1, 1),
    _Pmops2dAlmlineAlarmIndex_Type()
)
pmops2dAlmlineAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmlineAlarmIndex.setStatus("current")
_Pmops2dAlmLosRxPortn_Type = EkiOnOff
_Pmops2dAlmLosRxPortn_Object = MibTableColumn
pmops2dAlmLosRxPortn = _Pmops2dAlmLosRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 32, 1, 2),
    _Pmops2dAlmLosRxPortn_Type()
)
pmops2dAlmLosRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLosRxPortn.setStatus("current")
_Pmops2dAlmLosTxPortn_Type = EkiOnOff
_Pmops2dAlmLosTxPortn_Object = MibTableColumn
pmops2dAlmLosTxPortn = _Pmops2dAlmLosTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 32, 1, 4),
    _Pmops2dAlmLosTxPortn_Type()
)
pmops2dAlmLosTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLosTxPortn.setStatus("current")
_Pmops2dAlmSwitchPositionOnePortn_Type = EkiOnOff
_Pmops2dAlmSwitchPositionOnePortn_Object = MibTableColumn
pmops2dAlmSwitchPositionOnePortn = _Pmops2dAlmSwitchPositionOnePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 32, 1, 6),
    _Pmops2dAlmSwitchPositionOnePortn_Type()
)
pmops2dAlmSwitchPositionOnePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmSwitchPositionOnePortn.setStatus("current")
_Pmops2dAlmSwitchPositionTwoPortn_Type = EkiOnOff
_Pmops2dAlmSwitchPositionTwoPortn_Object = MibTableColumn
pmops2dAlmSwitchPositionTwoPortn = _Pmops2dAlmSwitchPositionTwoPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 32, 1, 7),
    _Pmops2dAlmSwitchPositionTwoPortn_Type()
)
pmops2dAlmSwitchPositionTwoPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmSwitchPositionTwoPortn.setStatus("current")
_Pmops2dAlmlineMeasAlaTable_Object = MibTable
pmops2dAlmlineMeasAlaTable = _Pmops2dAlmlineMeasAlaTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pmops2dAlmlineMeasAlaTable.setStatus("current")
_Pmops2dAlmlineMeasAlaEntry_Object = MibTableRow
pmops2dAlmlineMeasAlaEntry = _Pmops2dAlmlineMeasAlaEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 40, 1)
)
pmops2dAlmlineMeasAlaEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dAlmlineMeasAlaIndex"),
)
if mibBuilder.loadTexts:
    pmops2dAlmlineMeasAlaEntry.setStatus("current")


class _Pmops2dAlmlineMeasAlaIndex_Type(Integer32):
    """Custom type pmops2dAlmlineMeasAlaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dAlmlineMeasAlaIndex_Type.__name__ = "Integer32"
_Pmops2dAlmlineMeasAlaIndex_Object = MibTableColumn
pmops2dAlmlineMeasAlaIndex = _Pmops2dAlmlineMeasAlaIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 40, 1, 1),
    _Pmops2dAlmlineMeasAlaIndex_Type()
)
pmops2dAlmlineMeasAlaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmlineMeasAlaIndex.setStatus("current")
_Pmops2dAlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pmops2dAlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pmops2dAlmLineTxPwrLowAlaPortn = _Pmops2dAlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 40, 1, 2),
    _Pmops2dAlmLineTxPwrLowAlaPortn_Type()
)
pmops2dAlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineTxPwrLowAlaPortn.setStatus("current")
_Pmops2dAlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pmops2dAlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pmops2dAlmLineTxPwrHighAlaPortn = _Pmops2dAlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 40, 1, 3),
    _Pmops2dAlmLineTxPwrHighAlaPortn_Type()
)
pmops2dAlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineTxPwrHighAlaPortn.setStatus("current")
_Pmops2dAlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pmops2dAlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pmops2dAlmLineRxPwrLowAlaPortn = _Pmops2dAlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 40, 1, 4),
    _Pmops2dAlmLineRxPwrLowAlaPortn_Type()
)
pmops2dAlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineRxPwrLowAlaPortn.setStatus("current")
_Pmops2dAlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pmops2dAlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pmops2dAlmLineRxPwrHighAlaPortn = _Pmops2dAlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 2, 40, 1, 5),
    _Pmops2dAlmLineRxPwrHighAlaPortn_Type()
)
pmops2dAlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineRxPwrHighAlaPortn.setStatus("current")
_Pmops2dAlmLineCrit_ObjectIdentity = ObjectIdentity
pmops2dAlmLineCrit = _Pmops2dAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3)
)
_Pmops2dAlmsynthLineAlmTable_Object = MibTable
pmops2dAlmsynthLineAlmTable = _Pmops2dAlmsynthLineAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3, 16)
)
if mibBuilder.loadTexts:
    pmops2dAlmsynthLineAlmTable.setStatus("current")
_Pmops2dAlmsynthLineAlmEntry_Object = MibTableRow
pmops2dAlmsynthLineAlmEntry = _Pmops2dAlmsynthLineAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3, 16, 1)
)
pmops2dAlmsynthLineAlmEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dAlmsynthLineAlmIndex"),
)
if mibBuilder.loadTexts:
    pmops2dAlmsynthLineAlmEntry.setStatus("current")


class _Pmops2dAlmsynthLineAlmIndex_Type(Integer32):
    """Custom type pmops2dAlmsynthLineAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dAlmsynthLineAlmIndex_Type.__name__ = "Integer32"
_Pmops2dAlmsynthLineAlmIndex_Object = MibTableColumn
pmops2dAlmsynthLineAlmIndex = _Pmops2dAlmsynthLineAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3, 16, 1, 1),
    _Pmops2dAlmsynthLineAlmIndex_Type()
)
pmops2dAlmsynthLineAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmsynthLineAlmIndex.setStatus("current")
_Pmops2dAlmLineHwFailAccPortn_Type = EkiOnOff
_Pmops2dAlmLineHwFailAccPortn_Object = MibTableColumn
pmops2dAlmLineHwFailAccPortn = _Pmops2dAlmLineHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3, 16, 1, 5),
    _Pmops2dAlmLineHwFailAccPortn_Type()
)
pmops2dAlmLineHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineHwFailAccPortn.setStatus("current")
_Pmops2dAlmLineMeasWngPortn_Type = EkiOnOff
_Pmops2dAlmLineMeasWngPortn_Object = MibTableColumn
pmops2dAlmLineMeasWngPortn = _Pmops2dAlmLineMeasWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3, 16, 1, 10),
    _Pmops2dAlmLineMeasWngPortn_Type()
)
pmops2dAlmLineMeasWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineMeasWngPortn.setStatus("current")
_Pmops2dAlmLineMeasAlmPortn_Type = EkiOnOff
_Pmops2dAlmLineMeasAlmPortn_Object = MibTableColumn
pmops2dAlmLineMeasAlmPortn = _Pmops2dAlmLineMeasAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3, 16, 1, 11),
    _Pmops2dAlmLineMeasAlmPortn_Type()
)
pmops2dAlmLineMeasAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineMeasAlmPortn.setStatus("current")
_Pmops2dAlmLineFailAccPortn_Type = EkiOnOff
_Pmops2dAlmLineFailAccPortn_Object = MibTableColumn
pmops2dAlmLineFailAccPortn = _Pmops2dAlmLineFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 2, 3, 3, 16, 1, 13),
    _Pmops2dAlmLineFailAccPortn_Type()
)
pmops2dAlmLineFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dAlmLineFailAccPortn.setStatus("current")
_Pmops2dmeasures_ObjectIdentity = ObjectIdentity
pmops2dmeasures = _Pmops2dmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3)
)
_Pmops2dMesrOther_ObjectIdentity = ObjectIdentity
pmops2dMesrOther = _Pmops2dMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 1)
)
_Pmops2dMesrClient_ObjectIdentity = ObjectIdentity
pmops2dMesrClient = _Pmops2dMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 2)
)
_Pmops2dMesrLine_ObjectIdentity = ObjectIdentity
pmops2dMesrLine = _Pmops2dMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3)
)
_Pmops2dMesrtxPowerTable_Object = MibTable
pmops2dMesrtxPowerTable = _Pmops2dMesrtxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 16)
)
if mibBuilder.loadTexts:
    pmops2dMesrtxPowerTable.setStatus("current")
_Pmops2dMesrtxPowerEntry_Object = MibTableRow
pmops2dMesrtxPowerEntry = _Pmops2dMesrtxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 16, 1)
)
pmops2dMesrtxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dMesrtxPowerIndex"),
)
if mibBuilder.loadTexts:
    pmops2dMesrtxPowerEntry.setStatus("current")


class _Pmops2dMesrtxPowerIndex_Type(Integer32):
    """Custom type pmops2dMesrtxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dMesrtxPowerIndex_Type.__name__ = "Integer32"
_Pmops2dMesrtxPowerIndex_Object = MibTableColumn
pmops2dMesrtxPowerIndex = _Pmops2dMesrtxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 16, 1, 1),
    _Pmops2dMesrtxPowerIndex_Type()
)
pmops2dMesrtxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dMesrtxPowerIndex.setStatus("current")


class _Pmops2dMesrtxPowerPortn_Type(Integer32):
    """Custom type pmops2dMesrtxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmops2dMesrtxPowerPortn_Type.__name__ = "Integer32"
_Pmops2dMesrtxPowerPortn_Object = MibTableColumn
pmops2dMesrtxPowerPortn = _Pmops2dMesrtxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 16, 1, 2),
    _Pmops2dMesrtxPowerPortn_Type()
)
pmops2dMesrtxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dMesrtxPowerPortn.setStatus("current")
_Pmops2dMesrrxPowerTable_Object = MibTable
pmops2dMesrrxPowerTable = _Pmops2dMesrrxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pmops2dMesrrxPowerTable.setStatus("current")
_Pmops2dMesrrxPowerEntry_Object = MibTableRow
pmops2dMesrrxPowerEntry = _Pmops2dMesrrxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 24, 1)
)
pmops2dMesrrxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dMesrrxPowerIndex"),
)
if mibBuilder.loadTexts:
    pmops2dMesrrxPowerEntry.setStatus("current")


class _Pmops2dMesrrxPowerIndex_Type(Integer32):
    """Custom type pmops2dMesrrxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dMesrrxPowerIndex_Type.__name__ = "Integer32"
_Pmops2dMesrrxPowerIndex_Object = MibTableColumn
pmops2dMesrrxPowerIndex = _Pmops2dMesrrxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 24, 1, 1),
    _Pmops2dMesrrxPowerIndex_Type()
)
pmops2dMesrrxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dMesrrxPowerIndex.setStatus("current")


class _Pmops2dMesrrxPowerPortn_Type(Integer32):
    """Custom type pmops2dMesrrxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmops2dMesrrxPowerPortn_Type.__name__ = "Integer32"
_Pmops2dMesrrxPowerPortn_Object = MibTableColumn
pmops2dMesrrxPowerPortn = _Pmops2dMesrrxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 3, 3, 24, 1, 2),
    _Pmops2dMesrrxPowerPortn_Type()
)
pmops2dMesrrxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dMesrrxPowerPortn.setStatus("current")
_Pmops2dcontrolsWrite_ObjectIdentity = ObjectIdentity
pmops2dcontrolsWrite = _Pmops2dcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6)
)
_Pmops2dCtrlOther_ObjectIdentity = ObjectIdentity
pmops2dCtrlOther = _Pmops2dCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1)
)
_Pmops2dCtrlsynth0_ObjectIdentity = ObjectIdentity
pmops2dCtrlsynth0 = _Pmops2dCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 0)
)
_Pmops2dCtrlConfLoad_Type = EkiOnOff
_Pmops2dCtrlConfLoad_Object = MibScalar
pmops2dCtrlConfLoad = _Pmops2dCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 0, 1),
    _Pmops2dCtrlConfLoad_Type()
)
pmops2dCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlConfLoad.setStatus("current")
_Pmops2dCtrlConfFlash_Type = EkiOnOff
_Pmops2dCtrlConfFlash_Object = MibScalar
pmops2dCtrlConfFlash = _Pmops2dCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 0, 9),
    _Pmops2dCtrlConfFlash_Type()
)
pmops2dCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlConfFlash.setStatus("current")
_Pmops2dCtrlConfClear_Type = EkiOnOff
_Pmops2dCtrlConfClear_Object = MibScalar
pmops2dCtrlConfClear = _Pmops2dCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 0, 13),
    _Pmops2dCtrlConfClear_Type()
)
pmops2dCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlConfClear.setStatus("current")
_Pmops2dCtrlsynth4_ObjectIdentity = ObjectIdentity
pmops2dCtrlsynth4 = _Pmops2dCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 4)
)
_Pmops2dCtrlCorrelatOn_Type = EkiOnOff
_Pmops2dCtrlCorrelatOn_Object = MibScalar
pmops2dCtrlCorrelatOn = _Pmops2dCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 4, 1),
    _Pmops2dCtrlCorrelatOn_Type()
)
pmops2dCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlCorrelatOn.setStatus("current")
_Pmops2dCtrlCorrelatOff_Type = EkiOnOff
_Pmops2dCtrlCorrelatOff_Object = MibScalar
pmops2dCtrlCorrelatOff = _Pmops2dCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 4, 2),
    _Pmops2dCtrlCorrelatOff_Type()
)
pmops2dCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlCorrelatOff.setStatus("current")
_Pmops2dCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmops2dCtrlswMgnt = _Pmops2dCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 5)
)
_Pmops2dCtrlColdReset_Type = EkiOnOff
_Pmops2dCtrlColdReset_Object = MibScalar
pmops2dCtrlColdReset = _Pmops2dCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 5, 2),
    _Pmops2dCtrlColdReset_Type()
)
pmops2dCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlColdReset.setStatus("current")
_Pmops2dCtrlWarmReset_Type = EkiOnOff
_Pmops2dCtrlWarmReset_Object = MibScalar
pmops2dCtrlWarmReset = _Pmops2dCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 5, 3),
    _Pmops2dCtrlWarmReset_Type()
)
pmops2dCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlWarmReset.setStatus("current")
_Pmops2dCtrlledTest_ObjectIdentity = ObjectIdentity
pmops2dCtrlledTest = _Pmops2dCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 64)
)
_Pmops2dCtrlGreenLed_Type = EkiOnOff
_Pmops2dCtrlGreenLed_Object = MibScalar
pmops2dCtrlGreenLed = _Pmops2dCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 64, 1),
    _Pmops2dCtrlGreenLed_Type()
)
pmops2dCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlGreenLed.setStatus("current")
_Pmops2dCtrlRedLed_Type = EkiOnOff
_Pmops2dCtrlRedLed_Object = MibScalar
pmops2dCtrlRedLed = _Pmops2dCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 64, 2),
    _Pmops2dCtrlRedLed_Type()
)
pmops2dCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlRedLed.setStatus("current")
_Pmops2dCtrlLedOff_Type = EkiOnOff
_Pmops2dCtrlLedOff_Object = MibScalar
pmops2dCtrlLedOff = _Pmops2dCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 1, 64, 3),
    _Pmops2dCtrlLedOff_Type()
)
pmops2dCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCtrlLedOff.setStatus("current")
_Pmops2dCtrlClient_ObjectIdentity = ObjectIdentity
pmops2dCtrlClient = _Pmops2dCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 2)
)
_Pmops2dCtrlLine_ObjectIdentity = ObjectIdentity
pmops2dCtrlLine = _Pmops2dCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 6, 3)
)
_Pmops2dri_ObjectIdentity = ObjectIdentity
pmops2dri = _Pmops2dri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7)
)
_Pmops2driTable_ObjectIdentity = ObjectIdentity
pmops2driTable = _Pmops2driTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1)
)
_Pmops2dRinvSfpTable_Object = MibTable
pmops2dRinvSfpTable = _Pmops2dRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmops2dRinvSfpTable.setStatus("current")
_Pmops2dRinvSfpEntry_Object = MibTableRow
pmops2dRinvSfpEntry = _Pmops2dRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 1, 1)
)
pmops2dRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pmops2dRinvSfpEntry.setStatus("current")


class _Pmops2dRinvSfpIndex_Type(Integer32):
    """Custom type pmops2dRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmops2dRinvSfpIndex_Type.__name__ = "Integer32"
_Pmops2dRinvSfpIndex_Object = MibTableColumn
pmops2dRinvSfpIndex = _Pmops2dRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 1, 1, 1),
    _Pmops2dRinvSfpIndex_Type()
)
pmops2dRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dRinvSfpIndex.setStatus("current")
_Pmops2dRinvSfp_Type = DisplayString
_Pmops2dRinvSfp_Object = MibTableColumn
pmops2dRinvSfp = _Pmops2dRinvSfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 1, 1, 2),
    _Pmops2dRinvSfp_Type()
)
pmops2dRinvSfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dRinvSfp.setStatus("current")
_Pmops2dRinvLineTable_Object = MibTable
pmops2dRinvLineTable = _Pmops2dRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmops2dRinvLineTable.setStatus("current")
_Pmops2dRinvLineEntry_Object = MibTableRow
pmops2dRinvLineEntry = _Pmops2dRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 2, 1)
)
pmops2dRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmops2dRinvLineEntry.setStatus("current")


class _Pmops2dRinvLineIndex_Type(Integer32):
    """Custom type pmops2dRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmops2dRinvLineIndex_Type.__name__ = "Integer32"
_Pmops2dRinvLineIndex_Object = MibTableColumn
pmops2dRinvLineIndex = _Pmops2dRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 2, 1, 1),
    _Pmops2dRinvLineIndex_Type()
)
pmops2dRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dRinvLineIndex.setStatus("current")
_Pmops2dRinvLine_Type = DisplayString
_Pmops2dRinvLine_Object = MibTableColumn
pmops2dRinvLine = _Pmops2dRinvLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 1, 2, 1, 2),
    _Pmops2dRinvLine_Type()
)
pmops2dRinvLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dRinvLine.setStatus("current")
_Pmops2dRinvReloadInventory_Type = EkiOnOff
_Pmops2dRinvReloadInventory_Object = MibScalar
pmops2dRinvReloadInventory = _Pmops2dRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 2),
    _Pmops2dRinvReloadInventory_Type()
)
pmops2dRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dRinvReloadInventory.setStatus("current")
_Pmops2dRinvHwPlatform_Type = DisplayString
_Pmops2dRinvHwPlatform_Object = MibScalar
pmops2dRinvHwPlatform = _Pmops2dRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 3),
    _Pmops2dRinvHwPlatform_Type()
)
pmops2dRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dRinvHwPlatform.setStatus("current")
_Pmops2dRinvModulePlatform_Type = DisplayString
_Pmops2dRinvModulePlatform_Object = MibScalar
pmops2dRinvModulePlatform = _Pmops2dRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 4),
    _Pmops2dRinvModulePlatform_Type()
)
pmops2dRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dRinvModulePlatform.setStatus("current")
_Pmops2dRinvSwPlatform_Type = DisplayString
_Pmops2dRinvSwPlatform_Object = MibScalar
pmops2dRinvSwPlatform = _Pmops2dRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 7, 5),
    _Pmops2dRinvSwPlatform_Type()
)
pmops2dRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dRinvSwPlatform.setStatus("current")
_Pmops2dConfig_ObjectIdentity = ObjectIdentity
pmops2dConfig = _Pmops2dConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9)
)
_Pmops2dCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pmops2dCfgAccessCAisCsf = _Pmops2dCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 1)
)
_Pmops2dCfgClientcaiscsfTable_Object = MibTable
pmops2dCfgClientcaiscsfTable = _Pmops2dCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pmops2dCfgClientcaiscsfTable.setStatus("current")
_Pmops2dCfgClientcaiscsfEntry_Object = MibTableRow
pmops2dCfgClientcaiscsfEntry = _Pmops2dCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 1, 1, 1)
)
pmops2dCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pmops2dCfgClientcaiscsfEntry.setStatus("current")


class _Pmops2dCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pmops2dCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pmops2dCfgClientcaiscsfIndex_Object = MibTableColumn
pmops2dCfgClientcaiscsfIndex = _Pmops2dCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 1, 1, 1, 1),
    _Pmops2dCfgClientcaiscsfIndex_Type()
)
pmops2dCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dCfgClientcaiscsfIndex.setStatus("current")


class _Pmops2dCfgReservedPortn_Type(Unsigned32):
    """Custom type pmops2dCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmops2dCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pmops2dCfgReservedPortn_Object = MibTableColumn
pmops2dCfgReservedPortn = _Pmops2dCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 1, 1, 1, 3),
    _Pmops2dCfgReservedPortn_Type()
)
pmops2dCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCfgReservedPortn.setStatus("current")
_Pmops2dCfgStartUp_ObjectIdentity = ObjectIdentity
pmops2dCfgStartUp = _Pmops2dCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2)
)
_Pmops2dCfgClientStartupTable_Object = MibTable
pmops2dCfgClientStartupTable = _Pmops2dCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pmops2dCfgClientStartupTable.setStatus("current")
_Pmops2dCfgClientStartupEntry_Object = MibTableRow
pmops2dCfgClientStartupEntry = _Pmops2dCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 1, 1)
)
pmops2dCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmops2dCfgClientStartupEntry.setStatus("current")


class _Pmops2dCfgClientStartupIndex_Type(Integer32):
    """Custom type pmops2dCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pmops2dCfgClientStartupIndex_Object = MibTableColumn
pmops2dCfgClientStartupIndex = _Pmops2dCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 1, 1, 1),
    _Pmops2dCfgClientStartupIndex_Type()
)
pmops2dCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dCfgClientStartupIndex.setStatus("current")


class _Pmops2dCfgClientSwitchModePortn_Type(Unsigned32):
    """Custom type pmops2dCfgClientSwitchModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmops2dCfgClientSwitchModePortn_Type.__name__ = "Unsigned32"
_Pmops2dCfgClientSwitchModePortn_Object = MibTableColumn
pmops2dCfgClientSwitchModePortn = _Pmops2dCfgClientSwitchModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 1, 1, 3),
    _Pmops2dCfgClientSwitchModePortn_Type()
)
pmops2dCfgClientSwitchModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCfgClientSwitchModePortn.setStatus("current")
_Pmops2dCfgLineStartupThreshTable_Object = MibTable
pmops2dCfgLineStartupThreshTable = _Pmops2dCfgLineStartupThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pmops2dCfgLineStartupThreshTable.setStatus("current")
_Pmops2dCfgLineStartupThreshEntry_Object = MibTableRow
pmops2dCfgLineStartupThreshEntry = _Pmops2dCfgLineStartupThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 2, 1)
)
pmops2dCfgLineStartupThreshEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dCfgLineStartupThreshIndex"),
)
if mibBuilder.loadTexts:
    pmops2dCfgLineStartupThreshEntry.setStatus("current")


class _Pmops2dCfgLineStartupThreshIndex_Type(Integer32):
    """Custom type pmops2dCfgLineStartupThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dCfgLineStartupThreshIndex_Type.__name__ = "Integer32"
_Pmops2dCfgLineStartupThreshIndex_Object = MibTableColumn
pmops2dCfgLineStartupThreshIndex = _Pmops2dCfgLineStartupThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 2, 1, 1),
    _Pmops2dCfgLineStartupThreshIndex_Type()
)
pmops2dCfgLineStartupThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dCfgLineStartupThreshIndex.setStatus("current")


class _Pmops2dCfgLineRxPwrSettingPortn_Type(Unsigned32):
    """Custom type pmops2dCfgLineRxPwrSettingPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmops2dCfgLineRxPwrSettingPortn_Type.__name__ = "Unsigned32"
_Pmops2dCfgLineRxPwrSettingPortn_Object = MibTableColumn
pmops2dCfgLineRxPwrSettingPortn = _Pmops2dCfgLineRxPwrSettingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 2, 2, 1, 4),
    _Pmops2dCfgLineRxPwrSettingPortn_Type()
)
pmops2dCfgLineRxPwrSettingPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCfgLineRxPwrSettingPortn.setStatus("current")
_Pmops2dCfgOther_ObjectIdentity = ObjectIdentity
pmops2dCfgOther = _Pmops2dCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 3)
)
_Pmops2dtablemoduleOther_ObjectIdentity = ObjectIdentity
pmops2dtablemoduleOther = _Pmops2dtablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 3, 1)
)


class _Pmops2dCfgoutOfService_Type(Unsigned32):
    """Custom type pmops2dCfgoutOfService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmops2dCfgoutOfService_Type.__name__ = "Unsigned32"
_Pmops2dCfgoutOfService_Object = MibScalar
pmops2dCfgoutOfService = _Pmops2dCfgoutOfService_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 3, 1, 2),
    _Pmops2dCfgoutOfService_Type()
)
pmops2dCfgoutOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCfgoutOfService.setStatus("current")
_Pmops2dCfgLabels_ObjectIdentity = ObjectIdentity
pmops2dCfgLabels = _Pmops2dCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4)
)
_Pmops2dCfgLabelclientTable_Object = MibTable
pmops2dCfgLabelclientTable = _Pmops2dCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pmops2dCfgLabelclientTable.setStatus("current")
_Pmops2dCfgLabelclientEntry_Object = MibTableRow
pmops2dCfgLabelclientEntry = _Pmops2dCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 1, 1)
)
pmops2dCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmops2dCfgLabelclientEntry.setStatus("current")


class _Pmops2dCfgLabelclientIndex_Type(Integer32):
    """Custom type pmops2dCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmops2dCfgLabelclientIndex_Object = MibTableColumn
pmops2dCfgLabelclientIndex = _Pmops2dCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 1, 1, 1),
    _Pmops2dCfgLabelclientIndex_Type()
)
pmops2dCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dCfgLabelclientIndex.setStatus("current")


class _Pmops2dCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmops2dCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmops2dCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmops2dCfgLabelclientPortn_Object = MibTableColumn
pmops2dCfgLabelclientPortn = _Pmops2dCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 1, 1, 3),
    _Pmops2dCfgLabelclientPortn_Type()
)
pmops2dCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCfgLabelclientPortn.setStatus("current")
_Pmops2dCfgLabellineTable_Object = MibTable
pmops2dCfgLabellineTable = _Pmops2dCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pmops2dCfgLabellineTable.setStatus("current")
_Pmops2dCfgLabellineEntry_Object = MibTableRow
pmops2dCfgLabellineEntry = _Pmops2dCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 2, 1)
)
pmops2dCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmops2d-MIB", "pmops2dCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmops2dCfgLabellineEntry.setStatus("current")


class _Pmops2dCfgLabellineIndex_Type(Integer32):
    """Custom type pmops2dCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmops2dCfgLabellineIndex_Type.__name__ = "Integer32"
_Pmops2dCfgLabellineIndex_Object = MibTableColumn
pmops2dCfgLabellineIndex = _Pmops2dCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 2, 1, 1),
    _Pmops2dCfgLabellineIndex_Type()
)
pmops2dCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dCfgLabellineIndex.setStatus("current")


class _Pmops2dCfgLabellinePortn_Type(DisplayString):
    """Custom type pmops2dCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmops2dCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmops2dCfgLabellinePortn_Object = MibTableColumn
pmops2dCfgLabellinePortn = _Pmops2dCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 4, 2, 1, 3),
    _Pmops2dCfgLabellinePortn_Type()
)
pmops2dCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCfgLabellinePortn.setStatus("current")
_Pmops2dCfgWriteConfiguration_Type = EkiOnOff
_Pmops2dCfgWriteConfiguration_Object = MibScalar
pmops2dCfgWriteConfiguration = _Pmops2dCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 9, 257),
    _Pmops2dCfgWriteConfiguration_Type()
)
pmops2dCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmops2dCfgWriteConfiguration.setStatus("current")
_Pmops2dtraps_ObjectIdentity = ObjectIdentity
pmops2dtraps = _Pmops2dtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10)
)


class _Pmops2dtrapPortNumber_Type(Integer32):
    """Custom type pmops2dtrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmops2dtrapPortNumber_Type.__name__ = "Integer32"
_Pmops2dtrapPortNumber_Object = MibScalar
pmops2dtrapPortNumber = _Pmops2dtrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 2),
    _Pmops2dtrapPortNumber_Type()
)
pmops2dtrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dtrapPortNumber.setStatus("current")


class _Pmops2dtrapLineNumber_Type(Integer32):
    """Custom type pmops2dtrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmops2dtrapLineNumber_Type.__name__ = "Integer32"
_Pmops2dtrapLineNumber_Object = MibScalar
pmops2dtrapLineNumber = _Pmops2dtrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 3),
    _Pmops2dtrapLineNumber_Type()
)
pmops2dtrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dtrapLineNumber.setStatus("current")


class _Pmops2dtrapBoardNumber_Type(Integer32):
    """Custom type pmops2dtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmops2dtrapBoardNumber_Type.__name__ = "Integer32"
_Pmops2dtrapBoardNumber_Object = MibScalar
pmops2dtrapBoardNumber = _Pmops2dtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 4),
    _Pmops2dtrapBoardNumber_Type()
)
pmops2dtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmops2dtrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmops2dLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 30)
)
pmops2dLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineMeasWngPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapLineNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmops2dLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 31)
)
pmops2dLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineMeasWngPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapLineNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmops2dLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 32)
)
pmops2dLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineMeasAlmPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapLineNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmops2dLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 33)
)
pmops2dLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineMeasAlmPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapLineNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmops2dLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 34)
)
pmops2dLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineHwFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapLineNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dLineTrapCritGoesOn.setStatus(
        "current"
    )

pmops2dLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 35)
)
pmops2dLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dAlmLineHwFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapLineNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dLineTrapCritGoesOff.setStatus(
        "current"
    )

pmops2dClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 44)
)
pmops2dClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmClientFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dAlmClientHwFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapPortNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dClientTrapCritGoesOn.setStatus(
        "current"
    )

pmops2dClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 45)
)
pmops2dClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmClientFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dAlmClientHwFailAccPortn"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapPortNumber"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dClientTrapCritGoesOff.setStatus(
        "current"
    )

pmops2dPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 50)
)
pmops2dPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmDefFuseB"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dAlmDefFuseA"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmops2dPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 71, 10, 51)
)
pmops2dPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops2d-MIB", "pmops2dAlmDefFuseB"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dAlmDefFuseA"),
        ("EKINOPS-Pmops2d-MIB", "pmops2dtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmops2dPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmops2d-MIB",
    **{"Pmops2dSwitchMode": Pmops2dSwitchMode,
       "modulePmops2d": modulePmops2d,
       "pmops2dalarms": pmops2dalarms,
       "pmops2dAlmOther": pmops2dAlmOther,
       "pmops2dAlmOtherNurg": pmops2dAlmOtherNurg,
       "pmops2dAlmswitchOutOfService": pmops2dAlmswitchOutOfService,
       "pmops2dAlmOpsaOutofservice": pmops2dAlmOpsaOutofservice,
       "pmops2dAlmOpsbOutofservice": pmops2dAlmOpsbOutofservice,
       "pmops2dAlmOtherUrg": pmops2dAlmOtherUrg,
       "pmops2dAlmOtherCrit": pmops2dAlmOtherCrit,
       "pmops2dAlmsynthAlm0": pmops2dAlmsynthAlm0,
       "pmops2dAlmModuleGlobFailure": pmops2dAlmModuleGlobFailure,
       "pmops2dAlmDefFuseA": pmops2dAlmDefFuseA,
       "pmops2dAlmDefFuseB": pmops2dAlmDefFuseB,
       "pmops2dAlmClient": pmops2dAlmClient,
       "pmops2dAlmClientNurg": pmops2dAlmClientNurg,
       "pmops2dAlmClientUrg": pmops2dAlmClientUrg,
       "pmops2dAlmclientComAlarmTable": pmops2dAlmclientComAlarmTable,
       "pmops2dAlmclientComAlarmEntry": pmops2dAlmclientComAlarmEntry,
       "pmops2dAlmclientComAlarmIndex": pmops2dAlmclientComAlarmIndex,
       "pmops2dAlmClientComSwitchFailPortn": pmops2dAlmClientComSwitchFailPortn,
       "pmops2dAlmClientCrit": pmops2dAlmClientCrit,
       "pmops2dAlmsynthClientAlmTable": pmops2dAlmsynthClientAlmTable,
       "pmops2dAlmsynthClientAlmEntry": pmops2dAlmsynthClientAlmEntry,
       "pmops2dAlmsynthClientAlmIndex": pmops2dAlmsynthClientAlmIndex,
       "pmops2dAlmClientHwFailAccPortn": pmops2dAlmClientHwFailAccPortn,
       "pmops2dAlmClientFailAccPortn": pmops2dAlmClientFailAccPortn,
       "pmops2dAlmLine": pmops2dAlmLine,
       "pmops2dAlmLineNurg": pmops2dAlmLineNurg,
       "pmops2dAlmlineMeasWngTable": pmops2dAlmlineMeasWngTable,
       "pmops2dAlmlineMeasWngEntry": pmops2dAlmlineMeasWngEntry,
       "pmops2dAlmlineMeasWngIndex": pmops2dAlmlineMeasWngIndex,
       "pmops2dAlmLineTxPwrLowWngPortn": pmops2dAlmLineTxPwrLowWngPortn,
       "pmops2dAlmLineTxPwrHighWngPortn": pmops2dAlmLineTxPwrHighWngPortn,
       "pmops2dAlmLineRxPwrLowWngPortn": pmops2dAlmLineRxPwrLowWngPortn,
       "pmops2dAlmLineRxPwrHighWngPortn": pmops2dAlmLineRxPwrHighWngPortn,
       "pmops2dAlmLineUrg": pmops2dAlmLineUrg,
       "pmops2dAlmlineAlarmTable": pmops2dAlmlineAlarmTable,
       "pmops2dAlmlineAlarmEntry": pmops2dAlmlineAlarmEntry,
       "pmops2dAlmlineAlarmIndex": pmops2dAlmlineAlarmIndex,
       "pmops2dAlmLosRxPortn": pmops2dAlmLosRxPortn,
       "pmops2dAlmLosTxPortn": pmops2dAlmLosTxPortn,
       "pmops2dAlmSwitchPositionOnePortn": pmops2dAlmSwitchPositionOnePortn,
       "pmops2dAlmSwitchPositionTwoPortn": pmops2dAlmSwitchPositionTwoPortn,
       "pmops2dAlmlineMeasAlaTable": pmops2dAlmlineMeasAlaTable,
       "pmops2dAlmlineMeasAlaEntry": pmops2dAlmlineMeasAlaEntry,
       "pmops2dAlmlineMeasAlaIndex": pmops2dAlmlineMeasAlaIndex,
       "pmops2dAlmLineTxPwrLowAlaPortn": pmops2dAlmLineTxPwrLowAlaPortn,
       "pmops2dAlmLineTxPwrHighAlaPortn": pmops2dAlmLineTxPwrHighAlaPortn,
       "pmops2dAlmLineRxPwrLowAlaPortn": pmops2dAlmLineRxPwrLowAlaPortn,
       "pmops2dAlmLineRxPwrHighAlaPortn": pmops2dAlmLineRxPwrHighAlaPortn,
       "pmops2dAlmLineCrit": pmops2dAlmLineCrit,
       "pmops2dAlmsynthLineAlmTable": pmops2dAlmsynthLineAlmTable,
       "pmops2dAlmsynthLineAlmEntry": pmops2dAlmsynthLineAlmEntry,
       "pmops2dAlmsynthLineAlmIndex": pmops2dAlmsynthLineAlmIndex,
       "pmops2dAlmLineHwFailAccPortn": pmops2dAlmLineHwFailAccPortn,
       "pmops2dAlmLineMeasWngPortn": pmops2dAlmLineMeasWngPortn,
       "pmops2dAlmLineMeasAlmPortn": pmops2dAlmLineMeasAlmPortn,
       "pmops2dAlmLineFailAccPortn": pmops2dAlmLineFailAccPortn,
       "pmops2dmeasures": pmops2dmeasures,
       "pmops2dMesrOther": pmops2dMesrOther,
       "pmops2dMesrClient": pmops2dMesrClient,
       "pmops2dMesrLine": pmops2dMesrLine,
       "pmops2dMesrtxPowerTable": pmops2dMesrtxPowerTable,
       "pmops2dMesrtxPowerEntry": pmops2dMesrtxPowerEntry,
       "pmops2dMesrtxPowerIndex": pmops2dMesrtxPowerIndex,
       "pmops2dMesrtxPowerPortn": pmops2dMesrtxPowerPortn,
       "pmops2dMesrrxPowerTable": pmops2dMesrrxPowerTable,
       "pmops2dMesrrxPowerEntry": pmops2dMesrrxPowerEntry,
       "pmops2dMesrrxPowerIndex": pmops2dMesrrxPowerIndex,
       "pmops2dMesrrxPowerPortn": pmops2dMesrrxPowerPortn,
       "pmops2dcontrolsWrite": pmops2dcontrolsWrite,
       "pmops2dCtrlOther": pmops2dCtrlOther,
       "pmops2dCtrlsynth0": pmops2dCtrlsynth0,
       "pmops2dCtrlConfLoad": pmops2dCtrlConfLoad,
       "pmops2dCtrlConfFlash": pmops2dCtrlConfFlash,
       "pmops2dCtrlConfClear": pmops2dCtrlConfClear,
       "pmops2dCtrlsynth4": pmops2dCtrlsynth4,
       "pmops2dCtrlCorrelatOn": pmops2dCtrlCorrelatOn,
       "pmops2dCtrlCorrelatOff": pmops2dCtrlCorrelatOff,
       "pmops2dCtrlswMgnt": pmops2dCtrlswMgnt,
       "pmops2dCtrlColdReset": pmops2dCtrlColdReset,
       "pmops2dCtrlWarmReset": pmops2dCtrlWarmReset,
       "pmops2dCtrlledTest": pmops2dCtrlledTest,
       "pmops2dCtrlGreenLed": pmops2dCtrlGreenLed,
       "pmops2dCtrlRedLed": pmops2dCtrlRedLed,
       "pmops2dCtrlLedOff": pmops2dCtrlLedOff,
       "pmops2dCtrlClient": pmops2dCtrlClient,
       "pmops2dCtrlLine": pmops2dCtrlLine,
       "pmops2dri": pmops2dri,
       "pmops2driTable": pmops2driTable,
       "pmops2dRinvSfpTable": pmops2dRinvSfpTable,
       "pmops2dRinvSfpEntry": pmops2dRinvSfpEntry,
       "pmops2dRinvSfpIndex": pmops2dRinvSfpIndex,
       "pmops2dRinvSfp": pmops2dRinvSfp,
       "pmops2dRinvLineTable": pmops2dRinvLineTable,
       "pmops2dRinvLineEntry": pmops2dRinvLineEntry,
       "pmops2dRinvLineIndex": pmops2dRinvLineIndex,
       "pmops2dRinvLine": pmops2dRinvLine,
       "pmops2dRinvReloadInventory": pmops2dRinvReloadInventory,
       "pmops2dRinvHwPlatform": pmops2dRinvHwPlatform,
       "pmops2dRinvModulePlatform": pmops2dRinvModulePlatform,
       "pmops2dRinvSwPlatform": pmops2dRinvSwPlatform,
       "pmops2dConfig": pmops2dConfig,
       "pmops2dCfgAccessCAisCsf": pmops2dCfgAccessCAisCsf,
       "pmops2dCfgClientcaiscsfTable": pmops2dCfgClientcaiscsfTable,
       "pmops2dCfgClientcaiscsfEntry": pmops2dCfgClientcaiscsfEntry,
       "pmops2dCfgClientcaiscsfIndex": pmops2dCfgClientcaiscsfIndex,
       "pmops2dCfgReservedPortn": pmops2dCfgReservedPortn,
       "pmops2dCfgStartUp": pmops2dCfgStartUp,
       "pmops2dCfgClientStartupTable": pmops2dCfgClientStartupTable,
       "pmops2dCfgClientStartupEntry": pmops2dCfgClientStartupEntry,
       "pmops2dCfgClientStartupIndex": pmops2dCfgClientStartupIndex,
       "pmops2dCfgClientSwitchModePortn": pmops2dCfgClientSwitchModePortn,
       "pmops2dCfgLineStartupThreshTable": pmops2dCfgLineStartupThreshTable,
       "pmops2dCfgLineStartupThreshEntry": pmops2dCfgLineStartupThreshEntry,
       "pmops2dCfgLineStartupThreshIndex": pmops2dCfgLineStartupThreshIndex,
       "pmops2dCfgLineRxPwrSettingPortn": pmops2dCfgLineRxPwrSettingPortn,
       "pmops2dCfgOther": pmops2dCfgOther,
       "pmops2dtablemoduleOther": pmops2dtablemoduleOther,
       "pmops2dCfgoutOfService": pmops2dCfgoutOfService,
       "pmops2dCfgLabels": pmops2dCfgLabels,
       "pmops2dCfgLabelclientTable": pmops2dCfgLabelclientTable,
       "pmops2dCfgLabelclientEntry": pmops2dCfgLabelclientEntry,
       "pmops2dCfgLabelclientIndex": pmops2dCfgLabelclientIndex,
       "pmops2dCfgLabelclientPortn": pmops2dCfgLabelclientPortn,
       "pmops2dCfgLabellineTable": pmops2dCfgLabellineTable,
       "pmops2dCfgLabellineEntry": pmops2dCfgLabellineEntry,
       "pmops2dCfgLabellineIndex": pmops2dCfgLabellineIndex,
       "pmops2dCfgLabellinePortn": pmops2dCfgLabellinePortn,
       "pmops2dCfgWriteConfiguration": pmops2dCfgWriteConfiguration,
       "pmops2dtraps": pmops2dtraps,
       "pmops2dtrapPortNumber": pmops2dtrapPortNumber,
       "pmops2dtrapLineNumber": pmops2dtrapLineNumber,
       "pmops2dtrapBoardNumber": pmops2dtrapBoardNumber,
       "pmops2dLineTrapNotUrgentGoesOn": pmops2dLineTrapNotUrgentGoesOn,
       "pmops2dLineTrapNotUrgentGoesOff": pmops2dLineTrapNotUrgentGoesOff,
       "pmops2dLineTrapUrgentGoesOn": pmops2dLineTrapUrgentGoesOn,
       "pmops2dLineTrapUrgentGoesOff": pmops2dLineTrapUrgentGoesOff,
       "pmops2dLineTrapCritGoesOn": pmops2dLineTrapCritGoesOn,
       "pmops2dLineTrapCritGoesOff": pmops2dLineTrapCritGoesOff,
       "pmops2dClientTrapCritGoesOn": pmops2dClientTrapCritGoesOn,
       "pmops2dClientTrapCritGoesOff": pmops2dClientTrapCritGoesOff,
       "pmops2dPowerTrapUrgentGoesOn": pmops2dPowerTrapUrgentGoesOn,
       "pmops2dPowerTrapUrgentGoesOff": pmops2dPowerTrapUrgentGoesOff}
)
