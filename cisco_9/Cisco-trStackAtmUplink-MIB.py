# SNMP MIB module (Cisco-trStackAtmUplink-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/Cisco-trStackAtmUplink-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:14:15 2025
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

(ciscoTsUplinkMIBs,) = mibBuilder.importSymbols(
    "CISCO-TS-STACK-MIB",
    "ciscoTsUplinkMIBs")

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


# Types definitions



class AtmAddress(OctetString):
    """Custom type AtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )





class ModuleInteger(Integer32):
    """Custom type ModuleInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )





class VapInteger(Integer32):
    """Custom type VapInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )





class VpiInteger(Integer32):
    """Custom type VpiInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )





class VciInteger(Integer32):
    """Custom type VciInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )





class TrafficDescrType(Integer32):
    """Custom type TrafficDescrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("atmfNoClpNoScr", 3),
          ("atmfNoClpScr", 6),
          ("atmfClpNoTaggingScr", 7),
          ("atmfClpTaggingScr", 8),
          ("bestEffort", 9),
          ("atmClpABR", 10))
    )





class QosClass(Integer32):
    """Custom type QosClass based on Integer32"""
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
        *(("qos1", 1),
          ("qos2", 2),
          ("qos3", 3),
          ("qos4", 4),
          ("qosNone", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Atm155MBUplinkMIB_ObjectIdentity = ObjectIdentity
atm155MBUplinkMIB = _Atm155MBUplinkMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1)
)
_AtmUplinkInformation_ObjectIdentity = ObjectIdentity
atmUplinkInformation = _AtmUplinkInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1)
)
_AtmUplinkInfoTable_Object = MibTable
atmUplinkInfoTable = _AtmUplinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmUplinkInfoTable.setStatus("mandatory")
_AtmUplinkInfoEntry_Object = MibTableRow
atmUplinkInfoEntry = _AtmUplinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1)
)
atmUplinkInfoEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    atmUplinkInfoEntry.setStatus("mandatory")
_AtmUplinkModuleIndex_Type = ModuleInteger
_AtmUplinkModuleIndex_Object = MibTableColumn
atmUplinkModuleIndex = _AtmUplinkModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 1),
    _AtmUplinkModuleIndex_Type()
)
atmUplinkModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmUplinkModuleIndex.setStatus("mandatory")
_InfoHardwareProductId_Type = DisplayString
_InfoHardwareProductId_Object = MibTableColumn
infoHardwareProductId = _InfoHardwareProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 2),
    _InfoHardwareProductId_Type()
)
infoHardwareProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareProductId.setStatus("mandatory")
_InfoHardwareVersion_Type = DisplayString
_InfoHardwareVersion_Object = MibTableColumn
infoHardwareVersion = _InfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 3),
    _InfoHardwareVersion_Type()
)
infoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareVersion.setStatus("mandatory")
_InfoHardwareECOLevel_Type = DisplayString
_InfoHardwareECOLevel_Object = MibTableColumn
infoHardwareECOLevel = _InfoHardwareECOLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 4),
    _InfoHardwareECOLevel_Type()
)
infoHardwareECOLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareECOLevel.setStatus("mandatory")
_InfoHardwareSerialNumber_Type = DisplayString
_InfoHardwareSerialNumber_Object = MibTableColumn
infoHardwareSerialNumber = _InfoHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 5),
    _InfoHardwareSerialNumber_Type()
)
infoHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareSerialNumber.setStatus("mandatory")
_InfoSoftwareProductId_Type = DisplayString
_InfoSoftwareProductId_Object = MibTableColumn
infoSoftwareProductId = _InfoSoftwareProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 6),
    _InfoSoftwareProductId_Type()
)
infoSoftwareProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareProductId.setStatus("mandatory")
_InfoSoftwareVersion_Type = DisplayString
_InfoSoftwareVersion_Object = MibTableColumn
infoSoftwareVersion = _InfoSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 7),
    _InfoSoftwareVersion_Type()
)
infoSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareVersion.setStatus("mandatory")
_InfoSoftwareECOLevel_Type = DisplayString
_InfoSoftwareECOLevel_Object = MibTableColumn
infoSoftwareECOLevel = _InfoSoftwareECOLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 8),
    _InfoSoftwareECOLevel_Type()
)
infoSoftwareECOLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareECOLevel.setStatus("mandatory")
_InfoBootpromVersion_Type = DisplayString
_InfoBootpromVersion_Object = MibTableColumn
infoBootpromVersion = _InfoBootpromVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 1, 1, 1, 9),
    _InfoBootpromVersion_Type()
)
infoBootpromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBootpromVersion.setStatus("mandatory")
_AtmUplinkConfiguration_ObjectIdentity = ObjectIdentity
atmUplinkConfiguration = _AtmUplinkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2)
)
_AtmPortHwSetupTable_Object = MibTable
atmPortHwSetupTable = _AtmPortHwSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmPortHwSetupTable.setStatus("mandatory")
_AtmPortHwSetupEntry_Object = MibTableRow
atmPortHwSetupEntry = _AtmPortHwSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 1, 1)
)
atmPortHwSetupEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    atmPortHwSetupEntry.setStatus("mandatory")


class _HwConfigMasterTiming_Type(Integer32):
    """Custom type hwConfigMasterTiming based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("local", 2))
    )


_HwConfigMasterTiming_Type.__name__ = "Integer32"
_HwConfigMasterTiming_Object = MibTableColumn
hwConfigMasterTiming = _HwConfigMasterTiming_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 1, 1, 1),
    _HwConfigMasterTiming_Type()
)
hwConfigMasterTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConfigMasterTiming.setStatus("mandatory")


class _HwConfigTcFramingMode_Type(Integer32):
    """Custom type hwConfigTcFramingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 1),
          ("sonet", 2))
    )


_HwConfigTcFramingMode_Type.__name__ = "Integer32"
_HwConfigTcFramingMode_Object = MibTableColumn
hwConfigTcFramingMode = _HwConfigTcFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 1, 1, 2),
    _HwConfigTcFramingMode_Type()
)
hwConfigTcFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConfigTcFramingMode.setStatus("mandatory")


class _HwConfigEmptyCells_Type(Integer32):
    """Custom type hwConfigEmptyCells based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassigned", 2))
    )


_HwConfigEmptyCells_Type.__name__ = "Integer32"
_HwConfigEmptyCells_Object = MibTableColumn
hwConfigEmptyCells = _HwConfigEmptyCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 1, 1, 3),
    _HwConfigEmptyCells_Type()
)
hwConfigEmptyCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConfigEmptyCells.setStatus("mandatory")
_CommonVapParameterTable_Object = MibTable
commonVapParameterTable = _CommonVapParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    commonVapParameterTable.setStatus("mandatory")
_CommonVapParameterEntry_Object = MibTableRow
commonVapParameterEntry = _CommonVapParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1)
)
commonVapParameterEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    commonVapParameterEntry.setStatus("mandatory")


class _ConfigEnableSvcSupport_Type(Integer32):
    """Custom type configEnableSvcSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_ConfigEnableSvcSupport_Type.__name__ = "Integer32"
_ConfigEnableSvcSupport_Object = MibTableColumn
configEnableSvcSupport = _ConfigEnableSvcSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 1),
    _ConfigEnableSvcSupport_Type()
)
configEnableSvcSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableSvcSupport.setStatus("mandatory")


class _ConfigIlmiAddressRegistrationSupport_Type(Integer32):
    """Custom type configIlmiAddressRegistrationSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_ConfigIlmiAddressRegistrationSupport_Type.__name__ = "Integer32"
_ConfigIlmiAddressRegistrationSupport_Object = MibTableColumn
configIlmiAddressRegistrationSupport = _ConfigIlmiAddressRegistrationSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 2),
    _ConfigIlmiAddressRegistrationSupport_Type()
)
configIlmiAddressRegistrationSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIlmiAddressRegistrationSupport.setStatus("mandatory")


class _ConfigCommonNumberOfVccs_Type(Integer32):
    """Custom type configCommonNumberOfVccs based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 2048),
    )


_ConfigCommonNumberOfVccs_Type.__name__ = "Integer32"
_ConfigCommonNumberOfVccs_Object = MibTableColumn
configCommonNumberOfVccs = _ConfigCommonNumberOfVccs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 3),
    _ConfigCommonNumberOfVccs_Type()
)
configCommonNumberOfVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonNumberOfVccs.setStatus("mandatory")


class _ConfigCommonNumberOfDestinations_Type(Integer32):
    """Custom type configCommonNumberOfDestinations based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4096),
    )


_ConfigCommonNumberOfDestinations_Type.__name__ = "Integer32"
_ConfigCommonNumberOfDestinations_Object = MibTableColumn
configCommonNumberOfDestinations = _ConfigCommonNumberOfDestinations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 4),
    _ConfigCommonNumberOfDestinations_Type()
)
configCommonNumberOfDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonNumberOfDestinations.setStatus("mandatory")


class _ConfigUniVersion_Type(Integer32):
    """Custom type configUniVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_ConfigUniVersion_Type.__name__ = "Integer32"
_ConfigUniVersion_Object = MibTableColumn
configUniVersion = _ConfigUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 5),
    _ConfigUniVersion_Type()
)
configUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configUniVersion.setStatus("mandatory")


class _ConfigMaxLineRate_Type(Integer32):
    """Custom type configMaxLineRate based on Integer32"""
    defaultValue = 353208

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(353, 353208),
    )


_ConfigMaxLineRate_Type.__name__ = "Integer32"
_ConfigMaxLineRate_Object = MibTableColumn
configMaxLineRate = _ConfigMaxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 6),
    _ConfigMaxLineRate_Type()
)
configMaxLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMaxLineRate.setStatus("mandatory")
_ConfigResetCounters_Type = Integer32
_ConfigResetCounters_Object = MibTableColumn
configResetCounters = _ConfigResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 7),
    _ConfigResetCounters_Type()
)
configResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configResetCounters.setStatus("mandatory")


class _ConfigModuleState_Type(Integer32):
    """Custom type configModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("booting", 3),
          ("down", 4),
          ("goingUp", 5),
          ("up", 6),
          ("goingDown", 7),
          ("failing", 8))
    )


_ConfigModuleState_Type.__name__ = "Integer32"
_ConfigModuleState_Object = MibTableColumn
configModuleState = _ConfigModuleState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 2, 1, 8),
    _ConfigModuleState_Type()
)
configModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModuleState.setStatus("mandatory")
_VapConfigTable_Object = MibTable
vapConfigTable = _VapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vapConfigTable.setStatus("mandatory")
_VapConfigEntry_Object = MibTableRow
vapConfigEntry = _VapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1)
)
vapConfigEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "vapIndex"),
)
if mibBuilder.loadTexts:
    vapConfigEntry.setStatus("mandatory")
_VapIndex_Type = VapInteger
_VapIndex_Object = MibTableColumn
vapIndex = _VapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 1),
    _VapIndex_Type()
)
vapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vapIndex.setStatus("mandatory")
_VapLecIndex_Type = Integer32
_VapLecIndex_Object = MibTableColumn
vapLecIndex = _VapLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 2),
    _VapLecIndex_Type()
)
vapLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapLecIndex.setStatus("mandatory")


class _VapAtmAddressAssignment_Type(Integer32):
    """Custom type vapAtmAddressAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_VapAtmAddressAssignment_Type.__name__ = "Integer32"
