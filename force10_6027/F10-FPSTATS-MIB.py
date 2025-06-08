# SNMP MIB module (F10-FPSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/F10-FPSTATS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:14 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

f10FpStatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16)
)
if mibBuilder.loadTexts:
    f10FpStatsMib.setRevisions(
        ("2013-02-20 12:00",
         "2011-03-22 12:48")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ComType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F10FpStatsObject_ObjectIdentity = ObjectIdentity
f10FpStatsObject = _F10FpStatsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1)
)
_FpStatsObjects_ObjectIdentity = ObjectIdentity
fpStatsObjects = _FpStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1)
)
_FpCpuDataPlaneTable_Object = MibTable
fpCpuDataPlaneTable = _FpCpuDataPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fpCpuDataPlaneTable.setStatus("current")
_FpCpuDataPlaneStatsEntry_Object = MibTableRow
fpCpuDataPlaneStatsEntry = _FpCpuDataPlaneStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1)
)
fpCpuDataPlaneStatsEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
)
if mibBuilder.loadTexts:
    fpCpuDataPlaneStatsEntry.setStatus("current")


class _FpStackUnitIndex_Type(Integer32):
    """Custom type fpStackUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FpStackUnitIndex_Type.__name__ = "Integer32"
_FpStackUnitIndex_Object = MibTableColumn
fpStackUnitIndex = _FpStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 1),
    _FpStackUnitIndex_Type()
)
fpStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpStackUnitIndex.setStatus("current")
_FpRxHandle_Type = Integer32
_FpRxHandle_Object = MibTableColumn
fpRxHandle = _FpRxHandle_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 2),
    _FpRxHandle_Type()
)
fpRxHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxHandle.setStatus("current")
_FpNoMhdr_Type = Integer32
_FpNoMhdr_Object = MibTableColumn
fpNoMhdr = _FpNoMhdr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 3),
    _FpNoMhdr_Type()
)
fpNoMhdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpNoMhdr.setStatus("current")
_FpNoMBuf_Type = Integer32
_FpNoMBuf_Object = MibTableColumn
fpNoMBuf = _FpNoMBuf_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 4),
    _FpNoMBuf_Type()
)
fpNoMBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpNoMBuf.setStatus("current")
_FpNoClus_Type = Integer32
_FpNoClus_Object = MibTableColumn
fpNoClus = _FpNoClus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 5),
    _FpNoClus_Type()
)
fpNoClus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpNoClus.setStatus("current")
_FpRecvd_Type = Integer32
_FpRecvd_Object = MibTableColumn
fpRecvd = _FpRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 6),
    _FpRecvd_Type()
)
fpRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRecvd.setStatus("current")
_FpDropped_Type = Integer32
_FpDropped_Object = MibTableColumn
fpDropped = _FpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 7),
    _FpDropped_Type()
)
fpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDropped.setStatus("current")
_FpRecvToNet_Type = Integer32
_FpRecvToNet_Object = MibTableColumn
fpRecvToNet = _FpRecvToNet_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 8),
    _FpRecvToNet_Type()
)
fpRecvToNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRecvToNet.setStatus("current")
_FpRxError_Type = Integer32
_FpRxError_Object = MibTableColumn
fpRxError = _FpRxError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 9),
    _FpRxError_Type()
)
fpRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxError.setStatus("current")
_FpRxDatapathError_Type = Integer32
_FpRxDatapathError_Object = MibTableColumn
fpRxDatapathError = _FpRxDatapathError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 10),
    _FpRxDatapathError_Type()
)
fpRxDatapathError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxDatapathError.setStatus("current")
_FpRxPktCOS0_Type = Integer32
_FpRxPktCOS0_Object = MibTableColumn
fpRxPktCOS0 = _FpRxPktCOS0_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 11),
    _FpRxPktCOS0_Type()
)
fpRxPktCOS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS0.setStatus("deprecated")
_FpRxPktCOS1_Type = Integer32
_FpRxPktCOS1_Object = MibTableColumn
fpRxPktCOS1 = _FpRxPktCOS1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 12),
    _FpRxPktCOS1_Type()
)
fpRxPktCOS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS1.setStatus("deprecated")
_FpRxPktCOS2_Type = Integer32
_FpRxPktCOS2_Object = MibTableColumn
fpRxPktCOS2 = _FpRxPktCOS2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 13),
    _FpRxPktCOS2_Type()
)
fpRxPktCOS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS2.setStatus("deprecated")
_FpRxPktCOS3_Type = Integer32
_FpRxPktCOS3_Object = MibTableColumn
fpRxPktCOS3 = _FpRxPktCOS3_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 14),
    _FpRxPktCOS3_Type()
)
fpRxPktCOS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS3.setStatus("deprecated")
_FpRxPktCOS4_Type = Integer32
_FpRxPktCOS4_Object = MibTableColumn
fpRxPktCOS4 = _FpRxPktCOS4_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 15),
    _FpRxPktCOS4_Type()
)
fpRxPktCOS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS4.setStatus("deprecated")
_FpRxPktCOS5_Type = Integer32
_FpRxPktCOS5_Object = MibTableColumn
fpRxPktCOS5 = _FpRxPktCOS5_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 16),
    _FpRxPktCOS5_Type()
)
fpRxPktCOS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS5.setStatus("deprecated")
_FpRxPktCOS6_Type = Integer32
_FpRxPktCOS6_Object = MibTableColumn
fpRxPktCOS6 = _FpRxPktCOS6_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 17),
    _FpRxPktCOS6_Type()
)
fpRxPktCOS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS6.setStatus("deprecated")
_FpRxPktCOS7_Type = Integer32
_FpRxPktCOS7_Object = MibTableColumn
fpRxPktCOS7 = _FpRxPktCOS7_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 18),
    _FpRxPktCOS7_Type()
)
fpRxPktCOS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS7.setStatus("deprecated")
_FpRxPktUnit0_Type = Integer32
_FpRxPktUnit0_Object = MibTableColumn
fpRxPktUnit0 = _FpRxPktUnit0_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 19),
    _FpRxPktUnit0_Type()
)
fpRxPktUnit0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktUnit0.setStatus("current")
_FpRxPktUnit1_Type = Integer32
_FpRxPktUnit1_Object = MibTableColumn
fpRxPktUnit1 = _FpRxPktUnit1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 20),
    _FpRxPktUnit1_Type()
)
fpRxPktUnit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktUnit1.setStatus("current")
_FpRxPktUnit2_Type = Integer32
_FpRxPktUnit2_Object = MibTableColumn
fpRxPktUnit2 = _FpRxPktUnit2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 21),
    _FpRxPktUnit2_Type()
)
fpRxPktUnit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktUnit2.setStatus("current")
_FpRxPktUnit3_Type = Integer32
_FpRxPktUnit3_Object = MibTableColumn
fpRxPktUnit3 = _FpRxPktUnit3_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 22),
    _FpRxPktUnit3_Type()
)
fpRxPktUnit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktUnit3.setStatus("current")
_FpTransmitted_Type = Integer32
_FpTransmitted_Object = MibTableColumn
fpTransmitted = _FpTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 23),
    _FpTransmitted_Type()
)
fpTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTransmitted.setStatus("current")
_FpTxRequested_Type = Integer32
_FpTxRequested_Object = MibTableColumn
fpTxRequested = _FpTxRequested_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 24),
    _FpTxRequested_Type()
)
fpTxRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxRequested.setStatus("current")
_FpNoTxDesc_Type = Integer32
_FpNoTxDesc_Object = MibTableColumn
fpNoTxDesc = _FpNoTxDesc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 25),
    _FpNoTxDesc_Type()
)
fpNoTxDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpNoTxDesc.setStatus("current")
_FpTxError_Type = Integer32
_FpTxError_Object = MibTableColumn
fpTxError = _FpTxError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 26),
    _FpTxError_Type()
)
fpTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxError.setStatus("current")
_FpTxReqTooLarge_Type = Integer32
_FpTxReqTooLarge_Object = MibTableColumn
fpTxReqTooLarge = _FpTxReqTooLarge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 27),
    _FpTxReqTooLarge_Type()
)
fpTxReqTooLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxReqTooLarge.setStatus("current")
_FpTxInternalError_Type = Integer32
_FpTxInternalError_Object = MibTableColumn
fpTxInternalError = _FpTxInternalError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 28),
    _FpTxInternalError_Type()
)
fpTxInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxInternalError.setStatus("current")
_FpTxDatapathErr_Type = Integer32
_FpTxDatapathErr_Object = MibTableColumn
fpTxDatapathErr = _FpTxDatapathErr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 29),
    _FpTxDatapathErr_Type()
)
fpTxDatapathErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxDatapathErr.setStatus("current")
_FpTxPktCOS0_Type = Integer32
_FpTxPktCOS0_Object = MibTableColumn
fpTxPktCOS0 = _FpTxPktCOS0_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 30),
    _FpTxPktCOS0_Type()
)
fpTxPktCOS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS0.setStatus("deprecated")
_FpTxPktCOS1_Type = Integer32
_FpTxPktCOS1_Object = MibTableColumn
fpTxPktCOS1 = _FpTxPktCOS1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 31),
    _FpTxPktCOS1_Type()
)
fpTxPktCOS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS1.setStatus("deprecated")
_FpTxPktCOS2_Type = Integer32
_FpTxPktCOS2_Object = MibTableColumn
fpTxPktCOS2 = _FpTxPktCOS2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 32),
    _FpTxPktCOS2_Type()
)
fpTxPktCOS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS2.setStatus("deprecated")
_FpTxPktCOS3_Type = Integer32
_FpTxPktCOS3_Object = MibTableColumn
fpTxPktCOS3 = _FpTxPktCOS3_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 33),
    _FpTxPktCOS3_Type()
)
fpTxPktCOS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS3.setStatus("deprecated")
_FpTxPktCOS4_Type = Integer32
_FpTxPktCOS4_Object = MibTableColumn
fpTxPktCOS4 = _FpTxPktCOS4_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 34),
    _FpTxPktCOS4_Type()
)
fpTxPktCOS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS4.setStatus("deprecated")
_FpTxPktCOS5_Type = Integer32
_FpTxPktCOS5_Object = MibTableColumn
fpTxPktCOS5 = _FpTxPktCOS5_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 35),
    _FpTxPktCOS5_Type()
)
fpTxPktCOS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS5.setStatus("deprecated")
_FpTxPktCOS6_Type = Integer32
_FpTxPktCOS6_Object = MibTableColumn
fpTxPktCOS6 = _FpTxPktCOS6_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 36),
    _FpTxPktCOS6_Type()
)
fpTxPktCOS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS6.setStatus("deprecated")
_FpTxPktCOS7_Type = Integer32
_FpTxPktCOS7_Object = MibTableColumn
fpTxPktCOS7 = _FpTxPktCOS7_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 37),
    _FpTxPktCOS7_Type()
)
fpTxPktCOS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS7.setStatus("deprecated")
_FpTxPktUnit0_Type = Integer32
_FpTxPktUnit0_Object = MibTableColumn
fpTxPktUnit0 = _FpTxPktUnit0_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 38),
    _FpTxPktUnit0_Type()
)
fpTxPktUnit0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktUnit0.setStatus("current")
_FpTxPktUnit1_Type = Integer32
_FpTxPktUnit1_Object = MibTableColumn
fpTxPktUnit1 = _FpTxPktUnit1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 39),
    _FpTxPktUnit1_Type()
)
fpTxPktUnit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktUnit1.setStatus("current")
_FpTxPktUnit2_Type = Integer32
_FpTxPktUnit2_Object = MibTableColumn
fpTxPktUnit2 = _FpTxPktUnit2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 40),
    _FpTxPktUnit2_Type()
)
fpTxPktUnit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktUnit2.setStatus("current")
_FpTxPktUnit3_Type = Integer32
_FpTxPktUnit3_Object = MibTableColumn
fpTxPktUnit3 = _FpTxPktUnit3_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 1, 1, 41),
    _FpTxPktUnit3_Type()
)
fpTxPktUnit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktUnit3.setStatus("current")
_FpCpuPartyBusTable_Object = MibTable
fpCpuPartyBusTable = _FpCpuPartyBusTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fpCpuPartyBusTable.setStatus("current")
_FpCpuPartyBusStatsEntry_Object = MibTableRow
fpCpuPartyBusStatsEntry = _FpCpuPartyBusStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1)
)
fpCpuPartyBusStatsEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
)
if mibBuilder.loadTexts:
    fpCpuPartyBusStatsEntry.setStatus("current")
_FpPartyBusInputPackets_Type = Counter32
_FpPartyBusInputPackets_Object = MibTableColumn
fpPartyBusInputPackets = _FpPartyBusInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1, 1),
    _FpPartyBusInputPackets_Type()
)
fpPartyBusInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPartyBusInputPackets.setStatus("current")
_FpPartyBusInputBytes_Type = Counter32
_FpPartyBusInputBytes_Object = MibTableColumn
fpPartyBusInputBytes = _FpPartyBusInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1, 2),
    _FpPartyBusInputBytes_Type()
)
fpPartyBusInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPartyBusInputBytes.setStatus("current")
_FpPartyBusInputDropped_Type = Counter32
_FpPartyBusInputDropped_Object = MibTableColumn
fpPartyBusInputDropped = _FpPartyBusInputDropped_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1, 3),
    _FpPartyBusInputDropped_Type()
)
fpPartyBusInputDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPartyBusInputDropped.setStatus("current")
_FpPartyBusInputError_Type = Counter32
_FpPartyBusInputError_Object = MibTableColumn
fpPartyBusInputError = _FpPartyBusInputError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1, 4),
    _FpPartyBusInputError_Type()
)
fpPartyBusInputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPartyBusInputError.setStatus("current")
_FpPartyBusOutputPackets_Type = Counter32
_FpPartyBusOutputPackets_Object = MibTableColumn
fpPartyBusOutputPackets = _FpPartyBusOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1, 5),
    _FpPartyBusOutputPackets_Type()
)
fpPartyBusOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPartyBusOutputPackets.setStatus("current")
_FpPartyBusOutputBytes_Type = Counter32
_FpPartyBusOutputBytes_Object = MibTableColumn
fpPartyBusOutputBytes = _FpPartyBusOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1, 6),
    _FpPartyBusOutputBytes_Type()
)
fpPartyBusOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPartyBusOutputBytes.setStatus("current")
_FpPartyBusOutputError_Type = Counter32
_FpPartyBusOutputError_Object = MibTableColumn
fpPartyBusOutputError = _FpPartyBusOutputError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 2, 1, 7),
    _FpPartyBusOutputError_Type()
)
fpPartyBusOutputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPartyBusOutputError.setStatus("current")
_FpDropsTable_Object = MibTable
fpDropsTable = _FpDropsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fpDropsTable.setStatus("current")
_FpDropsEntry_Object = MibTableRow
fpDropsEntry = _FpDropsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1)
)
fpDropsEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
)
if mibBuilder.loadTexts:
    fpDropsEntry.setStatus("current")


class _FpStackPortIndex_Type(Integer32):
    """Custom type fpStackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_FpStackPortIndex_Type.__name__ = "Integer32"
