# SNMP MIB module (NITROSECURITY-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nitrosecurity_23128/NITROSECURITY-BASE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:45:52 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nitroRegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23128)
)
if mibBuilder.loadTexts:
    nitroRegMIB.setRevisions(
        ("2011-03-28 00:00",
         "2010-11-08 00:00",
         "2010-11-01 00:00",
         "2008-11-24 00:00",
         "2008-02-05 00:00",
         "2006-08-29 17:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BlacklistActions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("remove", 1))
    )



class BlacklistTypes(TextualConvention, Integer32):
    status = "current"
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
        *(("blacklist", 1),
          ("whitelist", 2),
          ("destinationBlacklist", 3),
          ("quarantine1", 4),
          ("quarantine2", 5),
          ("quarantine3", 6))
    )



# MIB Managed Objects in the order of their OIDs

_NitroEvents_ObjectIdentity = ObjectIdentity
nitroEvents = _NitroEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 0)
)
_NitroObjects_ObjectIdentity = ObjectIdentity
nitroObjects = _NitroObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 1)
)
_Health_ObjectIdentity = ObjectIdentity
health = _Health_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3)
)
if mibBuilder.loadTexts:
    health.setStatus("current")
_HealthESM_ObjectIdentity = ObjectIdentity
healthESM = _HealthESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1)
)
if mibBuilder.loadTexts:
    healthESM.setStatus("current")


class _EsmCpu_Type(Unsigned32):
    """Custom type esmCpu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EsmCpu_Type.__name__ = "Unsigned32"
_EsmCpu_Object = MibScalar
esmCpu = _EsmCpu_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 1),
    _EsmCpu_Type()
)
esmCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmCpu.setStatus("current")
if mibBuilder.loadTexts:
    esmCpu.setUnits("percent")
_EsmRamTotal_Type = Unsigned32
_EsmRamTotal_Object = MibScalar
esmRamTotal = _EsmRamTotal_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 2),
    _EsmRamTotal_Type()
)
esmRamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmRamTotal.setStatus("current")
if mibBuilder.loadTexts:
    esmRamTotal.setUnits("megabytes")
_EsmRamFree_Type = Unsigned32
_EsmRamFree_Object = MibScalar
esmRamFree = _EsmRamFree_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 3),
    _EsmRamFree_Type()
)
esmRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmRamFree.setStatus("current")
if mibBuilder.loadTexts:
    esmRamFree.setUnits("megabytes")
_EsmDatabaseHDTotal_Type = Unsigned32
_EsmDatabaseHDTotal_Object = MibScalar
esmDatabaseHDTotal = _EsmDatabaseHDTotal_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 4),
    _EsmDatabaseHDTotal_Type()
)
esmDatabaseHDTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmDatabaseHDTotal.setStatus("current")
if mibBuilder.loadTexts:
    esmDatabaseHDTotal.setUnits("megabytes")
_EsmDatabaseHDFree_Type = Unsigned32
_EsmDatabaseHDFree_Object = MibScalar
esmDatabaseHDFree = _EsmDatabaseHDFree_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 5),
    _EsmDatabaseHDFree_Type()
)
esmDatabaseHDFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmDatabaseHDFree.setStatus("current")
if mibBuilder.loadTexts:
    esmDatabaseHDFree.setUnits("megabytes")
_EsmTime_Type = Unsigned32
_EsmTime_Object = MibScalar
esmTime = _EsmTime_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 6),
    _EsmTime_Type()
)
esmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmTime.setStatus("current")
if mibBuilder.loadTexts:
    esmTime.setUnits("seconds since 1970-1-1 00:00:0.0 (GMT)")
_EsmVersion_Type = OctetString
_EsmVersion_Object = MibScalar
esmVersion = _EsmVersion_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 7),
    _EsmVersion_Type()
)
esmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmVersion.setStatus("current")
_EsmMachineID_Type = OctetString
_EsmMachineID_Object = MibScalar
esmMachineID = _EsmMachineID_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 8),
    _EsmMachineID_Type()
)
esmMachineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmMachineID.setStatus("current")
_EsmModel_Type = OctetString
_EsmModel_Object = MibScalar
esmModel = _EsmModel_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 1, 9),
    _EsmModel_Type()
)
esmModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmModel.setStatus("current")
_HealthIPS_ObjectIdentity = ObjectIdentity
healthIPS = _HealthIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2)
)
if mibBuilder.loadTexts:
    healthIPS.setStatus("current")
_IpsName_Type = OctetString
_IpsName_Object = MibScalar
ipsName = _IpsName_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 1),
    _IpsName_Type()
)
ipsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsName.setStatus("current")
_IpsID_Type = OctetString
_IpsID_Object = MibScalar
ipsID = _IpsID_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 2),
    _IpsID_Type()
)
ipsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsID.setStatus("current")


class _IpsConnectionAvailable_Type(Unsigned32):
    """Custom type ipsConnectionAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IpsConnectionAvailable_Type.__name__ = "Unsigned32"
