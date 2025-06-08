# SNMP MIB module (CIE1000-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-PORT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000DisplayString,
 CIE1000InterfaceIndex,
 CIE1000PortStatusSpeed,
 CIE1000SfpTransceiver,
 CIE1000Unsigned8) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InterfaceIndex",
    "CIE1000PortStatusSpeed",
    "CIE1000SfpTransceiver",
    "CIE1000Unsigned8")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000PortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11)
)
if mibBuilder.loadTexts:
    cie1000PortMib.setRevisions(
        ("2015-07-07 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000PortFc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class CIE1000PortMedia(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rj45", 0),
          ("sfp", 1),
          ("dual", 2))
    )



class CIE1000PortPhyVeriPhyStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("correctlyTerminatedPair", 0),
          ("openPair", 1),
          ("shortPair", 2),
          ("abnormalTermination", 4),
          ("crossPairShortToPairA", 8),
          ("crossPairShortToPairB", 9),
          ("crossPairShortToPairC", 10),
          ("crossPairShortToPairD", 11),
          ("abnormalCrossPairCouplingToPairA", 12),
          ("abnormalCrossPairCouplingToPairB", 13),
          ("abnormalCrossPairCouplingToPairC", 14),
          ("abnormalCrossPairCouplingToPairD", 15),
          ("unknownResult", 16),
          ("veriPhyRunning", 17))
    )



class CIE1000PortSpeed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("force10ModeFdx", 0),
          ("force10ModeHdx", 1),
          ("force100ModeFdx", 2),
          ("force100ModeHdx", 3),
          ("force1GModeFdx", 4),
          ("autoNegMode", 5),
          ("force2G5ModeFdx", 6),
          ("force5GModeFdx", 7),
          ("force10GModeFdx", 8),
          ("force12GModeFdx", 9))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000PortMibObjects_ObjectIdentity = ObjectIdentity
cie1000PortMibObjects = _Cie1000PortMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1)
)
_Cie1000PortConfig_ObjectIdentity = ObjectIdentity
cie1000PortConfig = _Cie1000PortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2)
)
_Cie1000PortConfigTable_Object = MibTable
cie1000PortConfigTable = _Cie1000PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000PortConfigTable.setStatus("current")
_Cie1000PortConfigEntry_Object = MibTableRow
cie1000PortConfigEntry = _Cie1000PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1)
)
cie1000PortConfigEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortConfigEntry.setStatus("current")
_Cie1000PortConfigIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortConfigIfIndex_Object = MibTableColumn
cie1000PortConfigIfIndex = _Cie1000PortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 1),
    _Cie1000PortConfigIfIndex_Type()
)
cie1000PortConfigIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortConfigIfIndex.setStatus("current")
_Cie1000PortConfigShutdown_Type = TruthValue
_Cie1000PortConfigShutdown_Object = MibTableColumn
cie1000PortConfigShutdown = _Cie1000PortConfigShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 2),
    _Cie1000PortConfigShutdown_Type()
)
cie1000PortConfigShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigShutdown.setStatus("current")
_Cie1000PortConfigSpeed_Type = CIE1000PortSpeed
_Cie1000PortConfigSpeed_Object = MibTableColumn
cie1000PortConfigSpeed = _Cie1000PortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 3),
    _Cie1000PortConfigSpeed_Type()
)
cie1000PortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigSpeed.setStatus("current")
_Cie1000PortConfigAdvertiseDisabled_Type = CIE1000Unsigned8
_Cie1000PortConfigAdvertiseDisabled_Object = MibTableColumn
cie1000PortConfigAdvertiseDisabled = _Cie1000PortConfigAdvertiseDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 4),
    _Cie1000PortConfigAdvertiseDisabled_Type()
)
cie1000PortConfigAdvertiseDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigAdvertiseDisabled.setStatus("current")
_Cie1000PortConfigMediaType_Type = CIE1000PortMedia
_Cie1000PortConfigMediaType_Object = MibTableColumn
cie1000PortConfigMediaType = _Cie1000PortConfigMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 5),
    _Cie1000PortConfigMediaType_Type()
)
cie1000PortConfigMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigMediaType.setStatus("current")
_Cie1000PortConfigFC_Type = CIE1000PortFc
_Cie1000PortConfigFC_Object = MibTableColumn
cie1000PortConfigFC = _Cie1000PortConfigFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 6),
    _Cie1000PortConfigFC_Type()
)
cie1000PortConfigFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigFC.setStatus("current")
_Cie1000PortConfigMTU_Type = Unsigned32
_Cie1000PortConfigMTU_Object = MibTableColumn
cie1000PortConfigMTU = _Cie1000PortConfigMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 7),
    _Cie1000PortConfigMTU_Type()
)
cie1000PortConfigMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigMTU.setStatus("current")
_Cie1000PortConfigExcessiveRestart_Type = TruthValue
_Cie1000PortConfigExcessiveRestart_Object = MibTableColumn
cie1000PortConfigExcessiveRestart = _Cie1000PortConfigExcessiveRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 8),
    _Cie1000PortConfigExcessiveRestart_Type()
)
cie1000PortConfigExcessiveRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigExcessiveRestart.setStatus("current")
_Cie1000PortConfigPFC_Type = CIE1000Unsigned8
_Cie1000PortConfigPFC_Object = MibTableColumn
cie1000PortConfigPFC = _Cie1000PortConfigPFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 9),
    _Cie1000PortConfigPFC_Type()
)
cie1000PortConfigPFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigPFC.setStatus("current")
_Cie1000PortConfigFrameLengthCheck_Type = TruthValue
_Cie1000PortConfigFrameLengthCheck_Object = MibTableColumn
cie1000PortConfigFrameLengthCheck = _Cie1000PortConfigFrameLengthCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 2, 1, 1, 10),
    _Cie1000PortConfigFrameLengthCheck_Type()
)
cie1000PortConfigFrameLengthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortConfigFrameLengthCheck.setStatus("current")
_Cie1000PortStatus_ObjectIdentity = ObjectIdentity
cie1000PortStatus = _Cie1000PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3)
)
_Cie1000PortStatusInformationTable_Object = MibTable
cie1000PortStatusInformationTable = _Cie1000PortStatusInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000PortStatusInformationTable.setStatus("current")
_Cie1000PortStatusInformationEntry_Object = MibTableRow
cie1000PortStatusInformationEntry = _Cie1000PortStatusInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1)
)
cie1000PortStatusInformationEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortStatusInformationIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortStatusInformationEntry.setStatus("current")
_Cie1000PortStatusInformationIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortStatusInformationIfIndex_Object = MibTableColumn
cie1000PortStatusInformationIfIndex = _Cie1000PortStatusInformationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 1),
    _Cie1000PortStatusInformationIfIndex_Type()
)
cie1000PortStatusInformationIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationIfIndex.setStatus("current")
_Cie1000PortStatusInformationLink_Type = TruthValue
_Cie1000PortStatusInformationLink_Object = MibTableColumn
cie1000PortStatusInformationLink = _Cie1000PortStatusInformationLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 2),
    _Cie1000PortStatusInformationLink_Type()
)
cie1000PortStatusInformationLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationLink.setStatus("current")
_Cie1000PortStatusInformationFdx_Type = TruthValue
_Cie1000PortStatusInformationFdx_Object = MibTableColumn
cie1000PortStatusInformationFdx = _Cie1000PortStatusInformationFdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 3),
    _Cie1000PortStatusInformationFdx_Type()
)
cie1000PortStatusInformationFdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationFdx.setStatus("current")
_Cie1000PortStatusInformationFiber_Type = TruthValue
_Cie1000PortStatusInformationFiber_Object = MibTableColumn
cie1000PortStatusInformationFiber = _Cie1000PortStatusInformationFiber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 4),
    _Cie1000PortStatusInformationFiber_Type()
)
cie1000PortStatusInformationFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationFiber.setStatus("current")
_Cie1000PortStatusInformationSpeed_Type = CIE1000PortStatusSpeed
_Cie1000PortStatusInformationSpeed_Object = MibTableColumn
cie1000PortStatusInformationSpeed = _Cie1000PortStatusInformationSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 5),
    _Cie1000PortStatusInformationSpeed_Type()
)
cie1000PortStatusInformationSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationSpeed.setStatus("current")
_Cie1000PortStatusInformationSFPType_Type = CIE1000SfpTransceiver
_Cie1000PortStatusInformationSFPType_Object = MibTableColumn
cie1000PortStatusInformationSFPType = _Cie1000PortStatusInformationSFPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 6),
    _Cie1000PortStatusInformationSFPType_Type()
)
cie1000PortStatusInformationSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationSFPType.setStatus("current")