_VapAtmAddressAssignment_Object = MibTableColumn
vapAtmAddressAssignment = _VapAtmAddressAssignment_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 3),
    _VapAtmAddressAssignment_Type()
)
vapAtmAddressAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapAtmAddressAssignment.setStatus("mandatory")
_VapAtmAddress_Type = AtmAddress
_VapAtmAddress_Object = MibTableColumn
vapAtmAddress = _VapAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 4),
    _VapAtmAddress_Type()
)
vapAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapAtmAddress.setStatus("mandatory")
_VapLecsAtmAddress_Type = AtmAddress
_VapLecsAtmAddress_Object = MibTableColumn
vapLecsAtmAddress = _VapLecsAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 5),
    _VapLecsAtmAddress_Type()
)
vapLecsAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapLecsAtmAddress.setStatus("mandatory")


class _VapLecsVpi_Type(VpiInteger):
    """Custom type vapLecsVpi based on VpiInteger"""
    defaultValue = 0


_VapLecsVpi_Type.__name__ = "VpiInteger"
_VapLecsVpi_Object = MibTableColumn
vapLecsVpi = _VapLecsVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 6),
    _VapLecsVpi_Type()
)
vapLecsVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapLecsVpi.setStatus("mandatory")


class _VapLecsVci_Type(VciInteger):
    """Custom type vapLecsVci based on VciInteger"""
    defaultValue = 0


_VapLecsVci_Type.__name__ = "VciInteger"
_VapLecsVci_Object = MibTableColumn
vapLecsVci = _VapLecsVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 7),
    _VapLecsVci_Type()
)
vapLecsVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapLecsVci.setStatus("mandatory")


class _VapGuaranteedVccs_Type(Integer32):
    """Custom type vapGuaranteedVccs based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2048),
    )


_VapGuaranteedVccs_Type.__name__ = "Integer32"
_VapGuaranteedVccs_Object = MibTableColumn
vapGuaranteedVccs = _VapGuaranteedVccs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 8),
    _VapGuaranteedVccs_Type()
)
vapGuaranteedVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapGuaranteedVccs.setStatus("mandatory")


class _VapGuaranteedDestinations_Type(Integer32):
    """Custom type vapGuaranteedDestinations based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_VapGuaranteedDestinations_Type.__name__ = "Integer32"
_VapGuaranteedDestinations_Object = MibTableColumn
vapGuaranteedDestinations = _VapGuaranteedDestinations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 9),
    _VapGuaranteedDestinations_Type()
)
vapGuaranteedDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapGuaranteedDestinations.setStatus("mandatory")


class _VapDefaultTrafficProfile_Type(Integer32):
    """Custom type vapDefaultTrafficProfile based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_VapDefaultTrafficProfile_Type.__name__ = "Integer32"
_VapDefaultTrafficProfile_Object = MibTableColumn
vapDefaultTrafficProfile = _VapDefaultTrafficProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 10),
    _VapDefaultTrafficProfile_Type()
)
vapDefaultTrafficProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDefaultTrafficProfile.setStatus("mandatory")


class _VapMaxRxRateDifference_Type(Integer32):
    """Custom type vapMaxRxRateDifference based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VapMaxRxRateDifference_Type.__name__ = "Integer32"
_VapMaxRxRateDifference_Object = MibTableColumn
vapMaxRxRateDifference = _VapMaxRxRateDifference_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 11),
    _VapMaxRxRateDifference_Type()
)
vapMaxRxRateDifference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapMaxRxRateDifference.setStatus("mandatory")


class _VapMaxTxRateDifference_Type(Integer32):
    """Custom type vapMaxTxRateDifference based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VapMaxTxRateDifference_Type.__name__ = "Integer32"
_VapMaxTxRateDifference_Object = MibTableColumn
vapMaxTxRateDifference = _VapMaxTxRateDifference_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 12),
    _VapMaxTxRateDifference_Type()
)
vapMaxTxRateDifference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapMaxTxRateDifference.setStatus("mandatory")


class _VapTraceMask_Type(Integer32):
    """Custom type vapTraceMask based on Integer32"""
    defaultValue = 0


_VapTraceMask_Type.__name__ = "Integer32"
_VapTraceMask_Object = MibTableColumn
vapTraceMask = _VapTraceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 13),
    _VapTraceMask_Type()
)
vapTraceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapTraceMask.setStatus("mandatory")
_VapResetCounters_Type = Integer32
_VapResetCounters_Object = MibTableColumn
vapResetCounters = _VapResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 14),
    _VapResetCounters_Type()
)
vapResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapResetCounters.setStatus("mandatory")
_VapResetAddrs_Type = Integer32
_VapResetAddrs_Object = MibTableColumn
vapResetAddrs = _VapResetAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 15),
    _VapResetAddrs_Type()
)
vapResetAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapResetAddrs.setStatus("mandatory")


class _VapMaxExplorerRate_Type(Integer32):
    """Custom type vapMaxExplorerRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5000),
    )


_VapMaxExplorerRate_Type.__name__ = "Integer32"
_VapMaxExplorerRate_Object = MibTableColumn
vapMaxExplorerRate = _VapMaxExplorerRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 16),
    _VapMaxExplorerRate_Type()
)
vapMaxExplorerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapMaxExplorerRate.setStatus("mandatory")


class _VapSpanningTreeMode_Type(Integer32):
    """Custom type vapSpanningTreeMode based on Integer32"""
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
        *(("auto", 1),
          ("forwarding", 2),
          ("blocking", 3),
          ("unknown", 4))
    )


_VapSpanningTreeMode_Type.__name__ = "Integer32"
_VapSpanningTreeMode_Object = MibTableColumn
vapSpanningTreeMode = _VapSpanningTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 17),
    _VapSpanningTreeMode_Type()
)
vapSpanningTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapSpanningTreeMode.setStatus("mandatory")


class _VapState_Type(Integer32):
    """Custom type vapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("unknown", 1),
          ("disabled", 2),
          ("goingUp", 3),
          ("up", 4),
          ("goingAdminDown", 5),
          ("adminDown", 6),
          ("failing", 7),
          ("waitingForModuleUp", 8),
          ("forwarding", 9))
    )


_VapState_Type.__name__ = "Integer32"
_VapState_Object = MibTableColumn
vapState = _VapState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 3, 1, 18),
    _VapState_Type()
)
vapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapState.setStatus("mandatory")
_PvcConfigTable_Object = MibTable
pvcConfigTable = _PvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pvcConfigTable.setStatus("mandatory")
_PvcConfigEntry_Object = MibTableRow
pvcConfigEntry = _PvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1)
)
pvcConfigEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "pvcVpi"),
    (0, "Cisco-trStackAtmUplink-MIB", "pvcVci"),
)
if mibBuilder.loadTexts:
    pvcConfigEntry.setStatus("mandatory")
_PvcVpi_Type = VpiInteger
_PvcVpi_Object = MibTableColumn
pvcVpi = _PvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1, 1),
    _PvcVpi_Type()
)
pvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvcVpi.setStatus("mandatory")
_PvcVci_Type = VciInteger
_PvcVci_Object = MibTableColumn
pvcVci = _PvcVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1, 2),
    _PvcVci_Type()
)
pvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvcVci.setStatus("mandatory")
_PvcAtmAddress_Type = AtmAddress
_PvcAtmAddress_Object = MibTableColumn
pvcAtmAddress = _PvcAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1, 3),
    _PvcAtmAddress_Type()
)
pvcAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcAtmAddress.setStatus("mandatory")


class _PvcType_Type(Integer32):
    """Custom type pvcType based on Integer32"""
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
        *(("dataDirectVcc", 1),
          ("controlDirectVcc", 2),
          ("controlDistributeVcc", 3),
          ("multicastSendVcc", 4),
          ("multicastForwardVcc", 5))
    )


_PvcType_Type.__name__ = "Integer32"
_PvcType_Object = MibTableColumn
pvcType = _PvcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1, 4),
    _PvcType_Type()
)
pvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcType.setStatus("mandatory")


class _PvcTrafficProfileIndex_Type(Integer32):
    """Custom type pvcTrafficProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_PvcTrafficProfileIndex_Type.__name__ = "Integer32"
_PvcTrafficProfileIndex_Object = MibTableColumn
pvcTrafficProfileIndex = _PvcTrafficProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1, 5),
    _PvcTrafficProfileIndex_Type()
)
pvcTrafficProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcTrafficProfileIndex.setStatus("mandatory")
_PvcVapIndex_Type = VapInteger
_PvcVapIndex_Object = MibTableColumn
pvcVapIndex = _PvcVapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1, 6),
    _PvcVapIndex_Type()
)
pvcVapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcVapIndex.setStatus("mandatory")
_PvcRowStatus_Type = RowStatus
_PvcRowStatus_Object = MibTableColumn
pvcRowStatus = _PvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 4, 1, 7),
    _PvcRowStatus_Type()
)
pvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRowStatus.setStatus("mandatory")
_TpTrafficProfileTable_Object = MibTable
tpTrafficProfileTable = _TpTrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tpTrafficProfileTable.setStatus("mandatory")
_TpTrafficProfileEntry_Object = MibTableRow
tpTrafficProfileEntry = _TpTrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1)
)
tpTrafficProfileEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "tpTrafficProfileIndex"),
)
if mibBuilder.loadTexts:
    tpTrafficProfileEntry.setStatus("mandatory")


class _TpTrafficProfileIndex_Type(Integer32):
    """Custom type tpTrafficProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TpTrafficProfileIndex_Type.__name__ = "Integer32"
_TpTrafficProfileIndex_Object = MibTableColumn
tpTrafficProfileIndex = _TpTrafficProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 1),
    _TpTrafficProfileIndex_Type()
)
tpTrafficProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpTrafficProfileIndex.setStatus("mandatory")
_TpTrafficType_Type = TrafficDescrType
_TpTrafficType_Object = MibTableColumn
tpTrafficType = _TpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 2),
    _TpTrafficType_Type()
)
tpTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTrafficType.setStatus("mandatory")


class _TpTrafficDescriptorParam1_Type(Integer32):
    """Custom type tpTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TpTrafficDescriptorParam1_Type.__name__ = "Integer32"
_TpTrafficDescriptorParam1_Object = MibTableColumn
tpTrafficDescriptorParam1 = _TpTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 3),
    _TpTrafficDescriptorParam1_Type()
)
tpTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTrafficDescriptorParam1.setStatus("mandatory")


class _TpTrafficDescriptorParam2_Type(Integer32):
    """Custom type tpTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TpTrafficDescriptorParam2_Type.__name__ = "Integer32"
_TpTrafficDescriptorParam2_Object = MibTableColumn
tpTrafficDescriptorParam2 = _TpTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 4),
    _TpTrafficDescriptorParam2_Type()
)
tpTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTrafficDescriptorParam2.setStatus("mandatory")


class _TpTrafficDescriptorParam3_Type(Integer32):
    """Custom type tpTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TpTrafficDescriptorParam3_Type.__name__ = "Integer32"