_IpsConnectionAvailable_Object = MibScalar
ipsConnectionAvailable = _IpsConnectionAvailable_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 3),
    _IpsConnectionAvailable_Type()
)
ipsConnectionAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsConnectionAvailable.setStatus("current")
_IpsStatus_Type = OctetString
_IpsStatus_Object = MibScalar
ipsStatus = _IpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 4),
    _IpsStatus_Type()
)
ipsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsStatus.setStatus("current")
_IpsBypassStatus_Type = OctetString
_IpsBypassStatus_Object = MibScalar
ipsBypassStatus = _IpsBypassStatus_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 5),
    _IpsBypassStatus_Type()
)
ipsBypassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsBypassStatus.setStatus("current")
_IpsMode_Type = OctetString
_IpsMode_Object = MibScalar
ipsMode = _IpsMode_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 6),
    _IpsMode_Type()
)
ipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsMode.setStatus("current")


class _IpsCpu_Type(Unsigned32):
    """Custom type ipsCpu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IpsCpu_Type.__name__ = "Unsigned32"
_IpsCpu_Object = MibScalar
ipsCpu = _IpsCpu_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 7),
    _IpsCpu_Type()
)
ipsCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCpu.setStatus("current")
if mibBuilder.loadTexts:
    ipsCpu.setUnits("percent")
_IpsRamTotal_Type = Unsigned32
_IpsRamTotal_Object = MibScalar
ipsRamTotal = _IpsRamTotal_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 8),
    _IpsRamTotal_Type()
)
ipsRamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsRamTotal.setStatus("current")
if mibBuilder.loadTexts:
    ipsRamTotal.setUnits("megabytes")
_IpsRamFree_Type = Unsigned32
_IpsRamFree_Object = MibScalar
ipsRamFree = _IpsRamFree_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 9),
    _IpsRamFree_Type()
)
ipsRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsRamFree.setStatus("current")
if mibBuilder.loadTexts:
    ipsRamFree.setUnits("megabytes")
_IpsDatabaseHDTotal_Type = Unsigned32
_IpsDatabaseHDTotal_Object = MibScalar
ipsDatabaseHDTotal = _IpsDatabaseHDTotal_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 10),
    _IpsDatabaseHDTotal_Type()
)
ipsDatabaseHDTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsDatabaseHDTotal.setStatus("current")
if mibBuilder.loadTexts:
    ipsDatabaseHDTotal.setUnits("megabytes")
_IpsDatabaseHDFree_Type = Unsigned32
_IpsDatabaseHDFree_Object = MibScalar
ipsDatabaseHDFree = _IpsDatabaseHDFree_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 11),
    _IpsDatabaseHDFree_Type()
)
ipsDatabaseHDFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsDatabaseHDFree.setStatus("current")
if mibBuilder.loadTexts:
    ipsDatabaseHDFree.setUnits("megabytes")
_IpsTime_Type = Unsigned32
_IpsTime_Object = MibScalar
ipsTime = _IpsTime_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 12),
    _IpsTime_Type()
)
ipsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsTime.setStatus("current")
if mibBuilder.loadTexts:
    ipsTime.setUnits("seconds since 1970-1-1 00:00:0.0 (GMT)")
_IpsVersion_Type = OctetString
_IpsVersion_Object = MibScalar
ipsVersion = _IpsVersion_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 13),
    _IpsVersion_Type()
)
ipsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsVersion.setStatus("current")
_IpsMachineID_Type = OctetString
_IpsMachineID_Object = MibScalar
ipsMachineID = _IpsMachineID_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 14),
    _IpsMachineID_Type()
)
ipsMachineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsMachineID.setStatus("current")
_IpsModel_Type = OctetString
_IpsModel_Object = MibScalar
ipsModel = _IpsModel_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 15),
    _IpsModel_Type()
)
ipsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsModel.setStatus("current")
_IpsAlertRate_Type = Unsigned32
_IpsAlertRate_Object = MibScalar
ipsAlertRate = _IpsAlertRate_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 16),
    _IpsAlertRate_Type()
)
ipsAlertRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAlertRate.setStatus("current")
if mibBuilder.loadTexts:
    ipsAlertRate.setUnits("alerts per minue")
_IpsFlowRate_Type = Unsigned32
_IpsFlowRate_Object = MibScalar
ipsFlowRate = _IpsFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 2, 17),
    _IpsFlowRate_Type()
)
ipsFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsFlowRate.setStatus("current")
if mibBuilder.loadTexts:
    ipsFlowRate.setUnits("flows per minue")
_HealthReceiver_ObjectIdentity = ObjectIdentity
healthReceiver = _HealthReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3)
)
if mibBuilder.loadTexts:
    healthReceiver.setStatus("current")
_ReceiverName_Type = OctetString
_ReceiverName_Object = MibScalar
receiverName = _ReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 1),
    _ReceiverName_Type()
)
receiverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverName.setStatus("current")
_ReceiverID_Type = OctetString
_ReceiverID_Object = MibScalar
receiverID = _ReceiverID_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 2),
    _ReceiverID_Type()
)
receiverID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverID.setStatus("current")


class _ReceiverConnectionAvailable_Type(Unsigned32):
    """Custom type receiverConnectionAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ReceiverConnectionAvailable_Type.__name__ = "Unsigned32"