_FpStackPortIndex_Object = MibTableColumn
fpStackPortIndex = _FpStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 1),
    _FpStackPortIndex_Type()
)
fpStackPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpStackPortIndex.setStatus("current")
_FpIngressDrops_Type = Counter64
_FpIngressDrops_Object = MibTableColumn
fpIngressDrops = _FpIngressDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 2),
    _FpIngressDrops_Type()
)
fpIngressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngressDrops.setStatus("current")
_FpIngIBPCBPFullDrops_Type = Counter64
_FpIngIBPCBPFullDrops_Object = MibTableColumn
fpIngIBPCBPFullDrops = _FpIngIBPCBPFullDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 3),
    _FpIngIBPCBPFullDrops_Type()
)
fpIngIBPCBPFullDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngIBPCBPFullDrops.setStatus("current")
_FpIngPortSTPnotFwdDrops_Type = Counter64
_FpIngPortSTPnotFwdDrops_Object = MibTableColumn
fpIngPortSTPnotFwdDrops = _FpIngPortSTPnotFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 4),
    _FpIngPortSTPnotFwdDrops_Type()
)
fpIngPortSTPnotFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngPortSTPnotFwdDrops.setStatus("current")
_FpIngIPv4L3Discards_Type = Counter64
_FpIngIPv4L3Discards_Object = MibTableColumn
fpIngIPv4L3Discards = _FpIngIPv4L3Discards_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 5),
    _FpIngIPv4L3Discards_Type()
)
fpIngIPv4L3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngIPv4L3Discards.setStatus("current")
_FpIngPolicyDiscards_Type = Counter64
_FpIngPolicyDiscards_Object = MibTableColumn
fpIngPolicyDiscards = _FpIngPolicyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 6),
    _FpIngPolicyDiscards_Type()
)
fpIngPolicyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngPolicyDiscards.setStatus("current")
_FpIngPacketsDroppedByFP_Type = Counter64
_FpIngPacketsDroppedByFP_Object = MibTableColumn
fpIngPacketsDroppedByFP = _FpIngPacketsDroppedByFP_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 7),
    _FpIngPacketsDroppedByFP_Type()
)
fpIngPacketsDroppedByFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngPacketsDroppedByFP.setStatus("current")
_FpIngL2L3Drops_Type = Counter64
_FpIngL2L3Drops_Object = MibTableColumn
fpIngL2L3Drops = _FpIngL2L3Drops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 8),
    _FpIngL2L3Drops_Type()
)
fpIngL2L3Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngL2L3Drops.setStatus("current")
_FpIngPortBitMapZeroDrops_Type = Counter64
_FpIngPortBitMapZeroDrops_Object = MibTableColumn
fpIngPortBitMapZeroDrops = _FpIngPortBitMapZeroDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 9),
    _FpIngPortBitMapZeroDrops_Type()
)
fpIngPortBitMapZeroDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngPortBitMapZeroDrops.setStatus("current")
_FpIngRxVLANDrops_Type = Counter64
_FpIngRxVLANDrops_Object = MibTableColumn
fpIngRxVLANDrops = _FpIngRxVLANDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 10),
    _FpIngRxVLANDrops_Type()
)
fpIngRxVLANDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngRxVLANDrops.setStatus("current")
_FpIngressFCSDrops_Type = Counter64
_FpIngressFCSDrops_Object = MibTableColumn
fpIngressFCSDrops = _FpIngressFCSDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 11),
    _FpIngressFCSDrops_Type()
)
fpIngressFCSDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngressFCSDrops.setStatus("current")
_FpIngressMTUExceeds_Type = Counter64
_FpIngressMTUExceeds_Object = MibTableColumn
fpIngressMTUExceeds = _FpIngressMTUExceeds_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 12),
    _FpIngressMTUExceeds_Type()
)
fpIngressMTUExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngressMTUExceeds.setStatus("current")
_FpMMUHOLDrops_Type = Counter64
_FpMMUHOLDrops_Object = MibTableColumn
fpMMUHOLDrops = _FpMMUHOLDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 13),
    _FpMMUHOLDrops_Type()
)
fpMMUHOLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpMMUHOLDrops.setStatus("current")
_FpMMUTxPurgeCellErr_Type = Counter64
_FpMMUTxPurgeCellErr_Object = MibTableColumn
fpMMUTxPurgeCellErr = _FpMMUTxPurgeCellErr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 14),
    _FpMMUTxPurgeCellErr_Type()
)
fpMMUTxPurgeCellErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpMMUTxPurgeCellErr.setStatus("current")
_FpMMUAgedDrops_Type = Counter64
_FpMMUAgedDrops_Object = MibTableColumn
fpMMUAgedDrops = _FpMMUAgedDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 15),
    _FpMMUAgedDrops_Type()
)
fpMMUAgedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpMMUAgedDrops.setStatus("current")
_FpEgressFCSDrops_Type = Counter64
_FpEgressFCSDrops_Object = MibTableColumn
fpEgressFCSDrops = _FpEgressFCSDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 16),
    _FpEgressFCSDrops_Type()
)
fpEgressFCSDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgressFCSDrops.setStatus("current")
_FpEgIPv4L3UCAgedDrops_Type = Counter64
_FpEgIPv4L3UCAgedDrops_Object = MibTableColumn
fpEgIPv4L3UCAgedDrops = _FpEgIPv4L3UCAgedDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 17),
    _FpEgIPv4L3UCAgedDrops_Type()
)
fpEgIPv4L3UCAgedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgIPv4L3UCAgedDrops.setStatus("current")
_FpEgTTLThresholdDrops_Type = Counter64
_FpEgTTLThresholdDrops_Object = MibTableColumn
fpEgTTLThresholdDrops = _FpEgTTLThresholdDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 18),
    _FpEgTTLThresholdDrops_Type()
)
fpEgTTLThresholdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgTTLThresholdDrops.setStatus("current")
_FpEgInvalidVLANCounterDrops_Type = Counter64
_FpEgInvalidVLANCounterDrops_Object = MibTableColumn
fpEgInvalidVLANCounterDrops = _FpEgInvalidVLANCounterDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 19),
    _FpEgInvalidVLANCounterDrops_Type()
)
fpEgInvalidVLANCounterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgInvalidVLANCounterDrops.setStatus("current")
_FpEgL2MCDrops_Type = Counter64
_FpEgL2MCDrops_Object = MibTableColumn
fpEgL2MCDrops = _FpEgL2MCDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 20),
    _FpEgL2MCDrops_Type()
)
fpEgL2MCDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgL2MCDrops.setStatus("current")
_FpEgPktDropsOfAnyCondition_Type = Counter64
_FpEgPktDropsOfAnyCondition_Object = MibTableColumn
fpEgPktDropsOfAnyCondition = _FpEgPktDropsOfAnyCondition_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 21),
    _FpEgPktDropsOfAnyCondition_Type()
)
fpEgPktDropsOfAnyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgPktDropsOfAnyCondition.setStatus("current")
_FpEgHgMacUnderFlow_Type = Counter64
_FpEgHgMacUnderFlow_Object = MibTableColumn
fpEgHgMacUnderFlow = _FpEgHgMacUnderFlow_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 22),
    _FpEgHgMacUnderFlow_Type()
)
fpEgHgMacUnderFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgHgMacUnderFlow.setStatus("current")
_FpEgTxErrPktCounter_Type = Counter64
_FpEgTxErrPktCounter_Object = MibTableColumn
fpEgTxErrPktCounter = _FpEgTxErrPktCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 23),
    _FpEgTxErrPktCounter_Type()
)
fpEgTxErrPktCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgTxErrPktCounter.setStatus("current")
_FpFlowControlDrops_Type = Counter64
_FpFlowControlDrops_Object = MibTableColumn
fpFlowControlDrops = _FpFlowControlDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 3, 1, 24),
    _FpFlowControlDrops_Type()
)
fpFlowControlDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpFlowControlDrops.setStatus("current")
_FpPacketBufferTable_Object = MibTable
fpPacketBufferTable = _FpPacketBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fpPacketBufferTable.setStatus("current")
_FpPacketBufferEntry_Object = MibTableRow
fpPacketBufferEntry = _FpPacketBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 4, 1)
)
fpPacketBufferEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpPortPipe"),
)
if mibBuilder.loadTexts:
    fpPacketBufferEntry.setStatus("current")