_TpTrafficDescriptorParam3_Object = MibTableColumn
tpTrafficDescriptorParam3 = _TpTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 5),
    _TpTrafficDescriptorParam3_Type()
)
tpTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTrafficDescriptorParam3.setStatus("mandatory")


class _TpTrafficDescriptorParam4_Type(Integer32):
    """Custom type tpTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TpTrafficDescriptorParam4_Type.__name__ = "Integer32"
_TpTrafficDescriptorParam4_Object = MibTableColumn
tpTrafficDescriptorParam4 = _TpTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 6),
    _TpTrafficDescriptorParam4_Type()
)
tpTrafficDescriptorParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTrafficDescriptorParam4.setStatus("mandatory")


class _TpTrafficDescriptorParam5_Type(Integer32):
    """Custom type tpTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TpTrafficDescriptorParam5_Type.__name__ = "Integer32"
_TpTrafficDescriptorParam5_Object = MibTableColumn
tpTrafficDescriptorParam5 = _TpTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 7),
    _TpTrafficDescriptorParam5_Type()
)
tpTrafficDescriptorParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTrafficDescriptorParam5.setStatus("mandatory")
_TpQosClass_Type = QosClass
_TpQosClass_Object = MibTableColumn
tpQosClass = _TpQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 8),
    _TpQosClass_Type()
)
tpQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosClass.setStatus("mandatory")
_TpRowStatus_Type = RowStatus
_TpRowStatus_Object = MibTableColumn
tpRowStatus = _TpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 5, 1, 9),
    _TpRowStatus_Type()
)
tpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRowStatus.setStatus("mandatory")
_MapVapTrafficProfileMappingTable_Object = MibTable
mapVapTrafficProfileMappingTable = _MapVapTrafficProfileMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mapVapTrafficProfileMappingTable.setStatus("mandatory")
_MapVapTrafficProfileMappingEntry_Object = MibTableRow
mapVapTrafficProfileMappingEntry = _MapVapTrafficProfileMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1)
)
mapVapTrafficProfileMappingEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "vapIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "mapMappingIndex"),
)
if mibBuilder.loadTexts:
    mapVapTrafficProfileMappingEntry.setStatus("mandatory")


class _MapMappingIndex_Type(Integer32):
    """Custom type mapMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MapMappingIndex_Type.__name__ = "Integer32"
_MapMappingIndex_Object = MibTableColumn
mapMappingIndex = _MapMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 1),
    _MapMappingIndex_Type()
)
mapMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mapMappingIndex.setStatus("mandatory")
_MapTargetAtmAddress_Type = AtmAddress
_MapTargetAtmAddress_Object = MibTableColumn
mapTargetAtmAddress = _MapTargetAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 2),
    _MapTargetAtmAddress_Type()
)
mapTargetAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTargetAtmAddress.setStatus("mandatory")
_MapAddressMask_Type = AtmAddress
_MapAddressMask_Object = MibTableColumn
mapAddressMask = _MapAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 3),
    _MapAddressMask_Type()
)
mapAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapAddressMask.setStatus("mandatory")


class _MapVccType_Type(Integer32):
    """Custom type mapVccType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dataDirectVcc", 1),
          ("controlDirectVcc", 2),
          ("controlDistributeVcc", 3),
          ("multicastSendVcc", 4),
          ("multicastForwardVcc", 5),
          ("anyType", 6))
    )


_MapVccType_Type.__name__ = "Integer32"
_MapVccType_Object = MibTableColumn
mapVccType = _MapVccType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 4),
    _MapVccType_Type()
)
mapVccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapVccType.setStatus("mandatory")


class _MapTableProfile0Index_Type(Integer32):
    """Custom type mapTableProfile0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile0Index_Type.__name__ = "Integer32"
_MapTableProfile0Index_Object = MibTableColumn
mapTableProfile0Index = _MapTableProfile0Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 5),
    _MapTableProfile0Index_Type()
)
mapTableProfile0Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile0Index.setStatus("mandatory")


class _MapTableProfile1Index_Type(Integer32):
    """Custom type mapTableProfile1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile1Index_Type.__name__ = "Integer32"
_MapTableProfile1Index_Object = MibTableColumn
mapTableProfile1Index = _MapTableProfile1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 6),
    _MapTableProfile1Index_Type()
)
mapTableProfile1Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile1Index.setStatus("mandatory")


class _MapTableProfile2Index_Type(Integer32):
    """Custom type mapTableProfile2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile2Index_Type.__name__ = "Integer32"
_MapTableProfile2Index_Object = MibTableColumn
mapTableProfile2Index = _MapTableProfile2Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 7),
    _MapTableProfile2Index_Type()
)
mapTableProfile2Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile2Index.setStatus("mandatory")


class _MapTableProfile3Index_Type(Integer32):
    """Custom type mapTableProfile3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile3Index_Type.__name__ = "Integer32"
_MapTableProfile3Index_Object = MibTableColumn
mapTableProfile3Index = _MapTableProfile3Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 8),
    _MapTableProfile3Index_Type()
)
mapTableProfile3Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile3Index.setStatus("mandatory")


class _MapTableProfile4Index_Type(Integer32):
    """Custom type mapTableProfile4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile4Index_Type.__name__ = "Integer32"
_MapTableProfile4Index_Object = MibTableColumn
mapTableProfile4Index = _MapTableProfile4Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 9),
    _MapTableProfile4Index_Type()
)
mapTableProfile4Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile4Index.setStatus("mandatory")


class _MapTableProfile5Index_Type(Integer32):
    """Custom type mapTableProfile5Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile5Index_Type.__name__ = "Integer32"
_MapTableProfile5Index_Object = MibTableColumn
mapTableProfile5Index = _MapTableProfile5Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 10),
    _MapTableProfile5Index_Type()
)
mapTableProfile5Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile5Index.setStatus("mandatory")


class _MapTableProfile6Index_Type(Integer32):
    """Custom type mapTableProfile6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile6Index_Type.__name__ = "Integer32"
_MapTableProfile6Index_Object = MibTableColumn
mapTableProfile6Index = _MapTableProfile6Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 11),
    _MapTableProfile6Index_Type()
)
mapTableProfile6Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile6Index.setStatus("mandatory")


class _MapTableProfile7Index_Type(Integer32):
    """Custom type mapTableProfile7Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile7Index_Type.__name__ = "Integer32"
_MapTableProfile7Index_Object = MibTableColumn
mapTableProfile7Index = _MapTableProfile7Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 12),
    _MapTableProfile7Index_Type()
)
mapTableProfile7Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile7Index.setStatus("mandatory")


class _MapTableProfile8Index_Type(Integer32):
    """Custom type mapTableProfile8Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile8Index_Type.__name__ = "Integer32"
_MapTableProfile8Index_Object = MibTableColumn
mapTableProfile8Index = _MapTableProfile8Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 13),
    _MapTableProfile8Index_Type()
)
mapTableProfile8Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile8Index.setStatus("mandatory")


class _MapTableProfile9Index_Type(Integer32):
    """Custom type mapTableProfile9Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MapTableProfile9Index_Type.__name__ = "Integer32"
_MapTableProfile9Index_Object = MibTableColumn
mapTableProfile9Index = _MapTableProfile9Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 14),
    _MapTableProfile9Index_Type()
)
mapTableProfile9Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapTableProfile9Index.setStatus("mandatory")
_MapRowStatus_Type = RowStatus
_MapRowStatus_Object = MibTableColumn
mapRowStatus = _MapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 6, 1, 15),
    _MapRowStatus_Type()
)
mapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapRowStatus.setStatus("mandatory")
_SignallingConfigTable_Object = MibTable
signallingConfigTable = _SignallingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7)
)
if mibBuilder.loadTexts:
    signallingConfigTable.setStatus("mandatory")
_SignallingConfigEntry_Object = MibTableRow
signallingConfigEntry = _SignallingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1)
)
signallingConfigEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    signallingConfigEntry.setStatus("mandatory")


class _ConfigSigMaxSigProtStevs_Type(Integer32):
    """Custom type configSigMaxSigProtStevs based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ConfigSigMaxSigProtStevs_Type.__name__ = "Integer32"
_ConfigSigMaxSigProtStevs_Object = MibTableColumn
configSigMaxSigProtStevs = _ConfigSigMaxSigProtStevs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 1),
    _ConfigSigMaxSigProtStevs_Type()
)
configSigMaxSigProtStevs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigMaxSigProtStevs.setStatus("mandatory")


class _ConfigSigT301_Type(Integer32):
    """Custom type configSigT301 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigSigT301_Type.__name__ = "Integer32"
_ConfigSigT301_Object = MibTableColumn
configSigT301 = _ConfigSigT301_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 2),
    _ConfigSigT301_Type()
)
configSigT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT301.setStatus("mandatory")


class _ConfigSigT303_Type(Integer32):
    """Custom type configSigT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT303_Type.__name__ = "Integer32"
_ConfigSigT303_Object = MibTableColumn
configSigT303 = _ConfigSigT303_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 3),
    _ConfigSigT303_Type()
)
configSigT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT303.setStatus("mandatory")


class _ConfigSigT308_Type(Integer32):
    """Custom type configSigT308 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT308_Type.__name__ = "Integer32"
_ConfigSigT308_Object = MibTableColumn
configSigT308 = _ConfigSigT308_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 4),
    _ConfigSigT308_Type()
)
configSigT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT308.setStatus("mandatory")


class _ConfigSigT309_Type(Integer32):
    """Custom type configSigT309 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT309_Type.__name__ = "Integer32"
_ConfigSigT309_Object = MibTableColumn
configSigT309 = _ConfigSigT309_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 5),
    _ConfigSigT309_Type()
)
configSigT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT309.setStatus("mandatory")


class _ConfigSigT310_Type(Integer32):
    """Custom type configSigT310 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT310_Type.__name__ = "Integer32"
_ConfigSigT310_Object = MibTableColumn
configSigT310 = _ConfigSigT310_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 6),
    _ConfigSigT310_Type()
)
configSigT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT310.setStatus("mandatory")


class _ConfigSigT313_Type(Integer32):
    """Custom type configSigT313 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT313_Type.__name__ = "Integer32"
_ConfigSigT313_Object = MibTableColumn
configSigT313 = _ConfigSigT313_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 7),
    _ConfigSigT313_Type()
)
configSigT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT313.setStatus("mandatory")


class _ConfigSigT316_Type(Integer32):
    """Custom type configSigT316 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT316_Type.__name__ = "Integer32"
_ConfigSigT316_Object = MibTableColumn
configSigT316 = _ConfigSigT316_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 8),
    _ConfigSigT316_Type()
)
configSigT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT316.setStatus("mandatory")


class _ConfigSigT317_Type(Integer32):
    """Custom type configSigT317 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT317_Type.__name__ = "Integer32"
_ConfigSigT317_Object = MibTableColumn
configSigT317 = _ConfigSigT317_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 9),
    _ConfigSigT317_Type()
)
configSigT317.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT317.setStatus("mandatory")


class _ConfigSigT322_Type(Integer32):
    """Custom type configSigT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSigT322_Type.__name__ = "Integer32"
