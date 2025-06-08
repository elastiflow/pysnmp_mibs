# SNMP MIB module (OC-HOME-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/OC-HOME-NETWORK-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:18 2025
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

(clabProjOpenCable,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjOpenCable")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ocHnMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ocHnMibModule.setRevisions(
        ("2013-05-30 00:00",
         "2013-04-18 00:00",
         "2012-02-24 00:00",
         "2010-09-10 00:00",
         "2010-05-07 00:00",
         "2009-09-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Tenths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class PowerUnit(TextualConvention, Integer32):
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
        *(("other", 1),
          ("dBmV", 2),
          ("dBm", 3),
          ("mW", 4))
    )



# MIB Managed Objects in the order of their OIDs

_OcHnNotifications_ObjectIdentity = ObjectIdentity
ocHnNotifications = _OcHnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 1)
)
_OcHnMibObjects_ObjectIdentity = ObjectIdentity
ocHnMibObjects = _OcHnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2)
)
_OcHnHomeNetStatus_ObjectIdentity = ObjectIdentity
ocHnHomeNetStatus = _OcHnHomeNetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1)
)
_OcHnRsdManagerStatus_ObjectIdentity = ObjectIdentity
ocHnRsdManagerStatus = _OcHnRsdManagerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 1)
)


class _OcHnRsdManagerImportanceNumber_Type(Unsigned32):
    """Custom type ocHnRsdManagerImportanceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OcHnRsdManagerImportanceNumber_Type.__name__ = "Unsigned32"
_OcHnRsdManagerImportanceNumber_Object = MibScalar
ocHnRsdManagerImportanceNumber = _OcHnRsdManagerImportanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 1, 1),
    _OcHnRsdManagerImportanceNumber_Type()
)
ocHnRsdManagerImportanceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnRsdManagerImportanceNumber.setStatus("current")
_OcHnRsdManagerPreferredStatus_Type = TruthValue
_OcHnRsdManagerPreferredStatus_Object = MibScalar
ocHnRsdManagerPreferredStatus = _OcHnRsdManagerPreferredStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 1, 2),
    _OcHnRsdManagerPreferredStatus_Type()
)
ocHnRsdManagerPreferredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnRsdManagerPreferredStatus.setStatus("current")
_OcHnDevUpnpServiceTable_Object = MibTable
ocHnDevUpnpServiceTable = _OcHnDevUpnpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ocHnDevUpnpServiceTable.setStatus("current")
_OcHnDevUpnpServiceEntry_Object = MibTableRow
ocHnDevUpnpServiceEntry = _OcHnDevUpnpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 2, 1)
)
ocHnDevUpnpServiceEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnDevUpnpServiceIndex"),
)
if mibBuilder.loadTexts:
    ocHnDevUpnpServiceEntry.setStatus("current")


class _OcHnDevUpnpServiceIndex_Type(Unsigned32):
    """Custom type ocHnDevUpnpServiceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnDevUpnpServiceIndex_Type.__name__ = "Unsigned32"
_OcHnDevUpnpServiceIndex_Object = MibTableColumn
ocHnDevUpnpServiceIndex = _OcHnDevUpnpServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 2, 1, 1),
    _OcHnDevUpnpServiceIndex_Type()
)
ocHnDevUpnpServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnDevUpnpServiceIndex.setStatus("current")


class _OcHnDevUpnpServiceType_Type(Integer32):
    """Custom type ocHnDevUpnpServiceType based on Integer32"""
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
        *(("cds", 1),
          ("srs", 2),
          ("qosManager", 3),
          ("qosDevice", 4),
          ("qosPolicyHolder", 5),
          ("avt", 6),
          ("cm", 7),
          ("rcs", 8))
    )


_OcHnDevUpnpServiceType_Type.__name__ = "Integer32"
_OcHnDevUpnpServiceType_Object = MibTableColumn
ocHnDevUpnpServiceType = _OcHnDevUpnpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 2, 1, 2),
    _OcHnDevUpnpServiceType_Type()
)
ocHnDevUpnpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevUpnpServiceType.setStatus("current")
_OcHnDevUpnpServiceAvailable_Type = TruthValue
_OcHnDevUpnpServiceAvailable_Object = MibTableColumn
ocHnDevUpnpServiceAvailable = _OcHnDevUpnpServiceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 2, 1, 3),
    _OcHnDevUpnpServiceAvailable_Type()
)
ocHnDevUpnpServiceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevUpnpServiceAvailable.setStatus("current")
_OcHnDevSupportedChannelTable_Object = MibTable
ocHnDevSupportedChannelTable = _OcHnDevSupportedChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelTable.setStatus("current")
_OcHnDevSupportedChannelEntry_Object = MibTableRow
ocHnDevSupportedChannelEntry = _OcHnDevSupportedChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 3, 1)
)
ocHnDevSupportedChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OC-HOME-NETWORK-MIB", "ocHnDevSupportedChannelIndex"),
)
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelEntry.setStatus("current")


class _OcHnDevSupportedChannelIndex_Type(Unsigned32):
    """Custom type ocHnDevSupportedChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnDevSupportedChannelIndex_Type.__name__ = "Unsigned32"
_OcHnDevSupportedChannelIndex_Object = MibTableColumn
ocHnDevSupportedChannelIndex = _OcHnDevSupportedChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 3, 1, 1),
    _OcHnDevSupportedChannelIndex_Type()
)
ocHnDevSupportedChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelIndex.setStatus("current")
_OcHnDevSupportedChannelLastOperatingFreq_Type = TruthValue
_OcHnDevSupportedChannelLastOperatingFreq_Object = MibTableColumn
ocHnDevSupportedChannelLastOperatingFreq = _OcHnDevSupportedChannelLastOperatingFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 3, 1, 2),
    _OcHnDevSupportedChannelLastOperatingFreq_Type()
)
ocHnDevSupportedChannelLastOperatingFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelLastOperatingFreq.setStatus("current")
_OcHnDevSupportedChannelInUse_Type = TruthValue
_OcHnDevSupportedChannelInUse_Object = MibTableColumn
ocHnDevSupportedChannelInUse = _OcHnDevSupportedChannelInUse_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 3, 1, 3),
    _OcHnDevSupportedChannelInUse_Type()
)
ocHnDevSupportedChannelInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelInUse.setStatus("current")


class _OcHnDevSupportedChannelFrequency_Type(Unsigned32):
    """Custom type ocHnDevSupportedChannelFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000000),
    )


_OcHnDevSupportedChannelFrequency_Type.__name__ = "Unsigned32"
_OcHnDevSupportedChannelFrequency_Object = MibTableColumn
ocHnDevSupportedChannelFrequency = _OcHnDevSupportedChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 3, 1, 4),
    _OcHnDevSupportedChannelFrequency_Type()
)
ocHnDevSupportedChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelFrequency.setUnits("hertz")
_OcHnDevSupportedChannelEligible_Type = TruthValue
_OcHnDevSupportedChannelEligible_Object = MibTableColumn
ocHnDevSupportedChannelEligible = _OcHnDevSupportedChannelEligible_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 3, 1, 5),
    _OcHnDevSupportedChannelEligible_Type()
)
ocHnDevSupportedChannelEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnDevSupportedChannelEligible.setStatus("current")
_OcHnDevProperties_ObjectIdentity = ObjectIdentity
ocHnDevProperties = _OcHnDevProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 4)
)
_OcHnDevPropertiesFriendlyName_Type = SnmpAdminString
_OcHnDevPropertiesFriendlyName_Object = MibScalar
ocHnDevPropertiesFriendlyName = _OcHnDevPropertiesFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 1, 4, 1),
    _OcHnDevPropertiesFriendlyName_Type()
)
ocHnDevPropertiesFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevPropertiesFriendlyName.setStatus("current")
_OcHnROConfiguration_ObjectIdentity = ObjectIdentity
ocHnROConfiguration = _OcHnROConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2)
)
_OcHnRotameterConfigTable_Object = MibTable
ocHnRotameterConfigTable = _OcHnRotameterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ocHnRotameterConfigTable.setStatus("current")
_OcHnRotameterConfigEntry_Object = MibTableRow
ocHnRotameterConfigEntry = _OcHnRotameterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1)
)
ocHnRotameterConfigEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnRotameterConfigIndex"),
)
if mibBuilder.loadTexts:
    ocHnRotameterConfigEntry.setStatus("current")


class _OcHnRotameterConfigIndex_Type(Unsigned32):
    """Custom type ocHnRotameterConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnRotameterConfigIndex_Type.__name__ = "Unsigned32"
_OcHnRotameterConfigIndex_Object = MibTableColumn
ocHnRotameterConfigIndex = _OcHnRotameterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1, 1),
    _OcHnRotameterConfigIndex_Type()
)
ocHnRotameterConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnRotameterConfigIndex.setStatus("current")
_OcHnRotameterConfigRowStatus_Type = RowStatus
_OcHnRotameterConfigRowStatus_Object = MibTableColumn
ocHnRotameterConfigRowStatus = _OcHnRotameterConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1, 2),
    _OcHnRotameterConfigRowStatus_Type()
)
ocHnRotameterConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnRotameterConfigRowStatus.setStatus("current")
_OcHnRotameterConfigObservationActive_Type = TruthValue
_OcHnRotameterConfigObservationActive_Object = MibTableColumn
ocHnRotameterConfigObservationActive = _OcHnRotameterConfigObservationActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1, 3),
    _OcHnRotameterConfigObservationActive_Type()
)
ocHnRotameterConfigObservationActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnRotameterConfigObservationActive.setStatus("current")
_OcHnRotameterConfigPeriod_Type = Unsigned32
_OcHnRotameterConfigPeriod_Object = MibTableColumn
ocHnRotameterConfigPeriod = _OcHnRotameterConfigPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1, 4),
    _OcHnRotameterConfigPeriod_Type()
)
ocHnRotameterConfigPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnRotameterConfigPeriod.setStatus("current")
_OcHnRotameterConfigMonitorResolutionPeriod_Type = Unsigned32
_OcHnRotameterConfigMonitorResolutionPeriod_Object = MibTableColumn
ocHnRotameterConfigMonitorResolutionPeriod = _OcHnRotameterConfigMonitorResolutionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1, 5),
    _OcHnRotameterConfigMonitorResolutionPeriod_Type()
)
ocHnRotameterConfigMonitorResolutionPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnRotameterConfigMonitorResolutionPeriod.setStatus("current")
_OcHnRotameterConfigQosSegmentId_Type = OctetString
_OcHnRotameterConfigQosSegmentId_Object = MibTableColumn
ocHnRotameterConfigQosSegmentId = _OcHnRotameterConfigQosSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1, 6),
    _OcHnRotameterConfigQosSegmentId_Type()
)
ocHnRotameterConfigQosSegmentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnRotameterConfigQosSegmentId.setStatus("current")
_OcHnRotameterConfigEndpointMacAddress_Type = MacAddress
_OcHnRotameterConfigEndpointMacAddress_Object = MibTableColumn
ocHnRotameterConfigEndpointMacAddress = _OcHnRotameterConfigEndpointMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 1, 1, 7),
    _OcHnRotameterConfigEndpointMacAddress_Type()
)
ocHnRotameterConfigEndpointMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnRotameterConfigEndpointMacAddress.setStatus("current")
_OcHnPerStreamRotameterConfigTable_Object = MibTable
ocHnPerStreamRotameterConfigTable = _OcHnPerStreamRotameterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ocHnPerStreamRotameterConfigTable.setStatus("current")
_OcHnPerStreamRotameterConfigEntry_Object = MibTableRow
ocHnPerStreamRotameterConfigEntry = _OcHnPerStreamRotameterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 2, 1)
)
ocHnPerStreamRotameterConfigEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnPerStreamRotameterConfigIndex"),
    (0, "OC-HOME-NETWORK-MIB", "ocHnRotameterConfigIndex"),
)
if mibBuilder.loadTexts:
    ocHnPerStreamRotameterConfigEntry.setStatus("current")


class _OcHnPerStreamRotameterConfigIndex_Type(Unsigned32):
    """Custom type ocHnPerStreamRotameterConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnPerStreamRotameterConfigIndex_Type.__name__ = "Unsigned32"
_OcHnPerStreamRotameterConfigIndex_Object = MibTableColumn
ocHnPerStreamRotameterConfigIndex = _OcHnPerStreamRotameterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 2, 1, 1),
    _OcHnPerStreamRotameterConfigIndex_Type()
)
ocHnPerStreamRotameterConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnPerStreamRotameterConfigIndex.setStatus("current")
_OcHnPerStreamRotameterConfigRowStatus_Type = RowStatus
_OcHnPerStreamRotameterConfigRowStatus_Object = MibTableColumn
ocHnPerStreamRotameterConfigRowStatus = _OcHnPerStreamRotameterConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 2, 1, 2),
    _OcHnPerStreamRotameterConfigRowStatus_Type()
)
ocHnPerStreamRotameterConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnPerStreamRotameterConfigRowStatus.setStatus("current")