class _FpPortPipe_Type(Integer32):
    """Custom type fpPortPipe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FpPortPipe_Type.__name__ = "Integer32"
_FpPortPipe_Object = MibTableColumn
fpPortPipe = _FpPortPipe_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 4, 1, 1),
    _FpPortPipe_Type()
)
fpPortPipe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpPortPipe.setStatus("current")
_FpTotalPacketBuffer_Type = Counter32
_FpTotalPacketBuffer_Object = MibTableColumn
fpTotalPacketBuffer = _FpTotalPacketBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 4, 1, 2),
    _FpTotalPacketBuffer_Type()
)
fpTotalPacketBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTotalPacketBuffer.setStatus("current")
_FpCurrentAvailBuffer_Type = Counter32
_FpCurrentAvailBuffer_Object = MibTableColumn
fpCurrentAvailBuffer = _FpCurrentAvailBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 4, 1, 3),
    _FpCurrentAvailBuffer_Type()
)
fpCurrentAvailBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCurrentAvailBuffer.setStatus("current")
_FpPacketBufferAlloc_Type = Counter32
_FpPacketBufferAlloc_Object = MibTableColumn
fpPacketBufferAlloc = _FpPacketBufferAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 4, 1, 4),
    _FpPacketBufferAlloc_Type()
)
fpPacketBufferAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPacketBufferAlloc.setStatus("current")
_FpStatsPerPortTable_Object = MibTable
fpStatsPerPortTable = _FpStatsPerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fpStatsPerPortTable.setStatus("current")
_FpStatsPerPortEntry_Object = MibTableRow
fpStatsPerPortEntry = _FpStatsPerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 5, 1)
)
fpStatsPerPortEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
)
if mibBuilder.loadTexts:
    fpStatsPerPortEntry.setStatus("current")
_FpCurrentUsagePerPort_Type = Counter32
_FpCurrentUsagePerPort_Object = MibTableColumn
fpCurrentUsagePerPort = _FpCurrentUsagePerPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 5, 1, 1),
    _FpCurrentUsagePerPort_Type()
)
fpCurrentUsagePerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCurrentUsagePerPort.setStatus("current")
_FpDefaultPacketBuffAlloc_Type = Counter32
_FpDefaultPacketBuffAlloc_Object = MibTableColumn
fpDefaultPacketBuffAlloc = _FpDefaultPacketBuffAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 5, 1, 2),
    _FpDefaultPacketBuffAlloc_Type()
)
fpDefaultPacketBuffAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDefaultPacketBuffAlloc.setStatus("current")
_FpMaxLimitPerPort_Type = Counter32
_FpMaxLimitPerPort_Object = MibTableColumn
fpMaxLimitPerPort = _FpMaxLimitPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 5, 1, 3),
    _FpMaxLimitPerPort_Type()
)
fpMaxLimitPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpMaxLimitPerPort.setStatus("current")
_FpStatsPerCOSTable_Object = MibTable
fpStatsPerCOSTable = _FpStatsPerCOSTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fpStatsPerCOSTable.setStatus("current")
_FpStatsPerCOSEntry_Object = MibTableRow
fpStatsPerCOSEntry = _FpStatsPerCOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 6, 1)
)
fpStatsPerCOSEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
    (0, "F10-FPSTATS-MIB", "fpPerPortCOSNumber"),
)
if mibBuilder.loadTexts:
    fpStatsPerCOSEntry.setStatus("current")


class _FpPerPortCOSNumber_Type(Integer32):
    """Custom type fpPerPortCOSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_FpPerPortCOSNumber_Type.__name__ = "Integer32"
_FpPerPortCOSNumber_Object = MibTableColumn
fpPerPortCOSNumber = _FpPerPortCOSNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 6, 1, 1),
    _FpPerPortCOSNumber_Type()
)
fpPerPortCOSNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpPerPortCOSNumber.setStatus("current")
_FpCurrentUsagePerCOS_Type = Counter32
_FpCurrentUsagePerCOS_Object = MibTableColumn
fpCurrentUsagePerCOS = _FpCurrentUsagePerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 6, 1, 2),
    _FpCurrentUsagePerCOS_Type()
)
fpCurrentUsagePerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCurrentUsagePerCOS.setStatus("current")
_FpDefaultPacketBuffAllocPerCOS_Type = Counter32
_FpDefaultPacketBuffAllocPerCOS_Object = MibTableColumn
fpDefaultPacketBuffAllocPerCOS = _FpDefaultPacketBuffAllocPerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 6, 1, 3),
    _FpDefaultPacketBuffAllocPerCOS_Type()
)
fpDefaultPacketBuffAllocPerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDefaultPacketBuffAllocPerCOS.setStatus("current")
_FpMaxLimitPerCOS_Type = Counter32
_FpMaxLimitPerCOS_Object = MibTableColumn
fpMaxLimitPerCOS = _FpMaxLimitPerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 6, 1, 4),
    _FpMaxLimitPerCOS_Type()
)
fpMaxLimitPerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpMaxLimitPerCOS.setStatus("current")
_FpHOLDropsPerCOS_Type = Counter64
_FpHOLDropsPerCOS_Object = MibTableColumn
fpHOLDropsPerCOS = _FpHOLDropsPerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 6, 1, 5),
    _FpHOLDropsPerCOS_Type()
)
fpHOLDropsPerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpHOLDropsPerCOS.setStatus("current")
_FpCpuDataPlaneCOSTable_Object = MibTable
fpCpuDataPlaneCOSTable = _FpCpuDataPlaneCOSTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fpCpuDataPlaneCOSTable.setStatus("current")
_FpCpuDataPlaneCOSEntry_Object = MibTableRow
fpCpuDataPlaneCOSEntry = _FpCpuDataPlaneCOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 7, 1)
)
fpCpuDataPlaneCOSEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpCOSIndex"),
)
if mibBuilder.loadTexts:
    fpCpuDataPlaneCOSEntry.setStatus("current")


class _FpCOSIndex_Type(Integer32):
    """Custom type fpCOSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FpCOSIndex_Type.__name__ = "Integer32"
_FpCOSIndex_Object = MibTableColumn
fpCOSIndex = _FpCOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 7, 1, 1),
    _FpCOSIndex_Type()
)
fpCOSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpCOSIndex.setStatus("current")
_FpRxPktCOS_Type = Counter32
_FpRxPktCOS_Object = MibTableColumn
fpRxPktCOS = _FpRxPktCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 7, 1, 2),
    _FpRxPktCOS_Type()
)
fpRxPktCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRxPktCOS.setStatus("current")
_FpTxPktCOS_Type = Counter32
_FpTxPktCOS_Object = MibTableColumn
fpTxPktCOS = _FpTxPktCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 7, 1, 3),
    _FpTxPktCOS_Type()
)
fpTxPktCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTxPktCOS.setStatus("current")
_FpEgrQBuffSnapshotTable_Object = MibTable
fpEgrQBuffSnapshotTable = _FpEgrQBuffSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 8)
)
if mibBuilder.loadTexts:
    fpEgrQBuffSnapshotTable.setStatus("current")
_FpEgrQBuffSnapshotEntry_Object = MibTableRow
fpEgrQBuffSnapshotEntry = _FpEgrQBuffSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 8, 1)
)
fpEgrQBuffSnapshotEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
    (0, "F10-FPSTATS-MIB", "fpPerPortCOSNumber"),
)
if mibBuilder.loadTexts:
    fpEgrQBuffSnapshotEntry.setStatus("current")
_FpEgrQTotBuffCells_Type = Counter32
_FpEgrQTotBuffCells_Object = MibTableColumn
fpEgrQTotBuffCells = _FpEgrQTotBuffCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 8, 1, 1),
    _FpEgrQTotBuffCells_Type()
)
fpEgrQTotBuffCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgrQTotBuffCells.setStatus("current")
_FpIngPgBuffSnapshotTable_Object = MibTable
fpIngPgBuffSnapshotTable = _FpIngPgBuffSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 9)
)
if mibBuilder.loadTexts:
    fpIngPgBuffSnapshotTable.setStatus("current")
_FpIngPgBuffSnapshotEntry_Object = MibTableRow
fpIngPgBuffSnapshotEntry = _FpIngPgBuffSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 9, 1)
)
fpIngPgBuffSnapshotEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
    (0, "F10-FPSTATS-MIB", "fpPerPortPGIndex"),
)
if mibBuilder.loadTexts:
    fpIngPgBuffSnapshotEntry.setStatus("current")
_FpPerPortPGIndex_Type = Integer32
_FpPerPortPGIndex_Object = MibTableColumn
fpPerPortPGIndex = _FpPerPortPGIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 9, 1, 1),
    _FpPerPortPGIndex_Type()
)
fpPerPortPGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpPerPortPGIndex.setStatus("current")
_FpIngSharedCells_Type = Counter32
_FpIngSharedCells_Object = MibTableColumn
fpIngSharedCells = _FpIngSharedCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 9, 1, 2),
    _FpIngSharedCells_Type()
)
fpIngSharedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngSharedCells.setStatus("current")
_FpIngHeadroomCells_Type = Counter32
_FpIngHeadroomCells_Object = MibTableColumn
fpIngHeadroomCells = _FpIngHeadroomCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 9, 1, 3),
    _FpIngHeadroomCells_Type()
)
fpIngHeadroomCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIngHeadroomCells.setStatus("current")
_FpStatsPerPgTable_Object = MibTable
fpStatsPerPgTable = _FpStatsPerPgTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fpStatsPerPgTable.setStatus("current")
_FpStatsPerPgEntry_Object = MibTableRow
fpStatsPerPgEntry = _FpStatsPerPgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1)
)
fpStatsPerPgEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
    (0, "F10-FPSTATS-MIB", "fpPerPortPGIndex"),
)
if mibBuilder.loadTexts:
    fpStatsPerPgEntry.setStatus("current")
_FpStatsPgLimitMinCells_Type = Integer32
_FpStatsPgLimitMinCells_Object = MibTableColumn
fpStatsPgLimitMinCells = _FpStatsPgLimitMinCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1, 1),
    _FpStatsPgLimitMinCells_Type()
)
fpStatsPgLimitMinCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpStatsPgLimitMinCells.setStatus("current")
_FpStatsPgSharedCells_Type = Integer32
_FpStatsPgSharedCells_Object = MibTableColumn
fpStatsPgSharedCells = _FpStatsPgSharedCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1, 2),
    _FpStatsPgSharedCells_Type()
)
fpStatsPgSharedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpStatsPgSharedCells.setStatus("current")


class _FpStatsPgSharedMode_Type(Integer32):
    """Custom type fpStatsPgSharedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_FpStatsPgSharedMode_Type.__name__ = "Integer32"
_FpStatsPgSharedMode_Object = MibTableColumn
fpStatsPgSharedMode = _FpStatsPgSharedMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1, 3),
    _FpStatsPgSharedMode_Type()
)
fpStatsPgSharedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpStatsPgSharedMode.setStatus("current")
_FpStatsPgHdrmCells_Type = Integer32
_FpStatsPgHdrmCells_Object = MibTableColumn
fpStatsPgHdrmCells = _FpStatsPgHdrmCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1, 4),
    _FpStatsPgHdrmCells_Type()
)
fpStatsPgHdrmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpStatsPgHdrmCells.setStatus("current")
_FpStatsPgCounterMinCells_Type = Counter32
_FpStatsPgCounterMinCells_Object = MibTableColumn
fpStatsPgCounterMinCells = _FpStatsPgCounterMinCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1, 5),
    _FpStatsPgCounterMinCells_Type()
)
fpStatsPgCounterMinCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpStatsPgCounterMinCells.setStatus("current")
_FpStatsPgCounterSharedCells_Type = Counter32
_FpStatsPgCounterSharedCells_Object = MibTableColumn
fpStatsPgCounterSharedCells = _FpStatsPgCounterSharedCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1, 6),
    _FpStatsPgCounterSharedCells_Type()
)
fpStatsPgCounterSharedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpStatsPgCounterSharedCells.setStatus("current")
_FpStatsPgCounterHdrmCells_Type = Counter32
_FpStatsPgCounterHdrmCells_Object = MibTableColumn
fpStatsPgCounterHdrmCells = _FpStatsPgCounterHdrmCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 10, 1, 7),
    _FpStatsPgCounterHdrmCells_Type()
)
fpStatsPgCounterHdrmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpStatsPgCounterHdrmCells.setStatus("current")
_PfcPerPrioTable_Object = MibTable
pfcPerPrioTable = _PfcPerPrioTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pfcPerPrioTable.setStatus("current")
_PfcPerPrioEntry_Object = MibTableRow
pfcPerPrioEntry = _PfcPerPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 11, 1)
)
pfcPerPrioEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
    (0, "F10-FPSTATS-MIB", "prioIndex"),
)
if mibBuilder.loadTexts:
    pfcPerPrioEntry.setStatus("current")