_ReceiverConnectionAvailable_Object = MibScalar
receiverConnectionAvailable = _ReceiverConnectionAvailable_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 3),
    _ReceiverConnectionAvailable_Type()
)
receiverConnectionAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverConnectionAvailable.setStatus("current")
_ReceiverStatus_Type = OctetString
_ReceiverStatus_Object = MibScalar
receiverStatus = _ReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 4),
    _ReceiverStatus_Type()
)
receiverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverStatus.setStatus("current")


class _ReceiverCpu_Type(Unsigned32):
    """Custom type receiverCpu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ReceiverCpu_Type.__name__ = "Unsigned32"
_ReceiverCpu_Object = MibScalar
receiverCpu = _ReceiverCpu_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 5),
    _ReceiverCpu_Type()
)
receiverCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverCpu.setStatus("current")
if mibBuilder.loadTexts:
    receiverCpu.setUnits("percent")
_ReceiverRamTotal_Type = Unsigned32
_ReceiverRamTotal_Object = MibScalar
receiverRamTotal = _ReceiverRamTotal_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 6),
    _ReceiverRamTotal_Type()
)
receiverRamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverRamTotal.setStatus("current")
if mibBuilder.loadTexts:
    receiverRamTotal.setUnits("megabytes")
_ReceiverRamFree_Type = Unsigned32
_ReceiverRamFree_Object = MibScalar
receiverRamFree = _ReceiverRamFree_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 7),
    _ReceiverRamFree_Type()
)
receiverRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverRamFree.setStatus("current")
if mibBuilder.loadTexts:
    receiverRamFree.setUnits("megabytes")
_ReceiverDatabaseHDTotal_Type = Unsigned32
_ReceiverDatabaseHDTotal_Object = MibScalar
receiverDatabaseHDTotal = _ReceiverDatabaseHDTotal_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 8),
    _ReceiverDatabaseHDTotal_Type()
)
receiverDatabaseHDTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverDatabaseHDTotal.setStatus("current")
if mibBuilder.loadTexts:
    receiverDatabaseHDTotal.setUnits("megabytes")
_ReceiverDatabaseHDFree_Type = Unsigned32
_ReceiverDatabaseHDFree_Object = MibScalar
receiverDatabaseHDFree = _ReceiverDatabaseHDFree_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 9),
    _ReceiverDatabaseHDFree_Type()
)
receiverDatabaseHDFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverDatabaseHDFree.setStatus("current")
if mibBuilder.loadTexts:
    receiverDatabaseHDFree.setUnits("megabytes")
_ReceiverTime_Type = Unsigned32
_ReceiverTime_Object = MibScalar
receiverTime = _ReceiverTime_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 10),
    _ReceiverTime_Type()
)
receiverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverTime.setStatus("current")
if mibBuilder.loadTexts:
    receiverTime.setUnits("seconds since 1970-1-1 00:00:0.0 (GMT)")
_ReceiverVersion_Type = OctetString
_ReceiverVersion_Object = MibScalar
receiverVersion = _ReceiverVersion_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 11),
    _ReceiverVersion_Type()
)
receiverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverVersion.setStatus("current")
_ReceiverMachineID_Type = OctetString
_ReceiverMachineID_Object = MibScalar
receiverMachineID = _ReceiverMachineID_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 12),
    _ReceiverMachineID_Type()
)
receiverMachineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverMachineID.setStatus("current")
_ReceiverModel_Type = OctetString
_ReceiverModel_Object = MibScalar
receiverModel = _ReceiverModel_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 13),
    _ReceiverModel_Type()
)
receiverModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverModel.setStatus("current")
_ReceiverAlertRate_Type = Unsigned32
_ReceiverAlertRate_Object = MibScalar
receiverAlertRate = _ReceiverAlertRate_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 14),
    _ReceiverAlertRate_Type()
)
receiverAlertRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverAlertRate.setStatus("current")
if mibBuilder.loadTexts:
    receiverAlertRate.setUnits("alerts per minue")
_ReceiverFlowRate_Type = Integer32
_ReceiverFlowRate_Object = MibScalar
receiverFlowRate = _ReceiverFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 3, 3, 15),
    _ReceiverFlowRate_Type()
)
receiverFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverFlowRate.setStatus("current")
if mibBuilder.loadTexts:
    receiverFlowRate.setUnits("flows per minue")
_Blacklist_ObjectIdentity = ObjectIdentity
blacklist = _Blacklist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4)
)
if mibBuilder.loadTexts:
    blacklist.setStatus("current")
_BlacklistIPSName_Type = OctetString
_BlacklistIPSName_Object = MibScalar
blacklistIPSName = _BlacklistIPSName_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 1),
    _BlacklistIPSName_Type()
)
blacklistIPSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistIPSName.setStatus("current")
_BlacklistIPSID_Type = OctetString
_BlacklistIPSID_Object = MibScalar
blacklistIPSID = _BlacklistIPSID_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 2),
    _BlacklistIPSID_Type()
)
blacklistIPSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistIPSID.setStatus("current")
_BlacklistGroupName_Type = OctetString
_BlacklistGroupName_Object = MibScalar
blacklistGroupName = _BlacklistGroupName_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 3),
    _BlacklistGroupName_Type()
)
blacklistGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistGroupName.setStatus("current")


class _BlacklistType_Type(BlacklistTypes):
    """Custom type blacklistType based on BlacklistTypes"""
    defaultValue = 1


_BlacklistType_Type.__name__ = "BlacklistTypes"
_BlacklistType_Object = MibScalar
blacklistType = _BlacklistType_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 4),
    _BlacklistType_Type()
)
blacklistType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistType.setStatus("current")
_BlacklistIPAddress_Type = IpAddress
_BlacklistIPAddress_Object = MibScalar
blacklistIPAddress = _BlacklistIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 5),
    _BlacklistIPAddress_Type()
)
blacklistIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistIPAddress.setStatus("current")


class _BlacklistIPMask_Type(Unsigned32):
    """Custom type blacklistIPMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_BlacklistIPMask_Type.__name__ = "Unsigned32"