class _OcHnPerStreamRotameterConfigLayer2StreamId_Type(OctetString):
    """Custom type ocHnPerStreamRotameterConfigLayer2StreamId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixedLength = 64


_OcHnPerStreamRotameterConfigLayer2StreamId_Type.__name__ = "OctetString"
_OcHnPerStreamRotameterConfigLayer2StreamId_Object = MibTableColumn
ocHnPerStreamRotameterConfigLayer2StreamId = _OcHnPerStreamRotameterConfigLayer2StreamId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 2, 1, 3),
    _OcHnPerStreamRotameterConfigLayer2StreamId_Type()
)
ocHnPerStreamRotameterConfigLayer2StreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnPerStreamRotameterConfigLayer2StreamId.setStatus("current")
_OcHnPerStreamRotameterConfigTrafficHandle_Type = OctetString
_OcHnPerStreamRotameterConfigTrafficHandle_Object = MibTableColumn
ocHnPerStreamRotameterConfigTrafficHandle = _OcHnPerStreamRotameterConfigTrafficHandle_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 2, 1, 4),
    _OcHnPerStreamRotameterConfigTrafficHandle_Type()
)
ocHnPerStreamRotameterConfigTrafficHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnPerStreamRotameterConfigTrafficHandle.setStatus("current")
_OcHnPerStreamRotameterConfigObservationActive_Type = TruthValue
_OcHnPerStreamRotameterConfigObservationActive_Object = MibTableColumn
ocHnPerStreamRotameterConfigObservationActive = _OcHnPerStreamRotameterConfigObservationActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 2, 2, 1, 5),
    _OcHnPerStreamRotameterConfigObservationActive_Type()
)
ocHnPerStreamRotameterConfigObservationActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnPerStreamRotameterConfigObservationActive.setStatus("current")
_OcHnQos_ObjectIdentity = ObjectIdentity
ocHnQos = _OcHnQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3)
)
_OcHnQosTrafficInfo_ObjectIdentity = ObjectIdentity
ocHnQosTrafficInfo = _OcHnQosTrafficInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1)
)
_OcHnQosStreamsInfoCollectionTrigger_Type = TruthValue
_OcHnQosStreamsInfoCollectionTrigger_Object = MibScalar
ocHnQosStreamsInfoCollectionTrigger = _OcHnQosStreamsInfoCollectionTrigger_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 1),
    _OcHnQosStreamsInfoCollectionTrigger_Type()
)
ocHnQosStreamsInfoCollectionTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnQosStreamsInfoCollectionTrigger.setStatus("current")
_OcHnQosTrafficDescTable_Object = MibTable
ocHnQosTrafficDescTable = _OcHnQosTrafficDescTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ocHnQosTrafficDescTable.setStatus("current")
_OcHnQosTrafficDescEntry_Object = MibTableRow
ocHnQosTrafficDescEntry = _OcHnQosTrafficDescEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1)
)
ocHnQosTrafficDescEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnQosTrafficDescIndex"),
)
if mibBuilder.loadTexts:
    ocHnQosTrafficDescEntry.setStatus("current")


class _OcHnQosTrafficDescIndex_Type(Unsigned32):
    """Custom type ocHnQosTrafficDescIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnQosTrafficDescIndex_Type.__name__ = "Unsigned32"
_OcHnQosTrafficDescIndex_Object = MibTableColumn
ocHnQosTrafficDescIndex = _OcHnQosTrafficDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 1),
    _OcHnQosTrafficDescIndex_Type()
)
ocHnQosTrafficDescIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnQosTrafficDescIndex.setStatus("current")
_OcHnQosTrafficHandle_Type = OctetString
_OcHnQosTrafficHandle_Object = MibTableColumn
ocHnQosTrafficHandle = _OcHnQosTrafficHandle_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 2),
    _OcHnQosTrafficHandle_Type()
)
ocHnQosTrafficHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficHandle.setStatus("current")
_OcHnQosTrafficQDMacAddress_Type = MacAddress
_OcHnQosTrafficQDMacAddress_Object = MibTableColumn
ocHnQosTrafficQDMacAddress = _OcHnQosTrafficQDMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 3),
    _OcHnQosTrafficQDMacAddress_Type()
)
ocHnQosTrafficQDMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficQDMacAddress.setStatus("current")
_OcHnQosTrafficNetworkAddressType_Type = InetAddressType
_OcHnQosTrafficNetworkAddressType_Object = MibTableColumn
ocHnQosTrafficNetworkAddressType = _OcHnQosTrafficNetworkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 4),
    _OcHnQosTrafficNetworkAddressType_Type()
)
ocHnQosTrafficNetworkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficNetworkAddressType.setStatus("current")
_OcHnQosTrafficSourceAddress_Type = InetAddress
_OcHnQosTrafficSourceAddress_Object = MibTableColumn
ocHnQosTrafficSourceAddress = _OcHnQosTrafficSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 5),
    _OcHnQosTrafficSourceAddress_Type()
)
ocHnQosTrafficSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficSourceAddress.setStatus("current")
_OcHnQosTrafficSourcePort_Type = InetPortNumber
_OcHnQosTrafficSourcePort_Object = MibTableColumn
ocHnQosTrafficSourcePort = _OcHnQosTrafficSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 6),
    _OcHnQosTrafficSourcePort_Type()
)
ocHnQosTrafficSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficSourcePort.setStatus("current")
_OcHnQosTrafficDestinationAddress_Type = InetAddress
_OcHnQosTrafficDestinationAddress_Object = MibTableColumn
ocHnQosTrafficDestinationAddress = _OcHnQosTrafficDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 7),
    _OcHnQosTrafficDestinationAddress_Type()
)
ocHnQosTrafficDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficDestinationAddress.setStatus("current")
_OcHnQosTrafficDestinationPort_Type = InetPortNumber
_OcHnQosTrafficDestinationPort_Object = MibTableColumn
ocHnQosTrafficDestinationPort = _OcHnQosTrafficDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 8),
    _OcHnQosTrafficDestinationPort_Type()
)
ocHnQosTrafficDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficDestinationPort.setStatus("current")


class _OcHnQosTrafficIpProtocol_Type(Unsigned32):
    """Custom type ocHnQosTrafficIpProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OcHnQosTrafficIpProtocol_Type.__name__ = "Unsigned32"
_OcHnQosTrafficIpProtocol_Object = MibTableColumn
ocHnQosTrafficIpProtocol = _OcHnQosTrafficIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 9),
    _OcHnQosTrafficIpProtocol_Type()
)
ocHnQosTrafficIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficIpProtocol.setStatus("current")
_OcHnQosTrafficV3TrafficIdSourceUuid_Type = OctetString
_OcHnQosTrafficV3TrafficIdSourceUuid_Object = MibTableColumn
ocHnQosTrafficV3TrafficIdSourceUuid = _OcHnQosTrafficV3TrafficIdSourceUuid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 10),
    _OcHnQosTrafficV3TrafficIdSourceUuid_Type()
)
ocHnQosTrafficV3TrafficIdSourceUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficV3TrafficIdSourceUuid.setStatus("current")
_OcHnQosTrafficV3TrafficIdDestinationUuid_Type = OctetString
_OcHnQosTrafficV3TrafficIdDestinationUuid_Object = MibTableColumn
ocHnQosTrafficV3TrafficIdDestinationUuid = _OcHnQosTrafficV3TrafficIdDestinationUuid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 11),
    _OcHnQosTrafficV3TrafficIdDestinationUuid_Type()
)
ocHnQosTrafficV3TrafficIdDestinationUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficV3TrafficIdDestinationUuid.setStatus("current")


class _OcHnQosTrafficMediaServerConnectionId_Type(Integer32):
    """Custom type ocHnQosTrafficMediaServerConnectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_OcHnQosTrafficMediaServerConnectionId_Type.__name__ = "Integer32"
_OcHnQosTrafficMediaServerConnectionId_Object = MibTableColumn
ocHnQosTrafficMediaServerConnectionId = _OcHnQosTrafficMediaServerConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 12),
    _OcHnQosTrafficMediaServerConnectionId_Type()
)
ocHnQosTrafficMediaServerConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficMediaServerConnectionId.setStatus("current")


class _OcHnQosTrafficMediaRendererConnectionId_Type(Integer32):
    """Custom type ocHnQosTrafficMediaRendererConnectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_OcHnQosTrafficMediaRendererConnectionId_Type.__name__ = "Integer32"
_OcHnQosTrafficMediaRendererConnectionId_Object = MibTableColumn
ocHnQosTrafficMediaRendererConnectionId = _OcHnQosTrafficMediaRendererConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 13),
    _OcHnQosTrafficMediaRendererConnectionId_Type()
)
ocHnQosTrafficMediaRendererConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficMediaRendererConnectionId.setStatus("current")
_OcHnQosTrafficLeaseTime_Type = Unsigned32
_OcHnQosTrafficLeaseTime_Object = MibTableColumn
ocHnQosTrafficLeaseTime = _OcHnQosTrafficLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 14),
    _OcHnQosTrafficLeaseTime_Type()
)
ocHnQosTrafficLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosTrafficLeaseTime.setUnits("seconds")
_OcHnQosTrafficCritical_Type = TruthValue
_OcHnQosTrafficCritical_Object = MibTableColumn
ocHnQosTrafficCritical = _OcHnQosTrafficCritical_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 15),
    _OcHnQosTrafficCritical_Type()
)
ocHnQosTrafficCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficCritical.setStatus("current")


class _OcHnQosTrafficUserName_Type(SnmpAdminString):
    """Custom type ocHnQosTrafficUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OcHnQosTrafficUserName_Type.__name__ = "SnmpAdminString"
_OcHnQosTrafficUserName_Object = MibTableColumn
ocHnQosTrafficUserName = _OcHnQosTrafficUserName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 16),
    _OcHnQosTrafficUserName_Type()
)
ocHnQosTrafficUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficUserName.setStatus("current")
_OcHnQosTrafficVendorApplicationName_Type = OctetString
_OcHnQosTrafficVendorApplicationName_Object = MibTableColumn
ocHnQosTrafficVendorApplicationName = _OcHnQosTrafficVendorApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 17),
    _OcHnQosTrafficVendorApplicationName_Type()
)
ocHnQosTrafficVendorApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficVendorApplicationName.setStatus("current")
_OcHnQosTrafficPortName_Type = OctetString
_OcHnQosTrafficPortName_Object = MibTableColumn
ocHnQosTrafficPortName = _OcHnQosTrafficPortName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 18),
    _OcHnQosTrafficPortName_Type()
)
ocHnQosTrafficPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficPortName.setStatus("current")
_OcHnQosTrafficServiceProviderServiceName_Type = OctetString
_OcHnQosTrafficServiceProviderServiceName_Object = MibTableColumn
ocHnQosTrafficServiceProviderServiceName = _OcHnQosTrafficServiceProviderServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 19),
    _OcHnQosTrafficServiceProviderServiceName_Type()
)
ocHnQosTrafficServiceProviderServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficServiceProviderServiceName.setStatus("current")
_OcHnQosTrafficCpName_Type = SnmpAdminString
_OcHnQosTrafficCpName_Object = MibTableColumn
ocHnQosTrafficCpName = _OcHnQosTrafficCpName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 2, 1, 20),
    _OcHnQosTrafficCpName_Type()
)
ocHnQosTrafficCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficCpName.setStatus("current")
_OcHnQosTspecTable_Object = MibTable
ocHnQosTspecTable = _OcHnQosTspecTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ocHnQosTspecTable.setStatus("current")
_OcHnQosTspecEntry_Object = MibTableRow
ocHnQosTspecEntry = _OcHnQosTspecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1)
)
ocHnQosTspecEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnQosTspecTableIndex"),
    (0, "OC-HOME-NETWORK-MIB", "ocHnQosTrafficHandle"),
)
if mibBuilder.loadTexts:
    ocHnQosTspecEntry.setStatus("current")


class _OcHnQosTspecTableIndex_Type(Unsigned32):
    """Custom type ocHnQosTspecTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnQosTspecTableIndex_Type.__name__ = "Unsigned32"
_OcHnQosTspecTableIndex_Object = MibTableColumn
ocHnQosTspecTableIndex = _OcHnQosTspecTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 1),
    _OcHnQosTspecTableIndex_Type()
)
ocHnQosTspecTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnQosTspecTableIndex.setStatus("current")
_OcHnQosTspec_Type = Unsigned32
_OcHnQosTspec_Object = MibTableColumn
ocHnQosTspec = _OcHnQosTspec_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 2),
    _OcHnQosTspec_Type()
)
ocHnQosTspec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspec.setStatus("current")
_OcHnQosActiveTspec_Type = TruthValue
_OcHnQosActiveTspec_Object = MibTableColumn
ocHnQosActiveTspec = _OcHnQosActiveTspec_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 3),
    _OcHnQosActiveTspec_Type()
)
ocHnQosActiveTspec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosActiveTspec.setStatus("current")


class _OcHnQosTspecTrafficClass_Type(Integer32):
    """Custom type ocHnQosTspecTrafficClass based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("networkControl", 2),
          ("streamingControl", 3),
          ("voice", 4),
          ("av", 5),
          ("data", 6),
          ("audio", 7),
          ("image", 8),
          ("background", 9),
          ("gaming", 10))
    )


_OcHnQosTspecTrafficClass_Type.__name__ = "Integer32"
_OcHnQosTspecTrafficClass_Object = MibTableColumn
ocHnQosTspecTrafficClass = _OcHnQosTspecTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 4),
    _OcHnQosTspecTrafficClass_Type()
)
ocHnQosTspecTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecTrafficClass.setStatus("current")