class _PrioIndex_Type(Integer32):
    """Custom type prioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PrioIndex_Type.__name__ = "Integer32"
_PrioIndex_Object = MibTableColumn
prioIndex = _PrioIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 11, 1, 1),
    _PrioIndex_Type()
)
prioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIndex.setStatus("current")
_PfcPerPrioRequests_Type = Counter64
_PfcPerPrioRequests_Object = MibTableColumn
pfcPerPrioRequests = _PfcPerPrioRequests_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 11, 1, 2),
    _PfcPerPrioRequests_Type()
)
pfcPerPrioRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfcPerPrioRequests.setStatus("current")
if mibBuilder.loadTexts:
    pfcPerPrioRequests.setUnits("Requests")
_PfcPerPrioIndications_Type = Counter64
_PfcPerPrioIndications_Object = MibTableColumn
pfcPerPrioIndications = _PfcPerPrioIndications_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 11, 1, 3),
    _PfcPerPrioIndications_Type()
)
pfcPerPrioIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfcPerPrioIndications.setStatus("current")
if mibBuilder.loadTexts:
    pfcPerPrioIndications.setUnits("Indications")
_FpCpuPartyBusPortStatsTable_Object = MibTable
fpCpuPartyBusPortStatsTable = _FpCpuPartyBusPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12)
)
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsTable.setStatus("current")
_FpCpuPartyBusPortStatsEntry_Object = MibTableRow
fpCpuPartyBusPortStatsEntry = _FpCpuPartyBusPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1)
)
fpCpuPartyBusPortStatsEntry.setIndexNames(
    (0, "F10-FPSTATS-MIB", "fpStackUnitIndex"),
    (0, "F10-FPSTATS-MIB", "fpStackPortIndex"),
)
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsEntry.setStatus("current")
_FpCpuPartyBusPortStatsOutOctets_Type = Counter64
_FpCpuPartyBusPortStatsOutOctets_Object = MibTableColumn
fpCpuPartyBusPortStatsOutOctets = _FpCpuPartyBusPortStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 1),
    _FpCpuPartyBusPortStatsOutOctets_Type()
)
fpCpuPartyBusPortStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutOctets.setStatus("current")
_FpCpuPartyBusPortStatsOutDropPkts_Type = Counter32
_FpCpuPartyBusPortStatsOutDropPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutDropPkts = _FpCpuPartyBusPortStatsOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 2),
    _FpCpuPartyBusPortStatsOutDropPkts_Type()
)
fpCpuPartyBusPortStatsOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutDropPkts.setStatus("current")
_FpCpuPartyBusPortStatsOutCOS0Pkts_Type = Counter32
_FpCpuPartyBusPortStatsOutCOS0Pkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutCOS0Pkts = _FpCpuPartyBusPortStatsOutCOS0Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 3),
    _FpCpuPartyBusPortStatsOutCOS0Pkts_Type()
)
fpCpuPartyBusPortStatsOutCOS0Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutCOS0Pkts.setStatus("current")
_FpCpuPartyBusPortStatsOutCOS1Pkts_Type = Counter32
_FpCpuPartyBusPortStatsOutCOS1Pkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutCOS1Pkts = _FpCpuPartyBusPortStatsOutCOS1Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 4),
    _FpCpuPartyBusPortStatsOutCOS1Pkts_Type()
)
fpCpuPartyBusPortStatsOutCOS1Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutCOS1Pkts.setStatus("current")
_FpCpuPartyBusPortStatsOutCOS2Pkts_Type = Counter32
_FpCpuPartyBusPortStatsOutCOS2Pkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutCOS2Pkts = _FpCpuPartyBusPortStatsOutCOS2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 5),
    _FpCpuPartyBusPortStatsOutCOS2Pkts_Type()
)
fpCpuPartyBusPortStatsOutCOS2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutCOS2Pkts.setStatus("current")
_FpCpuPartyBusPortStatsOutCOS3Pkts_Type = Counter32
_FpCpuPartyBusPortStatsOutCOS3Pkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutCOS3Pkts = _FpCpuPartyBusPortStatsOutCOS3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 6),
    _FpCpuPartyBusPortStatsOutCOS3Pkts_Type()
)
fpCpuPartyBusPortStatsOutCOS3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutCOS3Pkts.setStatus("current")
_FpCpuPartyBusPortStatsOutCOS4Pkts_Type = Counter32
_FpCpuPartyBusPortStatsOutCOS4Pkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutCOS4Pkts = _FpCpuPartyBusPortStatsOutCOS4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 7),
    _FpCpuPartyBusPortStatsOutCOS4Pkts_Type()
)
fpCpuPartyBusPortStatsOutCOS4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutCOS4Pkts.setStatus("current")
_FpCpuPartyBusPortStatsOutCOS5Pkts_Type = Counter32
_FpCpuPartyBusPortStatsOutCOS5Pkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutCOS5Pkts = _FpCpuPartyBusPortStatsOutCOS5Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 8),
    _FpCpuPartyBusPortStatsOutCOS5Pkts_Type()
)
fpCpuPartyBusPortStatsOutCOS5Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutCOS5Pkts.setStatus("current")
_FpCpuPartyBusPortStatsOutUnicastPkts_Type = Counter32
_FpCpuPartyBusPortStatsOutUnicastPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutUnicastPkts = _FpCpuPartyBusPortStatsOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 9),
    _FpCpuPartyBusPortStatsOutUnicastPkts_Type()
)
fpCpuPartyBusPortStatsOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutUnicastPkts.setStatus("current")
_FpCpuPartyBusPortStatsOutMulticastPkts_Type = Counter32
_FpCpuPartyBusPortStatsOutMulticastPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutMulticastPkts = _FpCpuPartyBusPortStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 10),
    _FpCpuPartyBusPortStatsOutMulticastPkts_Type()
)
fpCpuPartyBusPortStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutMulticastPkts.setStatus("current")
_FpCpuPartyBusPortStatsOutBroadcastPkts_Type = Counter32
_FpCpuPartyBusPortStatsOutBroadcastPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutBroadcastPkts = _FpCpuPartyBusPortStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 11),
    _FpCpuPartyBusPortStatsOutBroadcastPkts_Type()
)
fpCpuPartyBusPortStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutBroadcastPkts.setStatus("current")
_FpCpuPartyBusPortStatsOutPausePkts_Type = Counter32
_FpCpuPartyBusPortStatsOutPausePkts_Object = MibTableColumn
fpCpuPartyBusPortStatsOutPausePkts = _FpCpuPartyBusPortStatsOutPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 12),
    _FpCpuPartyBusPortStatsOutPausePkts_Type()
)
fpCpuPartyBusPortStatsOutPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutPausePkts.setStatus("current")
_FpCpuPartyBusPortStatsOutCollisions_Type = Counter32
_FpCpuPartyBusPortStatsOutCollisions_Object = MibTableColumn
fpCpuPartyBusPortStatsOutCollisions = _FpCpuPartyBusPortStatsOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 13),
    _FpCpuPartyBusPortStatsOutCollisions_Type()
)
fpCpuPartyBusPortStatsOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutCollisions.setStatus("current")
_FpCpuPartyBusPortStatsOutSingleCollisions_Type = Counter32
_FpCpuPartyBusPortStatsOutSingleCollisions_Object = MibTableColumn
fpCpuPartyBusPortStatsOutSingleCollisions = _FpCpuPartyBusPortStatsOutSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 14),
    _FpCpuPartyBusPortStatsOutSingleCollisions_Type()
)
fpCpuPartyBusPortStatsOutSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutSingleCollisions.setStatus("current")
_FpCpuPartyBusPortStatsOutMultiCollisions_Type = Counter32
_FpCpuPartyBusPortStatsOutMultiCollisions_Object = MibTableColumn
fpCpuPartyBusPortStatsOutMultiCollisions = _FpCpuPartyBusPortStatsOutMultiCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 15),
    _FpCpuPartyBusPortStatsOutMultiCollisions_Type()
)
fpCpuPartyBusPortStatsOutMultiCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutMultiCollisions.setStatus("current")
_FpCpuPartyBusPortStatsOutLateCollisions_Type = Counter32
_FpCpuPartyBusPortStatsOutLateCollisions_Object = MibTableColumn
fpCpuPartyBusPortStatsOutLateCollisions = _FpCpuPartyBusPortStatsOutLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 16),
    _FpCpuPartyBusPortStatsOutLateCollisions_Type()
)
fpCpuPartyBusPortStatsOutLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutLateCollisions.setStatus("current")
_FpCpuPartyBusPortStatsOutExcessCollisions_Type = Counter32
_FpCpuPartyBusPortStatsOutExcessCollisions_Object = MibTableColumn
fpCpuPartyBusPortStatsOutExcessCollisions = _FpCpuPartyBusPortStatsOutExcessCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 17),
    _FpCpuPartyBusPortStatsOutExcessCollisions_Type()
)
fpCpuPartyBusPortStatsOutExcessCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutExcessCollisions.setStatus("current")
_FpCpuPartyBusPortStatsOutDeferred_Type = Counter32
_FpCpuPartyBusPortStatsOutDeferred_Object = MibTableColumn
fpCpuPartyBusPortStatsOutDeferred = _FpCpuPartyBusPortStatsOutDeferred_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 18),
    _FpCpuPartyBusPortStatsOutDeferred_Type()
)
fpCpuPartyBusPortStatsOutDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutDeferred.setStatus("current")
_FpCpuPartyBusPortStatsOutDiscarded_Type = Counter32
_FpCpuPartyBusPortStatsOutDiscarded_Object = MibTableColumn
fpCpuPartyBusPortStatsOutDiscarded = _FpCpuPartyBusPortStatsOutDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 19),
    _FpCpuPartyBusPortStatsOutDiscarded_Type()
)
fpCpuPartyBusPortStatsOutDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsOutDiscarded.setStatus("current")
_FpCpuPartyBusPortStatsInOctets_Type = Counter64
_FpCpuPartyBusPortStatsInOctets_Object = MibTableColumn
fpCpuPartyBusPortStatsInOctets = _FpCpuPartyBusPortStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 20),
    _FpCpuPartyBusPortStatsInOctets_Type()
)
fpCpuPartyBusPortStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInOctets.setStatus("current")
_FpCpuPartyBusPortStatsInUndersizePkts_Type = Counter32
_FpCpuPartyBusPortStatsInUndersizePkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInUndersizePkts = _FpCpuPartyBusPortStatsInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 21),
    _FpCpuPartyBusPortStatsInUndersizePkts_Type()
)
fpCpuPartyBusPortStatsInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInUndersizePkts.setStatus("current")
_FpCpuPartyBusPortStatsInOversizePkts_Type = Counter32
_FpCpuPartyBusPortStatsInOversizePkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInOversizePkts = _FpCpuPartyBusPortStatsInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 22),
    _FpCpuPartyBusPortStatsInOversizePkts_Type()
)
fpCpuPartyBusPortStatsInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInOversizePkts.setStatus("current")
_FpCpuPartyBusPortStatsInPausePkts_Type = Counter32
_FpCpuPartyBusPortStatsInPausePkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInPausePkts = _FpCpuPartyBusPortStatsInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 23),
    _FpCpuPartyBusPortStatsInPausePkts_Type()
)
fpCpuPartyBusPortStatsInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInPausePkts.setStatus("current")
_FpCpuPartyBusPortStatsIn64OctetPkts_Type = Counter32
_FpCpuPartyBusPortStatsIn64OctetPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsIn64OctetPkts = _FpCpuPartyBusPortStatsIn64OctetPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 24),
    _FpCpuPartyBusPortStatsIn64OctetPkts_Type()
)
fpCpuPartyBusPortStatsIn64OctetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsIn64OctetPkts.setStatus("current")
_FpCpuPartyBusPortStatsIn65To127OctetPkts_Type = Counter32
_FpCpuPartyBusPortStatsIn65To127OctetPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsIn65To127OctetPkts = _FpCpuPartyBusPortStatsIn65To127OctetPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 25),
    _FpCpuPartyBusPortStatsIn65To127OctetPkts_Type()
)
fpCpuPartyBusPortStatsIn65To127OctetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsIn65To127OctetPkts.setStatus("current")
_FpCpuPartyBusPortStatsIn128To255OctetPkts_Type = Counter32
_FpCpuPartyBusPortStatsIn128To255OctetPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsIn128To255OctetPkts = _FpCpuPartyBusPortStatsIn128To255OctetPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 26),
    _FpCpuPartyBusPortStatsIn128To255OctetPkts_Type()
)
fpCpuPartyBusPortStatsIn128To255OctetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsIn128To255OctetPkts.setStatus("current")
_FpCpuPartyBusPortStatsIn256To511OctetPkts_Type = Counter32
_FpCpuPartyBusPortStatsIn256To511OctetPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsIn256To511OctetPkts = _FpCpuPartyBusPortStatsIn256To511OctetPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 27),
    _FpCpuPartyBusPortStatsIn256To511OctetPkts_Type()
)
fpCpuPartyBusPortStatsIn256To511OctetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsIn256To511OctetPkts.setStatus("current")
_FpCpuPartyBusPortStatsIn512To1023OctetPkts_Type = Counter32
_FpCpuPartyBusPortStatsIn512To1023OctetPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsIn512To1023OctetPkts = _FpCpuPartyBusPortStatsIn512To1023OctetPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 28),
    _FpCpuPartyBusPortStatsIn512To1023OctetPkts_Type()
)
fpCpuPartyBusPortStatsIn512To1023OctetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsIn512To1023OctetPkts.setStatus("current")
_FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Type = Counter32
_FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts = _FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 29),
    _FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Type()
)
fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts.setStatus("current")
_FpCpuPartyBusPortStatsInJabbers_Type = Counter32
_FpCpuPartyBusPortStatsInJabbers_Object = MibTableColumn
fpCpuPartyBusPortStatsInJabbers = _FpCpuPartyBusPortStatsInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 30),
    _FpCpuPartyBusPortStatsInJabbers_Type()
)
fpCpuPartyBusPortStatsInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInJabbers.setStatus("current")
_FpCpuPartyBusPortStatsInAlignErrors_Type = Counter32
_FpCpuPartyBusPortStatsInAlignErrors_Object = MibTableColumn
fpCpuPartyBusPortStatsInAlignErrors = _FpCpuPartyBusPortStatsInAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 31),
    _FpCpuPartyBusPortStatsInAlignErrors_Type()
)
fpCpuPartyBusPortStatsInAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInAlignErrors.setStatus("current")
_FpCpuPartyBusPortStatsInFcsErrors_Type = Counter32
_FpCpuPartyBusPortStatsInFcsErrors_Object = MibTableColumn
fpCpuPartyBusPortStatsInFcsErrors = _FpCpuPartyBusPortStatsInFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 32),
    _FpCpuPartyBusPortStatsInFcsErrors_Type()
)
fpCpuPartyBusPortStatsInFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInFcsErrors.setStatus("current")
_FpCpuPartyBusPortStatsInGoodOctets_Type = Counter32
_FpCpuPartyBusPortStatsInGoodOctets_Object = MibTableColumn
fpCpuPartyBusPortStatsInGoodOctets = _FpCpuPartyBusPortStatsInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 33),
    _FpCpuPartyBusPortStatsInGoodOctets_Type()
)
fpCpuPartyBusPortStatsInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInGoodOctets.setStatus("current")
_FpCpuPartyBusPortStatsInDropPkts_Type = Counter32
_FpCpuPartyBusPortStatsInDropPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInDropPkts = _FpCpuPartyBusPortStatsInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 34),
    _FpCpuPartyBusPortStatsInDropPkts_Type()
)
fpCpuPartyBusPortStatsInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInDropPkts.setStatus("current")
_FpCpuPartyBusPortStatsInUnicastPkts_Type = Counter32
_FpCpuPartyBusPortStatsInUnicastPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInUnicastPkts = _FpCpuPartyBusPortStatsInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 35),
    _FpCpuPartyBusPortStatsInUnicastPkts_Type()
)
fpCpuPartyBusPortStatsInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInUnicastPkts.setStatus("current")
_FpCpuPartyBusPortStatsInMulticastPkts_Type = Counter32
_FpCpuPartyBusPortStatsInMulticastPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInMulticastPkts = _FpCpuPartyBusPortStatsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 36),
    _FpCpuPartyBusPortStatsInMulticastPkts_Type()
)
fpCpuPartyBusPortStatsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInMulticastPkts.setStatus("current")
_FpCpuPartyBusPortStatsInBroadcastPkts_Type = Counter32
_FpCpuPartyBusPortStatsInBroadcastPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInBroadcastPkts = _FpCpuPartyBusPortStatsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 37),
    _FpCpuPartyBusPortStatsInBroadcastPkts_Type()
)
fpCpuPartyBusPortStatsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInBroadcastPkts.setStatus("current")
_FpCpuPartyBusPortStatsInSrcAddrChanges_Type = Counter32
_FpCpuPartyBusPortStatsInSrcAddrChanges_Object = MibTableColumn
fpCpuPartyBusPortStatsInSrcAddrChanges = _FpCpuPartyBusPortStatsInSrcAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 38),
    _FpCpuPartyBusPortStatsInSrcAddrChanges_Type()
)
fpCpuPartyBusPortStatsInSrcAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInSrcAddrChanges.setStatus("current")
_FpCpuPartyBusPortStatsInFragments_Type = Counter32
_FpCpuPartyBusPortStatsInFragments_Object = MibTableColumn
fpCpuPartyBusPortStatsInFragments = _FpCpuPartyBusPortStatsInFragments_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 39),
    _FpCpuPartyBusPortStatsInFragments_Type()
)
fpCpuPartyBusPortStatsInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInFragments.setStatus("current")
_FpCpuPartyBusPortStatsInJumboPkts_Type = Counter32
_FpCpuPartyBusPortStatsInJumboPkts_Object = MibTableColumn
fpCpuPartyBusPortStatsInJumboPkts = _FpCpuPartyBusPortStatsInJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 40),
    _FpCpuPartyBusPortStatsInJumboPkts_Type()
)
fpCpuPartyBusPortStatsInJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInJumboPkts.setStatus("current")
_FpCpuPartyBusPortStatsInSymbolErrors_Type = Counter32
_FpCpuPartyBusPortStatsInSymbolErrors_Object = MibTableColumn
fpCpuPartyBusPortStatsInSymbolErrors = _FpCpuPartyBusPortStatsInSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 41),
    _FpCpuPartyBusPortStatsInSymbolErrors_Type()
)
fpCpuPartyBusPortStatsInSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInSymbolErrors.setStatus("current")
_FpCpuPartyBusPortStatsInInRangeErrors_Type = Counter32
_FpCpuPartyBusPortStatsInInRangeErrors_Object = MibTableColumn
fpCpuPartyBusPortStatsInInRangeErrors = _FpCpuPartyBusPortStatsInInRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 42),
    _FpCpuPartyBusPortStatsInInRangeErrors_Type()
)
fpCpuPartyBusPortStatsInInRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInInRangeErrors.setStatus("current")
_FpCpuPartyBusPortStatsInOutRangeErrors_Type = Counter32
_FpCpuPartyBusPortStatsInOutRangeErrors_Object = MibTableColumn
fpCpuPartyBusPortStatsInOutRangeErrors = _FpCpuPartyBusPortStatsInOutRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 12, 1, 43),
    _FpCpuPartyBusPortStatsInOutRangeErrors_Type()
)
fpCpuPartyBusPortStatsInOutRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCpuPartyBusPortStatsInOutRangeErrors.setStatus("current")
_FpDropsIfTable_Object = MibTable
fpDropsIfTable = _FpDropsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fpDropsIfTable.setStatus("current")
_FpDropsIfEntry_Object = MibTableRow
fpDropsIfEntry = _FpDropsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1)
)
fpDropsIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fpDropsIfEntry.setStatus("current")
_FpIfIngressDrops_Type = Counter64
_FpIfIngressDrops_Object = MibTableColumn
fpIfIngressDrops = _FpIfIngressDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 1),
    _FpIfIngressDrops_Type()
)
fpIfIngressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngressDrops.setStatus("current")
_FpIfIngIBPCBPFullDrops_Type = Counter64
_FpIfIngIBPCBPFullDrops_Object = MibTableColumn
fpIfIngIBPCBPFullDrops = _FpIfIngIBPCBPFullDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 2),
    _FpIfIngIBPCBPFullDrops_Type()
)
fpIfIngIBPCBPFullDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngIBPCBPFullDrops.setStatus("current")
_FpIfIngPortSTPnotFwdDrops_Type = Counter64
_FpIfIngPortSTPnotFwdDrops_Object = MibTableColumn
fpIfIngPortSTPnotFwdDrops = _FpIfIngPortSTPnotFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 3),
    _FpIfIngPortSTPnotFwdDrops_Type()
)
fpIfIngPortSTPnotFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngPortSTPnotFwdDrops.setStatus("current")
_FpIfIngIPv4L3Discards_Type = Counter64
_FpIfIngIPv4L3Discards_Object = MibTableColumn
fpIfIngIPv4L3Discards = _FpIfIngIPv4L3Discards_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 4),
    _FpIfIngIPv4L3Discards_Type()
)
fpIfIngIPv4L3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngIPv4L3Discards.setStatus("current")
_FpIfIngPolicyDiscards_Type = Counter64
_FpIfIngPolicyDiscards_Object = MibTableColumn
fpIfIngPolicyDiscards = _FpIfIngPolicyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 5),
    _FpIfIngPolicyDiscards_Type()
)
fpIfIngPolicyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngPolicyDiscards.setStatus("current")
_FpIfIngPacketsDroppedByFP_Type = Counter64
_FpIfIngPacketsDroppedByFP_Object = MibTableColumn
fpIfIngPacketsDroppedByFP = _FpIfIngPacketsDroppedByFP_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 6),
    _FpIfIngPacketsDroppedByFP_Type()
)
fpIfIngPacketsDroppedByFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngPacketsDroppedByFP.setStatus("current")
_FpIfIngL2L3Drops_Type = Counter64
_FpIfIngL2L3Drops_Object = MibTableColumn
fpIfIngL2L3Drops = _FpIfIngL2L3Drops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 7),
    _FpIfIngL2L3Drops_Type()
)
fpIfIngL2L3Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngL2L3Drops.setStatus("current")
_FpIfIngPortBitMapZeroDrops_Type = Counter64
_FpIfIngPortBitMapZeroDrops_Object = MibTableColumn
fpIfIngPortBitMapZeroDrops = _FpIfIngPortBitMapZeroDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 8),
    _FpIfIngPortBitMapZeroDrops_Type()
)
fpIfIngPortBitMapZeroDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngPortBitMapZeroDrops.setStatus("current")
_FpIfIngRxVLANDrops_Type = Counter64
_FpIfIngRxVLANDrops_Object = MibTableColumn
fpIfIngRxVLANDrops = _FpIfIngRxVLANDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 9),
    _FpIfIngRxVLANDrops_Type()
)
fpIfIngRxVLANDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngRxVLANDrops.setStatus("current")
_FpIfIngressFCSDrops_Type = Counter64
_FpIfIngressFCSDrops_Object = MibTableColumn
fpIfIngressFCSDrops = _FpIfIngressFCSDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 10),
    _FpIfIngressFCSDrops_Type()
)
fpIfIngressFCSDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngressFCSDrops.setStatus("current")
_FpIfIngressMTUExceeds_Type = Counter64
_FpIfIngressMTUExceeds_Object = MibTableColumn
fpIfIngressMTUExceeds = _FpIfIngressMTUExceeds_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 11),
    _FpIfIngressMTUExceeds_Type()
)
fpIfIngressMTUExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngressMTUExceeds.setStatus("current")
_FpIfMMUHOLDrops_Type = Counter64
_FpIfMMUHOLDrops_Object = MibTableColumn
fpIfMMUHOLDrops = _FpIfMMUHOLDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 12),
    _FpIfMMUHOLDrops_Type()
)
fpIfMMUHOLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfMMUHOLDrops.setStatus("current")
_FpIfMMUTxPurgeCellErr_Type = Counter64
_FpIfMMUTxPurgeCellErr_Object = MibTableColumn
fpIfMMUTxPurgeCellErr = _FpIfMMUTxPurgeCellErr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 13),
    _FpIfMMUTxPurgeCellErr_Type()
)
fpIfMMUTxPurgeCellErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfMMUTxPurgeCellErr.setStatus("current")
_FpIfMMUAgedDrops_Type = Counter64
_FpIfMMUAgedDrops_Object = MibTableColumn
fpIfMMUAgedDrops = _FpIfMMUAgedDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 14),
    _FpIfMMUAgedDrops_Type()
)
fpIfMMUAgedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfMMUAgedDrops.setStatus("current")
_FpIfEgressFCSDrops_Type = Counter64
_FpIfEgressFCSDrops_Object = MibTableColumn
fpIfEgressFCSDrops = _FpIfEgressFCSDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 15),
    _FpIfEgressFCSDrops_Type()
)
fpIfEgressFCSDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgressFCSDrops.setStatus("current")
_FpIfEgIPv4L3UCAgedDrops_Type = Counter64
_FpIfEgIPv4L3UCAgedDrops_Object = MibTableColumn
fpIfEgIPv4L3UCAgedDrops = _FpIfEgIPv4L3UCAgedDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 16),
    _FpIfEgIPv4L3UCAgedDrops_Type()
)
fpIfEgIPv4L3UCAgedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgIPv4L3UCAgedDrops.setStatus("current")
_FpIfEgTTLThresholdDrops_Type = Counter64
_FpIfEgTTLThresholdDrops_Object = MibTableColumn
fpIfEgTTLThresholdDrops = _FpIfEgTTLThresholdDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 17),
    _FpIfEgTTLThresholdDrops_Type()
)
fpIfEgTTLThresholdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgTTLThresholdDrops.setStatus("current")
_FpIfEgInvalidVLANCounterDrops_Type = Counter64
_FpIfEgInvalidVLANCounterDrops_Object = MibTableColumn
fpIfEgInvalidVLANCounterDrops = _FpIfEgInvalidVLANCounterDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 18),
    _FpIfEgInvalidVLANCounterDrops_Type()
)
fpIfEgInvalidVLANCounterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgInvalidVLANCounterDrops.setStatus("current")
_FpIfEgL2MCDrops_Type = Counter64
_FpIfEgL2MCDrops_Object = MibTableColumn
fpIfEgL2MCDrops = _FpIfEgL2MCDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 19),
    _FpIfEgL2MCDrops_Type()
)
fpIfEgL2MCDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgL2MCDrops.setStatus("current")
_FpIfEgPktDropsOfAnyCondition_Type = Counter64
_FpIfEgPktDropsOfAnyCondition_Object = MibTableColumn
fpIfEgPktDropsOfAnyCondition = _FpIfEgPktDropsOfAnyCondition_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 20),
    _FpIfEgPktDropsOfAnyCondition_Type()
)
fpIfEgPktDropsOfAnyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgPktDropsOfAnyCondition.setStatus("current")
_FpIfEgHgMacUnderFlow_Type = Counter64
_FpIfEgHgMacUnderFlow_Object = MibTableColumn
fpIfEgHgMacUnderFlow = _FpIfEgHgMacUnderFlow_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 21),
    _FpIfEgHgMacUnderFlow_Type()
)
fpIfEgHgMacUnderFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgHgMacUnderFlow.setStatus("current")
_FpIfEgTxErrPktCounter_Type = Counter64
_FpIfEgTxErrPktCounter_Object = MibTableColumn
fpIfEgTxErrPktCounter = _FpIfEgTxErrPktCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 13, 1, 22),
    _FpIfEgTxErrPktCounter_Type()
)
fpIfEgTxErrPktCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgTxErrPktCounter.setStatus("current")
_FpStatsPerIfTable_Object = MibTable
fpStatsPerIfTable = _FpStatsPerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 14)
)
if mibBuilder.loadTexts:
    fpStatsPerIfTable.setStatus("current")
_FpStatsPerIfEntry_Object = MibTableRow
fpStatsPerIfEntry = _FpStatsPerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 14, 1)
)
fpStatsPerIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fpStatsPerIfEntry.setStatus("current")
_FpIfCurrentUsagePerPort_Type = Counter32
_FpIfCurrentUsagePerPort_Object = MibTableColumn
fpIfCurrentUsagePerPort = _FpIfCurrentUsagePerPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 14, 1, 1),
    _FpIfCurrentUsagePerPort_Type()
)
fpIfCurrentUsagePerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfCurrentUsagePerPort.setStatus("current")
_FpIfDefaultPacketBuffAlloc_Type = Counter32
_FpIfDefaultPacketBuffAlloc_Object = MibTableColumn
fpIfDefaultPacketBuffAlloc = _FpIfDefaultPacketBuffAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 14, 1, 2),
    _FpIfDefaultPacketBuffAlloc_Type()
)
fpIfDefaultPacketBuffAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfDefaultPacketBuffAlloc.setStatus("current")
_FpIfMaxLimitPerPort_Type = Counter32
_FpIfMaxLimitPerPort_Object = MibTableColumn
fpIfMaxLimitPerPort = _FpIfMaxLimitPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 14, 1, 3),
    _FpIfMaxLimitPerPort_Type()
)
fpIfMaxLimitPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfMaxLimitPerPort.setStatus("current")
_FpStatsPerIfCOSTable_Object = MibTable
fpStatsPerIfCOSTable = _FpStatsPerIfCOSTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 15)
)
if mibBuilder.loadTexts:
    fpStatsPerIfCOSTable.setStatus("current")
_FpStatsPerIfCOSEntry_Object = MibTableRow
fpStatsPerIfCOSEntry = _FpStatsPerIfCOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 15, 1)
)
fpStatsPerIfCOSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "F10-FPSTATS-MIB", "fpIfPerCOSNumber"),
)
if mibBuilder.loadTexts:
    fpStatsPerIfCOSEntry.setStatus("current")


class _FpIfPerCOSNumber_Type(Integer32):
    """Custom type fpIfPerCOSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_FpIfPerCOSNumber_Type.__name__ = "Integer32"