class _Cie1000PortStatusInformationSFPVendorName_Type(CIE1000DisplayString):
    """Custom type cie1000PortStatusInformationSFPVendorName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Cie1000PortStatusInformationSFPVendorName_Type.__name__ = "CIE1000DisplayString"
_Cie1000PortStatusInformationSFPVendorName_Object = MibTableColumn
cie1000PortStatusInformationSFPVendorName = _Cie1000PortStatusInformationSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 7),
    _Cie1000PortStatusInformationSFPVendorName_Type()
)
cie1000PortStatusInformationSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationSFPVendorName.setStatus("current")


class _Cie1000PortStatusInformationSFPVendorPN_Type(CIE1000DisplayString):
    """Custom type cie1000PortStatusInformationSFPVendorPN based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Cie1000PortStatusInformationSFPVendorPN_Type.__name__ = "CIE1000DisplayString"
_Cie1000PortStatusInformationSFPVendorPN_Object = MibTableColumn
cie1000PortStatusInformationSFPVendorPN = _Cie1000PortStatusInformationSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 8),
    _Cie1000PortStatusInformationSFPVendorPN_Type()
)
cie1000PortStatusInformationSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationSFPVendorPN.setStatus("current")


class _Cie1000PortStatusInformationSFPVendorRev_Type(CIE1000DisplayString):
    """Custom type cie1000PortStatusInformationSFPVendorRev based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Cie1000PortStatusInformationSFPVendorRev_Type.__name__ = "CIE1000DisplayString"
_Cie1000PortStatusInformationSFPVendorRev_Object = MibTableColumn
cie1000PortStatusInformationSFPVendorRev = _Cie1000PortStatusInformationSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 9),
    _Cie1000PortStatusInformationSFPVendorRev_Type()
)
cie1000PortStatusInformationSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationSFPVendorRev.setStatus("current")


class _Cie1000PortStatusInformationSFPVendorSN_Type(CIE1000DisplayString):
    """Custom type cie1000PortStatusInformationSFPVendorSN based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Cie1000PortStatusInformationSFPVendorSN_Type.__name__ = "CIE1000DisplayString"
_Cie1000PortStatusInformationSFPVendorSN_Object = MibTableColumn
cie1000PortStatusInformationSFPVendorSN = _Cie1000PortStatusInformationSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 10),
    _Cie1000PortStatusInformationSFPVendorSN_Type()
)
cie1000PortStatusInformationSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationSFPVendorSN.setStatus("current")
_Cie1000PortStatusInformationRxUtilization_Type = Unsigned32
_Cie1000PortStatusInformationRxUtilization_Object = MibTableColumn
cie1000PortStatusInformationRxUtilization = _Cie1000PortStatusInformationRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 11),
    _Cie1000PortStatusInformationRxUtilization_Type()
)
cie1000PortStatusInformationRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationRxUtilization.setStatus("current")
_Cie1000PortStatusInformationTxUtilization_Type = Unsigned32
_Cie1000PortStatusInformationTxUtilization_Object = MibTableColumn
cie1000PortStatusInformationTxUtilization = _Cie1000PortStatusInformationTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 12),
    _Cie1000PortStatusInformationTxUtilization_Type()
)
cie1000PortStatusInformationTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationTxUtilization.setStatus("current")
_Cie1000PortStatusInformationRxErrorUtilization_Type = Unsigned32
_Cie1000PortStatusInformationRxErrorUtilization_Object = MibTableColumn
cie1000PortStatusInformationRxErrorUtilization = _Cie1000PortStatusInformationRxErrorUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 13),
    _Cie1000PortStatusInformationRxErrorUtilization_Type()
)
cie1000PortStatusInformationRxErrorUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationRxErrorUtilization.setStatus("current")
_Cie1000PortStatusInformationTxErrorUtilization_Type = Unsigned32
_Cie1000PortStatusInformationTxErrorUtilization_Object = MibTableColumn
cie1000PortStatusInformationTxErrorUtilization = _Cie1000PortStatusInformationTxErrorUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 1, 1, 14),
    _Cie1000PortStatusInformationTxErrorUtilization_Type()
)
cie1000PortStatusInformationTxErrorUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusInformationTxErrorUtilization.setStatus("current")
_Cie1000PortStatusVeriPhyResult_ObjectIdentity = ObjectIdentity
cie1000PortStatusVeriPhyResult = _Cie1000PortStatusVeriPhyResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3)
)
_Cie1000PortStatusVeriPhyResultTable_Object = MibTable
cie1000PortStatusVeriPhyResultTable = _Cie1000PortStatusVeriPhyResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultTable.setStatus("current")
_Cie1000PortStatusVeriPhyResultEntry_Object = MibTableRow
cie1000PortStatusVeriPhyResultEntry = _Cie1000PortStatusVeriPhyResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1)
)
cie1000PortStatusVeriPhyResultEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultEntry.setStatus("current")
_Cie1000PortStatusVeriPhyResultIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortStatusVeriPhyResultIfIndex_Object = MibTableColumn
cie1000PortStatusVeriPhyResultIfIndex = _Cie1000PortStatusVeriPhyResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 1),
    _Cie1000PortStatusVeriPhyResultIfIndex_Type()
)
cie1000PortStatusVeriPhyResultIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultIfIndex.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairA_Type = CIE1000PortPhyVeriPhyStatus
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairA_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyStatusPairA = _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 2),
    _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairA_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyStatusPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyStatusPairA.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairB_Type = CIE1000PortPhyVeriPhyStatus
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairB_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyStatusPairB = _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 3),
    _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairB_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyStatusPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyStatusPairB.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairC_Type = CIE1000PortPhyVeriPhyStatus
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairC_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyStatusPairC = _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 4),
    _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairC_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyStatusPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyStatusPairC.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairD_Type = CIE1000PortPhyVeriPhyStatus