class _OcHnQosTspecReqQosType_Type(Integer32):
    """Custom type ocHnQosTspecReqQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("prioritized", 1),
          ("hybrid", 2),
          ("parameterized", 3))
    )


_OcHnQosTspecReqQosType_Type.__name__ = "Integer32"
_OcHnQosTspecReqQosType_Object = MibTableColumn
ocHnQosTspecReqQosType = _OcHnQosTspecReqQosType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 5),
    _OcHnQosTspecReqQosType_Type()
)
ocHnQosTspecReqQosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecReqQosType.setStatus("current")
_OcHnQosTspecDataRate_Type = Unsigned32
_OcHnQosTspecDataRate_Object = MibTableColumn
ocHnQosTspecDataRate = _OcHnQosTspecDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 6),
    _OcHnQosTspecDataRate_Type()
)
ocHnQosTspecDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecDataRate.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosTspecDataRate.setUnits("octets/sec")
_OcHnQosTspecPeakDataRate_Type = Unsigned32
_OcHnQosTspecPeakDataRate_Object = MibTableColumn
ocHnQosTspecPeakDataRate = _OcHnQosTspecPeakDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 7),
    _OcHnQosTspecPeakDataRate_Type()
)
ocHnQosTspecPeakDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecPeakDataRate.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosTspecPeakDataRate.setUnits("octets/sec")
_OcHnQosTspecMaxBurstSize_Type = Unsigned32
_OcHnQosTspecMaxBurstSize_Object = MibTableColumn
ocHnQosTspecMaxBurstSize = _OcHnQosTspecMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 8),
    _OcHnQosTspecMaxBurstSize_Type()
)
ocHnQosTspecMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosTspecMaxBurstSize.setUnits("octets/sec")
_OcHnQosTspecMaxPacketSize_Type = Unsigned32
_OcHnQosTspecMaxPacketSize_Object = MibTableColumn
ocHnQosTspecMaxPacketSize = _OcHnQosTspecMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 9),
    _OcHnQosTspecMaxPacketSize_Type()
)
ocHnQosTspecMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecMaxPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosTspecMaxPacketSize.setUnits("bytes")
_OcHnQosTspecE2EMaxDelayHigh_Type = Unsigned32
_OcHnQosTspecE2EMaxDelayHigh_Object = MibTableColumn
ocHnQosTspecE2EMaxDelayHigh = _OcHnQosTspecE2EMaxDelayHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 10),
    _OcHnQosTspecE2EMaxDelayHigh_Type()
)
ocHnQosTspecE2EMaxDelayHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecE2EMaxDelayHigh.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosTspecE2EMaxDelayHigh.setUnits("microseconds")
_OcHnQosTspecE2EMaxJitter_Type = Unsigned32
_OcHnQosTspecE2EMaxJitter_Object = MibTableColumn
ocHnQosTspecE2EMaxJitter = _OcHnQosTspecE2EMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 1, 3, 1, 11),
    _OcHnQosTspecE2EMaxJitter_Type()
)
ocHnQosTspecE2EMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTspecE2EMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosTspecE2EMaxJitter.setUnits("microseconds")
_OcHnQosPolicyTable_Object = MibTable
ocHnQosPolicyTable = _OcHnQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ocHnQosPolicyTable.setStatus("current")
_OcHnQosPolicyEntry_Object = MibTableRow
ocHnQosPolicyEntry = _OcHnQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1)
)
ocHnQosPolicyEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnQosPolicyRuleIdentifier"),
)
if mibBuilder.loadTexts:
    ocHnQosPolicyEntry.setStatus("current")


class _OcHnQosPolicyRuleIdentifier_Type(Unsigned32):
    """Custom type ocHnQosPolicyRuleIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OcHnQosPolicyRuleIdentifier_Type.__name__ = "Unsigned32"
_OcHnQosPolicyRuleIdentifier_Object = MibTableColumn
ocHnQosPolicyRuleIdentifier = _OcHnQosPolicyRuleIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 1),
    _OcHnQosPolicyRuleIdentifier_Type()
)
ocHnQosPolicyRuleIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnQosPolicyRuleIdentifier.setStatus("current")
_OcHnQosPolicyRowStatus_Type = RowStatus
_OcHnQosPolicyRowStatus_Object = MibTableColumn
ocHnQosPolicyRowStatus = _OcHnQosPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 2),
    _OcHnQosPolicyRowStatus_Type()
)
ocHnQosPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyRowStatus.setStatus("current")
_OcHnQosPolicyIpAddressType_Type = InetAddressType
_OcHnQosPolicyIpAddressType_Object = MibTableColumn
ocHnQosPolicyIpAddressType = _OcHnQosPolicyIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 3),
    _OcHnQosPolicyIpAddressType_Type()
)
ocHnQosPolicyIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyIpAddressType.setStatus("current")
_OcHnQosPolicySourceAddressUpLimit_Type = InetAddress
_OcHnQosPolicySourceAddressUpLimit_Object = MibTableColumn
ocHnQosPolicySourceAddressUpLimit = _OcHnQosPolicySourceAddressUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 4),
    _OcHnQosPolicySourceAddressUpLimit_Type()
)
ocHnQosPolicySourceAddressUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicySourceAddressUpLimit.setStatus("current")
_OcHnQosPolicySourceAddressLowLimit_Type = InetAddress
_OcHnQosPolicySourceAddressLowLimit_Object = MibTableColumn
ocHnQosPolicySourceAddressLowLimit = _OcHnQosPolicySourceAddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 5),
    _OcHnQosPolicySourceAddressLowLimit_Type()
)
ocHnQosPolicySourceAddressLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicySourceAddressLowLimit.setStatus("current")
_OcHnQosPolicySourcePortUpLimit_Type = InetPortNumber
_OcHnQosPolicySourcePortUpLimit_Object = MibTableColumn
ocHnQosPolicySourcePortUpLimit = _OcHnQosPolicySourcePortUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 6),
    _OcHnQosPolicySourcePortUpLimit_Type()
)
ocHnQosPolicySourcePortUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicySourcePortUpLimit.setStatus("current")
_OcHnQosPolicySourcePortLowLimit_Type = InetPortNumber
_OcHnQosPolicySourcePortLowLimit_Object = MibTableColumn
ocHnQosPolicySourcePortLowLimit = _OcHnQosPolicySourcePortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 7),
    _OcHnQosPolicySourcePortLowLimit_Type()
)
ocHnQosPolicySourcePortLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicySourcePortLowLimit.setStatus("current")
_OcHnQosPolicyDestinationAddressUpLimit_Type = InetAddress
_OcHnQosPolicyDestinationAddressUpLimit_Object = MibTableColumn
ocHnQosPolicyDestinationAddressUpLimit = _OcHnQosPolicyDestinationAddressUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 8),
    _OcHnQosPolicyDestinationAddressUpLimit_Type()
)
ocHnQosPolicyDestinationAddressUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyDestinationAddressUpLimit.setStatus("current")
_OcHnQosPolicyDestinationAddressLowLimit_Type = InetAddress
_OcHnQosPolicyDestinationAddressLowLimit_Object = MibTableColumn
ocHnQosPolicyDestinationAddressLowLimit = _OcHnQosPolicyDestinationAddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 9),
    _OcHnQosPolicyDestinationAddressLowLimit_Type()
)
ocHnQosPolicyDestinationAddressLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyDestinationAddressLowLimit.setStatus("current")
_OcHnQosPolicyDestinationPortUpLimit_Type = InetPortNumber
_OcHnQosPolicyDestinationPortUpLimit_Object = MibTableColumn
ocHnQosPolicyDestinationPortUpLimit = _OcHnQosPolicyDestinationPortUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 10),
    _OcHnQosPolicyDestinationPortUpLimit_Type()
)
ocHnQosPolicyDestinationPortUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyDestinationPortUpLimit.setStatus("current")
_OcHnQosPolicyDestinationPortLowLimit_Type = InetPortNumber
_OcHnQosPolicyDestinationPortLowLimit_Object = MibTableColumn
ocHnQosPolicyDestinationPortLowLimit = _OcHnQosPolicyDestinationPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 11),
    _OcHnQosPolicyDestinationPortLowLimit_Type()
)
ocHnQosPolicyDestinationPortLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyDestinationPortLowLimit.setStatus("current")


class _OcHnQosPolicyIpProtocolUpLimit_Type(Unsigned32):
    """Custom type ocHnQosPolicyIpProtocolUpLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OcHnQosPolicyIpProtocolUpLimit_Type.__name__ = "Unsigned32"
_OcHnQosPolicyIpProtocolUpLimit_Object = MibTableColumn
ocHnQosPolicyIpProtocolUpLimit = _OcHnQosPolicyIpProtocolUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 12),
    _OcHnQosPolicyIpProtocolUpLimit_Type()
)
ocHnQosPolicyIpProtocolUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyIpProtocolUpLimit.setStatus("current")


class _OcHnQosPolicyIpProtocolLowLimit_Type(Unsigned32):
    """Custom type ocHnQosPolicyIpProtocolLowLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OcHnQosPolicyIpProtocolLowLimit_Type.__name__ = "Unsigned32"
_OcHnQosPolicyIpProtocolLowLimit_Object = MibTableColumn
ocHnQosPolicyIpProtocolLowLimit = _OcHnQosPolicyIpProtocolLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 13),
    _OcHnQosPolicyIpProtocolLowLimit_Type()
)
ocHnQosPolicyIpProtocolLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyIpProtocolLowLimit.setStatus("current")


class _OcHnQosPolicyTrafficClass_Type(Integer32):
    """Custom type ocHnQosPolicyTrafficClass based on Integer32"""
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
        *(("networkControl", 0),
          ("streamingControl", 1),
          ("voice", 2),
          ("av", 3),
          ("data", 4),
          ("audio", 5),
          ("image", 6),
          ("gaming", 7),
          ("other", 8),
          ("background", 9))
    )


_OcHnQosPolicyTrafficClass_Type.__name__ = "Integer32"
_OcHnQosPolicyTrafficClass_Object = MibTableColumn
ocHnQosPolicyTrafficClass = _OcHnQosPolicyTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 14),
    _OcHnQosPolicyTrafficClass_Type()
)
ocHnQosPolicyTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyTrafficClass.setStatus("current")
_OcHnQosPolicyPeakDataRateUpLimit_Type = Unsigned32
_OcHnQosPolicyPeakDataRateUpLimit_Object = MibTableColumn
ocHnQosPolicyPeakDataRateUpLimit = _OcHnQosPolicyPeakDataRateUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 15),
    _OcHnQosPolicyPeakDataRateUpLimit_Type()
)
ocHnQosPolicyPeakDataRateUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyPeakDataRateUpLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyPeakDataRateUpLimit.setUnits("octets/sec")
_OcHnQosPolicyPeakDataRateLowLimit_Type = Unsigned32
_OcHnQosPolicyPeakDataRateLowLimit_Object = MibTableColumn
ocHnQosPolicyPeakDataRateLowLimit = _OcHnQosPolicyPeakDataRateLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 16),
    _OcHnQosPolicyPeakDataRateLowLimit_Type()
)
ocHnQosPolicyPeakDataRateLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyPeakDataRateLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyPeakDataRateLowLimit.setUnits("octets/sec")
_OcHnQosPolicyMeanDataRateUpLimit_Type = Unsigned32
_OcHnQosPolicyMeanDataRateUpLimit_Object = MibTableColumn
ocHnQosPolicyMeanDataRateUpLimit = _OcHnQosPolicyMeanDataRateUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 17),
    _OcHnQosPolicyMeanDataRateUpLimit_Type()
)
ocHnQosPolicyMeanDataRateUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyMeanDataRateUpLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyMeanDataRateUpLimit.setUnits("octets/sec")
_OcHnQosPolicyMeanDataRateLowLimit_Type = Unsigned32
_OcHnQosPolicyMeanDataRateLowLimit_Object = MibTableColumn
ocHnQosPolicyMeanDataRateLowLimit = _OcHnQosPolicyMeanDataRateLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 18),
    _OcHnQosPolicyMeanDataRateLowLimit_Type()
)
ocHnQosPolicyMeanDataRateLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyMeanDataRateLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyMeanDataRateLowLimit.setUnits("octets/sec")
_OcHnQosPolicyMaxBurstSizeUpLimit_Type = Unsigned32
_OcHnQosPolicyMaxBurstSizeUpLimit_Object = MibTableColumn
ocHnQosPolicyMaxBurstSizeUpLimit = _OcHnQosPolicyMaxBurstSizeUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 19),
    _OcHnQosPolicyMaxBurstSizeUpLimit_Type()
)
ocHnQosPolicyMaxBurstSizeUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyMaxBurstSizeUpLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyMaxBurstSizeUpLimit.setUnits("octets/sec")
_OcHnQosPolicyMaxBurstSizeLowLimit_Type = Unsigned32
_OcHnQosPolicyMaxBurstSizeLowLimit_Object = MibTableColumn
ocHnQosPolicyMaxBurstSizeLowLimit = _OcHnQosPolicyMaxBurstSizeLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 20),
    _OcHnQosPolicyMaxBurstSizeLowLimit_Type()
)
ocHnQosPolicyMaxBurstSizeLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyMaxBurstSizeLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyMaxBurstSizeLowLimit.setUnits("octets/sec")
_OcHnQosPolicyE2EMaxDelayHighLimit_Type = Unsigned32
_OcHnQosPolicyE2EMaxDelayHighLimit_Object = MibTableColumn
ocHnQosPolicyE2EMaxDelayHighLimit = _OcHnQosPolicyE2EMaxDelayHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 21),
    _OcHnQosPolicyE2EMaxDelayHighLimit_Type()
)
ocHnQosPolicyE2EMaxDelayHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyE2EMaxDelayHighLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyE2EMaxDelayHighLimit.setUnits("microseconds")
_OcHnQosPolicyE2EMaxDelayLowLimit_Type = Unsigned32
_OcHnQosPolicyE2EMaxDelayLowLimit_Object = MibTableColumn
ocHnQosPolicyE2EMaxDelayLowLimit = _OcHnQosPolicyE2EMaxDelayLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 22),
    _OcHnQosPolicyE2EMaxDelayLowLimit_Type()
)
ocHnQosPolicyE2EMaxDelayLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyE2EMaxDelayLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    ocHnQosPolicyE2EMaxDelayLowLimit.setUnits("microseconds")
_OcHnQosPolicyBoundaryAddressType_Type = InetAddressType
_OcHnQosPolicyBoundaryAddressType_Object = MibTableColumn
ocHnQosPolicyBoundaryAddressType = _OcHnQosPolicyBoundaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 23),
    _OcHnQosPolicyBoundaryAddressType_Type()
)
ocHnQosPolicyBoundaryAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyBoundaryAddressType.setStatus("current")
_OcHnQosPolicyBoundarySourceAddressUpLimit_Type = InetAddress
_OcHnQosPolicyBoundarySourceAddressUpLimit_Object = MibTableColumn
ocHnQosPolicyBoundarySourceAddressUpLimit = _OcHnQosPolicyBoundarySourceAddressUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 24),
    _OcHnQosPolicyBoundarySourceAddressUpLimit_Type()
)
ocHnQosPolicyBoundarySourceAddressUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyBoundarySourceAddressUpLimit.setStatus("current")
_OcHnQosPolicyBoundarySourceAddressLowLimit_Type = InetAddress
_OcHnQosPolicyBoundarySourceAddressLowLimit_Object = MibTableColumn
ocHnQosPolicyBoundarySourceAddressLowLimit = _OcHnQosPolicyBoundarySourceAddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 25),
    _OcHnQosPolicyBoundarySourceAddressLowLimit_Type()
)
ocHnQosPolicyBoundarySourceAddressLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyBoundarySourceAddressLowLimit.setStatus("current")
_OcHnQosPolicyBoundaryDestinationAddressUpLimit_Type = InetAddress
_OcHnQosPolicyBoundaryDestinationAddressUpLimit_Object = MibTableColumn
ocHnQosPolicyBoundaryDestinationAddressUpLimit = _OcHnQosPolicyBoundaryDestinationAddressUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 26),
    _OcHnQosPolicyBoundaryDestinationAddressUpLimit_Type()
)
ocHnQosPolicyBoundaryDestinationAddressUpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyBoundaryDestinationAddressUpLimit.setStatus("current")
_OcHnQosPolicyBoundaryDestinationAddressLowLimit_Type = InetAddress
_OcHnQosPolicyBoundaryDestinationAddressLowLimit_Object = MibTableColumn
ocHnQosPolicyBoundaryDestinationAddressLowLimit = _OcHnQosPolicyBoundaryDestinationAddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 27),
    _OcHnQosPolicyBoundaryDestinationAddressLowLimit_Type()
)
ocHnQosPolicyBoundaryDestinationAddressLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyBoundaryDestinationAddressLowLimit.setStatus("current")
_OcHnQosPolicyUserName_Type = SnmpAdminString
_OcHnQosPolicyUserName_Object = MibTableColumn
ocHnQosPolicyUserName = _OcHnQosPolicyUserName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 28),
    _OcHnQosPolicyUserName_Type()
)
ocHnQosPolicyUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyUserName.setStatus("current")
_OcHnQosPolicyVendorApplicationName_Type = SnmpAdminString
_OcHnQosPolicyVendorApplicationName_Object = MibTableColumn
ocHnQosPolicyVendorApplicationName = _OcHnQosPolicyVendorApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 29),
    _OcHnQosPolicyVendorApplicationName_Type()
)
ocHnQosPolicyVendorApplicationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyVendorApplicationName.setStatus("current")
_OcHnQosPolicyPortName_Type = SnmpAdminString
_OcHnQosPolicyPortName_Object = MibTableColumn
ocHnQosPolicyPortName = _OcHnQosPolicyPortName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 30),
    _OcHnQosPolicyPortName_Type()
)
ocHnQosPolicyPortName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyPortName.setStatus("current")
_OcHnQosPolicyServiceProviderServiceName_Type = SnmpAdminString
_OcHnQosPolicyServiceProviderServiceName_Object = MibTableColumn
ocHnQosPolicyServiceProviderServiceName = _OcHnQosPolicyServiceProviderServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 31),
    _OcHnQosPolicyServiceProviderServiceName_Type()
)
ocHnQosPolicyServiceProviderServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyServiceProviderServiceName.setStatus("current")
_OcHnQosPolicyCriticalFlag_Type = TruthValue
_OcHnQosPolicyCriticalFlag_Object = MibTableColumn
ocHnQosPolicyCriticalFlag = _OcHnQosPolicyCriticalFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 32),
    _OcHnQosPolicyCriticalFlag_Type()
)
ocHnQosPolicyCriticalFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyCriticalFlag.setStatus("current")