_FpIfPerCOSNumber_Object = MibTableColumn
fpIfPerCOSNumber = _FpIfPerCOSNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 15, 1, 1),
    _FpIfPerCOSNumber_Type()
)
fpIfPerCOSNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpIfPerCOSNumber.setStatus("current")
_FpIfCurrentUsagePerCOS_Type = Counter32
_FpIfCurrentUsagePerCOS_Object = MibTableColumn
fpIfCurrentUsagePerCOS = _FpIfCurrentUsagePerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 15, 1, 2),
    _FpIfCurrentUsagePerCOS_Type()
)
fpIfCurrentUsagePerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfCurrentUsagePerCOS.setStatus("current")
_FpIfDefaultPacketBuffAllocPerCOS_Type = Counter32
_FpIfDefaultPacketBuffAllocPerCOS_Object = MibTableColumn
fpIfDefaultPacketBuffAllocPerCOS = _FpIfDefaultPacketBuffAllocPerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 15, 1, 3),
    _FpIfDefaultPacketBuffAllocPerCOS_Type()
)
fpIfDefaultPacketBuffAllocPerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfDefaultPacketBuffAllocPerCOS.setStatus("current")
_FpIfMaxLimitPerCOS_Type = Counter32
_FpIfMaxLimitPerCOS_Object = MibTableColumn
fpIfMaxLimitPerCOS = _FpIfMaxLimitPerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 15, 1, 4),
    _FpIfMaxLimitPerCOS_Type()
)
fpIfMaxLimitPerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfMaxLimitPerCOS.setStatus("current")
_FpIfHOLDropsPerCOS_Type = Counter64
_FpIfHOLDropsPerCOS_Object = MibTableColumn
fpIfHOLDropsPerCOS = _FpIfHOLDropsPerCOS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 15, 1, 5),
    _FpIfHOLDropsPerCOS_Type()
)
fpIfHOLDropsPerCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfHOLDropsPerCOS.setStatus("current")
_FpEgrQBuffSnapshotIfTable_Object = MibTable
fpEgrQBuffSnapshotIfTable = _FpEgrQBuffSnapshotIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 16)
)
if mibBuilder.loadTexts:
    fpEgrQBuffSnapshotIfTable.setStatus("current")