_ConfigSigT322_Object = MibTableColumn
configSigT322 = _ConfigSigT322_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 7, 1, 10),
    _ConfigSigT322_Type()
)
configSigT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSigT322.setStatus("mandatory")
_SscopConfigTable_Object = MibTable
sscopConfigTable = _SscopConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8)
)
if mibBuilder.loadTexts:
    sscopConfigTable.setStatus("mandatory")
_SscopConfigEntry_Object = MibTableRow
sscopConfigEntry = _SscopConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1)
)
sscopConfigEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    sscopConfigEntry.setStatus("mandatory")


class _ConfigSscopMaxRcvWinSize_Type(Integer32):
    """Custom type configSscopMaxRcvWinSize based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ConfigSscopMaxRcvWinSize_Type.__name__ = "Integer32"
_ConfigSscopMaxRcvWinSize_Object = MibTableColumn
configSscopMaxRcvWinSize = _ConfigSscopMaxRcvWinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 1),
    _ConfigSscopMaxRcvWinSize_Type()
)
configSscopMaxRcvWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopMaxRcvWinSize.setStatus("mandatory")


class _ConfigSscopMaxCc_Type(Integer32):
    """Custom type configSscopMaxCc based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSscopMaxCc_Type.__name__ = "Integer32"
_ConfigSscopMaxCc_Object = MibTableColumn
configSscopMaxCc = _ConfigSscopMaxCc_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 2),
    _ConfigSscopMaxCc_Type()
)
configSscopMaxCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopMaxCc.setStatus("mandatory")


class _ConfigSscopMaxPd_Type(Integer32):
    """Custom type configSscopMaxPd based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSscopMaxPd_Type.__name__ = "Integer32"
_ConfigSscopMaxPd_Object = MibTableColumn
configSscopMaxPd = _ConfigSscopMaxPd_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 3),
    _ConfigSscopMaxPd_Type()
)
configSscopMaxPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopMaxPd.setStatus("mandatory")


class _ConfigSscopMaxStat_Type(Integer32):
    """Custom type configSscopMaxStat based on Integer32"""
    defaultValue = 67

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1023),
    )


_ConfigSscopMaxStat_Type.__name__ = "Integer32"
_ConfigSscopMaxStat_Object = MibTableColumn
configSscopMaxStat = _ConfigSscopMaxStat_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 4),
    _ConfigSscopMaxStat_Type()
)
configSscopMaxStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopMaxStat.setStatus("mandatory")


class _ConfigSscopTimerPoll_Type(Integer32):
    """Custom type configSscopTimerPoll based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ConfigSscopTimerPoll_Type.__name__ = "Integer32"
_ConfigSscopTimerPoll_Object = MibTableColumn
configSscopTimerPoll = _ConfigSscopTimerPoll_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 5),
    _ConfigSscopTimerPoll_Type()
)
configSscopTimerPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopTimerPoll.setStatus("mandatory")


class _ConfigSscopTimerNoResponse_Type(Integer32):
    """Custom type configSscopTimerNoResponse based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSscopTimerNoResponse_Type.__name__ = "Integer32"
_ConfigSscopTimerNoResponse_Object = MibTableColumn
configSscopTimerNoResponse = _ConfigSscopTimerNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 6),
    _ConfigSscopTimerNoResponse_Type()
)
configSscopTimerNoResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopTimerNoResponse.setStatus("mandatory")


class _ConfigSscopTimerKeepAlive_Type(Integer32):
    """Custom type configSscopTimerKeepAlive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSscopTimerKeepAlive_Type.__name__ = "Integer32"
_ConfigSscopTimerKeepAlive_Object = MibTableColumn
configSscopTimerKeepAlive = _ConfigSscopTimerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 7),
    _ConfigSscopTimerKeepAlive_Type()
)
configSscopTimerKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopTimerKeepAlive.setStatus("mandatory")


class _ConfigSscopTimerIdle_Type(Integer32):
    """Custom type configSscopTimerIdle based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSscopTimerIdle_Type.__name__ = "Integer32"
_ConfigSscopTimerIdle_Object = MibTableColumn
configSscopTimerIdle = _ConfigSscopTimerIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 8),
    _ConfigSscopTimerIdle_Type()
)
configSscopTimerIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopTimerIdle.setStatus("mandatory")


class _ConfigSscopTimerCc_Type(Integer32):
    """Custom type configSscopTimerCc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSscopTimerCc_Type.__name__ = "Integer32"
_ConfigSscopTimerCc_Object = MibTableColumn
configSscopTimerCc = _ConfigSscopTimerCc_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 9),
    _ConfigSscopTimerCc_Type()
)
configSscopTimerCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopTimerCc.setStatus("mandatory")


class _ConfigSscopMaxSduSize_Type(Integer32):
    """Custom type configSscopMaxSduSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_ConfigSscopMaxSduSize_Type.__name__ = "Integer32"
_ConfigSscopMaxSduSize_Object = MibTableColumn
configSscopMaxSduSize = _ConfigSscopMaxSduSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 10),
    _ConfigSscopMaxSduSize_Type()
)
configSscopMaxSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopMaxSduSize.setStatus("mandatory")


class _ConfigSscopMaxUuSize_Type(Integer32):
    """Custom type configSscopMaxUuSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_ConfigSscopMaxUuSize_Type.__name__ = "Integer32"
_ConfigSscopMaxUuSize_Object = MibTableColumn
configSscopMaxUuSize = _ConfigSscopMaxUuSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 2, 8, 1, 11),
    _ConfigSscopMaxUuSize_Type()
)
configSscopMaxUuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSscopMaxUuSize.setStatus("mandatory")
_AtmUplinkStatus_ObjectIdentity = ObjectIdentity
atmUplinkStatus = _AtmUplinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3)
)
_VccStatusTable_Object = MibTable
vccStatusTable = _VccStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vccStatusTable.setStatus("mandatory")
_VccStatusEntry_Object = MibTableRow
vccStatusEntry = _VccStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1)
)
vccStatusEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "vccVpi"),
    (0, "Cisco-trStackAtmUplink-MIB", "vccVci"),
)
if mibBuilder.loadTexts:
    vccStatusEntry.setStatus("mandatory")
_VccVpi_Type = VpiInteger
_VccVpi_Object = MibTableColumn
vccVpi = _VccVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 1),
    _VccVpi_Type()
)
vccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vccVpi.setStatus("mandatory")
_VccVci_Type = VciInteger
_VccVci_Object = MibTableColumn
vccVci = _VccVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 2),
    _VccVci_Type()
)
vccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vccVci.setStatus("mandatory")


class _VccUsage_Type(Integer32):
    """Custom type vccUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("sscop", 1),
          ("ilmi", 2),
          ("oam", 3),
          ("laneConfig", 4),
          ("laneControlDirect", 5),
          ("laneControlDistribute", 6),
          ("laneMulticastSend", 7),
          ("laneMulticastForward", 8),
          ("laneDataDirect", 9))
    )


_VccUsage_Type.__name__ = "Integer32"
_VccUsage_Object = MibTableColumn
vccUsage = _VccUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 3),
    _VccUsage_Type()
)
vccUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccUsage.setStatus("mandatory")
_VccInstance_Type = Integer32
_VccInstance_Object = MibTableColumn
vccInstance = _VccInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 4),
    _VccInstance_Type()
)
vccInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccInstance.setStatus("mandatory")


class _VccCreateMeans_Type(Integer32):
    """Custom type vccCreateMeans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("pvc", 2),
          ("incomingPoint2PointSvc", 3),
          ("outgoingPoint2PointSvc", 4),
          ("incomingPoint2MultipointSvc", 5),
          ("outgoingPoint2MultipointSvc", 6))
    )


_VccCreateMeans_Type.__name__ = "Integer32"
_VccCreateMeans_Object = MibTableColumn
vccCreateMeans = _VccCreateMeans_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 5),
    _VccCreateMeans_Type()
)
vccCreateMeans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccCreateMeans.setStatus("mandatory")
_VccTxTrafficDescriptorType_Type = TrafficDescrType
_VccTxTrafficDescriptorType_Object = MibTableColumn
vccTxTrafficDescriptorType = _VccTxTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 6),
    _VccTxTrafficDescriptorType_Type()
)
vccTxTrafficDescriptorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxTrafficDescriptorType.setStatus("mandatory")


class _VccTxTrafficDescriptorParam1_Type(Integer32):
    """Custom type vccTxTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VccTxTrafficDescriptorParam1_Type.__name__ = "Integer32"
_VccTxTrafficDescriptorParam1_Object = MibTableColumn
vccTxTrafficDescriptorParam1 = _VccTxTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 7),
    _VccTxTrafficDescriptorParam1_Type()
)
vccTxTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxTrafficDescriptorParam1.setStatus("mandatory")


class _VccTxTrafficDescriptorParam2_Type(Integer32):
    """Custom type vccTxTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VccTxTrafficDescriptorParam2_Type.__name__ = "Integer32"
_VccTxTrafficDescriptorParam2_Object = MibTableColumn
vccTxTrafficDescriptorParam2 = _VccTxTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 8),
    _VccTxTrafficDescriptorParam2_Type()
)
vccTxTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxTrafficDescriptorParam2.setStatus("mandatory")


class _VccTxTrafficDescriptorParam3_Type(Integer32):
    """Custom type vccTxTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VccTxTrafficDescriptorParam3_Type.__name__ = "Integer32"
_VccTxTrafficDescriptorParam3_Object = MibTableColumn
vccTxTrafficDescriptorParam3 = _VccTxTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 9),
    _VccTxTrafficDescriptorParam3_Type()
)
vccTxTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxTrafficDescriptorParam3.setStatus("mandatory")


class _VccTxTrafficDescriptorParam4_Type(Integer32):
    """Custom type vccTxTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VccTxTrafficDescriptorParam4_Type.__name__ = "Integer32"
_VccTxTrafficDescriptorParam4_Object = MibTableColumn
vccTxTrafficDescriptorParam4 = _VccTxTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 10),
    _VccTxTrafficDescriptorParam4_Type()
)
vccTxTrafficDescriptorParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxTrafficDescriptorParam4.setStatus("mandatory")


class _VccTxTrafficDescriptorParam5_Type(Integer32):
    """Custom type vccTxTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VccTxTrafficDescriptorParam5_Type.__name__ = "Integer32"
_VccTxTrafficDescriptorParam5_Object = MibTableColumn
vccTxTrafficDescriptorParam5 = _VccTxTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 11),
    _VccTxTrafficDescriptorParam5_Type()
)
vccTxTrafficDescriptorParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxTrafficDescriptorParam5.setStatus("mandatory")
_VccTxQosClass_Type = QosClass
_VccTxQosClass_Object = MibTableColumn
vccTxQosClass = _VccTxQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 12),
    _VccTxQosClass_Type()
)
vccTxQosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxQosClass.setStatus("mandatory")
_VccTxFrameDiscard_Type = TruthValue
_VccTxFrameDiscard_Object = MibTableColumn
vccTxFrameDiscard = _VccTxFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 13),
    _VccTxFrameDiscard_Type()
)
vccTxFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxFrameDiscard.setStatus("mandatory")


class _VccServiceCategory_Type(Integer32):
    """Custom type vccServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("cbr", 2),
          ("rtVbr", 3),
          ("nrtVbr", 4),
          ("abr", 5),
          ("ubr", 6))
    )