class _OcHnQosPolicyRequestedQosType_Type(Integer32):
    """Custom type ocHnQosPolicyRequestedQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullyPrioritized", 1),
          ("hybrid", 2),
          ("fullyParameterized", 3))
    )


_OcHnQosPolicyRequestedQosType_Type.__name__ = "Integer32"
_OcHnQosPolicyRequestedQosType_Object = MibTableColumn
ocHnQosPolicyRequestedQosType = _OcHnQosPolicyRequestedQosType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 33),
    _OcHnQosPolicyRequestedQosType_Type()
)
ocHnQosPolicyRequestedQosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyRequestedQosType.setStatus("current")


class _OcHnQosPolicyStartTime_Type(Unsigned32):
    """Custom type ocHnQosPolicyStartTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_OcHnQosPolicyStartTime_Type.__name__ = "Unsigned32"
_OcHnQosPolicyStartTime_Object = MibTableColumn
ocHnQosPolicyStartTime = _OcHnQosPolicyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 34),
    _OcHnQosPolicyStartTime_Type()
)
ocHnQosPolicyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyStartTime.setStatus("current")


class _OcHnQosPolicyEndTime_Type(Unsigned32):
    """Custom type ocHnQosPolicyEndTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_OcHnQosPolicyEndTime_Type.__name__ = "Unsigned32"
_OcHnQosPolicyEndTime_Object = MibTableColumn
ocHnQosPolicyEndTime = _OcHnQosPolicyEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 35),
    _OcHnQosPolicyEndTime_Type()
)
ocHnQosPolicyEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyEndTime.setStatus("current")


class _OcHnQosPolicyTrafficLeaseTimeUpValue_Type(Unsigned32):
    """Custom type ocHnQosPolicyTrafficLeaseTimeUpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_OcHnQosPolicyTrafficLeaseTimeUpValue_Type.__name__ = "Unsigned32"
_OcHnQosPolicyTrafficLeaseTimeUpValue_Object = MibTableColumn
ocHnQosPolicyTrafficLeaseTimeUpValue = _OcHnQosPolicyTrafficLeaseTimeUpValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 36),
    _OcHnQosPolicyTrafficLeaseTimeUpValue_Type()
)
ocHnQosPolicyTrafficLeaseTimeUpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyTrafficLeaseTimeUpValue.setStatus("current")


class _OcHnQosPolicyTrafficLeaseTimeLowValue_Type(Unsigned32):
    """Custom type ocHnQosPolicyTrafficLeaseTimeLowValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_OcHnQosPolicyTrafficLeaseTimeLowValue_Type.__name__ = "Unsigned32"
_OcHnQosPolicyTrafficLeaseTimeLowValue_Object = MibTableColumn
ocHnQosPolicyTrafficLeaseTimeLowValue = _OcHnQosPolicyTrafficLeaseTimeLowValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 37),
    _OcHnQosPolicyTrafficLeaseTimeLowValue_Type()
)
ocHnQosPolicyTrafficLeaseTimeLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyTrafficLeaseTimeLowValue.setStatus("current")


class _OcHnQosPolicyRuleType_Type(Integer32):
    """Custom type ocHnQosPolicyRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operatorOnly", 0),
          ("homeUser", 1),
          ("operatorForHomeUser", 2),
          ("other", 3))
    )


_OcHnQosPolicyRuleType_Type.__name__ = "Integer32"
_OcHnQosPolicyRuleType_Object = MibTableColumn
ocHnQosPolicyRuleType = _OcHnQosPolicyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 38),
    _OcHnQosPolicyRuleType_Type()
)
ocHnQosPolicyRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyRuleType.setStatus("current")


class _OcHnQosPolicyRulePriority_Type(Unsigned32):
    """Custom type ocHnQosPolicyRulePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OcHnQosPolicyRulePriority_Type.__name__ = "Unsigned32"
_OcHnQosPolicyRulePriority_Object = MibTableColumn
ocHnQosPolicyRulePriority = _OcHnQosPolicyRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 39),
    _OcHnQosPolicyRulePriority_Type()
)
ocHnQosPolicyRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyRulePriority.setStatus("current")


class _OcHnQosPolicyTrafficImportanceNumber_Type(Unsigned32):
    """Custom type ocHnQosPolicyTrafficImportanceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_OcHnQosPolicyTrafficImportanceNumber_Type.__name__ = "Unsigned32"
_OcHnQosPolicyTrafficImportanceNumber_Object = MibTableColumn
ocHnQosPolicyTrafficImportanceNumber = _OcHnQosPolicyTrafficImportanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 40),
    _OcHnQosPolicyTrafficImportanceNumber_Type()
)
ocHnQosPolicyTrafficImportanceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyTrafficImportanceNumber.setStatus("current")


class _OcHnQosPolicyUserImportanceNumber_Type(Unsigned32):
    """Custom type ocHnQosPolicyUserImportanceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OcHnQosPolicyUserImportanceNumber_Type.__name__ = "Unsigned32"
_OcHnQosPolicyUserImportanceNumber_Object = MibTableColumn
ocHnQosPolicyUserImportanceNumber = _OcHnQosPolicyUserImportanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 2, 1, 41),
    _OcHnQosPolicyUserImportanceNumber_Type()
)
ocHnQosPolicyUserImportanceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosPolicyUserImportanceNumber.setStatus("current")
_OcHnQosROStatsTable_Object = MibTable
ocHnQosROStatsTable = _OcHnQosROStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ocHnQosROStatsTable.setStatus("current")
_OcHnQosROStatsEntry_Object = MibTableRow
ocHnQosROStatsEntry = _OcHnQosROStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1)
)
ocHnQosROStatsEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnQosROStatsIndex"),
)
if mibBuilder.loadTexts:
    ocHnQosROStatsEntry.setStatus("current")


class _OcHnQosROStatsIndex_Type(Unsigned32):
    """Custom type ocHnQosROStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnQosROStatsIndex_Type.__name__ = "Unsigned32"
_OcHnQosROStatsIndex_Object = MibTableColumn
ocHnQosROStatsIndex = _OcHnQosROStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 1),
    _OcHnQosROStatsIndex_Type()
)
ocHnQosROStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnQosROStatsIndex.setStatus("current")
_OcHnQosROStatsIdentifier_Type = Unsigned32
_OcHnQosROStatsIdentifier_Object = MibTableColumn
ocHnQosROStatsIdentifier = _OcHnQosROStatsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 2),
    _OcHnQosROStatsIdentifier_Type()
)
ocHnQosROStatsIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsIdentifier.setStatus("current")
_OcHnQosROStatsMacAddress_Type = MacAddress
_OcHnQosROStatsMacAddress_Object = MibTableColumn
ocHnQosROStatsMacAddress = _OcHnQosROStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 3),
    _OcHnQosROStatsMacAddress_Type()
)
ocHnQosROStatsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsMacAddress.setStatus("current")
_OcHnQosROStatsObservationMacAddress_Type = MacAddress
_OcHnQosROStatsObservationMacAddress_Object = MibTableColumn
ocHnQosROStatsObservationMacAddress = _OcHnQosROStatsObservationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 4),
    _OcHnQosROStatsObservationMacAddress_Type()
)
ocHnQosROStatsObservationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsObservationMacAddress.setStatus("current")
_OcHnQosROStatsQosSegmentId_Type = OctetString
_OcHnQosROStatsQosSegmentId_Object = MibTableColumn
ocHnQosROStatsQosSegmentId = _OcHnQosROStatsQosSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 5),
    _OcHnQosROStatsQosSegmentId_Type()
)
ocHnQosROStatsQosSegmentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnQosROStatsQosSegmentId.setStatus("current")
_OcHnQosROStatsTotalTrafficBytes_Type = Counter32
_OcHnQosROStatsTotalTrafficBytes_Object = MibTableColumn
ocHnQosROStatsTotalTrafficBytes = _OcHnQosROStatsTotalTrafficBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 6),
    _OcHnQosROStatsTotalTrafficBytes_Type()
)
ocHnQosROStatsTotalTrafficBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsTotalTrafficBytes.setStatus("current")
_OcHnQosROStatsTotalParameterizedBytes_Type = Counter32
_OcHnQosROStatsTotalParameterizedBytes_Object = MibTableColumn
ocHnQosROStatsTotalParameterizedBytes = _OcHnQosROStatsTotalParameterizedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 7),
    _OcHnQosROStatsTotalParameterizedBytes_Type()
)
ocHnQosROStatsTotalParameterizedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsTotalParameterizedBytes.setStatus("current")
_OcHnQosROStatsTotalParameterizedPackets_Type = Counter32
_OcHnQosROStatsTotalParameterizedPackets_Object = MibTableColumn
ocHnQosROStatsTotalParameterizedPackets = _OcHnQosROStatsTotalParameterizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 8),
    _OcHnQosROStatsTotalParameterizedPackets_Type()
)
ocHnQosROStatsTotalParameterizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsTotalParameterizedPackets.setStatus("current")
_OcHnQosROStatsTotalParameterizedPacketsDropped_Type = Counter32
_OcHnQosROStatsTotalParameterizedPacketsDropped_Object = MibTableColumn
ocHnQosROStatsTotalParameterizedPacketsDropped = _OcHnQosROStatsTotalParameterizedPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 9),
    _OcHnQosROStatsTotalParameterizedPacketsDropped_Type()
)
ocHnQosROStatsTotalParameterizedPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsTotalParameterizedPacketsDropped.setStatus("current")
_OcHnQosROStatsReportingDateAndTime_Type = SnmpAdminString
_OcHnQosROStatsReportingDateAndTime_Object = MibTableColumn
ocHnQosROStatsReportingDateAndTime = _OcHnQosROStatsReportingDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 10),
    _OcHnQosROStatsReportingDateAndTime_Type()
)
ocHnQosROStatsReportingDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsReportingDateAndTime.setStatus("current")
_OcHnQosROStatsObservationPeriod_Type = Unsigned32
_OcHnQosROStatsObservationPeriod_Object = MibTableColumn
ocHnQosROStatsObservationPeriod = _OcHnQosROStatsObservationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 11),
    _OcHnQosROStatsObservationPeriod_Type()
)
ocHnQosROStatsObservationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsObservationPeriod.setStatus("current")
_OcHnQosROStatsMonitorResolutionPeriod_Type = Unsigned32
_OcHnQosROStatsMonitorResolutionPeriod_Object = MibTableColumn
ocHnQosROStatsMonitorResolutionPeriod = _OcHnQosROStatsMonitorResolutionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 3, 1, 12),
    _OcHnQosROStatsMonitorResolutionPeriod_Type()
)
ocHnQosROStatsMonitorResolutionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosROStatsMonitorResolutionPeriod.setStatus("current")
_OcHnQosStreamStatisticsTable_Object = MibTable
ocHnQosStreamStatisticsTable = _OcHnQosStreamStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsTable.setStatus("current")
_OcHnQosStreamStatisticsEntry_Object = MibTableRow
ocHnQosStreamStatisticsEntry = _OcHnQosStreamStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1)
)
ocHnQosStreamStatisticsEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnQosROStatsIndex"),
)
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsEntry.setStatus("current")
_OcHnQosStreamStatisticsTrafficHandle_Type = OctetString
_OcHnQosStreamStatisticsTrafficHandle_Object = MibTableColumn
ocHnQosStreamStatisticsTrafficHandle = _OcHnQosStreamStatisticsTrafficHandle_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 1),
    _OcHnQosStreamStatisticsTrafficHandle_Type()
)
ocHnQosStreamStatisticsTrafficHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsTrafficHandle.setStatus("current")