_FpEgrQBuffSnapshotIfEntry_Object = MibTableRow
fpEgrQBuffSnapshotIfEntry = _FpEgrQBuffSnapshotIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 16, 1)
)
fpEgrQBuffSnapshotIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "F10-FPSTATS-MIB", "fpIfPerCOSNumber"),
)
if mibBuilder.loadTexts:
    fpEgrQBuffSnapshotIfEntry.setStatus("current")
_FpIfEgrQTotBuffCells_Type = Counter32
_FpIfEgrQTotBuffCells_Object = MibTableColumn
fpIfEgrQTotBuffCells = _FpIfEgrQTotBuffCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 16, 1, 1),
    _FpIfEgrQTotBuffCells_Type()
)
fpIfEgrQTotBuffCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfEgrQTotBuffCells.setStatus("current")
_FpIngPgBuffSnapshotIfTable_Object = MibTable
fpIngPgBuffSnapshotIfTable = _FpIngPgBuffSnapshotIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 17)
)
if mibBuilder.loadTexts:
    fpIngPgBuffSnapshotIfTable.setStatus("current")
_FpIngPgBuffSnapshotIfEntry_Object = MibTableRow
fpIngPgBuffSnapshotIfEntry = _FpIngPgBuffSnapshotIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 17, 1)
)
fpIngPgBuffSnapshotIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "F10-FPSTATS-MIB", "fpIfPerPGIndex"),
)
if mibBuilder.loadTexts:
    fpIngPgBuffSnapshotIfEntry.setStatus("current")
_FpIfPerPGIndex_Type = Integer32
_FpIfPerPGIndex_Object = MibTableColumn
fpIfPerPGIndex = _FpIfPerPGIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 17, 1, 1),
    _FpIfPerPGIndex_Type()
)
fpIfPerPGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpIfPerPGIndex.setStatus("current")
_FpIfIngSharedCells_Type = Counter32
_FpIfIngSharedCells_Object = MibTableColumn
fpIfIngSharedCells = _FpIfIngSharedCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 17, 1, 2),
    _FpIfIngSharedCells_Type()
)
fpIfIngSharedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngSharedCells.setStatus("current")
_FpIfIngHeadroomCells_Type = Counter32
_FpIfIngHeadroomCells_Object = MibTableColumn
fpIfIngHeadroomCells = _FpIfIngHeadroomCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 17, 1, 3),
    _FpIfIngHeadroomCells_Type()
)
fpIfIngHeadroomCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfIngHeadroomCells.setStatus("current")
_FpStatsPerPgIfTable_Object = MibTable
fpStatsPerPgIfTable = _FpStatsPerPgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18)
)
if mibBuilder.loadTexts:
    fpStatsPerPgIfTable.setStatus("current")
_FpStatsPerPgIfEntry_Object = MibTableRow
fpStatsPerPgIfEntry = _FpStatsPerPgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1)
)
fpStatsPerPgIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "F10-FPSTATS-MIB", "fpIfPerPGIndex"),
)
if mibBuilder.loadTexts:
    fpStatsPerPgIfEntry.setStatus("current")
_FpIfStatsPgLimitMinCells_Type = Integer32
_FpIfStatsPgLimitMinCells_Object = MibTableColumn
fpIfStatsPgLimitMinCells = _FpIfStatsPgLimitMinCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1, 1),
    _FpIfStatsPgLimitMinCells_Type()
)
fpIfStatsPgLimitMinCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfStatsPgLimitMinCells.setStatus("current")
_FpIfStatsPgSharedCells_Type = Integer32
_FpIfStatsPgSharedCells_Object = MibTableColumn
fpIfStatsPgSharedCells = _FpIfStatsPgSharedCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1, 2),
    _FpIfStatsPgSharedCells_Type()
)
fpIfStatsPgSharedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfStatsPgSharedCells.setStatus("current")