_Cie1000PortStatusVeriPhyResultVeriPhyStatusPairD_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyStatusPairD = _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 5),
    _Cie1000PortStatusVeriPhyResultVeriPhyStatusPairD_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyStatusPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyStatusPairD.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA_Type = CIE1000Unsigned8
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA = _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 6),
    _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB_Type = CIE1000Unsigned8
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB = _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 7),
    _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC_Type = CIE1000Unsigned8
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC = _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 8),
    _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC.setStatus("current")
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD_Type = CIE1000Unsigned8
_Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD_Object = MibTableColumn
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD = _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 3, 3, 1, 1, 9),
    _Cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD_Type()
)
cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD.setStatus("current")
_Cie1000PortControl_ObjectIdentity = ObjectIdentity
cie1000PortControl = _Cie1000PortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4)
)
_Cie1000PortControlStatisticsClear_ObjectIdentity = ObjectIdentity
cie1000PortControlStatisticsClear = _Cie1000PortControlStatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 1)
)
_Cie1000PortControlStatisticsClearTable_Object = MibTable
cie1000PortControlStatisticsClearTable = _Cie1000PortControlStatisticsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cie1000PortControlStatisticsClearTable.setStatus("current")
_Cie1000PortControlStatisticsClearEntry_Object = MibTableRow
cie1000PortControlStatisticsClearEntry = _Cie1000PortControlStatisticsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 1, 1, 1)
)
cie1000PortControlStatisticsClearEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortControlStatisticsClearIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortControlStatisticsClearEntry.setStatus("current")
_Cie1000PortControlStatisticsClearIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortControlStatisticsClearIfIndex_Object = MibTableColumn
cie1000PortControlStatisticsClearIfIndex = _Cie1000PortControlStatisticsClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 1, 1, 1, 1),
    _Cie1000PortControlStatisticsClearIfIndex_Type()
)
cie1000PortControlStatisticsClearIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortControlStatisticsClearIfIndex.setStatus("current")
_Cie1000PortControlStatisticsClearStatisticsClear_Type = TruthValue
_Cie1000PortControlStatisticsClearStatisticsClear_Object = MibTableColumn
cie1000PortControlStatisticsClearStatisticsClear = _Cie1000PortControlStatisticsClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 1, 1, 1, 2),
    _Cie1000PortControlStatisticsClearStatisticsClear_Type()
)
cie1000PortControlStatisticsClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortControlStatisticsClearStatisticsClear.setStatus("current")
_Cie1000PortControlVeriPhyStart_ObjectIdentity = ObjectIdentity
cie1000PortControlVeriPhyStart = _Cie1000PortControlVeriPhyStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 2)
)
_Cie1000PortControlVeriPhyStartTable_Object = MibTable
cie1000PortControlVeriPhyStartTable = _Cie1000PortControlVeriPhyStartTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000PortControlVeriPhyStartTable.setStatus("current")
_Cie1000PortControlVeriPhyStartEntry_Object = MibTableRow
cie1000PortControlVeriPhyStartEntry = _Cie1000PortControlVeriPhyStartEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 2, 1, 1)
)
cie1000PortControlVeriPhyStartEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortControlVeriPhyStartIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortControlVeriPhyStartEntry.setStatus("current")
_Cie1000PortControlVeriPhyStartIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortControlVeriPhyStartIfIndex_Object = MibTableColumn
cie1000PortControlVeriPhyStartIfIndex = _Cie1000PortControlVeriPhyStartIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 2, 1, 1, 1),
    _Cie1000PortControlVeriPhyStartIfIndex_Type()
)
cie1000PortControlVeriPhyStartIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortControlVeriPhyStartIfIndex.setStatus("current")
_Cie1000PortControlVeriPhyStartStart_Type = TruthValue
_Cie1000PortControlVeriPhyStartStart_Object = MibTableColumn
cie1000PortControlVeriPhyStartStart = _Cie1000PortControlVeriPhyStartStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 4, 2, 1, 1, 2),
    _Cie1000PortControlVeriPhyStartStart_Type()
)
cie1000PortControlVeriPhyStartStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortControlVeriPhyStartStart.setStatus("current")
_Cie1000PortStatistics_ObjectIdentity = ObjectIdentity
cie1000PortStatistics = _Cie1000PortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5)
)
_Cie1000PortStatisticsRmonStatisticsTable_Object = MibTable
cie1000PortStatisticsRmonStatisticsTable = _Cie1000PortStatisticsRmonStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTable.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsEntry_Object = MibTableRow
cie1000PortStatisticsRmonStatisticsEntry = _Cie1000PortStatisticsRmonStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1)
)
cie1000PortStatisticsRmonStatisticsEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsEntry.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortStatisticsRmonStatisticsIfIndex_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsIfIndex = _Cie1000PortStatisticsRmonStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 1),
    _Cie1000PortStatisticsRmonStatisticsIfIndex_Type()
)
cie1000PortStatisticsRmonStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsIfIndex.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxDropEvents_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxDropEvents_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxDropEvents = _Cie1000PortStatisticsRmonStatisticsRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 2),
    _Cie1000PortStatisticsRmonStatisticsRxDropEvents_Type()
)
cie1000PortStatisticsRmonStatisticsRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxDropEvents.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxOctets_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxOctets_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxOctets = _Cie1000PortStatisticsRmonStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 3),
    _Cie1000PortStatisticsRmonStatisticsRxOctets_Type()
)
cie1000PortStatisticsRmonStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxOctets.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxPkts = _Cie1000PortStatisticsRmonStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 4),
    _Cie1000PortStatisticsRmonStatisticsRxPkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxBroadcastPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxBroadcastPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxBroadcastPkts = _Cie1000PortStatisticsRmonStatisticsRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 5),
    _Cie1000PortStatisticsRmonStatisticsRxBroadcastPkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxBroadcastPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxMulticastPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxMulticastPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxMulticastPkts = _Cie1000PortStatisticsRmonStatisticsRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 6),
    _Cie1000PortStatisticsRmonStatisticsRxMulticastPkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxMulticastPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts = _Cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 7),
    _Cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxUndersizePkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxUndersizePkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxUndersizePkts = _Cie1000PortStatisticsRmonStatisticsRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 8),
    _Cie1000PortStatisticsRmonStatisticsRxUndersizePkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxUndersizePkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxOversizePkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxOversizePkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxOversizePkts = _Cie1000PortStatisticsRmonStatisticsRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 9),
    _Cie1000PortStatisticsRmonStatisticsRxOversizePkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxOversizePkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxFragmentsPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxFragmentsPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxFragmentsPkts = _Cie1000PortStatisticsRmonStatisticsRxFragmentsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 10),
    _Cie1000PortStatisticsRmonStatisticsRxFragmentsPkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxFragmentsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxFragmentsPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRxJabbersPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRxJabbersPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRxJabbersPkts = _Cie1000PortStatisticsRmonStatisticsRxJabbersPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 11),
    _Cie1000PortStatisticsRmonStatisticsRxJabbersPkts_Type()
)
cie1000PortStatisticsRmonStatisticsRxJabbersPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRxJabbersPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRx64Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRx64Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRx64Pkts = _Cie1000PortStatisticsRmonStatisticsRx64Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 12),
    _Cie1000PortStatisticsRmonStatisticsRx64Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsRx64Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRx64Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRx65to127Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRx65to127Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRx65to127Pkts = _Cie1000PortStatisticsRmonStatisticsRx65to127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 13),
    _Cie1000PortStatisticsRmonStatisticsRx65to127Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsRx65to127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRx65to127Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRx128to255Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRx128to255Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRx128to255Pkts = _Cie1000PortStatisticsRmonStatisticsRx128to255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 14),
    _Cie1000PortStatisticsRmonStatisticsRx128to255Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsRx128to255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRx128to255Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRx256to511Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRx256to511Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRx256to511Pkts = _Cie1000PortStatisticsRmonStatisticsRx256to511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 15),
    _Cie1000PortStatisticsRmonStatisticsRx256to511Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsRx256to511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRx256to511Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRx512to1023Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRx512to1023Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRx512to1023Pkts = _Cie1000PortStatisticsRmonStatisticsRx512to1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 16),
    _Cie1000PortStatisticsRmonStatisticsRx512to1023Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsRx512to1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRx512to1023Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts = _Cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 17),
    _Cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsRx1519PktsToMax_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsRx1519PktsToMax_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsRx1519PktsToMax = _Cie1000PortStatisticsRmonStatisticsRx1519PktsToMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 18),
    _Cie1000PortStatisticsRmonStatisticsRx1519PktsToMax_Type()
)
cie1000PortStatisticsRmonStatisticsRx1519PktsToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsRx1519PktsToMax.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTxDropEvents_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTxDropEvents_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTxDropEvents = _Cie1000PortStatisticsRmonStatisticsTxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 19),
    _Cie1000PortStatisticsRmonStatisticsTxDropEvents_Type()
)
cie1000PortStatisticsRmonStatisticsTxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTxDropEvents.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTxOctets_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTxOctets_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTxOctets = _Cie1000PortStatisticsRmonStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 20),
    _Cie1000PortStatisticsRmonStatisticsTxOctets_Type()
)
cie1000PortStatisticsRmonStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTxOctets.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTxPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTxPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTxPkts = _Cie1000PortStatisticsRmonStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 21),
    _Cie1000PortStatisticsRmonStatisticsTxPkts_Type()
)
cie1000PortStatisticsRmonStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTxPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTxBroadcastPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTxBroadcastPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTxBroadcastPkts = _Cie1000PortStatisticsRmonStatisticsTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 22),
    _Cie1000PortStatisticsRmonStatisticsTxBroadcastPkts_Type()
)
cie1000PortStatisticsRmonStatisticsTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTxBroadcastPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTxMulticastPkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTxMulticastPkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTxMulticastPkts = _Cie1000PortStatisticsRmonStatisticsTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 23),
    _Cie1000PortStatisticsRmonStatisticsTxMulticastPkts_Type()
)
cie1000PortStatisticsRmonStatisticsTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTxMulticastPkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTx64Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTx64Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTx64Pkts = _Cie1000PortStatisticsRmonStatisticsTx64Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 24),
    _Cie1000PortStatisticsRmonStatisticsTx64Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsTx64Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTx64Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTx65to127Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTx65to127Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTx65to127Pkts = _Cie1000PortStatisticsRmonStatisticsTx65to127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 25),
    _Cie1000PortStatisticsRmonStatisticsTx65to127Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsTx65to127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTx65to127Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTx128to255Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTx128to255Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTx128to255Pkts = _Cie1000PortStatisticsRmonStatisticsTx128to255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 26),
    _Cie1000PortStatisticsRmonStatisticsTx128to255Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsTx128to255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTx128to255Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTx256to511Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTx256to511Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTx256to511Pkts = _Cie1000PortStatisticsRmonStatisticsTx256to511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 27),
    _Cie1000PortStatisticsRmonStatisticsTx256to511Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsTx256to511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTx256to511Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTx512to1023Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTx512to1023Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTx512to1023Pkts = _Cie1000PortStatisticsRmonStatisticsTx512to1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 28),
    _Cie1000PortStatisticsRmonStatisticsTx512to1023Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsTx512to1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTx512to1023Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts = _Cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 29),
    _Cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts_Type()
)
cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts.setStatus("current")
_Cie1000PortStatisticsRmonStatisticsTx1519PktsToMax_Type = Counter64
_Cie1000PortStatisticsRmonStatisticsTx1519PktsToMax_Object = MibTableColumn
cie1000PortStatisticsRmonStatisticsTx1519PktsToMax = _Cie1000PortStatisticsRmonStatisticsTx1519PktsToMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 1, 1, 30),
    _Cie1000PortStatisticsRmonStatisticsTx1519PktsToMax_Type()
)
cie1000PortStatisticsRmonStatisticsTx1519PktsToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTx1519PktsToMax.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTable_Object = MibTable
cie1000PortStatisticsIfGroupStatisticsTable = _Cie1000PortStatisticsIfGroupStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTable.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsEntry_Object = MibTableRow
cie1000PortStatisticsIfGroupStatisticsEntry = _Cie1000PortStatisticsIfGroupStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1)
)
cie1000PortStatisticsIfGroupStatisticsEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsEntry.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortStatisticsIfGroupStatisticsIfIndex_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsIfIndex = _Cie1000PortStatisticsIfGroupStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 1),
    _Cie1000PortStatisticsIfGroupStatisticsIfIndex_Type()
)
cie1000PortStatisticsIfGroupStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsIfIndex.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsRxOctets_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsRxOctets_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsRxOctets = _Cie1000PortStatisticsIfGroupStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 2),
    _Cie1000PortStatisticsIfGroupStatisticsRxOctets_Type()
)
cie1000PortStatisticsIfGroupStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsRxOctets.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts = _Cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 3),
    _Cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts = _Cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 4),
    _Cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts = _Cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 5),
    _Cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts = _Cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 6),
    _Cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsRxDiscards_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsRxDiscards_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsRxDiscards = _Cie1000PortStatisticsIfGroupStatisticsRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 7),
    _Cie1000PortStatisticsIfGroupStatisticsRxDiscards_Type()
)
cie1000PortStatisticsIfGroupStatisticsRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsRxDiscards.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsRxErrors_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsRxErrors_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsRxErrors = _Cie1000PortStatisticsIfGroupStatisticsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 8),
    _Cie1000PortStatisticsIfGroupStatisticsRxErrors_Type()
)
cie1000PortStatisticsIfGroupStatisticsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsRxErrors.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTxOctets_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsTxOctets_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsTxOctets = _Cie1000PortStatisticsIfGroupStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 9),
    _Cie1000PortStatisticsIfGroupStatisticsTxOctets_Type()
)
cie1000PortStatisticsIfGroupStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTxOctets.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts = _Cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 10),
    _Cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts = _Cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 11),
    _Cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts = _Cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 12),
    _Cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts = _Cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 13),
    _Cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts = _Cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 14),
    _Cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts.setStatus("current")