class _OcHnQosStreamStatisticsLayer2StreamId_Type(OctetString):
    """Custom type ocHnQosStreamStatisticsLayer2StreamId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixedLength = 64


_OcHnQosStreamStatisticsLayer2StreamId_Type.__name__ = "OctetString"
_OcHnQosStreamStatisticsLayer2StreamId_Object = MibTableColumn
ocHnQosStreamStatisticsLayer2StreamId = _OcHnQosStreamStatisticsLayer2StreamId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 2),
    _OcHnQosStreamStatisticsLayer2StreamId_Type()
)
ocHnQosStreamStatisticsLayer2StreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsLayer2StreamId.setStatus("current")
_OcHnQosStreamStatisticsPktsTransmitted_Type = Counter32
_OcHnQosStreamStatisticsPktsTransmitted_Object = MibTableColumn
ocHnQosStreamStatisticsPktsTransmitted = _OcHnQosStreamStatisticsPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 3),
    _OcHnQosStreamStatisticsPktsTransmitted_Type()
)
ocHnQosStreamStatisticsPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsPktsTransmitted.setStatus("current")
_OcHnQosStreamStatisticsPktsReceived_Type = Counter32
_OcHnQosStreamStatisticsPktsReceived_Object = MibTableColumn
ocHnQosStreamStatisticsPktsReceived = _OcHnQosStreamStatisticsPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 4),
    _OcHnQosStreamStatisticsPktsReceived_Type()
)
ocHnQosStreamStatisticsPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsPktsReceived.setStatus("current")
_OcHnQosStreamStatisticsErrorPktsDropped_Type = Counter32
_OcHnQosStreamStatisticsErrorPktsDropped_Object = MibTableColumn
ocHnQosStreamStatisticsErrorPktsDropped = _OcHnQosStreamStatisticsErrorPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 5),
    _OcHnQosStreamStatisticsErrorPktsDropped_Type()
)
ocHnQosStreamStatisticsErrorPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsErrorPktsDropped.setStatus("current")
_OcHnQosStreamStatisticsBytesTransmitted_Type = Counter32
_OcHnQosStreamStatisticsBytesTransmitted_Object = MibTableColumn
ocHnQosStreamStatisticsBytesTransmitted = _OcHnQosStreamStatisticsBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 6),
    _OcHnQosStreamStatisticsBytesTransmitted_Type()
)
ocHnQosStreamStatisticsBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsBytesTransmitted.setStatus("current")
_OcHnQosStreamStatisticsBytesReceived_Type = Counter32
_OcHnQosStreamStatisticsBytesReceived_Object = MibTableColumn
ocHnQosStreamStatisticsBytesReceived = _OcHnQosStreamStatisticsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 7),
    _OcHnQosStreamStatisticsBytesReceived_Type()
)
ocHnQosStreamStatisticsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsBytesReceived.setStatus("current")
_OcHnQosStreamStatisticsPeakDataRateViolations_Type = TruthValue
_OcHnQosStreamStatisticsPeakDataRateViolations_Object = MibTableColumn
ocHnQosStreamStatisticsPeakDataRateViolations = _OcHnQosStreamStatisticsPeakDataRateViolations_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 4, 1, 8),
    _OcHnQosStreamStatisticsPeakDataRateViolations_Type()
)
ocHnQosStreamStatisticsPeakDataRateViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosStreamStatisticsPeakDataRateViolations.setStatus("current")
_OcHnQosPriorityTrafficTable_Object = MibTable
ocHnQosPriorityTrafficTable = _OcHnQosPriorityTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    ocHnQosPriorityTrafficTable.setStatus("current")
_OcHnQosPriorityTrafficEntry_Object = MibTableRow
ocHnQosPriorityTrafficEntry = _OcHnQosPriorityTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1)
)
ocHnQosPriorityTrafficEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnQosROStatsIndex"),
)
if mibBuilder.loadTexts:
    ocHnQosPriorityTrafficEntry.setStatus("current")
_OcHnQosTrafficTotalBytesPriority0_Type = Counter32
_OcHnQosTrafficTotalBytesPriority0_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority0 = _OcHnQosTrafficTotalBytesPriority0_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 1),
    _OcHnQosTrafficTotalBytesPriority0_Type()
)
ocHnQosTrafficTotalBytesPriority0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority0.setStatus("current")
_OcHnQosTrafficTotalBytesPriority1_Type = Counter32
_OcHnQosTrafficTotalBytesPriority1_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority1 = _OcHnQosTrafficTotalBytesPriority1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 2),
    _OcHnQosTrafficTotalBytesPriority1_Type()
)
ocHnQosTrafficTotalBytesPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority1.setStatus("current")
_OcHnQosTrafficTotalBytesPriority2_Type = Counter32
_OcHnQosTrafficTotalBytesPriority2_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority2 = _OcHnQosTrafficTotalBytesPriority2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 3),
    _OcHnQosTrafficTotalBytesPriority2_Type()
)
ocHnQosTrafficTotalBytesPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority2.setStatus("current")
_OcHnQosTrafficTotalBytesPriority3_Type = Counter32
_OcHnQosTrafficTotalBytesPriority3_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority3 = _OcHnQosTrafficTotalBytesPriority3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 4),
    _OcHnQosTrafficTotalBytesPriority3_Type()
)
ocHnQosTrafficTotalBytesPriority3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority3.setStatus("current")
_OcHnQosTrafficTotalBytesPriority4_Type = Counter32
_OcHnQosTrafficTotalBytesPriority4_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority4 = _OcHnQosTrafficTotalBytesPriority4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 5),
    _OcHnQosTrafficTotalBytesPriority4_Type()
)
ocHnQosTrafficTotalBytesPriority4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority4.setStatus("current")
_OcHnQosTrafficTotalBytesPriority5_Type = Counter32
_OcHnQosTrafficTotalBytesPriority5_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority5 = _OcHnQosTrafficTotalBytesPriority5_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 6),
    _OcHnQosTrafficTotalBytesPriority5_Type()
)
ocHnQosTrafficTotalBytesPriority5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority5.setStatus("current")
_OcHnQosTrafficTotalBytesPriority6_Type = Counter32
_OcHnQosTrafficTotalBytesPriority6_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority6 = _OcHnQosTrafficTotalBytesPriority6_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 7),
    _OcHnQosTrafficTotalBytesPriority6_Type()
)
ocHnQosTrafficTotalBytesPriority6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority6.setStatus("current")
_OcHnQosTrafficTotalBytesPriority7_Type = Counter32
_OcHnQosTrafficTotalBytesPriority7_Object = MibTableColumn
ocHnQosTrafficTotalBytesPriority7 = _OcHnQosTrafficTotalBytesPriority7_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 5, 1, 8),
    _OcHnQosTrafficTotalBytesPriority7_Type()
)
ocHnQosTrafficTotalBytesPriority7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnQosTrafficTotalBytesPriority7.setStatus("current")
_OcHnStaticPQosConfiguration_ObjectIdentity = ObjectIdentity
ocHnStaticPQosConfiguration = _OcHnStaticPQosConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6)
)
_OcHnStaticPQosStatus_Type = TruthValue
_OcHnStaticPQosStatus_Object = MibScalar
ocHnStaticPQosStatus = _OcHnStaticPQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6, 1),
    _OcHnStaticPQosStatus_Type()
)
ocHnStaticPQosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnStaticPQosStatus.setStatus("current")
_OcHnStaticPQosDeviceTable_Object = MibTable
ocHnStaticPQosDeviceTable = _OcHnStaticPQosDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    ocHnStaticPQosDeviceTable.setStatus("current")
_OcHnStaticPQosDeviceEntry_Object = MibTableRow
ocHnStaticPQosDeviceEntry = _OcHnStaticPQosDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6, 2, 1)
)
ocHnStaticPQosDeviceEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnStaticPQosDeviceIndex"),
)
if mibBuilder.loadTexts:
    ocHnStaticPQosDeviceEntry.setStatus("current")


class _OcHnStaticPQosDeviceIndex_Type(Unsigned32):
    """Custom type ocHnStaticPQosDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnStaticPQosDeviceIndex_Type.__name__ = "Unsigned32"
_OcHnStaticPQosDeviceIndex_Object = MibTableColumn
ocHnStaticPQosDeviceIndex = _OcHnStaticPQosDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6, 2, 1, 1),
    _OcHnStaticPQosDeviceIndex_Type()
)
ocHnStaticPQosDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnStaticPQosDeviceIndex.setStatus("current")
_OcHnStaticPQosDeviceRowStatus_Type = RowStatus
_OcHnStaticPQosDeviceRowStatus_Object = MibTableColumn
ocHnStaticPQosDeviceRowStatus = _OcHnStaticPQosDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6, 2, 1, 2),
    _OcHnStaticPQosDeviceRowStatus_Type()
)
ocHnStaticPQosDeviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnStaticPQosDeviceRowStatus.setStatus("current")
_OcHnStaticPQosDeviceActive_Type = TruthValue
_OcHnStaticPQosDeviceActive_Object = MibTableColumn
ocHnStaticPQosDeviceActive = _OcHnStaticPQosDeviceActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6, 2, 1, 3),
    _OcHnStaticPQosDeviceActive_Type()
)
ocHnStaticPQosDeviceActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnStaticPQosDeviceActive.setStatus("current")
_OcHnStaticPQosDeviceMACAddress_Type = MacAddress
_OcHnStaticPQosDeviceMACAddress_Object = MibTableColumn
ocHnStaticPQosDeviceMACAddress = _OcHnStaticPQosDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 3, 6, 2, 1, 4),
    _OcHnStaticPQosDeviceMACAddress_Type()
)
ocHnStaticPQosDeviceMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ocHnStaticPQosDeviceMACAddress.setStatus("current")
_OcHnDevInterfaceStatus_ObjectIdentity = ObjectIdentity
ocHnDevInterfaceStatus = _OcHnDevInterfaceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4)
)
_OcHnDevInterfaceConfigTable_Object = MibTable
ocHnDevInterfaceConfigTable = _OcHnDevInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ocHnDevInterfaceConfigTable.setStatus("current")
_OcHnDevInterfaceConfigEntry_Object = MibTableRow
ocHnDevInterfaceConfigEntry = _OcHnDevInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 1, 1)
)
ocHnDevInterfaceConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ocHnDevInterfaceConfigEntry.setStatus("current")
_OcHnDevInterfaceConfigMaxPowerLevel_Type = Integer32
_OcHnDevInterfaceConfigMaxPowerLevel_Object = MibTableColumn
ocHnDevInterfaceConfigMaxPowerLevel = _OcHnDevInterfaceConfigMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 1, 1, 2),
    _OcHnDevInterfaceConfigMaxPowerLevel_Type()
)
ocHnDevInterfaceConfigMaxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnDevInterfaceConfigMaxPowerLevel.setStatus("current")
_OcHnDevInterfaceConfigPowerUnits_Type = PowerUnit
_OcHnDevInterfaceConfigPowerUnits_Object = MibTableColumn
ocHnDevInterfaceConfigPowerUnits = _OcHnDevInterfaceConfigPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 1, 1, 3),
    _OcHnDevInterfaceConfigPowerUnits_Type()
)
ocHnDevInterfaceConfigPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevInterfaceConfigPowerUnits.setStatus("current")
_OcHnDevInterfaceConfigMaxParameterizedBandwidth_Type = Unsigned32
_OcHnDevInterfaceConfigMaxParameterizedBandwidth_Object = MibTableColumn
ocHnDevInterfaceConfigMaxParameterizedBandwidth = _OcHnDevInterfaceConfigMaxParameterizedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 1, 1, 4),
    _OcHnDevInterfaceConfigMaxParameterizedBandwidth_Type()
)
ocHnDevInterfaceConfigMaxParameterizedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnDevInterfaceConfigMaxParameterizedBandwidth.setStatus("current")


class _OcHnDevInterfaceConfigEnableEncryption_Type(Integer32):
    """Custom type ocHnDevInterfaceConfigEnableEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_OcHnDevInterfaceConfigEnableEncryption_Type.__name__ = "Integer32"
_OcHnDevInterfaceConfigEnableEncryption_Object = MibTableColumn
ocHnDevInterfaceConfigEnableEncryption = _OcHnDevInterfaceConfigEnableEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 1, 1, 5),
    _OcHnDevInterfaceConfigEnableEncryption_Type()
)
ocHnDevInterfaceConfigEnableEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnDevInterfaceConfigEnableEncryption.setStatus("current")


class _OcHnDevInterfaceConfigEncryptionPassphrase_Type(SnmpAdminString):
    """Custom type ocHnDevInterfaceConfigEncryptionPassphrase based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
        ValueSizeConstraint(32, 32),
    )