_VccServiceCategory_Type.__name__ = "Integer32"
_VccServiceCategory_Object = MibTableColumn
vccServiceCategory = _VccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 14),
    _VccServiceCategory_Type()
)
vccServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccServiceCategory.setStatus("mandatory")
_VccAtmAddress_Type = AtmAddress
_VccAtmAddress_Object = MibTableColumn
vccAtmAddress = _VccAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 15),
    _VccAtmAddress_Type()
)
vccAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccAtmAddress.setStatus("mandatory")
_VccTxFrames_Type = Counter32
_VccTxFrames_Object = MibTableColumn
vccTxFrames = _VccTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 16),
    _VccTxFrames_Type()
)
vccTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxFrames.setStatus("mandatory")
_VccTxHighBytes_Type = Counter32
_VccTxHighBytes_Object = MibTableColumn
vccTxHighBytes = _VccTxHighBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 17),
    _VccTxHighBytes_Type()
)
vccTxHighBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxHighBytes.setStatus("mandatory")
_VccTxLowBytes_Type = Counter32
_VccTxLowBytes_Object = MibTableColumn
vccTxLowBytes = _VccTxLowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 18),
    _VccTxLowBytes_Type()
)
vccTxLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccTxLowBytes.setStatus("mandatory")
_VccRxFrames_Type = Counter32
_VccRxFrames_Object = MibTableColumn
vccRxFrames = _VccRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 19),
    _VccRxFrames_Type()
)
vccRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccRxFrames.setStatus("mandatory")
_VccRxHighBytes_Type = Counter32
_VccRxHighBytes_Object = MibTableColumn
vccRxHighBytes = _VccRxHighBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 20),
    _VccRxHighBytes_Type()
)
vccRxHighBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccRxHighBytes.setStatus("mandatory")
_VccRxLowBytes_Type = Counter32
_VccRxLowBytes_Object = MibTableColumn
vccRxLowBytes = _VccRxLowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 1, 1, 21),
    _VccRxLowBytes_Type()
)
vccRxLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccRxLowBytes.setStatus("mandatory")
_MacAddressConnectionTable_Object = MibTable
macAddressConnectionTable = _MacAddressConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    macAddressConnectionTable.setStatus("mandatory")
_MacAddressConnectionEntry_Object = MibTableRow
macAddressConnectionEntry = _MacAddressConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 2, 1)
)
macAddressConnectionEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "vapIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "macAddress"),
)
if mibBuilder.loadTexts:
    macAddressConnectionEntry.setStatus("mandatory")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 2, 1, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAddress.setStatus("mandatory")
_MacVpi_Type = VpiInteger
_MacVpi_Object = MibTableColumn
macVpi = _MacVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 2, 1, 2),
    _MacVpi_Type()
)
macVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVpi.setStatus("mandatory")
_MacVci_Type = VciInteger
_MacVci_Object = MibTableColumn
macVci = _MacVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 2, 1, 3),
    _MacVci_Type()
)
macVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVci.setStatus("mandatory")
_LogMessageTable_Object = MibTable
logMessageTable = _LogMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    logMessageTable.setStatus("mandatory")
_LogMessageEntry_Object = MibTableRow
logMessageEntry = _LogMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 3, 1)
)
logMessageEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "logMessageIndex"),
)
if mibBuilder.loadTexts:
    logMessageEntry.setStatus("mandatory")


class _LogMessageIndex_Type(Integer32):
    """Custom type logMessageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LogMessageIndex_Type.__name__ = "Integer32"
_LogMessageIndex_Object = MibTableColumn
logMessageIndex = _LogMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 3, 1, 1),
    _LogMessageIndex_Type()
)
logMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logMessageIndex.setStatus("mandatory")
_LogMessageTime_Type = TimeTicks
_LogMessageTime_Object = MibTableColumn
logMessageTime = _LogMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 3, 1, 2),
    _LogMessageTime_Type()
)
logMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMessageTime.setStatus("mandatory")
_LogMessageText_Type = DisplayString
_LogMessageText_Object = MibTableColumn
logMessageText = _LogMessageText_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 3, 1, 3),
    _LogMessageText_Type()
)
logMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMessageText.setStatus("mandatory")
_LedStatusTable_Object = MibTable
ledStatusTable = _LedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ledStatusTable.setStatus("mandatory")
_LedStatusEntry_Object = MibTableRow
ledStatusEntry = _LedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 4, 1)
)
ledStatusEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    ledStatusEntry.setStatus("mandatory")


class _LedDiag_Type(Integer32):
    """Custom type ledDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LedDiag_Type.__name__ = "Integer32"
_LedDiag_Object = MibTableColumn
ledDiag = _LedDiag_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 4, 1, 1),
    _LedDiag_Type()
)
ledDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledDiag.setStatus("mandatory")


class _LedError_Type(Integer32):
    """Custom type ledError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LedError_Type.__name__ = "Integer32"
_LedError_Object = MibTableColumn
ledError = _LedError_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 4, 1, 2),
    _LedError_Type()
)
ledError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledError.setStatus("mandatory")


class _LedSigLoss_Type(Integer32):
    """Custom type ledSigLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LedSigLoss_Type.__name__ = "Integer32"
_LedSigLoss_Object = MibTableColumn
ledSigLoss = _LedSigLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 4, 1, 3),
    _LedSigLoss_Type()
)
ledSigLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledSigLoss.setStatus("mandatory")


