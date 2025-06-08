# SNMP MIB module (AR-DOCREADER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arh_49796/AR-DOCREADER-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:29:24 2025
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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

arDocreaderMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 1972)
)
if mibBuilder.loadTexts:
    arDocreaderMib.setRevisions(
        ("2021-02-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Arh_ObjectIdentity = ObjectIdentity
arh = _Arh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796)
)
_DocumentReader_ObjectIdentity = ObjectIdentity
documentReader = _DocumentReader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796, 2)
)
_AgentVersion_Type = DisplayString
_AgentVersion_Object = MibScalar
agentVersion = _AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 1),
    _AgentVersion_Type()
)
agentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVersion.setStatus("current")


class _OperationalMode_Type(Integer32):
    """Custom type operationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eprus", 1),
          ("nisweb", 2),
          ("netAPI", 3))
    )


_OperationalMode_Type.__name__ = "Integer32"
_OperationalMode_Object = MibScalar
operationalMode = _OperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 2),
    _OperationalMode_Type()
)
operationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationalMode.setStatus("current")
_ReaderApplication_ObjectIdentity = ObjectIdentity
readerApplication = _ReaderApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796, 2, 3)
)
_Nisweb_ObjectIdentity = ObjectIdentity
nisweb = _Nisweb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796, 2, 3, 1)
)
_Eprus_ObjectIdentity = ObjectIdentity
eprus = _Eprus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796, 2, 3, 2)
)
_NetAPI_ObjectIdentity = ObjectIdentity
netAPI = _NetAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796, 2, 3, 3)
)
_NetworkConfig_ObjectIdentity = ObjectIdentity
networkConfig = _NetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4)
)
_LanConfigTable_Object = MibTable
lanConfigTable = _LanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lanConfigTable.setStatus("current")
_LanConfigEntry_Object = MibTableRow
lanConfigEntry = _LanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1)
)
lanConfigEntry.setIndexNames(
    (0, "AR-DOCREADER-MIB", "lanConfigHostName"),
)
if mibBuilder.loadTexts:
    lanConfigEntry.setStatus("current")
_LanConfigHostName_Type = DisplayString
_LanConfigHostName_Object = MibTableColumn
lanConfigHostName = _LanConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 1),
    _LanConfigHostName_Type()
)
lanConfigHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lanConfigHostName.setStatus("current")
_LanConfigDhcp_Type = Integer32
_LanConfigDhcp_Object = MibTableColumn
lanConfigDhcp = _LanConfigDhcp_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 2),
    _LanConfigDhcp_Type()
)
lanConfigDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigDhcp.setStatus("current")
_LanConfigTitleOfTheSite_Type = DisplayString
_LanConfigTitleOfTheSite_Object = MibTableColumn
lanConfigTitleOfTheSite = _LanConfigTitleOfTheSite_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 3),
    _LanConfigTitleOfTheSite_Type()
)
lanConfigTitleOfTheSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigTitleOfTheSite.setStatus("current")
_LanConfigIpv4address_Type = IpAddress
_LanConfigIpv4address_Object = MibTableColumn
lanConfigIpv4address = _LanConfigIpv4address_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 4),
    _LanConfigIpv4address_Type()
)
lanConfigIpv4address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv4address.setStatus("current")
_LanConfigIpv4netmask_Type = DisplayString
_LanConfigIpv4netmask_Object = MibTableColumn
lanConfigIpv4netmask = _LanConfigIpv4netmask_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 5),
    _LanConfigIpv4netmask_Type()
)
lanConfigIpv4netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv4netmask.setStatus("current")
_LanConfigIpv4gateway_Type = IpAddress
_LanConfigIpv4gateway_Object = MibTableColumn
lanConfigIpv4gateway = _LanConfigIpv4gateway_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 6),
    _LanConfigIpv4gateway_Type()
)
lanConfigIpv4gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv4gateway.setStatus("current")
_LanConfigIpv4dns1_Type = IpAddress
_LanConfigIpv4dns1_Object = MibTableColumn
lanConfigIpv4dns1 = _LanConfigIpv4dns1_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 7),
    _LanConfigIpv4dns1_Type()
)
lanConfigIpv4dns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv4dns1.setStatus("current")
_LanConfigIpv4dns2_Type = IpAddress
_LanConfigIpv4dns2_Object = MibTableColumn
lanConfigIpv4dns2 = _LanConfigIpv4dns2_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 8),
    _LanConfigIpv4dns2_Type()
)
lanConfigIpv4dns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv4dns2.setStatus("current")
_LanConfigIpv6address_Type = IpAddress
_LanConfigIpv6address_Object = MibTableColumn
lanConfigIpv6address = _LanConfigIpv6address_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 9),
    _LanConfigIpv6address_Type()
)
lanConfigIpv6address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv6address.setStatus("current")
_LanConfigIpv6gateway_Type = IpAddress
_LanConfigIpv6gateway_Object = MibTableColumn
lanConfigIpv6gateway = _LanConfigIpv6gateway_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 10),
    _LanConfigIpv6gateway_Type()
)
lanConfigIpv6gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv6gateway.setStatus("current")
_LanConfigIpv6dns1_Type = IpAddress
_LanConfigIpv6dns1_Object = MibTableColumn
lanConfigIpv6dns1 = _LanConfigIpv6dns1_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 11),
    _LanConfigIpv6dns1_Type()
)
lanConfigIpv6dns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv6dns1.setStatus("current")
_LanConfigIpv6dns2_Type = IpAddress
_LanConfigIpv6dns2_Object = MibTableColumn
lanConfigIpv6dns2 = _LanConfigIpv6dns2_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 1, 1, 12),
    _LanConfigIpv6dns2_Type()
)
lanConfigIpv6dns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIpv6dns2.setStatus("current")
_WifiConfigTable_Object = MibTable
wifiConfigTable = _WifiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2)
)
if mibBuilder.loadTexts:
    wifiConfigTable.setStatus("current")
_WifiConfigEntry_Object = MibTableRow
wifiConfigEntry = _WifiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1)
)
wifiConfigEntry.setIndexNames(
    (0, "AR-DOCREADER-MIB", "wifiConfigHostName"),
)
if mibBuilder.loadTexts:
    wifiConfigEntry.setStatus("current")
_WifiConfigHostName_Type = DisplayString
_WifiConfigHostName_Object = MibTableColumn
wifiConfigHostName = _WifiConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 1),
    _WifiConfigHostName_Type()
)
wifiConfigHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigHostName.setStatus("current")
_WifiConfigDhcp_Type = Integer32
_WifiConfigDhcp_Object = MibTableColumn
wifiConfigDhcp = _WifiConfigDhcp_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 2),
    _WifiConfigDhcp_Type()
)
wifiConfigDhcp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigDhcp.setStatus("current")
_WifiConfigIpv4address_Type = IpAddress
_WifiConfigIpv4address_Object = MibTableColumn
wifiConfigIpv4address = _WifiConfigIpv4address_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 4),
    _WifiConfigIpv4address_Type()
)
wifiConfigIpv4address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv4address.setStatus("current")
_WifiConfigIpv4netmask_Type = DisplayString
_WifiConfigIpv4netmask_Object = MibTableColumn
wifiConfigIpv4netmask = _WifiConfigIpv4netmask_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 5),
    _WifiConfigIpv4netmask_Type()
)
wifiConfigIpv4netmask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv4netmask.setStatus("current")
_WifiConfigIpv4gateway_Type = IpAddress
_WifiConfigIpv4gateway_Object = MibTableColumn
wifiConfigIpv4gateway = _WifiConfigIpv4gateway_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 6),
    _WifiConfigIpv4gateway_Type()
)
wifiConfigIpv4gateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv4gateway.setStatus("current")
_WifiConfigIpv4dns1_Type = IpAddress
_WifiConfigIpv4dns1_Object = MibTableColumn
wifiConfigIpv4dns1 = _WifiConfigIpv4dns1_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 7),
    _WifiConfigIpv4dns1_Type()
)
wifiConfigIpv4dns1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv4dns1.setStatus("current")
_WifiConfigIpv4dns2_Type = IpAddress
_WifiConfigIpv4dns2_Object = MibTableColumn
wifiConfigIpv4dns2 = _WifiConfigIpv4dns2_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 8),
    _WifiConfigIpv4dns2_Type()
)
wifiConfigIpv4dns2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv4dns2.setStatus("current")
_WifiConfigIpv6address_Type = IpAddress
_WifiConfigIpv6address_Object = MibTableColumn
wifiConfigIpv6address = _WifiConfigIpv6address_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 9),
    _WifiConfigIpv6address_Type()
)
wifiConfigIpv6address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv6address.setStatus("current")
_WifiConfigIpv6gateway_Type = IpAddress
_WifiConfigIpv6gateway_Object = MibTableColumn
wifiConfigIpv6gateway = _WifiConfigIpv6gateway_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 10),
    _WifiConfigIpv6gateway_Type()
)
wifiConfigIpv6gateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv6gateway.setStatus("current")
_WifiConfigIpv6dns1_Type = IpAddress
_WifiConfigIpv6dns1_Object = MibTableColumn
wifiConfigIpv6dns1 = _WifiConfigIpv6dns1_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 11),
    _WifiConfigIpv6dns1_Type()
)
wifiConfigIpv6dns1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv6dns1.setStatus("current")
_WifiConfigIpv6dns2_Type = IpAddress
_WifiConfigIpv6dns2_Object = MibTableColumn
wifiConfigIpv6dns2 = _WifiConfigIpv6dns2_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 4, 2, 1, 12),
    _WifiConfigIpv6dns2_Type()
)
wifiConfigIpv6dns2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wifiConfigIpv6dns2.setStatus("current")
_DateConfig_ObjectIdentity = ObjectIdentity
dateConfig = _DateConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49796, 2, 5)
)
_DateAndTimeConfigTable_Object = MibTable
dateAndTimeConfigTable = _DateAndTimeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 5, 1)
)
if mibBuilder.loadTexts:
    dateAndTimeConfigTable.setStatus("current")
_DateAndTimeConfigEntry_Object = MibTableRow
dateAndTimeConfigEntry = _DateAndTimeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 5, 1, 1)
)
dateAndTimeConfigEntry.setIndexNames(
    (0, "AR-DOCREADER-MIB", "dateAndTimeConfigHostName"),
)
if mibBuilder.loadTexts:
    dateAndTimeConfigEntry.setStatus("current")
_DateAndTimeConfigHostName_Type = DisplayString
_DateAndTimeConfigHostName_Object = MibTableColumn
dateAndTimeConfigHostName = _DateAndTimeConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 5, 1, 1, 1),
    _DateAndTimeConfigHostName_Type()
)
dateAndTimeConfigHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dateAndTimeConfigHostName.setStatus("current")
_DateAndTimeConfigDateTime_Type = DateAndTime
_DateAndTimeConfigDateTime_Object = MibTableColumn
dateAndTimeConfigDateTime = _DateAndTimeConfigDateTime_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 5, 1, 1, 2),
    _DateAndTimeConfigDateTime_Type()
)
dateAndTimeConfigDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateAndTimeConfigDateTime.setStatus("current")
_DateAndTimeConfigNtpServer_Type = DisplayString
_DateAndTimeConfigNtpServer_Object = MibTableColumn
dateAndTimeConfigNtpServer = _DateAndTimeConfigNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 49796, 2, 5, 1, 1, 3),
    _DateAndTimeConfigNtpServer_Type()
)
dateAndTimeConfigNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateAndTimeConfigNtpServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AR-DOCREADER-MIB",
    **{"arDocreaderMib": arDocreaderMib,
       "arh": arh,
       "documentReader": documentReader,
       "agentVersion": agentVersion,
       "operationalMode": operationalMode,
       "readerApplication": readerApplication,
       "nisweb": nisweb,
       "eprus": eprus,
       "netAPI": netAPI,
       "networkConfig": networkConfig,
       "lanConfigTable": lanConfigTable,
       "lanConfigEntry": lanConfigEntry,
       "lanConfigHostName": lanConfigHostName,
       "lanConfigDhcp": lanConfigDhcp,
       "lanConfigTitleOfTheSite": lanConfigTitleOfTheSite,
       "lanConfigIpv4address": lanConfigIpv4address,
       "lanConfigIpv4netmask": lanConfigIpv4netmask,
       "lanConfigIpv4gateway": lanConfigIpv4gateway,
       "lanConfigIpv4dns1": lanConfigIpv4dns1,
       "lanConfigIpv4dns2": lanConfigIpv4dns2,
       "lanConfigIpv6address": lanConfigIpv6address,
       "lanConfigIpv6gateway": lanConfigIpv6gateway,
       "lanConfigIpv6dns1": lanConfigIpv6dns1,
       "lanConfigIpv6dns2": lanConfigIpv6dns2,
       "wifiConfigTable": wifiConfigTable,
       "wifiConfigEntry": wifiConfigEntry,
       "wifiConfigHostName": wifiConfigHostName,
       "wifiConfigDhcp": wifiConfigDhcp,
       "wifiConfigIpv4address": wifiConfigIpv4address,
       "wifiConfigIpv4netmask": wifiConfigIpv4netmask,
       "wifiConfigIpv4gateway": wifiConfigIpv4gateway,
       "wifiConfigIpv4dns1": wifiConfigIpv4dns1,
       "wifiConfigIpv4dns2": wifiConfigIpv4dns2,
       "wifiConfigIpv6address": wifiConfigIpv6address,
       "wifiConfigIpv6gateway": wifiConfigIpv6gateway,
       "wifiConfigIpv6dns1": wifiConfigIpv6dns1,
       "wifiConfigIpv6dns2": wifiConfigIpv6dns2,
       "dateConfig": dateConfig,
       "dateAndTimeConfigTable": dateAndTimeConfigTable,
       "dateAndTimeConfigEntry": dateAndTimeConfigEntry,
       "dateAndTimeConfigHostName": dateAndTimeConfigHostName,
       "dateAndTimeConfigDateTime": dateAndTimeConfigDateTime,
       "dateAndTimeConfigNtpServer": dateAndTimeConfigNtpServer}
)