_OcHnDevInterfaceConfigEncryptionPassphrase_Type.__name__ = "SnmpAdminString"
_OcHnDevInterfaceConfigEncryptionPassphrase_Object = MibTableColumn
ocHnDevInterfaceConfigEncryptionPassphrase = _OcHnDevInterfaceConfigEncryptionPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 1, 1, 6),
    _OcHnDevInterfaceConfigEncryptionPassphrase_Type()
)
ocHnDevInterfaceConfigEncryptionPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnDevInterfaceConfigEncryptionPassphrase.setStatus("current")
_OcHnDevInterfaceStatusTable_Object = MibTable
ocHnDevInterfaceStatusTable = _OcHnDevInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusTable.setStatus("current")
_OcHnDevInterfaceStatusEntry_Object = MibTableRow
ocHnDevInterfaceStatusEntry = _OcHnDevInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2, 1)
)
ocHnDevInterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusEntry.setStatus("current")
_OcHnDevInterfaceStatusTxBroadcastRate_Type = Unsigned32
_OcHnDevInterfaceStatusTxBroadcastRate_Object = MibTableColumn
ocHnDevInterfaceStatusTxBroadcastRate = _OcHnDevInterfaceStatusTxBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2, 1, 1),
    _OcHnDevInterfaceStatusTxBroadcastRate_Type()
)
ocHnDevInterfaceStatusTxBroadcastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusTxBroadcastRate.setStatus("current")
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusTxBroadcastRate.setUnits("bits/sec")
_OcHnDevInterfaceStatusTxBroadcastLevel_Type = Tenths
_OcHnDevInterfaceStatusTxBroadcastLevel_Object = MibTableColumn
ocHnDevInterfaceStatusTxBroadcastLevel = _OcHnDevInterfaceStatusTxBroadcastLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2, 1, 2),
    _OcHnDevInterfaceStatusTxBroadcastLevel_Type()
)
ocHnDevInterfaceStatusTxBroadcastLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusTxBroadcastLevel.setStatus("current")
_OcHnDevInterfaceStatusMaxTxPowerLevel_Type = Tenths
_OcHnDevInterfaceStatusMaxTxPowerLevel_Object = MibTableColumn
ocHnDevInterfaceStatusMaxTxPowerLevel = _OcHnDevInterfaceStatusMaxTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2, 1, 3),
    _OcHnDevInterfaceStatusMaxTxPowerLevel_Type()
)
ocHnDevInterfaceStatusMaxTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusMaxTxPowerLevel.setStatus("current")
_OcHnDevInterfaceStatusPowerUnits_Type = PowerUnit
_OcHnDevInterfaceStatusPowerUnits_Object = MibTableColumn
ocHnDevInterfaceStatusPowerUnits = _OcHnDevInterfaceStatusPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2, 1, 4),
    _OcHnDevInterfaceStatusPowerUnits_Type()
)
ocHnDevInterfaceStatusPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusPowerUnits.setStatus("current")
_OcHnDevInterfaceStatusMaxParameterizedBandwidth_Type = Unsigned32
_OcHnDevInterfaceStatusMaxParameterizedBandwidth_Object = MibTableColumn
ocHnDevInterfaceStatusMaxParameterizedBandwidth = _OcHnDevInterfaceStatusMaxParameterizedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2, 1, 5),
    _OcHnDevInterfaceStatusMaxParameterizedBandwidth_Type()
)
ocHnDevInterfaceStatusMaxParameterizedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusMaxParameterizedBandwidth.setStatus("current")
_OcHnDevInterfaceStatusLayer2Scheduler_Type = TruthValue
_OcHnDevInterfaceStatusLayer2Scheduler_Object = MibTableColumn
ocHnDevInterfaceStatusLayer2Scheduler = _OcHnDevInterfaceStatusLayer2Scheduler_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 2, 1, 6),
    _OcHnDevInterfaceStatusLayer2Scheduler_Type()
)
ocHnDevInterfaceStatusLayer2Scheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevInterfaceStatusLayer2Scheduler.setStatus("current")
_OcHnDevConnectionTable_Object = MibTable
ocHnDevConnectionTable = _OcHnDevConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    ocHnDevConnectionTable.setStatus("current")
_OcHnDevConnectionEntry_Object = MibTableRow
ocHnDevConnectionEntry = _OcHnDevConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1)
)
ocHnDevConnectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OC-HOME-NETWORK-MIB", "ocHnDevConnectionIndex"),
)
if mibBuilder.loadTexts:
    ocHnDevConnectionEntry.setStatus("current")


class _OcHnDevConnectionIndex_Type(Unsigned32):
    """Custom type ocHnDevConnectionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcHnDevConnectionIndex_Type.__name__ = "Unsigned32"
_OcHnDevConnectionIndex_Object = MibTableColumn
ocHnDevConnectionIndex = _OcHnDevConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 1),
    _OcHnDevConnectionIndex_Type()
)
ocHnDevConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnDevConnectionIndex.setStatus("current")
_OcHnDevConnectionDestMac_Type = MacAddress
_OcHnDevConnectionDestMac_Object = MibTableColumn
ocHnDevConnectionDestMac = _OcHnDevConnectionDestMac_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 2),
    _OcHnDevConnectionDestMac_Type()
)
ocHnDevConnectionDestMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionDestMac.setStatus("current")
_OcHnDevConnectionRxLinkRate_Type = Unsigned32
_OcHnDevConnectionRxLinkRate_Object = MibTableColumn
ocHnDevConnectionRxLinkRate = _OcHnDevConnectionRxLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 3),
    _OcHnDevConnectionRxLinkRate_Type()
)
ocHnDevConnectionRxLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionRxLinkRate.setStatus("current")
if mibBuilder.loadTexts:
    ocHnDevConnectionRxLinkRate.setUnits("bits/sec")
_OcHnDevConnectionRxModulationType_Type = SnmpAdminString
_OcHnDevConnectionRxModulationType_Object = MibTableColumn
ocHnDevConnectionRxModulationType = _OcHnDevConnectionRxModulationType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 4),
    _OcHnDevConnectionRxModulationType_Type()
)
ocHnDevConnectionRxModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionRxModulationType.setStatus("current")
_OcHnDevConnectionRxBroadcastRate_Type = Unsigned32
_OcHnDevConnectionRxBroadcastRate_Object = MibTableColumn
ocHnDevConnectionRxBroadcastRate = _OcHnDevConnectionRxBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 5),
    _OcHnDevConnectionRxBroadcastRate_Type()
)
ocHnDevConnectionRxBroadcastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionRxBroadcastRate.setStatus("current")
if mibBuilder.loadTexts:
    ocHnDevConnectionRxBroadcastRate.setUnits("bits/sec")
_OcHnDevConnectionRxSignalStrength_Type = Tenths
_OcHnDevConnectionRxSignalStrength_Object = MibTableColumn
ocHnDevConnectionRxSignalStrength = _OcHnDevConnectionRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 6),
    _OcHnDevConnectionRxSignalStrength_Type()
)
ocHnDevConnectionRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionRxSignalStrength.setStatus("current")
_OcHnDevConnectionTxUnicastLevel_Type = Tenths
_OcHnDevConnectionTxUnicastLevel_Object = MibTableColumn
ocHnDevConnectionTxUnicastLevel = _OcHnDevConnectionTxUnicastLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 7),
    _OcHnDevConnectionTxUnicastLevel_Type()
)
ocHnDevConnectionTxUnicastLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionTxUnicastLevel.setStatus("current")
_OcHnDevConnectionPowerUnits_Type = PowerUnit
_OcHnDevConnectionPowerUnits_Object = MibTableColumn
ocHnDevConnectionPowerUnits = _OcHnDevConnectionPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 8),
    _OcHnDevConnectionPowerUnits_Type()
)
ocHnDevConnectionPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionPowerUnits.setStatus("current")
_OcHnDevConnectionTxLinkRate_Type = Unsigned32
_OcHnDevConnectionTxLinkRate_Object = MibTableColumn
ocHnDevConnectionTxLinkRate = _OcHnDevConnectionTxLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 9),
    _OcHnDevConnectionTxLinkRate_Type()
)
ocHnDevConnectionTxLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionTxLinkRate.setStatus("current")
if mibBuilder.loadTexts:
    ocHnDevConnectionTxLinkRate.setUnits("bits/sec")
_OcHnDevConnectionTxModulationType_Type = SnmpAdminString
_OcHnDevConnectionTxModulationType_Object = MibTableColumn
ocHnDevConnectionTxModulationType = _OcHnDevConnectionTxModulationType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 4, 3, 1, 10),
    _OcHnDevConnectionTxModulationType_Type()
)
ocHnDevConnectionTxModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnDevConnectionTxModulationType.setStatus("current")
_OcHnNetConfig_ObjectIdentity = ObjectIdentity
ocHnNetConfig = _OcHnNetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5)
)
_OcHnNetConfigViewPrimaryOutputPort_Type = TruthValue
_OcHnNetConfigViewPrimaryOutputPort_Object = MibScalar
ocHnNetConfigViewPrimaryOutputPort = _OcHnNetConfigViewPrimaryOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 1),
    _OcHnNetConfigViewPrimaryOutputPort_Type()
)
ocHnNetConfigViewPrimaryOutputPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnNetConfigViewPrimaryOutputPort.setStatus("current")
_OcHnNetConfigViewPrimaryOutputPortOrgID_Type = Unsigned32
_OcHnNetConfigViewPrimaryOutputPortOrgID_Object = MibScalar
ocHnNetConfigViewPrimaryOutputPortOrgID = _OcHnNetConfigViewPrimaryOutputPortOrgID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 2),
    _OcHnNetConfigViewPrimaryOutputPortOrgID_Type()
)
ocHnNetConfigViewPrimaryOutputPortOrgID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnNetConfigViewPrimaryOutputPortOrgID.setStatus("current")
_OcHnIPAddressPrefixTable_Object = MibTable
ocHnIPAddressPrefixTable = _OcHnIPAddressPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixTable.setStatus("current")
_OcHnIPAddressPrefixEntry_Object = MibTableRow
ocHnIPAddressPrefixEntry = _OcHnIPAddressPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3, 1)
)
ocHnIPAddressPrefixEntry.setIndexNames(
    (0, "OC-HOME-NETWORK-MIB", "ocHnIPAddressPrefixIndex"),
)
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixEntry.setStatus("current")


class _OcHnIPAddressPrefixIndex_Type(Integer32):
    """Custom type ocHnIPAddressPrefixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OcHnIPAddressPrefixIndex_Type.__name__ = "Integer32"
_OcHnIPAddressPrefixIndex_Object = MibTableColumn
ocHnIPAddressPrefixIndex = _OcHnIPAddressPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3, 1, 1),
    _OcHnIPAddressPrefixIndex_Type()
)
ocHnIPAddressPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixIndex.setStatus("current")