_Cie1000PortStatisticsIfGroupStatisticsTxErrorPkts_Type = Counter64
_Cie1000PortStatisticsIfGroupStatisticsTxErrorPkts_Object = MibTableColumn
cie1000PortStatisticsIfGroupStatisticsTxErrorPkts = _Cie1000PortStatisticsIfGroupStatisticsTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 2, 1, 15),
    _Cie1000PortStatisticsIfGroupStatisticsTxErrorPkts_Type()
)
cie1000PortStatisticsIfGroupStatisticsTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTxErrorPkts.setStatus("current")
_Cie1000PortStatisticsEthernetLikeStatisticsTable_Object = MibTable
cie1000PortStatisticsEthernetLikeStatisticsTable = _Cie1000PortStatisticsEthernetLikeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsEthernetLikeStatisticsTable.setStatus("current")
_Cie1000PortStatisticsEthernetLikeStatisticsEntry_Object = MibTableRow
cie1000PortStatisticsEthernetLikeStatisticsEntry = _Cie1000PortStatisticsEthernetLikeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 3, 1)
)
cie1000PortStatisticsEthernetLikeStatisticsEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortStatisticsEthernetLikeStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsEthernetLikeStatisticsEntry.setStatus("current")
_Cie1000PortStatisticsEthernetLikeStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortStatisticsEthernetLikeStatisticsIfIndex_Object = MibTableColumn
cie1000PortStatisticsEthernetLikeStatisticsIfIndex = _Cie1000PortStatisticsEthernetLikeStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 3, 1, 1),
    _Cie1000PortStatisticsEthernetLikeStatisticsIfIndex_Type()
)
cie1000PortStatisticsEthernetLikeStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatisticsEthernetLikeStatisticsIfIndex.setStatus("current")
_Cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames_Type = Counter64
_Cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames_Object = MibTableColumn
cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames = _Cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 3, 1, 2),
    _Cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames_Type()
)
cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames.setStatus("current")
_Cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames_Type = Counter64
_Cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames_Object = MibTableColumn
cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames = _Cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 3, 1, 3),
    _Cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames_Type()
)
cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames.setStatus("current")
_Cie1000PortStatisticsQueuesStatisticsTable_Object = MibTable
cie1000PortStatisticsQueuesStatisticsTable = _Cie1000PortStatisticsQueuesStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsQueuesStatisticsTable.setStatus("current")
_Cie1000PortStatisticsQueuesStatisticsEntry_Object = MibTableRow
cie1000PortStatisticsQueuesStatisticsEntry = _Cie1000PortStatisticsQueuesStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 4, 1)
)
cie1000PortStatisticsQueuesStatisticsEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortStatisticsQueuesStatisticsIfIndex"),
    (0, "CIE1000-PORT-MIB", "cie1000PortStatisticsQueuesStatisticsQueue"),
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsQueuesStatisticsEntry.setStatus("current")
_Cie1000PortStatisticsQueuesStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortStatisticsQueuesStatisticsIfIndex_Object = MibTableColumn
cie1000PortStatisticsQueuesStatisticsIfIndex = _Cie1000PortStatisticsQueuesStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 4, 1, 1),
    _Cie1000PortStatisticsQueuesStatisticsIfIndex_Type()
)
cie1000PortStatisticsQueuesStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatisticsQueuesStatisticsIfIndex.setStatus("current")