class _FpIfStatsPgSharedMode_Type(Integer32):
    """Custom type fpIfStatsPgSharedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_FpIfStatsPgSharedMode_Type.__name__ = "Integer32"
_FpIfStatsPgSharedMode_Object = MibTableColumn
fpIfStatsPgSharedMode = _FpIfStatsPgSharedMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1, 3),
    _FpIfStatsPgSharedMode_Type()
)
fpIfStatsPgSharedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfStatsPgSharedMode.setStatus("current")
_FpIfStatsPgHdrmCells_Type = Integer32
_FpIfStatsPgHdrmCells_Object = MibTableColumn
fpIfStatsPgHdrmCells = _FpIfStatsPgHdrmCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1, 4),
    _FpIfStatsPgHdrmCells_Type()
)
fpIfStatsPgHdrmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfStatsPgHdrmCells.setStatus("current")
_FpIfStatsPgCounterMinCells_Type = Counter32
_FpIfStatsPgCounterMinCells_Object = MibTableColumn
fpIfStatsPgCounterMinCells = _FpIfStatsPgCounterMinCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1, 5),
    _FpIfStatsPgCounterMinCells_Type()
)
fpIfStatsPgCounterMinCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfStatsPgCounterMinCells.setStatus("current")
_FpIfStatsPgCounterSharedCells_Type = Counter32
_FpIfStatsPgCounterSharedCells_Object = MibTableColumn
fpIfStatsPgCounterSharedCells = _FpIfStatsPgCounterSharedCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1, 6),
    _FpIfStatsPgCounterSharedCells_Type()
)
fpIfStatsPgCounterSharedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfStatsPgCounterSharedCells.setStatus("current")
_FpIfStatsPgCounterHdrmCells_Type = Counter32
_FpIfStatsPgCounterHdrmCells_Object = MibTableColumn
fpIfStatsPgCounterHdrmCells = _FpIfStatsPgCounterHdrmCells_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 18, 1, 7),
    _FpIfStatsPgCounterHdrmCells_Type()
)
fpIfStatsPgCounterHdrmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIfStatsPgCounterHdrmCells.setStatus("current")
_PfcPerPrioIfTable_Object = MibTable
pfcPerPrioIfTable = _PfcPerPrioIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 19)
)
if mibBuilder.loadTexts:
    pfcPerPrioIfTable.setStatus("current")
_PfcPerPrioIfEntry_Object = MibTableRow
pfcPerPrioIfEntry = _PfcPerPrioIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 19, 1)
)
pfcPerPrioIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "F10-FPSTATS-MIB", "ifPrioIndex"),
)
if mibBuilder.loadTexts:
    pfcPerPrioIfEntry.setStatus("current")


class _IfPrioIndex_Type(Integer32):
    """Custom type ifPrioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IfPrioIndex_Type.__name__ = "Integer32"
_IfPrioIndex_Object = MibTableColumn
ifPrioIndex = _IfPrioIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 19, 1, 1),
    _IfPrioIndex_Type()
)
ifPrioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifPrioIndex.setStatus("current")
_IfPfcPerPrioRequests_Type = Counter64
_IfPfcPerPrioRequests_Object = MibTableColumn
ifPfcPerPrioRequests = _IfPfcPerPrioRequests_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 19, 1, 2),
    _IfPfcPerPrioRequests_Type()
)
ifPfcPerPrioRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPfcPerPrioRequests.setStatus("current")
if mibBuilder.loadTexts:
    ifPfcPerPrioRequests.setUnits("Requests")
_IfPfcPerPrioIndications_Type = Counter64
_IfPfcPerPrioIndications_Object = MibTableColumn
ifPfcPerPrioIndications = _IfPfcPerPrioIndications_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 19, 1, 3),
    _IfPfcPerPrioIndications_Type()
)
ifPfcPerPrioIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPfcPerPrioIndications.setStatus("current")
if mibBuilder.loadTexts:
    ifPfcPerPrioIndications.setUnits("Indications")
_FpEgrQIfCounterTable_Object = MibTable
fpEgrQIfCounterTable = _FpEgrQIfCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 20)
)
if mibBuilder.loadTexts:
    fpEgrQIfCounterTable.setStatus("current")
_FpEgrQIfCounterEntry_Object = MibTableRow
fpEgrQIfCounterEntry = _FpEgrQIfCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 20, 1)
)
fpEgrQIfCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "F10-FPSTATS-MIB", "fpEgrQComType"),
    (0, "F10-FPSTATS-MIB", "fpPerPortCOSNumber"),
)
if mibBuilder.loadTexts:
    fpEgrQIfCounterEntry.setStatus("current")