class _OcHnIPAddressPrefixInterfaceNumber_Type(Integer32):
    """Custom type ocHnIPAddressPrefixInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 2147483647),
    )


_OcHnIPAddressPrefixInterfaceNumber_Type.__name__ = "Integer32"
_OcHnIPAddressPrefixInterfaceNumber_Object = MibTableColumn
ocHnIPAddressPrefixInterfaceNumber = _OcHnIPAddressPrefixInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3, 1, 2),
    _OcHnIPAddressPrefixInterfaceNumber_Type()
)
ocHnIPAddressPrefixInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixInterfaceNumber.setStatus("current")
_OcHnIPAddressPrefixType_Type = InetAddressType
_OcHnIPAddressPrefixType_Object = MibTableColumn
ocHnIPAddressPrefixType = _OcHnIPAddressPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3, 1, 3),
    _OcHnIPAddressPrefixType_Type()
)
ocHnIPAddressPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixType.setStatus("current")
_OcHnIPAddressPrefixLength_Type = InetAddressPrefixLength
_OcHnIPAddressPrefixLength_Object = MibTableColumn
ocHnIPAddressPrefixLength = _OcHnIPAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3, 1, 4),
    _OcHnIPAddressPrefixLength_Type()
)
ocHnIPAddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixLength.setStatus("current")
_OcHnIPAddressPrefixPrefix_Type = InetAddress
_OcHnIPAddressPrefixPrefix_Object = MibTableColumn
ocHnIPAddressPrefixPrefix = _OcHnIPAddressPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3, 1, 5),
    _OcHnIPAddressPrefixPrefix_Type()
)
ocHnIPAddressPrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixPrefix.setStatus("current")
_OcHnIPAddressPrefixPolicy_Type = TruthValue
_OcHnIPAddressPrefixPolicy_Object = MibTableColumn
ocHnIPAddressPrefixPolicy = _OcHnIPAddressPrefixPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 3, 1, 6),
    _OcHnIPAddressPrefixPolicy_Type()
)
ocHnIPAddressPrefixPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocHnIPAddressPrefixPolicy.setStatus("current")
_OcHnNetConfigPersistentLinkLocalAddress_Type = TruthValue
_OcHnNetConfigPersistentLinkLocalAddress_Object = MibScalar
ocHnNetConfigPersistentLinkLocalAddress = _OcHnNetConfigPersistentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 2, 5, 4),
    _OcHnNetConfigPersistentLinkLocalAddress_Type()
)
ocHnNetConfigPersistentLinkLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocHnNetConfigPersistentLinkLocalAddress.setStatus("current")
_OcHnConformance_ObjectIdentity = ObjectIdentity
ocHnConformance = _OcHnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3)
)
_OcHnMIBCompliances_ObjectIdentity = ObjectIdentity
ocHnMIBCompliances = _OcHnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 1)
)
_OcHnMIBGroups_ObjectIdentity = ObjectIdentity
ocHnMIBGroups = _OcHnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 2)
)

# Managed Objects groups

ocHnHomeNetworkStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 2, 1)
)
ocHnHomeNetworkStatusGroup.setObjects(
      *(("OC-HOME-NETWORK-MIB", "ocHnRsdManagerImportanceNumber"),
        ("OC-HOME-NETWORK-MIB", "ocHnRsdManagerPreferredStatus"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevUpnpServiceType"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevUpnpServiceAvailable"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevSupportedChannelLastOperatingFreq"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevSupportedChannelInUse"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevSupportedChannelFrequency"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevSupportedChannelEligible"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevPropertiesFriendlyName"))
)
if mibBuilder.loadTexts:
    ocHnHomeNetworkStatusGroup.setStatus("current")

ocHnGenericDevInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 2, 2)
)
ocHnGenericDevInterfaceGroup.setObjects(
      *(("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceConfigMaxPowerLevel"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceConfigPowerUnits"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceConfigMaxParameterizedBandwidth"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceConfigEnableEncryption"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceConfigEncryptionPassphrase"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceStatusLayer2Scheduler"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceStatusTxBroadcastLevel"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceStatusTxBroadcastRate"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceStatusMaxTxPowerLevel"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceStatusPowerUnits"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevInterfaceStatusMaxParameterizedBandwidth"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionDestMac"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionRxLinkRate"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionRxModulationType"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionRxBroadcastRate"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionRxSignalStrength"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionPowerUnits"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionTxUnicastLevel"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionTxLinkRate"),
        ("OC-HOME-NETWORK-MIB", "ocHnDevConnectionTxModulationType"))
)
if mibBuilder.loadTexts:
    ocHnGenericDevInterfaceGroup.setStatus("current")

ocHnRotameterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 2, 3)
)
ocHnRotameterConfigGroup.setObjects(
      *(("OC-HOME-NETWORK-MIB", "ocHnRotameterConfigRowStatus"),
        ("OC-HOME-NETWORK-MIB", "ocHnRotameterConfigQosSegmentId"),
        ("OC-HOME-NETWORK-MIB", "ocHnRotameterConfigObservationActive"),
        ("OC-HOME-NETWORK-MIB", "ocHnRotameterConfigEndpointMacAddress"),
        ("OC-HOME-NETWORK-MIB", "ocHnRotameterConfigPeriod"),
        ("OC-HOME-NETWORK-MIB", "ocHnRotameterConfigMonitorResolutionPeriod"),
        ("OC-HOME-NETWORK-MIB", "ocHnPerStreamRotameterConfigRowStatus"),
        ("OC-HOME-NETWORK-MIB", "ocHnPerStreamRotameterConfigLayer2StreamId"),
        ("OC-HOME-NETWORK-MIB", "ocHnPerStreamRotameterConfigTrafficHandle"),
        ("OC-HOME-NETWORK-MIB", "ocHnPerStreamRotameterConfigObservationActive"))
)
if mibBuilder.loadTexts:
    ocHnRotameterConfigGroup.setStatus("current")

ocHnQosTrafficDescInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 2, 4)
)
ocHnQosTrafficDescInfo.setObjects(
      *(("OC-HOME-NETWORK-MIB", "ocHnQosStreamsInfoCollectionTrigger"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficQDMacAddress"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficHandle"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficNetworkAddressType"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficSourceAddress"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficSourcePort"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficDestinationAddress"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficDestinationPort"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficIpProtocol"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficV3TrafficIdSourceUuid"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficV3TrafficIdDestinationUuid"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficMediaServerConnectionId"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficMediaRendererConnectionId"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficLeaseTime"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficCritical"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficUserName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficVendorApplicationName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficPortName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficServiceProviderServiceName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficCpName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspec"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosActiveTspec"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecTrafficClass"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecReqQosType"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecDataRate"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecPeakDataRate"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecMaxBurstSize"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecMaxPacketSize"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecE2EMaxDelayHigh"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTspecE2EMaxJitter"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyRowStatus"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyIpAddressType"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicySourceAddressUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicySourceAddressLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicySourcePortUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicySourcePortLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyDestinationAddressUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyDestinationAddressLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyDestinationPortUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyDestinationPortLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyIpProtocolUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyIpProtocolLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyTrafficClass"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyPeakDataRateUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyPeakDataRateLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyMeanDataRateUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyMeanDataRateLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyMaxBurstSizeUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyMaxBurstSizeLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyE2EMaxDelayHighLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyE2EMaxDelayLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyBoundaryAddressType"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyBoundarySourceAddressUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyBoundarySourceAddressLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyBoundaryDestinationAddressUpLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyBoundaryDestinationAddressLowLimit"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyUserName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyVendorApplicationName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyPortName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyServiceProviderServiceName"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyCriticalFlag"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyRequestedQosType"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyStartTime"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyEndTime"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyTrafficLeaseTimeUpValue"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyTrafficLeaseTimeLowValue"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyRuleType"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyRulePriority"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyTrafficImportanceNumber"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosPolicyUserImportanceNumber"))
)
if mibBuilder.loadTexts:
    ocHnQosTrafficDescInfo.setStatus("current")

ocHnQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 2, 5)
)
ocHnQosGroup.setObjects(
      *(("OC-HOME-NETWORK-MIB", "ocHnQosROStatsIdentifier"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsMacAddress"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsObservationMacAddress"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsQosSegmentId"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsTotalTrafficBytes"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsTotalParameterizedBytes"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsTotalParameterizedPackets"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsTotalParameterizedPacketsDropped"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsReportingDateAndTime"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsObservationPeriod"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosROStatsMonitorResolutionPeriod"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsLayer2StreamId"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsPktsTransmitted"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsPktsReceived"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsErrorPktsDropped"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsBytesTransmitted"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsBytesReceived"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsTrafficHandle"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosStreamStatisticsPeakDataRateViolations"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority0"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority1"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority2"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority3"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority4"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority5"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority6"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficTotalBytesPriority7"),
        ("OC-HOME-NETWORK-MIB", "ocHnStaticPQosStatus"),
        ("OC-HOME-NETWORK-MIB", "ocHnStaticPQosDeviceRowStatus"),
        ("OC-HOME-NETWORK-MIB", "ocHnStaticPQosDeviceActive"),
        ("OC-HOME-NETWORK-MIB", "ocHnStaticPQosDeviceMACAddress"))
)
if mibBuilder.loadTexts:
    ocHnQosGroup.setStatus("current")

ocHnNetConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 2, 6)
)
ocHnNetConfigGroup.setObjects(
      *(("OC-HOME-NETWORK-MIB", "ocHnNetConfigViewPrimaryOutputPort"),
        ("OC-HOME-NETWORK-MIB", "ocHnNetConfigViewPrimaryOutputPortOrgID"),
        ("OC-HOME-NETWORK-MIB", "ocHnNetConfigPersistentLinkLocalAddress"),
        ("OC-HOME-NETWORK-MIB", "ocHnIPAddressPrefixInterfaceNumber"),
        ("OC-HOME-NETWORK-MIB", "ocHnIPAddressPrefixType"),
        ("OC-HOME-NETWORK-MIB", "ocHnIPAddressPrefixLength"),
        ("OC-HOME-NETWORK-MIB", "ocHnIPAddressPrefixPrefix"),
        ("OC-HOME-NETWORK-MIB", "ocHnIPAddressPrefixPolicy"))
)
if mibBuilder.loadTexts:
    ocHnNetConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ocHnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 2, 3, 1, 1)
)
ocHnMIBCompliance.setObjects(
      *(("OC-HOME-NETWORK-MIB", "ocHnHomeNetworkStatusGroup"),
        ("OC-HOME-NETWORK-MIB", "ocHnGenericDevInterfaceGroup"),
        ("OC-HOME-NETWORK-MIB", "ocHnNetConfigGroup"),
        ("OC-HOME-NETWORK-MIB", "ocHnRotameterConfigGroup"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosTrafficDescInfo"),
        ("OC-HOME-NETWORK-MIB", "ocHnQosGroup"))
)
if mibBuilder.loadTexts:
    ocHnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OC-HOME-NETWORK-MIB",
    **{"Tenths": Tenths,
       "PowerUnit": PowerUnit,
       "ocHnMibModule": ocHnMibModule,
       "ocHnNotifications": ocHnNotifications,
       "ocHnMibObjects": ocHnMibObjects,
       "ocHnHomeNetStatus": ocHnHomeNetStatus,
       "ocHnRsdManagerStatus": ocHnRsdManagerStatus,
       "ocHnRsdManagerImportanceNumber": ocHnRsdManagerImportanceNumber,
       "ocHnRsdManagerPreferredStatus": ocHnRsdManagerPreferredStatus,
       "ocHnDevUpnpServiceTable": ocHnDevUpnpServiceTable,
       "ocHnDevUpnpServiceEntry": ocHnDevUpnpServiceEntry,
       "ocHnDevUpnpServiceIndex": ocHnDevUpnpServiceIndex,
       "ocHnDevUpnpServiceType": ocHnDevUpnpServiceType,
       "ocHnDevUpnpServiceAvailable": ocHnDevUpnpServiceAvailable,
       "ocHnDevSupportedChannelTable": ocHnDevSupportedChannelTable,
       "ocHnDevSupportedChannelEntry": ocHnDevSupportedChannelEntry,
       "ocHnDevSupportedChannelIndex": ocHnDevSupportedChannelIndex,
       "ocHnDevSupportedChannelLastOperatingFreq": ocHnDevSupportedChannelLastOperatingFreq,
       "ocHnDevSupportedChannelInUse": ocHnDevSupportedChannelInUse,
       "ocHnDevSupportedChannelFrequency": ocHnDevSupportedChannelFrequency,
       "ocHnDevSupportedChannelEligible": ocHnDevSupportedChannelEligible,
       "ocHnDevProperties": ocHnDevProperties,
       "ocHnDevPropertiesFriendlyName": ocHnDevPropertiesFriendlyName,
       "ocHnROConfiguration": ocHnROConfiguration,
       "ocHnRotameterConfigTable": ocHnRotameterConfigTable,
       "ocHnRotameterConfigEntry": ocHnRotameterConfigEntry,
       "ocHnRotameterConfigIndex": ocHnRotameterConfigIndex,
       "ocHnRotameterConfigRowStatus": ocHnRotameterConfigRowStatus,
       "ocHnRotameterConfigObservationActive": ocHnRotameterConfigObservationActive,
       "ocHnRotameterConfigPeriod": ocHnRotameterConfigPeriod,
       "ocHnRotameterConfigMonitorResolutionPeriod": ocHnRotameterConfigMonitorResolutionPeriod,
       "ocHnRotameterConfigQosSegmentId": ocHnRotameterConfigQosSegmentId,
       "ocHnRotameterConfigEndpointMacAddress": ocHnRotameterConfigEndpointMacAddress,
       "ocHnPerStreamRotameterConfigTable": ocHnPerStreamRotameterConfigTable,
       "ocHnPerStreamRotameterConfigEntry": ocHnPerStreamRotameterConfigEntry,
       "ocHnPerStreamRotameterConfigIndex": ocHnPerStreamRotameterConfigIndex,
       "ocHnPerStreamRotameterConfigRowStatus": ocHnPerStreamRotameterConfigRowStatus,
       "ocHnPerStreamRotameterConfigLayer2StreamId": ocHnPerStreamRotameterConfigLayer2StreamId,
       "ocHnPerStreamRotameterConfigTrafficHandle": ocHnPerStreamRotameterConfigTrafficHandle,
       "ocHnPerStreamRotameterConfigObservationActive": ocHnPerStreamRotameterConfigObservationActive,
       "ocHnQos": ocHnQos,
       "ocHnQosTrafficInfo": ocHnQosTrafficInfo,
       "ocHnQosStreamsInfoCollectionTrigger": ocHnQosStreamsInfoCollectionTrigger,
       "ocHnQosTrafficDescTable": ocHnQosTrafficDescTable,
       "ocHnQosTrafficDescEntry": ocHnQosTrafficDescEntry,
       "ocHnQosTrafficDescIndex": ocHnQosTrafficDescIndex,
       "ocHnQosTrafficHandle": ocHnQosTrafficHandle,
       "ocHnQosTrafficQDMacAddress": ocHnQosTrafficQDMacAddress,
       "ocHnQosTrafficNetworkAddressType": ocHnQosTrafficNetworkAddressType,
       "ocHnQosTrafficSourceAddress": ocHnQosTrafficSourceAddress,
       "ocHnQosTrafficSourcePort": ocHnQosTrafficSourcePort,
       "ocHnQosTrafficDestinationAddress": ocHnQosTrafficDestinationAddress,
       "ocHnQosTrafficDestinationPort": ocHnQosTrafficDestinationPort,
       "ocHnQosTrafficIpProtocol": ocHnQosTrafficIpProtocol,
       "ocHnQosTrafficV3TrafficIdSourceUuid": ocHnQosTrafficV3TrafficIdSourceUuid,
       "ocHnQosTrafficV3TrafficIdDestinationUuid": ocHnQosTrafficV3TrafficIdDestinationUuid,
       "ocHnQosTrafficMediaServerConnectionId": ocHnQosTrafficMediaServerConnectionId,
       "ocHnQosTrafficMediaRendererConnectionId": ocHnQosTrafficMediaRendererConnectionId,
       "ocHnQosTrafficLeaseTime": ocHnQosTrafficLeaseTime,
       "ocHnQosTrafficCritical": ocHnQosTrafficCritical,
       "ocHnQosTrafficUserName": ocHnQosTrafficUserName,
       "ocHnQosTrafficVendorApplicationName": ocHnQosTrafficVendorApplicationName,
       "ocHnQosTrafficPortName": ocHnQosTrafficPortName,
       "ocHnQosTrafficServiceProviderServiceName": ocHnQosTrafficServiceProviderServiceName,
       "ocHnQosTrafficCpName": ocHnQosTrafficCpName,
       "ocHnQosTspecTable": ocHnQosTspecTable,
       "ocHnQosTspecEntry": ocHnQosTspecEntry,
       "ocHnQosTspecTableIndex": ocHnQosTspecTableIndex,
       "ocHnQosTspec": ocHnQosTspec,
       "ocHnQosActiveTspec": ocHnQosActiveTspec,
       "ocHnQosTspecTrafficClass": ocHnQosTspecTrafficClass,
       "ocHnQosTspecReqQosType": ocHnQosTspecReqQosType,
       "ocHnQosTspecDataRate": ocHnQosTspecDataRate,
       "ocHnQosTspecPeakDataRate": ocHnQosTspecPeakDataRate,
       "ocHnQosTspecMaxBurstSize": ocHnQosTspecMaxBurstSize,
       "ocHnQosTspecMaxPacketSize": ocHnQosTspecMaxPacketSize,
       "ocHnQosTspecE2EMaxDelayHigh": ocHnQosTspecE2EMaxDelayHigh,
       "ocHnQosTspecE2EMaxJitter": ocHnQosTspecE2EMaxJitter,
       "ocHnQosPolicyTable": ocHnQosPolicyTable,
       "ocHnQosPolicyEntry": ocHnQosPolicyEntry,
       "ocHnQosPolicyRuleIdentifier": ocHnQosPolicyRuleIdentifier,
       "ocHnQosPolicyRowStatus": ocHnQosPolicyRowStatus,
       "ocHnQosPolicyIpAddressType": ocHnQosPolicyIpAddressType,
       "ocHnQosPolicySourceAddressUpLimit": ocHnQosPolicySourceAddressUpLimit,
       "ocHnQosPolicySourceAddressLowLimit": ocHnQosPolicySourceAddressLowLimit,
       "ocHnQosPolicySourcePortUpLimit": ocHnQosPolicySourcePortUpLimit,
       "ocHnQosPolicySourcePortLowLimit": ocHnQosPolicySourcePortLowLimit,
       "ocHnQosPolicyDestinationAddressUpLimit": ocHnQosPolicyDestinationAddressUpLimit,
       "ocHnQosPolicyDestinationAddressLowLimit": ocHnQosPolicyDestinationAddressLowLimit,
       "ocHnQosPolicyDestinationPortUpLimit": ocHnQosPolicyDestinationPortUpLimit,
       "ocHnQosPolicyDestinationPortLowLimit": ocHnQosPolicyDestinationPortLowLimit,
       "ocHnQosPolicyIpProtocolUpLimit": ocHnQosPolicyIpProtocolUpLimit,
       "ocHnQosPolicyIpProtocolLowLimit": ocHnQosPolicyIpProtocolLowLimit,
       "ocHnQosPolicyTrafficClass": ocHnQosPolicyTrafficClass,
       "ocHnQosPolicyPeakDataRateUpLimit": ocHnQosPolicyPeakDataRateUpLimit,
       "ocHnQosPolicyPeakDataRateLowLimit": ocHnQosPolicyPeakDataRateLowLimit,
       "ocHnQosPolicyMeanDataRateUpLimit": ocHnQosPolicyMeanDataRateUpLimit,
       "ocHnQosPolicyMeanDataRateLowLimit": ocHnQosPolicyMeanDataRateLowLimit,
       "ocHnQosPolicyMaxBurstSizeUpLimit": ocHnQosPolicyMaxBurstSizeUpLimit,
       "ocHnQosPolicyMaxBurstSizeLowLimit": ocHnQosPolicyMaxBurstSizeLowLimit,
       "ocHnQosPolicyE2EMaxDelayHighLimit": ocHnQosPolicyE2EMaxDelayHighLimit,
       "ocHnQosPolicyE2EMaxDelayLowLimit": ocHnQosPolicyE2EMaxDelayLowLimit,
       "ocHnQosPolicyBoundaryAddressType": ocHnQosPolicyBoundaryAddressType,
       "ocHnQosPolicyBoundarySourceAddressUpLimit": ocHnQosPolicyBoundarySourceAddressUpLimit,
       "ocHnQosPolicyBoundarySourceAddressLowLimit": ocHnQosPolicyBoundarySourceAddressLowLimit,
       "ocHnQosPolicyBoundaryDestinationAddressUpLimit": ocHnQosPolicyBoundaryDestinationAddressUpLimit,
       "ocHnQosPolicyBoundaryDestinationAddressLowLimit": ocHnQosPolicyBoundaryDestinationAddressLowLimit,
       "ocHnQosPolicyUserName": ocHnQosPolicyUserName,
       "ocHnQosPolicyVendorApplicationName": ocHnQosPolicyVendorApplicationName,
       "ocHnQosPolicyPortName": ocHnQosPolicyPortName,
       "ocHnQosPolicyServiceProviderServiceName": ocHnQosPolicyServiceProviderServiceName,
       "ocHnQosPolicyCriticalFlag": ocHnQosPolicyCriticalFlag,
       "ocHnQosPolicyRequestedQosType": ocHnQosPolicyRequestedQosType,
       "ocHnQosPolicyStartTime": ocHnQosPolicyStartTime,
       "ocHnQosPolicyEndTime": ocHnQosPolicyEndTime,
       "ocHnQosPolicyTrafficLeaseTimeUpValue": ocHnQosPolicyTrafficLeaseTimeUpValue,
       "ocHnQosPolicyTrafficLeaseTimeLowValue": ocHnQosPolicyTrafficLeaseTimeLowValue,
       "ocHnQosPolicyRuleType": ocHnQosPolicyRuleType,
       "ocHnQosPolicyRulePriority": ocHnQosPolicyRulePriority,
       "ocHnQosPolicyTrafficImportanceNumber": ocHnQosPolicyTrafficImportanceNumber,
       "ocHnQosPolicyUserImportanceNumber": ocHnQosPolicyUserImportanceNumber,
       "ocHnQosROStatsTable": ocHnQosROStatsTable,
       "ocHnQosROStatsEntry": ocHnQosROStatsEntry,
       "ocHnQosROStatsIndex": ocHnQosROStatsIndex,
       "ocHnQosROStatsIdentifier": ocHnQosROStatsIdentifier,
       "ocHnQosROStatsMacAddress": ocHnQosROStatsMacAddress,
       "ocHnQosROStatsObservationMacAddress": ocHnQosROStatsObservationMacAddress,
       "ocHnQosROStatsQosSegmentId": ocHnQosROStatsQosSegmentId,
       "ocHnQosROStatsTotalTrafficBytes": ocHnQosROStatsTotalTrafficBytes,
       "ocHnQosROStatsTotalParameterizedBytes": ocHnQosROStatsTotalParameterizedBytes,
       "ocHnQosROStatsTotalParameterizedPackets": ocHnQosROStatsTotalParameterizedPackets,
       "ocHnQosROStatsTotalParameterizedPacketsDropped": ocHnQosROStatsTotalParameterizedPacketsDropped,
       "ocHnQosROStatsReportingDateAndTime": ocHnQosROStatsReportingDateAndTime,
       "ocHnQosROStatsObservationPeriod": ocHnQosROStatsObservationPeriod,
       "ocHnQosROStatsMonitorResolutionPeriod": ocHnQosROStatsMonitorResolutionPeriod,
       "ocHnQosStreamStatisticsTable": ocHnQosStreamStatisticsTable,
       "ocHnQosStreamStatisticsEntry": ocHnQosStreamStatisticsEntry,
       "ocHnQosStreamStatisticsTrafficHandle": ocHnQosStreamStatisticsTrafficHandle,
       "ocHnQosStreamStatisticsLayer2StreamId": ocHnQosStreamStatisticsLayer2StreamId,
       "ocHnQosStreamStatisticsPktsTransmitted": ocHnQosStreamStatisticsPktsTransmitted,
       "ocHnQosStreamStatisticsPktsReceived": ocHnQosStreamStatisticsPktsReceived,
       "ocHnQosStreamStatisticsErrorPktsDropped": ocHnQosStreamStatisticsErrorPktsDropped,
       "ocHnQosStreamStatisticsBytesTransmitted": ocHnQosStreamStatisticsBytesTransmitted,
       "ocHnQosStreamStatisticsBytesReceived": ocHnQosStreamStatisticsBytesReceived,
       "ocHnQosStreamStatisticsPeakDataRateViolations": ocHnQosStreamStatisticsPeakDataRateViolations,
       "ocHnQosPriorityTrafficTable": ocHnQosPriorityTrafficTable,
       "ocHnQosPriorityTrafficEntry": ocHnQosPriorityTrafficEntry,
       "ocHnQosTrafficTotalBytesPriority0": ocHnQosTrafficTotalBytesPriority0,
       "ocHnQosTrafficTotalBytesPriority1": ocHnQosTrafficTotalBytesPriority1,
       "ocHnQosTrafficTotalBytesPriority2": ocHnQosTrafficTotalBytesPriority2,
       "ocHnQosTrafficTotalBytesPriority3": ocHnQosTrafficTotalBytesPriority3,
       "ocHnQosTrafficTotalBytesPriority4": ocHnQosTrafficTotalBytesPriority4,
       "ocHnQosTrafficTotalBytesPriority5": ocHnQosTrafficTotalBytesPriority5,
       "ocHnQosTrafficTotalBytesPriority6": ocHnQosTrafficTotalBytesPriority6,
       "ocHnQosTrafficTotalBytesPriority7": ocHnQosTrafficTotalBytesPriority7,
       "ocHnStaticPQosConfiguration": ocHnStaticPQosConfiguration,
       "ocHnStaticPQosStatus": ocHnStaticPQosStatus,
       "ocHnStaticPQosDeviceTable": ocHnStaticPQosDeviceTable,
       "ocHnStaticPQosDeviceEntry": ocHnStaticPQosDeviceEntry,
       "ocHnStaticPQosDeviceIndex": ocHnStaticPQosDeviceIndex,
       "ocHnStaticPQosDeviceRowStatus": ocHnStaticPQosDeviceRowStatus,
       "ocHnStaticPQosDeviceActive": ocHnStaticPQosDeviceActive,
       "ocHnStaticPQosDeviceMACAddress": ocHnStaticPQosDeviceMACAddress,
       "ocHnDevInterfaceStatus": ocHnDevInterfaceStatus,
       "ocHnDevInterfaceConfigTable": ocHnDevInterfaceConfigTable,
       "ocHnDevInterfaceConfigEntry": ocHnDevInterfaceConfigEntry,
       "ocHnDevInterfaceConfigMaxPowerLevel": ocHnDevInterfaceConfigMaxPowerLevel,
       "ocHnDevInterfaceConfigPowerUnits": ocHnDevInterfaceConfigPowerUnits,
       "ocHnDevInterfaceConfigMaxParameterizedBandwidth": ocHnDevInterfaceConfigMaxParameterizedBandwidth,
       "ocHnDevInterfaceConfigEnableEncryption": ocHnDevInterfaceConfigEnableEncryption,
       "ocHnDevInterfaceConfigEncryptionPassphrase": ocHnDevInterfaceConfigEncryptionPassphrase,
       "ocHnDevInterfaceStatusTable": ocHnDevInterfaceStatusTable,
       "ocHnDevInterfaceStatusEntry": ocHnDevInterfaceStatusEntry,
       "ocHnDevInterfaceStatusTxBroadcastRate": ocHnDevInterfaceStatusTxBroadcastRate,
       "ocHnDevInterfaceStatusTxBroadcastLevel": ocHnDevInterfaceStatusTxBroadcastLevel,
       "ocHnDevInterfaceStatusMaxTxPowerLevel": ocHnDevInterfaceStatusMaxTxPowerLevel,
       "ocHnDevInterfaceStatusPowerUnits": ocHnDevInterfaceStatusPowerUnits,
       "ocHnDevInterfaceStatusMaxParameterizedBandwidth": ocHnDevInterfaceStatusMaxParameterizedBandwidth,
       "ocHnDevInterfaceStatusLayer2Scheduler": ocHnDevInterfaceStatusLayer2Scheduler,
       "ocHnDevConnectionTable": ocHnDevConnectionTable,
       "ocHnDevConnectionEntry": ocHnDevConnectionEntry,
       "ocHnDevConnectionIndex": ocHnDevConnectionIndex,
       "ocHnDevConnectionDestMac": ocHnDevConnectionDestMac,
       "ocHnDevConnectionRxLinkRate": ocHnDevConnectionRxLinkRate,
       "ocHnDevConnectionRxModulationType": ocHnDevConnectionRxModulationType,
       "ocHnDevConnectionRxBroadcastRate": ocHnDevConnectionRxBroadcastRate,
       "ocHnDevConnectionRxSignalStrength": ocHnDevConnectionRxSignalStrength,
       "ocHnDevConnectionTxUnicastLevel": ocHnDevConnectionTxUnicastLevel,
       "ocHnDevConnectionPowerUnits": ocHnDevConnectionPowerUnits,
       "ocHnDevConnectionTxLinkRate": ocHnDevConnectionTxLinkRate,
       "ocHnDevConnectionTxModulationType": ocHnDevConnectionTxModulationType,
       "ocHnNetConfig": ocHnNetConfig,
       "ocHnNetConfigViewPrimaryOutputPort": ocHnNetConfigViewPrimaryOutputPort,
       "ocHnNetConfigViewPrimaryOutputPortOrgID": ocHnNetConfigViewPrimaryOutputPortOrgID,
       "ocHnIPAddressPrefixTable": ocHnIPAddressPrefixTable,
       "ocHnIPAddressPrefixEntry": ocHnIPAddressPrefixEntry,
       "ocHnIPAddressPrefixIndex": ocHnIPAddressPrefixIndex,
       "ocHnIPAddressPrefixInterfaceNumber": ocHnIPAddressPrefixInterfaceNumber,
       "ocHnIPAddressPrefixType": ocHnIPAddressPrefixType,
       "ocHnIPAddressPrefixLength": ocHnIPAddressPrefixLength,
       "ocHnIPAddressPrefixPrefix": ocHnIPAddressPrefixPrefix,
       "ocHnIPAddressPrefixPolicy": ocHnIPAddressPrefixPolicy,
       "ocHnNetConfigPersistentLinkLocalAddress": ocHnNetConfigPersistentLinkLocalAddress,
       "ocHnConformance": ocHnConformance,
       "ocHnMIBCompliances": ocHnMIBCompliances,
       "ocHnMIBCompliance": ocHnMIBCompliance,
       "ocHnMIBGroups": ocHnMIBGroups,
       "ocHnHomeNetworkStatusGroup": ocHnHomeNetworkStatusGroup,
       "ocHnGenericDevInterfaceGroup": ocHnGenericDevInterfaceGroup,
       "ocHnRotameterConfigGroup": ocHnRotameterConfigGroup,
       "ocHnQosTrafficDescInfo": ocHnQosTrafficDescInfo,
       "ocHnQosGroup": ocHnQosGroup,
       "ocHnNetConfigGroup": ocHnNetConfigGroup}
)
