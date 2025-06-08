# SNMP MIB module (VMWARE-NSX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vmware_6876/VMWARE-NSX-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:23:13 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwNSXsys,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNSXsys")


# MODULE-IDENTITY

vmwNSXsysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1)
)
if mibBuilder.loadTexts:
    vmwNSXsysMIB.setRevisions(
        ("2021-04-22 00:00",
         "2021-03-25 00:00",
         "2021-01-30 00:00",
         "2020-10-30 00:00",
         "2020-09-22 00:00",
         "2020-06-29 00:00",
         "2020-03-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwNsxTDataCenterFeatureIdType(TextualConvention, Integer32):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              24,
              28,
              30,
              31,
              32,
              33,
              35,
              36,
              38)
        )
    )
    namedValues = NamedValues(
        *(("managerHealth", 1),
          ("edgeHealth", 2),
          ("certificates", 3),
          ("passwordManagement", 4),
          ("licenses", 5),
          ("intelligenceHealth", 6),
          ("infrastructureCommunication", 7),
          ("intelligenceCommunication", 9),
          ("cniHealth", 10),
          ("ncpHealth", 11),
          ("nodeAgentsHealth", 12),
          ("endpointProtection", 13),
          ("vpn", 15),
          ("alarmManagement", 16),
          ("loadBalancer", 17),
          ("transportNodeHealth", 18),
          ("infrastructureService", 19),
          ("dhcp", 20),
          ("highAvailability", 21),
          ("capacity", 22),
          ("auditLogHealth", 24),
          ("routing", 28),
          ("dns", 30),
          ("distributedFirewall", 31),
          ("federation", 32),
          ("distributedIdsIps", 33),
          ("communication", 35),
          ("identityFirewall", 36),
          ("ipam", 38))
    )



class VmwNsxTDataCenterEventTypeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSeverityType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )



class VmwNsxTDataCenterNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNodeTypeType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("manager", 0),
          ("edge", 1),
          ("esx", 2),
          ("kvm", 3),
          ("publiccloudgateway", 4),
          ("intelligence", 5),
          ("autonomousedge", 6),
          ("globalmanager", 7))
    )



class VmwNsxTDataCenterEntityIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSystemResourceUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDiskPartitionNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLicenseEditionTypeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterApplianceAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCurrentGatewayStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCurrentServiceStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDatapathResourceUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDHCPPoolUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeServiceNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFailureReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPreviousGatewayStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPreviousServiceStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSystemUsageThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterUsernameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDHCPServerIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterServiceNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterIntelligenceNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterHostnameOrIPAddressWithPortType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEventIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterActiveGlobalManagerType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterActiveGlobalManagersType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSessionDownReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterManagerNodeNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTransportNodeAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTransportNodeNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCentralControlPlaneIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTunnelDownReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterHeapTypeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMempoolNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPasswordExpirationDaysType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterBGPNeighborIPType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLDAPServerType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPeerAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMaxIDSEventsAllowedType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterStaticAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDuplicateIPAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCapacityDisplayNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCapacityUsageCountType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeNICNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRxRingBufferOverflowPercentageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTxRingBufferOverflowPercentageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSrIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterIDSEventsCountType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteSiteNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterBGPSourceIPType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteSiteIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSiteIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSiteNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLrIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRxMissesType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRxProcessedType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTxMissesType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTxProcessedType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLrportIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterServiceIPType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteManagerNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDirectoryDomainType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTimeoutInMinutesType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMaxCapacityThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMinCapacityThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMaxSupportedCapacityCountType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLatencySourceType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLatencyThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLatencyValueType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterApplianceFQDNType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteApplianceAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterManagerNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDisplayedLicenseKeyType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeThreadNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterIntentPathType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_VmwNsxTDataCenterNotifications_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterNotifications = _VmwNsxTDataCenterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotifications.setStatus("current")
_VmwNsxTManagerHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTManagerHealthFeaturePrefix = _VmwNsxTManagerHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1)
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthFeaturePrefix.setStatus("current")
_VmwNsxTManagerHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTManagerHealthFeature = _VmwNsxTManagerHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthFeature.setStatus("current")
_VmwNsxTEdgeHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTEdgeHealthFeaturePrefix = _VmwNsxTEdgeHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2)
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthFeaturePrefix.setStatus("current")
_VmwNsxTEdgeHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTEdgeHealthFeature = _VmwNsxTEdgeHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthFeature.setStatus("current")
_VmwNsxTCertificatesFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCertificatesFeaturePrefix = _VmwNsxTCertificatesFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3)
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesFeaturePrefix.setStatus("current")
_VmwNsxTCertificatesFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCertificatesFeature = _VmwNsxTCertificatesFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesFeature.setStatus("current")
_VmwNsxTPasswordManagementFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTPasswordManagementFeaturePrefix = _VmwNsxTPasswordManagementFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4)
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementFeaturePrefix.setStatus("current")
_VmwNsxTPasswordManagementFeature_ObjectIdentity = ObjectIdentity
vmwNsxTPasswordManagementFeature = _VmwNsxTPasswordManagementFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementFeature.setStatus("current")
_VmwNsxTLicensesFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTLicensesFeaturePrefix = _VmwNsxTLicensesFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5)
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesFeaturePrefix.setStatus("current")
_VmwNsxTLicensesFeature_ObjectIdentity = ObjectIdentity
vmwNsxTLicensesFeature = _VmwNsxTLicensesFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesFeature.setStatus("current")
_VmwNsxTIntelligenceHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceHealthFeaturePrefix = _VmwNsxTIntelligenceHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthFeaturePrefix.setStatus("current")
_VmwNsxTIntelligenceHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceHealthFeature = _VmwNsxTIntelligenceHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthFeature.setStatus("current")
_VmwNsxTInfrastructureCommunicationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureCommunicationFeaturePrefix = _VmwNsxTInfrastructureCommunicationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationFeaturePrefix.setStatus("current")
_VmwNsxTInfrastructureCommunicationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureCommunicationFeature = _VmwNsxTInfrastructureCommunicationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationFeature.setStatus("current")
_VmwNsxTIntelligenceCommunicationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceCommunicationFeaturePrefix = _VmwNsxTIntelligenceCommunicationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationFeaturePrefix.setStatus("current")
_VmwNsxTIntelligenceCommunicationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceCommunicationFeature = _VmwNsxTIntelligenceCommunicationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationFeature.setStatus("current")
_VmwNsxTCniHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCniHealthFeaturePrefix = _VmwNsxTCniHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10)
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthFeaturePrefix.setStatus("current")
_VmwNsxTCniHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCniHealthFeature = _VmwNsxTCniHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthFeature.setStatus("current")
_VmwNsxTNCPHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTNCPHealthFeaturePrefix = _VmwNsxTNCPHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11)
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthFeaturePrefix.setStatus("current")
_VmwNsxTNCPHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTNCPHealthFeature = _VmwNsxTNCPHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthFeature.setStatus("current")
_VmwNsxTNodeAgentsHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTNodeAgentsHealthFeaturePrefix = _VmwNsxTNodeAgentsHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12)
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthFeaturePrefix.setStatus("current")
_VmwNsxTNodeAgentsHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTNodeAgentsHealthFeature = _VmwNsxTNodeAgentsHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthFeature.setStatus("current")
_VmwNsxTEndpointProtectionFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTEndpointProtectionFeaturePrefix = _VmwNsxTEndpointProtectionFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13)
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionFeaturePrefix.setStatus("current")
_VmwNsxTEndpointProtectionFeature_ObjectIdentity = ObjectIdentity
vmwNsxTEndpointProtectionFeature = _VmwNsxTEndpointProtectionFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionFeature.setStatus("current")
_VmwNsxTVPNFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTVPNFeaturePrefix = _VmwNsxTVPNFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15)
)
if mibBuilder.loadTexts:
    vmwNsxTVPNFeaturePrefix.setStatus("current")
_VmwNsxTVPNFeature_ObjectIdentity = ObjectIdentity
vmwNsxTVPNFeature = _VmwNsxTVPNFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTVPNFeature.setStatus("current")
_VmwNsxTAlarmManagementFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTAlarmManagementFeaturePrefix = _VmwNsxTAlarmManagementFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16)
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementFeaturePrefix.setStatus("current")
_VmwNsxTAlarmManagementFeature_ObjectIdentity = ObjectIdentity
vmwNsxTAlarmManagementFeature = _VmwNsxTAlarmManagementFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementFeature.setStatus("current")
_VmwNsxTLoadBalancerFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTLoadBalancerFeaturePrefix = _VmwNsxTLoadBalancerFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17)
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerFeaturePrefix.setStatus("current")
_VmwNsxTLoadBalancerFeature_ObjectIdentity = ObjectIdentity
vmwNsxTLoadBalancerFeature = _VmwNsxTLoadBalancerFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerFeature.setStatus("current")
_VmwNsxTTransportNodeHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTTransportNodeHealthFeaturePrefix = _VmwNsxTTransportNodeHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18)
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthFeaturePrefix.setStatus("current")
_VmwNsxTTransportNodeHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTTransportNodeHealthFeature = _VmwNsxTTransportNodeHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthFeature.setStatus("current")
_VmwNsxTInfrastructureServiceFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureServiceFeaturePrefix = _VmwNsxTInfrastructureServiceFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceFeaturePrefix.setStatus("current")
_VmwNsxTInfrastructureServiceFeature_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureServiceFeature = _VmwNsxTInfrastructureServiceFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceFeature.setStatus("current")
_VmwNsxTDHCPFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDHCPFeaturePrefix = _VmwNsxTDHCPFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20)
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPFeaturePrefix.setStatus("current")
_VmwNsxTDHCPFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDHCPFeature = _VmwNsxTDHCPFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPFeature.setStatus("current")
_VmwNsxTHighAvailabilityFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTHighAvailabilityFeaturePrefix = _VmwNsxTHighAvailabilityFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21)
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityFeaturePrefix.setStatus("current")
_VmwNsxTHighAvailabilityFeature_ObjectIdentity = ObjectIdentity
vmwNsxTHighAvailabilityFeature = _VmwNsxTHighAvailabilityFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityFeature.setStatus("current")
_VmwNsxTCapacityFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCapacityFeaturePrefix = _VmwNsxTCapacityFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22)
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityFeaturePrefix.setStatus("current")
_VmwNsxTCapacityFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCapacityFeature = _VmwNsxTCapacityFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityFeature.setStatus("current")
_VmwNsxTAuditLogHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTAuditLogHealthFeaturePrefix = _VmwNsxTAuditLogHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24)
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthFeaturePrefix.setStatus("current")
_VmwNsxTAuditLogHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTAuditLogHealthFeature = _VmwNsxTAuditLogHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthFeature.setStatus("current")
_VmwNsxTRoutingFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTRoutingFeaturePrefix = _VmwNsxTRoutingFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28)
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingFeaturePrefix.setStatus("current")
_VmwNsxTRoutingFeature_ObjectIdentity = ObjectIdentity
vmwNsxTRoutingFeature = _VmwNsxTRoutingFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingFeature.setStatus("current")
_VmwNsxTDNSFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDNSFeaturePrefix = _VmwNsxTDNSFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30)
)
if mibBuilder.loadTexts:
    vmwNsxTDNSFeaturePrefix.setStatus("current")
_VmwNsxTDNSFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDNSFeature = _VmwNsxTDNSFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDNSFeature.setStatus("current")
_VmwNsxTDistributedFirewallFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedFirewallFeaturePrefix = _VmwNsxTDistributedFirewallFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallFeaturePrefix.setStatus("current")
_VmwNsxTDistributedFirewallFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedFirewallFeature = _VmwNsxTDistributedFirewallFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallFeature.setStatus("current")
_VmwNsxTFederationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTFederationFeaturePrefix = _VmwNsxTFederationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32)
)
if mibBuilder.loadTexts:
    vmwNsxTFederationFeaturePrefix.setStatus("current")
_VmwNsxTFederationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTFederationFeature = _VmwNsxTFederationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTFederationFeature.setStatus("current")
_VmwNsxTDistributedIDSIPSFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedIDSIPSFeaturePrefix = _VmwNsxTDistributedIDSIPSFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSFeaturePrefix.setStatus("current")
_VmwNsxTDistributedIDSIPSFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedIDSIPSFeature = _VmwNsxTDistributedIDSIPSFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSFeature.setStatus("current")
_VmwNsxTCommunicationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCommunicationFeaturePrefix = _VmwNsxTCommunicationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35)
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationFeaturePrefix.setStatus("current")
_VmwNsxTCommunicationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCommunicationFeature = _VmwNsxTCommunicationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationFeature.setStatus("current")
_VmwNsxTIdentityFirewallFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIdentityFirewallFeaturePrefix = _VmwNsxTIdentityFirewallFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36)
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallFeaturePrefix.setStatus("current")
_VmwNsxTIdentityFirewallFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIdentityFirewallFeature = _VmwNsxTIdentityFirewallFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallFeature.setStatus("current")
_VmwNsxTIPAMFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIPAMFeaturePrefix = _VmwNsxTIPAMFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38)
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMFeaturePrefix.setStatus("current")
_VmwNsxTIPAMFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIPAMFeature = _VmwNsxTIPAMFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMFeature.setStatus("current")
_VmwNsxTDataCenterData_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterData = _VmwNsxTDataCenterData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1)
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterData.setStatus("current")
_VmwNsxTDataCenterTimestamp_Type = DateAndTime
_VmwNsxTDataCenterTimestamp_Object = MibScalar
vmwNsxTDataCenterTimestamp = _VmwNsxTDataCenterTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 1),
    _VmwNsxTDataCenterTimestamp_Type()
)
vmwNsxTDataCenterTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTimestamp.setStatus("current")
_VmwNsxTDataCenterFeatureName_Type = VmwNsxTDataCenterFeatureIdType
_VmwNsxTDataCenterFeatureName_Object = MibScalar
vmwNsxTDataCenterFeatureName = _VmwNsxTDataCenterFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 2),
    _VmwNsxTDataCenterFeatureName_Type()
)
vmwNsxTDataCenterFeatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFeatureName.setStatus("current")
_VmwNsxTDataCenterEventType_Type = VmwNsxTDataCenterEventTypeType
_VmwNsxTDataCenterEventType_Object = MibScalar
vmwNsxTDataCenterEventType = _VmwNsxTDataCenterEventType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 3),
    _VmwNsxTDataCenterEventType_Type()
)
vmwNsxTDataCenterEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEventType.setStatus("current")
_VmwNsxTDataCenterEventSeverity_Type = VmwNsxTDataCenterSeverityType
_VmwNsxTDataCenterEventSeverity_Object = MibScalar
vmwNsxTDataCenterEventSeverity = _VmwNsxTDataCenterEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 4),
    _VmwNsxTDataCenterEventSeverity_Type()
)
vmwNsxTDataCenterEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEventSeverity.setStatus("current")
_VmwNsxTDataCenterNodeId_Type = VmwNsxTDataCenterNodeIdType
_VmwNsxTDataCenterNodeId_Object = MibScalar
vmwNsxTDataCenterNodeId = _VmwNsxTDataCenterNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 5),
    _VmwNsxTDataCenterNodeId_Type()
)
vmwNsxTDataCenterNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNodeId.setStatus("current")
_VmwNsxTDataCenterNodeType_Type = VmwNsxTDataCenterNodeTypeType
_VmwNsxTDataCenterNodeType_Object = MibScalar
vmwNsxTDataCenterNodeType = _VmwNsxTDataCenterNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 6),
    _VmwNsxTDataCenterNodeType_Type()
)
vmwNsxTDataCenterNodeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNodeType.setStatus("current")
_VmwNsxTDataCenterEntityId_Type = VmwNsxTDataCenterEntityIdType
_VmwNsxTDataCenterEntityId_Object = MibScalar
vmwNsxTDataCenterEntityId = _VmwNsxTDataCenterEntityId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 21),
    _VmwNsxTDataCenterEntityId_Type()
)
vmwNsxTDataCenterEntityId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEntityId.setStatus("current")
_VmwNsxTDataCenterSystemResourceUsage_Type = VmwNsxTDataCenterSystemResourceUsageType
_VmwNsxTDataCenterSystemResourceUsage_Object = MibScalar
vmwNsxTDataCenterSystemResourceUsage = _VmwNsxTDataCenterSystemResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 22),
    _VmwNsxTDataCenterSystemResourceUsage_Type()
)
vmwNsxTDataCenterSystemResourceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSystemResourceUsage.setStatus("current")
_VmwNsxTDataCenterDiskPartitionName_Type = VmwNsxTDataCenterDiskPartitionNameType
_VmwNsxTDataCenterDiskPartitionName_Object = MibScalar
vmwNsxTDataCenterDiskPartitionName = _VmwNsxTDataCenterDiskPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 23),
    _VmwNsxTDataCenterDiskPartitionName_Type()
)
vmwNsxTDataCenterDiskPartitionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDiskPartitionName.setStatus("current")
_VmwNsxTDataCenterLicenseEditionType_Type = VmwNsxTDataCenterLicenseEditionTypeType
_VmwNsxTDataCenterLicenseEditionType_Object = MibScalar
vmwNsxTDataCenterLicenseEditionType = _VmwNsxTDataCenterLicenseEditionType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 24),
    _VmwNsxTDataCenterLicenseEditionType_Type()
)
vmwNsxTDataCenterLicenseEditionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLicenseEditionType.setStatus("current")
_VmwNsxTDataCenterApplianceAddress_Type = VmwNsxTDataCenterApplianceAddressType
_VmwNsxTDataCenterApplianceAddress_Object = MibScalar
vmwNsxTDataCenterApplianceAddress = _VmwNsxTDataCenterApplianceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 25),
    _VmwNsxTDataCenterApplianceAddress_Type()
)
vmwNsxTDataCenterApplianceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterApplianceAddress.setStatus("current")
_VmwNsxTDataCenterCurrentGatewayState_Type = VmwNsxTDataCenterCurrentGatewayStateType
_VmwNsxTDataCenterCurrentGatewayState_Object = MibScalar
vmwNsxTDataCenterCurrentGatewayState = _VmwNsxTDataCenterCurrentGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 26),
    _VmwNsxTDataCenterCurrentGatewayState_Type()
)
vmwNsxTDataCenterCurrentGatewayState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCurrentGatewayState.setStatus("current")
_VmwNsxTDataCenterCurrentServiceState_Type = VmwNsxTDataCenterCurrentServiceStateType
_VmwNsxTDataCenterCurrentServiceState_Object = MibScalar
vmwNsxTDataCenterCurrentServiceState = _VmwNsxTDataCenterCurrentServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 27),
    _VmwNsxTDataCenterCurrentServiceState_Type()
)
vmwNsxTDataCenterCurrentServiceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCurrentServiceState.setStatus("current")
_VmwNsxTDataCenterDatapathResourceUsage_Type = VmwNsxTDataCenterDatapathResourceUsageType
_VmwNsxTDataCenterDatapathResourceUsage_Object = MibScalar
vmwNsxTDataCenterDatapathResourceUsage = _VmwNsxTDataCenterDatapathResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 28),
    _VmwNsxTDataCenterDatapathResourceUsage_Type()
)
vmwNsxTDataCenterDatapathResourceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDatapathResourceUsage.setStatus("current")
_VmwNsxTDataCenterDHCPPoolUsage_Type = VmwNsxTDataCenterDHCPPoolUsageType
_VmwNsxTDataCenterDHCPPoolUsage_Object = MibScalar
vmwNsxTDataCenterDHCPPoolUsage = _VmwNsxTDataCenterDHCPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 29),
    _VmwNsxTDataCenterDHCPPoolUsage_Type()
)
vmwNsxTDataCenterDHCPPoolUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDHCPPoolUsage.setStatus("current")
_VmwNsxTDataCenterEdgeServiceName_Type = VmwNsxTDataCenterEdgeServiceNameType
_VmwNsxTDataCenterEdgeServiceName_Object = MibScalar
vmwNsxTDataCenterEdgeServiceName = _VmwNsxTDataCenterEdgeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 30),
    _VmwNsxTDataCenterEdgeServiceName_Type()
)
vmwNsxTDataCenterEdgeServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeServiceName.setStatus("current")
_VmwNsxTDataCenterFailureReason_Type = VmwNsxTDataCenterFailureReasonType
_VmwNsxTDataCenterFailureReason_Object = MibScalar
vmwNsxTDataCenterFailureReason = _VmwNsxTDataCenterFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 31),
    _VmwNsxTDataCenterFailureReason_Type()
)
vmwNsxTDataCenterFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFailureReason.setStatus("current")
_VmwNsxTDataCenterPreviousGatewayState_Type = VmwNsxTDataCenterPreviousGatewayStateType
_VmwNsxTDataCenterPreviousGatewayState_Object = MibScalar
vmwNsxTDataCenterPreviousGatewayState = _VmwNsxTDataCenterPreviousGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 32),
    _VmwNsxTDataCenterPreviousGatewayState_Type()
)
vmwNsxTDataCenterPreviousGatewayState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPreviousGatewayState.setStatus("current")
_VmwNsxTDataCenterPreviousServiceState_Type = VmwNsxTDataCenterPreviousServiceStateType
_VmwNsxTDataCenterPreviousServiceState_Object = MibScalar
vmwNsxTDataCenterPreviousServiceState = _VmwNsxTDataCenterPreviousServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 33),
    _VmwNsxTDataCenterPreviousServiceState_Type()
)
vmwNsxTDataCenterPreviousServiceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPreviousServiceState.setStatus("current")
_VmwNsxTDataCenterSystemUsageThreshold_Type = VmwNsxTDataCenterSystemUsageThresholdType
_VmwNsxTDataCenterSystemUsageThreshold_Object = MibScalar
vmwNsxTDataCenterSystemUsageThreshold = _VmwNsxTDataCenterSystemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 34),
    _VmwNsxTDataCenterSystemUsageThreshold_Type()
)
vmwNsxTDataCenterSystemUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSystemUsageThreshold.setStatus("current")
_VmwNsxTDataCenterUsername_Type = VmwNsxTDataCenterUsernameType
_VmwNsxTDataCenterUsername_Object = MibScalar
vmwNsxTDataCenterUsername = _VmwNsxTDataCenterUsername_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 35),
    _VmwNsxTDataCenterUsername_Type()
)
vmwNsxTDataCenterUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterUsername.setStatus("current")
_VmwNsxTDataCenterDHCPServerId_Type = VmwNsxTDataCenterDHCPServerIdType
_VmwNsxTDataCenterDHCPServerId_Object = MibScalar
vmwNsxTDataCenterDHCPServerId = _VmwNsxTDataCenterDHCPServerId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 36),
    _VmwNsxTDataCenterDHCPServerId_Type()
)
vmwNsxTDataCenterDHCPServerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDHCPServerId.setStatus("current")
_VmwNsxTDataCenterServiceName_Type = VmwNsxTDataCenterServiceNameType
_VmwNsxTDataCenterServiceName_Object = MibScalar
vmwNsxTDataCenterServiceName = _VmwNsxTDataCenterServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 37),
    _VmwNsxTDataCenterServiceName_Type()
)
vmwNsxTDataCenterServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterServiceName.setStatus("current")
_VmwNsxTDataCenterIntelligenceNodeId_Type = VmwNsxTDataCenterIntelligenceNodeIdType
_VmwNsxTDataCenterIntelligenceNodeId_Object = MibScalar
vmwNsxTDataCenterIntelligenceNodeId = _VmwNsxTDataCenterIntelligenceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 38),
    _VmwNsxTDataCenterIntelligenceNodeId_Type()
)
vmwNsxTDataCenterIntelligenceNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterIntelligenceNodeId.setStatus("current")
_VmwNsxTDataCenterHostnameOrIPAddressWithPort_Type = VmwNsxTDataCenterHostnameOrIPAddressWithPortType
_VmwNsxTDataCenterHostnameOrIPAddressWithPort_Object = MibScalar
vmwNsxTDataCenterHostnameOrIPAddressWithPort = _VmwNsxTDataCenterHostnameOrIPAddressWithPort_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 39),
    _VmwNsxTDataCenterHostnameOrIPAddressWithPort_Type()
)
vmwNsxTDataCenterHostnameOrIPAddressWithPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterHostnameOrIPAddressWithPort.setStatus("current")
_VmwNsxTDataCenterEventId_Type = VmwNsxTDataCenterEventIdType
_VmwNsxTDataCenterEventId_Object = MibScalar
vmwNsxTDataCenterEventId = _VmwNsxTDataCenterEventId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 40),
    _VmwNsxTDataCenterEventId_Type()
)
vmwNsxTDataCenterEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEventId.setStatus("current")
_VmwNsxTDataCenterActiveGlobalManager_Type = VmwNsxTDataCenterActiveGlobalManagerType
_VmwNsxTDataCenterActiveGlobalManager_Object = MibScalar
vmwNsxTDataCenterActiveGlobalManager = _VmwNsxTDataCenterActiveGlobalManager_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 41),
    _VmwNsxTDataCenterActiveGlobalManager_Type()
)
vmwNsxTDataCenterActiveGlobalManager.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterActiveGlobalManager.setStatus("current")
_VmwNsxTDataCenterActiveGlobalManagers_Type = VmwNsxTDataCenterActiveGlobalManagersType
_VmwNsxTDataCenterActiveGlobalManagers_Object = MibScalar
vmwNsxTDataCenterActiveGlobalManagers = _VmwNsxTDataCenterActiveGlobalManagers_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 42),
    _VmwNsxTDataCenterActiveGlobalManagers_Type()
)
vmwNsxTDataCenterActiveGlobalManagers.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterActiveGlobalManagers.setStatus("current")
_VmwNsxTDataCenterSessionDownReason_Type = VmwNsxTDataCenterSessionDownReasonType
_VmwNsxTDataCenterSessionDownReason_Object = MibScalar
vmwNsxTDataCenterSessionDownReason = _VmwNsxTDataCenterSessionDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 43),
    _VmwNsxTDataCenterSessionDownReason_Type()
)
vmwNsxTDataCenterSessionDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSessionDownReason.setStatus("current")
_VmwNsxTDataCenterManagerNodeName_Type = VmwNsxTDataCenterManagerNodeNameType
_VmwNsxTDataCenterManagerNodeName_Object = MibScalar
vmwNsxTDataCenterManagerNodeName = _VmwNsxTDataCenterManagerNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 44),
    _VmwNsxTDataCenterManagerNodeName_Type()
)
vmwNsxTDataCenterManagerNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterManagerNodeName.setStatus("current")
_VmwNsxTDataCenterTransportNodeAddress_Type = VmwNsxTDataCenterTransportNodeAddressType
_VmwNsxTDataCenterTransportNodeAddress_Object = MibScalar
vmwNsxTDataCenterTransportNodeAddress = _VmwNsxTDataCenterTransportNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 45),
    _VmwNsxTDataCenterTransportNodeAddress_Type()
)
vmwNsxTDataCenterTransportNodeAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTransportNodeAddress.setStatus("current")
_VmwNsxTDataCenterTransportNodeName_Type = VmwNsxTDataCenterTransportNodeNameType
_VmwNsxTDataCenterTransportNodeName_Object = MibScalar
vmwNsxTDataCenterTransportNodeName = _VmwNsxTDataCenterTransportNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 46),
    _VmwNsxTDataCenterTransportNodeName_Type()
)
vmwNsxTDataCenterTransportNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTransportNodeName.setStatus("current")
_VmwNsxTDataCenterCentralControlPlaneId_Type = VmwNsxTDataCenterCentralControlPlaneIdType
_VmwNsxTDataCenterCentralControlPlaneId_Object = MibScalar
vmwNsxTDataCenterCentralControlPlaneId = _VmwNsxTDataCenterCentralControlPlaneId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 47),
    _VmwNsxTDataCenterCentralControlPlaneId_Type()
)
vmwNsxTDataCenterCentralControlPlaneId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCentralControlPlaneId.setStatus("current")
_VmwNsxTDataCenterTunnelDownReason_Type = VmwNsxTDataCenterTunnelDownReasonType
_VmwNsxTDataCenterTunnelDownReason_Object = MibScalar
vmwNsxTDataCenterTunnelDownReason = _VmwNsxTDataCenterTunnelDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 48),
    _VmwNsxTDataCenterTunnelDownReason_Type()
)
vmwNsxTDataCenterTunnelDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTunnelDownReason.setStatus("current")
_VmwNsxTDataCenterHeapType_Type = VmwNsxTDataCenterHeapTypeType
_VmwNsxTDataCenterHeapType_Object = MibScalar
vmwNsxTDataCenterHeapType = _VmwNsxTDataCenterHeapType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 49),
    _VmwNsxTDataCenterHeapType_Type()
)
vmwNsxTDataCenterHeapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterHeapType.setStatus("current")
_VmwNsxTDataCenterMempoolName_Type = VmwNsxTDataCenterMempoolNameType
_VmwNsxTDataCenterMempoolName_Object = MibScalar
vmwNsxTDataCenterMempoolName = _VmwNsxTDataCenterMempoolName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 50),
    _VmwNsxTDataCenterMempoolName_Type()
)
vmwNsxTDataCenterMempoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMempoolName.setStatus("current")
_VmwNsxTDataCenterPasswordExpirationDays_Type = VmwNsxTDataCenterPasswordExpirationDaysType
_VmwNsxTDataCenterPasswordExpirationDays_Object = MibScalar
vmwNsxTDataCenterPasswordExpirationDays = _VmwNsxTDataCenterPasswordExpirationDays_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 51),
    _VmwNsxTDataCenterPasswordExpirationDays_Type()
)
vmwNsxTDataCenterPasswordExpirationDays.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPasswordExpirationDays.setStatus("current")
_VmwNsxTDataCenterBGPNeighborIP_Type = VmwNsxTDataCenterBGPNeighborIPType
_VmwNsxTDataCenterBGPNeighborIP_Object = MibScalar
vmwNsxTDataCenterBGPNeighborIP = _VmwNsxTDataCenterBGPNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 52),
    _VmwNsxTDataCenterBGPNeighborIP_Type()
)
vmwNsxTDataCenterBGPNeighborIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBGPNeighborIP.setStatus("current")
_VmwNsxTDataCenterLDAPServer_Type = VmwNsxTDataCenterLDAPServerType
_VmwNsxTDataCenterLDAPServer_Object = MibScalar
vmwNsxTDataCenterLDAPServer = _VmwNsxTDataCenterLDAPServer_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 53),
    _VmwNsxTDataCenterLDAPServer_Type()
)
vmwNsxTDataCenterLDAPServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLDAPServer.setStatus("current")
_VmwNsxTDataCenterPeerAddress_Type = VmwNsxTDataCenterPeerAddressType
_VmwNsxTDataCenterPeerAddress_Object = MibScalar
vmwNsxTDataCenterPeerAddress = _VmwNsxTDataCenterPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 54),
    _VmwNsxTDataCenterPeerAddress_Type()
)
vmwNsxTDataCenterPeerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPeerAddress.setStatus("current")
_VmwNsxTDataCenterMaxIDSEventsAllowed_Type = VmwNsxTDataCenterMaxIDSEventsAllowedType
_VmwNsxTDataCenterMaxIDSEventsAllowed_Object = MibScalar
vmwNsxTDataCenterMaxIDSEventsAllowed = _VmwNsxTDataCenterMaxIDSEventsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 55),
    _VmwNsxTDataCenterMaxIDSEventsAllowed_Type()
)
vmwNsxTDataCenterMaxIDSEventsAllowed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMaxIDSEventsAllowed.setStatus("current")
_VmwNsxTDataCenterStaticAddress_Type = VmwNsxTDataCenterStaticAddressType
_VmwNsxTDataCenterStaticAddress_Object = MibScalar
vmwNsxTDataCenterStaticAddress = _VmwNsxTDataCenterStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 56),
    _VmwNsxTDataCenterStaticAddress_Type()
)
vmwNsxTDataCenterStaticAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterStaticAddress.setStatus("current")
_VmwNsxTDataCenterDuplicateIPAddress_Type = VmwNsxTDataCenterDuplicateIPAddressType
_VmwNsxTDataCenterDuplicateIPAddress_Object = MibScalar
vmwNsxTDataCenterDuplicateIPAddress = _VmwNsxTDataCenterDuplicateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 57),
    _VmwNsxTDataCenterDuplicateIPAddress_Type()
)
vmwNsxTDataCenterDuplicateIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDuplicateIPAddress.setStatus("current")
_VmwNsxTDataCenterCapacityDisplayName_Type = VmwNsxTDataCenterCapacityDisplayNameType
_VmwNsxTDataCenterCapacityDisplayName_Object = MibScalar
vmwNsxTDataCenterCapacityDisplayName = _VmwNsxTDataCenterCapacityDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 58),
    _VmwNsxTDataCenterCapacityDisplayName_Type()
)
vmwNsxTDataCenterCapacityDisplayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCapacityDisplayName.setStatus("current")
_VmwNsxTDataCenterCapacityUsageCount_Type = VmwNsxTDataCenterCapacityUsageCountType
_VmwNsxTDataCenterCapacityUsageCount_Object = MibScalar
vmwNsxTDataCenterCapacityUsageCount = _VmwNsxTDataCenterCapacityUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 59),
    _VmwNsxTDataCenterCapacityUsageCount_Type()
)
vmwNsxTDataCenterCapacityUsageCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCapacityUsageCount.setStatus("current")
_VmwNsxTDataCenterEdgeNICName_Type = VmwNsxTDataCenterEdgeNICNameType
_VmwNsxTDataCenterEdgeNICName_Object = MibScalar
vmwNsxTDataCenterEdgeNICName = _VmwNsxTDataCenterEdgeNICName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 60),
    _VmwNsxTDataCenterEdgeNICName_Type()
)
vmwNsxTDataCenterEdgeNICName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeNICName.setStatus("current")
_VmwNsxTDataCenterRxRingBufferOverflowPercentage_Type = VmwNsxTDataCenterRxRingBufferOverflowPercentageType
_VmwNsxTDataCenterRxRingBufferOverflowPercentage_Object = MibScalar
vmwNsxTDataCenterRxRingBufferOverflowPercentage = _VmwNsxTDataCenterRxRingBufferOverflowPercentage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 61),
    _VmwNsxTDataCenterRxRingBufferOverflowPercentage_Type()
)
vmwNsxTDataCenterRxRingBufferOverflowPercentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRxRingBufferOverflowPercentage.setStatus("current")
_VmwNsxTDataCenterTxRingBufferOverflowPercentage_Type = VmwNsxTDataCenterTxRingBufferOverflowPercentageType
_VmwNsxTDataCenterTxRingBufferOverflowPercentage_Object = MibScalar
vmwNsxTDataCenterTxRingBufferOverflowPercentage = _VmwNsxTDataCenterTxRingBufferOverflowPercentage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 62),
    _VmwNsxTDataCenterTxRingBufferOverflowPercentage_Type()
)
vmwNsxTDataCenterTxRingBufferOverflowPercentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTxRingBufferOverflowPercentage.setStatus("current")
_VmwNsxTDataCenterSrId_Type = VmwNsxTDataCenterSrIdType
_VmwNsxTDataCenterSrId_Object = MibScalar
vmwNsxTDataCenterSrId = _VmwNsxTDataCenterSrId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 63),
    _VmwNsxTDataCenterSrId_Type()
)
vmwNsxTDataCenterSrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSrId.setStatus("current")
_VmwNsxTDataCenterIDSEventsCount_Type = VmwNsxTDataCenterIDSEventsCountType
_VmwNsxTDataCenterIDSEventsCount_Object = MibScalar
vmwNsxTDataCenterIDSEventsCount = _VmwNsxTDataCenterIDSEventsCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 64),
    _VmwNsxTDataCenterIDSEventsCount_Type()
)
vmwNsxTDataCenterIDSEventsCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterIDSEventsCount.setStatus("current")
_VmwNsxTDataCenterRemoteSiteName_Type = VmwNsxTDataCenterRemoteSiteNameType
_VmwNsxTDataCenterRemoteSiteName_Object = MibScalar
vmwNsxTDataCenterRemoteSiteName = _VmwNsxTDataCenterRemoteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 65),
    _VmwNsxTDataCenterRemoteSiteName_Type()
)
vmwNsxTDataCenterRemoteSiteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteSiteName.setStatus("current")
_VmwNsxTDataCenterBGPSourceIP_Type = VmwNsxTDataCenterBGPSourceIPType
_VmwNsxTDataCenterBGPSourceIP_Object = MibScalar
vmwNsxTDataCenterBGPSourceIP = _VmwNsxTDataCenterBGPSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 66),
    _VmwNsxTDataCenterBGPSourceIP_Type()
)
vmwNsxTDataCenterBGPSourceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBGPSourceIP.setStatus("current")
_VmwNsxTDataCenterRemoteSiteId_Type = VmwNsxTDataCenterRemoteSiteIdType
_VmwNsxTDataCenterRemoteSiteId_Object = MibScalar
vmwNsxTDataCenterRemoteSiteId = _VmwNsxTDataCenterRemoteSiteId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 67),
    _VmwNsxTDataCenterRemoteSiteId_Type()
)
vmwNsxTDataCenterRemoteSiteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteSiteId.setStatus("current")
_VmwNsxTDataCenterSiteId_Type = VmwNsxTDataCenterSiteIdType
_VmwNsxTDataCenterSiteId_Object = MibScalar
vmwNsxTDataCenterSiteId = _VmwNsxTDataCenterSiteId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 68),
    _VmwNsxTDataCenterSiteId_Type()
)
vmwNsxTDataCenterSiteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSiteId.setStatus("current")
_VmwNsxTDataCenterSiteName_Type = VmwNsxTDataCenterSiteNameType
_VmwNsxTDataCenterSiteName_Object = MibScalar
vmwNsxTDataCenterSiteName = _VmwNsxTDataCenterSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 69),
    _VmwNsxTDataCenterSiteName_Type()
)
vmwNsxTDataCenterSiteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSiteName.setStatus("current")
_VmwNsxTDataCenterLrId_Type = VmwNsxTDataCenterLrIdType
_VmwNsxTDataCenterLrId_Object = MibScalar
vmwNsxTDataCenterLrId = _VmwNsxTDataCenterLrId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 70),
    _VmwNsxTDataCenterLrId_Type()
)
vmwNsxTDataCenterLrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLrId.setStatus("current")
_VmwNsxTDataCenterRxMisses_Type = VmwNsxTDataCenterRxMissesType
_VmwNsxTDataCenterRxMisses_Object = MibScalar
vmwNsxTDataCenterRxMisses = _VmwNsxTDataCenterRxMisses_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 71),
    _VmwNsxTDataCenterRxMisses_Type()
)
vmwNsxTDataCenterRxMisses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRxMisses.setStatus("current")
_VmwNsxTDataCenterRxProcessed_Type = VmwNsxTDataCenterRxProcessedType
_VmwNsxTDataCenterRxProcessed_Object = MibScalar
vmwNsxTDataCenterRxProcessed = _VmwNsxTDataCenterRxProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 72),
    _VmwNsxTDataCenterRxProcessed_Type()
)
vmwNsxTDataCenterRxProcessed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRxProcessed.setStatus("current")
_VmwNsxTDataCenterTxMisses_Type = VmwNsxTDataCenterTxMissesType
_VmwNsxTDataCenterTxMisses_Object = MibScalar
vmwNsxTDataCenterTxMisses = _VmwNsxTDataCenterTxMisses_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 73),
    _VmwNsxTDataCenterTxMisses_Type()
)
vmwNsxTDataCenterTxMisses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTxMisses.setStatus("current")
_VmwNsxTDataCenterTxProcessed_Type = VmwNsxTDataCenterTxProcessedType
_VmwNsxTDataCenterTxProcessed_Object = MibScalar
vmwNsxTDataCenterTxProcessed = _VmwNsxTDataCenterTxProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 74),
    _VmwNsxTDataCenterTxProcessed_Type()
)
vmwNsxTDataCenterTxProcessed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTxProcessed.setStatus("current")
_VmwNsxTDataCenterLrportId_Type = VmwNsxTDataCenterLrportIdType
_VmwNsxTDataCenterLrportId_Object = MibScalar
vmwNsxTDataCenterLrportId = _VmwNsxTDataCenterLrportId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 75),
    _VmwNsxTDataCenterLrportId_Type()
)
vmwNsxTDataCenterLrportId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLrportId.setStatus("current")
_VmwNsxTDataCenterServiceIP_Type = VmwNsxTDataCenterServiceIPType
_VmwNsxTDataCenterServiceIP_Object = MibScalar
vmwNsxTDataCenterServiceIP = _VmwNsxTDataCenterServiceIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 77),
    _VmwNsxTDataCenterServiceIP_Type()
)
vmwNsxTDataCenterServiceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterServiceIP.setStatus("current")
_VmwNsxTDataCenterRemoteManagerNodeId_Type = VmwNsxTDataCenterRemoteManagerNodeIdType
_VmwNsxTDataCenterRemoteManagerNodeId_Object = MibScalar
vmwNsxTDataCenterRemoteManagerNodeId = _VmwNsxTDataCenterRemoteManagerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 80),
    _VmwNsxTDataCenterRemoteManagerNodeId_Type()
)
vmwNsxTDataCenterRemoteManagerNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteManagerNodeId.setStatus("current")
_VmwNsxTDataCenterDirectoryDomain_Type = VmwNsxTDataCenterDirectoryDomainType
_VmwNsxTDataCenterDirectoryDomain_Object = MibScalar
vmwNsxTDataCenterDirectoryDomain = _VmwNsxTDataCenterDirectoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 81),
    _VmwNsxTDataCenterDirectoryDomain_Type()
)
vmwNsxTDataCenterDirectoryDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDirectoryDomain.setStatus("current")
_VmwNsxTDataCenterTimeoutInMinutes_Type = VmwNsxTDataCenterTimeoutInMinutesType
_VmwNsxTDataCenterTimeoutInMinutes_Object = MibScalar
vmwNsxTDataCenterTimeoutInMinutes = _VmwNsxTDataCenterTimeoutInMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 82),
    _VmwNsxTDataCenterTimeoutInMinutes_Type()
)
vmwNsxTDataCenterTimeoutInMinutes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTimeoutInMinutes.setStatus("current")
_VmwNsxTDataCenterMaxCapacityThreshold_Type = VmwNsxTDataCenterMaxCapacityThresholdType
_VmwNsxTDataCenterMaxCapacityThreshold_Object = MibScalar
vmwNsxTDataCenterMaxCapacityThreshold = _VmwNsxTDataCenterMaxCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 83),
    _VmwNsxTDataCenterMaxCapacityThreshold_Type()
)
vmwNsxTDataCenterMaxCapacityThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMaxCapacityThreshold.setStatus("current")
_VmwNsxTDataCenterMinCapacityThreshold_Type = VmwNsxTDataCenterMinCapacityThresholdType
_VmwNsxTDataCenterMinCapacityThreshold_Object = MibScalar
vmwNsxTDataCenterMinCapacityThreshold = _VmwNsxTDataCenterMinCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 84),
    _VmwNsxTDataCenterMinCapacityThreshold_Type()
)
vmwNsxTDataCenterMinCapacityThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMinCapacityThreshold.setStatus("current")
_VmwNsxTDataCenterMaxSupportedCapacityCount_Type = VmwNsxTDataCenterMaxSupportedCapacityCountType
_VmwNsxTDataCenterMaxSupportedCapacityCount_Object = MibScalar
vmwNsxTDataCenterMaxSupportedCapacityCount = _VmwNsxTDataCenterMaxSupportedCapacityCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 85),
    _VmwNsxTDataCenterMaxSupportedCapacityCount_Type()
)
vmwNsxTDataCenterMaxSupportedCapacityCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMaxSupportedCapacityCount.setStatus("current")
_VmwNsxTDataCenterLatencySource_Type = VmwNsxTDataCenterLatencySourceType
_VmwNsxTDataCenterLatencySource_Object = MibScalar
vmwNsxTDataCenterLatencySource = _VmwNsxTDataCenterLatencySource_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 86),
    _VmwNsxTDataCenterLatencySource_Type()
)
vmwNsxTDataCenterLatencySource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLatencySource.setStatus("current")
_VmwNsxTDataCenterLatencyThreshold_Type = VmwNsxTDataCenterLatencyThresholdType
_VmwNsxTDataCenterLatencyThreshold_Object = MibScalar
vmwNsxTDataCenterLatencyThreshold = _VmwNsxTDataCenterLatencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 87),
    _VmwNsxTDataCenterLatencyThreshold_Type()
)
vmwNsxTDataCenterLatencyThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLatencyThreshold.setStatus("current")
_VmwNsxTDataCenterLatencyValue_Type = VmwNsxTDataCenterLatencyValueType
_VmwNsxTDataCenterLatencyValue_Object = MibScalar
vmwNsxTDataCenterLatencyValue = _VmwNsxTDataCenterLatencyValue_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 88),
    _VmwNsxTDataCenterLatencyValue_Type()
)
vmwNsxTDataCenterLatencyValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLatencyValue.setStatus("current")
_VmwNsxTDataCenterApplianceFQDN_Type = VmwNsxTDataCenterApplianceFQDNType
_VmwNsxTDataCenterApplianceFQDN_Object = MibScalar
vmwNsxTDataCenterApplianceFQDN = _VmwNsxTDataCenterApplianceFQDN_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 89),
    _VmwNsxTDataCenterApplianceFQDN_Type()
)
vmwNsxTDataCenterApplianceFQDN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterApplianceFQDN.setStatus("current")
_VmwNsxTDataCenterRemoteApplianceAddress_Type = VmwNsxTDataCenterRemoteApplianceAddressType
_VmwNsxTDataCenterRemoteApplianceAddress_Object = MibScalar
vmwNsxTDataCenterRemoteApplianceAddress = _VmwNsxTDataCenterRemoteApplianceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 90),
    _VmwNsxTDataCenterRemoteApplianceAddress_Type()
)
vmwNsxTDataCenterRemoteApplianceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteApplianceAddress.setStatus("current")
_VmwNsxTDataCenterManagerNodeId_Type = VmwNsxTDataCenterManagerNodeIdType
_VmwNsxTDataCenterManagerNodeId_Object = MibScalar
vmwNsxTDataCenterManagerNodeId = _VmwNsxTDataCenterManagerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 91),
    _VmwNsxTDataCenterManagerNodeId_Type()
)
vmwNsxTDataCenterManagerNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterManagerNodeId.setStatus("current")
_VmwNsxTDataCenterDisplayedLicenseKey_Type = VmwNsxTDataCenterDisplayedLicenseKeyType
_VmwNsxTDataCenterDisplayedLicenseKey_Object = MibScalar
vmwNsxTDataCenterDisplayedLicenseKey = _VmwNsxTDataCenterDisplayedLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 92),
    _VmwNsxTDataCenterDisplayedLicenseKey_Type()
)
vmwNsxTDataCenterDisplayedLicenseKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDisplayedLicenseKey.setStatus("current")
_VmwNsxTDataCenterEdgeThreadName_Type = VmwNsxTDataCenterEdgeThreadNameType
_VmwNsxTDataCenterEdgeThreadName_Object = MibScalar
vmwNsxTDataCenterEdgeThreadName = _VmwNsxTDataCenterEdgeThreadName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 93),
    _VmwNsxTDataCenterEdgeThreadName_Type()
)
vmwNsxTDataCenterEdgeThreadName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeThreadName.setStatus("current")
_VmwNsxTDataCenterIntentPath_Type = VmwNsxTDataCenterIntentPathType
_VmwNsxTDataCenterIntentPath_Object = MibScalar
vmwNsxTDataCenterIntentPath = _VmwNsxTDataCenterIntentPath_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 94),
    _VmwNsxTDataCenterIntentPath_Type()
)
vmwNsxTDataCenterIntentPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterIntentPath.setStatus("current")
_VmwNsxTDataCenterConformance_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterConformance = _VmwNsxTDataCenterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2)
)
_VmwNsxTDataCenterCompliances_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterCompliances = _VmwNsxTDataCenterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1)
)
_VmwNsxTDataCenterSMIBGroups_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterSMIBGroups = _VmwNsxTDataCenterSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2)
)