class _Cie1000PortStatisticsQueuesStatisticsQueue_Type(Integer32):
    """Custom type cie1000PortStatisticsQueuesStatisticsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000PortStatisticsQueuesStatisticsQueue_Type.__name__ = "Integer32"
_Cie1000PortStatisticsQueuesStatisticsQueue_Object = MibTableColumn
cie1000PortStatisticsQueuesStatisticsQueue = _Cie1000PortStatisticsQueuesStatisticsQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 4, 1, 2),
    _Cie1000PortStatisticsQueuesStatisticsQueue_Type()
)
cie1000PortStatisticsQueuesStatisticsQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatisticsQueuesStatisticsQueue.setStatus("current")
_Cie1000PortStatisticsQueuesStatisticsRxPrio_Type = Counter64
_Cie1000PortStatisticsQueuesStatisticsRxPrio_Object = MibTableColumn
cie1000PortStatisticsQueuesStatisticsRxPrio = _Cie1000PortStatisticsQueuesStatisticsRxPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 4, 1, 3),
    _Cie1000PortStatisticsQueuesStatisticsRxPrio_Type()
)
cie1000PortStatisticsQueuesStatisticsRxPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsQueuesStatisticsRxPrio.setStatus("current")
_Cie1000PortStatisticsQueuesStatisticsTxPrio_Type = Counter64
_Cie1000PortStatisticsQueuesStatisticsTxPrio_Object = MibTableColumn
cie1000PortStatisticsQueuesStatisticsTxPrio = _Cie1000PortStatisticsQueuesStatisticsTxPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 4, 1, 4),
    _Cie1000PortStatisticsQueuesStatisticsTxPrio_Type()
)
cie1000PortStatisticsQueuesStatisticsTxPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsQueuesStatisticsTxPrio.setStatus("current")
_Cie1000PortStatisticsBridgeStatisticsTable_Object = MibTable
cie1000PortStatisticsBridgeStatisticsTable = _Cie1000PortStatisticsBridgeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 5)
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsBridgeStatisticsTable.setStatus("current")
_Cie1000PortStatisticsBridgeStatisticsEntry_Object = MibTableRow
cie1000PortStatisticsBridgeStatisticsEntry = _Cie1000PortStatisticsBridgeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 5, 1)
)
cie1000PortStatisticsBridgeStatisticsEntry.setIndexNames(
    (0, "CIE1000-PORT-MIB", "cie1000PortStatisticsBridgeStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsBridgeStatisticsEntry.setStatus("current")
_Cie1000PortStatisticsBridgeStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortStatisticsBridgeStatisticsIfIndex_Object = MibTableColumn
cie1000PortStatisticsBridgeStatisticsIfIndex = _Cie1000PortStatisticsBridgeStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 5, 1, 1),
    _Cie1000PortStatisticsBridgeStatisticsIfIndex_Type()
)
cie1000PortStatisticsBridgeStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortStatisticsBridgeStatisticsIfIndex.setStatus("current")
_Cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard_Type = Counter64
_Cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard_Object = MibTableColumn
cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard = _Cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 1, 5, 5, 1, 2),
    _Cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard_Type()
)
cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard.setStatus("current")
_Cie1000PortMibConformance_ObjectIdentity = ObjectIdentity
cie1000PortMibConformance = _Cie1000PortMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2)
)
_Cie1000PortMibCompliances_ObjectIdentity = ObjectIdentity
cie1000PortMibCompliances = _Cie1000PortMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 1)
)
_Cie1000PortMibGroups_ObjectIdentity = ObjectIdentity
cie1000PortMibGroups = _Cie1000PortMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2)
)

# Managed Objects groups

cie1000PortConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 1)
)
cie1000PortConfigInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortConfigIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigShutdown"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigSpeed"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigAdvertiseDisabled"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigMediaType"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigFC"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigMTU"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigExcessiveRestart"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigPFC"),
        ("CIE1000-PORT-MIB", "cie1000PortConfigFrameLengthCheck"))
)
if mibBuilder.loadTexts:
    cie1000PortConfigInfoGroup.setStatus("current")

cie1000PortStatusInformationTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 2)
)
cie1000PortStatusInformationTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortStatusInformationIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationLink"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationFdx"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationFiber"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationSpeed"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationSFPType"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationSFPVendorName"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationSFPVendorPN"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationSFPVendorRev"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationSFPVendorSN"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationRxUtilization"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationTxUtilization"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationRxErrorUtilization"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationTxErrorUtilization"))
)
if mibBuilder.loadTexts:
    cie1000PortStatusInformationTableInfoGroup.setStatus("current")

cie1000PortStatusVeriPhyResultTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 3)
)
cie1000PortStatusVeriPhyResultTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyStatusPairA"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyStatusPairB"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyStatusPairC"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyStatusPairD"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD"))
)
if mibBuilder.loadTexts:
    cie1000PortStatusVeriPhyResultTableInfoGroup.setStatus("current")

cie1000PortControlStatisticsClearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 4)
)
cie1000PortControlStatisticsClearTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortControlStatisticsClearIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortControlStatisticsClearStatisticsClear"))
)
if mibBuilder.loadTexts:
    cie1000PortControlStatisticsClearTableInfoGroup.setStatus("current")

cie1000PortControlVeriPhyStartTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 5)
)
cie1000PortControlVeriPhyStartTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortControlVeriPhyStartIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortControlVeriPhyStartStart"))
)
if mibBuilder.loadTexts:
    cie1000PortControlVeriPhyStartTableInfoGroup.setStatus("current")

cie1000PortStatisticsRmonStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 6)
)
cie1000PortStatisticsRmonStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxDropEvents"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxOctets"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxBroadcastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxMulticastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxUndersizePkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxOversizePkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxFragmentsPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRxJabbersPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRx64Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRx65to127Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRx128to255Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRx256to511Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRx512to1023Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsRx1519PktsToMax"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTxDropEvents"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTxOctets"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTxPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTxBroadcastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTxMulticastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTx64Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTx65to127Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTx128to255Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTx256to511Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTx512to1023Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTx1519PktsToMax"))
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsRmonStatisticsTableInfoGroup.setStatus("current")

cie1000PortStatisticsIfGroupStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 7)
)
cie1000PortStatisticsIfGroupStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsRxOctets"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsRxDiscards"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsRxErrors"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTxOctets"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTxErrorPkts"))
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsIfGroupStatisticsTableInfoGroup.setStatus("current")

cie1000PortStatisticsEthernetLikeStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 8)
)
cie1000PortStatisticsEthernetLikeStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortStatisticsEthernetLikeStatisticsIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames"))
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsEthernetLikeStatisticsTableInfoGroup.setStatus("current")

cie1000PortStatisticsQueuesStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 9)
)
cie1000PortStatisticsQueuesStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortStatisticsQueuesStatisticsIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsQueuesStatisticsQueue"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsQueuesStatisticsRxPrio"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsQueuesStatisticsTxPrio"))
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsQueuesStatisticsTableInfoGroup.setStatus("current")

cie1000PortStatisticsBridgeStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 2, 10)
)
cie1000PortStatisticsBridgeStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortStatisticsBridgeStatisticsIfIndex"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard"))
)
if mibBuilder.loadTexts:
    cie1000PortStatisticsBridgeStatisticsTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000PortMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 11, 2, 1, 1)
)
cie1000PortMibCompliance.setObjects(
      *(("CIE1000-PORT-MIB", "cie1000PortConfigInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusInformationTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortStatusVeriPhyResultTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortControlStatisticsClearTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortControlVeriPhyStartTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsRmonStatisticsTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsIfGroupStatisticsTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsEthernetLikeStatisticsTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsQueuesStatisticsTableInfoGroup"),
        ("CIE1000-PORT-MIB", "cie1000PortStatisticsBridgeStatisticsTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000PortMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-PORT-MIB",
    **{"CIE1000PortFc": CIE1000PortFc,
       "CIE1000PortMedia": CIE1000PortMedia,
       "CIE1000PortPhyVeriPhyStatus": CIE1000PortPhyVeriPhyStatus,
       "CIE1000PortSpeed": CIE1000PortSpeed,
       "cie1000PortMib": cie1000PortMib,
       "cie1000PortMibObjects": cie1000PortMibObjects,
       "cie1000PortConfig": cie1000PortConfig,
       "cie1000PortConfigTable": cie1000PortConfigTable,
       "cie1000PortConfigEntry": cie1000PortConfigEntry,
       "cie1000PortConfigIfIndex": cie1000PortConfigIfIndex,
       "cie1000PortConfigShutdown": cie1000PortConfigShutdown,
       "cie1000PortConfigSpeed": cie1000PortConfigSpeed,
       "cie1000PortConfigAdvertiseDisabled": cie1000PortConfigAdvertiseDisabled,
       "cie1000PortConfigMediaType": cie1000PortConfigMediaType,
       "cie1000PortConfigFC": cie1000PortConfigFC,
       "cie1000PortConfigMTU": cie1000PortConfigMTU,
       "cie1000PortConfigExcessiveRestart": cie1000PortConfigExcessiveRestart,
       "cie1000PortConfigPFC": cie1000PortConfigPFC,
       "cie1000PortConfigFrameLengthCheck": cie1000PortConfigFrameLengthCheck,
       "cie1000PortStatus": cie1000PortStatus,
       "cie1000PortStatusInformationTable": cie1000PortStatusInformationTable,
       "cie1000PortStatusInformationEntry": cie1000PortStatusInformationEntry,
       "cie1000PortStatusInformationIfIndex": cie1000PortStatusInformationIfIndex,
       "cie1000PortStatusInformationLink": cie1000PortStatusInformationLink,
       "cie1000PortStatusInformationFdx": cie1000PortStatusInformationFdx,
       "cie1000PortStatusInformationFiber": cie1000PortStatusInformationFiber,
       "cie1000PortStatusInformationSpeed": cie1000PortStatusInformationSpeed,
       "cie1000PortStatusInformationSFPType": cie1000PortStatusInformationSFPType,
       "cie1000PortStatusInformationSFPVendorName": cie1000PortStatusInformationSFPVendorName,
       "cie1000PortStatusInformationSFPVendorPN": cie1000PortStatusInformationSFPVendorPN,
       "cie1000PortStatusInformationSFPVendorRev": cie1000PortStatusInformationSFPVendorRev,
       "cie1000PortStatusInformationSFPVendorSN": cie1000PortStatusInformationSFPVendorSN,
       "cie1000PortStatusInformationRxUtilization": cie1000PortStatusInformationRxUtilization,
       "cie1000PortStatusInformationTxUtilization": cie1000PortStatusInformationTxUtilization,
       "cie1000PortStatusInformationRxErrorUtilization": cie1000PortStatusInformationRxErrorUtilization,
       "cie1000PortStatusInformationTxErrorUtilization": cie1000PortStatusInformationTxErrorUtilization,
       "cie1000PortStatusVeriPhyResult": cie1000PortStatusVeriPhyResult,
       "cie1000PortStatusVeriPhyResultTable": cie1000PortStatusVeriPhyResultTable,
       "cie1000PortStatusVeriPhyResultEntry": cie1000PortStatusVeriPhyResultEntry,
       "cie1000PortStatusVeriPhyResultIfIndex": cie1000PortStatusVeriPhyResultIfIndex,
       "cie1000PortStatusVeriPhyResultVeriPhyStatusPairA": cie1000PortStatusVeriPhyResultVeriPhyStatusPairA,
       "cie1000PortStatusVeriPhyResultVeriPhyStatusPairB": cie1000PortStatusVeriPhyResultVeriPhyStatusPairB,
       "cie1000PortStatusVeriPhyResultVeriPhyStatusPairC": cie1000PortStatusVeriPhyResultVeriPhyStatusPairC,
       "cie1000PortStatusVeriPhyResultVeriPhyStatusPairD": cie1000PortStatusVeriPhyResultVeriPhyStatusPairD,
       "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA": cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairA,
       "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB": cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairB,
       "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC": cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairC,
       "cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD": cie1000PortStatusVeriPhyResultVeriPhyLengthStatusPairD,
       "cie1000PortControl": cie1000PortControl,
       "cie1000PortControlStatisticsClear": cie1000PortControlStatisticsClear,
       "cie1000PortControlStatisticsClearTable": cie1000PortControlStatisticsClearTable,
       "cie1000PortControlStatisticsClearEntry": cie1000PortControlStatisticsClearEntry,
       "cie1000PortControlStatisticsClearIfIndex": cie1000PortControlStatisticsClearIfIndex,
       "cie1000PortControlStatisticsClearStatisticsClear": cie1000PortControlStatisticsClearStatisticsClear,
       "cie1000PortControlVeriPhyStart": cie1000PortControlVeriPhyStart,
       "cie1000PortControlVeriPhyStartTable": cie1000PortControlVeriPhyStartTable,
       "cie1000PortControlVeriPhyStartEntry": cie1000PortControlVeriPhyStartEntry,
       "cie1000PortControlVeriPhyStartIfIndex": cie1000PortControlVeriPhyStartIfIndex,
       "cie1000PortControlVeriPhyStartStart": cie1000PortControlVeriPhyStartStart,
       "cie1000PortStatistics": cie1000PortStatistics,
       "cie1000PortStatisticsRmonStatisticsTable": cie1000PortStatisticsRmonStatisticsTable,
       "cie1000PortStatisticsRmonStatisticsEntry": cie1000PortStatisticsRmonStatisticsEntry,
       "cie1000PortStatisticsRmonStatisticsIfIndex": cie1000PortStatisticsRmonStatisticsIfIndex,
       "cie1000PortStatisticsRmonStatisticsRxDropEvents": cie1000PortStatisticsRmonStatisticsRxDropEvents,
       "cie1000PortStatisticsRmonStatisticsRxOctets": cie1000PortStatisticsRmonStatisticsRxOctets,
       "cie1000PortStatisticsRmonStatisticsRxPkts": cie1000PortStatisticsRmonStatisticsRxPkts,
       "cie1000PortStatisticsRmonStatisticsRxBroadcastPkts": cie1000PortStatisticsRmonStatisticsRxBroadcastPkts,
       "cie1000PortStatisticsRmonStatisticsRxMulticastPkts": cie1000PortStatisticsRmonStatisticsRxMulticastPkts,
       "cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts": cie1000PortStatisticsRmonStatisticsRxCrcAlignErrPkts,
       "cie1000PortStatisticsRmonStatisticsRxUndersizePkts": cie1000PortStatisticsRmonStatisticsRxUndersizePkts,
       "cie1000PortStatisticsRmonStatisticsRxOversizePkts": cie1000PortStatisticsRmonStatisticsRxOversizePkts,
       "cie1000PortStatisticsRmonStatisticsRxFragmentsPkts": cie1000PortStatisticsRmonStatisticsRxFragmentsPkts,
       "cie1000PortStatisticsRmonStatisticsRxJabbersPkts": cie1000PortStatisticsRmonStatisticsRxJabbersPkts,
       "cie1000PortStatisticsRmonStatisticsRx64Pkts": cie1000PortStatisticsRmonStatisticsRx64Pkts,
       "cie1000PortStatisticsRmonStatisticsRx65to127Pkts": cie1000PortStatisticsRmonStatisticsRx65to127Pkts,
       "cie1000PortStatisticsRmonStatisticsRx128to255Pkts": cie1000PortStatisticsRmonStatisticsRx128to255Pkts,
       "cie1000PortStatisticsRmonStatisticsRx256to511Pkts": cie1000PortStatisticsRmonStatisticsRx256to511Pkts,
       "cie1000PortStatisticsRmonStatisticsRx512to1023Pkts": cie1000PortStatisticsRmonStatisticsRx512to1023Pkts,
       "cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts": cie1000PortStatisticsRmonStatisticsRx1024to1518Pkts,
       "cie1000PortStatisticsRmonStatisticsRx1519PktsToMax": cie1000PortStatisticsRmonStatisticsRx1519PktsToMax,
       "cie1000PortStatisticsRmonStatisticsTxDropEvents": cie1000PortStatisticsRmonStatisticsTxDropEvents,
       "cie1000PortStatisticsRmonStatisticsTxOctets": cie1000PortStatisticsRmonStatisticsTxOctets,
       "cie1000PortStatisticsRmonStatisticsTxPkts": cie1000PortStatisticsRmonStatisticsTxPkts,
       "cie1000PortStatisticsRmonStatisticsTxBroadcastPkts": cie1000PortStatisticsRmonStatisticsTxBroadcastPkts,
       "cie1000PortStatisticsRmonStatisticsTxMulticastPkts": cie1000PortStatisticsRmonStatisticsTxMulticastPkts,
       "cie1000PortStatisticsRmonStatisticsTx64Pkts": cie1000PortStatisticsRmonStatisticsTx64Pkts,
       "cie1000PortStatisticsRmonStatisticsTx65to127Pkts": cie1000PortStatisticsRmonStatisticsTx65to127Pkts,
       "cie1000PortStatisticsRmonStatisticsTx128to255Pkts": cie1000PortStatisticsRmonStatisticsTx128to255Pkts,
       "cie1000PortStatisticsRmonStatisticsTx256to511Pkts": cie1000PortStatisticsRmonStatisticsTx256to511Pkts,
       "cie1000PortStatisticsRmonStatisticsTx512to1023Pkts": cie1000PortStatisticsRmonStatisticsTx512to1023Pkts,
       "cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts": cie1000PortStatisticsRmonStatisticsTx1024to1518Pkts,
       "cie1000PortStatisticsRmonStatisticsTx1519PktsToMax": cie1000PortStatisticsRmonStatisticsTx1519PktsToMax,
       "cie1000PortStatisticsIfGroupStatisticsTable": cie1000PortStatisticsIfGroupStatisticsTable,
       "cie1000PortStatisticsIfGroupStatisticsEntry": cie1000PortStatisticsIfGroupStatisticsEntry,
       "cie1000PortStatisticsIfGroupStatisticsIfIndex": cie1000PortStatisticsIfGroupStatisticsIfIndex,
       "cie1000PortStatisticsIfGroupStatisticsRxOctets": cie1000PortStatisticsIfGroupStatisticsRxOctets,
       "cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts": cie1000PortStatisticsIfGroupStatisticsRxUnicastPkts,
       "cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts": cie1000PortStatisticsIfGroupStatisticsRxMulticastPkts,
       "cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts": cie1000PortStatisticsIfGroupStatisticsRxBroadcastPkts,
       "cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts": cie1000PortStatisticsIfGroupStatisticsRxNonUnicastPkts,
       "cie1000PortStatisticsIfGroupStatisticsRxDiscards": cie1000PortStatisticsIfGroupStatisticsRxDiscards,
       "cie1000PortStatisticsIfGroupStatisticsRxErrors": cie1000PortStatisticsIfGroupStatisticsRxErrors,
       "cie1000PortStatisticsIfGroupStatisticsTxOctets": cie1000PortStatisticsIfGroupStatisticsTxOctets,
       "cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts": cie1000PortStatisticsIfGroupStatisticsTxUnicastPkts,
       "cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts": cie1000PortStatisticsIfGroupStatisticsTxMulticastPkts,
       "cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts": cie1000PortStatisticsIfGroupStatisticsTxBroadcastPkts,
       "cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts": cie1000PortStatisticsIfGroupStatisticsTxNonUnicastPkts,
       "cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts": cie1000PortStatisticsIfGroupStatisticsTxDiscardPkts,
       "cie1000PortStatisticsIfGroupStatisticsTxErrorPkts": cie1000PortStatisticsIfGroupStatisticsTxErrorPkts,
       "cie1000PortStatisticsEthernetLikeStatisticsTable": cie1000PortStatisticsEthernetLikeStatisticsTable,
       "cie1000PortStatisticsEthernetLikeStatisticsEntry": cie1000PortStatisticsEthernetLikeStatisticsEntry,
       "cie1000PortStatisticsEthernetLikeStatisticsIfIndex": cie1000PortStatisticsEthernetLikeStatisticsIfIndex,
       "cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames": cie1000PortStatisticsEthernetLikeStatisticsRxPauseFrames,
       "cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames": cie1000PortStatisticsEthernetLikeStatisticsTxPauseFrames,
       "cie1000PortStatisticsQueuesStatisticsTable": cie1000PortStatisticsQueuesStatisticsTable,
       "cie1000PortStatisticsQueuesStatisticsEntry": cie1000PortStatisticsQueuesStatisticsEntry,
       "cie1000PortStatisticsQueuesStatisticsIfIndex": cie1000PortStatisticsQueuesStatisticsIfIndex,
       "cie1000PortStatisticsQueuesStatisticsQueue": cie1000PortStatisticsQueuesStatisticsQueue,
       "cie1000PortStatisticsQueuesStatisticsRxPrio": cie1000PortStatisticsQueuesStatisticsRxPrio,
       "cie1000PortStatisticsQueuesStatisticsTxPrio": cie1000PortStatisticsQueuesStatisticsTxPrio,
       "cie1000PortStatisticsBridgeStatisticsTable": cie1000PortStatisticsBridgeStatisticsTable,
       "cie1000PortStatisticsBridgeStatisticsEntry": cie1000PortStatisticsBridgeStatisticsEntry,
       "cie1000PortStatisticsBridgeStatisticsIfIndex": cie1000PortStatisticsBridgeStatisticsIfIndex,
       "cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard": cie1000PortStatisticsBridgeStatisticsRxBridgeDiscard,
       "cie1000PortMibConformance": cie1000PortMibConformance,
       "cie1000PortMibCompliances": cie1000PortMibCompliances,
       "cie1000PortMibCompliance": cie1000PortMibCompliance,
       "cie1000PortMibGroups": cie1000PortMibGroups,
       "cie1000PortConfigInfoGroup": cie1000PortConfigInfoGroup,
       "cie1000PortStatusInformationTableInfoGroup": cie1000PortStatusInformationTableInfoGroup,
       "cie1000PortStatusVeriPhyResultTableInfoGroup": cie1000PortStatusVeriPhyResultTableInfoGroup,
       "cie1000PortControlStatisticsClearTableInfoGroup": cie1000PortControlStatisticsClearTableInfoGroup,
       "cie1000PortControlVeriPhyStartTableInfoGroup": cie1000PortControlVeriPhyStartTableInfoGroup,
       "cie1000PortStatisticsRmonStatisticsTableInfoGroup": cie1000PortStatisticsRmonStatisticsTableInfoGroup,
       "cie1000PortStatisticsIfGroupStatisticsTableInfoGroup": cie1000PortStatisticsIfGroupStatisticsTableInfoGroup,
       "cie1000PortStatisticsEthernetLikeStatisticsTableInfoGroup": cie1000PortStatisticsEthernetLikeStatisticsTableInfoGroup,
       "cie1000PortStatisticsQueuesStatisticsTableInfoGroup": cie1000PortStatisticsQueuesStatisticsTableInfoGroup,
       "cie1000PortStatisticsBridgeStatisticsTableInfoGroup": cie1000PortStatisticsBridgeStatisticsTableInfoGroup}
)