_BlacklistIPMask_Object = MibScalar
blacklistIPMask = _BlacklistIPMask_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 6),
    _BlacklistIPMask_Type()
)
blacklistIPMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistIPMask.setStatus("current")


class _BlacklistDestinationPort_Type(Unsigned32):
    """Custom type blacklistDestinationPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BlacklistDestinationPort_Type.__name__ = "Unsigned32"
_BlacklistDestinationPort_Object = MibScalar
blacklistDestinationPort = _BlacklistDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 7),
    _BlacklistDestinationPort_Type()
)
blacklistDestinationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistDestinationPort.setStatus("current")


class _BlacklistDuration_Type(Unsigned32):
    """Custom type blacklistDuration based on Unsigned32"""
    defaultValue = 0


_BlacklistDuration_Type.__name__ = "Unsigned32"
_BlacklistDuration_Object = MibScalar
blacklistDuration = _BlacklistDuration_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 8),
    _BlacklistDuration_Type()
)
blacklistDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistDuration.setStatus("current")
if mibBuilder.loadTexts:
    blacklistDuration.setUnits("seconds")


class _BlacklistAction_Type(BlacklistActions):
    """Custom type blacklistAction based on BlacklistActions"""
    defaultValue = 0


_BlacklistAction_Type.__name__ = "BlacklistActions"
_BlacklistAction_Object = MibScalar
blacklistAction = _BlacklistAction_Object(
    (1, 3, 6, 1, 4, 1, 23128, 1, 4, 9),
    _BlacklistAction_Type()
)
blacklistAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blacklistAction.setStatus("current")
_NitroConf_ObjectIdentity = ObjectIdentity
nitroConf = _NitroConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 3)
)
_NitroGroups_ObjectIdentity = ObjectIdentity
nitroGroups = _NitroGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 3, 1)
)
_NitroCompls_ObjectIdentity = ObjectIdentity
nitroCompls = _NitroCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23128, 3, 2)
)

# Managed Objects groups

nitroESMHealthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23128, 3, 1, 4)
)
nitroESMHealthGroup.setObjects(
      *(("NITROSECURITY-BASE-MIB", "esmCpu"),
        ("NITROSECURITY-BASE-MIB", "esmRamTotal"),
        ("NITROSECURITY-BASE-MIB", "esmRamFree"),
        ("NITROSECURITY-BASE-MIB", "esmDatabaseHDTotal"),
        ("NITROSECURITY-BASE-MIB", "esmDatabaseHDFree"),
        ("NITROSECURITY-BASE-MIB", "esmTime"),
        ("NITROSECURITY-BASE-MIB", "esmVersion"),
        ("NITROSECURITY-BASE-MIB", "esmMachineID"),
        ("NITROSECURITY-BASE-MIB", "esmModel"))
)
if mibBuilder.loadTexts:
    nitroESMHealthGroup.setStatus("current")

nitroIPSHealthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23128, 3, 1, 5)
)
nitroIPSHealthGroup.setObjects(
      *(("NITROSECURITY-BASE-MIB", "ipsName"),
        ("NITROSECURITY-BASE-MIB", "ipsID"),
        ("NITROSECURITY-BASE-MIB", "ipsConnectionAvailable"),
        ("NITROSECURITY-BASE-MIB", "ipsStatus"),
        ("NITROSECURITY-BASE-MIB", "ipsBypassStatus"),
        ("NITROSECURITY-BASE-MIB", "ipsMode"),
        ("NITROSECURITY-BASE-MIB", "ipsCpu"),
        ("NITROSECURITY-BASE-MIB", "ipsRamTotal"),
        ("NITROSECURITY-BASE-MIB", "ipsRamFree"),
        ("NITROSECURITY-BASE-MIB", "ipsDatabaseHDTotal"),
        ("NITROSECURITY-BASE-MIB", "ipsDatabaseHDFree"),
        ("NITROSECURITY-BASE-MIB", "ipsTime"),
        ("NITROSECURITY-BASE-MIB", "ipsVersion"),
        ("NITROSECURITY-BASE-MIB", "ipsMachineID"),
        ("NITROSECURITY-BASE-MIB", "ipsModel"),
        ("NITROSECURITY-BASE-MIB", "ipsAlertRate"),
        ("NITROSECURITY-BASE-MIB", "ipsFlowRate"))
)
if mibBuilder.loadTexts:
    nitroIPSHealthGroup.setStatus("current")

nitroReceiverHealthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23128, 3, 1, 6)
)
nitroReceiverHealthGroup.setObjects(
      *(("NITROSECURITY-BASE-MIB", "receiverName"),
        ("NITROSECURITY-BASE-MIB", "receiverID"),
        ("NITROSECURITY-BASE-MIB", "receiverConnectionAvailable"),
        ("NITROSECURITY-BASE-MIB", "receiverStatus"),
        ("NITROSECURITY-BASE-MIB", "receiverCpu"),
        ("NITROSECURITY-BASE-MIB", "receiverRamTotal"),
        ("NITROSECURITY-BASE-MIB", "receiverRamFree"),
        ("NITROSECURITY-BASE-MIB", "receiverDatabaseHDTotal"),
        ("NITROSECURITY-BASE-MIB", "receiverDatabaseHDFree"),
        ("NITROSECURITY-BASE-MIB", "receiverTime"),
        ("NITROSECURITY-BASE-MIB", "receiverVersion"),
        ("NITROSECURITY-BASE-MIB", "receiverMachineID"),
        ("NITROSECURITY-BASE-MIB", "receiverModel"),
        ("NITROSECURITY-BASE-MIB", "receiverAlertRate"),
        ("NITROSECURITY-BASE-MIB", "receiverFlowRate"))
)
if mibBuilder.loadTexts:
    nitroReceiverHealthGroup.setStatus("current")

nitroBlacklistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23128, 3, 1, 7)
)
nitroBlacklistGroup.setObjects(
      *(("NITROSECURITY-BASE-MIB", "blacklistIPSName"),
        ("NITROSECURITY-BASE-MIB", "blacklistIPSID"),
        ("NITROSECURITY-BASE-MIB", "blacklistGroupName"),
        ("NITROSECURITY-BASE-MIB", "blacklistType"),
        ("NITROSECURITY-BASE-MIB", "blacklistIPAddress"),
        ("NITROSECURITY-BASE-MIB", "blacklistIPMask"),
        ("NITROSECURITY-BASE-MIB", "blacklistDestinationPort"),
        ("NITROSECURITY-BASE-MIB", "blacklistDuration"),
        ("NITROSECURITY-BASE-MIB", "blacklistAction"))
)
if mibBuilder.loadTexts:
    nitroBlacklistGroup.setStatus("current")


# Notification objects

nitroBlacklistNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 23128, 0, 3)
)
nitroBlacklistNotify.setObjects(
      *(("NITROSECURITY-BASE-MIB", "blacklistIPSName"),
        ("NITROSECURITY-BASE-MIB", "blacklistIPSID"),
        ("NITROSECURITY-BASE-MIB", "blacklistGroupName"),
        ("NITROSECURITY-BASE-MIB", "blacklistType"),
        ("NITROSECURITY-BASE-MIB", "blacklistIPAddress"),
        ("NITROSECURITY-BASE-MIB", "blacklistIPMask"),
        ("NITROSECURITY-BASE-MIB", "blacklistDestinationPort"),
        ("NITROSECURITY-BASE-MIB", "blacklistDuration"),
        ("NITROSECURITY-BASE-MIB", "blacklistAction"))
)
if mibBuilder.loadTexts:
    nitroBlacklistNotify.setStatus(
        "current"
    )


# Notifications groups

nitroNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 23128, 3, 1, 8)
)
nitroNotifications.setObjects(
    ("NITROSECURITY-BASE-MIB", "nitroBlacklistNotify")
)
if mibBuilder.loadTexts:
    nitroNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NITROSECURITY-BASE-MIB",
    **{"BlacklistActions": BlacklistActions,
       "BlacklistTypes": BlacklistTypes,
       "nitroRegMIB": nitroRegMIB,
       "nitroEvents": nitroEvents,
       "nitroBlacklistNotify": nitroBlacklistNotify,
       "nitroObjects": nitroObjects,
       "health": health,
       "healthESM": healthESM,
       "esmCpu": esmCpu,
       "esmRamTotal": esmRamTotal,
       "esmRamFree": esmRamFree,
       "esmDatabaseHDTotal": esmDatabaseHDTotal,
       "esmDatabaseHDFree": esmDatabaseHDFree,
       "esmTime": esmTime,
       "esmVersion": esmVersion,
       "esmMachineID": esmMachineID,
       "esmModel": esmModel,
       "healthIPS": healthIPS,
       "ipsName": ipsName,
       "ipsID": ipsID,
       "ipsConnectionAvailable": ipsConnectionAvailable,
       "ipsStatus": ipsStatus,
       "ipsBypassStatus": ipsBypassStatus,
       "ipsMode": ipsMode,
       "ipsCpu": ipsCpu,
       "ipsRamTotal": ipsRamTotal,
       "ipsRamFree": ipsRamFree,
       "ipsDatabaseHDTotal": ipsDatabaseHDTotal,
       "ipsDatabaseHDFree": ipsDatabaseHDFree,
       "ipsTime": ipsTime,
       "ipsVersion": ipsVersion,
       "ipsMachineID": ipsMachineID,
       "ipsModel": ipsModel,
       "ipsAlertRate": ipsAlertRate,
       "ipsFlowRate": ipsFlowRate,
       "healthReceiver": healthReceiver,
       "receiverName": receiverName,
       "receiverID": receiverID,
       "receiverConnectionAvailable": receiverConnectionAvailable,
       "receiverStatus": receiverStatus,
       "receiverCpu": receiverCpu,
       "receiverRamTotal": receiverRamTotal,
       "receiverRamFree": receiverRamFree,
       "receiverDatabaseHDTotal": receiverDatabaseHDTotal,
       "receiverDatabaseHDFree": receiverDatabaseHDFree,
       "receiverTime": receiverTime,
       "receiverVersion": receiverVersion,
       "receiverMachineID": receiverMachineID,
       "receiverModel": receiverModel,
       "receiverAlertRate": receiverAlertRate,
       "receiverFlowRate": receiverFlowRate,
       "blacklist": blacklist,
       "blacklistIPSName": blacklistIPSName,
       "blacklistIPSID": blacklistIPSID,
       "blacklistGroupName": blacklistGroupName,
       "blacklistType": blacklistType,
       "blacklistIPAddress": blacklistIPAddress,
       "blacklistIPMask": blacklistIPMask,
       "blacklistDestinationPort": blacklistDestinationPort,
       "blacklistDuration": blacklistDuration,
       "blacklistAction": blacklistAction,
       "nitroConf": nitroConf,
       "nitroGroups": nitroGroups,
       "nitroESMHealthGroup": nitroESMHealthGroup,
       "nitroIPSHealthGroup": nitroIPSHealthGroup,
       "nitroReceiverHealthGroup": nitroReceiverHealthGroup,
       "nitroBlacklistGroup": nitroBlacklistGroup,
       "nitroNotifications": nitroNotifications,
       "nitroCompls": nitroCompls}
)