# Managed Objects groups

vmwNsxTDataCenterNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 1)
)
vmwNsxTDataCenterNotificationInfoGroup.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPPoolUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDuplicateIPAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFailureReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHeapType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMempoolName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPasswordExpirationDays"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSessionDownReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterStaticAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTunnelDownReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 3)
)
vmwNsxTDataCenterNotificationInfoGroup2.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPSourceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup2.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 5)
)
vmwNsxTDataCenterNotificationInfoGroup3.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxProcessed"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxProcessed"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup3.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 7)
)
vmwNsxTDataCenterNotificationInfoGroup4.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManager"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManagers"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceFQDN"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDirectoryDomain"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeThreadName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHostnameOrIPAddressWithPort"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIDSEventsCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLDAPServer"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencySource"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyValue"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxIDSEventsAllowed"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxSupportedCapacityCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMinCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimeoutInMinutes"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup4.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 11)
)
vmwNsxTDataCenterNotificationInfoGroup6.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrportId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup6.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 13)
)
vmwNsxTDataCenterNotificationInfoGroup7.setObjects(
    ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath")
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup7.setStatus("current")


# Notification objects

vmwNsxTManagerHealthManagerCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 1)
)
vmwNsxTManagerHealthManagerCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 2)
)
vmwNsxTManagerHealthManagerCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 3)
)
vmwNsxTManagerHealthManagerCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 4)
)
vmwNsxTManagerHealthManagerCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 5)
)
vmwNsxTManagerHealthManagerMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 6)
)
vmwNsxTManagerHealthManagerMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 7)
)
vmwNsxTManagerHealthManagerMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 8)
)
vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 9)
)
vmwNsxTManagerHealthManagerDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 10)
)
vmwNsxTManagerHealthManagerDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 11)
)
vmwNsxTManagerHealthManagerDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 12)
)
vmwNsxTManagerHealthManagerDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 13)
)
vmwNsxTManagerHealthManagerConfigDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 14)
)
vmwNsxTManagerHealthManagerConfigDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 15)
)
vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 16)
)
vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthDuplicateIPAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 17)
)
vmwNsxTManagerHealthDuplicateIPAddress.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDuplicateIPAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthDuplicateIPAddress.setStatus(
        "current"
    )