class _LedRxSync_Type(Integer32):
    """Custom type ledRxSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LedRxSync_Type.__name__ = "Integer32"
_LedRxSync_Object = MibTableColumn
ledRxSync = _LedRxSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 3, 4, 1, 4),
    _LedRxSync_Type()
)
ledRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledRxSync.setStatus("mandatory")
_AtmUplinkStatistics_ObjectIdentity = ObjectIdentity
atmUplinkStatistics = _AtmUplinkStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4)
)
_VapFrameFwStatisticsTable_Object = MibTable
vapFrameFwStatisticsTable = _VapFrameFwStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vapFrameFwStatisticsTable.setStatus("mandatory")
_VapFrameFwStatisticsEntry_Object = MibTableRow
vapFrameFwStatisticsEntry = _VapFrameFwStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1)
)
vapFrameFwStatisticsEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "vapIndex"),
)
if mibBuilder.loadTexts:
    vapFrameFwStatisticsEntry.setStatus("mandatory")
_VapFfsIdfInvalidRoutes_Type = Counter32
_VapFfsIdfInvalidRoutes_Object = MibTableColumn
vapFfsIdfInvalidRoutes = _VapFfsIdfInvalidRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 1),
    _VapFfsIdfInvalidRoutes_Type()
)
vapFfsIdfInvalidRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfInvalidRoutes.setStatus("mandatory")
_VapFfsIdfRingNumberMismatches_Type = Counter32
_VapFfsIdfRingNumberMismatches_Object = MibTableColumn
vapFfsIdfRingNumberMismatches = _VapFfsIdfRingNumberMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 2),
    _VapFfsIdfRingNumberMismatches_Type()
)
vapFfsIdfRingNumberMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfRingNumberMismatches.setStatus("mandatory")
_VapFfsIdfDuplicateRingNumbers_Type = Counter32
_VapFfsIdfDuplicateRingNumbers_Object = MibTableColumn
vapFfsIdfDuplicateRingNumbers = _VapFfsIdfDuplicateRingNumbers_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 3),
    _VapFfsIdfDuplicateRingNumbers_Type()
)
vapFfsIdfDuplicateRingNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfDuplicateRingNumbers.setStatus("mandatory")
_VapFfsIdfTooLargeFrames_Type = Counter32
_VapFfsIdfTooLargeFrames_Object = MibTableColumn
vapFfsIdfTooLargeFrames = _VapFfsIdfTooLargeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 4),
    _VapFfsIdfTooLargeFrames_Type()
)
vapFfsIdfTooLargeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfTooLargeFrames.setStatus("mandatory")
_VapFfsIdfTooLongRouteDescriptors_Type = Counter32
_VapFfsIdfTooLongRouteDescriptors_Object = MibTableColumn
vapFfsIdfTooLongRouteDescriptors = _VapFfsIdfTooLongRouteDescriptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 5),
    _VapFfsIdfTooLongRouteDescriptors_Type()
)
vapFfsIdfTooLongRouteDescriptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfTooLongRouteDescriptors.setStatus("mandatory")
_VapFfsIdfBlockedByMacAddressFilters_Type = Counter32
_VapFfsIdfBlockedByMacAddressFilters_Object = MibTableColumn
vapFfsIdfBlockedByMacAddressFilters = _VapFfsIdfBlockedByMacAddressFilters_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 6),
    _VapFfsIdfBlockedByMacAddressFilters_Type()
)
vapFfsIdfBlockedByMacAddressFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfBlockedByMacAddressFilters.setStatus("mandatory")
_VapFfsIdfBlockedBySapFilters_Type = Counter32
_VapFfsIdfBlockedBySapFilters_Object = MibTableColumn
vapFfsIdfBlockedBySapFilters = _VapFfsIdfBlockedBySapFilters_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 7),
    _VapFfsIdfBlockedBySapFilters_Type()
)
vapFfsIdfBlockedBySapFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfBlockedBySapFilters.setStatus("mandatory")
_VapFfsIdfCRFMismatches_Type = Counter32
_VapFfsIdfCRFMismatches_Object = MibTableColumn
vapFfsIdfCRFMismatches = _VapFfsIdfCRFMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 8),
    _VapFfsIdfCRFMismatches_Type()
)
vapFfsIdfCRFMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfCRFMismatches.setStatus("mandatory")
_VapFfsIdfExplorerOverflows_Type = Counter32
_VapFfsIdfExplorerOverflows_Object = MibTableColumn
vapFfsIdfExplorerOverflows = _VapFfsIdfExplorerOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 9),
    _VapFfsIdfExplorerOverflows_Type()
)
vapFfsIdfExplorerOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsIdfExplorerOverflows.setStatus("mandatory")
_VapFfsUfNonSourceRoutedFrames_Type = Counter32
_VapFfsUfNonSourceRoutedFrames_Object = MibTableColumn
vapFfsUfNonSourceRoutedFrames = _VapFfsUfNonSourceRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 10),
    _VapFfsUfNonSourceRoutedFrames_Type()
)
vapFfsUfNonSourceRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsUfNonSourceRoutedFrames.setStatus("mandatory")
_VapFfsUfSpecificallyRoutedFrames_Type = Counter32
_VapFfsUfSpecificallyRoutedFrames_Object = MibTableColumn
vapFfsUfSpecificallyRoutedFrames = _VapFfsUfSpecificallyRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 11),
    _VapFfsUfSpecificallyRoutedFrames_Type()
)
vapFfsUfSpecificallyRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsUfSpecificallyRoutedFrames.setStatus("mandatory")
_VapFfsUfSTEFrames_Type = Counter32
_VapFfsUfSTEFrames_Object = MibTableColumn
vapFfsUfSTEFrames = _VapFfsUfSTEFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 12),
    _VapFfsUfSTEFrames_Type()
)
vapFfsUfSTEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsUfSTEFrames.setStatus("mandatory")
_VapFfsUfAREFrames_Type = Counter32
_VapFfsUfAREFrames_Object = MibTableColumn
vapFfsUfAREFrames = _VapFfsUfAREFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 13),
    _VapFfsUfAREFrames_Type()
)
vapFfsUfAREFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsUfAREFrames.setStatus("mandatory")
_VapFfsBfNonSourceRoutedFrames_Type = Counter32
_VapFfsBfNonSourceRoutedFrames_Object = MibTableColumn
vapFfsBfNonSourceRoutedFrames = _VapFfsBfNonSourceRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 14),
    _VapFfsBfNonSourceRoutedFrames_Type()
)
vapFfsBfNonSourceRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsBfNonSourceRoutedFrames.setStatus("mandatory")
_VapFfsBfSpecificallyRoutedFrames_Type = Counter32
_VapFfsBfSpecificallyRoutedFrames_Object = MibTableColumn
vapFfsBfSpecificallyRoutedFrames = _VapFfsBfSpecificallyRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 15),
    _VapFfsBfSpecificallyRoutedFrames_Type()
)
vapFfsBfSpecificallyRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsBfSpecificallyRoutedFrames.setStatus("mandatory")
_VapFfsBfSTEFrames_Type = Counter32
_VapFfsBfSTEFrames_Object = MibTableColumn
vapFfsBfSTEFrames = _VapFfsBfSTEFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 16),
    _VapFfsBfSTEFrames_Type()
)
vapFfsBfSTEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsBfSTEFrames.setStatus("mandatory")
_VapFfsBfAREFrames_Type = Counter32
_VapFfsBfAREFrames_Object = MibTableColumn
vapFfsBfAREFrames = _VapFfsBfAREFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 17),
    _VapFfsBfAREFrames_Type()
)
vapFfsBfAREFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsBfAREFrames.setStatus("mandatory")
_VapFfsMfNonSourceRoutedFrames_Type = Counter32
_VapFfsMfNonSourceRoutedFrames_Object = MibTableColumn
vapFfsMfNonSourceRoutedFrames = _VapFfsMfNonSourceRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 18),
    _VapFfsMfNonSourceRoutedFrames_Type()
)
vapFfsMfNonSourceRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsMfNonSourceRoutedFrames.setStatus("mandatory")
_VapFfsMfSpecificallyRoutedFrames_Type = Counter32
_VapFfsMfSpecificallyRoutedFrames_Object = MibTableColumn
vapFfsMfSpecificallyRoutedFrames = _VapFfsMfSpecificallyRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 19),
    _VapFfsMfSpecificallyRoutedFrames_Type()
)
vapFfsMfSpecificallyRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsMfSpecificallyRoutedFrames.setStatus("mandatory")
_VapFfsMfSTEFrames_Type = Counter32
_VapFfsMfSTEFrames_Object = MibTableColumn
vapFfsMfSTEFrames = _VapFfsMfSTEFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 20),
    _VapFfsMfSTEFrames_Type()
)
vapFfsMfSTEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsMfSTEFrames.setStatus("mandatory")
_VapFfsMfAREFrames_Type = Counter32
_VapFfsMfAREFrames_Object = MibTableColumn
vapFfsMfAREFrames = _VapFfsMfAREFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 21),
    _VapFfsMfAREFrames_Type()
)
vapFfsMfAREFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsMfAREFrames.setStatus("mandatory")
_VapFfsReceivedHighBytes_Type = Counter32
_VapFfsReceivedHighBytes_Object = MibTableColumn
vapFfsReceivedHighBytes = _VapFfsReceivedHighBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 22),
    _VapFfsReceivedHighBytes_Type()
)
vapFfsReceivedHighBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsReceivedHighBytes.setStatus("mandatory")
_VapFfsReceivedLowBytes_Type = Counter32
_VapFfsReceivedLowBytes_Object = MibTableColumn
vapFfsReceivedLowBytes = _VapFfsReceivedLowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 23),
    _VapFfsReceivedLowBytes_Type()
)
vapFfsReceivedLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsReceivedLowBytes.setStatus("mandatory")
_VapFfsFfNonSourceRoutedFrames_Type = Counter32
_VapFfsFfNonSourceRoutedFrames_Object = MibTableColumn
vapFfsFfNonSourceRoutedFrames = _VapFfsFfNonSourceRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 24),
    _VapFfsFfNonSourceRoutedFrames_Type()
)
vapFfsFfNonSourceRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsFfNonSourceRoutedFrames.setStatus("mandatory")
_VapFfsFfSpecificallyRoutedFrames_Type = Counter32
_VapFfsFfSpecificallyRoutedFrames_Object = MibTableColumn
vapFfsFfSpecificallyRoutedFrames = _VapFfsFfSpecificallyRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 25),
    _VapFfsFfSpecificallyRoutedFrames_Type()
)
vapFfsFfSpecificallyRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsFfSpecificallyRoutedFrames.setStatus("mandatory")
_VapFfsFfSTEFrames_Type = Counter32
_VapFfsFfSTEFrames_Object = MibTableColumn
vapFfsFfSTEFrames = _VapFfsFfSTEFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 26),
    _VapFfsFfSTEFrames_Type()
)
vapFfsFfSTEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsFfSTEFrames.setStatus("mandatory")
_VapFfsFfAREFrames_Type = Counter32
_VapFfsFfAREFrames_Object = MibTableColumn
vapFfsFfAREFrames = _VapFfsFfAREFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 27),
    _VapFfsFfAREFrames_Type()
)
vapFfsFfAREFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsFfAREFrames.setStatus("mandatory")
_VapFfsForwardedHighBytes_Type = Counter32
_VapFfsForwardedHighBytes_Object = MibTableColumn
vapFfsForwardedHighBytes = _VapFfsForwardedHighBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 28),
    _VapFfsForwardedHighBytes_Type()
)
vapFfsForwardedHighBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsForwardedHighBytes.setStatus("mandatory")
_VapFfsForwardedLowBytes_Type = Counter32
_VapFfsForwardedLowBytes_Object = MibTableColumn
vapFfsForwardedLowBytes = _VapFfsForwardedLowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 29),
    _VapFfsForwardedLowBytes_Type()
)
vapFfsForwardedLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsForwardedLowBytes.setStatus("mandatory")
_VapFfsOdfInactiveVaps_Type = Counter32
_VapFfsOdfInactiveVaps_Object = MibTableColumn
vapFfsOdfInactiveVaps = _VapFfsOdfInactiveVaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 30),
    _VapFfsOdfInactiveVaps_Type()
)
vapFfsOdfInactiveVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsOdfInactiveVaps.setStatus("mandatory")
_VapFfsOdfBlockedVaps_Type = Counter32
_VapFfsOdfBlockedVaps_Object = MibTableColumn
vapFfsOdfBlockedVaps = _VapFfsOdfBlockedVaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 31),
    _VapFfsOdfBlockedVaps_Type()
)
vapFfsOdfBlockedVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsOdfBlockedVaps.setStatus("mandatory")
_VapFfsOdfBlockedBySapFilters_Type = Counter32
_VapFfsOdfBlockedBySapFilters_Object = MibTableColumn
vapFfsOdfBlockedBySapFilters = _VapFfsOdfBlockedBySapFilters_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 32),
    _VapFfsOdfBlockedBySapFilters_Type()
)
vapFfsOdfBlockedBySapFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsOdfBlockedBySapFilters.setStatus("mandatory")
_VapFfsOdfTooLargeFrames_Type = Counter32
_VapFfsOdfTooLargeFrames_Object = MibTableColumn
vapFfsOdfTooLargeFrames = _VapFfsOdfTooLargeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 33),
    _VapFfsOdfTooLargeFrames_Type()
)
vapFfsOdfTooLargeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsOdfTooLargeFrames.setStatus("mandatory")
_VapFfsTfNonSourceRoutedFrames_Type = Counter32
_VapFfsTfNonSourceRoutedFrames_Object = MibTableColumn
vapFfsTfNonSourceRoutedFrames = _VapFfsTfNonSourceRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 34),
    _VapFfsTfNonSourceRoutedFrames_Type()
)
vapFfsTfNonSourceRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsTfNonSourceRoutedFrames.setStatus("mandatory")
_VapFfsTfSpecificallyRoutedFrames_Type = Counter32
_VapFfsTfSpecificallyRoutedFrames_Object = MibTableColumn
vapFfsTfSpecificallyRoutedFrames = _VapFfsTfSpecificallyRoutedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 35),
    _VapFfsTfSpecificallyRoutedFrames_Type()
)
vapFfsTfSpecificallyRoutedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsTfSpecificallyRoutedFrames.setStatus("mandatory")
_VapFfsTfSTEFrames_Type = Counter32
_VapFfsTfSTEFrames_Object = MibTableColumn
vapFfsTfSTEFrames = _VapFfsTfSTEFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 36),
    _VapFfsTfSTEFrames_Type()
)
vapFfsTfSTEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsTfSTEFrames.setStatus("mandatory")
_VapFfsTfAREFrames_Type = Counter32
_VapFfsTfAREFrames_Object = MibTableColumn
vapFfsTfAREFrames = _VapFfsTfAREFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 37),
    _VapFfsTfAREFrames_Type()
)
vapFfsTfAREFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsTfAREFrames.setStatus("mandatory")
_VapFfsTransmittedHighBytes_Type = Counter32
_VapFfsTransmittedHighBytes_Object = MibTableColumn
vapFfsTransmittedHighBytes = _VapFfsTransmittedHighBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 38),
    _VapFfsTransmittedHighBytes_Type()
)
vapFfsTransmittedHighBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsTransmittedHighBytes.setStatus("mandatory")
_VapFfsTransmittedLowBytes_Type = Counter32
_VapFfsTransmittedLowBytes_Object = MibTableColumn
vapFfsTransmittedLowBytes = _VapFfsTransmittedLowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 39),
    _VapFfsTransmittedLowBytes_Type()
)
vapFfsTransmittedLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsTransmittedLowBytes.setStatus("mandatory")
_VapFfsLastResetTime_Type = TimeTicks
_VapFfsLastResetTime_Object = MibTableColumn
vapFfsLastResetTime = _VapFfsLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 1, 1, 40),
    _VapFfsLastResetTime_Type()
)
vapFfsLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapFfsLastResetTime.setStatus("mandatory")
_VapLaneStatisticsTable_Object = MibTable
vapLaneStatisticsTable = _VapLaneStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 2)
)
if mibBuilder.loadTexts:
    vapLaneStatisticsTable.setStatus("mandatory")
_VapLaneStatisticsEntry_Object = MibTableRow
vapLaneStatisticsEntry = _VapLaneStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 2, 1)
)
vapLaneStatisticsEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
    (0, "Cisco-trStackAtmUplink-MIB", "vapIndex"),
)
if mibBuilder.loadTexts:
    vapLaneStatisticsEntry.setStatus("mandatory")
_VapLsLeastActiveVccDisconnectedEvents_Type = Counter32
_VapLsLeastActiveVccDisconnectedEvents_Object = MibTableColumn
vapLsLeastActiveVccDisconnectedEvents = _VapLsLeastActiveVccDisconnectedEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 2, 1, 1),
    _VapLsLeastActiveVccDisconnectedEvents_Type()
)
vapLsLeastActiveVccDisconnectedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapLsLeastActiveVccDisconnectedEvents.setStatus("mandatory")
_VapLsNoLeastActiveVccFoundEvents_Type = Counter32
_VapLsNoLeastActiveVccFoundEvents_Object = MibTableColumn
vapLsNoLeastActiveVccFoundEvents = _VapLsNoLeastActiveVccFoundEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 2, 1, 2),
    _VapLsNoLeastActiveVccFoundEvents_Type()
)
vapLsNoLeastActiveVccFoundEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapLsNoLeastActiveVccFoundEvents.setStatus("mandatory")
_VapLsLastResetTime_Type = TimeTicks
_VapLsLastResetTime_Object = MibTableColumn
vapLsLastResetTime = _VapLsLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 2, 1, 3),
    _VapLsLastResetTime_Type()
)
vapLsLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapLsLastResetTime.setStatus("mandatory")
_GlobalOutboundStatTable_Object = MibTable
globalOutboundStatTable = _GlobalOutboundStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 3)
)
if mibBuilder.loadTexts:
    globalOutboundStatTable.setStatus("mandatory")
_GlobalOutboundStatEntry_Object = MibTableRow
globalOutboundStatEntry = _GlobalOutboundStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 3, 1)
)
globalOutboundStatEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    globalOutboundStatEntry.setStatus("mandatory")
_OutboundDfBadChannels_Type = Counter32
_OutboundDfBadChannels_Object = MibTableColumn
outboundDfBadChannels = _OutboundDfBadChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 3, 1, 1),
    _OutboundDfBadChannels_Type()
)
outboundDfBadChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundDfBadChannels.setStatus("mandatory")
_OutboundDfInvalidTags_Type = Counter32
_OutboundDfInvalidTags_Object = MibTableColumn
outboundDfInvalidTags = _OutboundDfInvalidTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 3, 1, 2),
    _OutboundDfInvalidTags_Type()
)
outboundDfInvalidTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundDfInvalidTags.setStatus("mandatory")
_OutboundStatLastResetTime_Type = TimeTicks
_OutboundStatLastResetTime_Object = MibTableColumn
outboundStatLastResetTime = _OutboundStatLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 3, 1, 3),
    _OutboundStatLastResetTime_Type()
)
outboundStatLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundStatLastResetTime.setStatus("mandatory")
_AtmDiagnosticsTable_Object = MibTable
atmDiagnosticsTable = _AtmDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4)
)
if mibBuilder.loadTexts:
    atmDiagnosticsTable.setStatus("mandatory")
_AtmDiagnosticsEntry_Object = MibTableRow
atmDiagnosticsEntry = _AtmDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1)
)
atmDiagnosticsEntry.setIndexNames(
    (0, "Cisco-trStackAtmUplink-MIB", "atmUplinkModuleIndex"),
)
if mibBuilder.loadTexts:
    atmDiagnosticsEntry.setStatus("mandatory")
_AtmDiagsDroppedPackets_Type = Counter32
_AtmDiagsDroppedPackets_Object = MibTableColumn
atmDiagsDroppedPackets = _AtmDiagsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 1),
    _AtmDiagsDroppedPackets_Type()
)
atmDiagsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsDroppedPackets.setStatus("mandatory")
_AtmDiagsCrcErrors_Type = Counter32
_AtmDiagsCrcErrors_Object = MibTableColumn
atmDiagsCrcErrors = _AtmDiagsCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 2),
    _AtmDiagsCrcErrors_Type()
)
atmDiagsCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsCrcErrors.setStatus("mandatory")
_AtmDiagsOverflows_Type = Counter32
_AtmDiagsOverflows_Object = MibTableColumn
atmDiagsOverflows = _AtmDiagsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 3),
    _AtmDiagsOverflows_Type()
)
atmDiagsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsOverflows.setStatus("mandatory")
_AtmDiagsFrameTooLongErrors_Type = Counter32
_AtmDiagsFrameTooLongErrors_Object = MibTableColumn
atmDiagsFrameTooLongErrors = _AtmDiagsFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 4),
    _AtmDiagsFrameTooLongErrors_Type()
)
atmDiagsFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsFrameTooLongErrors.setStatus("mandatory")
_AtmDiagsFrameTooShortErrors_Type = Counter32
_AtmDiagsFrameTooShortErrors_Object = MibTableColumn
atmDiagsFrameTooShortErrors = _AtmDiagsFrameTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 5),
    _AtmDiagsFrameTooShortErrors_Type()
)
atmDiagsFrameTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsFrameTooShortErrors.setStatus("mandatory")
_AtmDiagsUnknownVccErrors_Type = Counter32
_AtmDiagsUnknownVccErrors_Object = MibTableColumn
atmDiagsUnknownVccErrors = _AtmDiagsUnknownVccErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 6),
    _AtmDiagsUnknownVccErrors_Type()
)
atmDiagsUnknownVccErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsUnknownVccErrors.setStatus("mandatory")
_AtmDiagsReceivedHighBytes_Type = Counter32
_AtmDiagsReceivedHighBytes_Object = MibTableColumn
atmDiagsReceivedHighBytes = _AtmDiagsReceivedHighBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 7),
    _AtmDiagsReceivedHighBytes_Type()
)
atmDiagsReceivedHighBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsReceivedHighBytes.setStatus("mandatory")
_AtmDiagsReceivedLowBytes_Type = Counter32
_AtmDiagsReceivedLowBytes_Object = MibTableColumn
atmDiagsReceivedLowBytes = _AtmDiagsReceivedLowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 8),
    _AtmDiagsReceivedLowBytes_Type()
)
atmDiagsReceivedLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsReceivedLowBytes.setStatus("mandatory")
_AtmDiagsTransmittedHighBytes_Type = Counter32
_AtmDiagsTransmittedHighBytes_Object = MibTableColumn
atmDiagsTransmittedHighBytes = _AtmDiagsTransmittedHighBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 9),
    _AtmDiagsTransmittedHighBytes_Type()
)
atmDiagsTransmittedHighBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsTransmittedHighBytes.setStatus("mandatory")
_AtmDiagsTransmittedLowBytes_Type = Counter32
_AtmDiagsTransmittedLowBytes_Object = MibTableColumn
atmDiagsTransmittedLowBytes = _AtmDiagsTransmittedLowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 10),
    _AtmDiagsTransmittedLowBytes_Type()
)
atmDiagsTransmittedLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsTransmittedLowBytes.setStatus("mandatory")
_AtmDiagsLastResetTime_Type = TimeTicks
_AtmDiagsLastResetTime_Object = MibTableColumn
atmDiagsLastResetTime = _AtmDiagsLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9, 1, 4, 4, 1, 11),
    _AtmDiagsLastResetTime_Type()
)
atmDiagsLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiagsLastResetTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Cisco-trStackAtmUplink-MIB",
    **{"AtmAddress": AtmAddress,
       "MacAddress": MacAddress,
       "TruthValue": TruthValue,
       "ModuleInteger": ModuleInteger,
       "VapInteger": VapInteger,
       "VpiInteger": VpiInteger,
       "VciInteger": VciInteger,
       "RowStatus": RowStatus,
       "TrafficDescrType": TrafficDescrType,
       "QosClass": QosClass,
       "atm155MBUplinkMIB": atm155MBUplinkMIB,
       "atmUplinkInformation": atmUplinkInformation,
       "atmUplinkInfoTable": atmUplinkInfoTable,
       "atmUplinkInfoEntry": atmUplinkInfoEntry,
       "atmUplinkModuleIndex": atmUplinkModuleIndex,
       "infoHardwareProductId": infoHardwareProductId,
       "infoHardwareVersion": infoHardwareVersion,
       "infoHardwareECOLevel": infoHardwareECOLevel,
       "infoHardwareSerialNumber": infoHardwareSerialNumber,
       "infoSoftwareProductId": infoSoftwareProductId,
       "infoSoftwareVersion": infoSoftwareVersion,
       "infoSoftwareECOLevel": infoSoftwareECOLevel,
       "infoBootpromVersion": infoBootpromVersion,
       "atmUplinkConfiguration": atmUplinkConfiguration,
       "atmPortHwSetupTable": atmPortHwSetupTable,
       "atmPortHwSetupEntry": atmPortHwSetupEntry,
       "hwConfigMasterTiming": hwConfigMasterTiming,
       "hwConfigTcFramingMode": hwConfigTcFramingMode,
       "hwConfigEmptyCells": hwConfigEmptyCells,
       "commonVapParameterTable": commonVapParameterTable,
       "commonVapParameterEntry": commonVapParameterEntry,
       "configEnableSvcSupport": configEnableSvcSupport,
       "configIlmiAddressRegistrationSupport": configIlmiAddressRegistrationSupport,
       "configCommonNumberOfVccs": configCommonNumberOfVccs,
       "configCommonNumberOfDestinations": configCommonNumberOfDestinations,
       "configUniVersion": configUniVersion,
       "configMaxLineRate": configMaxLineRate,
       "configResetCounters": configResetCounters,
       "configModuleState": configModuleState,
       "vapConfigTable": vapConfigTable,
       "vapConfigEntry": vapConfigEntry,
       "vapIndex": vapIndex,
       "vapLecIndex": vapLecIndex,
       "vapAtmAddressAssignment": vapAtmAddressAssignment,
       "vapAtmAddress": vapAtmAddress,
       "vapLecsAtmAddress": vapLecsAtmAddress,
       "vapLecsVpi": vapLecsVpi,
       "vapLecsVci": vapLecsVci,
       "vapGuaranteedVccs": vapGuaranteedVccs,
       "vapGuaranteedDestinations": vapGuaranteedDestinations,
       "vapDefaultTrafficProfile": vapDefaultTrafficProfile,
       "vapMaxRxRateDifference": vapMaxRxRateDifference,
       "vapMaxTxRateDifference": vapMaxTxRateDifference,
       "vapTraceMask": vapTraceMask,
       "vapResetCounters": vapResetCounters,
       "vapResetAddrs": vapResetAddrs,
       "vapMaxExplorerRate": vapMaxExplorerRate,
       "vapSpanningTreeMode": vapSpanningTreeMode,
       "vapState": vapState,
       "pvcConfigTable": pvcConfigTable,
       "pvcConfigEntry": pvcConfigEntry,
       "pvcVpi": pvcVpi,
       "pvcVci": pvcVci,
       "pvcAtmAddress": pvcAtmAddress,
       "pvcType": pvcType,
       "pvcTrafficProfileIndex": pvcTrafficProfileIndex,
       "pvcVapIndex": pvcVapIndex,
       "pvcRowStatus": pvcRowStatus,
       "tpTrafficProfileTable": tpTrafficProfileTable,
       "tpTrafficProfileEntry": tpTrafficProfileEntry,
       "tpTrafficProfileIndex": tpTrafficProfileIndex,
       "tpTrafficType": tpTrafficType,
       "tpTrafficDescriptorParam1": tpTrafficDescriptorParam1,
       "tpTrafficDescriptorParam2": tpTrafficDescriptorParam2,
       "tpTrafficDescriptorParam3": tpTrafficDescriptorParam3,
       "tpTrafficDescriptorParam4": tpTrafficDescriptorParam4,
       "tpTrafficDescriptorParam5": tpTrafficDescriptorParam5,
       "tpQosClass": tpQosClass,
       "tpRowStatus": tpRowStatus,
       "mapVapTrafficProfileMappingTable": mapVapTrafficProfileMappingTable,
       "mapVapTrafficProfileMappingEntry": mapVapTrafficProfileMappingEntry,
       "mapMappingIndex": mapMappingIndex,
       "mapTargetAtmAddress": mapTargetAtmAddress,
       "mapAddressMask": mapAddressMask,
       "mapVccType": mapVccType,
       "mapTableProfile0Index": mapTableProfile0Index,
       "mapTableProfile1Index": mapTableProfile1Index,
       "mapTableProfile2Index": mapTableProfile2Index,
       "mapTableProfile3Index": mapTableProfile3Index,
       "mapTableProfile4Index": mapTableProfile4Index,
       "mapTableProfile5Index": mapTableProfile5Index,
       "mapTableProfile6Index": mapTableProfile6Index,
       "mapTableProfile7Index": mapTableProfile7Index,
       "mapTableProfile8Index": mapTableProfile8Index,
       "mapTableProfile9Index": mapTableProfile9Index,
       "mapRowStatus": mapRowStatus,
       "signallingConfigTable": signallingConfigTable,
       "signallingConfigEntry": signallingConfigEntry,
       "configSigMaxSigProtStevs": configSigMaxSigProtStevs,
       "configSigT301": configSigT301,
       "configSigT303": configSigT303,
       "configSigT308": configSigT308,
       "configSigT309": configSigT309,
       "configSigT310": configSigT310,
       "configSigT313": configSigT313,
       "configSigT316": configSigT316,
       "configSigT317": configSigT317,
       "configSigT322": configSigT322,
       "sscopConfigTable": sscopConfigTable,
       "sscopConfigEntry": sscopConfigEntry,
       "configSscopMaxRcvWinSize": configSscopMaxRcvWinSize,
       "configSscopMaxCc": configSscopMaxCc,
       "configSscopMaxPd": configSscopMaxPd,
       "configSscopMaxStat": configSscopMaxStat,
       "configSscopTimerPoll": configSscopTimerPoll,
       "configSscopTimerNoResponse": configSscopTimerNoResponse,
       "configSscopTimerKeepAlive": configSscopTimerKeepAlive,
       "configSscopTimerIdle": configSscopTimerIdle,
       "configSscopTimerCc": configSscopTimerCc,
       "configSscopMaxSduSize": configSscopMaxSduSize,
       "configSscopMaxUuSize": configSscopMaxUuSize,
       "atmUplinkStatus": atmUplinkStatus,
       "vccStatusTable": vccStatusTable,
       "vccStatusEntry": vccStatusEntry,
       "vccVpi": vccVpi,
       "vccVci": vccVci,
       "vccUsage": vccUsage,
       "vccInstance": vccInstance,
       "vccCreateMeans": vccCreateMeans,
       "vccTxTrafficDescriptorType": vccTxTrafficDescriptorType,
       "vccTxTrafficDescriptorParam1": vccTxTrafficDescriptorParam1,
       "vccTxTrafficDescriptorParam2": vccTxTrafficDescriptorParam2,
       "vccTxTrafficDescriptorParam3": vccTxTrafficDescriptorParam3,
       "vccTxTrafficDescriptorParam4": vccTxTrafficDescriptorParam4,
       "vccTxTrafficDescriptorParam5": vccTxTrafficDescriptorParam5,
       "vccTxQosClass": vccTxQosClass,
       "vccTxFrameDiscard": vccTxFrameDiscard,
       "vccServiceCategory": vccServiceCategory,
       "vccAtmAddress": vccAtmAddress,
       "vccTxFrames": vccTxFrames,
       "vccTxHighBytes": vccTxHighBytes,
       "vccTxLowBytes": vccTxLowBytes,
       "vccRxFrames": vccRxFrames,
       "vccRxHighBytes": vccRxHighBytes,
       "vccRxLowBytes": vccRxLowBytes,
       "macAddressConnectionTable": macAddressConnectionTable,
       "macAddressConnectionEntry": macAddressConnectionEntry,
       "macAddress": macAddress,
       "macVpi": macVpi,
       "macVci": macVci,
       "logMessageTable": logMessageTable,
       "logMessageEntry": logMessageEntry,
       "logMessageIndex": logMessageIndex,
       "logMessageTime": logMessageTime,
       "logMessageText": logMessageText,
       "ledStatusTable": ledStatusTable,
       "ledStatusEntry": ledStatusEntry,
       "ledDiag": ledDiag,
       "ledError": ledError,
       "ledSigLoss": ledSigLoss,
       "ledRxSync": ledRxSync,
       "atmUplinkStatistics": atmUplinkStatistics,
       "vapFrameFwStatisticsTable": vapFrameFwStatisticsTable,
       "vapFrameFwStatisticsEntry": vapFrameFwStatisticsEntry,
       "vapFfsIdfInvalidRoutes": vapFfsIdfInvalidRoutes,
       "vapFfsIdfRingNumberMismatches": vapFfsIdfRingNumberMismatches,
       "vapFfsIdfDuplicateRingNumbers": vapFfsIdfDuplicateRingNumbers,
       "vapFfsIdfTooLargeFrames": vapFfsIdfTooLargeFrames,
       "vapFfsIdfTooLongRouteDescriptors": vapFfsIdfTooLongRouteDescriptors,
       "vapFfsIdfBlockedByMacAddressFilters": vapFfsIdfBlockedByMacAddressFilters,
       "vapFfsIdfBlockedBySapFilters": vapFfsIdfBlockedBySapFilters,
       "vapFfsIdfCRFMismatches": vapFfsIdfCRFMismatches,
       "vapFfsIdfExplorerOverflows": vapFfsIdfExplorerOverflows,
       "vapFfsUfNonSourceRoutedFrames": vapFfsUfNonSourceRoutedFrames,
       "vapFfsUfSpecificallyRoutedFrames": vapFfsUfSpecificallyRoutedFrames,
       "vapFfsUfSTEFrames": vapFfsUfSTEFrames,
       "vapFfsUfAREFrames": vapFfsUfAREFrames,
       "vapFfsBfNonSourceRoutedFrames": vapFfsBfNonSourceRoutedFrames,
       "vapFfsBfSpecificallyRoutedFrames": vapFfsBfSpecificallyRoutedFrames,
       "vapFfsBfSTEFrames": vapFfsBfSTEFrames,
       "vapFfsBfAREFrames": vapFfsBfAREFrames,
       "vapFfsMfNonSourceRoutedFrames": vapFfsMfNonSourceRoutedFrames,
       "vapFfsMfSpecificallyRoutedFrames": vapFfsMfSpecificallyRoutedFrames,
       "vapFfsMfSTEFrames": vapFfsMfSTEFrames,
       "vapFfsMfAREFrames": vapFfsMfAREFrames,
       "vapFfsReceivedHighBytes": vapFfsReceivedHighBytes,
       "vapFfsReceivedLowBytes": vapFfsReceivedLowBytes,
       "vapFfsFfNonSourceRoutedFrames": vapFfsFfNonSourceRoutedFrames,
       "vapFfsFfSpecificallyRoutedFrames": vapFfsFfSpecificallyRoutedFrames,
       "vapFfsFfSTEFrames": vapFfsFfSTEFrames,
       "vapFfsFfAREFrames": vapFfsFfAREFrames,
       "vapFfsForwardedHighBytes": vapFfsForwardedHighBytes,
       "vapFfsForwardedLowBytes": vapFfsForwardedLowBytes,
       "vapFfsOdfInactiveVaps": vapFfsOdfInactiveVaps,
       "vapFfsOdfBlockedVaps": vapFfsOdfBlockedVaps,
       "vapFfsOdfBlockedBySapFilters": vapFfsOdfBlockedBySapFilters,
       "vapFfsOdfTooLargeFrames": vapFfsOdfTooLargeFrames,
       "vapFfsTfNonSourceRoutedFrames": vapFfsTfNonSourceRoutedFrames,
       "vapFfsTfSpecificallyRoutedFrames": vapFfsTfSpecificallyRoutedFrames,
       "vapFfsTfSTEFrames": vapFfsTfSTEFrames,
       "vapFfsTfAREFrames": vapFfsTfAREFrames,
       "vapFfsTransmittedHighBytes": vapFfsTransmittedHighBytes,
       "vapFfsTransmittedLowBytes": vapFfsTransmittedLowBytes,
       "vapFfsLastResetTime": vapFfsLastResetTime,
       "vapLaneStatisticsTable": vapLaneStatisticsTable,
       "vapLaneStatisticsEntry": vapLaneStatisticsEntry,
       "vapLsLeastActiveVccDisconnectedEvents": vapLsLeastActiveVccDisconnectedEvents,
       "vapLsNoLeastActiveVccFoundEvents": vapLsNoLeastActiveVccFoundEvents,
       "vapLsLastResetTime": vapLsLastResetTime,
       "globalOutboundStatTable": globalOutboundStatTable,
       "globalOutboundStatEntry": globalOutboundStatEntry,
       "outboundDfBadChannels": outboundDfBadChannels,
       "outboundDfInvalidTags": outboundDfInvalidTags,
       "outboundStatLastResetTime": outboundStatLastResetTime,
       "atmDiagnosticsTable": atmDiagnosticsTable,
       "atmDiagnosticsEntry": atmDiagnosticsEntry,
       "atmDiagsDroppedPackets": atmDiagsDroppedPackets,
       "atmDiagsCrcErrors": atmDiagsCrcErrors,
       "atmDiagsOverflows": atmDiagsOverflows,
       "atmDiagsFrameTooLongErrors": atmDiagsFrameTooLongErrors,
       "atmDiagsFrameTooShortErrors": atmDiagsFrameTooShortErrors,
       "atmDiagsUnknownVccErrors": atmDiagsUnknownVccErrors,
       "atmDiagsReceivedHighBytes": atmDiagsReceivedHighBytes,
       "atmDiagsReceivedLowBytes": atmDiagsReceivedLowBytes,
       "atmDiagsTransmittedHighBytes": atmDiagsTransmittedHighBytes,
       "atmDiagsTransmittedLowBytes": atmDiagsTransmittedLowBytes,
       "atmDiagsLastResetTime": atmDiagsLastResetTime}
)