_FpEgrQComType_Type = ComType
_FpEgrQComType_Object = MibTableColumn
fpEgrQComType = _FpEgrQComType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 20, 1, 1),
    _FpEgrQComType_Type()
)
fpEgrQComType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fpEgrQComType.setStatus("current")
_FpEgrQTxPackets_Type = Counter64
_FpEgrQTxPackets_Object = MibTableColumn
fpEgrQTxPackets = _FpEgrQTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 20, 1, 2),
    _FpEgrQTxPackets_Type()
)
fpEgrQTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgrQTxPackets.setStatus("current")
_FpEgrQTxBytes_Type = Counter64
_FpEgrQTxBytes_Object = MibTableColumn
fpEgrQTxBytes = _FpEgrQTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 20, 1, 3),
    _FpEgrQTxBytes_Type()
)
fpEgrQTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgrQTxBytes.setStatus("current")
_FpEgrQDroppedPackets_Type = Counter64
_FpEgrQDroppedPackets_Object = MibTableColumn
fpEgrQDroppedPackets = _FpEgrQDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 20, 1, 4),
    _FpEgrQDroppedPackets_Type()
)
fpEgrQDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgrQDroppedPackets.setStatus("current")
_FpEgrQDroppedBytes_Type = Counter64
_FpEgrQDroppedBytes_Object = MibTableColumn
fpEgrQDroppedBytes = _FpEgrQDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 16, 1, 1, 20, 1, 5),
    _FpEgrQDroppedBytes_Type()
)
fpEgrQDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEgrQDroppedBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-FPSTATS-MIB",
    **{"ComType": ComType,
       "f10FpStatsMib": f10FpStatsMib,
       "f10FpStatsObject": f10FpStatsObject,
       "fpStatsObjects": fpStatsObjects,
       "fpCpuDataPlaneTable": fpCpuDataPlaneTable,
       "fpCpuDataPlaneStatsEntry": fpCpuDataPlaneStatsEntry,
       "fpStackUnitIndex": fpStackUnitIndex,
       "fpRxHandle": fpRxHandle,
       "fpNoMhdr": fpNoMhdr,
       "fpNoMBuf": fpNoMBuf,
       "fpNoClus": fpNoClus,
       "fpRecvd": fpRecvd,
       "fpDropped": fpDropped,
       "fpRecvToNet": fpRecvToNet,
       "fpRxError": fpRxError,
       "fpRxDatapathError": fpRxDatapathError,
       "fpRxPktCOS0": fpRxPktCOS0,
       "fpRxPktCOS1": fpRxPktCOS1,
       "fpRxPktCOS2": fpRxPktCOS2,
       "fpRxPktCOS3": fpRxPktCOS3,
       "fpRxPktCOS4": fpRxPktCOS4,
       "fpRxPktCOS5": fpRxPktCOS5,
       "fpRxPktCOS6": fpRxPktCOS6,
       "fpRxPktCOS7": fpRxPktCOS7,
       "fpRxPktUnit0": fpRxPktUnit0,
       "fpRxPktUnit1": fpRxPktUnit1,
       "fpRxPktUnit2": fpRxPktUnit2,
       "fpRxPktUnit3": fpRxPktUnit3,
       "fpTransmitted": fpTransmitted,
       "fpTxRequested": fpTxRequested,
       "fpNoTxDesc": fpNoTxDesc,
       "fpTxError": fpTxError,
       "fpTxReqTooLarge": fpTxReqTooLarge,
       "fpTxInternalError": fpTxInternalError,
       "fpTxDatapathErr": fpTxDatapathErr,
       "fpTxPktCOS0": fpTxPktCOS0,
       "fpTxPktCOS1": fpTxPktCOS1,
       "fpTxPktCOS2": fpTxPktCOS2,
       "fpTxPktCOS3": fpTxPktCOS3,
       "fpTxPktCOS4": fpTxPktCOS4,
       "fpTxPktCOS5": fpTxPktCOS5,
       "fpTxPktCOS6": fpTxPktCOS6,
       "fpTxPktCOS7": fpTxPktCOS7,
       "fpTxPktUnit0": fpTxPktUnit0,
       "fpTxPktUnit1": fpTxPktUnit1,
       "fpTxPktUnit2": fpTxPktUnit2,
       "fpTxPktUnit3": fpTxPktUnit3,
       "fpCpuPartyBusTable": fpCpuPartyBusTable,
       "fpCpuPartyBusStatsEntry": fpCpuPartyBusStatsEntry,
       "fpPartyBusInputPackets": fpPartyBusInputPackets,
       "fpPartyBusInputBytes": fpPartyBusInputBytes,
       "fpPartyBusInputDropped": fpPartyBusInputDropped,
       "fpPartyBusInputError": fpPartyBusInputError,
       "fpPartyBusOutputPackets": fpPartyBusOutputPackets,
       "fpPartyBusOutputBytes": fpPartyBusOutputBytes,
       "fpPartyBusOutputError": fpPartyBusOutputError,
       "fpDropsTable": fpDropsTable,
       "fpDropsEntry": fpDropsEntry,
       "fpStackPortIndex": fpStackPortIndex,
       "fpIngressDrops": fpIngressDrops,
       "fpIngIBPCBPFullDrops": fpIngIBPCBPFullDrops,
       "fpIngPortSTPnotFwdDrops": fpIngPortSTPnotFwdDrops,
       "fpIngIPv4L3Discards": fpIngIPv4L3Discards,
       "fpIngPolicyDiscards": fpIngPolicyDiscards,
       "fpIngPacketsDroppedByFP": fpIngPacketsDroppedByFP,
       "fpIngL2L3Drops": fpIngL2L3Drops,
       "fpIngPortBitMapZeroDrops": fpIngPortBitMapZeroDrops,
       "fpIngRxVLANDrops": fpIngRxVLANDrops,
       "fpIngressFCSDrops": fpIngressFCSDrops,
       "fpIngressMTUExceeds": fpIngressMTUExceeds,
       "fpMMUHOLDrops": fpMMUHOLDrops,
       "fpMMUTxPurgeCellErr": fpMMUTxPurgeCellErr,
       "fpMMUAgedDrops": fpMMUAgedDrops,
       "fpEgressFCSDrops": fpEgressFCSDrops,
       "fpEgIPv4L3UCAgedDrops": fpEgIPv4L3UCAgedDrops,
       "fpEgTTLThresholdDrops": fpEgTTLThresholdDrops,
       "fpEgInvalidVLANCounterDrops": fpEgInvalidVLANCounterDrops,
       "fpEgL2MCDrops": fpEgL2MCDrops,
       "fpEgPktDropsOfAnyCondition": fpEgPktDropsOfAnyCondition,
       "fpEgHgMacUnderFlow": fpEgHgMacUnderFlow,
       "fpEgTxErrPktCounter": fpEgTxErrPktCounter,
       "fpFlowControlDrops": fpFlowControlDrops,
       "fpPacketBufferTable": fpPacketBufferTable,
       "fpPacketBufferEntry": fpPacketBufferEntry,
       "fpPortPipe": fpPortPipe,
       "fpTotalPacketBuffer": fpTotalPacketBuffer,
       "fpCurrentAvailBuffer": fpCurrentAvailBuffer,
       "fpPacketBufferAlloc": fpPacketBufferAlloc,
       "fpStatsPerPortTable": fpStatsPerPortTable,
       "fpStatsPerPortEntry": fpStatsPerPortEntry,
       "fpCurrentUsagePerPort": fpCurrentUsagePerPort,
       "fpDefaultPacketBuffAlloc": fpDefaultPacketBuffAlloc,
       "fpMaxLimitPerPort": fpMaxLimitPerPort,
       "fpStatsPerCOSTable": fpStatsPerCOSTable,
       "fpStatsPerCOSEntry": fpStatsPerCOSEntry,
       "fpPerPortCOSNumber": fpPerPortCOSNumber,
       "fpCurrentUsagePerCOS": fpCurrentUsagePerCOS,
       "fpDefaultPacketBuffAllocPerCOS": fpDefaultPacketBuffAllocPerCOS,
       "fpMaxLimitPerCOS": fpMaxLimitPerCOS,
       "fpHOLDropsPerCOS": fpHOLDropsPerCOS,
       "fpCpuDataPlaneCOSTable": fpCpuDataPlaneCOSTable,
       "fpCpuDataPlaneCOSEntry": fpCpuDataPlaneCOSEntry,
       "fpCOSIndex": fpCOSIndex,
       "fpRxPktCOS": fpRxPktCOS,
       "fpTxPktCOS": fpTxPktCOS,
       "fpEgrQBuffSnapshotTable": fpEgrQBuffSnapshotTable,
       "fpEgrQBuffSnapshotEntry": fpEgrQBuffSnapshotEntry,
       "fpEgrQTotBuffCells": fpEgrQTotBuffCells,
       "fpIngPgBuffSnapshotTable": fpIngPgBuffSnapshotTable,
       "fpIngPgBuffSnapshotEntry": fpIngPgBuffSnapshotEntry,
       "fpPerPortPGIndex": fpPerPortPGIndex,
       "fpIngSharedCells": fpIngSharedCells,
       "fpIngHeadroomCells": fpIngHeadroomCells,
       "fpStatsPerPgTable": fpStatsPerPgTable,
       "fpStatsPerPgEntry": fpStatsPerPgEntry,
       "fpStatsPgLimitMinCells": fpStatsPgLimitMinCells,
       "fpStatsPgSharedCells": fpStatsPgSharedCells,
       "fpStatsPgSharedMode": fpStatsPgSharedMode,
       "fpStatsPgHdrmCells": fpStatsPgHdrmCells,
       "fpStatsPgCounterMinCells": fpStatsPgCounterMinCells,
       "fpStatsPgCounterSharedCells": fpStatsPgCounterSharedCells,
       "fpStatsPgCounterHdrmCells": fpStatsPgCounterHdrmCells,
       "pfcPerPrioTable": pfcPerPrioTable,
       "pfcPerPrioEntry": pfcPerPrioEntry,
       "prioIndex": prioIndex,
       "pfcPerPrioRequests": pfcPerPrioRequests,
       "pfcPerPrioIndications": pfcPerPrioIndications,
       "fpCpuPartyBusPortStatsTable": fpCpuPartyBusPortStatsTable,
       "fpCpuPartyBusPortStatsEntry": fpCpuPartyBusPortStatsEntry,
       "fpCpuPartyBusPortStatsOutOctets": fpCpuPartyBusPortStatsOutOctets,
       "fpCpuPartyBusPortStatsOutDropPkts": fpCpuPartyBusPortStatsOutDropPkts,
       "fpCpuPartyBusPortStatsOutCOS0Pkts": fpCpuPartyBusPortStatsOutCOS0Pkts,
       "fpCpuPartyBusPortStatsOutCOS1Pkts": fpCpuPartyBusPortStatsOutCOS1Pkts,
       "fpCpuPartyBusPortStatsOutCOS2Pkts": fpCpuPartyBusPortStatsOutCOS2Pkts,
       "fpCpuPartyBusPortStatsOutCOS3Pkts": fpCpuPartyBusPortStatsOutCOS3Pkts,
       "fpCpuPartyBusPortStatsOutCOS4Pkts": fpCpuPartyBusPortStatsOutCOS4Pkts,
       "fpCpuPartyBusPortStatsOutCOS5Pkts": fpCpuPartyBusPortStatsOutCOS5Pkts,
       "fpCpuPartyBusPortStatsOutUnicastPkts": fpCpuPartyBusPortStatsOutUnicastPkts,
       "fpCpuPartyBusPortStatsOutMulticastPkts": fpCpuPartyBusPortStatsOutMulticastPkts,
       "fpCpuPartyBusPortStatsOutBroadcastPkts": fpCpuPartyBusPortStatsOutBroadcastPkts,
       "fpCpuPartyBusPortStatsOutPausePkts": fpCpuPartyBusPortStatsOutPausePkts,
       "fpCpuPartyBusPortStatsOutCollisions": fpCpuPartyBusPortStatsOutCollisions,
       "fpCpuPartyBusPortStatsOutSingleCollisions": fpCpuPartyBusPortStatsOutSingleCollisions,
       "fpCpuPartyBusPortStatsOutMultiCollisions": fpCpuPartyBusPortStatsOutMultiCollisions,
       "fpCpuPartyBusPortStatsOutLateCollisions": fpCpuPartyBusPortStatsOutLateCollisions,
       "fpCpuPartyBusPortStatsOutExcessCollisions": fpCpuPartyBusPortStatsOutExcessCollisions,
       "fpCpuPartyBusPortStatsOutDeferred": fpCpuPartyBusPortStatsOutDeferred,
       "fpCpuPartyBusPortStatsOutDiscarded": fpCpuPartyBusPortStatsOutDiscarded,
       "fpCpuPartyBusPortStatsInOctets": fpCpuPartyBusPortStatsInOctets,
       "fpCpuPartyBusPortStatsInUndersizePkts": fpCpuPartyBusPortStatsInUndersizePkts,
       "fpCpuPartyBusPortStatsInOversizePkts": fpCpuPartyBusPortStatsInOversizePkts,
       "fpCpuPartyBusPortStatsInPausePkts": fpCpuPartyBusPortStatsInPausePkts,
       "fpCpuPartyBusPortStatsIn64OctetPkts": fpCpuPartyBusPortStatsIn64OctetPkts,
       "fpCpuPartyBusPortStatsIn65To127OctetPkts": fpCpuPartyBusPortStatsIn65To127OctetPkts,
       "fpCpuPartyBusPortStatsIn128To255OctetPkts": fpCpuPartyBusPortStatsIn128To255OctetPkts,
       "fpCpuPartyBusPortStatsIn256To511OctetPkts": fpCpuPartyBusPortStatsIn256To511OctetPkts,
       "fpCpuPartyBusPortStatsIn512To1023OctetPkts": fpCpuPartyBusPortStatsIn512To1023OctetPkts,
       "fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts": fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts,
       "fpCpuPartyBusPortStatsInJabbers": fpCpuPartyBusPortStatsInJabbers,
       "fpCpuPartyBusPortStatsInAlignErrors": fpCpuPartyBusPortStatsInAlignErrors,
       "fpCpuPartyBusPortStatsInFcsErrors": fpCpuPartyBusPortStatsInFcsErrors,
       "fpCpuPartyBusPortStatsInGoodOctets": fpCpuPartyBusPortStatsInGoodOctets,
       "fpCpuPartyBusPortStatsInDropPkts": fpCpuPartyBusPortStatsInDropPkts,
       "fpCpuPartyBusPortStatsInUnicastPkts": fpCpuPartyBusPortStatsInUnicastPkts,
       "fpCpuPartyBusPortStatsInMulticastPkts": fpCpuPartyBusPortStatsInMulticastPkts,
       "fpCpuPartyBusPortStatsInBroadcastPkts": fpCpuPartyBusPortStatsInBroadcastPkts,
       "fpCpuPartyBusPortStatsInSrcAddrChanges": fpCpuPartyBusPortStatsInSrcAddrChanges,
       "fpCpuPartyBusPortStatsInFragments": fpCpuPartyBusPortStatsInFragments,
       "fpCpuPartyBusPortStatsInJumboPkts": fpCpuPartyBusPortStatsInJumboPkts,
       "fpCpuPartyBusPortStatsInSymbolErrors": fpCpuPartyBusPortStatsInSymbolErrors,
       "fpCpuPartyBusPortStatsInInRangeErrors": fpCpuPartyBusPortStatsInInRangeErrors,
       "fpCpuPartyBusPortStatsInOutRangeErrors": fpCpuPartyBusPortStatsInOutRangeErrors,
       "fpDropsIfTable": fpDropsIfTable,
       "fpDropsIfEntry": fpDropsIfEntry,
       "fpIfIngressDrops": fpIfIngressDrops,
       "fpIfIngIBPCBPFullDrops": fpIfIngIBPCBPFullDrops,
       "fpIfIngPortSTPnotFwdDrops": fpIfIngPortSTPnotFwdDrops,
       "fpIfIngIPv4L3Discards": fpIfIngIPv4L3Discards,
       "fpIfIngPolicyDiscards": fpIfIngPolicyDiscards,
       "fpIfIngPacketsDroppedByFP": fpIfIngPacketsDroppedByFP,
       "fpIfIngL2L3Drops": fpIfIngL2L3Drops,
       "fpIfIngPortBitMapZeroDrops": fpIfIngPortBitMapZeroDrops,
       "fpIfIngRxVLANDrops": fpIfIngRxVLANDrops,
       "fpIfIngressFCSDrops": fpIfIngressFCSDrops,
       "fpIfIngressMTUExceeds": fpIfIngressMTUExceeds,
       "fpIfMMUHOLDrops": fpIfMMUHOLDrops,
       "fpIfMMUTxPurgeCellErr": fpIfMMUTxPurgeCellErr,
       "fpIfMMUAgedDrops": fpIfMMUAgedDrops,
       "fpIfEgressFCSDrops": fpIfEgressFCSDrops,
       "fpIfEgIPv4L3UCAgedDrops": fpIfEgIPv4L3UCAgedDrops,
       "fpIfEgTTLThresholdDrops": fpIfEgTTLThresholdDrops,
       "fpIfEgInvalidVLANCounterDrops": fpIfEgInvalidVLANCounterDrops,
       "fpIfEgL2MCDrops": fpIfEgL2MCDrops,
       "fpIfEgPktDropsOfAnyCondition": fpIfEgPktDropsOfAnyCondition,
       "fpIfEgHgMacUnderFlow": fpIfEgHgMacUnderFlow,
       "fpIfEgTxErrPktCounter": fpIfEgTxErrPktCounter,
       "fpStatsPerIfTable": fpStatsPerIfTable,
       "fpStatsPerIfEntry": fpStatsPerIfEntry,
       "fpIfCurrentUsagePerPort": fpIfCurrentUsagePerPort,
       "fpIfDefaultPacketBuffAlloc": fpIfDefaultPacketBuffAlloc,
       "fpIfMaxLimitPerPort": fpIfMaxLimitPerPort,
       "fpStatsPerIfCOSTable": fpStatsPerIfCOSTable,
       "fpStatsPerIfCOSEntry": fpStatsPerIfCOSEntry,
       "fpIfPerCOSNumber": fpIfPerCOSNumber,
       "fpIfCurrentUsagePerCOS": fpIfCurrentUsagePerCOS,
       "fpIfDefaultPacketBuffAllocPerCOS": fpIfDefaultPacketBuffAllocPerCOS,
       "fpIfMaxLimitPerCOS": fpIfMaxLimitPerCOS,
       "fpIfHOLDropsPerCOS": fpIfHOLDropsPerCOS,
       "fpEgrQBuffSnapshotIfTable": fpEgrQBuffSnapshotIfTable,
       "fpEgrQBuffSnapshotIfEntry": fpEgrQBuffSnapshotIfEntry,
       "fpIfEgrQTotBuffCells": fpIfEgrQTotBuffCells,
       "fpIngPgBuffSnapshotIfTable": fpIngPgBuffSnapshotIfTable,
       "fpIngPgBuffSnapshotIfEntry": fpIngPgBuffSnapshotIfEntry,
       "fpIfPerPGIndex": fpIfPerPGIndex,
       "fpIfIngSharedCells": fpIfIngSharedCells,
       "fpIfIngHeadroomCells": fpIfIngHeadroomCells,
       "fpStatsPerPgIfTable": fpStatsPerPgIfTable,
       "fpStatsPerPgIfEntry": fpStatsPerPgIfEntry,
       "fpIfStatsPgLimitMinCells": fpIfStatsPgLimitMinCells,
       "fpIfStatsPgSharedCells": fpIfStatsPgSharedCells,
       "fpIfStatsPgSharedMode": fpIfStatsPgSharedMode,
       "fpIfStatsPgHdrmCells": fpIfStatsPgHdrmCells,
       "fpIfStatsPgCounterMinCells": fpIfStatsPgCounterMinCells,
       "fpIfStatsPgCounterSharedCells": fpIfStatsPgCounterSharedCells,
       "fpIfStatsPgCounterHdrmCells": fpIfStatsPgCounterHdrmCells,
       "pfcPerPrioIfTable": pfcPerPrioIfTable,
       "pfcPerPrioIfEntry": pfcPerPrioIfEntry,
       "ifPrioIndex": ifPrioIndex,
       "ifPfcPerPrioRequests": ifPfcPerPrioRequests,
       "ifPfcPerPrioIndications": ifPfcPerPrioIndications,
       "fpEgrQIfCounterTable": fpEgrQIfCounterTable,
       "fpEgrQIfCounterEntry": fpEgrQIfCounterEntry,
       "fpEgrQComType": fpEgrQComType,
       "fpEgrQTxPackets": fpEgrQTxPackets,
       "fpEgrQTxBytes": fpEgrQTxBytes,
       "fpEgrQDroppedPackets": fpEgrQDroppedPackets,
       "fpEgrQDroppedBytes": fpEgrQDroppedBytes}
)