vmwNsxTManagerHealthDuplicateIPAddressClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 18)
)
vmwNsxTManagerHealthDuplicateIPAddressClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDuplicateIPAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthDuplicateIPAddressClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 19)
)
vmwNsxTManagerHealthOperationsDbDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 20)
)
vmwNsxTManagerHealthOperationsDbDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 21)
)
vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 22)
)
vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthStorageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 23)
)
vmwNsxTManagerHealthStorageError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthStorageError.setStatus(
        "current"
    )

vmwNsxTManagerHealthStorageErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 24)
)
vmwNsxTManagerHealthStorageErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthStorageErrorClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 1)
)
vmwNsxTEdgeHealthEdgeCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 2)
)
vmwNsxTEdgeHealthEdgeCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 3)
)
vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 4)
)
vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 5)
)
vmwNsxTEdgeHealthEdgeMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 6)
)
vmwNsxTEdgeHealthEdgeMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 7)
)
vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 8)
)
vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 9)
)
vmwNsxTEdgeHealthEdgeDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 10)
)
vmwNsxTEdgeHealthEdgeDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 11)
)
vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 12)
)
vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 17)
)
vmwNsxTEdgeHealthEdgeDatapathCPUHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 18)
)
vmwNsxTEdgeHealthEdgeDatapathCPUHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 19)
)
vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 20)
)
vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 21)
)
vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 22)
)
vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 23)
)
vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 24)
)
vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathMempoolHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 25)
)
vmwNsxTEdgeHealthEdgeDatapathMempoolHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMempoolName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathMempoolHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 26)
)
vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMempoolName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 27)
)
vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 28)
)
vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICLinkStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 29)
)
vmwNsxTEdgeHealthEdgeNICLinkStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICLinkStatusDown.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 30)
)
vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 31)
)
vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxProcessed"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 32)
)
vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 33)
)
vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxProcessed"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 34)
)
vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthStorageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 37)
)
vmwNsxTEdgeHealthStorageError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthStorageError.setStatus(
        "current"
    )

vmwNsxTEdgeHealthStorageErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 38)
)
vmwNsxTEdgeHealthStorageErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthStorageErrorClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthDatapathThreadDeadlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 45)
)
vmwNsxTEdgeHealthDatapathThreadDeadlocked.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeThreadName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthDatapathThreadDeadlocked.setStatus(
        "current"
    )

vmwNsxTEdgeHealthDatapathThreadDeadlockedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 46)
)
vmwNsxTEdgeHealthDatapathThreadDeadlockedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeThreadName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthDatapathThreadDeadlockedClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpirationApproaching = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 1)
)
vmwNsxTCertificatesCertificateExpirationApproaching.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpirationApproaching.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpirationApproachingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 2)
)
vmwNsxTCertificatesCertificateExpirationApproachingClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpirationApproachingClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 3)
)
vmwNsxTCertificatesCertificateExpired.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpired.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 4)
)
vmwNsxTCertificatesCertificateExpiredClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpiredClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateIsAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 5)
)
vmwNsxTCertificatesCertificateIsAboutToExpire.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateIsAboutToExpire.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateIsAboutToExpireClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 6)
)
vmwNsxTCertificatesCertificateIsAboutToExpireClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateIsAboutToExpireClear.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpirationApproaching = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 1)
)
vmwNsxTPasswordManagementPasswordExpirationApproaching.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPasswordExpirationDays"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpirationApproaching.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpirationApproachingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 2)
)
vmwNsxTPasswordManagementPasswordExpirationApproachingClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpirationApproachingClear.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 3)
)
vmwNsxTPasswordManagementPasswordExpired.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpired.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 4)
)
vmwNsxTPasswordManagementPasswordExpiredClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpiredClear.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordIsAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 5)
)
vmwNsxTPasswordManagementPasswordIsAboutToExpire.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPasswordExpirationDays"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordIsAboutToExpire.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordIsAboutToExpireClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 6)
)
vmwNsxTPasswordManagementPasswordIsAboutToExpireClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordIsAboutToExpireClear.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 1)
)
vmwNsxTLicensesLicenseExpired.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseExpired.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseExpiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 2)
)
vmwNsxTLicensesLicenseExpiredClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseExpiredClear.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseIsAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 3)
)
vmwNsxTLicensesLicenseIsAboutToExpire.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseIsAboutToExpire.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseIsAboutToExpireClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 4)
)
vmwNsxTLicensesLicenseIsAboutToExpireClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseIsAboutToExpireClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 41)
)
vmwNsxTIntelligenceHealthCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 42)
)
vmwNsxTIntelligenceHealthCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 43)
)
vmwNsxTIntelligenceHealthCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 44)
)
vmwNsxTIntelligenceHealthCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 45)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 46)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 47)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 48)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 49)
)
vmwNsxTIntelligenceHealthDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 50)
)
vmwNsxTIntelligenceHealthDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 51)
)
vmwNsxTIntelligenceHealthDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 52)
)
vmwNsxTIntelligenceHealthDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 53)
)
vmwNsxTIntelligenceHealthMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 54)
)
vmwNsxTIntelligenceHealthMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 55)
)
vmwNsxTIntelligenceHealthMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 56)
)
vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthNodeStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 57)
)
vmwNsxTIntelligenceHealthNodeStatusDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthNodeStatusDegraded.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthNodeStatusDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 58)
)
vmwNsxTIntelligenceHealthNodeStatusDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthNodeStatusDegradedClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthStorageLatencyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 63)
)
vmwNsxTIntelligenceHealthStorageLatencyHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthStorageLatencyHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthStorageLatencyHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 64)
)
vmwNsxTIntelligenceHealthStorageLatencyHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthStorageLatencyHighClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureCommunicationEdgeTunnelsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7, 0, 17)
)
vmwNsxTInfrastructureCommunicationEdgeTunnelsDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationEdgeTunnelsDown.setStatus(
        "current"
    )

vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7, 0, 18)
)
vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9, 0, 7)
)
vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected.setStatus(
        "current"
    )

vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9, 0, 8)
)
vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear.setStatus(
        "current"
    )

vmwNsxTCniHealthHyperbusManagerConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10, 0, 3)
)
vmwNsxTCniHealthHyperbusManagerConnectionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthHyperbusManagerConnectionDown.setStatus(
        "current"
    )

vmwNsxTCniHealthHyperbusManagerConnectionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10, 0, 4)
)
vmwNsxTCniHealthHyperbusManagerConnectionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthHyperbusManagerConnectionDownClear.setStatus(
        "current"
    )

vmwNsxTNCPHealthNCPPluginDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11, 0, 3)
)
vmwNsxTNCPHealthNCPPluginDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthNCPPluginDown.setStatus(
        "current"
    )

vmwNsxTNCPHealthNCPPluginDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11, 0, 4)
)
vmwNsxTNCPHealthNCPPluginDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthNCPPluginDownClear.setStatus(
        "current"
    )

vmwNsxTNodeAgentsHealthNodeAgentsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12, 0, 3)
)
vmwNsxTNodeAgentsHealthNodeAgentsDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthNodeAgentsDown.setStatus(
        "current"
    )

vmwNsxTNodeAgentsHealthNodeAgentsDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12, 0, 4)
)
vmwNsxTNodeAgentsHealthNodeAgentsDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthNodeAgentsDownClear.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionEAMStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 1)
)
vmwNsxTEndpointProtectionEAMStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionEAMStatusDown.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionEAMStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 2)
)
vmwNsxTEndpointProtectionEAMStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionEAMStatusDownClear.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionPartnerChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 3)
)
vmwNsxTEndpointProtectionPartnerChannelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionPartnerChannelDown.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionPartnerChannelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 4)
)
vmwNsxTEndpointProtectionPartnerChannelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionPartnerChannelDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 7)
)
vmwNsxTVPNIPsecPolicyBasedSessionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSessionDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedSessionDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedSessionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 8)
)
vmwNsxTVPNIPsecPolicyBasedSessionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedSessionDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 9)
)
vmwNsxTVPNIPsecPolicyBasedTunnelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedTunnelDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedTunnelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 10)
)
vmwNsxTVPNIPsecPolicyBasedTunnelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedTunnelDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 11)
)
vmwNsxTVPNIPsecRouteBasedSessionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSessionDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedSessionDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedSessionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 12)
)
vmwNsxTVPNIPsecRouteBasedSessionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedSessionDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 13)
)
vmwNsxTVPNIPsecRouteBasedTunnelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTunnelDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedTunnelDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedTunnelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 14)
)
vmwNsxTVPNIPsecRouteBasedTunnelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedTunnelDownClear.setStatus(
        "current"
    )

vmwNsxTVPNL2VpnSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 15)
)
vmwNsxTVPNL2VpnSessionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNL2VpnSessionDown.setStatus(
        "current"
    )

vmwNsxTVPNL2VpnSessionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 16)
)
vmwNsxTVPNL2VpnSessionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNL2VpnSessionDownClear.setStatus(
        "current"
    )

vmwNsxTAlarmManagementAlarmServiceOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 1)
)
vmwNsxTAlarmManagementAlarmServiceOverloaded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementAlarmServiceOverloaded.setStatus(
        "current"
    )

vmwNsxTAlarmManagementAlarmServiceOverloadedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 2)
)
vmwNsxTAlarmManagementAlarmServiceOverloadedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementAlarmServiceOverloadedClear.setStatus(
        "current"
    )

vmwNsxTAlarmManagementHeavyVolumeOfAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 3)
)
vmwNsxTAlarmManagementHeavyVolumeOfAlarms.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementHeavyVolumeOfAlarms.setStatus(
        "current"
    )

vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 4)
)
vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBCPUVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 1)
)
vmwNsxTLoadBalancerLBCPUVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBCPUVeryHigh.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBCPUVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 2)
)
vmwNsxTLoadBalancerLBCPUVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBCPUVeryHighClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 3)
)
vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 4)
)
vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 5)
)
vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 6)
)
vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 7)
)
vmwNsxTLoadBalancerLBStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 8)
)
vmwNsxTLoadBalancerLBStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDownClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerPoolStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 9)
)
vmwNsxTLoadBalancerPoolStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerPoolStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerPoolStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 10)
)
vmwNsxTLoadBalancerPoolStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerPoolStatusDownClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerVirtualServerStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 11)
)
vmwNsxTLoadBalancerVirtualServerStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerVirtualServerStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerVirtualServerStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 12)
)
vmwNsxTLoadBalancerVirtualServerStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerVirtualServerStatusDownClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 15)
)
vmwNsxTLoadBalancerLBStatusDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDegraded.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 16)
)
vmwNsxTLoadBalancerLBStatusDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDegradedClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerDLBStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 17)
)
vmwNsxTLoadBalancerDLBStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerDLBStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerDLBStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 18)
)
vmwNsxTLoadBalancerDLBStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerDLBStatusDownClear.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthNVDSUplinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 3)
)
vmwNsxTTransportNodeHealthNVDSUplinkDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthNVDSUplinkDown.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthNVDSUplinkDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 4)
)
vmwNsxTTransportNodeHealthNVDSUplinkDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthNVDSUplinkDownClear.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthLAGMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 5)
)
vmwNsxTTransportNodeHealthLAGMemberDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthLAGMemberDown.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthLAGMemberDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 6)
)
vmwNsxTTransportNodeHealthLAGMemberDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthLAGMemberDownClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 1)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusChanged.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentServiceState"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusChanged.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 2)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentServiceState"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 3)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusDown.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 4)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceServiceStatusUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 7)
)
vmwNsxTInfrastructureServiceServiceStatusUnknown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceServiceStatusUnknown.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceServiceStatusUnknownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 8)
)
vmwNsxTInfrastructureServiceServiceStatusUnknownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceServiceStatusUnknownClear.setStatus(
        "current"
    )

vmwNsxTDHCPPoolLeaseAllocationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 1)
)
vmwNsxTDHCPPoolLeaseAllocationFailed.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolLeaseAllocationFailed.setStatus(
        "current"
    )

vmwNsxTDHCPPoolLeaseAllocationFailedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 2)
)
vmwNsxTDHCPPoolLeaseAllocationFailedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolLeaseAllocationFailedClear.setStatus(
        "current"
    )

vmwNsxTDHCPPoolOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 3)
)
vmwNsxTDHCPPoolOverloaded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPPoolUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolOverloaded.setStatus(
        "current"
    )

vmwNsxTDHCPPoolOverloadedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 4)
)
vmwNsxTDHCPPoolOverloadedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolOverloadedClear.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier0GatewayFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 9)
)
vmwNsxTHighAvailabilityTier0GatewayFailover.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentGatewayState"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier0GatewayFailover.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier0GatewayFailoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 10)
)
vmwNsxTHighAvailabilityTier0GatewayFailoverClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier0GatewayFailoverClear.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier1GatewayFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 11)
)
vmwNsxTHighAvailabilityTier1GatewayFailover.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentGatewayState"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier1GatewayFailover.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier1GatewayFailoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 12)
)
vmwNsxTHighAvailabilityTier1GatewayFailoverClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier1GatewayFailoverClear.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 1)
)
vmwNsxTCapacityMaximumCapacity.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxSupportedCapacityCount"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacity.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 2)
)
vmwNsxTCapacityMaximumCapacityClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxSupportedCapacityCount"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacityClear.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacityThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 3)
)
vmwNsxTCapacityMaximumCapacityThreshold.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacityThreshold.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacityThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 4)
)
vmwNsxTCapacityMaximumCapacityThresholdClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacityThresholdClear.setStatus(
        "current"
    )

vmwNsxTCapacityMinimumCapacityThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 5)
)
vmwNsxTCapacityMinimumCapacityThreshold.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMinCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMinimumCapacityThreshold.setStatus(
        "current"
    )

vmwNsxTCapacityMinimumCapacityThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 6)
)
vmwNsxTCapacityMinimumCapacityThresholdClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMinCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMinimumCapacityThresholdClear.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthAuditLogFileUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 1)
)
vmwNsxTAuditLogHealthAuditLogFileUpdateError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthAuditLogFileUpdateError.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 2)
)
vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthRemoteLoggingServerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 3)
)
vmwNsxTAuditLogHealthRemoteLoggingServerError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHostnameOrIPAddressWithPort"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthRemoteLoggingServerError.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 4)
)
vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHostnameOrIPAddressWithPort"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear.setStatus(
        "current"
    )

vmwNsxTRoutingBGPDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 1)
)
vmwNsxTRoutingBGPDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFailureReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBGPDown.setStatus(
        "current"
    )

vmwNsxTRoutingBGPDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 2)
)
vmwNsxTRoutingBGPDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBGPDownClear.setStatus(
        "current"
    )

vmwNsxTRoutingStaticRoutingRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 5)
)
vmwNsxTRoutingStaticRoutingRemoved.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterStaticAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingStaticRoutingRemoved.setStatus(
        "current"
    )

vmwNsxTRoutingStaticRoutingRemovedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 6)
)
vmwNsxTRoutingStaticRoutingRemovedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterStaticAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingStaticRoutingRemovedClear.setStatus(
        "current"
    )

vmwNsxTRoutingBFDDownOnExternalInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 7)
)
vmwNsxTRoutingBFDDownOnExternalInterface.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBFDDownOnExternalInterface.setStatus(
        "current"
    )

vmwNsxTRoutingBFDDownOnExternalInterfaceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 8)
)
vmwNsxTRoutingBFDDownOnExternalInterfaceClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBFDDownOnExternalInterfaceClear.setStatus(
        "current"
    )

vmwNsxTRoutingRoutingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 9)
)
vmwNsxTRoutingRoutingDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingRoutingDown.setStatus(
        "current"
    )

vmwNsxTRoutingRoutingDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 10)
)
vmwNsxTRoutingRoutingDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingRoutingDownClear.setStatus(
        "current"
    )

vmwNsxTRoutingOSPFNeighborWentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 11)
)
vmwNsxTRoutingOSPFNeighborWentDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingOSPFNeighborWentDown.setStatus(
        "current"
    )

vmwNsxTRoutingOSPFNeighborWentDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 12)
)
vmwNsxTRoutingOSPFNeighborWentDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingOSPFNeighborWentDownClear.setStatus(
        "current"
    )

vmwNsxTRoutingProxyARPNotConfiguredForServiceIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 13)
)
vmwNsxTRoutingProxyARPNotConfiguredForServiceIP.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrportId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingProxyARPNotConfiguredForServiceIP.setStatus(
        "current"
    )

vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 14)
)
vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrportId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 1)
)
vmwNsxTDNSForwarderDisabled.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDisabled.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDisabledClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 2)
)
vmwNsxTDNSForwarderDisabledClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDisabledClear.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 3)
)
vmwNsxTDNSForwarderDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDown.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 4)
)
vmwNsxTDNSForwarderDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDownClear.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 1)
)
vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 2)
)
vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 3)
)
vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHeapType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 4)
)
vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHeapType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTFederationRtepBGPDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 1)
)
vmwNsxTFederationRtepBGPDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPSourceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFailureReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepBGPDown.setStatus(
        "current"
    )

vmwNsxTFederationRtepBGPDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 2)
)
vmwNsxTFederationRtepBGPDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPSourceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepBGPDownClear.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 3)
)
vmwNsxTFederationLmToLmSynchronizationError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationError.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 4)
)
vmwNsxTFederationLmToLmSynchronizationErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationErrorClear.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 5)
)
vmwNsxTFederationLmToLmSynchronizationWarning.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationWarning.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 6)
)
vmwNsxTFederationLmToLmSynchronizationWarningClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationWarningClear.setStatus(
        "current"
    )

vmwNsxTFederationRtepConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 7)
)
vmwNsxTFederationRtepConnectivityLost.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepConnectivityLost.setStatus(
        "current"
    )

vmwNsxTFederationRtepConnectivityLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 8)
)
vmwNsxTFederationRtepConnectivityLostClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepConnectivityLostClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSplitBrain = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 9)
)
vmwNsxTFederationGMToGMSplitBrain.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManagers"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSplitBrain.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSplitBrainClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 10)
)
vmwNsxTFederationGMToGMSplitBrainClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManager"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSplitBrainClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSMaxEventsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 3)
)
vmwNsxTDistributedIDSIPSMaxEventsReached.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIDSEventsCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxIDSEventsAllowed"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSMaxEventsReached.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSMaxEventsReachedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 4)
)
vmwNsxTDistributedIDSIPSMaxEventsReachedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIDSEventsCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxIDSEventsAllowed"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSMaxEventsReachedClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 7)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 8)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 9)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 10)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 13)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineDown.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 14)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 15)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 16)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 17)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 18)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 19)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 20)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 21)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 22)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 1)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDown.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 2)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerControlChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 3)
)
vmwNsxTCommunicationManagerControlChannelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerControlChannelDown.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerControlChannelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 4)
)
vmwNsxTCommunicationManagerControlChannelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerControlChannelDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDownLg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 5)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDownLg.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDownLg.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 6)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 7)
)
vmwNsxTCommunicationControlChannelToManagerNodeDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimeoutInMinutes"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDown.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 8)
)
vmwNsxTCommunicationControlChannelToManagerNodeDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 9)
)
vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimeoutInMinutes"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 10)
)
vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 11)
)
vmwNsxTCommunicationControlChannelToTransportNodeDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDown.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 12)
)
vmwNsxTCommunicationControlChannelToTransportNodeDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerClusterLatencyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 17)
)
vmwNsxTCommunicationManagerClusterLatencyHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerClusterLatencyHigh.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerClusterLatencyHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 18)
)
vmwNsxTCommunicationManagerClusterLatencyHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerClusterLatencyHighClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDownLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 19)
)
vmwNsxTCommunicationControlChannelToTransportNodeDownLong.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDownLong.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 20)
)
vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNLookupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 21)
)
vmwNsxTCommunicationManagerFQDNLookupFailure.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceFQDN"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNLookupFailure.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNLookupFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 22)
)
vmwNsxTCommunicationManagerFQDNLookupFailureClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceFQDN"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNLookupFailureClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNReverseLookupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 23)
)
vmwNsxTCommunicationManagerFQDNReverseLookupFailure.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNReverseLookupFailure.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 24)
)
vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallConnectivityToLDAPServerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 1)
)
vmwNsxTIdentityFirewallConnectivityToLDAPServerLost.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLDAPServer"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallConnectivityToLDAPServerLost.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 2)
)
vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLDAPServer"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallErrorInDeltaSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 3)
)
vmwNsxTIdentityFirewallErrorInDeltaSync.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDirectoryDomain"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallErrorInDeltaSync.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallErrorInDeltaSyncClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 4)
)
vmwNsxTIdentityFirewallErrorInDeltaSyncClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDirectoryDomain"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallErrorInDeltaSyncClear.setStatus(
        "current"
    )

vmwNsxTIPAMIPBlockUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 1)
)
vmwNsxTIPAMIPBlockUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPBlockUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIPAMIPBlockUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 2)
)
vmwNsxTIPAMIPBlockUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPBlockUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIPAMIPPoolUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 3)
)
vmwNsxTIPAMIPPoolUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPPoolUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIPAMIPPoolUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 4)
)
vmwNsxTIPAMIPPoolUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPPoolUsageVeryHighClear.setStatus(
        "current"
    )


# Notifications groups

vmwNsxTDataCenterNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 2)
)
vmwNsxTDataCenterNotificationGroup.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementAlarmServiceOverloaded"),
        ("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementAlarmServiceOverloadedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementHeavyVolumeOfAlarms"),
        ("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpirationApproaching"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpirationApproachingClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpired"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpiredClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateIsAboutToExpire"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateIsAboutToExpireClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCniHealthHyperbusManagerConnectionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCniHealthHyperbusManagerConnectionDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolLeaseAllocationFailed"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolLeaseAllocationFailedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolOverloaded"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolOverloadedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDisabled"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDisabledClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathMempoolHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICLinkStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionEAMStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionEAMStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionPartnerChannelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionPartnerChannelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier0GatewayFailover"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier0GatewayFailoverClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier1GatewayFailover"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier1GatewayFailoverClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureCommunicationEdgeTunnelsDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusChanged"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthNodeStatusDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthNodeStatusDegradedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseExpired"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseExpiredClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseIsAboutToExpire"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseIsAboutToExpireClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBCPUVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBCPUVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerPoolStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerPoolStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerVirtualServerStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerVirtualServerStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthDuplicateIPAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthDuplicateIPAddressClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNCPHealthNCPPluginDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTNCPHealthNCPPluginDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNodeAgentsHealthNodeAgentsDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTNodeAgentsHealthNodeAgentsDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpirationApproaching"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpirationApproachingClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpired"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpiredClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordIsAboutToExpire"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordIsAboutToExpireClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBFDDownOnExternalInterface"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBFDDownOnExternalInterfaceClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBGPDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBGPDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingRoutingDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingRoutingDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingStaticRoutingRemoved"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingStaticRoutingRemovedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthLAGMemberDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthLAGMemberDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthNVDSUplinkDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthNVDSUplinkDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedSessionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedSessionDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedTunnelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedTunnelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedSessionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedSessionDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedTunnelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedTunnelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNL2VpnSessionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNL2VpnSessionDownClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 4)
)
vmwNsxTDataCenterNotificationGroup2.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthStorageError"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthStorageErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationError"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationWarning"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationWarningClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepBGPDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepBGPDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup2.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 6)
)
vmwNsxTDataCenterNotificationGroup3.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDownLg"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerControlChannelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerControlChannelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepConnectivityLost"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepConnectivityLostClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthStorageError"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthStorageErrorClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup3.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 8)
)
vmwNsxTDataCenterNotificationGroup4.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthAuditLogFileUpdateError"),
        ("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthRemoteLoggingServerError"),
        ("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacity"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacityClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacityThresholdClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMinimumCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMinimumCapacityThresholdClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDownLong"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerClusterLatencyHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerClusterLatencyHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNLookupFailure"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNLookupFailureClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNReverseLookupFailure"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSMaxEventsReached"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSMaxEventsReachedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthDatapathThreadDeadlocked"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthDatapathThreadDeadlockedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSplitBrain"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSplitBrainClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallConnectivityToLDAPServerLost"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallErrorInDeltaSync"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallErrorInDeltaSyncClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceServiceStatusUnknown"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceServiceStatusUnknownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthStorageLatencyHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthStorageLatencyHighClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup4.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup5 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 10)
)
vmwNsxTDataCenterNotificationGroup5.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTRoutingOSPFNeighborWentDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingOSPFNeighborWentDownClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup5.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup6 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 12)
)
vmwNsxTDataCenterNotificationGroup6.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTRoutingProxyARPNotConfiguredForServiceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup6.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup7 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 14)
)
vmwNsxTDataCenterNotificationGroup7.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTIPAMIPBlockUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIPAMIPBlockUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIPAMIPPoolUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIPAMIPPoolUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerDLBStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerDLBStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDegradedClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup7.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwNsxTDataCenterBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 1)
)
vmwNsxTDataCenterBasicCompliance.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 2)
)
vmwNsxTDataCenterBasicCompliance2.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance2.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 3)
)
vmwNsxTDataCenterBasicCompliance3.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance3.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 4)
)
vmwNsxTDataCenterBasicCompliance4.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance4.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 5)
)
vmwNsxTDataCenterBasicCompliance5.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance5.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 6)
)
vmwNsxTDataCenterBasicCompliance6.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup6"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance6.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 7)
)
vmwNsxTDataCenterBasicCompliance7.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup7"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup7"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-NSX-MIB",
    **{"VmwNsxTDataCenterFeatureIdType": VmwNsxTDataCenterFeatureIdType,
       "VmwNsxTDataCenterEventTypeType": VmwNsxTDataCenterEventTypeType,
       "VmwNsxTDataCenterSeverityType": VmwNsxTDataCenterSeverityType,
       "VmwNsxTDataCenterNodeIdType": VmwNsxTDataCenterNodeIdType,
       "VmwNsxTDataCenterNodeTypeType": VmwNsxTDataCenterNodeTypeType,
       "VmwNsxTDataCenterEntityIdType": VmwNsxTDataCenterEntityIdType,
       "VmwNsxTDataCenterSystemResourceUsageType": VmwNsxTDataCenterSystemResourceUsageType,
       "VmwNsxTDataCenterDiskPartitionNameType": VmwNsxTDataCenterDiskPartitionNameType,
       "VmwNsxTDataCenterLicenseEditionTypeType": VmwNsxTDataCenterLicenseEditionTypeType,
       "VmwNsxTDataCenterApplianceAddressType": VmwNsxTDataCenterApplianceAddressType,
       "VmwNsxTDataCenterCurrentGatewayStateType": VmwNsxTDataCenterCurrentGatewayStateType,
       "VmwNsxTDataCenterCurrentServiceStateType": VmwNsxTDataCenterCurrentServiceStateType,
       "VmwNsxTDataCenterDatapathResourceUsageType": VmwNsxTDataCenterDatapathResourceUsageType,
       "VmwNsxTDataCenterDHCPPoolUsageType": VmwNsxTDataCenterDHCPPoolUsageType,
       "VmwNsxTDataCenterEdgeServiceNameType": VmwNsxTDataCenterEdgeServiceNameType,
       "VmwNsxTDataCenterFailureReasonType": VmwNsxTDataCenterFailureReasonType,
       "VmwNsxTDataCenterPreviousGatewayStateType": VmwNsxTDataCenterPreviousGatewayStateType,
       "VmwNsxTDataCenterPreviousServiceStateType": VmwNsxTDataCenterPreviousServiceStateType,
       "VmwNsxTDataCenterSystemUsageThresholdType": VmwNsxTDataCenterSystemUsageThresholdType,
       "VmwNsxTDataCenterUsernameType": VmwNsxTDataCenterUsernameType,
       "VmwNsxTDataCenterDHCPServerIdType": VmwNsxTDataCenterDHCPServerIdType,
       "VmwNsxTDataCenterServiceNameType": VmwNsxTDataCenterServiceNameType,
       "VmwNsxTDataCenterIntelligenceNodeIdType": VmwNsxTDataCenterIntelligenceNodeIdType,
       "VmwNsxTDataCenterHostnameOrIPAddressWithPortType": VmwNsxTDataCenterHostnameOrIPAddressWithPortType,
       "VmwNsxTDataCenterEventIdType": VmwNsxTDataCenterEventIdType,
       "VmwNsxTDataCenterActiveGlobalManagerType": VmwNsxTDataCenterActiveGlobalManagerType,
       "VmwNsxTDataCenterActiveGlobalManagersType": VmwNsxTDataCenterActiveGlobalManagersType,
       "VmwNsxTDataCenterSessionDownReasonType": VmwNsxTDataCenterSessionDownReasonType,
       "VmwNsxTDataCenterManagerNodeNameType": VmwNsxTDataCenterManagerNodeNameType,
       "VmwNsxTDataCenterTransportNodeAddressType": VmwNsxTDataCenterTransportNodeAddressType,
       "VmwNsxTDataCenterTransportNodeNameType": VmwNsxTDataCenterTransportNodeNameType,
       "VmwNsxTDataCenterCentralControlPlaneIdType": VmwNsxTDataCenterCentralControlPlaneIdType,
       "VmwNsxTDataCenterTunnelDownReasonType": VmwNsxTDataCenterTunnelDownReasonType,
       "VmwNsxTDataCenterHeapTypeType": VmwNsxTDataCenterHeapTypeType,
       "VmwNsxTDataCenterMempoolNameType": VmwNsxTDataCenterMempoolNameType,
       "VmwNsxTDataCenterPasswordExpirationDaysType": VmwNsxTDataCenterPasswordExpirationDaysType,
       "VmwNsxTDataCenterBGPNeighborIPType": VmwNsxTDataCenterBGPNeighborIPType,
       "VmwNsxTDataCenterLDAPServerType": VmwNsxTDataCenterLDAPServerType,
       "VmwNsxTDataCenterPeerAddressType": VmwNsxTDataCenterPeerAddressType,
       "VmwNsxTDataCenterMaxIDSEventsAllowedType": VmwNsxTDataCenterMaxIDSEventsAllowedType,
       "VmwNsxTDataCenterStaticAddressType": VmwNsxTDataCenterStaticAddressType,
       "VmwNsxTDataCenterDuplicateIPAddressType": VmwNsxTDataCenterDuplicateIPAddressType,
       "VmwNsxTDataCenterCapacityDisplayNameType": VmwNsxTDataCenterCapacityDisplayNameType,
       "VmwNsxTDataCenterCapacityUsageCountType": VmwNsxTDataCenterCapacityUsageCountType,
       "VmwNsxTDataCenterEdgeNICNameType": VmwNsxTDataCenterEdgeNICNameType,
       "VmwNsxTDataCenterRxRingBufferOverflowPercentageType": VmwNsxTDataCenterRxRingBufferOverflowPercentageType,
       "VmwNsxTDataCenterTxRingBufferOverflowPercentageType": VmwNsxTDataCenterTxRingBufferOverflowPercentageType,
       "VmwNsxTDataCenterSrIdType": VmwNsxTDataCenterSrIdType,
       "VmwNsxTDataCenterIDSEventsCountType": VmwNsxTDataCenterIDSEventsCountType,
       "VmwNsxTDataCenterRemoteSiteNameType": VmwNsxTDataCenterRemoteSiteNameType,
       "VmwNsxTDataCenterBGPSourceIPType": VmwNsxTDataCenterBGPSourceIPType,
       "VmwNsxTDataCenterRemoteSiteIdType": VmwNsxTDataCenterRemoteSiteIdType,
       "VmwNsxTDataCenterSiteIdType": VmwNsxTDataCenterSiteIdType,
       "VmwNsxTDataCenterSiteNameType": VmwNsxTDataCenterSiteNameType,
       "VmwNsxTDataCenterLrIdType": VmwNsxTDataCenterLrIdType,
       "VmwNsxTDataCenterRxMissesType": VmwNsxTDataCenterRxMissesType,
       "VmwNsxTDataCenterRxProcessedType": VmwNsxTDataCenterRxProcessedType,
       "VmwNsxTDataCenterTxMissesType": VmwNsxTDataCenterTxMissesType,
       "VmwNsxTDataCenterTxProcessedType": VmwNsxTDataCenterTxProcessedType,
       "VmwNsxTDataCenterLrportIdType": VmwNsxTDataCenterLrportIdType,
       "VmwNsxTDataCenterServiceIPType": VmwNsxTDataCenterServiceIPType,
       "VmwNsxTDataCenterRemoteManagerNodeIdType": VmwNsxTDataCenterRemoteManagerNodeIdType,
       "VmwNsxTDataCenterDirectoryDomainType": VmwNsxTDataCenterDirectoryDomainType,
       "VmwNsxTDataCenterTimeoutInMinutesType": VmwNsxTDataCenterTimeoutInMinutesType,
       "VmwNsxTDataCenterMaxCapacityThresholdType": VmwNsxTDataCenterMaxCapacityThresholdType,
       "VmwNsxTDataCenterMinCapacityThresholdType": VmwNsxTDataCenterMinCapacityThresholdType,
       "VmwNsxTDataCenterMaxSupportedCapacityCountType": VmwNsxTDataCenterMaxSupportedCapacityCountType,
       "VmwNsxTDataCenterLatencySourceType": VmwNsxTDataCenterLatencySourceType,
       "VmwNsxTDataCenterLatencyThresholdType": VmwNsxTDataCenterLatencyThresholdType,
       "VmwNsxTDataCenterLatencyValueType": VmwNsxTDataCenterLatencyValueType,
       "VmwNsxTDataCenterApplianceFQDNType": VmwNsxTDataCenterApplianceFQDNType,
       "VmwNsxTDataCenterRemoteApplianceAddressType": VmwNsxTDataCenterRemoteApplianceAddressType,
       "VmwNsxTDataCenterManagerNodeIdType": VmwNsxTDataCenterManagerNodeIdType,
       "VmwNsxTDataCenterDisplayedLicenseKeyType": VmwNsxTDataCenterDisplayedLicenseKeyType,
       "VmwNsxTDataCenterEdgeThreadNameType": VmwNsxTDataCenterEdgeThreadNameType,
       "VmwNsxTDataCenterIntentPathType": VmwNsxTDataCenterIntentPathType,
       "vmwNSXsysMIB": vmwNSXsysMIB,
       "vmwNsxTDataCenterNotifications": vmwNsxTDataCenterNotifications,
       "vmwNsxTManagerHealthFeaturePrefix": vmwNsxTManagerHealthFeaturePrefix,
       "vmwNsxTManagerHealthFeature": vmwNsxTManagerHealthFeature,
       "vmwNsxTManagerHealthManagerCPUUsageHigh": vmwNsxTManagerHealthManagerCPUUsageHigh,
       "vmwNsxTManagerHealthManagerCPUUsageHighClear": vmwNsxTManagerHealthManagerCPUUsageHighClear,
       "vmwNsxTManagerHealthManagerCPUUsageVeryHigh": vmwNsxTManagerHealthManagerCPUUsageVeryHigh,
       "vmwNsxTManagerHealthManagerCPUUsageVeryHighClear": vmwNsxTManagerHealthManagerCPUUsageVeryHighClear,
       "vmwNsxTManagerHealthManagerMemoryUsageHigh": vmwNsxTManagerHealthManagerMemoryUsageHigh,
       "vmwNsxTManagerHealthManagerMemoryUsageHighClear": vmwNsxTManagerHealthManagerMemoryUsageHighClear,
       "vmwNsxTManagerHealthManagerMemoryUsageVeryHigh": vmwNsxTManagerHealthManagerMemoryUsageVeryHigh,
       "vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear": vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear,
       "vmwNsxTManagerHealthManagerDiskUsageHigh": vmwNsxTManagerHealthManagerDiskUsageHigh,
       "vmwNsxTManagerHealthManagerDiskUsageHighClear": vmwNsxTManagerHealthManagerDiskUsageHighClear,
       "vmwNsxTManagerHealthManagerDiskUsageVeryHigh": vmwNsxTManagerHealthManagerDiskUsageVeryHigh,
       "vmwNsxTManagerHealthManagerDiskUsageVeryHighClear": vmwNsxTManagerHealthManagerDiskUsageVeryHighClear,
       "vmwNsxTManagerHealthManagerConfigDiskUsageHigh": vmwNsxTManagerHealthManagerConfigDiskUsageHigh,
       "vmwNsxTManagerHealthManagerConfigDiskUsageHighClear": vmwNsxTManagerHealthManagerConfigDiskUsageHighClear,
       "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh": vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh,
       "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear": vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear,
       "vmwNsxTManagerHealthDuplicateIPAddress": vmwNsxTManagerHealthDuplicateIPAddress,
       "vmwNsxTManagerHealthDuplicateIPAddressClear": vmwNsxTManagerHealthDuplicateIPAddressClear,
       "vmwNsxTManagerHealthOperationsDbDiskUsageHigh": vmwNsxTManagerHealthOperationsDbDiskUsageHigh,
       "vmwNsxTManagerHealthOperationsDbDiskUsageHighClear": vmwNsxTManagerHealthOperationsDbDiskUsageHighClear,
       "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh": vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh,
       "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear": vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear,
       "vmwNsxTManagerHealthStorageError": vmwNsxTManagerHealthStorageError,
       "vmwNsxTManagerHealthStorageErrorClear": vmwNsxTManagerHealthStorageErrorClear,
       "vmwNsxTEdgeHealthFeaturePrefix": vmwNsxTEdgeHealthFeaturePrefix,
       "vmwNsxTEdgeHealthFeature": vmwNsxTEdgeHealthFeature,
       "vmwNsxTEdgeHealthEdgeCPUUsageHigh": vmwNsxTEdgeHealthEdgeCPUUsageHigh,
       "vmwNsxTEdgeHealthEdgeCPUUsageHighClear": vmwNsxTEdgeHealthEdgeCPUUsageHighClear,
       "vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh": vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh,
       "vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear": vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear,
       "vmwNsxTEdgeHealthEdgeMemoryUsageHigh": vmwNsxTEdgeHealthEdgeMemoryUsageHigh,
       "vmwNsxTEdgeHealthEdgeMemoryUsageHighClear": vmwNsxTEdgeHealthEdgeMemoryUsageHighClear,
       "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh": vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh,
       "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear": vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear,
       "vmwNsxTEdgeHealthEdgeDiskUsageHigh": vmwNsxTEdgeHealthEdgeDiskUsageHigh,
       "vmwNsxTEdgeHealthEdgeDiskUsageHighClear": vmwNsxTEdgeHealthEdgeDiskUsageHighClear,
       "vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh": vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh,
       "vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear": vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear,
       "vmwNsxTEdgeHealthEdgeDatapathCPUHigh": vmwNsxTEdgeHealthEdgeDatapathCPUHigh,
       "vmwNsxTEdgeHealthEdgeDatapathCPUHighClear": vmwNsxTEdgeHealthEdgeDatapathCPUHighClear,
       "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh": vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh,
       "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear": vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear,
       "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure": vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure,
       "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear": vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear,
       "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown": vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown,
       "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear": vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear,
       "vmwNsxTEdgeHealthEdgeDatapathMempoolHigh": vmwNsxTEdgeHealthEdgeDatapathMempoolHigh,
       "vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear": vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear,
       "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh": vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh,
       "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear": vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear,
       "vmwNsxTEdgeHealthEdgeNICLinkStatusDown": vmwNsxTEdgeHealthEdgeNICLinkStatusDown,
       "vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear": vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear,
       "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer": vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer,
       "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear": vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear,
       "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer": vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer,
       "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear": vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear,
       "vmwNsxTEdgeHealthStorageError": vmwNsxTEdgeHealthStorageError,
       "vmwNsxTEdgeHealthStorageErrorClear": vmwNsxTEdgeHealthStorageErrorClear,
       "vmwNsxTEdgeHealthDatapathThreadDeadlocked": vmwNsxTEdgeHealthDatapathThreadDeadlocked,
       "vmwNsxTEdgeHealthDatapathThreadDeadlockedClear": vmwNsxTEdgeHealthDatapathThreadDeadlockedClear,
       "vmwNsxTCertificatesFeaturePrefix": vmwNsxTCertificatesFeaturePrefix,
       "vmwNsxTCertificatesFeature": vmwNsxTCertificatesFeature,
       "vmwNsxTCertificatesCertificateExpirationApproaching": vmwNsxTCertificatesCertificateExpirationApproaching,
       "vmwNsxTCertificatesCertificateExpirationApproachingClear": vmwNsxTCertificatesCertificateExpirationApproachingClear,
       "vmwNsxTCertificatesCertificateExpired": vmwNsxTCertificatesCertificateExpired,
       "vmwNsxTCertificatesCertificateExpiredClear": vmwNsxTCertificatesCertificateExpiredClear,
       "vmwNsxTCertificatesCertificateIsAboutToExpire": vmwNsxTCertificatesCertificateIsAboutToExpire,
       "vmwNsxTCertificatesCertificateIsAboutToExpireClear": vmwNsxTCertificatesCertificateIsAboutToExpireClear,
       "vmwNsxTPasswordManagementFeaturePrefix": vmwNsxTPasswordManagementFeaturePrefix,
       "vmwNsxTPasswordManagementFeature": vmwNsxTPasswordManagementFeature,
       "vmwNsxTPasswordManagementPasswordExpirationApproaching": vmwNsxTPasswordManagementPasswordExpirationApproaching,
       "vmwNsxTPasswordManagementPasswordExpirationApproachingClear": vmwNsxTPasswordManagementPasswordExpirationApproachingClear,
       "vmwNsxTPasswordManagementPasswordExpired": vmwNsxTPasswordManagementPasswordExpired,
       "vmwNsxTPasswordManagementPasswordExpiredClear": vmwNsxTPasswordManagementPasswordExpiredClear,
       "vmwNsxTPasswordManagementPasswordIsAboutToExpire": vmwNsxTPasswordManagementPasswordIsAboutToExpire,
       "vmwNsxTPasswordManagementPasswordIsAboutToExpireClear": vmwNsxTPasswordManagementPasswordIsAboutToExpireClear,
       "vmwNsxTLicensesFeaturePrefix": vmwNsxTLicensesFeaturePrefix,
       "vmwNsxTLicensesFeature": vmwNsxTLicensesFeature,
       "vmwNsxTLicensesLicenseExpired": vmwNsxTLicensesLicenseExpired,
       "vmwNsxTLicensesLicenseExpiredClear": vmwNsxTLicensesLicenseExpiredClear,
       "vmwNsxTLicensesLicenseIsAboutToExpire": vmwNsxTLicensesLicenseIsAboutToExpire,
       "vmwNsxTLicensesLicenseIsAboutToExpireClear": vmwNsxTLicensesLicenseIsAboutToExpireClear,
       "vmwNsxTIntelligenceHealthFeaturePrefix": vmwNsxTIntelligenceHealthFeaturePrefix,
       "vmwNsxTIntelligenceHealthFeature": vmwNsxTIntelligenceHealthFeature,
       "vmwNsxTIntelligenceHealthCPUUsageHigh": vmwNsxTIntelligenceHealthCPUUsageHigh,
       "vmwNsxTIntelligenceHealthCPUUsageHighClear": vmwNsxTIntelligenceHealthCPUUsageHighClear,
       "vmwNsxTIntelligenceHealthCPUUsageVeryHigh": vmwNsxTIntelligenceHealthCPUUsageVeryHigh,
       "vmwNsxTIntelligenceHealthCPUUsageVeryHighClear": vmwNsxTIntelligenceHealthCPUUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh": vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear": vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh": vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear": vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthDiskUsageHigh": vmwNsxTIntelligenceHealthDiskUsageHigh,
       "vmwNsxTIntelligenceHealthDiskUsageHighClear": vmwNsxTIntelligenceHealthDiskUsageHighClear,
       "vmwNsxTIntelligenceHealthDiskUsageVeryHigh": vmwNsxTIntelligenceHealthDiskUsageVeryHigh,
       "vmwNsxTIntelligenceHealthDiskUsageVeryHighClear": vmwNsxTIntelligenceHealthDiskUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthMemoryUsageHigh": vmwNsxTIntelligenceHealthMemoryUsageHigh,
       "vmwNsxTIntelligenceHealthMemoryUsageHighClear": vmwNsxTIntelligenceHealthMemoryUsageHighClear,
       "vmwNsxTIntelligenceHealthMemoryUsageVeryHigh": vmwNsxTIntelligenceHealthMemoryUsageVeryHigh,
       "vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear": vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthNodeStatusDegraded": vmwNsxTIntelligenceHealthNodeStatusDegraded,
       "vmwNsxTIntelligenceHealthNodeStatusDegradedClear": vmwNsxTIntelligenceHealthNodeStatusDegradedClear,
       "vmwNsxTIntelligenceHealthStorageLatencyHigh": vmwNsxTIntelligenceHealthStorageLatencyHigh,
       "vmwNsxTIntelligenceHealthStorageLatencyHighClear": vmwNsxTIntelligenceHealthStorageLatencyHighClear,
       "vmwNsxTInfrastructureCommunicationFeaturePrefix": vmwNsxTInfrastructureCommunicationFeaturePrefix,
       "vmwNsxTInfrastructureCommunicationFeature": vmwNsxTInfrastructureCommunicationFeature,
       "vmwNsxTInfrastructureCommunicationEdgeTunnelsDown": vmwNsxTInfrastructureCommunicationEdgeTunnelsDown,
       "vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear": vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear,
       "vmwNsxTIntelligenceCommunicationFeaturePrefix": vmwNsxTIntelligenceCommunicationFeaturePrefix,
       "vmwNsxTIntelligenceCommunicationFeature": vmwNsxTIntelligenceCommunicationFeature,
       "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected": vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected,
       "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear": vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear,
       "vmwNsxTCniHealthFeaturePrefix": vmwNsxTCniHealthFeaturePrefix,
       "vmwNsxTCniHealthFeature": vmwNsxTCniHealthFeature,
       "vmwNsxTCniHealthHyperbusManagerConnectionDown": vmwNsxTCniHealthHyperbusManagerConnectionDown,
       "vmwNsxTCniHealthHyperbusManagerConnectionDownClear": vmwNsxTCniHealthHyperbusManagerConnectionDownClear,
       "vmwNsxTNCPHealthFeaturePrefix": vmwNsxTNCPHealthFeaturePrefix,
       "vmwNsxTNCPHealthFeature": vmwNsxTNCPHealthFeature,
       "vmwNsxTNCPHealthNCPPluginDown": vmwNsxTNCPHealthNCPPluginDown,
       "vmwNsxTNCPHealthNCPPluginDownClear": vmwNsxTNCPHealthNCPPluginDownClear,
       "vmwNsxTNodeAgentsHealthFeaturePrefix": vmwNsxTNodeAgentsHealthFeaturePrefix,
       "vmwNsxTNodeAgentsHealthFeature": vmwNsxTNodeAgentsHealthFeature,
       "vmwNsxTNodeAgentsHealthNodeAgentsDown": vmwNsxTNodeAgentsHealthNodeAgentsDown,
       "vmwNsxTNodeAgentsHealthNodeAgentsDownClear": vmwNsxTNodeAgentsHealthNodeAgentsDownClear,
       "vmwNsxTEndpointProtectionFeaturePrefix": vmwNsxTEndpointProtectionFeaturePrefix,
       "vmwNsxTEndpointProtectionFeature": vmwNsxTEndpointProtectionFeature,
       "vmwNsxTEndpointProtectionEAMStatusDown": vmwNsxTEndpointProtectionEAMStatusDown,
       "vmwNsxTEndpointProtectionEAMStatusDownClear": vmwNsxTEndpointProtectionEAMStatusDownClear,
       "vmwNsxTEndpointProtectionPartnerChannelDown": vmwNsxTEndpointProtectionPartnerChannelDown,
       "vmwNsxTEndpointProtectionPartnerChannelDownClear": vmwNsxTEndpointProtectionPartnerChannelDownClear,
       "vmwNsxTVPNFeaturePrefix": vmwNsxTVPNFeaturePrefix,
       "vmwNsxTVPNFeature": vmwNsxTVPNFeature,
       "vmwNsxTVPNIPsecPolicyBasedSessionDown": vmwNsxTVPNIPsecPolicyBasedSessionDown,
       "vmwNsxTVPNIPsecPolicyBasedSessionDownClear": vmwNsxTVPNIPsecPolicyBasedSessionDownClear,
       "vmwNsxTVPNIPsecPolicyBasedTunnelDown": vmwNsxTVPNIPsecPolicyBasedTunnelDown,
       "vmwNsxTVPNIPsecPolicyBasedTunnelDownClear": vmwNsxTVPNIPsecPolicyBasedTunnelDownClear,
       "vmwNsxTVPNIPsecRouteBasedSessionDown": vmwNsxTVPNIPsecRouteBasedSessionDown,
       "vmwNsxTVPNIPsecRouteBasedSessionDownClear": vmwNsxTVPNIPsecRouteBasedSessionDownClear,
       "vmwNsxTVPNIPsecRouteBasedTunnelDown": vmwNsxTVPNIPsecRouteBasedTunnelDown,
       "vmwNsxTVPNIPsecRouteBasedTunnelDownClear": vmwNsxTVPNIPsecRouteBasedTunnelDownClear,
       "vmwNsxTVPNL2VpnSessionDown": vmwNsxTVPNL2VpnSessionDown,
       "vmwNsxTVPNL2VpnSessionDownClear": vmwNsxTVPNL2VpnSessionDownClear,
       "vmwNsxTAlarmManagementFeaturePrefix": vmwNsxTAlarmManagementFeaturePrefix,
       "vmwNsxTAlarmManagementFeature": vmwNsxTAlarmManagementFeature,
       "vmwNsxTAlarmManagementAlarmServiceOverloaded": vmwNsxTAlarmManagementAlarmServiceOverloaded,
       "vmwNsxTAlarmManagementAlarmServiceOverloadedClear": vmwNsxTAlarmManagementAlarmServiceOverloadedClear,
       "vmwNsxTAlarmManagementHeavyVolumeOfAlarms": vmwNsxTAlarmManagementHeavyVolumeOfAlarms,
       "vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear": vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear,
       "vmwNsxTLoadBalancerFeaturePrefix": vmwNsxTLoadBalancerFeaturePrefix,
       "vmwNsxTLoadBalancerFeature": vmwNsxTLoadBalancerFeature,
       "vmwNsxTLoadBalancerLBCPUVeryHigh": vmwNsxTLoadBalancerLBCPUVeryHigh,
       "vmwNsxTLoadBalancerLBCPUVeryHighClear": vmwNsxTLoadBalancerLBCPUVeryHighClear,
       "vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh": vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh,
       "vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear": vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear,
       "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh": vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh,
       "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear": vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear,
       "vmwNsxTLoadBalancerLBStatusDown": vmwNsxTLoadBalancerLBStatusDown,
       "vmwNsxTLoadBalancerLBStatusDownClear": vmwNsxTLoadBalancerLBStatusDownClear,
       "vmwNsxTLoadBalancerPoolStatusDown": vmwNsxTLoadBalancerPoolStatusDown,
       "vmwNsxTLoadBalancerPoolStatusDownClear": vmwNsxTLoadBalancerPoolStatusDownClear,
       "vmwNsxTLoadBalancerVirtualServerStatusDown": vmwNsxTLoadBalancerVirtualServerStatusDown,
       "vmwNsxTLoadBalancerVirtualServerStatusDownClear": vmwNsxTLoadBalancerVirtualServerStatusDownClear,
       "vmwNsxTLoadBalancerLBStatusDegraded": vmwNsxTLoadBalancerLBStatusDegraded,
       "vmwNsxTLoadBalancerLBStatusDegradedClear": vmwNsxTLoadBalancerLBStatusDegradedClear,
       "vmwNsxTLoadBalancerDLBStatusDown": vmwNsxTLoadBalancerDLBStatusDown,
       "vmwNsxTLoadBalancerDLBStatusDownClear": vmwNsxTLoadBalancerDLBStatusDownClear,
       "vmwNsxTTransportNodeHealthFeaturePrefix": vmwNsxTTransportNodeHealthFeaturePrefix,
       "vmwNsxTTransportNodeHealthFeature": vmwNsxTTransportNodeHealthFeature,
       "vmwNsxTTransportNodeHealthNVDSUplinkDown": vmwNsxTTransportNodeHealthNVDSUplinkDown,
       "vmwNsxTTransportNodeHealthNVDSUplinkDownClear": vmwNsxTTransportNodeHealthNVDSUplinkDownClear,
       "vmwNsxTTransportNodeHealthLAGMemberDown": vmwNsxTTransportNodeHealthLAGMemberDown,
       "vmwNsxTTransportNodeHealthLAGMemberDownClear": vmwNsxTTransportNodeHealthLAGMemberDownClear,
       "vmwNsxTInfrastructureServiceFeaturePrefix": vmwNsxTInfrastructureServiceFeaturePrefix,
       "vmwNsxTInfrastructureServiceFeature": vmwNsxTInfrastructureServiceFeature,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusChanged": vmwNsxTInfrastructureServiceEdgeServiceStatusChanged,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear": vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusDown": vmwNsxTInfrastructureServiceEdgeServiceStatusDown,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear": vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear,
       "vmwNsxTInfrastructureServiceServiceStatusUnknown": vmwNsxTInfrastructureServiceServiceStatusUnknown,
       "vmwNsxTInfrastructureServiceServiceStatusUnknownClear": vmwNsxTInfrastructureServiceServiceStatusUnknownClear,
       "vmwNsxTDHCPFeaturePrefix": vmwNsxTDHCPFeaturePrefix,
       "vmwNsxTDHCPFeature": vmwNsxTDHCPFeature,
       "vmwNsxTDHCPPoolLeaseAllocationFailed": vmwNsxTDHCPPoolLeaseAllocationFailed,
       "vmwNsxTDHCPPoolLeaseAllocationFailedClear": vmwNsxTDHCPPoolLeaseAllocationFailedClear,
       "vmwNsxTDHCPPoolOverloaded": vmwNsxTDHCPPoolOverloaded,
       "vmwNsxTDHCPPoolOverloadedClear": vmwNsxTDHCPPoolOverloadedClear,
       "vmwNsxTHighAvailabilityFeaturePrefix": vmwNsxTHighAvailabilityFeaturePrefix,
       "vmwNsxTHighAvailabilityFeature": vmwNsxTHighAvailabilityFeature,
       "vmwNsxTHighAvailabilityTier0GatewayFailover": vmwNsxTHighAvailabilityTier0GatewayFailover,
       "vmwNsxTHighAvailabilityTier0GatewayFailoverClear": vmwNsxTHighAvailabilityTier0GatewayFailoverClear,
       "vmwNsxTHighAvailabilityTier1GatewayFailover": vmwNsxTHighAvailabilityTier1GatewayFailover,
       "vmwNsxTHighAvailabilityTier1GatewayFailoverClear": vmwNsxTHighAvailabilityTier1GatewayFailoverClear,
       "vmwNsxTCapacityFeaturePrefix": vmwNsxTCapacityFeaturePrefix,
       "vmwNsxTCapacityFeature": vmwNsxTCapacityFeature,
       "vmwNsxTCapacityMaximumCapacity": vmwNsxTCapacityMaximumCapacity,
       "vmwNsxTCapacityMaximumCapacityClear": vmwNsxTCapacityMaximumCapacityClear,
       "vmwNsxTCapacityMaximumCapacityThreshold": vmwNsxTCapacityMaximumCapacityThreshold,
       "vmwNsxTCapacityMaximumCapacityThresholdClear": vmwNsxTCapacityMaximumCapacityThresholdClear,
       "vmwNsxTCapacityMinimumCapacityThreshold": vmwNsxTCapacityMinimumCapacityThreshold,
       "vmwNsxTCapacityMinimumCapacityThresholdClear": vmwNsxTCapacityMinimumCapacityThresholdClear,
       "vmwNsxTAuditLogHealthFeaturePrefix": vmwNsxTAuditLogHealthFeaturePrefix,
       "vmwNsxTAuditLogHealthFeature": vmwNsxTAuditLogHealthFeature,
       "vmwNsxTAuditLogHealthAuditLogFileUpdateError": vmwNsxTAuditLogHealthAuditLogFileUpdateError,
       "vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear": vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear,
       "vmwNsxTAuditLogHealthRemoteLoggingServerError": vmwNsxTAuditLogHealthRemoteLoggingServerError,
       "vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear": vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear,
       "vmwNsxTRoutingFeaturePrefix": vmwNsxTRoutingFeaturePrefix,
       "vmwNsxTRoutingFeature": vmwNsxTRoutingFeature,
       "vmwNsxTRoutingBGPDown": vmwNsxTRoutingBGPDown,
       "vmwNsxTRoutingBGPDownClear": vmwNsxTRoutingBGPDownClear,
       "vmwNsxTRoutingStaticRoutingRemoved": vmwNsxTRoutingStaticRoutingRemoved,
       "vmwNsxTRoutingStaticRoutingRemovedClear": vmwNsxTRoutingStaticRoutingRemovedClear,
       "vmwNsxTRoutingBFDDownOnExternalInterface": vmwNsxTRoutingBFDDownOnExternalInterface,
       "vmwNsxTRoutingBFDDownOnExternalInterfaceClear": vmwNsxTRoutingBFDDownOnExternalInterfaceClear,
       "vmwNsxTRoutingRoutingDown": vmwNsxTRoutingRoutingDown,
       "vmwNsxTRoutingRoutingDownClear": vmwNsxTRoutingRoutingDownClear,
       "vmwNsxTRoutingOSPFNeighborWentDown": vmwNsxTRoutingOSPFNeighborWentDown,
       "vmwNsxTRoutingOSPFNeighborWentDownClear": vmwNsxTRoutingOSPFNeighborWentDownClear,
       "vmwNsxTRoutingProxyARPNotConfiguredForServiceIP": vmwNsxTRoutingProxyARPNotConfiguredForServiceIP,
       "vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear": vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear,
       "vmwNsxTDNSFeaturePrefix": vmwNsxTDNSFeaturePrefix,
       "vmwNsxTDNSFeature": vmwNsxTDNSFeature,
       "vmwNsxTDNSForwarderDisabled": vmwNsxTDNSForwarderDisabled,
       "vmwNsxTDNSForwarderDisabledClear": vmwNsxTDNSForwarderDisabledClear,
       "vmwNsxTDNSForwarderDown": vmwNsxTDNSForwarderDown,
       "vmwNsxTDNSForwarderDownClear": vmwNsxTDNSForwarderDownClear,
       "vmwNsxTDistributedFirewallFeaturePrefix": vmwNsxTDistributedFirewallFeaturePrefix,
       "vmwNsxTDistributedFirewallFeature": vmwNsxTDistributedFirewallFeature,
       "vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh": vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh,
       "vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear": vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear,
       "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh": vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh,
       "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear": vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear,
       "vmwNsxTFederationFeaturePrefix": vmwNsxTFederationFeaturePrefix,
       "vmwNsxTFederationFeature": vmwNsxTFederationFeature,
       "vmwNsxTFederationRtepBGPDown": vmwNsxTFederationRtepBGPDown,
       "vmwNsxTFederationRtepBGPDownClear": vmwNsxTFederationRtepBGPDownClear,
       "vmwNsxTFederationLmToLmSynchronizationError": vmwNsxTFederationLmToLmSynchronizationError,
       "vmwNsxTFederationLmToLmSynchronizationErrorClear": vmwNsxTFederationLmToLmSynchronizationErrorClear,
       "vmwNsxTFederationLmToLmSynchronizationWarning": vmwNsxTFederationLmToLmSynchronizationWarning,
       "vmwNsxTFederationLmToLmSynchronizationWarningClear": vmwNsxTFederationLmToLmSynchronizationWarningClear,
       "vmwNsxTFederationRtepConnectivityLost": vmwNsxTFederationRtepConnectivityLost,
       "vmwNsxTFederationRtepConnectivityLostClear": vmwNsxTFederationRtepConnectivityLostClear,
       "vmwNsxTFederationGMToGMSplitBrain": vmwNsxTFederationGMToGMSplitBrain,
       "vmwNsxTFederationGMToGMSplitBrainClear": vmwNsxTFederationGMToGMSplitBrainClear,
       "vmwNsxTDistributedIDSIPSFeaturePrefix": vmwNsxTDistributedIDSIPSFeaturePrefix,
       "vmwNsxTDistributedIDSIPSFeature": vmwNsxTDistributedIDSIPSFeature,
       "vmwNsxTDistributedIDSIPSMaxEventsReached": vmwNsxTDistributedIDSIPSMaxEventsReached,
       "vmwNsxTDistributedIDSIPSMaxEventsReachedClear": vmwNsxTDistributedIDSIPSMaxEventsReachedClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineDown": vmwNsxTDistributedIDSIPSNSXIDPSEngineDown,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear,
       "vmwNsxTCommunicationFeaturePrefix": vmwNsxTCommunicationFeaturePrefix,
       "vmwNsxTCommunicationFeature": vmwNsxTCommunicationFeature,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDown": vmwNsxTCommunicationManagementChannelToTransportNodeDown,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDownClear": vmwNsxTCommunicationManagementChannelToTransportNodeDownClear,
       "vmwNsxTCommunicationManagerControlChannelDown": vmwNsxTCommunicationManagerControlChannelDown,
       "vmwNsxTCommunicationManagerControlChannelDownClear": vmwNsxTCommunicationManagerControlChannelDownClear,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDownLg": vmwNsxTCommunicationManagementChannelToTransportNodeDownLg,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear": vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear,
       "vmwNsxTCommunicationControlChannelToManagerNodeDown": vmwNsxTCommunicationControlChannelToManagerNodeDown,
       "vmwNsxTCommunicationControlChannelToManagerNodeDownClear": vmwNsxTCommunicationControlChannelToManagerNodeDownClear,
       "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong": vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong,
       "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear": vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear,
       "vmwNsxTCommunicationControlChannelToTransportNodeDown": vmwNsxTCommunicationControlChannelToTransportNodeDown,
       "vmwNsxTCommunicationControlChannelToTransportNodeDownClear": vmwNsxTCommunicationControlChannelToTransportNodeDownClear,
       "vmwNsxTCommunicationManagerClusterLatencyHigh": vmwNsxTCommunicationManagerClusterLatencyHigh,
       "vmwNsxTCommunicationManagerClusterLatencyHighClear": vmwNsxTCommunicationManagerClusterLatencyHighClear,
       "vmwNsxTCommunicationControlChannelToTransportNodeDownLong": vmwNsxTCommunicationControlChannelToTransportNodeDownLong,
       "vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear": vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear,
       "vmwNsxTCommunicationManagerFQDNLookupFailure": vmwNsxTCommunicationManagerFQDNLookupFailure,
       "vmwNsxTCommunicationManagerFQDNLookupFailureClear": vmwNsxTCommunicationManagerFQDNLookupFailureClear,
       "vmwNsxTCommunicationManagerFQDNReverseLookupFailure": vmwNsxTCommunicationManagerFQDNReverseLookupFailure,
       "vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear": vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear,
       "vmwNsxTIdentityFirewallFeaturePrefix": vmwNsxTIdentityFirewallFeaturePrefix,
       "vmwNsxTIdentityFirewallFeature": vmwNsxTIdentityFirewallFeature,
       "vmwNsxTIdentityFirewallConnectivityToLDAPServerLost": vmwNsxTIdentityFirewallConnectivityToLDAPServerLost,
       "vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear": vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear,
       "vmwNsxTIdentityFirewallErrorInDeltaSync": vmwNsxTIdentityFirewallErrorInDeltaSync,
       "vmwNsxTIdentityFirewallErrorInDeltaSyncClear": vmwNsxTIdentityFirewallErrorInDeltaSyncClear,
       "vmwNsxTIPAMFeaturePrefix": vmwNsxTIPAMFeaturePrefix,
       "vmwNsxTIPAMFeature": vmwNsxTIPAMFeature,
       "vmwNsxTIPAMIPBlockUsageVeryHigh": vmwNsxTIPAMIPBlockUsageVeryHigh,
       "vmwNsxTIPAMIPBlockUsageVeryHighClear": vmwNsxTIPAMIPBlockUsageVeryHighClear,
       "vmwNsxTIPAMIPPoolUsageVeryHigh": vmwNsxTIPAMIPPoolUsageVeryHigh,
       "vmwNsxTIPAMIPPoolUsageVeryHighClear": vmwNsxTIPAMIPPoolUsageVeryHighClear,
       "vmwNsxTDataCenterData": vmwNsxTDataCenterData,
       "vmwNsxTDataCenterTimestamp": vmwNsxTDataCenterTimestamp,
       "vmwNsxTDataCenterFeatureName": vmwNsxTDataCenterFeatureName,
       "vmwNsxTDataCenterEventType": vmwNsxTDataCenterEventType,
       "vmwNsxTDataCenterEventSeverity": vmwNsxTDataCenterEventSeverity,
       "vmwNsxTDataCenterNodeId": vmwNsxTDataCenterNodeId,
       "vmwNsxTDataCenterNodeType": vmwNsxTDataCenterNodeType,
       "vmwNsxTDataCenterEntityId": vmwNsxTDataCenterEntityId,
       "vmwNsxTDataCenterSystemResourceUsage": vmwNsxTDataCenterSystemResourceUsage,
       "vmwNsxTDataCenterDiskPartitionName": vmwNsxTDataCenterDiskPartitionName,
       "vmwNsxTDataCenterLicenseEditionType": vmwNsxTDataCenterLicenseEditionType,
       "vmwNsxTDataCenterApplianceAddress": vmwNsxTDataCenterApplianceAddress,
       "vmwNsxTDataCenterCurrentGatewayState": vmwNsxTDataCenterCurrentGatewayState,
       "vmwNsxTDataCenterCurrentServiceState": vmwNsxTDataCenterCurrentServiceState,
       "vmwNsxTDataCenterDatapathResourceUsage": vmwNsxTDataCenterDatapathResourceUsage,
       "vmwNsxTDataCenterDHCPPoolUsage": vmwNsxTDataCenterDHCPPoolUsage,
       "vmwNsxTDataCenterEdgeServiceName": vmwNsxTDataCenterEdgeServiceName,
       "vmwNsxTDataCenterFailureReason": vmwNsxTDataCenterFailureReason,
       "vmwNsxTDataCenterPreviousGatewayState": vmwNsxTDataCenterPreviousGatewayState,
       "vmwNsxTDataCenterPreviousServiceState": vmwNsxTDataCenterPreviousServiceState,
       "vmwNsxTDataCenterSystemUsageThreshold": vmwNsxTDataCenterSystemUsageThreshold,
       "vmwNsxTDataCenterUsername": vmwNsxTDataCenterUsername,
       "vmwNsxTDataCenterDHCPServerId": vmwNsxTDataCenterDHCPServerId,
       "vmwNsxTDataCenterServiceName": vmwNsxTDataCenterServiceName,
       "vmwNsxTDataCenterIntelligenceNodeId": vmwNsxTDataCenterIntelligenceNodeId,
       "vmwNsxTDataCenterHostnameOrIPAddressWithPort": vmwNsxTDataCenterHostnameOrIPAddressWithPort,
       "vmwNsxTDataCenterEventId": vmwNsxTDataCenterEventId,
       "vmwNsxTDataCenterActiveGlobalManager": vmwNsxTDataCenterActiveGlobalManager,
       "vmwNsxTDataCenterActiveGlobalManagers": vmwNsxTDataCenterActiveGlobalManagers,
       "vmwNsxTDataCenterSessionDownReason": vmwNsxTDataCenterSessionDownReason,
       "vmwNsxTDataCenterManagerNodeName": vmwNsxTDataCenterManagerNodeName,
       "vmwNsxTDataCenterTransportNodeAddress": vmwNsxTDataCenterTransportNodeAddress,
       "vmwNsxTDataCenterTransportNodeName": vmwNsxTDataCenterTransportNodeName,
       "vmwNsxTDataCenterCentralControlPlaneId": vmwNsxTDataCenterCentralControlPlaneId,
       "vmwNsxTDataCenterTunnelDownReason": vmwNsxTDataCenterTunnelDownReason,
       "vmwNsxTDataCenterHeapType": vmwNsxTDataCenterHeapType,
       "vmwNsxTDataCenterMempoolName": vmwNsxTDataCenterMempoolName,
       "vmwNsxTDataCenterPasswordExpirationDays": vmwNsxTDataCenterPasswordExpirationDays,
       "vmwNsxTDataCenterBGPNeighborIP": vmwNsxTDataCenterBGPNeighborIP,
       "vmwNsxTDataCenterLDAPServer": vmwNsxTDataCenterLDAPServer,
       "vmwNsxTDataCenterPeerAddress": vmwNsxTDataCenterPeerAddress,
       "vmwNsxTDataCenterMaxIDSEventsAllowed": vmwNsxTDataCenterMaxIDSEventsAllowed,
       "vmwNsxTDataCenterStaticAddress": vmwNsxTDataCenterStaticAddress,
       "vmwNsxTDataCenterDuplicateIPAddress": vmwNsxTDataCenterDuplicateIPAddress,
       "vmwNsxTDataCenterCapacityDisplayName": vmwNsxTDataCenterCapacityDisplayName,
       "vmwNsxTDataCenterCapacityUsageCount": vmwNsxTDataCenterCapacityUsageCount,
       "vmwNsxTDataCenterEdgeNICName": vmwNsxTDataCenterEdgeNICName,
       "vmwNsxTDataCenterRxRingBufferOverflowPercentage": vmwNsxTDataCenterRxRingBufferOverflowPercentage,
       "vmwNsxTDataCenterTxRingBufferOverflowPercentage": vmwNsxTDataCenterTxRingBufferOverflowPercentage,
       "vmwNsxTDataCenterSrId": vmwNsxTDataCenterSrId,
       "vmwNsxTDataCenterIDSEventsCount": vmwNsxTDataCenterIDSEventsCount,
       "vmwNsxTDataCenterRemoteSiteName": vmwNsxTDataCenterRemoteSiteName,
       "vmwNsxTDataCenterBGPSourceIP": vmwNsxTDataCenterBGPSourceIP,
       "vmwNsxTDataCenterRemoteSiteId": vmwNsxTDataCenterRemoteSiteId,
       "vmwNsxTDataCenterSiteId": vmwNsxTDataCenterSiteId,
       "vmwNsxTDataCenterSiteName": vmwNsxTDataCenterSiteName,
       "vmwNsxTDataCenterLrId": vmwNsxTDataCenterLrId,
       "vmwNsxTDataCenterRxMisses": vmwNsxTDataCenterRxMisses,
       "vmwNsxTDataCenterRxProcessed": vmwNsxTDataCenterRxProcessed,
       "vmwNsxTDataCenterTxMisses": vmwNsxTDataCenterTxMisses,
       "vmwNsxTDataCenterTxProcessed": vmwNsxTDataCenterTxProcessed,
       "vmwNsxTDataCenterLrportId": vmwNsxTDataCenterLrportId,
       "vmwNsxTDataCenterServiceIP": vmwNsxTDataCenterServiceIP,
       "vmwNsxTDataCenterRemoteManagerNodeId": vmwNsxTDataCenterRemoteManagerNodeId,
       "vmwNsxTDataCenterDirectoryDomain": vmwNsxTDataCenterDirectoryDomain,
       "vmwNsxTDataCenterTimeoutInMinutes": vmwNsxTDataCenterTimeoutInMinutes,
       "vmwNsxTDataCenterMaxCapacityThreshold": vmwNsxTDataCenterMaxCapacityThreshold,
       "vmwNsxTDataCenterMinCapacityThreshold": vmwNsxTDataCenterMinCapacityThreshold,
       "vmwNsxTDataCenterMaxSupportedCapacityCount": vmwNsxTDataCenterMaxSupportedCapacityCount,
       "vmwNsxTDataCenterLatencySource": vmwNsxTDataCenterLatencySource,
       "vmwNsxTDataCenterLatencyThreshold": vmwNsxTDataCenterLatencyThreshold,
       "vmwNsxTDataCenterLatencyValue": vmwNsxTDataCenterLatencyValue,
       "vmwNsxTDataCenterApplianceFQDN": vmwNsxTDataCenterApplianceFQDN,
       "vmwNsxTDataCenterRemoteApplianceAddress": vmwNsxTDataCenterRemoteApplianceAddress,
       "vmwNsxTDataCenterManagerNodeId": vmwNsxTDataCenterManagerNodeId,
       "vmwNsxTDataCenterDisplayedLicenseKey": vmwNsxTDataCenterDisplayedLicenseKey,
       "vmwNsxTDataCenterEdgeThreadName": vmwNsxTDataCenterEdgeThreadName,
       "vmwNsxTDataCenterIntentPath": vmwNsxTDataCenterIntentPath,
       "vmwNsxTDataCenterConformance": vmwNsxTDataCenterConformance,
       "vmwNsxTDataCenterCompliances": vmwNsxTDataCenterCompliances,
       "vmwNsxTDataCenterBasicCompliance": vmwNsxTDataCenterBasicCompliance,
       "vmwNsxTDataCenterBasicCompliance2": vmwNsxTDataCenterBasicCompliance2,
       "vmwNsxTDataCenterBasicCompliance3": vmwNsxTDataCenterBasicCompliance3,
       "vmwNsxTDataCenterBasicCompliance4": vmwNsxTDataCenterBasicCompliance4,
       "vmwNsxTDataCenterBasicCompliance5": vmwNsxTDataCenterBasicCompliance5,
       "vmwNsxTDataCenterBasicCompliance6": vmwNsxTDataCenterBasicCompliance6,
       "vmwNsxTDataCenterBasicCompliance7": vmwNsxTDataCenterBasicCompliance7,
       "vmwNsxTDataCenterSMIBGroups": vmwNsxTDataCenterSMIBGroups,
       "vmwNsxTDataCenterNotificationInfoGroup": vmwNsxTDataCenterNotificationInfoGroup,
       "vmwNsxTDataCenterNotificationGroup": vmwNsxTDataCenterNotificationGroup,
       "vmwNsxTDataCenterNotificationInfoGroup2": vmwNsxTDataCenterNotificationInfoGroup2,
       "vmwNsxTDataCenterNotificationGroup2": vmwNsxTDataCenterNotificationGroup2,
       "vmwNsxTDataCenterNotificationInfoGroup3": vmwNsxTDataCenterNotificationInfoGroup3,
       "vmwNsxTDataCenterNotificationGroup3": vmwNsxTDataCenterNotificationGroup3,
       "vmwNsxTDataCenterNotificationInfoGroup4": vmwNsxTDataCenterNotificationInfoGroup4,
       "vmwNsxTDataCenterNotificationGroup4": vmwNsxTDataCenterNotificationGroup4,
       "vmwNsxTDataCenterNotificationGroup5": vmwNsxTDataCenterNotificationGroup5,
       "vmwNsxTDataCenterNotificationInfoGroup6": vmwNsxTDataCenterNotificationInfoGroup6,
       "vmwNsxTDataCenterNotificationGroup6": vmwNsxTDataCenterNotificationGroup6,
       "vmwNsxTDataCenterNotificationInfoGroup7": vmwNsxTDataCenterNotificationInfoGroup7,
       "vmwNsxTDataCenterNotificationGroup7": vmwNsxTDataCenterNotificationGroup7}
)
